"""validate.py — 01_caso_clima/alt_probes/annual_window

Usa case_runner.py centralizado + case_config.json declarativo (sonda V).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "common"))
from case_runner import run_case
if __name__ == "__main__":
    run_case(os.path.dirname(os.path.abspath(__file__)))
