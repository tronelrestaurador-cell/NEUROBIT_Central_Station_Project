# Resumen técnico
Extensión Chrome MV3 funcional con protocolo de mensajería Neurobit. Se propone reestructurar para modularidad, añadir scripts de inicialización, configurar integración VSCode/LLM local y preparar sistema de persistencia extensible. Mantenemos la arquitectura existente pero mejoramos escalabilidad y mantenibilidad.

Al final del compendio, encontraras lo que el usuario pidio.

----------compendio

# Árbol de directorios propuesto
```
neurobit/
├── .vscode/
│   ├── settings.json
│   ├── tasks.json
│   └── extensions.json
├── core/
│   ├── protocol.js
│   ├── persistence.js
│   └── kernel.js
├── connectors/
│   ├── ollama.js
│   ├── browser.js
│   └── mcp_server.py
├── automations/
│   ├── init_workspace.sh
│   ├── backup_system.py
│   └── env_validator.sh
├── tests/
│   └── unit/
├── config/
│   └── neurobit_config.json
├── data/
│   └── memoria_eva.jsonl
└── src/
    ├── manifest.json
    ├── background.js
    ├── content/
    │   └── content.js
    └── popup/
        ├── popup.html
        ├── popup.js
        ├── storage.js
        ├── injector.js
        ├── ollama.js
        └── styles.css
```

# Código de ajustes

## 1. Configuración VSCode (.vscode/settings.json)
```json
{
  "files.autoSave": "onFocusChange",
  "editor.tabSize": 2,
  "editor.renderWhitespace": "all",
  "files.associations": {
    "*.md": "markdown",
    "*.jsonl": "json"
  },
  "javascript.updateImportsOnFileMove.enabled": "always",
  "workbench.colorTheme": "Default Dark Modern",
  "terminal.integrated.defaultProfile.linux": "bash",
  "copilot.enable": {
    "*": true,
    "plaintext": true,
    "markdown": true
  },
  "extensions.ignoreRecommendations": false
}
```

## 2. Script de inicialización (automations/init_workspace.sh)
```bash
#!/bin/bash
set -e

# NEUROBIT Workspace Initializer
# Ejecutar desde la raíz del proyecto: ./automations/init_workspace.sh

PROJECT_ROOT=$(pwd)
DATA_DIR="$PROJECT_ROOT/data"
CONFIG_DIR="$PROJECT_ROOT/config"

echo "🚀 Iniciando configuración del workspace NEUROBIT..."

# Crear directorios esenciales
mkdir -p "$DATA_DIR"
mkdir -p "$CONFIG_DIR"
mkdir -p "$PROJECT_ROOT/core"
mkdir -p "$PROJECT_ROOT/connectors"
mkdir -p "$PROJECT_ROOT/automations"
mkdir -p "$PROJECT_ROOT/tests/unit"
mkdir -p "$PROJECT_ROOT/.vscode"

# Inicializar memoria persistente
if [ ! -f "$DATA_DIR/memoria_eva.jsonl" ]; then
  echo "📦 Creando memoria_eva.jsonl..."
  touch "$DATA_DIR/memoria_eva.jsonl"
  chmod 600 "$DATA_DIR/memoria_eva.jsonl"
fi

# Configuración base
if [ ! -f "$CONFIG_DIR/neurobit_config.json" ]; then
  echo "⚙️ Generando configuración base..."
  cat > "$CONFIG_DIR/neurobit_config.json" <<EOF
{
  "version": "2.1",
  "environment": "development",
  "ollama": {
    "endpoint": "http://localhost:11434/api/generate",
    "model": "neurobit-strict:latest",
    "timeout": 30000
  },
  "persistence": {
    "arca_path": "./data/memoria_eva.jsonl",
    "journal_path": "./data/writing.record"
  },
  "nodes": ["HOMO_VIVO", "NEUROBIT_D", "ESTACION_CENTRAL", "S0PHI", "QW3N4"]
}
EOF
fi

# Validar dependencias
echo "🔍 Verificando dependencias del sistema..."
if ! command -v ollama &> /dev/null; then
  echo "⚠️  Ollama no está instalado. Se requiere para el funcionamiento completo."
  echo "   Instrucciones: https://ollama.com/download/linux"
else
  echo "✅ Ollama disponible"
fi

if ! command -v python3 &> /dev/null; then
  echo "⚠️  Python3 no encontrado. Se requiere para scripts de automatización."
else
  echo "✅ Python3 disponible"
fi

echo "✅ Workspace NEUROBIT inicializado correctamente"
echo "💡 Siguiente paso: Configurar tu modelo local con 'ollama pull neurobit-strict:latest'"
```

