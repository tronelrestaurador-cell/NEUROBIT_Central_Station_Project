#!/usr/bin/env python3
"""message_validator.py - validador YAML/JSON mínimo para mensajes del salon"""
import sys
import json
import yaml

SCHEMA_MIN = {
    'required_keys': ['HEADER_NOTE', 'OBJETIVO', 'ACCIONES']
}

def validate_yaml(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
    except Exception as e:
        print('Error al leer YAML:', e)
        return False
    for k in SCHEMA_MIN['required_keys']:
        if k not in data:
            print('Falta clave requerida:', k)
            return False
    print('YAML válido (mimico)')
    return True

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Uso: message_validator.py <archivo.yaml>')
        sys.exit(2)
    path = sys.argv[1]
    validate_yaml(path)
