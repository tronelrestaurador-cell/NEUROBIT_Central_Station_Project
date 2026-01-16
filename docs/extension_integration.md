## Integración de la extensión MV3 y servidor MCP con la Estación Central

Este documento explica los pasos mínimos para integrar la extensión y el nuevo servidor MCP en la Estación Central.

1) Inicializar workspace

```bash
./automations/init_workspace.sh
```

2) Iniciar el servidor MCP (puerto 8090)

```bash
python3 connectors/mcp_server.py &
```

3) Probar el adaptador MCP desde Python

```python
from core.adapters import adapter_mcp
print(adapter_mcp.read_arca(3))
```

4) En la Estación Central: usar `core.adapters.adapter_mcp.send_message(envelope)` para registrar eventos en la arca.

5) Notas de seguridad:
- El archivo `data/memoria_eva.jsonl` es append-only; no lo reescribas.
- Valida siempre `MESSAGE_ID` y `content` antes de llamar a `send_message`.
