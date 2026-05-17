"""data.py — Carga datos climáticos con fallback sintético robusto.

Real: Intenta OWID, con timeout fallback a dataset derivado sintético pero realista.
Sintético: Forcing radiativo progresivo (CO₂-like) con acoplamiento ODE.
"""

import os
import sys
from datetime import datetime

import pandas as pd
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))


def load_real_data(start_date, end_date, seed=42):
    """Carga datos climáticos reales (anual interpolado a mensual).
    
    Fallback: Dataset sintético realista si APIs fallan o timeout.
    """
    # Intentar fetch remoto
    try:
        from fetch_real import load_real_data_annual
        df = load_real_data_annual(start_date, end_date, seed=seed)
        if df is not None and not df.empty:
            print(f"✓ Real data loaded: {len(df)} months from OWID")
            return df
    except Exception as e:
        print(f"Note: Remote OWID unavailable ({type(e).__name__})")
    
    # Fallback: Dataset sintético realista (determinista)
    print(f"Using realistic synthetic dataset (deterministic seed={seed})")
    return make_realistic_synthetic(start_date, end_date, seed=seed)


def make_realistic_synthetic(start_date, end_date, seed=42):
    """Dataset sintético realista: trend + ciclo estacional.
    
    Simula temperatura global anomalía con forcing CO₂-correlacionado.
    Determinista: mismo seed → mismo resultado.
    """
    rng = np.random.default_rng(seed)
    
    # Parse dates
    start = pd.to_datetime(start_date)
    end = pd.to_datetime(end_date)
    
    dates = pd.date_range(start=start, end=end, freq="MS")
    n = len(dates)
    
    if n < 12:
        dates = pd.date_range(start=start, end=end, freq="YS")
        n = len(dates)
    
    t = np.arange(n)
    
    # Trend: 0.015°C/año (IPCC-like warming trend)
    trend = 0.015 * (t / 12)  # mensual
    
    # Seasonality: ±0.3°C ciclo anual
    season = 0.3 * np.sin(2 * np.pi * t / 12)
    
    # Noise blanco pequeño
    noise = rng.normal(0, 0.05, n)
    
    # Temperatura anomalía total (detrended por el modelo)
    temp_anom = trend + season + noise
    
    # CO2: 315 ppm (1959) → 420 ppm (2023), lineal
    co2_1959 = 315.0
    co2_2023 = 420.0
    start_ref = pd.Timestamp(1959, 1, 1)
    end_ref = pd.Timestamp(2023, 12, 31)
    
    if start >= start_ref and end <= end_ref:
        months_elapsed = np.arange(n)
        total_months = (end_ref - start_ref).days // 30
        co2_trend = co2_1959 + (co2_2023 - co2_1959) * (months_elapsed / total_months)
        # Agregar ciclo anual pequeño (~1 ppm)
        co2 = co2_trend + 0.5 * np.sin(2 * np.pi * t / 12)
    else:
        # Genérico si está fuera del rango
        co2 = 350 + 0.1 * t + rng.normal(0, 0.1, n)
    
    df = pd.DataFrame({
        'date': dates,
        'value': temp_anom,
        'co2': co2
    })
    
    return df


def make_synthetic(start_date, end_date, seed=101):
    """Sintético tradicional: forcing radiativo creciente (CO₂-like)."""
    rng = np.random.default_rng(seed)
    
    dates = pd.date_range(start=start_date, end=end_date, freq="MS")
    steps = len(dates)
    if steps < 5:
        dates = pd.date_range(start=start_date, end=end_date, freq="YS")
        steps = len(dates)

    forcing = [0.005 * t + 0.3 * np.sin(2 * np.pi * t / 12) for t in range(steps)]
    
    # Simple ODE simulation
    x = np.zeros(steps)
    x[0] = 0.0
    for t in range(1, steps):
        dx = -0.04 * x[t-1] + 0.015 * forcing[t-1]
        x[t] = x[t-1] + dx + rng.normal(0, 0.03)
    
    obs = x + rng.normal(0.0, 0.05, size=steps)

    df = pd.DataFrame({"date": dates, "value": obs})
    meta = {"ode_true": {"alpha": 0.04, "beta": 0.015}, "measurement_noise": 0.05}
    return df, meta
