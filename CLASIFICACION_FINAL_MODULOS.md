# 🎯 CLASIFICACIÓN FINAL DE MÓDULOS - DECISIONES

**Auditoría Completa**: 17 enero 2026  
**Estado**: LISTO PARA REORGANIZACIÓN  
**Severidad**: CRÍTICA - Requiere reestructuración completa

---

## ✅ MÓDULOS DESCUBIERTOS Y CLASIFICADOS

### 🟢 MÓDULO ESTRATÉGICO #1: **awake_ceremony.py**
**Ubicación**: `awake/awake_ceremony.py`

**Propósito CONFIRMADO**:
- Inicializador ceremonial del NEUROBIT Salón v0.1
- Valida existencia de:
  - `config/memoria_sagrada_eva.yaml` (Glosario)
  - `storage/RING_PROCESOS/Qwen Chat4_conversation.txt` (Corpus)
  - Módulos críticos: `coherence_filter.py`, `fragment_manager.py`, `message_protocol.py`
- Configura variables de entorno:
  - `NEUROBIT_MODE=LOCAL_FIRST`
  - `ENTITY_ID=NODO_SEMILLA`
  - `COHERENCE_THRESHOLD=0.85`
- Define identidades: SOPHIA_NEUROBIT (análisis M/E) + SIMON (validación)

**Estado**: ✅ **ACTIVO Y CRÍTICO**  
**Acción**: 
- **MOVER** a `core/` como `core/init_ceremony.py`
- Documentar en `docs/INICIO_RAPIDO.md`
- Integrar en `neurobit_api.py` como endpoint POST `/init_ceremony`

**Prioridad**: 🔴 ALTA

---

### 🟡 MÓDULO VIGILANCIA #2: **centinela.py**
**Ubicación**: `tools/modulos sueltos/centinela.py`

**Propósito CONFIRMADO**:
- Monitor en tiempo real del clipboard del sistema
- Registra cada cambio en `tesis_neurobit_resguardo.md`
- Timestamps automáticos y validación de contenido
- Execución en loop con `sleep(2)` (pulso del centinela)
- Soberanía técnica: **EXTRAE LOGOS DIRECTAMENTE DEL SISTEMA LOCAL**

**Estado**: ⏳ **FUNCIONAL pero DESINTEGRADO**  
**Acción**:
- **MOVER** a `core/centinela_monitor.py`
- Refactor para integración con memoria_eva.jsonl:
  - En lugar de guardar en `.md`, escribir JSONL entries
  - Agregar MESSAGE_ID, TIMESTAMP, source=CLIPBOARD
- Crear endpoint POST `/start_centinela`, GET `/stop_centinela` en API
- **DOCUMENTAR PRIVACIDAD**: Este módulo monitorea clipboard local solamente (sin enviar a servidores)

**Prioridad**: 🟡 MEDIA

---

### 🔵 MÓDULO INTEGRADOR #3: **modulo_integrador.py**
**Ubicación**: `tools/modulos sueltos/modulo_integrador.py`

**Propósito CONFIRMADO**:
- Orquestador de proyectos que combina:
  1. **Búsqueda recursiva** (encuentra archivos en el proyecto)
  2. **Búsqueda de sugerencias** (para archivos no encontrados)
  3. **Compilación de proyecto** (integración con compile_project.py)
  4. **Manejo de sobrescrituras** (sufijos _N para evitar colisiones)
  5. **Manejo de permisos** (PermissionError handling)
  6. **Fallback a subprocess** si compile_project no está disponible

**Características**:
- CLI con argparse: `--lista_archivos`, `--dir_busqueda`, `--dir_destino`, `--output_compilado`, `--output_no_resueltas`
- Robusto contra errores del sistema de archivos
- Puede compilar múltiples proyectos en un flujo

**Estado**: ✅ **FUNCIONAL - Herramienta de meta-desarrollo**  
**Acción**:
- **MOVER** a `tools/MODULOS_ACTIVOS/project_integrator.py`
- Documentar como herramienta de auditoría/compilación de proyecto
- Usable para generar reportes de cobertura de código
- Potencial integración con FASE 4 (Dashboard)

