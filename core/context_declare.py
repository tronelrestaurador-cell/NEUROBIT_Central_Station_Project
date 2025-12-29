#!/usr/bin/env python3
"""context_declare.py - declara límites de visibilidad y políticas mínimas para la sesión"""
from pathlib import Path

def declare_limitations(root=None):
    if not root:
        root = Path(__file__).resolve().parents[1]
    cfg = root / 'config' / 'visibility_policy.txt'
    cfg.write_text('VISIBILITY: local_only\nRETAIN_DAYS: 365\nACCESS: NEUROBIT_DEV_TEAM')
    print('Visibility policy written to', cfg)

if __name__ == '__main__':
    declare_limitations()
