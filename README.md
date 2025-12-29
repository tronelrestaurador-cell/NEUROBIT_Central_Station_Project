Neurobit Salón v0.1

Scaffold mínimo para activar el Salón de Reuniones local.

Estructura:
- core/: lógica de gestión de rondas y validación mínima
- interface/: interfaz mínima estática
- storage/: RING_REGISTRO y RING_PROCESOS
- config/: contrato de protocolo (JSON Schema)

Iniciar (ejemplo):

```bash
python3 core/round_manager.py --init
python3 core/round_manager.py --status
```

Notas:
- Copia los snippets extraídos en `storage/RING_PROCESOS/` antes de lanzar la primera ronda, o usa el script `core/round_manager.py` para inicializar.
