# 🛠️ TOOLS - Herramientas y Utilidades

**Índice de herramientas de desarrollo, integración y mantenimiento**

---

## 📂 Estructura

```
TOOLS/
├── EXTRACTION/       Extractores de datos (conversaciones, código)
├── HELPERS/          Funciones auxiliares (metadatos, merge, etc.)
├── UTILITIES/        Herramientas especializadas
├── SERVERS/          Servidores auxiliares
├── SETUP/            Inicialización
├── DEV_TOOLS/        Herramientas de desarrollo
├── MODELS/           Modelos de IA (Ollama)
├── REVIEW/           Requieren verificación antes de usar
├── LEGACY/           Histórico y deprecated
└── README.md         (Este archivo)
```

---

## 🔧 SUBCARPETAS EN DETALLE

### **EXTRACTION/** — Extractores de Datos

Herramientas para convertir fuentes externas a envelopes NEUROBIT.

#### `extract_code_blocks.py`
```bash
python3 TOOLS/EXTRACTION/extract_code_blocks.py <archivo_entrada> <archivo_salida>
```
**Función**: Extrae bloques de código de documentos markdown o texto plano  
**Entrada**: Archivo con triple backticks (```)  
**Salida**: JSON con bloques identificados  

#### `extract_code_blocks_with_speakers.py`
```bash
python3 TOOLS/EXTRACTION/extract_code_blocks_with_speakers.py <archivo_entrada>
```
**Función**: Extrae bloques de código manteniendo quién habla (para diálogos)  
**Entrada**: Conversación con formato `[SPEAKER]: código`  
**Salida**: JSON con speaker_id + code_block  
**Caso**: Multi-agente conversations  

#### `extract_mhtml_conversation.py`
```bash
python3 TOOLS/EXTRACTION/extract_mhtml_conversation.py <archivo.mhtml> <salida.json>
```
**Función**: Extrae conversaciones de archivos MHTML (guardar página web)  
**Entrada**: Archivo .mhtml de una conversación (ChatGPT, Qwen, etc.)  
**Salida**: JSON estructurado con turnos de diálogo  
**Nota**: Integra con Centinela para captura automática  

---

### **HELPERS/** — Funciones Auxiliares

Pequeñas utilidades para preparación de datos.

#### `add_yaml_meta.py`
```bash
python3 TOOLS/HELPERS/add_yaml_meta.py \
  --input document.txt \
  --output document_with_meta.txt \
  --title "Mi Documento" \
  --author "Usuario" \
  --tags "neurobit,test"
```
**Función**: Agrega header YAML (metadatos) a archivos  
**Salida**: Archivo con metadata Frontmatter  

#### `merge_parts.py`
```bash
python3 TOOLS/HELPERS/merge_parts.py \
  --input-pattern "parte_*.txt" \
  --output merged.txt
```
**Función**: Fusiona fragmentos numerados en un archivo  
**Uso**: Reconstitución de archivos divididos por `MODULES/fragmentar.py`  

#### `compile_project.py`
```bash
python3 TOOLS/HELPERS/compile_project.py \
  --project /ruta/proyecto \
  --output compilado.txt
```
**Función**: Compila código fuente en un archivo único  
**Salida**: Archivo de texto con toda la fuente  
**Nota**: Considera Privacy/Copyright antes de usar  

---

### **UTILITIES/** — Herramientas Especializadas

#### `project_integrator.py` (antes: `modulo_integrador.py`)
```bash
python3 TOOLS/UTILITIES/project_integrator.py \
  --lista_archivos archivos.txt \
  --dir_busqueda /ruta/proyecto \
  --dir_destino /destino \
  --output_compilado salida.txt
```
**Función**: Orquestador que busca, localiza y compila archivos de proyecto  
**Capacidades**:
  - Búsqueda recursiva de archivos
  - Sugerencias si no encuentra exacto
  - Evita sobrescrituras (añade sufijo _N)
  - Manejo robusto de permisos

**Caso**: Auditoría y compilación de proyectos grandes  

#### `neurobit_pdf_splitter.py`
```bash
python3 TOOLS/UTILITIES/neurobit_pdf_splitter.py \
  --input documento.pdf \
  --output-dir pages/ \
  --pages-per-file 10
```
**Función**: Divide PDFs en partes manejables  
**Uso**: Preparación de documentos grandes para ingesta  

---

### **SERVERS/** — Servidores Auxiliares

#### `fragment_server.py`
```bash
python3 TOOLS/SERVERS/fragment_server.py &

# Cliente:
curl -X POST -H "Content-Type: application/json" \
  -d '{"text":"Mi texto largo...","max_length":5000}' \
  http://127.0.0.1:8001/fragment
```
**Función**: API REST para fragmentación de textos  
**Puerto**: 8001 (no interfiere con 5000 de neurobit_api.py)  
**Nota**: Versión simplificada, más ligera que la versión .old  

---

### **SETUP/** — Inicialización

#### `seed_memoria.py`
```bash
python3 TOOLS/SETUP/seed_memoria.py \
  --corpus corpus.txt \
  --output data/memoria_eva.jsonl
```
**Función**: Inicializa memoria_eva.jsonl con datos iniciales  
**Uso**: Setup de sesión nueva  

#### `neurobit_fix.sh`
```bash
bash TOOLS/SETUP/neurobit_fix.sh
```
**Función**: Script de reparación/reinicio  
**Acciones**: Limpia estado, reinicializa directorios clave  

---

### **DEV_TOOLS/** — Herramientas de Desarrollo

#### `descompilador_extension.py`
```bash
python3 TOOLS/DEV_TOOLS/descompilador_extension.py \
  --extension neurobit-message-builder.crx \
  --output extension_src/
```
**Función**: Extrae código de extensión Chrome (.crx)  
**Uso**: Análisis y debugging de extensiones  

---

### **MODELS/OLLAMA/** — Modelos de IA Local

```
MODELS/OLLAMA/
├── neurobit-light.modelfile
└── neurobit-strict.modelfile
```

**Uso con Ollama** (si lo tienes instalado):
```bash
# Crear modelo custom desde modelfile
ollama create neurobit-light -f TOOLS/MODELS/OLLAMA/neurobit-light.modelfile

# Ejecutar
ollama run neurobit-light
```

**Nota**: Requiere Ollama instalado. Ver https://ollama.ai

---

### **REVIEW/** — Requieren Verificación

#### `reconstruir_desde_especificacion.py`
```
⚠️  ESTADO: Requiere auditoría
```

**Propósito**: Similar a `core/adapters/adapter_rebuild_spec.py`  
**Acción requerida**: 
- [ ] Verificar si es más nueva versión
- [ ] Consolidar con existente
- [ ] Mover a LEGACY si es duplicado

---

### **LEGACY/** — Histórico y Deprecated

```
LEGACY/
├── fragment_server.py.old      (Versión compleja, usar simple)
├── GENERADOR_AUDIO_RESUMEN.py  (Experimental, sin usar)
├── modulos_sueltos.BACKUP/     (Backup de reorganización)
└── neurobit-gui.old/           (GUI 90% completa, abandonada)
```

**Regla**: No importar desde LEGACY sin motivo.  
**Referencia**: Consultar si necesitas código histórico.  

---

## 📖 FLUJO DE USO TÍPICO

### **Caso 1: Preparar conversación de navegador**

```bash
# 1. Guardar conversación de navegador como .mhtml
# (Right-click → Save as... → Web Page Complete)

# 2. Extraer estructura
python3 TOOLS/EXTRACTION/extract_mhtml_conversation.py \
  conversacion.mhtml output.json

# 3. Agregar metadatos
python3 TOOLS/HELPERS/add_yaml_meta.py \
  --input output.json \
  --author "Usuario" \
  --tags "sesion_001"

# 4. Enviar a NEUROBIT
curl -X POST -H "Content-Type: application/json" \
  -d @output.json \
  http://127.0.0.1:5000/analyze
```

---

### **Caso 2: Dividir documento grande**

```bash
# 1. Dividir en partes
python3 MODULES/fragmentar.py documento.txt 5000

# Genera: documento_1.txt, documento_2.txt, ...

# 2. Procesar cada parte
for part in documento_*.txt; do
  curl -X POST ... -d @$part http://127.0.0.1:5000/analyze
done

# 3. Reconstituciones (si necesario)
python3 TOOLS/HELPERS/merge_parts.py \
  --input-pattern "documento_*.txt" \
  --output reconstructed.txt
```

---

## ✅ CHECKLIST DE HERRAMIENTAS

| Herramienta | Carpeta | Estado | Usa frecuencia |
|------------|---------|--------|----------------|
| fragmentar | MODULES | ✅ Activo | Alta |
| extract_code_blocks | EXTRACTION | ✅ Activo | Media |
| extract_mhtml_conversation | EXTRACTION | ✅ Activo | Media |
| add_yaml_meta | HELPERS | ✅ Activo | Baja |
| merge_parts | HELPERS | ✅ Activo | Baja |
| project_integrator | UTILITIES | ✅ Activo | Baja |
| fragment_server | SERVERS | ✅ Activo | Media |
| seed_memoria | SETUP | ✅ Activo | Una vez |
| descompilador_extension | DEV_TOOLS | ✅ Activo | Rara |
| reconstruir_desde_especificacion | REVIEW | ⚠️ Revisar | No usar |

---

## 🚨 REGLAS IMPORTANTES

1. **Nunca edites LEGACY/** sin intención de documentar cambios
2. **Los extractores producen JSON**: Verifica formato antes de pasar a API
3. **REVIEW/** no debe usarse en producción: Requiere auditoría
4. **MODELS/** requiere Ollama instalado para funcionar
5. **Todos los scripts** deben ejecutarse desde raíz del proyecto

---

## 🔗 INTEGRACIÓN CON CORE

```
TOOLS/ → MODULES/ → core/coherence_filter.py
       → MODULES/ → core/agents_registry.py
       → EXTRACTION/ → core/centinela_monitor.py (entrada)
       → SERVERS/ → neurobit_api.py (endpoints auxiliares)
```

---

## 📞 AYUDA

Para cada herramienta:
```bash
python3 TOOLS/UTILITIES/tool_name.py --help
```

Para documentación detallada:
- `docs/QUE_HACE_CADA_CARPETA.md`
- `docs/INICIO_RAPIDO.md`

---

**Generado por**: Módulo de Validación Suprema NEUROBIT v2.1  
**Timestamp**: 17 enero 2026

