#!/usr/bin/env python3
"""Compat wrapper. Usa repos/scripts/build/actualizar_tablas_002.py."""
import runpy
from pathlib import Path
runpy.run_path(str(Path(__file__).resolve().parent / 'build' / 'actualizar_tablas_002.py'), run_name='__main__')
