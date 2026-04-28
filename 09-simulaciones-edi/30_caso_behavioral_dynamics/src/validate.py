"""validate.py — Behavioral Dynamics (Fajen-Warren 2003).

Caso 30 del corpus EDI. Conecta la iteración Steven (caso ancla canónico)
con la iteración Jacob (corpus EDI macro-temporal) bajo metodología
unificada.

Sonda ODE: mean_reversion (dinámica de Fajen-Warren forma de primer orden)
Datos: sintéticos basados en parámetros publicados (LoE=2)
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from case_runner import run_case

if __name__ == "__main__":
    run_case(os.path.dirname(os.path.abspath(__file__)))
