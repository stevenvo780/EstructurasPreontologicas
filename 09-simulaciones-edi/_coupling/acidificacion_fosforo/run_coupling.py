#!/usr/bin/env python3
"""run_coupling.py — par acidificacion oceanica -> fosforo

Eje N (No-localidad): mide si el fosforo (22_caso_fosforo, consumo de
fertilizante) se predice mejor fuera de muestra agregando la acidificacion
oceanica (19_caso_acidificacion_oceanica, pH) como driver rezagado, mas alla
de su propia autorregresion. Ver common_coupling.py para la definicion del
proxy honesto (reduccion de RMSE OLS AR1 con vs sin driver).

Series: ambas anuales, superpuestas en 1990-2020 (acidificacion: pH oceanico
sintetico/real del caso 19; fosforo: consumo de fertilizante World Bank del
caso 22).
"""
import json
import os
import sys

SIM_DIR = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # _coupling/

from common_coupling import compute_coupling_edi, load_annual_csv  # noqa: E402

ACID_CSV = os.path.join(SIM_DIR, "19_caso_acidificacion_oceanica", "data", "dataset.csv")
FOSFORO_CSV = os.path.join(SIM_DIR, "22_caso_fosforo", "data", "wb_fertilizer_consumption.csv")


def main():
    acid = load_annual_csv(ACID_CSV, rename_to="ph_oceanico")
    fosforo = load_annual_csv(FOSFORO_CSV, rename_to="fosforo")

    merged = fosforo.merge(acid, on="year", how="inner").sort_values("year").reset_index(drop=True)

    result = compute_coupling_edi(merged, target_col="fosforo", driver_col="ph_oceanico")
    result["pair"] = {"a": "19_caso_acidificacion_oceanica", "b": "22_caso_fosforo"}
    result["years_overlap"] = [int(merged["year"].min()), int(merged["year"].max())] if len(merged) else None

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs", "coupling_metrics.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    print(f"\nEscrito {out_path}")


if __name__ == "__main__":
    main()
