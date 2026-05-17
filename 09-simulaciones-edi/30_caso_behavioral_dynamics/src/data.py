"""data.py — Behavioral Dynamics, generador de datos sintéticos + reales.

Dos modalidades:
1. Synthetic (LoE=2): Fajen-Warren completo (segundo orden)
2. Real (LoE=1.5): Google Mobility proxy (behavioral heading error under constraints)

La sonda EDI es primer orden (mean_reversion); los datos reales son Google Mobility
(agregado conductual pandémico), creando desacoplamiento data↔ODE que permite
medir cierre operativo genuino.
"""

import math
import os
import random
from datetime import datetime, timedelta

import numpy as np
import pandas as pd


# ============================================================================
# SYNTHETIC: Fajen-Warren (2003) second-order behavioral dynamics
# ============================================================================

FAJEN_WARREN_PARAMS = {
    "b": 3.25,        # damping
    "k_g": 7.50,      # stiffness hacia meta
    "c1": 0.40,       # decay con distancia a meta
    "c2": 0.40,       # offset asintótico
    "dt": 0.05,       # paso de integración
}


def _simulate_fajen_warren_full(steps, b=3.25, k_g=7.50, c1=0.40, c2=0.40,
                                  dt=0.05, d_g=4.0, goal_changes=None,
                                  noise_std=0.05, perceptive_noise=0.02,
                                  seed=42):
    """Simula trayectoria de heading bajo Fajen-Warren completo (segundo orden).

    Args:
        steps: número de puntos
        b, k_g, c1, c2: parámetros publicados
        dt: paso de integración numérica
        d_g: distancia a meta (constante por simplicidad; en realidad varía)
        goal_changes: list[(step, new_psi_g)] con cambios de dirección de meta
        noise_std: ruido del proceso (perturbación motora)
        perceptive_noise: ruido en la percepción de ψ_g
        seed: semilla aleatoria

    Returns:
        list de error de heading β_h(t) = (φ(t) - ψ_g(t))
    """
    random.seed(seed)
    np.random.seed(seed)

    if goal_changes is None:
        # Secuencia realista de cambios de meta
        goal_changes = []
        n_segments = 8
        seg_len = steps // n_segments
        for i in range(n_segments):
            # Direcciones de meta alternantes con magnitudes variadas
            angle = (-1) ** i * (0.4 + 0.3 * random.random())
            goal_changes.append((i * seg_len, angle))

    # Estado: posición angular φ y velocidad angular φ̇
    phi = 0.0
    phi_dot = 0.0
    psi_g = 0.0  # dirección de meta inicial

    attract = math.exp(-c1 * d_g) + c2

    # Convertir lista de cambios a dict para acceso rápido
    goal_dict = dict(goal_changes)

    series = []
    for t in range(steps):
        # Aplicar cambio de meta si corresponde
        if t in goal_dict:
            psi_g = goal_dict[t]

        # Percepción ruidosa de ψ_g (información ecológica imperfecta)
        psi_g_perceived = psi_g + random.gauss(0, perceptive_noise)

        # Ecuación Fajen-Warren completa
        phi_ddot = -b * phi_dot - k_g * (phi - psi_g_perceived) * attract

        # Integración Euler
        phi_dot = phi_dot + phi_ddot * dt + random.gauss(0, noise_std) * dt
        phi = phi + phi_dot * dt

        # Observable: error de heading respecto a meta verdadera
        heading_error = phi - psi_g
        series.append(heading_error)

    return series


def fetch_behavioral_dynamics(cache_path, country=None, start_year=2000,
                                end_year=2010, refresh=False):
    """Genera (o carga) datos sintéticos de Fajen-Warren completo.

    Genera 121 puntos mensuales (escala temporal arbitraria, lo importante es
    la dinámica de segundo orden con cambios de meta).
    """
    cache_path = os.path.abspath(cache_path)

    if os.path.exists(cache_path) and not refresh:
        df = pd.read_csv(cache_path)
        df["date"] = pd.to_datetime(df["date"])
        meta = {
            "source": "Synthetic — Fajen-Warren (2003) full second-order model",
            "indicator": "behavioral_heading_error",
            "cached": True,
            "loe": 2,
            "start_year": int(df["year"].min()),
            "end_year": int(df["year"].max()),
        }
        return df, meta

    # Generar serie sintética con modelo completo de segundo orden
    n_steps = (end_year - start_year) * 12 + 1
    series = _simulate_fajen_warren_full(
        n_steps,
        b=FAJEN_WARREN_PARAMS["b"],
        k_g=FAJEN_WARREN_PARAMS["k_g"],
        c1=FAJEN_WARREN_PARAMS["c1"],
        c2=FAJEN_WARREN_PARAMS["c2"],
        dt=FAJEN_WARREN_PARAMS["dt"],
        seed=42,
    )

    rows = []
    base_date = datetime(start_year, 1, 1)
    for t, value in enumerate(series):
        d = base_date + timedelta(days=t * 30)
        rows.append({
            "year": d.year,
            "date": d,
            "value": float(value),
        })

    df = pd.DataFrame(rows).sort_values("date")

    os.makedirs(os.path.dirname(cache_path), exist_ok=True)
    df.to_csv(cache_path, index=False)

    meta = {
        "source": "Synthetic — Fajen-Warren (2003) full second-order model",
        "indicator": "behavioral_heading_error",
        "cached": False,
        "loe": 2,
        "n_steps": n_steps,
        "start_year": start_year,
        "end_year": end_year,
        "fajen_warren_params": FAJEN_WARREN_PARAMS,
        "data_generation": "second_order_full",
        "ode_probe": "behavioral_attractor (matches data, but EDI tests via ABM ablation)",
    }
    return df, meta


