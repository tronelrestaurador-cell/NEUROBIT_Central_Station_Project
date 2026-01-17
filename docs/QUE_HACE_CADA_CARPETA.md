# 📖 QUÉ HACE CADA CARPETA - Mapa Maestro del Proyecto

**Generado**: 17 enero 2026  
**Versión**: 2.0 Post-Reorganización  
**Propósito**: Guía clara de la estructura y propósito de cada carpeta

---

## 🎯 ESTRUCTURA DE CARPETAS

### **Tier 0: NÚCLEO OPERATIVO** (Lo que ejecutas)

#### `CORE/` — Lógica Principal del Proyecto
```
core/
├── init_ceremony.py          ⭐ Inicializador - ejecutar primero
├── centinela_monitor.py      ⭐ Monitor de clipboard local
├── agents_registry.py         Registro de agentes multi-plataforma
├── m_e_scoring.py             Análisis Moralidad/Emoción
├── coherence_filter.py        Filtro de coherencia textual
├── message_validator.py       Validación de envelopes NEUROBIT
├── round_manager.py           Orquestación de rondas colaborativas
├── context_declare.py         Contexto y metadatos
└── adapters/                  Adaptadores especializados
    └── adapter_rebuild_spec.py → PASO 1 (ya implementado)
```

**Responsabilidad**: Todo lo que hace el proyecto andar  
**Entrada**: JSON envelopes con `content` + metadatos  
**Salida**: Envelopes enriquecidos + persistencia en JSONL  
**Interacción**: Llamado desde neurobit_api.py o directamente  

**CÓMO USAR**:
```bash
# 1. Inicializar el sistema
python3 core/init_ceremony.py

# 2. Iniciar monitoreo de clipboard (background)
python3 core/centinela_monitor.py --start

# 3. Ver estado
python3 core/centinela_monitor.py --status

# 4. Parar monitoreo
python3 core/centinela_monitor.py --stop
```

---

#### `INTERFACE/` — Interfaces de Usuario
```
interface/
├── station_progresivo.html    GUI principal (Estación Central)
├── station_progresivo.js      Orquestador de interfaz
├── arquetipos.js              Matriz 13×13 + encoding/decoding
├── matriz_ui.js               Visualización interactiva de matriz
├── agents_management.js       Panel de gestión multi-agente
├── minimal_ui.html            UI alternativa simple
├── style.css                  Estilos compartidos
└── ...
```

**Responsabilidad**: Todo lo visual/interactivo  
**Tecnología**: HTML5 + Vanilla JavaScript (cero dependencias externas)  
**Ubicación**: Servido por `neurobit_api.py` en `/interface/`  
**Propósito**: Visualizar matriz, gestionar agentes, monitorear rondas  

**CÓMO USAR**:
```bash
# 1. Levantar API
python3 neurobit_api.py

# 2. Abrir navegador
http://127.0.0.1:5000/interface/station_progresivo.html
```

---

#### `CONFIG/` — Configuración y Glosario
```
config/
├── memoria_sagrada_eva.yaml   Diccionario de términos + config
├── protocol_contract_v0.1.json Especificación de envelopes
└── ...
```

**Responsabilidad**: Configuración centralizada  
**No tocar**: Estructura YAML debe mantenerse para coherencia  
**Referencia**: Consultado por core/ e init_ceremony.py  

---

#### `DATA/` — Persistencia Append-Only
```
data/
├── memoria_eva.jsonl           Histórico completo de mensajes (CRÍTICO)
├── agents_registry.jsonl       Registro de agentes activos
├── centinela_resguardo.jsonl   Logs del monitor de clipboard
├── .centinela_state            Estado del Centinela
└── backups/                    (si existen)
```

**Responsabilidad**: Persistencia única fuente de verdad  
**REGLA ORO**: Append-only, nunca sobrescribir, una línea JSON por entrada  
**Tamaño típico**: memoria_eva.jsonl crece ~100KB por sesión  
**Cuidado**: No eliminar archivos .jsonl sin backup previo  

---

### **Tier 1: MÓDULOS INTELIGENTES** (Extensiones activas)

#### `MODULES/` — Módulos Activos y Funcionales
```
MODULES/
├── fragmentar.py             División inteligente de textos
├── BUSCADOR_EVA.py          Full-text search en memoria JSONL
├── centinela.py             (DEPRECATED - Ver core/centinela_monitor.py)
└── README.md                Documentación de uso
```

**Responsabilidad**: Funcionalidad reutilizable  
**Importación**: `from MODULES import fragmentar`  
**Disponibilidad**: Listos para usar en integración o scripts  
**Integración**: Algunos exponen endpoints en API (ver FASE 3.2)  