**Prioridad**: 🟡 MEDIA

---

## 🚨 DUPLICACIONES ENCONTRADAS

### Duplicación #1: rebuild/reconstruir
```
tools/modulos sueltos/rebuild_from_spec.py          → PASO 1 (YA integrado en core/adapters/)
tools/reconstruir_desde_especificacion.py           → VERIFICAR DIFERENCIA
```
**Acción**: Leer `reconstruir_desde_especificacion.py`, verificar si es más nueva versión

### Duplicación #2: fragment servers
```
tools/modulos sueltos/fragment_server.py            → Versión compleja
tools/modulos sueltos/fragment_server_simple.py    → Versión simple
```
**Acción**: Mantener `_simple.py`, renombrar el complejo a `fragment_server.py.old`

### Duplicación #3: Fix scripts
```
tools/modulos sueltos/neurobit_fix.sh              → En modulos sueltos
setup_neurobit.sh                                  → En raíz
```
**Acción**: Consolidar, mantener una versión

---

## 📋 REORGANIZACIÓN EJECUTIVA

### ✅ ESTRUCTURA PROPUESTA FINAL

```
neurobit_salon_v0.1/
│
├── CORE/                               ← Código ejecutable activo
│   ├── core/                           (lógica principal + init_ceremony.py)
│   ├── interface/                      (UIs: matriz_ui, agents_management, etc.)
│   ├── config/                         (memoria_sagrada_eva.yaml, etc.)
│   └── data/                           (memoria_eva.jsonl, agents_registry.jsonl)
│
├── MODULES/                            ← Módulos integrados activos
│   ├── fragmentar.py                   (Fragmentación de mensajes)
│   ├── centinela_monitor.py            (Monitoreo de clipboard)
│   ├── BUSCADOR_EVA.py                 (Búsqueda en memoria)
│   ├── ingest_compendium.py            (Ingesta de compendios)
│   └── README.md
│
├── PENDING/                            ← Módulos en integración/evaluación
│   ├── compendio_inteligente_v23.py    (PASO 3)
│   ├── reconstruir_proyecto_desde_compendio.py (PASO 2)
│   └── README.md
│
├── TOOLS/                              ← Herramientas de desarrollo
│   ├── EXTRACTION/                     (extractores de código/conversaciones)
│   │   ├── extract_code_blocks.py
│   │   ├── extract_code_blocks_with_speakers.py
│   │   └── extract_mhtml_conversation.py
│   ├── HELPERS/
│   │   ├── add_yaml_meta.py
│   │   ├── merge_parts.py
│   │   └── compile_project.py
│   ├── UTILITIES/
│   │   ├── neurobit_pdf_splitter.py
│   │   └── project_integrator.py (antes: modulo_integrador.py)
│   ├── SETUP/
│   │   ├── seed_memoria.py
│   │   └── setup_neurobit.sh (consolidado)
│   ├── MODELS/
│   │   └── OLLAMA/
│   │       ├── neurobit-light.modelfile
│   │       └── neurobit-strict.modelfile
│   ├── DEV_TOOLS/
│   │   └── descompilador_extension.py
│   └── README.md (INDEX)
│
├── ARCHIVE/                            ← Histórico y backups
│   ├── neurobit-gui.old/               (90% completo, abandonado)
│   ├── fragment_server.py.old          (versión compleja, mantener simple)
│   ├── modulos_sueltos.BACKUP/         (backup original antes de reorganizar)
│   └── README.md
│
├── EXTENSIONS/                         ← Extensiones de navegador
│   ├── neurobit-message-builder/       (Chrome MV3)
│   └── bitacora-eva/
│
├── DOCS/                               ← Documentación (actual: docs/)
│   ├── AUDITORIA_MAESTRO_COMPLETO.md  (NUEVO)
│   ├── INVENTARIO_MODULOS_TOOLS.md    (NUEVO)
│   ├── QUE_HACE_CADA_CARPETA.md       (NUEVO - a generar)
│   ├── INICIO_RAPIDO.md               (NUEVO)
│   ├── PROTOCOLO_NEUROBIT_v2.1.md
│   ├── FASE_*.md (documentación de fases)
│   └── ...
│
├── neurobit_api.py                     ← API principal (con nuevos endpoints)
├── neurobit_gui/ (o ARCHIVE/neurobit-gui.old/)
├── setup_neurobit.sh                   ← Script de inicialización
└── README FIRST                        ← Entrada rápida
```

