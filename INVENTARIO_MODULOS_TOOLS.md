# 📦 INVENTARIO DETALLADO DE MÓDULOS - tools/modulos sueltos/
**Generado**: 17 enero 2026  
**Total módulos**: 23 archivos Python + shell + modelfiles  
**Propósito**: Clasificar estado de cada módulo (ACTIVO/IMPLEMENTADO/PENDIENTE/LEGACY)

---

## 🔴 MÓDULOS CRÍTICOS (Núcleo de NEUROBIT)

### 1. **fragmentar.py** ✅ ACTIVO
- **Propósito**: Divide archivos de texto en fragmentos respetando párrafos
- **Función**: `dividir_archivo(archivo_entrada, longitud_maxima=20000, nombre_archivo_salida=None)`
- **Estado**: ✅ FUNCIONAL - Core para fragmentación de mensajes
- **Usado por**: Potencialmente FASE 3.2 (Fragmentador)
- **Acción**: Mantener, considerar importar en `core/`

---

### 2. **rebuild_from_spec.py** ✅ IMPLEMENTADO (PASO 1)
- **Propósito**: Reconstruir proyecto desde especificación JSON
- **Integración**: YA en `core/adapters/adapter_rebuild_spec.py` ✅
- **Referencia**: Documentado en `INTEGRACION_REBUILD_SPEC.md`
- **Estado**: ✅ IMPLEMENTADO Y FUNCIONAL
- **Acción**: VERIFICADO - Mover a ARCHIVE o mantener en tools/ para referencia

---

### 3. **reconstruir_proyecto_desde_compendio.py** ⏳ PENDIENTE
- **Propósito**: PASO 2 - Reconstruir desde compendio inteligente
- **Relación**: Complemento a rebuild_from_spec.py
- **Estado**: ⏳ **REQUIERE INTEGRACIÓN**
- **Acción**: Leer, entender, integrar con PASO 2

---

### 4. **compendio_inteligente_v23.py** ⏳ PENDIENTE
- **Propósito**: PASO 3 - Generador inteligente de compendios
- **Versión**: v23 (múltiples iteraciones)
- **Estado**: ⏳ **REQUIERE EVALUACIÓN**
- **Acción**: Auditar si v23 es final o hay v24+, integrar con PASO 3

---

## 🟡 MÓDULOS DE APOYO (Helpers & Utilidades)

### 5. **centinela.py** 🟢 POTENCIAL ACTIVO
- **Propósito**: Monitor/vigilancia (propósito exacto revisar)
- **Estado**: ⏳ **REQUIERE LECTURA**
- **Acción**: Leer código, integrar con agents_registry si es relevante

---

### 6. **BUSCADOR_EVA.py** 🟢 POTENCIAL ACTIVO
- **Propósito**: Full-text search en memoria JSONL
- **Valor**: Alto - complementa memoria_eva.jsonl
- **Estado**: ⏳ **REQUIERE INTEGRACIÓN**
- **Acción**: Integrar con `/memoria` endpoint de API

---

### 7. **add_yaml_meta.py** 🟡 HELPER
- **Propósito**: Agregar metadatos YAML a archivos
- **Uso**: Preparación de datos
- **Estado**: Disponible, no crítico
- **Acción**: Mover a `tools/HELPERS/` carpeta nueva

---

### 8. **merge_parts.py** 🟡 HELPER
- **Propósito**: Fusionar fragmentos (inverse de fragmentar.py)
- **Uso**: Reconstitución de archivos
- **Estado**: Funcional
- **Acción**: Mover a `tools/HELPERS/`, documentar relación con fragmentar.py

---

### 9. **compile_project.py** 🟡 HELPER
- **Propósito**: Compilación de proyecto
- **Estado**: ⏳ **Revisar si se usa**
- **Acción**: Verificar dependencias, mover a ARCHIVE si obsoleto

---

### 10. **modulo_integrador.py** ❓ DESCONOCIDO
- **Propósito**: Desconocido (leer código)
- **Estado**: ⏳ **REQUIERE LECTURA**
- **Acción**: Auditar, clasificar

---

## 🔵 SERVIDORES (Prototipos)

### 11. **fragment_server.py** 📡 SERVIDOR
- **Propósito**: API HTTP para fragmentación
- **Estado**: ⏳ Prototipo, posible duplication
- **Acción**: Consolidar con fragment_server_simple.py

---

### 12. **fragment_server_simple.py** 📡 SERVIDOR (VERSIÓN SIMPLE)
- **Propósito**: Versión simplificada de fragment_server.py
- **Recomendación**: Mantener esta, archiva la anterior como .old
- **Acción**: Renombrar a `fragment_server.py.old`

---

## 🟠 EXTRACTORES (Herramientas de ingesta)

### 13. **extract_code_blocks.py** 📥 EXTRACTOR
- **Propósito**: Extraer bloques de código de texto/documentos
- **Valor**: Herramienta de ingesta
- **Estado**: Funcional
- **Acción**: Mover a `tools/EXTRACTION/`

