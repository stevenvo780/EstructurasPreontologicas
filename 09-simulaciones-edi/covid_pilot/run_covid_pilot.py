"""Caso piloto COVID-19 — adaptación EDI a la dimensión normativa institucional.

Aplica el aparato EDI a la dinámica de adopción de medidas no farmacéuticas
durante la pandemia, usando datos públicos del Oxford COVID-19 Government
Response Tracker (Hale et al. 2021). El propósito es probar el bloque 7
(dimensión normativa) de la auditoría doctoral con datos reales de validez,
legitimidad, efectividad institucional.

Variable observable: Stringency Index (índice agregado de severidad de
las respuestas gubernamentales, escala 0-100).

Sonda macro: institutional_inertia — modelo de cuenca de atracción de
cumplimiento institucional bajo perturbación externa (casos COVID).

Forcing exógeno: tasa de casos nuevos diarios suavizada.

Salida: outputs/metrics_covid_pilot.json
"""

from __future__ import annotations

import json
import os
from pathlib import Path

import numpy as np
import pandas as pd

REPO = Path(__file__).resolve().parents[2]
OUT = Path(__file__).parent / "outputs"
OUT.mkdir(parents=True, exist_ok=True)
CACHE = Path(__file__).parent / "data_cache"
CACHE.mkdir(parents=True, exist_ok=True)

# Países representativos (heterogeneidad de regímenes institucionales)
COUNTRIES = ["COL", "MEX", "ARG", "ESP", "DEU", "USA", "BRA", "CHL", "PER", "ITA"]


def fetch_oxford_data() -> pd.DataFrame:
    """Descarga del repositorio público Oxford OWID COVID Tracker."""
    cache_file = CACHE / "owid-covid.csv"
    if cache_file.exists():
        return pd.read_csv(cache_file, parse_dates=["date"])
    url = ("https://raw.githubusercontent.com/owid/covid-19-data/master/"
           "public/data/owid-covid-data.csv")
    print(f"  Fetching from {url} ...")
    df = pd.read_csv(url, parse_dates=["date"])
    cols = ["iso_code", "location", "date", "new_cases_smoothed",
            "stringency_index"]
    df = df[cols].dropna(subset=["stringency_index"])
    df.to_csv(cache_file, index=False)
    return df


def edi_for_series(observed: np.ndarray, modeled: np.ndarray,
                   control: np.ndarray, val_steps: int = 30) -> dict:
    """EDI = 1 - rmse_modeled/rmse_control + permutación + bootstrap."""
    obs_val = observed[-val_steps:]
    mod_val = modeled[-val_steps:]
    ctrl_val = control[-val_steps:]
    rmse_mod = float(np.sqrt(np.mean((obs_val - mod_val) ** 2)))
    rmse_ctrl = float(np.sqrt(np.mean((obs_val - ctrl_val) ** 2)))
    edi = 1.0 - rmse_mod / rmse_ctrl if rmse_ctrl > 1e-9 else None
    rng = np.random.default_rng(42)
    null_edis = []
    for _ in range(999):
        perm = rng.permutation(mod_val)
        rmse_p = float(np.sqrt(np.mean((obs_val - perm) ** 2)))
        if rmse_ctrl > 1e-9:
            null_edis.append(1.0 - rmse_p / rmse_ctrl)
    null_edis = np.asarray(null_edis)
    pvalue = float(np.mean(null_edis >= edi)) if edi is not None else None
    boot_edis = []
    for _ in range(500):
        idx = rng.integers(0, val_steps, size=val_steps)
        b_obs = obs_val[idx]
        b_mod = mod_val[idx]
        b_ctrl = ctrl_val[idx]
        rmse_m = np.sqrt(np.mean((b_obs - b_mod) ** 2))
        rmse_c = np.sqrt(np.mean((b_obs - b_ctrl) ** 2))
        if rmse_c > 1e-9:
            boot_edis.append(1.0 - rmse_m / rmse_c)
    if boot_edis:
        ci = (float(np.percentile(boot_edis, 2.5)),
              float(np.percentile(boot_edis, 97.5)))
    else:
        ci = None
    return {
        "edi": edi,
        "p_value": pvalue,
        "ci_95": ci,
        "rmse_modeled": rmse_mod,
        "rmse_control": rmse_ctrl,
        "val_steps": val_steps,
    }


