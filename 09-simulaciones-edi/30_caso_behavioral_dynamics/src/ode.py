"""ode.py — Behavioral Dynamics ODE.

Sonda macro: dinámica de heading bajo control informacional.

Modelo: dX = α(F - β·X) donde
  X = error de heading β_h = (φ - ψ_g) [en grados]
  F = flujo óptico exógeno (forcing)
  α = ganancia de acoplamiento (Fajen-Warren k_g escalado)
  β = amortiguamiento del sistema sensoriomotor (Fajen-Warren b)

Esta es la versión simplificada de primer orden de la ecuación de
Fajen-Warren (2003):
  φ̈ = -b φ̇ - k_g(φ - ψ_g)(e^{-c1 d_g} + c2)

Para el corpus EDI usamos la forma de primer orden porque captura
la atracción a la meta y permite ablación limpia del acoplamiento
informacional macro→micro.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from ode_models import simulate_ode_model

ODE_MODEL = "mean_reversion"
ODE_KEY = "heading_error"


def simulate_ode(params, steps, seed):
    p = dict(params)
    p["ode_model"] = ODE_MODEL
    if "ode_key" not in p:
        p["ode_key"] = ODE_KEY
    return simulate_ode_model(p, steps, seed=seed)
