# 🔍 AUDITORÍA MAESTRO - NEUROBIT SALÓN v0.1
**Generado**: 17 enero 2026 | **Estado**: Completo  
**Total de archivos**: 6,229+ | **Tamaño**: 2.1GB  
**Categoría**: CRÍTICO - Reorganización requerida

---

## 📊 RESUMEN EJECUTIVO

| Carpeta | Archivos | Tamaño | Tipo | Estado |
|---------|----------|--------|------|--------|
| **input_texts** | 10,679 | 1.3G | 🔴 DATOS | ⚠️ CRÍTICO |
| **BACKUP** | 12 | 308M | 🔴 DATOS | 📦 ARCHIVO |
| **Neurobit_message_builder_BROWSER-EXTENSION** | 3,772 | 203M | 🟢 EXTENSION | ⏳ INCOMPLETO |
| **storage** | 197 | 121M | 🔴 DATOS | 📂 MIXTO |
| **tools** | 50 | 25M | 🟡 MÓDULOS | ⚠️ DISPERSO |
| **docs** | 7 | 22M | 📚 DOCS | 📖 ÚTIL |
| **scripts** | 23 | 172K | 🟡 SCRIPTS | ⚠️ SIN USAR |
| **neurobit-gui** | 0 | 4.0K | 🔴 GUI | 📦 ABANDONADO |
| **core** | 41 | 268K | 🟢 ACTIVO | ✅ CORE |
| **interface** | 13 | 144K | 🟢 ACTIVO | ✅ TRABAJANDO |
| **config** | 4 | 20K | 🔧 CONFIG | ✅ CORE |
| **data** | 6 | 12M | 🔴 DATOS | ✅ JSONL |

---

## 🗂️ ANÁLISIS DETALLADO POR CARPETA

### 🔴 CATEGORÍA: DATOS (Problemas principales)

#### **input_texts/** — 10,679 archivos | 1.3GB ⚠️⚠️⚠️
**PROBLEMA CRÍTICO**: Esta carpeta contiene casi **62% del proyecto**

**Contenido identificable**:
- Fragmentos de conversaciones (RONDAs, ACKs, alerts)
- Textos de sesiones (SALA_SESION_001.yaml, etc.)
- Partes fragmentadas (parte_01.txt hasta parte_NN.txt)
- Duplicados posibles y versiones antiguas

**RECOMENDACIÓN**:
```
input_texts/
├── ARCHIVOS/ (carpeta contenedora)
│   ├── RONDAS/ (organizar por sesión)
│   ├── FRAGMENTOS/ (partes numeradas)
│   ├── SESIONES/ (SALA_SESION_*.yaml)
│   └── LEGACY/ (archivos .old de respaldo)
```

**ACCIÓN INMEDIATA**: 
- [ ] Auditar subfolder structure dentro de input_texts
- [ ] Identificar duplicados
- [ ] Mover antiguos a LEGACY/ o renombrar .old

---

#### **BACKUP/** — 12 archivos | 308MB 📦
**CONTENIDO**: Respaldos históricos  
**ESTADO**: Archivado - conservar pero separar  
**RECOMENDACIÓN**: Renombrar a `BACKUP.old/` si no se usa, o mover a `data/backups/`

---

#### **storage/** — 197 archivos | 121MB 📂
**ESTRUCTURA ACTUAL**:
- `storage/RING_PROCESOS/` — Fragmentos de trabajo
- `storage/RING_REGISTRO/` — Registros y handoffs
- `storage/modules/` — Módulos dinámicos (mock_dispatcher, etc.)

**ESTADO**: Parcialmente organizado pero podría consolidarse  
**RECOMENDACIÓN**: Mantener estructura RING, pero:
```
storage/
├── RING_PROCESOS/ (✅ Mantener)
├── RING_REGISTRO/ (✅ Mantener)
├── modules/ (✅ Activo - módulos plugin)
└── LEGACY/ (archivos históricos con .old)
```