---

#### `MODULES_PENDING/` — En Evaluación o Integración
```
MODULES_PENDING/
├── compendio_inteligente_v23.py    (PASO 3 - Generador de compendios)
├── reconstruir_proyecto_desde_compendio.py  (PASO 2 - Reconstrucción)
└── README.md                         Status de integración
```

**Responsabilidad**: Módulos que aún no están integrados  
**Estado**: Funcionales pero requieren:
  - Testing adicional
  - Documentación mejorada
  - Integración con core/
  - Posibles refactores

**Timeline**: PASO 2 y PASO 3 de la hoja de ruta  

---

### **Tier 2: HERRAMIENTAS DE DESARROLLO** (Scripts y utilidades)

#### `TOOLS/EXTRACTION/` — Extractores de Datos
```
TOOLS/EXTRACTION/
├── extract_code_blocks.py               Extrae bloques de código
├── extract_code_blocks_with_speakers.py Extrae con identificación
├── extract_mhtml_conversation.py        Extrae de archivos MHTML (web)
└── README.md
```

**Uso**: Preparación de datos para ingesta  
**Caso**: Convertir conversaciones de navegador → Envelopes  

---

#### `TOOLS/HELPERS/` — Funciones Auxiliares
```
TOOLS/HELPERS/
├── add_yaml_meta.py              Agrega metadatos YAML
├── merge_parts.py                Fusiona fragmentos
├── compile_project.py            Compilación de proyecto
└── README.md
```

**Uso**: Tareas de mantenimiento y preparación  

---

#### `TOOLS/UTILITIES/` — Herramientas Especializadas
```
TOOLS/UTILITIES/
├── project_integrator.py         Orquestador de compilación (antes: modulo_integrador)
├── neurobit_pdf_splitter.py      Division de PDFs
└── README.md
```

**Caso de uso**: Preparación de documentos grandes para ingesta  

---

#### `TOOLS/SERVERS/` — Servidores Auxiliares
```
TOOLS/SERVERS/
└── fragment_server.py            API REST para fragmentación (versión simple)
```

**Nota**: `fragment_server.py.old` está en TOOLS/LEGACY/  

---

#### `TOOLS/SETUP/` — Inicialización
```
TOOLS/SETUP/
├── seed_memoria.py               Inicializa memoria_eva.jsonl
└── neurobit_fix.sh               Script de reparación
```

**Uso**: Setup inicial del proyecto  

---

#### `TOOLS/DEV_TOOLS/` — Herramientas de Desarrollo
```
TOOLS/DEV_TOOLS/
└── descompilador_extension.py    Descompila extensiones browser
```

---

#### `TOOLS/REVIEW/` — Verificación Requerida
```
TOOLS/REVIEW/
├── reconstruir_desde_especificacion.py  ⚠️ Verificar vs rebuild_from_spec
└── README.md
```

**Acción requerida**: Auditar duplicación antes de usar  

---

#### `TOOLS/LEGACY/` — Histórico y Deprecated
```
TOOLS/LEGACY/
├── fragment_server.py.old        (versión compleja - usar simple)
├── GENERADOR_AUDIO_RESUMEN.py   (experimental)
├── neurobit_fix.sh              (consolidado)
└── README.md
```

---

#### `TOOLS/MODELS/OLLAMA/` — Modelos de IA
```
TOOLS/MODELS/OLLAMA/
├── neurobit-light.modelfile     Modelo ligero
└── neurobit-strict.modelfile    Modelo con validación estricta
```

**Uso**: Para integración con Ollama (local LLM)  

---

### **Tier 3: DATOS Y REFERENCIAS** (Archivos grandes)

#### `STORAGE/` — Almacenamiento de Procesos
```
STORAGE/
├── RING_PROCESOS/               Fragmentos de trabajo, conversaciones
├── RING_REGISTRO/               Registros y handoffs
├── modules/                     Módulos dinámicos cargables
└── LEGACY/                      Archivos históricos
```

**Responsabilidad**: Datos transitorios de sesiones  
**Tamaño**: ~121MB  

---

#### `INPUT_TEXTS/` — Corpus de Entrada
```
INPUT_TEXTS/
├── ARCHIVOS/                    Carpeta contenedora
│   ├── RONDAS/                  Transcritos de sesiones
│   ├── FRAGMENTOS/              Partes numeradas
│   ├── SESIONES/                Archivos YAML de sesión
│   └── LEGACY/                  Archivos antiguos renombrados
└── ...
```

