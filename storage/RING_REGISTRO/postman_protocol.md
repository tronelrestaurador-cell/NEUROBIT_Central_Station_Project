# POSTMAN / CURL PROTOCOL — NEUROBIT_SALON_v0.1

Breve: instrucciones para que NODO_SEMILLA recupere fragmentos y entregue un paquete a SIMON vía HTTP.

1) RECUPERAR FUENTES
- Si hay endpoint público/privado: usar GET para descargar logs o fragmentos.
  Ejemplo (reemplazar URL y parámetros):

  curl -sS -o fragments.json "https://example.com/logs?from=2025-12-01&to=2025-12-28"

- Si los archivos están en disco local: copiar `Qwen Chat4_conversation.txt` y `Qwen Chat4_code_blocks_attributed.txt`.

2) NORMALIZAR TIMESTAMPS
- Recomendado: usar ISO-8601 (UTC). Si no están, indicar en el manifest el timezone original.

3) PREPARAR PAQUETE
- Estructura mínima del paquete `handoff_package/`:
  - `handoff.md` (este archivo operativo)
  - `manifest.json` (metadatos: fuentes, conteo, timestamps)
  - `fragments/` (archivos o JSON con fragmentos referenciados)
  - `snippets/` (opcional: los archivos de `code_snippets` relevantes)

Ejemplo de `manifest.json` (mínimo):

```
{
  "project":"NEUROBIT_SALON_v0.1",
  "handoff":"handoff.md",
  "generated_at":"2025-12-28T00:00:00Z",
  "sources":[{"type":"file","path":"Qwen Chat4_conversation.txt"},{"type":"dir","path":"code_snippets/"}],
  "snippet_count":77
}
```

4) COMPRIMIR PAQUETE

zip -r handoff_package.zip handoff_package/

5) ENVIAR A SIMON (POST multipart/form-data)

curl -X POST "https://simon.receiver.example/api/receive" \
  -F "file=@handoff_package.zip" \
  -F "meta=@manifest.json;type=application/json"

Nota: reemplazar URL de destino por la real y añadir autenticación si corresponde.

6) CONTROL BÁSICO
- El receptor (SIMON) debe devolver JSON con `{ status: "ok", id: "<ticket>" }`.
- Guardar ese ticket en `storage/RING_REGISTRO/` como referencia.

---
Archivo: `neurobit_salon_v0.1/storage/RING_REGISTRO/postman_protocol.md`