---

### 14. **extract_code_blocks_with_speakers.py** 📥 EXTRACTOR (VERSIÓN CON SPEAKERS)
- **Propósito**: Extractor que mantiene identificación de hablantes
- **Valor**: Especifico para multi-agent dialogues
- **Estado**: Funcional
- **Acción**: Mover a `tools/EXTRACTION/`, potencial integración con agents_registry

---

### 15. **extract_mhtml_conversation.py** 📥 EXTRACTOR MHTML
- **Propósito**: Extraer conversaciones de archivos MHTML (archivos web)
- **Uso**: Ingesta de conversaciones de navegador
- **Relación**: Posible complemento a Neurobit_message_builder_BROWSER-EXTENSION
- **Estado**: Funcional
- **Acción**: Mover a `tools/EXTRACTION/`, revisar integración con extension

---

## 🖥️ MODELOS OLLAMA

### 16. **neurobit-light.modelfile** 🤖 MODELO
- **Propósito**: Modelo Ollama ligero
- **Estado**: Disponible
- **Acción**: Mover a `tools/MODELS/OLLAMA/`

---

### 17. **neurobit-strict.modelfile** 🤖 MODELO
- **Propósito**: Modelo Ollama con validación estricta (protocolo NEUROBIT v2.1)
- **Estado**: Disponible
- **Acción**: Mover a `tools/MODELS/OLLAMA/`

---

## 🔧 SCRIPTS DE MANTENIMIENTO

### 18. **neurobit_fix.sh** 🔧 SCRIPT
- **Propósito**: Script de reparación/inicialización
- **Relación**: Similar a `setup_neurobit.sh` en root
- **Estado**: Revisar duplicación
- **Acción**: Consolidar o marcar como .old

---

### 19. **neurobit_pdf_splitter.py** 📄 UTILIDAD
- **Propósito**: Split PDF files
- **Valor**: Útil para ingesta de documentos
- **Estado**: Funcional
- **Acción**: Mover a `tools/UTILITIES/`

---

## 🌐 HERRAMIENTAS DE ROOT TOOLS/

### 20. **descompilador_extension.py** (root tools/) 🔧
- **Propósito**: Descompilación de extensiones
- **Relación**: Para Neurobit_message_builder_BROWSER-EXTENSION
- **Estado**: Herramienta de desarrollo
- **Acción**: Mover a `tools/DEV_TOOLS/`

---

### 21. **GENERADOR_AUDIO_RESUMEN.py** (root tools/) 🎵
- **Propósito**: Genera resumen de audio
- **Estado**: Especializado
- **Acción**: Revisar si se usa, si no → ARCHIVE.old

---

### 22. **ingest_compendium.py** (root tools/) 📥
- **Propósito**: Ingesta de compendios
- **Relación**: Complemento a compendio_inteligente_v23.py
- **Estado**: Funcional
- **Acción**: Consolidar bajo `tools/MODULES/`

---

### 23. **reconstruir_desde_especificacion.py** (root tools/) 📐
- **Propósito**: Similar a rebuild_from_spec.py
- **Acción**: **VERIFICAR DUPLICACIÓN** - ¿Es esta versión más nueva?
- **Estado**: Revisar relación con rebuild_from_spec.py

---

### 24. **seed_memoria.py** (root tools/) 🌱
- **Propósito**: Inicializa memoria_eva.jsonl
- **Valor**: Importante para setup inicial
- **Estado**: Funcional
- **Acción**: Mover a `tools/SETUP/`

---

## 📊 MATRIZ DE DECISIÓN

