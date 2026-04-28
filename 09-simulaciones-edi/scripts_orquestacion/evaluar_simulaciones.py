#!/usr/bin/env python3
"""Compat wrapper. Usa repos/scripts/build/evaluar_simulaciones.py."""
import runpy
from pathlib import Path
runpy.run_path(str(Path(__file__).resolve().parent / 'build' / 'evaluar_simulaciones.py'), run_name='__main__')
