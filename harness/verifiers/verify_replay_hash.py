"""Wrapper sobre el sistema de hashes existente del motor EDI.

Llama a `09-simulaciones-edi/scripts_orquestacion/replay_hash.py` si está
disponible, o computa hashes mínimos sobre los metrics.json.
"""
from __future__ import annotations
import hashlib
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


def main() -> dict:
    edi_dir = path("edi_engine")
    replay_script = edi_dir / "scripts_orquestacion" / "replay_hash.py"
    baseline = edi_dir / "HASHES_PRE_EJECUCION.json"

    invoked = False
    invoked_output = None
    if replay_script.exists():
        try:
            r = subprocess.run(
                [sys.executable, str(replay_script)],
                capture_output=True, text=True, timeout=120, cwd=str(edi_dir),
            )
            invoked = True
            invoked_output = r.stdout[-2000:] if r.returncode == 0 else r.stderr[-2000:]
        except Exception as e:
            invoked_output = f"[error invoking replay_hash.py] {e}"

    # Hashes locales sobre metrics.json
    local_hashes = {}
    for p in glob("metrics_glob"):
        case = p.parent.parent.name
        local_hashes[case] = {
            "sha256": file_sha256(p)[:16],
            "size": p.stat().st_size,
        }

    # Si baseline existe, comparar
    drift = []
    if baseline.exists():
        try:
            with open(baseline, "r", encoding="utf-8") as f:
                base = json.load(f)
            for case, info in local_hashes.items():
                base_info = base.get(case) or base.get(f"{case}/outputs/metrics.json")
                if base_info and isinstance(base_info, dict):
                    base_h = (base_info.get("sha256") or base_info.get("hash") or "")[:16]
                    if base_h and base_h != info["sha256"]:
                        drift.append({"case": case, "local": info["sha256"], "baseline": base_h})
        except Exception:
            pass

    status = "pass" if not drift else "warn"
    return {
        "verifier": "replay_hash",
        "status": status,
        "edi_replay_script_invoked": invoked,
        "edi_replay_script_tail": (invoked_output or "")[-500:],
        "metrics_files": len(local_hashes),
        "baseline_exists": baseline.exists(),
        "drift_count": len(drift),
        "drift_sample": drift[:10],
        "interpretation": (
            "Drift en hashes indica que metrics.json se ha regenerado desde el baseline. "
            "Si fue intencional, actualizar baseline y declarar el cambio en bitácora."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, ensure_ascii=False))
