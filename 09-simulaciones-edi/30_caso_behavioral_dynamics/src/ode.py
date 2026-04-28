"""ode.py — Behavioral Dynamics ODE (sonda de segundo orden).

Sonda macro: dinámica completa de Fajen-Warren con dependencia exponencial
de distancia a meta y damping de segundo orden.

  φ̈ = -b·φ̇ - k_g·(φ - ψ_g)·(e^{-c1·d_g} + c2)

donde ψ_g se toma del forcing exógeno (cambios de dirección de meta) y
los parámetros b, k_g, c1, c2 son los publicados por Fajen-Warren (2003).
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from ode_models import simulate_ode_model

ODE_MODEL = "behavioral_attractor"
ODE_KEY = "heading_error"


def simulate_ode(params, steps, seed):
    p = dict(params)
    p["ode_model"] = ODE_MODEL
    if "ode_key" not in p:
        p["ode_key"] = ODE_KEY
    # Parámetros de Fajen-Warren si no están especificados
    p.setdefault("fw_b", 3.25)
    p.setdefault("fw_k_g", 7.50)
    p.setdefault("fw_c1", 0.40)
    p.setdefault("fw_c2", 0.40)
    p.setdefault("fw_d_g", 4.0)
    p.setdefault("fw_dt", 0.05)
    return simulate_ode_model(p, steps, seed=seed)