---

### 🟢 CATEGORÍA: CÓDIGO ACTIVO (Mantener + Mejorar)

#### **core/** — 41 archivos | 268K ✅
**CONTENIDO IDENTIFICABLE**:
- `agents_registry.py` — Multi-agent system (500 líneas, reciente)
- `m_e_scoring.py` — Coherencia/Emoción scoring
- `message_validator.py` — Validación de envelopes
- `round_manager.py` — Orquestación de rondas
- `context_declare.py` — Contexto y metadatos
- Otros: adapters, coherence_filter, etc.

**ESTADO**: ✅ **ACTIVO Y FUNCIONAL**  
**ACCIÓN**: Listar detalladamente todos los .py para documentación

---

#### **interface/** — 13 archivos | 144K ✅
**CONTENIDO IDENTIFICABLE**:
- `station_progresivo.html` — GUI principal (con matriz 13×13)
- `arquetipos.js` — Matriz 13×13 core (400 líneas)
- `matriz_ui.js` — Interfaz matriz (300 líneas)
- `agents_management.js` — Panel de agentes (400 líneas)
- `station_progresivo.js` — Orquestación UI
- Otros: minimal_ui.html, etc.

**ESTADO**: ✅ **ACTIVO Y EN DESARROLLO**  
**ACCIÓN**: Documentar cada .js como "WORKING" o "HISTORICAL"

---

#### **config/** — 4 archivos | 20K ✅
**CONTENIDO**:
- `memoria_sagrada_eva.yaml` — Glosario y configuración
- `protocol_contract_v0.1.json` — Especificación de envelopes

**ESTADO**: ✅ **NÚCLEO - MANTENER**

---

#### **data/** — 6 archivos | 12M ✅
**CONTENIDO**:
- `memoria_eva.jsonl` — Append-only log (esencial)
- `agents_registry.jsonl` — Registro de agentes
- Otros archivos de estado

**ESTADO**: ✅ **NÚCLEO - MANTENER**  
**NOTA**: No tocar estructura JSONL

---

### 🟡 CATEGORÍA: MÓDULOS (Disperso - Necesita reorganización)

#### **tools/** — 50 archivos | 25M ⚠️
**SUBFOLDER CRÍTICO: `tools/modulos sueltos/`**  
Este es el corazón del problema. Contiene:

**Módulos Core (Recuperados)**:
- `fragmentar.py` — Fragmentación de mensajes
- `compendio_inteligente_v23.py` — Generador de compendios
- `rebuild_from_spec.py` — PASO 1 (ya integrado ✅)
- `reconstruir_proyecto_desde_compendio.py` — PASO 2 (pendiente)
- `centinela.py` — Monitor/vigilancia
- `BUSCADOR_EVA.py` — Full-text search en memoria

**Helpers**:
- `add_yaml_meta.py` — Agregar metadatos
- `merge_parts.py` — Fusionar fragmentos
- `compile_project.py` — Compilación
- `neurobit_fix.sh` — Script de reparación
- `neurobit_pdf_splitter.py` — Splitter PDF

**Servidores (Prototipos)**:
- `fragment_server.py` — Servidor de fragmentación
- `fragment_server_simple.py` — Versión simplificada

**Modelos Ollama**:
- `neurobit-light.modelfile`
- `neurobit-strict.modelfile`

**Datos (TEXTOS/)**:
- RONDAs, ACKs, alerts (8+ archivos)

**RECOMENDACIÓN - REORGANIZACIÓN**:
```
tools/
├── MODULOS_ACTIVOS/
│   ├── fragmentar.py (USAR)
│   ├── compendio_inteligente_v23.py (REVISAR)
│   ├── centinela.py (INTEGRAR)
│   └── BUSCADOR_EVA.py (INTEGRAR)
├── HELPERS/
│   ├── add_yaml_meta.py
│   ├── merge_parts.py
│   └── compile_project.py
├── SERVIDORES/
│   ├── fragment_server.py
│   └── fragment_server_simple.py (LEGACY - .old)
├── MODELOS_OLLAMA/
│   ├── neurobit-light.modelfile
│   └── neurobit-strict.modelfile
├── DATOS/
│   └── TEXTOS/ (referencia)
└── LEGACY/ (archivos antiguos renombrados .old)
```