## 3. MCP Server para LLM local (connectors/mcp_server.py)
```python
#!/usr/bin/env python3
"""
Servidor MCP (Model Connection Protocol) para integración con LLMs locales
Permite a VSCode/CodeLLM comunicarse con el sistema NEUROBIT
"""

import json
import os
import sys
import time
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse, parse_qs

# Configuración base
PROJECT_ROOT = Path(__file__).parent.parent
CONFIG_PATH = PROJECT_ROOT / "config" / "neurobit_config.json"
DATA_DIR = PROJECT_ROOT / "data"
MEMORIA_PATH = DATA_DIR / "memoria_eva.jsonl"

# Cargar configuración
try:
    with open(CONFIG_PATH, "r") as f:
        config = json.load(f)
except FileNotFoundError:
    print(f"❌ Archivo de configuración no encontrado: {CONFIG_PATH}")
    sys.exit(1)

class MCPHandler(BaseHTTPRequestHandler):
    """Manejador de solicitudes para el servidor MCP"""
    
    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def do_OPTIONS(self):
        """Manejar solicitudes OPTIONS para CORS"""
        self._set_headers(204)
    
    def do_GET(self):
        """Manejar solicitudes GET"""
        parsed_path = urlparse(self.path)
        query = parse_qs(parsed_path.query)
        
        if parsed_path.path == '/read_arca':
            self._read_arca(query)
        elif parsed_path.path == '/status':
            self._get_status()
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Endpoint no encontrado"}).encode())
    
    def do_POST(self):
        """Manejar solicitudes POST"""
        parsed_path = urlparse(self.path)
        
        if parsed_path.path == '/write_arca':
            self._write_arca()
        elif parsed_path.path == '/validate_with_simon':
            self._validate_with_simon()
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Endpoint no encontrado"}).encode())
    
    def _read_arca(self, query):
        """Leer los últimos N registros de la memoria"""
        try:
            limit = int(query.get('limit', [5])[0])
            records = []
            
            if MEMORIA_PATH.exists():
                with open(MEMORIA_PATH, 'r') as f:
                    lines = f.readlines()
                    # Obtener los últimos N registros
                    for line in lines[-limit:]:
                        try:
                            records.append(json.loads(line.strip()))
                        except json.JSONDecodeError:
                            continue
            
            self._set_headers()
            self.wfile.write(json.dumps({
                "status": "success",
                "count": len(records),
                "records": records
            }).encode())
        except Exception as e:
            self._set_headers(500)
            self.wfile.write(json.dumps({
                "error": f"Error al leer el Arca: {str(e)}"
            }).encode())
    
    def _write_arca(self):
        """Escribir un nuevo registro en la memoria"""
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            # Validar datos mínimos
            required_fields = ['MESSAGE_ID', 'content']
            if not all(field in data for field in required_fields):
                self._set_headers(400)
                self.wfile.write(json.dumps({
                    "error": f"Campos requeridos: {', '.join(required_fields)}"
                }).encode())
                return
            
            # Preparar registro
            record = {
                "timestamp": datetime.now().isoformat(),
                "session": data.get("SESSION_TAG", "DEFAULT_SESSION"),
                "message_id": data["MESSAGE_ID"],
                "origin": data.get("ORIGEN", "HOMO_VIVO"),
                "destination": data.get("DESTINO", "ESTACION_CENTRAL"),
                "content": data["content"],
                "version": config.get("version", "2.1")
            }
            
            # Escribir en memoria (append-only)
            with open(MEMORIA_PATH, 'a') as f:
                f.write(json.dumps(record) + '\n')
            
            self._set_headers()
            self.wfile.write(json.dumps({
                "status": "success",
                "message": f"Registro {data['MESSAGE_ID']} guardado"
            }).encode())
        except Exception as e:
            self._set_headers(500)
            self.wfile.write(json.dumps({
                "error": f"Error al escribir en el Arca: {str(e)}"
            }).encode())
    
    def _validate_with_simon(self):
        """Validar contenido con reglas de coherencia SIMON"""
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            content = data.get("content", "")
            if not content:
                self._set_headers(400)
                self.wfile.write(json.dumps({
                    "error": "Contenido vacío para validar"
                }).encode())
                return
            
            # Reglas básicas de validación SIMON (extensible)
            is_valid = True
            reasons = []
            
            # Regla 1: Longitud mínima
            if len(content.strip()) < 10:
                is_valid = False
                reasons.append("contenido_demasiado_corto")
            
            # Regla 2: No permitir contenido repetitivo simple
            if len(set(content.split())) < 3 and len(content) > 20:
                is_valid = False
                reasons.append("contenido_repetitivo")
            
            # Regla 3: Verificar protocolo mínimo
            required_headers = ["MESSAGE_ID", "TIMESTAMP", "ORIGEN", "DESTINO"]
            missing_headers = [h for h in required_headers if h not in content]
            if missing_headers:
                is_valid = False
                reasons.append(f"headers_faltantes:{','.join(missing_headers)}")
            
            response = {
                "status": "success",
                "is_valid": is_valid,
                "validation_time": datetime.now().isoformat()
            }
            
            if not is_valid:
                response["reasons"] = reasons
            
            self._set_headers()
            self.wfile.write(json.dumps(response).encode())
        except Exception as e:
            self._set_headers(500)
            self.wfile.write(json.dumps({
                "error": f"Error en validación SIMON: {str(e)}"
            }).encode())
    
    def _get_status(self):
        """Obtener estado del sistema"""
        try:
            record_count = 0
            last_update = "Nunca"
            
            if MEMORIA_PATH.exists():
                record_count = sum(1 for _ in open(MEMORIA_PATH))
                last_update = datetime.fromtimestamp(
                    os.path.getmtime(MEMORIA_PATH)
                ).isoformat()
            
            status = {
                "status": "operativo",
                "version": config.get("version", "2.1"),
                "environment": config.get("environment", "unknown"),
                "memory_records": record_count,
                "last_update": last_update,
                "ollama_endpoint": config.get("ollama", {}).get("endpoint", "no_configurado"),
                "timestamp": datetime.now().isoformat()
            }
            
            self._set_headers()
            self.wfile.write(json.dumps(status).encode())
        except Exception as e:
            self._set_headers(500)
            self.wfile.write(json.dumps({
                "error": f"Error al obtener estado: {str(e)}"
            }).encode())

def run_server(port=8090):
    """Iniciar servidor MCP"""
    server_address = ('', port)
    httpd = HTTPServer(server_address, MCPHandler)
    print(f"🧠 Servidor MCP NEUROBIT activo en http://localhost:{port}")
    print(f"📦 Arca ubicada en: {MEMORIA_PATH}")
    print("⌨️  Presiona Ctrl+C para detener")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Apagando servidor MCP...")
        httpd.server_close()

if __name__ == "__main__":
    # Validar que existan los directorios necesarios
    if not DATA_DIR.exists():
        DATA_DIR.mkdir(parents=True)
        print(f"✅ Creado directorio de datos: {DATA_DIR}")
    
    if not MEMORIA_PATH.exists():
        MEMORIA_PATH.touch()
        print(f"✅ Creado archivo de memoria: {MEMORIA_PATH}")
    
    # Iniciar servidor
    run_server()
```

