#!/usr/bin/env python3
"""neurobit_api.py

Micro-API minimalista para NEUROBIT.

Endpoints:
 - GET /            -> health
 - POST /analyze    -> acepta JSON con {"content": "..."} o un envelope parcial y devuelve el envelope completo con análisis M/E

Instalación rápida: pip install -r requirements.txt

Diseñado para ser usado con curl o testing simple.
"""

from __future__ import annotations

import json
try:
    from flask import Flask, request, jsonify, send_from_directory  # type: ignore
except Exception:
    # Flask may not be installed in the environment running static checks.
    Flask = None
    request = None
    def jsonify(x):
        return x

try:
    import jsonschema
except Exception:
    jsonschema = None

try:
    import yaml
except Exception:
    yaml = None

from core.coherence_filter import analyze as analyze_text
from core import participants as participants_mod
import importlib
import sys
from pathlib import Path

# Make storage/modules available on sys.path for dynamic module loading
modules_path = Path(__file__).resolve().parents[0] / 'storage' / 'modules'
if str(modules_path) not in sys.path:
    sys.path.insert(0, str(modules_path))

app = Flask(__name__)


def validate_envelope_partial(env: dict) -> tuple[bool, str]:
    """Validación ligera del esquema para envíeos parciales.

    Verifica presencia de claves útiles. No replace schema validation library.
    """
    if not isinstance(env, dict):
        return False, "payload must be a JSON object"
    # If user supplied raw content, we'll generate envelope; otherwise expect content key
    if "content" not in env:
        return False, "missing 'content' field"
    if not isinstance(env.get("content"), str):
        return False, "'content' must be a string"
    return True, "ok"


def validate_with_schema(env: dict) -> tuple[bool, str]:
    """Try to validate payload with a minimal schema using jsonschema if available.

    Falls back to validate_envelope_partial when jsonschema isn't installed.
    """
    if jsonschema is None:
        return validate_envelope_partial(env)
    # Minimal schema: content required, entity_id string optional, plane optional
    schema = {
        "type": "object",
        "properties": {
            "content": {"type": "string"},
            "entity_id": {"type": "string"},
            "perspective": {"type": "string"},
            "context": {"type": "string"},
            "intention": {"type": "string"},
            "glossary": {"type": "array"}
        },
        "required": ["content"]
    }
    try:
        jsonschema.validate(instance=env, schema=schema)
        return True, "ok"
    except jsonschema.ValidationError as e:
        return False, f"schema_validation_error: {e.message}"


@app.route("/", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "neurobit_api", "version": "v0.1"})


@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        payload = request.get_json(force=True)
    except Exception as e:
        return jsonify({"error": "invalid json", "detail": str(e)}), 400

    valid, msg = validate_with_schema(payload)
    if not valid:
        return jsonify({"error": "invalid_payload", "detail": msg}), 400

    metadata = {
        "entity_id": payload.get("entity_id", "UNKNOWN"),
        "perspective": payload.get("perspective", "tecnica"),
        "context": payload.get("context", ""),
        "intention": payload.get("intention", ""),
        "signed_by": payload.get("signed_by", "API") ,
        "action": payload.get("action", "store")
    }

    envelope = analyze_text(payload.get("content"), metadata=metadata, glossary=payload.get("glossary"))

    # Persist if requested
    if envelope.get("action") == "store" or payload.get("action") == "store":
        try:
            store_envelope(envelope)
            envelope['provenance']['stored'] = True
        except Exception as e:
            envelope['provenance']['stored'] = False
            envelope['provenance']['store_error'] = str(e)

    # Optional dispatch: if client requested action 'dispatch', attempt to load
    # a dispatcher module from storage/modules/mock_dispatcher and call it.
    if payload.get('action') == 'dispatch' or envelope.get('action') == 'dispatch':
        try:
            # default to mock_dispatcher; real integration modules can be placed
            # in storage/modules and expose send_message(envelope)
            dispatcher = importlib.import_module('mock_dispatcher')
            if hasattr(dispatcher, 'send_message'):
                result = dispatcher.send_message(envelope)
                envelope.setdefault('provenance', {})
                envelope['provenance']['dispatched'] = True
                envelope['provenance']['dispatch_result'] = result
            else:
                envelope.setdefault('provenance', {})
                envelope['provenance']['dispatched'] = False
                envelope['provenance']['dispatch_error'] = 'no send_message on module'
        except Exception as e:
            envelope.setdefault('provenance', {})
            envelope['provenance']['dispatched'] = False
            envelope['provenance']['dispatch_error'] = str(e)

    return jsonify(envelope)


@app.route('/memoria', methods=['GET'])
def memoria_list():
    """List entries from the append-only memoria_eva.jsonl file.
    Query params: page (1-based), limit (default 20)
    """
    page = int(request.args.get('page', '1') or 1)
    limit = int(request.args.get('limit', '20') or 20)
    if page < 1:
        page = 1
    if limit < 1:
        limit = 20

    import os
    from pathlib import Path
    base = Path(__file__).resolve().parents[0]
    out = base / 'data' / 'memoria_eva.jsonl'
    entries = []
    if out.exists():
        with out.open('r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    entries.append(json.loads(line))
                except Exception:
                    # ignore malformed lines
                    continue

    # reverse to show newest first
    entries = list(reversed(entries))
    start = (page - 1) * limit
    end = start + limit
    page_entries = entries[start:end]
    return jsonify({
        'page': page,
        'limit': limit,
        'total': len(entries),
        'items': page_entries
    })


@app.route('/participants', methods=['GET'])
def participants_list():
    """Return configured participants."""
    try:
        parts = participants_mod.list_participants()
        return jsonify({'participants': parts})
    except Exception as e:
        return jsonify({'error': 'failed_to_load_participants', 'detail': str(e)}), 500


@app.route('/interface/<path:filename>', methods=['GET'])
def serve_interface(filename):
    """Serve static files from the interface directory so the UI is reachable."""
    from pathlib import Path
    base_dir = Path(__file__).resolve().parents[0]
    interface_dir = base_dir / 'interface'
    # security: avoid directory traversal
    return send_from_directory(str(interface_dir), filename)


def store_envelope(envelope: dict) -> None:
    """Append the envelope JSON to the append-only Memoria Sagrada file.

    File: data/memoria_eva.jsonl (created if not exists)
    """
    import os
    from pathlib import Path

    base = Path(__file__).resolve().parents[0]
    data_dir = base / 'data'
    data_dir.mkdir(parents=True, exist_ok=True)
    out = data_dir / 'memoria_eva.jsonl'
    with out.open('a', encoding='utf-8') as f:
        f.write(json.dumps(envelope, ensure_ascii=False) + "\n")



if __name__ == "__main__":
    import os
    host = os.environ.get("NEUROBIT_HOST", "127.0.0.1")
    port = int(os.environ.get("NEUROBIT_PORT", 5000))
    # Allow toggling debug via env var, but disable the auto-reloader to avoid
    # issues when running inside this orchestrated terminal environment.
    debug_flag = os.environ.get("NEUROBIT_DEBUG", "0") in ("1", "true", "True")
    app.run(host=host, port=port, debug=debug_flag, use_reloader=False)
