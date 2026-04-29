"""
Baselines ARIMA / VAR / persistencia para los casos del corpus EDI con primary_arrays.json. — F15.

Compara el RMSE del modelo acoplado EDI (abm_coupled) contra:
  - persistencia (predicción = última observación de train)
  - ARIMA(1,1,1) univariado sobre obs
  - VAR(1) multivariado sobre [obs, forcing]
  - random walk con drift (np.cumsum)

Salida: 09-simulaciones-edi/baselines/baselines_report.{json,md}
"""
from __future__ import annotations
import json
import sys
import warnings
from pathlib import Path

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")

ROOT = Path(__file__).resolve().parent.parent
SIM_DIR = ROOT / "09-simulaciones-edi"
OUT_DIR = SIM_DIR / "baselines"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def rmse(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.sqrt(np.mean((y_true - y_pred) ** 2)))


def baseline_persistence(train: np.ndarray, val_len: int) -> np.ndarray:
    last = train[-1]
    return np.full(val_len, last)


def baseline_random_walk(train: np.ndarray, val_len: int, rng: np.random.Generator) -> np.ndarray:
    diffs = np.diff(train)
    drift = float(np.mean(diffs))
    sigma = float(np.std(diffs)) if len(diffs) > 1 else 0.0
    steps = rng.normal(drift, sigma, size=val_len)
    return train[-1] + np.cumsum(steps)


def baseline_arima(train: np.ndarray, val_len: int, order=(1, 1, 1)) -> np.ndarray | None:
    try:
        from statsmodels.tsa.arima.model import ARIMA
        model = ARIMA(train, order=order, enforce_stationarity=False, enforce_invertibility=False)
        fit = model.fit(method_kwargs={"warn_convergence": False})
        return np.asarray(fit.forecast(steps=val_len))
    except Exception as e:
        print(f"  ARIMA failed: {e}", file=sys.stderr)
        return None


def baseline_var(train_obs: np.ndarray, train_forcing: np.ndarray, val_len: int,
                 forcing_val: np.ndarray) -> np.ndarray | None:
    try:
        from statsmodels.tsa.api import VAR
        train_df = pd.DataFrame({"obs": train_obs, "forcing": train_forcing})
        diffs = train_df.diff().dropna()
        if len(diffs) < 10:
            return None
        model = VAR(diffs)
        fit = model.fit(maxlags=2, ic="aic", trend="c")
        forecast_diff = fit.forecast(diffs.values[-fit.k_ar:], steps=val_len)
        last_obs = train_obs[-1]
        preds = last_obs + np.cumsum(forecast_diff[:, 0])
        return preds
    except Exception as e:
        print(f"  VAR failed: {e}", file=sys.stderr)
        return None


def load_metrics_rmse(case_dir: Path) -> tuple[float | None, float | None, int | None]:
    metrics_file = case_dir / "outputs" / "metrics.json"
    if not metrics_file.exists():
        return None, None, None
    with open(metrics_file) as f:
        m = json.load(f)
    syn = m.get("phases", {}).get("synthetic") or {}
    err = syn.get("errors", {})
    val_steps = syn.get("data", {}).get("val_steps")
    return err.get("rmse_abm"), err.get("rmse_abm_no_ode"), val_steps


