#!/usr/bin/env python3
"""Compat wrapper. Usa repos/scripts/audit/verificar_consistencia.py."""
import runpy
from pathlib import Path
runpy.run_path(str(Path(__file__).resolve().parent / 'audit' / 'verificar_consistencia.py'), run_name='__main__')
