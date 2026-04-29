"""
Sondas secundarias sobre arrays primarios reales — F13.

Aplica `ALL_SECONDARY_PROBES` (`09-simulaciones-edi/common/full_secondary_probes.py`)
a las series **`obs`** y **`forcing`** que el aparato dumpeó en
`primary_arrays.json` durante la corrida del modelo, sin re-simular ni usar
proxys sintéticos.

Calcula:
  - RMSE de la sonda secundaria contra `obs`
  - RMSE de la trayectoria del modelo acoplado (`abm_coupled`) contra `obs`
  - RMSE del baseline (`abm_no_ode`) contra `obs`
  - EDI primario observado: 1 - RMSE_coupled / RMSE_no_ode
  - EDI secundario: 1 - RMSE_secondary / RMSE_no_ode
  - Convergencia inter-paradigma: |Δ_EDI| ≤ 0.05

Salida: `09-simulaciones-edi/multi_sonda/secondary_on_primary_arrays.{json,md}`.

**Diferencia con F13 anterior:** el módulo viejo (`scripts/run_full_secondary_probes.py`)
usaba un `_synthetic_proxy` derivado del EDI publicado, lo que producía circularidad. Este
script opera sobre los arrays primarios efectivamente generados por el modelo.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
SIM_DIR = ROOT / "09-simulaciones-edi"
sys.path.insert(0, str(SIM_DIR))
from common.full_secondary_probes import ALL_SECONDARY_PROBES  # noqa: E402

OUT_DIR = SIM_DIR / "multi_sonda"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def rmse(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.sqrt(np.mean((a - b) ** 2)))


def process_case(case_dir: Path) -> dict | None:
    arr_file = case_dir / "outputs" / "primary_arrays.json"
    if not arr_file.exists():
        return None
    case_id = case_dir.name
    probe_fn = ALL_SECONDARY_PROBES.get(case_id)
    if probe_fn is None:
        return {"case_id": case_id, "skip_reason": "no secondary probe registered"}

    with open(arr_file) as f:
        data = json.load(f)
    arr = data.get("arrays", {})
    obs = np.asarray(arr.get("obs", []), dtype=float)
    forcing = np.asarray(arr.get("forcing", []), dtype=float)
    coupled = np.asarray(arr.get("abm_coupled", []), dtype=float)
    no_ode = np.asarray(arr.get("abm_no_ode", []), dtype=float)
    if obs.size < 30 or forcing.size != obs.size:
        return {"case_id": case_id, "skip_reason": f"insufficient arrays (n={obs.size})"}

    try:
        result = probe_fn(obs, forcing)
    except Exception as e:
        return {"case_id": case_id, "skip_reason": f"probe execution failed: {e}"}

    pred = np.asarray(result.get("prediction"), dtype=float)
    if pred.size != obs.size:
        return {"case_id": case_id, "skip_reason": f"prediction length mismatch ({pred.size} vs {obs.size})"}

    rmse_coupled = rmse(obs, coupled)
    rmse_no_ode = rmse(obs, no_ode)
    rmse_secondary = rmse(obs, pred)
    edi_primary = 1 - rmse_coupled / rmse_no_ode if rmse_no_ode > 0 else None
    edi_secondary = 1 - rmse_secondary / rmse_no_ode if rmse_no_ode > 0 else None
    delta = abs(edi_primary - edi_secondary) if edi_primary is not None and edi_secondary is not None else None

    return {
        "case_id": case_id,
        "n": int(obs.size),
        "secondary_probe": result.get("probe"),
        "secondary_motivation": result.get("motivacion"),
        "rmse_coupled": rmse_coupled,
        "rmse_no_ode": rmse_no_ode,
        "rmse_secondary": rmse_secondary,
        "edi_primary": edi_primary,
        "edi_secondary": edi_secondary,
        "delta_edi": delta,
        "converge_under_005": bool(delta is not None and delta <= 0.05),
        "converge_under_010": bool(delta is not None and delta <= 0.10),
    }


def write_markdown(report: list[dict]) -> None:
    out = OUT_DIR / "secondary_on_primary_arrays.md"
    valid = [r for r in report if "skip_reason" not in r]
    skipped = [r for r in report if "skip_reason" in r]
    n_005 = sum(1 for r in valid if r["converge_under_005"])
    n_010 = sum(1 for r in valid if r["converge_under_010"])

    lines = [
        "# Sondas secundarias sobre arrays primarios — F13",
        "",
        "Aplicación de las sondas secundarias teóricamente independientes a las series **`obs`** y **`forcing`** efectivamente generadas durante la corrida del modelo (no proxys sintéticos derivados del EDI publicado). Esta versión cierra la circularidad detectada como F13 en la auditoría doctoral.",
        "",
        f"**Casos procesados:** {len(valid)} (de {len(report)} totales con `primary_arrays.json`).",
        f"**Convergencia |ΔEDI| ≤ 0.05:** {n_005}/{len(valid)}.",
        f"**Convergencia |ΔEDI| ≤ 0.10:** {n_010}/{len(valid)}.",
        "",
        "## Tabla por caso",
        "",
        "| Caso | n | Sonda secundaria | Motivación | EDI primario | EDI secundario | ΔEDI | conv ≤0.05 | conv ≤0.10 |",
        "|------|--:|------------------|------------|------------:|--------------:|-----:|:---------:|:---------:|",
    ]
    def fmt(x, p=3):
        return f"{x:.{p}f}" if isinstance(x, (int, float)) else "n/a"
    for r in valid:
        lines.append(
            f"| {r['case_id']} | {r['n']} "
            f"| {r['secondary_probe']} | {r['secondary_motivation']} "
            f"| {fmt(r['edi_primary'])} | {fmt(r['edi_secondary'])} "
            f"| {fmt(r['delta_edi'])} "
            f"| {'✓' if r['converge_under_005'] else '✗'} "
            f"| {'✓' if r['converge_under_010'] else '✗'} |"
        )
    if skipped:
        lines += ["", "## Casos saltados", ""]
        for r in skipped:
            lines.append(f"- `{r['case_id']}`: {r['skip_reason']}")
    lines += [
        "",
        "## Lectura",
        "",
        "1. **EDI primario** se calcula con la trayectoria del modelo acoplado real `abm_coupled` que el aparato produjo, no con el valor publicado en `metrics.json`. Discrepancias con el EDI publicado son normales: el publicado promedia bootstrap; este es puntual sobre el array primario.",
        "2. **EDI secundario** se calcula con la trayectoria que predice la sonda independiente sobre `obs` y `forcing` reales.",
        "3. **|ΔEDI| ≤ 0.05** es criterio de convergencia inter-paradigma fuerte (C1 de κ-ontológica fuerte).",
        "4. **|ΔEDI| ≤ 0.10** es criterio relajado, indicativo de coherencia parcial.",
        "5. Una sonda secundaria con EDI muy alto **igualándose** al primario es señal de que la dinámica admite descripción teóricamente independiente — esto fortalece la afirmación de κ-pragmática hacia κ-ontológica.",
        "",
        "## Limitación honesta",
        "",
        "Los 7 casos con `primary_arrays.json` son sólo el subconjunto del corpus para el que el dumpeo de arrays está activado. La extensión al resto del corpus (33 casos) requiere re-ejecución con `array_dump=True` (decisión técnica de Steven). Hasta entonces, F13 está **cerrado parcialmente, no completamente**.",
        "",
        "## Trazabilidad",
        "",
        "- Generado por: `scripts/run_secondary_probes_on_primary_arrays.py`",
        "- Sondas: `09-simulaciones-edi/common/full_secondary_probes.py::ALL_SECONDARY_PROBES`",
        "- Fuente: `09-simulaciones-edi/<caso>/outputs/primary_arrays.json` (campos `arrays.obs`, `arrays.forcing`, `arrays.abm_coupled`, `arrays.abm_no_ode`)",
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
        r = process_case(d)
        if r:
            report.append(r)
            tag = r.get("secondary_probe", r.get("skip_reason", "?"))
            print(f"  → {d.name}: {tag}")

    out_json = OUT_DIR / "secondary_on_primary_arrays.json"
    with open(out_json, "w") as f:
        json.dump({"n_cases": len([r for r in report if 'skip_reason' not in r]),
                   "results": report}, f, indent=2)
    print(f"  → {out_json}")
    write_markdown(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
