# NEUROBIT_DEV_TEAM "The Sofistas"

Este documento recoge la visión, arquitectura y artefactos inspirados en el texto compartido por el equipo —tope inicial para incorporar al COMPENDIO/README.

## Resumen

NEUROBIT_DEV_TEAM "The Sofistas" es un equipo de pensamiento lateral con enfoque en programación funcional, modularidad y arquitectura fractal recursiva. El objetivo es construir una Estación Central local que permita integrar validadores (LLM locales), dispatchers y módulos de persistencia, preservando soberanía de datos y transparencia.

### Principios

- Fractal recursiva: cada módulo contiene la esencia del sistema completo.
- Polisemia extrapolar: metadatos y tags que enriquecen contextos.
- Independencia modular: cada componente puede ejecutarse de forma autónoma.
- Ejecución local: el sistema corre en la máquina del usuario (APACHE/localhost), evitando fugas de datos.
- Ética: control del usuario sobre las decisiones críticas.

## Arquitectura propuesta (esquema)

ESTACIÓN CENTRAL (main_hub.py)

├── /modules/
│   ├── dispatcher.py
│   ├── validator.py
│   ├── sender.py
│   └── context_expander.py

├── /config/
│   └── system_vars.yaml

├── /data/
│   └── coherence_db/

└── /interface/
    ├── index.html
    ├── styles.css
    └── control.js

## Ejemplos incluidos (V0.1)

- `config/system_vars.yaml` (variables centrales y justificaciones)
- `core/context_expander.py` (implementación básica de polisemia fractal)
- `interface/index.html`, `interface/control.js`, `interface/styles.css` (frontend minimal)

### Ejemplo de contrato de integración para agentes (YAML)

```yaml
protocol_id: neurobit_agent_integration_v1
agent_requirements:
  - local_execution_only: true
  - no_external_data_leakage: true
  - explicit_consent_for_each_task: true
role_options:
  - validator
  - dispatcher
  - memory_keeper
  - creative_partner
```

### Ejemplo de agente (agent yaml)

```yaml
agent_id: "llama_local_01"
role: "validator"
permissions: ["read:/sala/inbox", "write:/sala/reports"]
restrictions: ["no_internet_access", "no_user_data_export"]
communication_channel: "http://localhost:8080/agent_api"
```

## Tareas propuestas

1. Revisar módulos sin modificar funcionalidad: `sala/app/`, `tools/`, `nodes/`, `memoria/`.
2. Copiar módulos clave a `storage/modules/` para evaluación controlada.
3. Generar adaptadores en `core/adapters/` que normalicen la API de dispatch/validator.
4. Ejecutar pruebas con `POST /analyze` y `action: dispatch` para validar la integración.

## Notas finales

Los archivos de ejemplo añadidos son una base para que el equipo pueda iterar: documentación, configuración y un frontend ligero. Se propone seguir con la importación controlada de módulos y la creación de shims/adaptadores.
