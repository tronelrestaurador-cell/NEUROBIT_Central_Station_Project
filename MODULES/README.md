# 📦 MODULES - Módulos Activos Integrados

**Colección de módulos listos para usar e integrados con NEUROBIT**

---

## 📂 Contenido

```
MODULES/
├── fragmentar.py          División inteligente de textos
├── BUSCADOR_EVA.py        Full-text search en memoria
├── centinela.py           (DEPRECATED - usar core/centinela_monitor.py)
└── README.md              (Este archivo)
```

---

## 🔧 MÓDULOS DISPONIBLES

### **1. fragmentar.py** ⭐ Core

```python
from MODULES.fragmentar import dividir_archivo

# Dividir archivo de texto
dividir_archivo(
    archivo_entrada="documento.txt",
    longitud_maxima=20000,  # Caracteres
    nombre_archivo_salida="fragmento"
)

# Genera: fragmento_1.txt, fragmento_2.txt, etc.
```

**Función**: Divide textos largos en fragmentos sin romper párrafos  
**Inteligencia**: Respeta límites de párrafos para coherencia  
**Entrada**: Cualquier archivo de texto (.txt, .md, .csv, etc.)  
**Salida**: Múltiples archivos numerados  

**Parámetros**:
- `archivo_entrada`: Ruta del archivo
- `longitud_maxima`: Máximo carácter por fragmento (default: 20000)
- `nombre_archivo_salida`: Prefijo para archivos generados

**Caso de uso**: Dividir mensajes largos para API (que tiene límites)  

**Ejemplo**:
```bash
# Dividir un libro en fragmentos de 10KB
python3 -c "
from MODULES.fragmentar import dividir_archivo
dividir_archivo('libro.txt', 10000, 'libro_parte')
"
```

---

### **2. BUSCADOR_EVA.py** 🔍 Full-Text Search

```python
from MODULES.BUSCADOR_EVA import buscar_memoria

# Buscar en memoria
resultados = buscar_memoria(
    query="matriz 13x13",
    limite=10,
    archivo="data/memoria_eva.jsonl"
)

for msg in resultados:
    print(f"[{msg['MESSAGE_ID']}] {msg['content'][:100]}")
```

**Función**: Full-text search en memoria_eva.jsonl  
**Tecnología**: Búsqueda de palabras clave (case-insensitive)  
**Entrada**: String de búsqueda  
**Salida**: Lista de envelopes que contienen la palabra  

**Parámetros**:
- `query`: Texto a buscar
- `limite`: Máximo de resultados (default: 50)
- `archivo`: Path a memoria_eva.jsonl

**Caso de uso**: Encontrar mensajes anteriores, investigación histórica  

**Ejemplo**:
```bash
python3 -c "
from MODULES.BUSCADOR_EVA import buscar_memoria

# Buscar por tema
resultados = buscar_memoria('soberanía técnica', limite=5)
print(f'Encontrados: {len(resultados)} messages')

# Ver contenido
for r in resultados:
    print(f'- {r.get(\"TIMESTAMP\")}: {r.get(\"content\")[:80]}')
"
```

**Integración API** (próximamente):
```bash
curl "http://127.0.0.1:5000/buscar_memoria?q=matriz" | jq .
```

---

### **3. centinela.py** ⚠️ DEPRECATED

**No usar.** Migrado a `core/centinela_monitor.py` con mejoras:
- Integración con JSONL
- Endpoints en API
- Better error handling

**Alternativa**:
```bash
python3 core/centinela_monitor.py --start
```

---

## 🚀 IMPORTACIÓN Y USO

### **En scripts Python**

```python
# Opción 1: Importación directa
from MODULES.fragmentar import dividir_archivo
fragmentos = dividir_archivo("texto.txt", 5000)

# Opción 2: Importación de módulo
import sys
sys.path.insert(0, "MODULES")
import fragmentar
fragmentar.dividir_archivo(...)
```

### **En línea de comando**

```bash
# Navega al directorio raíz del proyecto
cd /home/oxo-nuxun-80-08-unxnu-oxo/neurobit_salon_v0.1

# Ejecuta módulo con Python
python3 -c "from MODULES.fragmentar import dividir_archivo; ..."
```

### **En neurobit_api.py** (Próxima integración)

Los módulos estarán disponibles como endpoints:

```bash
# Fragmentar texto
curl -X POST -H "Content-Type: application/json" \
  -d '{"text":"Mi texto largo...","max_length":5000}' \
  http://127.0.0.1:5000/fragment

# Buscar
curl "http://127.0.0.1:5000/buscar?q=matriz" | jq .
```

---

## 📚 DOCUMENTACIÓN DE CADA MÓDULO

### **fragmentar.py**

**Ubicación**: `MODULES/fragmentar.py`  
**Líneas**: ~100  
**Dependencias**: None (stdlib only)  
**Versión**: 1.0  

**Interfaz**:
```python
def dividir_archivo(
    archivo_entrada: str,
    longitud_maxima: int = 20000,
    nombre_archivo_salida: str = None
) -> list[str]
```

