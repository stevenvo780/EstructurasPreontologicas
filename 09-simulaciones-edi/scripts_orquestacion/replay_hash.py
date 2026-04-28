#!/usr/bin/env python3
"""Compat wrapper. Usa repos/scripts/audit/replay_hash.py."""
import runpy
from pathlib import Path
runpy.run_path(str(Path(__file__).resolve().parent / 'audit' / 'replay_hash.py'), run_name='__main__')
