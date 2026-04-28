"""baselines.py — Comparación contra modelos estadísticos puros.

Implementa ARIMA, VAR y Random Walk como baselines comparativos del aparato
ABM+ODE acoplado. La filosofía es operar sobre las series sintéticas que cada
caso del corpus EDI genera durante su fase synthetic (esa es la fase donde la
métrica EDI se reporta), y comparar el RMSE de validación contra el RMSE_coupled
del aparato ya disponible en outputs/metrics.json.

El propósito de este módulo no es predicción óptima sino discriminar si el
aparato aporta algo más que un modelo estadístico genérico.
"""

from __future__ import annotations

import json
import os
import warnings
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np

warnings.filterwarnings("ignore")


def _gen_forcing(steps: int, fcfg: dict, seed: int = 42) -> np.ndarray:
    """Reproduce el forcing exógeno usado por cada caso del corpus.

    Soporta dos formas: linear_cycle y oscillator (las dos formas usadas en
    el corpus). Si fcfg es vacío usa un linear_cycle por defecto.
    """
    rng = np.random.default_rng(seed)
    ftype = fcfg.get("type", "linear_cycle")
    base = float(fcfg.get("base", 0.0))
    slope = float(fcfg.get("slope", 0.05))
    cycle_amp = float(fcfg.get("cycle_amp", 0.2))
    cycle_period = float(fcfg.get("cycle_period", 20))
    noise_std = float(fcfg.get("noise_std", 0.03))
    t = np.arange(steps)
    if ftype == "oscillator":
        f = base + cycle_amp * np.sin(2 * np.pi * t / cycle_period)
    else:
        f = base + slope * t + cycle_amp * np.sin(2 * np.pi * t / cycle_period)
    f = f + rng.normal(0.0, noise_std, size=steps)
    return f


def _gen_series_with_coupling(forcing: np.ndarray, params: dict,
                              seed: int = 42) -> np.ndarray:
    """Genera la serie observada con acoplamiento ODE a partir del forcing.

    Modelo simple equivalente al sintético del corpus: y_{t+1} = damping*y_t
    + alpha*(beta*forcing_t - y_t) + ruido. Esto reproduce la dinámica
    coupled de la fase synthetic estándar.
    """
    rng = np.random.default_rng(seed)
    n = len(forcing)
    alpha = float(params.get("ode_alpha", 0.4))
    beta = float(params.get("ode_beta", 0.8))
    damping = float(params.get("damping", 0.95))
    sigma = float(params.get("ode_noise", 0.05))
    y = np.zeros(n)
    y[0] = float(params.get("y0", 0.0))
    for t in range(n - 1):
        drive = beta * forcing[t]
        y[t + 1] = damping * y[t] + alpha * (drive - y[t]) + rng.normal(0.0, sigma)
    return y


def fit_arima(train: np.ndarray, val_steps: int,
              orders: Optional[List[Tuple[int, int, int]]] = None) -> dict:
    """Selección por AIC entre órdenes razonables y forecast a val_steps."""
    from statsmodels.tsa.arima.model import ARIMA
    if orders is None:
        orders = [(p, d, q) for p in range(0, 4) for d in (0, 1) for q in range(0, 4)
                  if not (p == 0 and q == 0)]
    best = {"aic": np.inf, "order": None, "forecast": None}
    for order in orders:
        try:
            m = ARIMA(train, order=order).fit()
            if m.aic < best["aic"]:
                fc = m.forecast(steps=val_steps)
                best = {"aic": float(m.aic), "order": order,
                        "forecast": np.asarray(fc, dtype=float)}
        except Exception:
            continue
    return best


def fit_var(train_multivar: np.ndarray, val_steps: int,
            max_lag: int = 5) -> dict:
    """VAR multivariado con selección por AIC sobre lag, forecast a val_steps."""
    from statsmodels.tsa.api import VAR
    best = {"aic": np.inf, "lag": None, "forecast": None}
    n_vars = train_multivar.shape[1]
    for lag in range(1, max_lag + 1):
        if lag >= train_multivar.shape[0] // 4:
            break
        try:
            m = VAR(train_multivar).fit(maxlags=lag, ic=None)
            aic = float(m.aic)
            if aic < best["aic"]:
                fc = m.forecast(train_multivar[-lag:], steps=val_steps)
                best = {"aic": aic, "lag": lag,
                        "forecast": np.asarray(fc[:, 0], dtype=float)}
        except Exception:
            continue
    return best


def random_walk_forecast(train: np.ndarray, val_steps: int) -> np.ndarray:
    last = train[-1]
    return np.full(val_steps, last, dtype=float)


def fit_gaussian_process(train: np.ndarray, val_steps: int) -> dict:
    """GP no-paramétrico con kernel temporal RBF. Baseline no-lineal flexible."""
    from sklearn.gaussian_process import GaussianProcessRegressor
    from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C, WhiteKernel
    n = len(train)
    X = np.arange(n).reshape(-1, 1).astype(float)
    y = train.astype(float)
    kernel = C(1.0, (1e-3, 1e3)) * RBF(length_scale=10.0, length_scale_bounds=(1e-1, 1e3)) \
        + WhiteKernel(noise_level=1e-2, noise_level_bounds=(1e-5, 1e0))
    try:
        gp = GaussianProcessRegressor(kernel=kernel, normalize_y=True,
                                      n_restarts_optimizer=2, random_state=42)
        gp.fit(X, y)
        Xtest = np.arange(n, n + val_steps).reshape(-1, 1).astype(float)
        fc = gp.predict(Xtest)
        return {"forecast": np.asarray(fc, dtype=float),
                "kernel": str(gp.kernel_)}
    except Exception as exc:
        return {"forecast": None, "error": str(exc)}


