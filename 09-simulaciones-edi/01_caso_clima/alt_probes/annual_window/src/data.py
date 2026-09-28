"""data.py — 01_caso_clima/alt_probes/annual_window

Sonda V (viscosidad/dependencia-instrumento): mismo observable (anomalia de
temperatura, detrended) y mismo dataset OWID que el caso base, pero se lee en
su resolucion NATIVA anual en vez de interpolar a mensual (instrumento de
integracion larga vs el instrumento de integracion corta del caso base).

Reusa fetch_real.fetch_owid_co2_temperature (el fetch/cache real) del caso
base y aplica el MISMO detrend lineal que fetch_real.load_real_data_annual,
pero sin la interpolacion mensual.
"""
import os
import sys

import numpy as np
import pandas as pd

_BASE_SRC = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "src"))
sys.path.insert(0, _BASE_SRC)

import fetch_real  # noqa: E402


def load_real_data(start_date, end_date, seed=42):
    start = pd.to_datetime(start_date)
    end = pd.to_datetime(end_date)
    start_year, end_year = start.year, end.year

    cache_dir = os.path.join(_BASE_SRC, "..", "data", "_cache")
    owid_cache = os.path.join(cache_dir, "owid_co2_temperature.csv")
    df = fetch_real.fetch_owid_co2_temperature(
        start_year=start_year, end_year=end_year, cache_path=owid_cache)
    if df is None or df.empty:
        print("Note: OWID sin datos, sonda annual_window sin real phase")
        return None

    df = df.rename(columns={"temperature_change_from_co2": "value"})
    df["date"] = pd.to_datetime(df["year"].astype(int).astype(str) + "-01-01")

    # Mismo detrend lineal que fetch_real.load_real_data_annual, para
    # que la comparacion de EDI entre sondas no confunda "detrend" con
    # "ventana de agregacion".
    if len(df) > 2:
        x = np.arange(len(df), dtype=float)
        y = df["value"].values
        z = np.polyfit(x, y, 1)
        df["value"] = y - np.polyval(z, x)

    out = df[["date", "value", "co2"]].reset_index(drop=True)
    print(f"✓ Sonda annual_window: {len(out)} filas anuales (instrumento=ventana anual nativa)")
    return out