## 4. Script de respaldo (automations/backup_system.py)
```python
#!/usr/bin/env python3
"""
Sistema de respaldo para NEUROBIT
Crea copias de seguridad incrementales de la memoria y configuración
"""

import json
import os
import shutil
import sys
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
BACKUP_DIR = PROJECT_ROOT / "backups"
CONFIG_DIR = PROJECT_ROOT / "config"

def create_backup():
    """Crear una copia de seguridad del sistema"""
    # Crear directorio de backups si no existe
    BACKUP_DIR.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = BACKUP_DIR / f"neurobit_backup_{timestamp}"
    backup_path.mkdir()
    
    print(f"📦 Creando respaldo en: {backup_path}")
    
    # Copiar memoria
    memoria_src = DATA_DIR / "memoria_eva.jsonl"
    if memoria_src.exists():
        shutil.copy2(memoria_src, backup_path / "memoria_eva.jsonl")
        print(f"✅ Memoria respaldada ({os.path.getsize(memoria_src)} bytes)")
    else:
        print("⚠️  Memoria no encontrada, continuando...")
    
    # Copiar configuración
    config_src = CONFIG_DIR / "neurobit_config.json"
    if config_src.exists():
        shutil.copy2(config_src, backup_path / "neurobit_config.json")
        print(f"✅ Configuración respaldada")
    else:
        print("⚠️  Configuración no encontrada")
    
    # Crear metadatos del respaldo
    metadata = {
        "backup_time": datetime.now().isoformat(),
        "source_paths": {
            "memoria": str(memoria_src),
            "config": str(config_src)
        },
        "backup_version": "1.0"
    }
    
    with open(backup_path / "metadata.json", "w") as f:
        json.dump(metadata, f, indent=2)
    
    print(f"✅ Respaldo completado exitosamente")
    return backup_path

def list_backups():
    """Listar todos los respaldos disponibles"""
    if not BACKUP_DIR.exists():
        print("🔍 No se encontraron respaldos")
        return []
    
    backups = sorted(
        [d for d in BACKUP_DIR.iterdir() if d.is_dir()],
        key=lambda x: x.name,
        reverse=True
    )
    
    if not backups:
        print("🔍 No se encontraron respaldos")
        return []
    
    print(f"\n📋 Respaldo(s) disponibles ({len(backups)}):")
    for i, backup in enumerate(backups, 1):
        meta_path = backup / "metadata.json"
        timestamp = "Desconocido"
        size = 0
        
        if meta_path.exists():
            try:
                with open(meta_path, "r") as f:
                    meta = json.load(f)
                    timestamp = meta.get("backup_time", timestamp)
            except:
                pass
        
        memoria_path = backup / "memoria_eva.jsonl"
        if memoria_path.exists():
            size = os.path.getsize(memoria_path)
        
        print(f"{i}. {backup.name} | {timestamp.split('T')[0]} | {size//1024}KB")
    
    return backups

def restore_backup(backup_index=None):
    """Restaurar un respaldo específico"""
    backups = list_backups()
    if not backups:
        return
    
    if backup_index is None:
        try:
            backup_index = int(input("\nSelecciona número de respaldo a restaurar: ")) - 1
        except ValueError:
            print("❌ Entrada inválida")
            return
    
    if backup_index < 0 or backup_index >= len(backups):
        print("❌ Índice de respaldo inválido")
        return
    
    backup_path = backups[backup_index]
    print(f"\n🔄 Restaurando desde: {backup_path.name}")
    
    # Confirmación
    confirm = input("⚠️  ESTA ACCIÓN SOBREESCRIBIRÁ DATOS ACTUALES. ¿Continuar? (s/n): ")
    if confirm.lower() != 's':
        print("🚫 Restauración cancelada")
        return
    
    # Restaurar memoria
    memoria_backup = backup_path / "memoria_eva.jsonl"
    if memoria_backup.exists():
        shutil.copy2(memoria_backup, DATA_DIR / "memoria_eva.jsonl")
        print("✅ Memoria restaurada")
    
    # Restaurar configuración
    config_backup = backup_path / "neurobit_config.json"
    if config_backup.exists():
        shutil.copy2(config_backup, CONFIG_DIR / "neurobit_config.json")
        print("✅ Configuración restaurada")
    
    print("🎉 Restauración completada exitosamente")
    print("💡 Reinicia la extensión para que los cambios surtan efecto")

def main():
    """Función principal"""
    print("🧠 NEUROBIT - Sistema de Respaldo")
    print("=" * 40)
    
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "create" or command == "backup":
            create_backup()
        elif command == "list" or command == "ls":
            list_backups()
        elif command == "restore":
            index = int(sys.argv[2]) - 1 if len(sys.argv) > 2 else None
            restore_backup(index)
        else:
            print(f"❌ Comando desconocido: {command}")
            print("Uso: backup_system.py [create|list|restore]")
    else:
        print("Uso: backup_system.py [create|list|restore]")
        print("Ejemplos:")
        print("  python3 backup_system.py create")
        print("  python3 backup_system.py list")
        print("  python3 backup_system.py restore 1")

if __name__ == "__main__":
    main()
```