def process_case(case_dir: Path) -> dict | None:
    arr_file = case_dir / "outputs" / "primary_arrays.json"
    if not arr_file.exists():
        return None
    with open(arr_file) as f:
        data = json.load(f)
    arrays = data.get("arrays", {})
    obs = np.asarray(arrays.get("obs", []), dtype=float)
    abm_coupled = np.asarray(arrays.get("abm_coupled", []), dtype=float)
    abm_no_ode = np.asarray(arrays.get("abm_no_ode", []), dtype=float)
    forcing = np.asarray(arrays.get("forcing", []), dtype=float)
    n = len(obs)
    if n < 30 or len(abm_coupled) != n:
        return {"case_id": case_dir.name, "skip_reason": f"n={n} or array mismatch"}

    rmse_coupled_meta, rmse_no_ode_meta, val_steps_meta = load_metrics_rmse(case_dir)
    val_len = val_steps_meta if val_steps_meta and val_steps_meta < n else max(int(n * 0.3), 5)
    train_len = n - val_len
    if train_len < 20:
        return {"case_id": case_dir.name, "skip_reason": f"train_len={train_len} too small"}

    obs_train, obs_val = obs[:train_len], obs[train_len:]
    forcing_train, forcing_val = forcing[:train_len] if forcing.size == n else None, forcing[train_len:] if forcing.size == n else None

    rng = np.random.default_rng(seed=42)
    results = {
        "case_id": case_dir.name,
        "n": n,
        "train_len": train_len,
        "val_len": val_len,
        "rmse": {},
        "edi_vs_baseline": {},
    }

    pred_persist = baseline_persistence(obs_train, val_len)
    results["rmse"]["persistence"] = rmse(obs_val, pred_persist)

    pred_rw = baseline_random_walk(obs_train, val_len, rng)
    results["rmse"]["random_walk"] = rmse(obs_val, pred_rw)

    pred_arima = baseline_arima(obs_train, val_len, order=(1, 1, 1))
    if pred_arima is not None and len(pred_arima) == val_len:
        results["rmse"]["arima_1_1_1"] = rmse(obs_val, pred_arima)
    else:
        pred_arima = baseline_arima(obs_train, val_len, order=(1, 0, 1))
        if pred_arima is not None and len(pred_arima) == val_len:
            results["rmse"]["arima_1_0_1"] = rmse(obs_val, pred_arima)

    if forcing_train is not None and len(forcing_train) == train_len and len(forcing_val) == val_len:
        pred_var = baseline_var(obs_train, forcing_train, val_len, forcing_val)
        if pred_var is not None and len(pred_var) == val_len:
            results["rmse"]["var_obs_forcing"] = rmse(obs_val, pred_var)

    rmse_coupled_val = rmse(obs_val, abm_coupled[train_len:])
    rmse_no_ode_val = rmse(obs_val, abm_no_ode[train_len:])
    results["rmse"]["abm_coupled_val"] = rmse_coupled_val
    results["rmse"]["abm_no_ode_val"] = rmse_no_ode_val
    if rmse_coupled_meta is not None:
        results["rmse"]["abm_coupled_metrics_full"] = rmse_coupled_meta
        results["rmse"]["abm_no_ode_metrics_full"] = rmse_no_ode_meta

    edi_internal = 1 - rmse_coupled_val / rmse_no_ode_val if rmse_no_ode_val > 0 else None
    results["edi_internal_val"] = edi_internal
    for name, val in results["rmse"].items():
        if name == "abm_coupled_val" or val is None or val <= 0:
            continue
        results["edi_vs_baseline"][name] = 1 - rmse_coupled_val / val

    return results


