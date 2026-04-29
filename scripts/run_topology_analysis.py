"""
Aplica el análisis topológico (Lyapunov + dimensión de correlación + mixing) — F4.

Sobre los casos con `primary_arrays.json`. Salida agregada en
`09-simulaciones-edi/topology/topology_report.{json,md}`.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
SIM_DIR = ROOT / "09-simulaciones-edi"
sys.path.insert(0, str(SIM_DIR))
from common.topology import topology_report  # noqa: E402

OUT_DIR = SIM_DIR / "topology"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def main() -> int:
    cases = sorted([d for d in SIM_DIR.iterdir()
                    if d.is_dir() and (d / "outputs" / "primary_arrays.json").exists()])
    print(f"casos con primary_arrays.json: {len(cases)}")
    results = []
    for d in cases:
        with open(d / "outputs" / "primary_arrays.json") as f:
            data = json.load(f)
        obs = np.asarray(data.get("arrays", {}).get("obs", []), dtype=float)
        if obs.size < 30:
            print(f"  skip {d.name} (n={obs.size})")
            continue
        n = obs.size
        dim = 5 if n >= 200 else 3
        rep = topology_report(obs, dim=dim)
        rep["case_id"] = d.name
        rep["case_name"] = data.get("case_id", d.name)
        results.append(rep)
        lyap = rep.get("lyapunov", {}).get("lyapunov_max")
        cd = rep.get("correlation_dimension", {}).get("correlation_dimension")
        lyap_s = f"{lyap:.4f}" if isinstance(lyap, float) else "n/a"
        cd_s = f"{cd:.3f}" if isinstance(cd, float) else "n/a"
        print(f"  → {d.name}: lambda_max={lyap_s}, D2={cd_s}")

    out_json = OUT_DIR / "topology_report.json"
    with open(out_json, "w") as f:
        json.dump({"n_cases": len(results), "results": results}, f, indent=2)
    print(f"  → {out_json}")

    lines = [
        "# Análisis topológico del corpus EDI (F4)",
        "",
        "Métricas estándar para validar carácter atractor de las trayectorias `obs` del corpus:",
        "exponente de Lyapunov máximo (Rosenstein 1993), dimensión de correlación (Grassberger-Procaccia 1983),",
        "tiempo de mezcla (ACF < 1/e). Embedding Takens con dim=5 y τ por primer cero de ACF.",
        "",
        f"**Casos analizados:** {len(results)} (sólo los que tienen `primary_arrays.json`).",
        "",
        "## Tabla resumen",
        "",
        "| Caso | n | τ | λ_max (Rosenstein) | r² fit | D₂ (Grass-Proc) | r² scaling | mixing time |",
        "|------|--:|--:|------------------:|------:|---------------:|----------:|------------:|",
    ]

    def fmt(x, p=4):
        if isinstance(x, (int, float)) and not (isinstance(x, float) and (x != x)):
            return f"{x:.{p}f}"
        return "n/a"

    for r in results:
        lyap = r.get("lyapunov", {})
        cd = r.get("correlation_dimension", {})
        mt = r.get("mixing_time", {})
        lyap_v = lyap.get("lyapunov_max") if "error" not in lyap else None
        lyap_r2 = lyap.get("linear_fit_r2") if "error" not in lyap else None
        cd_v = cd.get("correlation_dimension") if "error" not in cd else None
        cd_r2 = cd.get("log_log_r2") if "error" not in cd else None
        mt_v = mt.get("mixing_time") if "error" not in mt else None
        lines.append(
            f"| {r['case_id']} | {r['n']} | {r['tau_acf_zero']} "
            f"| {fmt(lyap_v)} | {fmt(lyap_r2, 3)} "
            f"| {fmt(cd_v, 2)} | {fmt(cd_r2, 3)} "
            f"| {mt_v if mt_v is not None else 'n/a'} |"
        )

    lines += [
        "",
        "## Lectura",
        "",
        "1. **λ_max > 0** indica sensibilidad a condiciones iniciales (caos determinista) — compatible con atractor extraño.",
        "2. **λ_max ≈ 0** indica régimen marginal o cuasi-periódico — compatible con atractor en el borde del caos.",
        "3. **λ_max < 0** indica convergencia a punto fijo o ciclo límite — compatible con atractor convergente.",
        "4. **D₂ no entera** (ej. 2.4) es firma de atractor fractal/extraño.",
        "5. **r² alto** del fit log-log (D₂) o lineal (λ) indica que la métrica es interpretable; r² bajo indica que la serie no admite tratamiento topológico estándar.",
        "",
        "## Limitaciones declaradas",
        "",
        "- Con n ≤ 200 puntos las estimaciones son **indicativas, no concluyentes**.",
        "- Rosenstein supone que los pares cercanos divergen exponencialmente al menos en una ventana inicial.",
        "- Grassberger-Procaccia es sensible al ruido aditivo: D₂ inflada si el ruido domina sobre la dinámica determinista.",
        "- La correspondencia entre estas métricas y el concepto operativo de \"atractor empírico\" del cap 02-01 §2.2 es **necesaria pero no suficiente**: una serie con λ_max > 0 admite tratamiento topológico, pero el dossier de anclaje exige además identificación material y especificación dinámica.",
        "",
        "## Trazabilidad",
        "",
        "- Generado por: `scripts/run_topology_analysis.py`",
        "- Implementación: `09-simulaciones-edi/common/topology.py`",
        "- Fuente de datos: `09-simulaciones-edi/<caso>/outputs/primary_arrays.json` (campo `arrays.obs`)",
    ]
    out_md = OUT_DIR / "topology_report.md"
    with open(out_md, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"  → {out_md}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