# Próximos pasos técnicos

1. Ejecutar `./automations/init_workspace.sh` para inicializar el entorno
2. Configurar VSCode con las extensiones recomendadas (ver `.vscode/extensions.json`)
3. Iniciar el servidor MCP: `python3 connectors/mcp_server.py`
4. Configurar modelo local: `ollama pull neurobit-strict:latest`
5. Validar integración ejecutando pruebas unitarias básicas en `tests/unit/`
6. Implementar protocolo de auditoría en `core/coherence_validator.js`

------------------ final del compendio

Lista consolidada de observaciones del beta-tester

(lo que el usuario realmente notó o pidió)

🟦 A. Estado y feedback al usuario (CRÍTICO)

El botón COPIAR funciona pero no lo parece

No hay feedback visual / cambio de estado.

El usuario duda si ocurrió la acción.

La línea de estado es útil y valorada

“Copiado al Arca actual” ✔

“NEUROBIT analizando…” gusta aunque sea simbólico.

👉 Necesidad clara:
feedback explícito, mínimo, inequívoco.

🟦 B. Persistencia y seguridad (MUY VALORADO)

La persistencia ante:

cierre del popup,

cambio de pestaña,

cierre del navegador
funciona y es celebrada.

El historial local / arca NO debe perderse nunca.