def write_markdown(report: list[dict]) -> None:
    out = OUT_DIR / "baselines_report.md"
    lines = [
        "# Reporte de baselines (F15)",
        "",
        "Comparación del modelo acoplado EDI (`abm_coupled`) contra baselines no-estructurales: persistencia, random walk con drift, ARIMA(1,1,1)/(1,0,1), VAR(1) con forcing exógeno.",
        "",
        f"**Casos procesados:** {len([r for r in report if 'skip_reason' not in r])}",
        f"**Generado:** {pd.Timestamp.utcnow().isoformat()}Z",
        "",
        "## Tabla de RMSE en validación",
        "",
        "| Caso | n | train | val | RMSE acoplado | RMSE sin-ODE | RMSE persist | RMSE RW | RMSE ARIMA | RMSE VAR | EDI(val) |",
        "|------|--:|------:|----:|--------------:|-------------:|-------------:|--------:|-----------:|---------:|---------:|",
    ]
    for r in report:
        if "skip_reason" in r:
            continue
        rmses = r["rmse"]
        arima = rmses.get("arima_1_1_1") or rmses.get("arima_1_0_1")
        var = rmses.get("var_obs_forcing")
        lines.append(
            f"| {r['case_id']} | {r['n']} | {r['train_len']} | {r['val_len']} "
            f"| {rmses.get('abm_coupled_val', 0):.4f} | {rmses.get('abm_no_ode_val', 0):.4f} "
            f"| {rmses.get('persistence', 0):.4f} | {rmses.get('random_walk', 0):.4f} "
            f"| {arima:.4f} " if arima else f"| n/a "
        )
    # Rebuild with cleaner formatting
    lines = lines[:8]
    lines.append(
        "| Caso | n | train | val | RMSE acoplado | RMSE sin-ODE | RMSE persist | RMSE RW | RMSE ARIMA | RMSE VAR | EDI(val) |"
    )
    lines.append(
        "|------|--:|------:|----:|--------------:|-------------:|-------------:|--------:|-----------:|---------:|---------:|"
    )
    for r in report:
        if "skip_reason" in r:
            continue
        rmses = r["rmse"]
        arima = rmses.get("arima_1_1_1") or rmses.get("arima_1_0_1")
        var = rmses.get("var_obs_forcing")
        edi_v = r.get("edi_internal_val")
        def fmt(x):
            return f"{x:.4f}" if isinstance(x, (int, float)) else "n/a"
        lines.append(
            f"| {r['case_id']} | {r['n']} | {r['train_len']} | {r['val_len']} "
            f"| {fmt(rmses.get('abm_coupled_val'))} | {fmt(rmses.get('abm_no_ode_val'))} "
            f"| {fmt(rmses.get('persistence'))} | {fmt(rmses.get('random_walk'))} "
            f"| {fmt(arima)} | {fmt(var)} | {fmt(edi_v)} |"
        )

    lines += [
        "",
        "## EDI vs baselines (1 - RMSE_acoplado / RMSE_baseline)",
        "",
        "Si EDI_vs_baseline > 0, el modelo acoplado supera al baseline.",
        "",
        "| Caso | vs persist | vs RW | vs ARIMA | vs VAR | vs sin-ODE |",
        "|------|----------:|------:|---------:|-------:|-----------:|",
    ]
    for r in report:
        if "skip_reason" in r:
            continue
        b = r["edi_vs_baseline"]
        arima_key = "arima_1_1_1" if "arima_1_1_1" in b else "arima_1_0_1"
        def fmt(x):
            return f"{x:+.4f}" if isinstance(x, (int, float)) else "n/a"
        lines.append(
            f"| {r['case_id']} "
            f"| {fmt(b.get('persistence'))} "
            f"| {fmt(b.get('random_walk'))} "
            f"| {fmt(b.get(arima_key))} "
            f"| {fmt(b.get('var_obs_forcing'))} "
            f"| {fmt(b.get('abm_no_ode_val'))} |"
        )

    skipped = [r for r in report if "skip_reason" in r]
    if skipped:
        lines += ["", "## Casos saltados", ""]
        for r in skipped:
            lines.append(f"- `{r['case_id']}`: {r['skip_reason']}")

    lines += [
        "",
        "## Lectura",
        "",
        "1. **Persistencia / RW** son baselines triviales. Que el modelo acoplado los supere es necesario pero insuficiente.",
        "2. **ARIMA(1,1,1)** captura autocorrelación + tendencia sin estructura física. Si el acoplado lo supera, hay valor más allá de regularidad temporal.",
        "3. **VAR(1) con forcing** captura linealmente la dependencia con el exógeno. Si el acoplado lo supera, hay no-linealidad estructural justificable.",
        "4. **EDI(val)** recalculado en held-out usando los mismos arrays. Discrepancias con el `metrics.json` original indican efecto de longitud de ventana (los `metrics.json` usan ventana completa con calibración).",
        "",
        "## Trazabilidad",
        "",
        "- Generado por: `scripts/baselines_arima_var.py`",
        "- Fuente: `09-simulaciones-edi/<caso>/outputs/primary_arrays.json`",
        "- Splits: usa `val_steps` del `metrics.json` cuando está disponible; si no, 30% del final.",
    ]
    with open(out, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"  → {out}")


def main() -> int:
    case_dirs = sorted([d for d in SIM_DIR.iterdir()
                        if d.is_dir() and (d / "outputs" / "primary_arrays.json").exists()])
    print(f"casos con primary_arrays.json: {len(case_dirs)}")
    report = []
    for d in case_dirs:
        print(f"→ {d.name}")
        r = process_case(d)
        if r:
            report.append(r)

    out_json = OUT_DIR / "baselines_report.json"
    with open(out_json, "w") as f:
        json.dump({"generated_at": pd.Timestamp.utcnow().isoformat() + "Z",
                   "n_cases": len(report),
                   "results": report}, f, indent=2)
    print(f"  → {out_json}")
    write_markdown(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
