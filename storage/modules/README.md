Storage modules folder

Place module folders here (e.g. dispatcher, digestor). Each module should expose a
well-known entrypoint. For example, a dispatcher module should provide a
callable `send_message(envelope: dict) -> dict` which returns a dict with at least
`status` and optional `detail`.

This directory contains a mock dispatcher for development and integration tests.