**ACCIONES INMEDIATAS**:
- [ ] Listar todos los .py en `tools/modulos sueltos/`
- [ ] Clasificar: ACTIVO / IMPLEMENTADO / PENDIENTE / LEGACY
- [ ] Documentar dependencias entre módulos
- [ ] Renombrar duplicados con sufijo .old

---

#### **scripts/** — 23 archivos | 172K ⚠️
**ESTADO**: No usado actualmente  
**ACCIÓN**: Auditar contenido, fusionar con `tools/` si es relevante, mover a LEGACY si no se usa

---

### 🔵 CATEGORÍA: EXTENSIONES Y ESPECIALIZACIONES

#### **Neurobit_message_builder_BROWSER-EXTENSION/** — 3,772 archivos | 203M ⏳
**CONTENIDO**:
- `manifest.json` — Chrome MV3 extension
- `background.js`, `popup.js`, `content.js` — Extension code
- `COPILOT_INSTRUCTIONS.md` — Documentación
- `neurobit_beta_release.md` — Release notes
- YAML configs: AUTO_GUARDADO.yaml, FIX_CRITICO_FEEDBACK.yaml, MEJORA_HISTORIAL.yaml

**ESTADO**: ⏳ **INCOMPLETO - No integrado con NEUROBIT v2.1**  
**RECOMENDACIÓN**: 
- [ ] Auditar estado actual (¿funciona?)
- [ ] Integrar con agents_registry.py
- [ ] Documentar en EXTENSIONS/

---

#### **bitacora_eva-extension/** — 7 archivos | 96K ⏳
**CONTENIDO**: Otra extensión (propósito desconocido)  
**ESTADO**: ⏳ **Revisar status**  
**ACCIÓN**: Consolidar con Neurobit_message_builder si es redundante

---

#### **neurobit-gui/** — 0 archivos | 4.0K 📦
**ESTADO**: Abandonado pero 90% completo  
**ACCIÓN**: Ya documentado en `neurobit-gui/ANALISIS_ABANDONO.md`  
**RECOMENDACIÓN**: Mover a `ARCHIVE/` o `LEGACY/`

---

### 🟡 CATEGORÍA: SOPORTE E INFRAESTRUCTURA

#### **docs/** — 7 archivos | 22M 📖
**CONTENIDO**: Documentación (valor alto)  
**ESTADO**: ✅ Útil  
**RECOMENDACIÓN**: Mantener, pero:
- [ ] Auditar qué está actualizado vs obsoleto
- [ ] Crear índice master de documentación

---

#### **config/** — 4 archivos | 20K ✅
**ESTADO**: Core configuration  
**RECOMENDACIÓN**: Mantener, expandir si es necesario

---

#### **logs/** — 0 archivos | 4.0K
**ESTADO**: Vacío, OK

---

#### **awake/** — 2 archivos | 16K ⚠️
**CONTENIDO**: `awake_ceremony.py` (propósito olvidado por usuario)  
**ACCIÓN CRÍTICA**: 
- [ ] Leer y documentar propósito
- [ ] Integrar con station_progresivo si es relevante
- [ ] Mover a LEGACY si no se usa

---

#### **inbox/**, **outbox/**, **messages/**, **fragments/** — Varios
**ESTADO**: Vacíos o minimal  
**RECOMENDACIÓN**: Consolidar bajo `data/` o eliminar si no se usan

---

#### **spec/** — 1 archivo | 8.0K
**CONTENIDO**: Especificaciones (revisar)  
**ACCIÓN**: Consolidar con `config/`

