#!/usr/bin/env python3
"""Compat wrapper. Usa repos/scripts/audit/_audit_fresh.py."""
import runpy
from pathlib import Path
runpy.run_path(str(Path(__file__).resolve().parent / 'audit' / '_audit_fresh.py'), run_name='__main__')