👉 Esto confirma que la decisión arquitectónica fue correcta.

🟦 C. Historial (UX problemática)

El historial:

no se puede expandir,

es incómodo para mensajes largos,

obliga a scrollear demasiado.

El usuario pide:

vista previa corta (5–7 líneas),

posibilidad de expandir / colapsar,

mantener historial como referencia, no editor.

👉 Esto es UX, no core lógico.

🟦 D. Secuencia y orden (ERROR FUNCIONAL)

El orden de mensajes en historial no es intuitivo

La secuencia aparece “al revés” para el flujo mental del usuario.

Guardar / Exportar:

el flujo no es claro,

el usuario no sabe qué ocurrió primero.

👉 Aquí hay confusión de flujo, no bug.

🟦 E. Autoguardado y conteo (IMPORTANTE)

Propuesta explícita del usuario:

autoguardado cada X mensajes,

ligado a contador,

sin intervención manual constante.

Quiere saber:

qué número de mensaje se copió,

qué ID quedó guardado.

👉 Esto apunta a trazabilidad, no estética.

🟦 F. Retención de estados del formulario

El formulario:

pierde ORIGEN / DESTINO,

pierde NODO / SESSION TAG.

El usuario pide:

checkbox / radial para retener estado,

autoincrement configurable,

posibilidad de sobrescribir manualmente.

👉 Esto es usabilidad técnica, no capricho.

🟦 G. Selección múltiple / operaciones en lote

Desea:

seleccionar varios mensajes del historial,

copiarlos/exportarlos juntos,

botón superior que obligue a revisar antes de exportar.

👉 Esto es una mejora, no imprescindible ahora.

🟦 H. Vista previa antes de inyectar (⭐ “frutillita del postre”)

Pedido explícito:

antes de inyectar al salón,

abrir ventana emergente de confirmación,

con el mismo CSS del preview,

desde ahí confirmar → inyectar + click real.

👉 No es comodidad: es trazabilidad fiel.
