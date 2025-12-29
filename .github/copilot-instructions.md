## Instrucciones rápidas para agentes de codificación (Copilot / AI)

Este repositorio (Neurobit Salón v0.1) es un scaffold ligero para ejecutar módulos de procesamiento de "envelopes" (mensajes), manejo de rondas y una API mínima. El propósito de este archivo es dar a un agente LLM la información esencial para ser productivo aquí: arquitectura, comandos útiles, convenciones y puntos de integración.

- Proyecto raíz: `neurobit_salon_v0.1/`
- Componentes clave: `core/` (lógica), `interface/` (estática), `storage/` (módulos y RING_*), `config/` (contratos), `data/` (memoria persistente).

Contrato rápido (inputs / outputs / errores esperados):
- Input principal: JSON con al menos la clave `content` (string). Muchas herramientas esperan un "envelope" parcial que luego se amplía.
- Output: envelope JSON enriquecido; persistencia en `data/memoria_eva.jsonl` es append-only (una línea JSON por entrada).
- Error modes: payload inválido (falta `content`), módulo de despacho ausente/no compatible.

Comandos y flujos concretos
- Iniciar servicio API (desarrollo local):
  - Establecer deps: `pip install -r requirements.txt` (si no existe, revisar `requirements.txt`).
  - Ejecutar: `python3 neurobit_api.py` (o `NEUROBIT_DEBUG=1 python3 neurobit_api.py`).
- Endpoint principal para pruebas: `POST /analyze` con JSON `{"content": "..."}`.
  - Ejemplo curl:
    curl -X POST -H "Content-Type: application/json" -d '{"content":"texto de prueba"}' http://127.0.0.1:5000/analyze
- Inicializar rondas (si existe `core/round_manager.py`):
  - `python3 core/round_manager.py --init`
  - `python3 core/round_manager.py --status`

Patrones y convenciones del código (NO aspiracionales, descubiertos):
- Persistencia ligera: `store_envelope()` escribe JSONL en `data/memoria_eva.jsonl`. No asumir una DB; las tareas deben respetar el append-only.
- Validación: la API espera `content`; si `jsonschema` está instalado se usa una validación mínima. Un agente debe preferir la función `validate_with_schema` cuando proponga cambios.
- Extensibilidad por módulos: el proyecto carga dinámicamente módulos desde `storage/modules` (e.g., `mock_dispatcher`). Los módulos de integración deben exponer funciones conocidas (p.ej. `send_message(envelope)`). Evitar llamadas externas si no se detecta el módulo.
- Archivo de configuración y glosario: `config/memoria_sagrada_eva.yaml` contiene definiciones de términos; útil para mantener coherencia terminológica.

Puntos de integración importantes
- `neurobit_api.py` — salud, `/analyze`, `/memoria`, `/participants`, y `serve_interface` (sirve archivos de `interface/`). Revisar `validate_with_schema`, `store_envelope()` y la sección de dispatch dinámico.
- `storage/modules/` — colocar módulos de integración aquí. Nombre y API esperada: por ejemplo `mock_dispatcher.py` con `send_message(envelope)`.
- `data/memoria_eva.jsonl` — fuente de verdad append-only; al editar tests o scripts, no sobrescribirlo sin respaldo.

Qué pedirle al agente (prompts útiles y tareas seguras)
- "Genera una PR que añada validación unitaria para `validate_with_schema` en `neurobit_api.py` (happy path + payload sin `content`)."
- "Crea un módulo de ejemplo `storage/modules/mock_dispatcher.py` que implemente `send_message(envelope)` y documenta su comportamiento en `storage/modules/README.md`." (no ejecutar la dispatch en producción por defecto).
- "Documenta `data/memoria_eva.jsonl` y añade una función helper `read_memoria(page, limit)` en `core/` con tests básicos."

Reglas y precauciones específicas del repo
- No cambiar el formato JSONL existente en `data/` (mantener una línea JSON por evento).
- Evitar asumir que `jsonschema` está presente; escribir código defensivo o añadir `requirements.txt` si se necesita.
- No habilitar dispatch automático en PRs de ejemplo; dejarlo desactivado por defecto y añadir pasos de configuración explícitos.

Archivos a inspeccionar primero
- `neurobit_api.py` (API + validaciones)
- `core/` (lógica principal, p.ej. `m_e_scoring.py` o `round_manager.py`)
- `storage/modules/` (módulos plug-in)
- `config/memoria_sagrada_eva.yaml` (glosario/terminología)
- `setup_neurobit.sh` (script de scaffold; contiene ejemplos de archivos generados automáticamente)

Si algo no es claro: pídeme que lea un archivo específico (path absoluto o relativo) y generaré una PR con cambios mínimos y tests cuando sea posible.

Fin. Pide retroalimentación sobre secciones incompletas o ejemplos que quieras añadir.
