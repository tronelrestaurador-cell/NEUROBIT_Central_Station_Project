# REPORTE DE SITUACIÓN: PROYECTO NEUROBIT_SALON_v0.1
**Estado**: Integración de Nodo MCP Local
**Protocolo**: Neurobit v2.1

## CONSTANTES Y VARIABLES
- **RING_PROCESOS**: Directorio de lógica activa (`storage/modules/`).
- **RING_REGISTRO**: Directorio de datos persistentes (`data/`).
- **ARCA_PATH**: `data/memoria_eva.jsonl` (Formato Append-only).
- **VERSION**: 2.1 (Soporte fractal).

## MÓDULOS ACTUALES
1. **neurobit_api.py**: Backend Flask/Python que recibe el Logos.
2. **simon_validator.py**: Centinela de integridad de código y protocolo.
3. **llama_dispatcher_connector.py**: Adaptador para comunicación local.
4. **compile_project.py**: Herramienta de unificación de archivos.

## CONECTORES Y TOOLS
- **Extensión Browser**: Captura datos y los envía vía POST a la API.
- **SIMON**: Valida que el `MESSAGE_ID` siga la sucesión (A1, A2, A3...).
- **Ollama Connector**: Interface con el modelo local.

## MISIÓN INMEDIATA
Construir un `neurobit_mcp_server.py` que permita al asistente de VSCode:
- Leer el estado actual del Arca.
- Escribir nuevos registros validados.
- Acceder a los metadatos de las conversaciones (6446 páginas de contexto resumido).
