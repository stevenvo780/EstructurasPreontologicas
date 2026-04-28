#!/usr/bin/env python3
"""Compat wrapper. Usa repos/scripts/audit/auditar_simulaciones.py."""
import runpy
from pathlib import Path
runpy.run_path(str(Path(__file__).resolve().parent / 'audit' / 'auditar_simulaciones.py'), run_name='__main__')
