#!/usr/bin/env python3
"""run_coupling.py — par deforestacion -> clima (temperatura regional)

Eje N (No-localidad): mide si la temperatura regional (01_caso_clima) se
predice mejor fuera de muestra agregando la deforestacion (16_caso_deforestacion)
como driver rezagado, mas alla de su propia autorregresion. Ver common_coupling.py
para la definicion del proxy honesto (reduccion de RMSE OLS AR1 con vs sin driver).

Series: ambas anuales, superpuestas en 1992-2022 (deforestacion World Bank
% cobertura forestal; clima temperatura OWID temperature_change_from_co2 anual,
mismo fetch/cache que 01_caso_clima/src/fetch_real.py).
"""
import json
import os
import sys

SIM_DIR = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # _coupling/
sys.path.insert(0, os.path.join(SIM_DIR, "01_caso_clima", "src"))

from common_coupling import compute_coupling_edi, load_annual_csv  # noqa: E402
import fetch_real  # noqa: E402

DEFOR_CSV = os.path.join(SIM_DIR, "16_caso_deforestacion", "data", "wb_deforestation.csv")
CLIMA_CACHE = os.path.join(SIM_DIR, "01_caso_clima", "data", "_cache", "owid_co2_temperature.csv")


def main():
    defor = load_annual_csv(DEFOR_CSV, rename_to="deforestacion")

    clima_raw = fetch_real.fetch_owid_co2_temperature(start_year=1990, end_year=2024, cache_path=CLIMA_CACHE)
    clima = clima_raw.rename(columns={"temperature_change_from_co2": "temp_regional"})[["year", "temp_regional"]]

    merged = defor.merge(clima, on="year", how="inner").sort_values("year").reset_index(drop=True)

    result = compute_coupling_edi(merged, target_col="temp_regional", driver_col="deforestacion")
    result["pair"] = {"a": "16_caso_deforestacion", "b": "01_caso_clima (temp regional)"}
    result["years_overlap"] = [int(merged["year"].min()), int(merged["year"].max())] if len(merged) else None

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs", "coupling_metrics.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    print(f"\nEscrito {out_path}")


if __name__ == "__main__":
    main()
