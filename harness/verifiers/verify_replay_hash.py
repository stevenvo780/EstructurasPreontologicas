"""Wrapper sobre el sistema de hashes existente del motor EDI.

Compara los hashes semánticos actuales (via
`scripts_orquestacion/audit/replay_hash.py`) contra
`replay_baseline.json`. Misma semántica que `--verify`: cambian o faltan
→ drift; casos nuevos → informativo.

2026-09-28: se eliminó la comparación contra HASHES_PRE_EJECUCION.json —
ese archivo es un freeze de SETUP (case_aggregates de código/parámetros),
no hashes de outputs; compararlo con sha256 de metrics.json era peras con
manzanas y el drift siempre daba 0. La correspondencia setup↔outputs
evolucionados es deuda de escala corpus (ver bitácora 2026-09-28-fix-all).
"""
from __future__ import annotations
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from harness.lib.tesis_paths import path, glob, repo_root


def file_sha256(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _load_replay_module(edi_dir: Path):
    """Importa audit/replay_hash.py por ruta (no es paquete)."""
    mod_path = edi_dir / "scripts_orquestacion" / "audit" / "replay_hash.py"
    spec = importlib.util.spec_from_file_location("edi_replay_hash", str(mod_path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> dict:
    edi_dir = path("edi_engine")
    replay_script = edi_dir / "scripts_orquestacion" / "replay_hash.py"
    baseline = edi_dir / "scripts_orquestacion" / "audit" / "replay_baseline.json"

    invoked = False
    invoked_output = None
    if replay_script.exists():
        try:
            r = subprocess.run(
                [sys.executable, str(replay_script), "--verify"],
                capture_output=True, text=True, timeout=120, cwd=str(edi_dir),
            )
            invoked = True
            invoked_output = r.stdout[-2000:] if r.returncode == 0 else r.stderr[-2000:]
        except Exception as e:
            invoked_output = f"[error invoking replay_hash.py] {e}"

    # Hashes semánticos locales (misma función que --verify usa)
    local_hashes = {}
    try:
        _mod = _load_replay_module(edi_dir)
        local_hashes = _mod.collect_hashes()
        metrics_files = len(list(glob("metrics_glob")))
    except Exception as e:
        return {
            "verifier": "replay_hash",
            "status": "warn",
            "error": f"no se pudo recolectar hashes: {e}",
            "edi_replay_script_invoked": invoked,
            "metrics_files": 0,
            "baseline_exists": baseline.exists(),
            "drift_count": 0,
            "drift_sample": [],
        }

    # Comparar contra replay_baseline.json (semántica de --verify)
    drift = []
    new_cases = []
    base = {}
    if baseline.exists():
        try:
            with open(baseline, "r", encoding="utf-8") as f:
                base = json.load(f)
        except Exception:
            base = {}
    for case, entry in sorted(local_hashes.items()):
        if case not in base:
            new_cases.append(case)
            continue
        b = base[case] or {}
        for key in ("metrics_md5", "report_md5"):
            if entry.get(key) != b.get(key):
                drift.append({"case": case, "field": key,
                              "local": entry.get(key), "baseline": b.get(key)})
                break
    for case in sorted(base):
        if case not in local_hashes:
            drift.append({"case": case, "field": "missing",
                          "local": None, "baseline": "present"})

    status = "pass" if not drift else "warn"
    return {
        "verifier": "replay_hash",
        "status": status,
        "edi_replay_script_invoked": invoked,
        "edi_replay_script_tail": (invoked_output or "")[-500:],
        "metrics_files": metrics_files,
        "baseline_exists": baseline.exists(),
        "drift_count": len(drift),
        "drift_sample": drift[:10],
        "new_cases": new_cases,
        "interpretation": (
            "Drift en hashes indica que metrics.json/report.md cambiaron desde "
            "replay_baseline.json. Si fue intencional, re-guardar baseline con "
            "`replay_hash.py --save` y declarar el cambio en bitácora."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, ensure_ascii=False))