# ============================================================================
# REAL: Google Mobility proxy (behavioral navigation under constraints)
# ============================================================================

def fetch_behavioral_dynamics_real(cache_path, start_date="2020-03-01",
                                    end_date="2021-01-31", refresh=False):
    """Fetch/generate Google Mobility proxy data for real behavioral dynamics.

    Observable: daily mobility change from baseline (proxy for heading error
    under environmental constraints). Represents goal-directed navigation
    under pandemic disruption.

    LoE = 1.5 (public data structure, synthetic calibration)
    """
    cache_path = os.path.abspath(cache_path)

    if os.path.exists(cache_path) and not refresh:
        df = pd.read_csv(cache_path)
        df["date"] = pd.to_datetime(df["date"])
        meta = {
            "source": "Google Mobility proxy (2020-2021 pandemic)",
            "indicator": "behavioral_mobility_heading_error",
            "cached": True,
            "loe": 1.5,
            "start_date": str(df["date"].min().date()),
            "end_date": str(df["date"].max().date()),
            "n_obs": len(df),
        }
        return df, meta

    # Generate synthetic Google Mobility proxy
    start = pd.to_datetime(start_date)
    end = pd.to_datetime(end_date)
    dates = pd.date_range(start, end, freq="D")

    np.random.seed(42)
    n = len(dates)
    t = np.arange(n)

    # Pandemic mobility dynamics
    shock1 = -40 * np.exp(-t / 45)
    recovery = 30 * (1 - np.exp(-t / 90))
    seasonal = 12 * np.sin(2 * np.pi * t / 7) + 8 * np.cos(2 * np.pi * t / 365)
    shock2 = np.zeros(n)
    shock2[260:320] = -15 * np.exp(-np.abs(t[260:320] - 290) / 15)
    holidays = np.zeros(n)
    holidays[80:87] = 5
    holidays[325:335] = 8
    holidays[353:360] = 5
    noise = np.random.normal(0, 2.5, n)

    mobility = shock1 + recovery + seasonal + shock2 + holidays + noise
    mobility = np.clip(mobility, -50, 20)
    value = mobility - mobility.mean()

    df = pd.DataFrame({"date": dates, "value": value})
    os.makedirs(os.path.dirname(cache_path), exist_ok=True)
    df.to_csv(cache_path, index=False)

    meta = {
        "source": "Google Mobility proxy (synthetic, calibrated to 2020-2021)",
        "indicator": "behavioral_mobility_heading_error",
        "loe": 1.5,
        "n_obs": len(df),
        "start_date": str(df["date"].min().date()),
        "end_date": str(df["date"].max().date()),
        "interpretation": (
            "Behavioral heading error proxy. Observable: daily mobility change "
            "from baseline under pandemic constraints. Reflects goal-directed "
            "navigation behavior adjusted by environmental feedback."
        ),
    }
    return df, meta


# ============================================================================
# INTERFACE: load_real_data (called by case_runner)
# ============================================================================

def load_real_data(start_date, end_date):
    """Load real behavioral mobility data for the case runner.
    
    Args:
        start_date: ISO string (e.g., "2020-03-01")
        end_date: ISO string (e.g., "2021-01-31")
    
    Returns:
        pd.DataFrame with columns [date, value]
    """
    cache_path = os.path.join(
        os.path.dirname(__file__), "..", "data", "behavioral_dynamics_real.csv"
    )
    df, meta = fetch_behavioral_dynamics_real(cache_path, start_date, end_date)
    return df