**Retorna**: Lista de rutas de archivos creados

**Ejemplo completo**:
```python
from MODULES.fragmentar import dividir_archivo
import os

archivo = "mi_conversacion.txt"
if os.path.exists(archivo):
    archivos_salida = dividir_archivo(
        archivo_entrada=archivo,
        longitud_maxima=15000,
        nombre_archivo_salida="conversacion_parte"
    )
    print(f"Generados {len(archivos_salida)} fragmentos:")
    for f in archivos_salida:
        tamaño = os.path.getsize(f)
        print(f"  - {f} ({tamaño} bytes)")
```

---

### **BUSCADOR_EVA.py**

**Ubicación**: `MODULES/BUSCADOR_EVA.py`  
**Líneas**: ~150  
**Dependencias**: json (stdlib)  
**Versión**: 1.0  

**Interfaz**:
```python
def buscar_memoria(
    query: str,
    limite: int = 50,
    archivo: str = "data/memoria_eva.jsonl"
) -> list[dict]
```

**Retorna**: Lista de envelopes que contienen la palabra clave

**Ejemplo completo**:
```python
from MODULES.BUSCADOR_EVA import buscar_memoria
import json

# Búsqueda
resultados = buscar_memoria("arquitectura", limite=10)

# Procesar resultados
for msg in resultados:
    print("="*50)
    print(f"ID: {msg.get('MESSAGE_ID')}")
    print(f"Timestamp: {msg.get('TIMESTAMP')}")
    print(f"Contenido: {msg.get('content')}")
    print(f"Coherencia: {msg.get('coherence', {}).get('score', 'N/A')}")

# Exportar a JSON
with open("resultados_busqueda.json", "w") as f:
    json.dump(resultados, f, indent=2, ensure_ascii=False)
```

---

## 🔗 INTEGRACIÓN CON CORE

Estos módulos se invocan desde:

1. **neurobit_api.py** (endpoints)
2. **core/coherence_filter.py** (análisis)
3. **core/agents_registry.py** (gestión)
4. Scripts standalone o herramientas externas

---

## 🎯 CASOS DE USO

### **Caso 1: Procesar documento grande**

```bash
# Documento de 500KB → dividir en 20KB fragmentos
python3 << 'EOF'
from MODULES.fragmentar import dividir_archivo

parts = dividir_archivo("tesis.pdf.txt", 20000, "tesis_parte")
print(f"✓ Dividido en {len(parts)} partes")

# Enviar cada parte a NEUROBIT
import subprocess
import json
for part in parts:
    with open(part) as f:
        contenido = f.read()
    payload = {"content": contenido}
    resultado = subprocess.run(
        ["curl", "-X", "POST", "-H", "Content-Type: application/json",
         "-d", json.dumps(payload), "http://127.0.0.1:5000/analyze"],
        capture_output=True, text=True
    )
    print(f"  {part}: enviado")
EOF
```

---

### **Caso 2: Recuperar conversación histórica**

```python
from MODULES.BUSCADOR_EVA import buscar_memoria
import json

# Buscar todas las menciones de "Matriz"
resultados = buscar_memoria("Matriz 13×13", limite=100)

# Agrupar por fecha
por_fecha = {}
for msg in resultados:
    fecha = msg['TIMESTAMP'][:10]
    if fecha not in por_fecha:
        por_fecha[fecha] = []
    por_fecha[fecha].append(msg)

# Mostrar resumen
for fecha in sorted(por_fecha.keys()):
    msgs = por_fecha[fecha]
    print(f"{fecha}: {len(msgs)} mensajes sobre Matriz")

# Guardar para análisis
with open("matriz_timeline.json", "w") as f:
    json.dump(por_fecha, f, indent=2, ensure_ascii=False)
```

---

## ✅ CHECKLIST DE INTEGRACIÓN

- [ ] ¿Importas `fragmentar` sin errores?
- [ ] ¿Memoria_eva.jsonl existe antes de usar `BUSCADOR_EVA`?
- [ ] ¿Puedes generar fragmentos exitosamente?
- [ ] ¿Las búsquedas retornan resultados?
- [ ] ¿Los módulos están actualizados en ARCHIVE/modulos_sueltos.BACKUP?

---

## 🚨 NOTAS IMPORTANTES

1. **fragmentar.py** respeta párrafos: no corta a mitad de línea
2. **BUSCADOR_EVA.py** es case-insensitive
3. Ambos son **pure Python**: sin dependencias externas
4. **Performance**: BUSCADOR_EVA es secuencial (O(n)). Documentos >100MB pueden ser lentos
5. **Encoding**: Asume UTF-8 para archivos

---

## 📚 VER TAMBIÉN

- `docs/INICIO_RAPIDO.md` — Uso en producción
- `docs/QUE_HACE_CADA_CARPETA.md` — Arquitectura general
- `TOOLS/README.md` — Otras herramientas disponibles
- `MODULES_PENDING/` — Módulos en evaluación

---

**Generado por**: Módulo de Validación Suprema NEUROBIT v2.1  
**Timestamp**: 17 enero 2026