---

---

## ✅ PLAN DE REORGANIZACIÓN RECOMENDADO

### FASE 1: Auditoría Detallada (Esta sesión)
1. ✅ Listar estructura general (HECHO)
2. ⏳ Listar detalladamente `tools/modulos sueltos/`
3. ⏳ Categorizar cada archivo: ACTIVO / IMPLEMENTADO / PENDIENTE / LEGACY / DUPLICADO
4. ⏳ Generar documento "QUÉ HACE CADA CARPETA"

### FASE 2: Reorganización (Próxima sesión)
```
neurobit_salon_v0.1/
├── CORE/                         (Código activo)
│   ├── core/                     (lógica principal)
│   ├── interface/                (UIs)
│   ├── config/                   (configuración)
│   └── data/                     (persistencia JSONL)
├── EXTENSIONES/                  (Extensiones browser, etc.)
│   ├── neurobit-message-builder/
│   └── bitacora-eva/
├── MODULES/                      (Módulos plugin)
│   ├── fragmentar.py
│   ├── compendio_inteligente.py
│   ├── centinela.py
│   └── ...
├── SCRIPTS/                      (Helpers y utilidades)
│   ├── compile_project.py
│   ├── add_yaml_meta.py
│   └── ...
├── DATA/                         (Grandes volúmenes de datos)
│   ├── INPUTS/ (actual: input_texts/)
│   ├── STORAGE/ (actual: storage/)
│   └── BACKUPS/
├── DOCS/                         (Documentación)
│   └── (actual: docs/)
├── ARCHIVE/                      (Histórico)
│   ├── neurobit-gui.old/
│   ├── abandoned_experiments/
│   └── backups.old/
└── README FIRST                  (Guía de entrada)
```

### FASE 3: Limpieza (Después de reorganización)
- [ ] Eliminar duplicados
- [ ] Renombrar versiones antiguas con .old
- [ ] Consolidar carpetas vacías
- [ ] Actualizar .gitignore si es necesario

---

## 🚨 ARCHIVOS CRÍTICOS A REVISAR YA

### ALTA PRIORIDAD:
1. **tools/modulos sueltos/** — Listar 50 archivos, categorizar
2. **awake/awake_ceremony.py** — Leer, entender propósito
3. **input_texts/** — ¿Substructure? ¿Duplicados?

### MEDIA PRIORIDAD:
1. **scripts/** — ¿Se usan? Consolidar o eliminar
2. **BACKUP/** — ¿Contiene recuperables?
3. **Neurobit_message_builder_BROWSER-EXTENSION/** — Estado de integración

### BAJA PRIORIDAD:
1. **neurobit-gui/** — Ya documentado, archivar
2. **docs/** — Auditar actualización

---

## 📝 COMANDOS ÚTILES PARA ESTA AUDITORÍA

### Listar contenido de tools/modulos sueltos/
```bash
find tools/modulos\ sueltos/ -maxdepth 1 -type f | sort
```

### Encontrar duplicados
```bash
find . -name "*.py" -o -name "*.js" | xargs -I {} basename {} | sort | uniq -d
```

### Tamaño de cada subcarpeta
```bash
du -sh */ | sort -hr
```

### Archivos sin modificar en último mes
```bash
find . -type f -mtime +30 | head -20
```

---

## 🎯 SIGUIENTE PASO

**Usuario debe confirmar**:
1. ¿Estás de acuerdo con esta estructura propuesta?
2. ¿Quieres que empiece a listar detalladamente `tools/modulos sueltos/`?
3. ¿Hay carpetas que NO debo tocar?
4. ¿Quieres que mantenga backups de todo antes de mover archivos?

---

**Generado por**: Módulo de Validación Neurobit v2.1  
**Rigor**: Epistemológicamente severo  
**Estado**: Listo para FASE 2 de reorganización

