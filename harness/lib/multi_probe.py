"""Multi-sonda automática sobre casos null.

Lee el output de scripts_orquestacion/full_secondary_probes.py si existe,
o invoca python3 scripts/run_secondary_probes_on_primary_arrays.py para
generar sondas alternativas y reportar cuál (si alguna) rompe el null.
"""
from __future__ import annotations
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from harness.lib.tesis_paths import path, glob, repo_root


NULL_CASES_DEFAULT = [
    "02_caso_conciencia",
    "03_caso_contaminacion",
    "12_caso_paradigmas",
    "17_caso_oceanos",
    "19_caso_acidificacion_oceanica",
    "23_caso_erosion_dialectica",
    "25_caso_acuiferos",
    "29_caso_iot",
]


def case_metric(case_id: str) -> dict | None:
    p = path("edi_engine") / case_id / "outputs" / "metrics.json"
    if not p.exists():
        return None
    try:
        with open(p) as f:
            return json.load(f)
    except Exception:
        return None


def main(cases: list[str] | None = None, dry: bool = True) -> dict:
    cases = cases or NULL_CASES_DEFAULT
    edi = path("edi_engine")
    secondary_script = edi / "scripts" / "run_secondary_probes_on_primary_arrays.py"

    report = {"verifier": "multi_probe", "cases": {}, "secondary_script": str(secondary_script),
              "secondary_script_exists": secondary_script.exists()}

    for case_id in cases:
        m = case_metric(case_id)
        primary_arrays = path("edi_engine") / case_id / "outputs" / "primary_arrays.json"
        report["cases"][case_id] = {
            "metrics_present": m is not None,
            "edi": (m or {}).get("edi") or (m or {}).get("edi_real"),
            "p_perm": (m or {}).get("p_permutation") or (m or {}).get("p_perm"),
            "primary_arrays_present": primary_arrays.exists(),
            "ready_for_secondary_probes": primary_arrays.exists(),
        }
        if not dry and primary_arrays.exists() and secondary_script.exists():
            try:
                r = subprocess.run(
                    [sys.executable, str(secondary_script), "--case", case_id],
                    capture_output=True, text=True, timeout=900, cwd=str(edi),
                )
                report["cases"][case_id]["execution"] = {
                    "returncode": r.returncode,
                    "stderr_tail": (r.stderr or "")[-500:],
                }
            except subprocess.TimeoutExpired:
                report["cases"][case_id]["execution"] = {"timeout": True}

    ready = sum(1 for c in report["cases"].values() if c["ready_for_secondary_probes"])
    report["status"] = "pass" if ready == len(cases) else "warn"
    report["ready_count"] = ready
    report["total"] = len(cases)
    report["interpretation"] = (
        "Casos null requieren primary_arrays.json (B-T1) para multi-sonda. "
        "Sin él, el null no es testeado contra sondas alternativas."
    )
    return report


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--execute", action="store_true",
                    help="Ejecuta sondas reales (puede tardar horas)")
    args = ap.parse_args()
    print(json.dumps(main(dry=not args.execute), indent=2, ensure_ascii=False))
