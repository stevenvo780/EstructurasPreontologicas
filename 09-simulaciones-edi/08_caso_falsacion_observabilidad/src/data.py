"""data.py — Caso 08: Falsación por Observabilidad Escasa.

Genera datos sintéticos de "causa común" (confounder) para probar que
el framework rechaza un driver insuficiente.

Diseño:
    Z(t)  = 0.05·t + 2·sin(0.5·t)       # causa oculta: tendencia + oscilación
    Y(t)  = Z(t) + ε_Y                   # target: realidad completa
    X(t)  = 0.05·t + ε_X                 # driver: solo tendencia (proxy pobre)

ρ(X, Y) alto (tendencia compartida), pero X carece de la componente
de alta frecuencia sin(0.5·t) que domina la dinámica de Y.

Parámetros:
    trend_slope  = 0.05 u/mes     (tendencia lineal)
    osc_ampl     = 2.0            (amplitud oscilación rápida)
    osc_freq     = 0.5 rad/mes    (T ≈ 12.6 meses)
    σ_Y          = 0.2            (ruido target)
    σ_X          = 0.1            (ruido driver)
"""

import os

import numpy as np
import pandas as pd


def fetch_sparse_happiness(cache_path, start_year=2005, end_year=2023, seed=42,
                           freq="MS"):
    """Genera datos sintéticos confounder: target con oscilación oculta,
    driver que solo captura la tendencia.

    Defaults = CSV canónico (217 filas mensuales 2005-2023, seed 42) que
    respalda outputs/metrics.json. Ver __main__ para regenerar el caché.
    """
    rng = np.random.default_rng(seed)

    dates = pd.date_range(start=f"{start_year}-01-01",
                          end=f"{end_year}-01-01", freq=freq)
    n = len(dates)
    t = np.arange(n, dtype=float)

    # Causa oculta Z: tendencia + oscilación rápida
    trend = 0.05 * t                        # 0.05 u/mes
    fast_osc = 2.0 * np.sin(0.5 * t)        # T ≈ 12.6 meses
    Z = trend + fast_osc

    # Target Y: realidad completa + ruido
    Y = Z + rng.normal(0.0, 0.2, n)

    # Driver X: solo tendencia (proxy insuficiente)
    X = trend + rng.normal(0.0, 0.1, n)

    df = pd.DataFrame({
        "date": dates,
        "value": Y,
        "insufficient_driver": X,
        "hidden_cause": Z,
    })

    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        df.to_csv(cache_path, index=False)

    meta = {"source": "Synthetic Confounder", "start_year": start_year,
            "end_year": end_year}
    return df, meta


if __name__ == "__main__":
    # Regenera el caché ignorado por git con los parámetros canónicos
    # (verificado 2026-09-28: reproduce outputs/metrics.json bit-idéntico).
    _here = os.path.dirname(os.path.abspath(__file__))
    _csv = os.path.join(_here, "..", "data", "sparse_happiness.csv")
    _df, _ = fetch_sparse_happiness(_csv)
    print(f"OK: {os.path.abspath(_csv)} ({len(_df)} filas)")