| Módulo | Acción | Carpeta Destino | Prioridad |
|--------|--------|-----------------|-----------|
| fragmentar.py | MANTENER | `tools/MODULES_ACTIVOS/` | 🔴 ALTA |
| rebuild_from_spec.py | MANTENER/REFERENCE | `tools/ARCHIVE/` | 🟡 MEDIA |
| reconstruir_proyecto_desde_compendio.py | LEER + INTEGRAR | `tools/MODULES_PENDIENTES/` | 🔴 ALTA |
| compendio_inteligente_v23.py | EVALUAR | `tools/MODULES_PENDIENTES/` | 🔴 ALTA |
| centinela.py | LEER + INTEGRAR | `tools/MODULES_ACTIVOS/` | 🟡 MEDIA |
| BUSCADOR_EVA.py | INTEGRAR | `tools/MODULES_ACTIVOS/` | 🟡 MEDIA |
| add_yaml_meta.py | MOVER | `tools/HELPERS/` | 🟢 BAJA |
| merge_parts.py | MOVER | `tools/HELPERS/` | 🟢 BAJA |
| compile_project.py | REVISAR | `tools/UTILITIES/` | 🟢 BAJA |
| modulo_integrador.py | REVISAR | `tools/REVIEW/` | 🟡 MEDIA |
| fragment_server.py | LEGACY | `tools/LEGACY/` | 🟢 BAJA |
| fragment_server_simple.py | MANTENER | `tools/SERVERS/` | 🟡 MEDIA |
| extract_code_blocks.py | MOVER | `tools/EXTRACTION/` | 🟢 BAJA |
| extract_code_blocks_with_speakers.py | MOVER | `tools/EXTRACTION/` | 🟡 MEDIA |
| extract_mhtml_conversation.py | MOVER | `tools/EXTRACTION/` | 🟡 MEDIA |
| neurobit-light.modelfile | MOVER | `tools/MODELS/OLLAMA/` | 🟢 BAJA |
| neurobit-strict.modelfile | MOVER | `tools/MODELS/OLLAMA/` | 🟢 BAJA |
| neurobit_fix.sh | REVIEW | `tools/SCRIPTS/` | 🟡 MEDIA |
| neurobit_pdf_splitter.py | MOVER | `tools/UTILITIES/` | 🟢 BAJA |
| descompilador_extension.py | MOVER | `tools/DEV_TOOLS/` | 🟢 BAJA |
| GENERADOR_AUDIO_RESUMEN.py | REVISAR | `tools/EXPERIMENTAL/` | 🟢 BAJA |
| ingest_compendium.py | CONSOLIDAR | `tools/MODULES_ACTIVOS/` | 🟡 MEDIA |
| reconstruir_desde_especificacion.py | **VERIFICAR DUPLICACIÓN** | TBD | 🔴 ALTA |
| seed_memoria.py | MOVER | `tools/SETUP/` | 🟡 MEDIA |

---

## 🚨 ACCIONES INMEDIATAS REQUERIDAS

### ANTES DE REORGANIZAR:
1. **LEER y CATEGORIZAR**:
   - [ ] `centinela.py` — ¿Qué hace exactamente?
   - [ ] `modulo_integrador.py` — Propósito desconocido
   - [ ] `awake/awake_ceremony.py` — User no recuerda
   
2. **VERIFICAR DUPLICACIONES**:
   - [ ] `rebuild_from_spec.py` vs `reconstruir_desde_especificacion.py`
   - [ ] `fragment_server.py` vs `fragment_server_simple.py`
   - [ ] `neurobit_fix.sh` vs `setup_neurobit.sh` (root)
   
3. **INTEGRAR EN CÓDIGO**:
   - [ ] `BUSCADOR_EVA.py` con API `/memoria`
   - [ ] `centinela.py` con agents_registry
   - [ ] `extract_mhtml_conversation.py` con Neurobit_message_builder_BROWSER-EXTENSION

4. **DOCUMENTAR DEPENDENCIAS**:
   - [ ] Qué módulos dependen de cuáles
   - [ ] Orden de ejecución/inicialización

---

## 📝 ESTRUCTURA PROPUESTA PARA tools/

```
tools/
├── MODULOS_ACTIVOS/
│   ├── fragmentar.py
│   ├── BUSCADOR_EVA.py
│   ├── centinela.py
│   ├── ingest_compendium.py
│   └── README.md (documentación)
├── MODULOS_PENDIENTES/
│   ├── reconstruir_proyecto_desde_compendio.py
│   ├── compendio_inteligente_v23.py
│   └── README.md (PASO 2 y PASO 3)
├── HELPERS/
│   ├── add_yaml_meta.py
│   ├── merge_parts.py
│   ├── compile_project.py
│   └── README.md
├── EXTRACTION/
│   ├── extract_code_blocks.py
│   ├── extract_code_blocks_with_speakers.py
│   ├── extract_mhtml_conversation.py
│   └── README.md
├── SERVERS/
│   └── fragment_server.py (versión simple)
├── UTILITIES/
│   ├── neurobit_pdf_splitter.py
│   └── README.md
├── MODELS/
│   └── OLLAMA/
│       ├── neurobit-light.modelfile
│       └── neurobit-strict.modelfile
├── SETUP/
│   └── seed_memoria.py
├── DEV_TOOLS/
│   └── descompilador_extension.py
├── SCRIPTS/
│   └── neurobit_fix.sh
├── LEGACY/
│   ├── fragment_server.py.old
│   ├── GENERADOR_AUDIO_RESUMEN.py.old
│   ├── modulos sueltos.old/ (backup original)
│   └── README.md (histórico)
├── REVIEW/
│   ├── modulo_integrador.py (revisar)
│   └── reconstruir_desde_especificacion.py (verificar vs rebuild_from_spec)
└── README.md (INDEX MAESTRO)
```

---

## 🎯 SIGUIENTE PASO

**Usuario debe confirmara**:
1. ¿Quieres que empiece a leer los módulos desconocidos (centinela, modulo_integrador, awake_ceremony)?
2. ¿Debo verificar duplicaciones antes de reorganizar?
3. ¿Quieres backup completo de `tools/modulos sueltos/` antes de mover?
4. ¿Autorizo la reorganización con esta estructura?

---

**Módulo de Validación Neurobit v2.1** | Rigor epistemológico | Severidad técnica

