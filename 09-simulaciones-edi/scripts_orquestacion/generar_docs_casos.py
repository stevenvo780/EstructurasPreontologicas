#!/usr/bin/env python3
"""Compat wrapper. Usa repos/scripts/build/generar_docs_casos.py."""
import runpy
from pathlib import Path
runpy.run_path(str(Path(__file__).resolve().parent / 'build' / 'generar_docs_casos.py'), run_name='__main__')
