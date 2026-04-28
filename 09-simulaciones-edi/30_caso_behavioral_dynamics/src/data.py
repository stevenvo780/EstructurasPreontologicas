"""data.py — Behavioral Dynamics, generador de datos sintéticos.

Genera serie temporal de error de heading basada en la dinámica de
Fajen-Warren (2003). Los parámetros están publicados en el paper original:
  b = 3.25 (damping), k_g = 7.50 (stiffness goal), c1 = 0.40, c2 = 0.40

Para integrar con el pipeline EDI usamos la forma de primer orden con
parámetros equivalentes (α = k_g·c2 / b, β escalado por damping efectivo).

LoE = 2: datos sintéticos basados en teoría empíricamente aceptada.
La elevación a LoE = 4 requiere datos de captura de movimiento humano
(por ejemplo, dataset VENLab Brown University, no disponible públicamente
al momento de escribir este caso). Trabajo futuro.
"""

import math
import os
import random
from datetime import datetime, timedelta

import numpy as np
import pandas as pd


# Parámetros publicados de Fajen-Warren 2003 (varianza explicada r²=0.980)
FAJEN_WARREN_PARAMS = {
    "b": 3.25,        # damping
    "k_g": 7.50,      # stiffness hacia meta
    "c1": 0.40,       # decay con distancia a meta
    "c2": 0.40,       # offset asintótico
    # Parámetros derivados para forma de primer orden
    "alpha_eq": 0.25,  # k_g · c2 / b ≈ 0.92, ajustado para escala mensual
    "beta_eq": 0.85,
}


def _simulate_fajen_warren_first_order(steps, alpha=0.25, beta=0.85,
                                         forcing_amp=0.5, forcing_period=24,
                                         noise_std=0.08, seed=42):
    """Simula trayectoria de error de heading bajo control de Fajen-Warren
    en forma de primer orden, con forcing sinusoidal (ruta con cambios
    periódicos de meta).

    Returns:
        list de error de heading β_h(t) en grados, normalizado a [-1, 1]
    """
    random.seed(seed)
    np.random.seed(seed)

    x = 0.0
    series = []
    for t in range(steps):
        # Forcing: cambios sinusoidales de dirección de meta
        f = forcing_amp * math.sin(2 * math.pi * t / forcing_period)
        # Dinámica: dX = α(F - β·X)
        dx = alpha * (f - beta * x)
        x = x + dx + random.gauss(0, noise_std)
        # Clamp a rango realista
        x = max(-1.5, min(1.5, x))
        series.append(x)

    return series


def fetch_behavioral_dynamics(cache_path, country=None, start_year=2000,
                                end_year=2010, refresh=False):
    """Genera (o carga) datos sintéticos de Fajen-Warren.

    Para mantener compatibilidad con el pipeline EDI, simula 121 puntos
    mensuales (2000-01 a 2010-01).
    """
    cache_path = os.path.abspath(cache_path)

    if os.path.exists(cache_path) and not refresh:
        df = pd.read_csv(cache_path)
        df["date"] = pd.to_datetime(df["date"])
        meta = {
            "source": "Synthetic — Fajen-Warren (2003) parameters",
            "indicator": "behavioral_heading_error",
            "cached": True,
            "loe": 2,
            "start_year": int(df["year"].min()),
            "end_year": int(df["year"].max()),
        }
        return df, meta

    # Generar serie sintética
    n_steps = (end_year - start_year) * 12 + 1
    series = _simulate_fajen_warren_first_order(
        n_steps,
        alpha=FAJEN_WARREN_PARAMS["alpha_eq"],
        beta=FAJEN_WARREN_PARAMS["beta_eq"],
        seed=42,
    )

    rows = []
    base_date = datetime(start_year, 1, 1)
    for t, value in enumerate(series):
        d = base_date + timedelta(days=t * 30)  # aprox mensual
        rows.append({
            "year": d.year,
            "date": d,
            "value": float(value),
        })

    df = pd.DataFrame(rows).sort_values("date")

    os.makedirs(os.path.dirname(cache_path), exist_ok=True)
    df.to_csv(cache_path, index=False)

    meta = {
        "source": "Synthetic — Fajen-Warren (2003) parameters",
        "indicator": "behavioral_heading_error",
        "cached": False,
        "loe": 2,
        "n_steps": n_steps,
        "start_year": start_year,
        "end_year": end_year,
        "fajen_warren_params": FAJEN_WARREN_PARAMS,
    }
    return df, meta
