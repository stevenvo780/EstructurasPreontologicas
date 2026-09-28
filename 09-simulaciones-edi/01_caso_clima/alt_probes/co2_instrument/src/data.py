"""data.py — 01_caso_clima/alt_probes/co2_instrument

Sonda V (viscosidad/dependencia-instrumento): mismo dataset OWID CO2+temperatura
que el caso base, pero el OBSERVABLE primario ahora es la concentracion de CO2
(sonda de composicion atmosferica) en vez de la temperatura (sonda termometrica).
La anomalia de temperatura detrended pasa a ser el driver exogeno.

Reusa fetch_real.py del caso base (01_caso_clima/src) para no duplicar el fetch
real ni introducir un dataset distinto — solo cambia que columna se lee como
"value" (el instrumento) y cual como driver.
"""
import os
import sys

_BASE_SRC = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "src"))
sys.path.insert(0, _BASE_SRC)

import fetch_real  # noqa: E402


def load_real_data(start_date, end_date, seed=42):
    df = fetch_real.load_real_data_annual(start_date, end_date, seed=seed)
    if df is None or df.empty:
        print("Note: fetch_real sin datos, sonda co2_instrument sin real phase")
        return None

    out = df.rename(columns={"value": "temp_anom"})
    if "co2" not in out.columns:
        raise ValueError("co2_instrument requiere columna 'co2' en fetch_real")
    out["value"] = out["co2"]
    out = out[["date", "value", "temp_anom"]]
    print(f"✓ Sonda co2_instrument: {len(out)} filas (instrumento=CO2, driver=temp_anom)")
    return out