**Tamaño**: 1.3GB (62% del proyecto)  
**Responsabilidad**: Corpus histórico de entrada  
**Nota**: Considerar mover a ARCHIVE si es histórico  

---

#### `DATA/` — Persistencia Activa
```
DATA/
├── memoria_eva.jsonl            ⭐ CRÍTICO - Append-only log
├── agents_registry.jsonl        Registro activo de agentes
├── centinela_resguardo.jsonl    Logs del monitor
└── backups/                     Respaldos
```

**Responsabilidad**: Estado actual del proyecto  
**Backup recomendado**: Antes de cambios importantes  

---

### **Tier 4: ARCHIVOS Y ESPECIALES** (Referencia)

#### `EXTENSIONS/` — Extensiones de Navegador
```
EXTENSIONS/
├── neurobit-message-builder/    Chrome MV3 extension
└── bitacora-eva/                Extension de captura
```

**Estado**: Integración en progreso con NEUROBIT v2.1  

---

#### `ARCHIVE/` — Histórico y Backups
```
ARCHIVE/
├── neurobit-gui.old/            GUI 90% completa, abandonada
├── modulos_sueltos.BACKUP/      Backup original de reorganización
├── fragment_server.py.old       Versión anterior
├── abandoned/                   Experimentos descontinuados
└── README.md
```

**Responsabilidad**: Preservar código valioso pero no activo  
**Acceso**: Consultar si se necesita referencia histórica  

---

#### `DOCS/` — Documentación
```
DOCS/
├── AUDITORIA_MAESTRO_COMPLETO.md         Análisis completo del proyecto
├── INVENTARIO_MODULOS_TOOLS.md           Clasificación de 23+ módulos
├── CLASIFICACION_FINAL_MODULOS.md        Decisiones de integración
├── QUE_HACE_CADA_CARPETA.md             ⭐ ESTE ARCHIVO
├── INICIO_RAPIDO.md                     Guía de primer paso
├── ESPECIFICACION_MATRIZ_13x13.md        Matriz 13×13 ejecutable
├── FASE_*.md                            Documentación de fases
└── ...
```

**Responsabilidad**: Guías, análisis, especificaciones  
**Actualización**: Cada vez que cambia arquitectura  

---

### **Root Level** — Archivos Principales

#### Archivos Clave
```
neurobit_api.py                 ⭐ API REST principal (Flask)
setup_neurobit.sh               Setup inicial del proyecto
README FIRST                    Entrada rápida al proyecto
README.md                       Documentación general
SALA_SESION_001.yaml           Configuración de sesión inicial

.github/
├── copilot-instructions.md    Instrucciones para agentes LLM
└── workflows/                 CI/CD (si aplica)

.git/                           Control de versiones
.venv/                          Virtual environment Python
logs/                           Logs de ejecución
inbox/, outbox/, messages/      Colas de mensajes
```

---

## 🚀 FLUJO DE TRABAJO TÍPICO

### **Inicio de sesión**
```bash
# 1. Inicializar sistema
python3 core/init_ceremony.py

# 2. Levantar API
python3 neurobit_api.py &

# 3. Abrir interfaz
http://127.0.0.1:5000/interface/station_progresivo.html

# 4. (Opcional) Iniciar monitoreo de clipboard
curl -X POST http://127.0.0.1:5000/start_centinela
```

### **Enviar mensaje**
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"content":"Mi mensaje"}' \
  http://127.0.0.1:5000/analyze
```

### **Ver memoria**
```bash
# Últimas 10 líneas
tail -10 data/memoria_eva.jsonl | jq .

# Ver estado de agentes
curl http://127.0.0.1:5000/list_agents | jq .
```

---

## 📋 CHECKLIST DE OPERACIÓN

- [ ] ¿core/init_ceremony.py ejecutado?
- [ ] ¿neurobit_api.py levantado?
- [ ] ¿MEMORIA_SAGRADA_EVA.yaml presente en config/?
- [ ] ¿data/memoria_eva.jsonl creado?
- [ ] ¿centinela monitorean en background si se requiere?
- [ ] ¿Interfaz accesible en navegador?

---

## 🎯 SIGUIENTE PASO

Si no sabes por dónde empezar:
1. Lee `INICIO_RAPIDO.md`
2. Ejecuta `python3 core/init_ceremony.py`
3. Abre `http://127.0.0.1:5000/interface/station_progresivo.html`

**Documentación generada por**: Módulo de Validación Suprema NEUROBIT v2.1  
**Severidad**: Epistemológicamente rigurosa

