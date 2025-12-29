#!/usr/bin/env python3
"""round_manager.py - gestor mínimo de rondas para neurobit_salon_v0.1

Funciones:
 - --init : inicializa el entorno (crea archivo de sesión inicial)
 - --status: muestra estado minimal
"""
import argparse
from pathlib import Path
import shutil
import sys

def init(args):
    root = Path(__file__).resolve().parents[1]
    storage = root / 'storage'
    ring_proc = storage / 'RING_PROCESOS'
    ring_reg = storage / 'RING_REGISTRO'
    ring_proc.mkdir(parents=True, exist_ok=True)
    ring_reg.mkdir(parents=True, exist_ok=True)
    # create initial session file
    session_file = ring_reg / 'SALA_SESION_001_INIT.txt'
    if not session_file.exists():
        session_file.write_text('SALA_SESION_001 - initialized\n')
    print('Initialized neurobit_salon at', root)
    print('Session file written to', session_file)

def status(args):
    root = Path(__file__).resolve().parents[1]
    print('Neurobit Salon root:', root)
    print('Storage contents:')
    for p in (root / 'storage').glob('**/*'):
        print('-', p.relative_to(root))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--init', action='store_true', help='Inicializa el salon')
    parser.add_argument('--status', action='store_true', help='Muestra estado')
    args = parser.parse_args()
    if args.init:
        init(args)
    elif args.status:
        status(args)
    else:
        parser.print_help()