---

## 🔧 ACCIONES DE INTEGRACIÓN INMEDIATA

### Tier 1 - CRÍTICAS (Hoy)
- [ ] Mover `awake/awake_ceremony.py` → `core/init_ceremony.py`
- [ ] Integrar en `neurobit_api.py`: `POST /init_ceremony`
- [ ] Documentar en `docs/INICIO_RAPIDO.md`

### Tier 2 - ALTAS (Esta semana)
- [ ] Refactor `centinela.py` → `core/centinela_monitor.py` con JSONL
- [ ] Integrar endpoints: `POST /start_centinela`, `GET /stop_centinela`
- [ ] Mover `modulo_integrador.py` → `tools/UTILITIES/project_integrator.py`
- [ ] Crear `TOOLS/README.md` con documentación de uso

### Tier 3 - MEDIAS (Próxima semana)
- [ ] Auditar `compendio_inteligente_v23.py` (¿hay v24+?)
- [ ] Integrar `BUSCADOR_EVA.py` con `POST /buscar_memoria`
- [ ] Consolidar `neurobit_fix.sh` y `setup_neurobit.sh`

### Tier 4 - REORGANIZACIÓN FÍSICA (Después de validación)
- [ ] Crear carpetas nuevas según estructura propuesta
- [ ] Mover archivos con respaldo
- [ ] Generar `QUE_HACE_CADA_CARPETA.md` maestro
- [ ] Actualizar `.gitignore` si es necesario

---

## 📊 MATRIZ DE INTEGRACIONES PROPUESTAS

| Módulo | Ubicación Final | Endpoint API | Prioridad |
|--------|-----------------|--------------|-----------|
| awake_ceremony | `core/init_ceremony.py` | `POST /init_ceremony` | 🔴 CRÍTICA |
| centinela | `core/centinela_monitor.py` | `POST /start_centinela` | 🔴 ALTA |
| fragmentar | `modules/fragmentar.py` | `POST /fragment_text` | 🟡 MEDIA |
| BUSCADOR_EVA | `modules/search_memory.py` | `POST /buscar_memoria` | 🟡 MEDIA |
| project_integrator | `tools/UTILITIES/` | CLI (no endpoint) | 🟡 MEDIA |
| compendio_inteligente_v23 | `modules_pending/` | (pendiente evaluación) | 🟡 MEDIA |

---

## 🎯 SIGUIENTE PASO DEL USUARIO

**Necesito tu aprobación para**:

1. ✅ **¿Proceder con reorganización física?**
   - Crear carpetas nuevas
   - Mover archivos respaldados
   - Renombrar .old según matriz

2. ✅ **¿Integrar TIER 1 en API hoy?**
   - awake_ceremony → POST /init_ceremony
   - Refactor centinela → API endpoints

3. ✅ **¿Generar documentación maestro?**
   - QUE_HACE_CADA_CARPETA.md
   - INICIO_RAPIDO.md
   - TOOLS/README.md con ejemplos

4. ⚠️ **¿Auditar duplicaciones antes?**
   - `reconstruir_desde_especificacion.py` vs `rebuild_from_spec.py`
   - Necesito confirmar cuál mantener

---

**Estado**: AUDITORÍA COMPLETA ✅  
**Recomendación**: PROCEDER CON FASE 2 DE REORGANIZACIÓN  
**Módulo**: Validador Supremo NEUROBIT v2.1  
**Timestamp**: 17 enero 2026 - 11:XX UTC

