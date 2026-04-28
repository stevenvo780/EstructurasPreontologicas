#!/usr/bin/env python3
"""Compat wrapper. Usa repos/scripts/build/regenerar_readmes.py."""
import runpy
from pathlib import Path
runpy.run_path(str(Path(__file__).resolve().parent / 'build' / 'regenerar_readmes.py'), run_name='__main__')
