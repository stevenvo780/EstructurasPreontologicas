"""data.py — 01_caso_clima/alt_probes/decadal_smoothed

Sonda V (viscosidad/dependencia-instrumento): mismo observable (temperatura),
mismo dataset OWID, misma resolucion mensual que el caso base, pero el
instrumento aplica un promedio movil centrado de 120 meses (~10 anios) antes
de leer el dato -- un sensor de banda ancha/baja frecuencia en vez del sensor
de banda estrecha (sin suavizar) del caso base.

Reusa fetch_real.load_real_data_annual (mismo fetch+detrend+interpolacion
mensual del caso base) y solo agrega el suavizado.
"""
import os
import sys

_BASE_SRC = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "src"))
sys.path.insert(0, _BASE_SRC)

import fetch_real  # noqa: E402

WINDOW_MONTHS = 120


def load_real_data(start_date, end_date, seed=42):
    df = fetch_real.load_real_data_annual(start_date, end_date, seed=seed)
    if df is None or df.empty:
        print("Note: fetch_real sin datos, sonda decadal_smoothed sin real phase")
        return None

    df = df.sort_values("date").reset_index(drop=True)
    win = min(WINDOW_MONTHS, max(3, len(df) // 2))
    df["value"] = df["value"].rolling(window=win, center=True, min_periods=1).mean()
    if "co2" in df.columns:
        df["co2"] = df["co2"].rolling(window=win, center=True, min_periods=1).mean()

    out = df[["date", "value", "co2"]] if "co2" in df.columns else df[["date", "value"]]
    print(f"✓ Sonda decadal_smoothed: {len(out)} filas (instrumento=promedio movil {win} meses)")
    return out