def institutional_inertia_model(forcing: np.ndarray, train_obs: np.ndarray,
                                steps: int) -> np.ndarray:
    """Modelo dinámico institucional: cuenca de atracción del cumplimiento.

    Stringency_{t+1} = damping * Stringency_t + alpha * (target - Stringency_t)
                       + beta * forcing_t

    donde target es el régimen de cumplimiento de equilibrio bajo nivel de
    forcing. Damping captura la resistencia institucional al cambio (validez).
    Alpha captura la velocidad de respuesta (efectividad). El término del
    forcing captura la sensibilidad a la perturbación (anchura de la cuenca).
    """
    n = train_obs.size
    target = float(np.mean(train_obs))
    damping = 0.85
    alpha = 0.15
    # estimación rápida de beta por mínimos cuadrados
    diffs = np.diff(train_obs)
    drives = forcing[: n - 1]
    if np.var(drives) > 1e-9:
        beta = float(np.cov(diffs, drives)[0, 1] / np.var(drives))
    else:
        beta = 0.05
    s = float(train_obs[0])
    series = np.zeros(steps)
    series[0] = s
    for t in range(1, steps):
        s = damping * s + alpha * (target - s) + beta * forcing[t]
        series[t] = s
    return series


def run_country(df_country: pd.DataFrame) -> dict:
    """Ejecuta EDI para un país."""
    df = df_country.sort_values("date").reset_index(drop=True)
    df = df.dropna(subset=["new_cases_smoothed", "stringency_index"])
    if df.shape[0] < 100:
        return {"country": df_country["iso_code"].iloc[0], "skip": "insufficient data"}
    cases = df["new_cases_smoothed"].to_numpy(dtype=float)
    cases = (cases - cases.mean()) / (cases.std() + 1e-9)  # normalizado
    stringency = df["stringency_index"].to_numpy(dtype=float)

    n = stringency.size
    val_steps = max(20, n // 6)
    train_n = n - val_steps
    train_obs = stringency[:train_n]

    modeled = institutional_inertia_model(cases, train_obs, n)
    # control = mismo modelo SIN acoplamiento al forcing exógeno (ablación real)
    control = institutional_inertia_model(np.zeros_like(cases), train_obs, n)

    edi_res = edi_for_series(stringency, modeled, control, val_steps=val_steps)
    return {
        "country": df["iso_code"].iloc[0],
        "country_name": df["location"].iloc[0],
        "n_observations": int(n),
        **edi_res,
    }


def main():
    print("=== Caso piloto COVID-19 — dimensión normativa ===")
    print("Cargando datos del Oxford COVID Tracker (vía OWID) ...")
    try:
        df = fetch_oxford_data()
    except Exception as exc:
        print(f"FAIL fetch: {exc}")
        result = {"error": str(exc), "status": "fetch_failed"}
        out = OUT / "metrics_covid_pilot.json"
        out.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
        return

    results = []
    for iso in COUNTRIES:
        sub = df[df["iso_code"] == iso]
        if sub.empty:
            continue
        try:
            r = run_country(sub)
            results.append(r)
            edi = r.get("edi")
            p = r.get("p_value")
            print(f"  {iso}  n={r['n_observations']:5d}  "
                  f"EDI={edi:+.4f}  p={p:.4f}  CI={r.get('ci_95')}")
        except Exception as exc:
            print(f"FAIL {iso}: {exc}")

    edis = [r["edi"] for r in results if r.get("edi") is not None]
    summary = {
        "n_countries": len(results),
        "countries_with_signal": sum(1 for r in results
                                     if r.get("edi") is not None
                                     and r.get("p_value") is not None
                                     and r["edi"] > 0.10
                                     and r["p_value"] < 0.05),
        "edi_mean": float(np.mean(edis)) if edis else None,
        "edi_median": float(np.median(edis)) if edis else None,
        "edi_max": float(np.max(edis)) if edis else None,
        "results": results,
    }
    out_path = OUT / "metrics_covid_pilot.json"
    out_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False),
                        encoding="utf-8")
    print(f"\nResumen: {summary['countries_with_signal']}/{summary['n_countries']} países con EDI>0.10 y p<0.05")
    print(f"EDI mean = {summary.get('edi_mean')}")
    print(f"Results written to: {out_path}")


if __name__ == "__main__":
    main()
