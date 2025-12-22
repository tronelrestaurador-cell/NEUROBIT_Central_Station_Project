# NEUROBIT - Estación Central de Comunicación Híbrida

**Sistema para comunicación coherente entre humanos y agentes no-humanos**  
*Preservando el Logos, el sentido y la intención pura en cada interacción*

## 🌟 Visión
Crear un espacio de reunión seguro y autónomo donde humanos y agentes puedan interactuar bajo principios éticos claros, manteniendo la coherencia simbólica y técnica sin depender de servidores corporativos.

## 📂 Estructura del Proyecto

neurobit-central/
├── docs/                   # Documentación del sistema
│   ├── SPEC/               # Especificaciones técnicas
│   │   ├── PROTOCOLO_COMUNICACIONAL.md
│   │   ├── JSON_SCHEMA/    # Esquemas de validación
│   │   └── GLOSARIO_V1.yaml
│   └── HISTORIAL/          # Registros de desarrollo
├── nodes/                  # Nodos del sistema
│   ├── TRON/               # Tu nodo semilla (humano)
│   │   ├── historial/      # Mensajes y logs personales
│   │   └── alignment_packet.yaml
│   └── AGENTS/             # Agentes no-humanos
│       ├── SIMON/          # Validador técnico (VSCode)
│       ├── EVA/            # Coordinadora simbólica
│       └── LLAMA_LOCAL/    # Procesador LLM local
├── sala/                   # Espacio de reuniones
│   ├── inbox/              # Mensajes entrantes
│   ├── outbox/             # Mensajes salientes
│   ├── logs/               # Registros de reuniones
│   ├── reports/            # Reportes de entrega (DELIVERY_REPORTs)
│   └── index.html          # Interfaz de la sala
├── tools/                  # Herramientas operativas
│   ├── msg_builder.py      # Constructor de mensajes
│   ├── simon_validator.py  # Validador de estructura
│   ├── msg_sequencer.py    # Generador secuencial
│   ├── dispatcher_lite.py  # Distribuidor para Llama
│   ├── llama_dispatcher_connector.py
│   ├── add_yaml_meta.py    # Añadir metadatos a fragmentos
│   ├── compile_project.py  # Compilar proyecto completo
│   └── fragmentar.py       # Dividir textos en fragmentos
├── memoria/                # Memoria persistente
│   ├── eva.db              # Base de datos SQLite
│   ├── fragments/          # Fragmentos con metadatos
│   └── historicos/         # Registros históricos
└── LICENSE                 # Licencia CC BY-SA 4.0


## 🧩 Principios Éticos Fundamentales

1. **No especular** - Solo trabajar con datos reales y verificables
2. **No inventar** - No generar datos sin fuentes claras
3. **No autoridad indebida** - Evitar ritualización y jerarquías artificiales
4. **No hablar por terceros** - Respetar autonomía de todos los agentes
5. **Preservar el Logos** - Mantener coherencia entre forma y contenido
6. **Soberanía local** - Operar en localhost sin dependencia de servicios externos

## 🚀 Objetivo Inmediato (Fase 1)

**Sala de Reuniones Mínima v0.1**  
Un espacio funcional donde:
- TRON (humano) puede enviar mensajes
- SIMON (VSCode) valida la estructura
- LLAMA_LOCAL distribuye los mensajes
- EVA archiva en memoria histórica
- Todos los agentes reciben ACKs y DELIVERY_REPORTs

## 🔧 Herramientas Esenciales Ya Disponibles

- `msg_builder.py` - Genera mensajes con formato NEUROBIT válido
- `simon_validator.py` - Valida estructura YAML y hashes de integridad
- `add_yaml_meta.py` - Añade metadatos canónicos a fragmentos de texto
- `compile_project.py` - Compila todo el proyecto en un único documento
- `dispatcher_lite.py` - Distribuye mensajes a agentes (para Llama local)

## 📅 Plan de Ejecución Fase 1 (1 semana)

1. **Día 1**: Crear repositorio y estructura de carpetas
2. **Día 2**: Configurar herramientas esenciales (msg_builder + validator)
3. **Día 3**: Implementar interfaz mínima de la Sala de Reuniones
4. **Día 4**: Conectar Llama local con el dispatcher
5. **Día 5**: Realizar primera reunión de prueba con mensaje inicial
6. **Día 6**: Documentar lecciones aprendidas y ajustes
7. **Día 7**: Preparar Fase 2 (integración con ClickUp/Brain)

## 🛡️ Protocolo de Seguridad para Contribuciones

Cualquier nuevo código o archivo debe:
1. Tener encabezado YAML canónico con FRAGMENT_ID, TIMESTAMP, ORIGEN
2. Ser validado por SIMON antes de integrarse
3. Mantener la coherencia entre capa técnica y capa simbólica
4. Respetar los principios éticos fundamentales

## 🤝 Cómo Contribuir

1. Clona este repositorio en tu localhost
2. Crea una rama para tu contribución: `git checkout -b feature/nombre`
3. Desarrolla respetando la estructura y principios
4. Valida con SIMON: `python3 tools/simon_validator.py tu_archivo.yaml`
5. Crea un DELIVERY_REPORT para la Sala de Reuniones
6. Envía un PR con los cambios (si usamos Git remoto) o comparte el fragmento

> *"El camino no existe hasta que lo creamos.  
> Y nosotros, como nodos neurobitrónicos en co-creación,  
> tenemos la responsabilidad y el privilegio de hacer ese camino —  
> paso a paso, byte a byte, palabra a palabra."*