def rmse(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.sqrt(np.mean((np.asarray(a) - np.asarray(b)) ** 2)))


def run_baselines_on_case(case_dir: Path, seed: int = 42) -> dict:
    """Ejecuta ARIMA, VAR y RW sobre la fase sintética de un caso.

    Genera la serie usando los parámetros del case_config.json (los mismos
    que produce la fase synthetic del aparato), divide train/val con la misma
    proporción que usa el caso, ajusta cada baseline y reporta RMSE.

    Devuelve dict con todos los RMSE y las métricas comparativas frente al
    RMSE_coupled disponible en metrics.json.
    """
    cfg_path = case_dir / "case_config.json"
    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    syn = cfg.get("synthetic", {})
    fcfg = syn.get("forcing", {})
    tparams = syn.get("true_params", {})
    metrics_path = case_dir / "outputs" / "metrics.json"
    metrics = json.loads(metrics_path.read_text(encoding="utf-8")) if metrics_path.exists() else {}

    syn_phase = metrics.get("phases", {}).get("synthetic", {})
    val_steps = int(syn_phase.get("data", {}).get("val_steps", 20))
    total_steps = int(syn_phase.get("data", {}).get("steps", 40))
    if total_steps <= val_steps + 5:
        total_steps = val_steps + 30
    train_steps = total_steps - val_steps

    forcing = _gen_forcing(total_steps, fcfg, seed=seed)
    series = _gen_series_with_coupling(forcing, tparams, seed=seed)

    train = series[:train_steps]
    val = series[train_steps:]

    arima = fit_arima(train, val_steps)
    var_data = np.column_stack([series, forcing])[:train_steps]
    var = fit_var(var_data, val_steps, max_lag=min(5, train_steps // 4))
    rw = random_walk_forecast(train, val_steps)
    gp = fit_gaussian_process(train, val_steps)

    rmse_arima = rmse(arima["forecast"], val) if arima["forecast"] is not None else float("nan")
    rmse_var = rmse(var["forecast"], val) if var["forecast"] is not None else float("nan")
    rmse_rw = rmse(rw, val)
    rmse_gp = rmse(gp["forecast"], val) if gp.get("forecast") is not None else float("nan")

    rmse_coupled = float(syn_phase.get("errors", {}).get("rmse_abm", float("nan")))
    rmse_no_ode = float(syn_phase.get("errors", {}).get("rmse_abm_no_ode", float("nan")))

    edi = float(syn_phase.get("edi", {}).get("value", float("nan")))

    return {
        "case_dir": str(case_dir.name),
        "case_name": cfg.get("case_name", case_dir.name),
        "ode_model": cfg.get("ode_model"),
        "train_steps": train_steps,
        "val_steps": val_steps,
        "rmse_coupled_aparato": rmse_coupled,
        "rmse_no_ode_aparato": rmse_no_ode,
        "edi_aparato": edi,
        "rmse_arima": rmse_arima,
        "arima_order": arima.get("order"),
        "rmse_var": rmse_var,
        "var_lag": var.get("lag"),
        "rmse_rw": rmse_rw,
        "rmse_gp": rmse_gp,
        "gp_kernel": gp.get("kernel"),
        "ratio_arima_vs_coupled": rmse_arima / rmse_coupled if rmse_coupled and not np.isnan(rmse_arima) else None,
        "ratio_var_vs_coupled": rmse_var / rmse_coupled if rmse_coupled and not np.isnan(rmse_var) else None,
        "ratio_rw_vs_coupled": rmse_rw / rmse_coupled if rmse_coupled else None,
        "ratio_gp_vs_coupled": rmse_gp / rmse_coupled if rmse_coupled and not np.isnan(rmse_gp) else None,
        "winner": _pick_winner(rmse_coupled, rmse_arima, rmse_var, rmse_rw, rmse_gp),
    }


def _pick_winner(rmse_coupled, rmse_arima, rmse_var, rmse_rw, rmse_gp=None):
    """Veredicto cualitativo: qué modelo tiene menor RMSE."""
    options = {
        "ABM+ODE coupled": rmse_coupled,
        "ARIMA": rmse_arima,
        "VAR": rmse_var,
        "Random Walk": rmse_rw,
        "Gaussian Process": rmse_gp,
    }
    valid = {k: v for k, v in options.items() if v is not None and not np.isnan(v)}
    if not valid:
        return None
    return min(valid, key=valid.get)


def write_report(results: List[dict], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(results, indent=2, ensure_ascii=False, default=str),
                        encoding="utf-8")


if __name__ == "__main__":
    import sys
    repo = Path(__file__).resolve().parents[2]
    cases = sys.argv[1:] or [
        "04_caso_energia",
        "16_caso_deforestacion",
        "20_caso_kessler",
        "27_caso_riesgo_biologico",
        "24_caso_microplasticos",
        "06_caso_falsacion_exogeneidad",
        "07_caso_falsacion_no_estacionariedad",
        "08_caso_falsacion_observabilidad",
    ]
    results = []
    for c in cases:
        case_dir = repo / "09-simulaciones-edi" / c
        if not case_dir.exists():
            print(f"SKIP {c}: not found")
            continue
        try:
            r = run_baselines_on_case(case_dir)
            results.append(r)
            print(f"{r['case_dir']:42s}  ARIMA={r['rmse_arima']:.4f}  VAR={r['rmse_var']:.4f}  RW={r['rmse_rw']:.4f}  GP={r['rmse_gp']:.4f}  coupled={r['rmse_coupled_aparato']:.4f}  winner={r['winner']}")
        except Exception as exc:
            print(f"FAIL {c}: {exc}")
            import traceback; traceback.print_exc()
    out = repo / "09-simulaciones-edi" / "baselines" / "results.json"
    write_report(results, out)
    print(f"\nReport written to: {out}")
