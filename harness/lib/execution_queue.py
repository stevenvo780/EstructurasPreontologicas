"""Cola de ejecución masiva para validaciones EDI con reintentos.

Resuelve la fricción declarada en propuesta §3 #9: run_all_validations_parallel.py
no maneja CUDA OOM ni reintentos inteligentes.

Diseño:
  - Lista de jobs (caso_id) con estado: pending|running|done|failed.
  - Estado persistido en harness/state.json (key: 'queue').
  - Cada job ejecuta `python3 09-simulaciones-edi/<caso>/src/validate.py`.
  - Reintentos exponenciales con fallback CPU si CUDA OOM.
  - Lock file (flock) para no chocar con otra invocación.
"""
from __future__ import annotations
import fcntl
import json
import os
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from harness.lib.tesis_paths import path, glob, repo_root
from harness.lib.state import load_state, save_state, now_iso

LOCK_PATH = repo_root() / ".cache_harness" / "queue.lock"
LOCK_PATH.parent.mkdir(parents=True, exist_ok=True)


def list_cases() -> list[str]:
    cases = []
    edi_dir = path("edi_engine")
    for d in sorted(edi_dir.glob("*_caso_*")):
        if (d / "src" / "validate.py").exists():
            cases.append(d.name)
    return cases


def run_case(case_id: str, force_cpu: bool = False, n_perm: int = 999, n_boot: int = 500,
             timeout_s: int = 1800) -> dict:
    edi_dir = path("edi_engine")
    case_dir = edi_dir / case_id
    script = case_dir / "src" / "validate.py"
    if not script.exists():
        return {"case": case_id, "status": "failed", "reason": "no validate.py"}
    env = os.environ.copy()
    env["HYPER_N_PERM"] = str(n_perm)
    env["HYPER_N_BOOT"] = str(n_boot)
    if force_cpu:
        env["CUDA_VISIBLE_DEVICES"] = ""
    started = time.time()
    try:
        proc = subprocess.run(
            [sys.executable, str(script)],
            cwd=str(case_dir / "src"),
            env=env,
            capture_output=True, text=True, timeout=timeout_s,
        )
        elapsed = time.time() - started
        ok = proc.returncode == 0
        cuda_oom = "CUDA out of memory" in (proc.stderr or "") or "OOM" in (proc.stderr or "")
        return {
            "case": case_id,
            "status": "done" if ok else "failed",
            "elapsed_s": round(elapsed, 1),
            "returncode": proc.returncode,
            "cuda_oom": cuda_oom,
            "stderr_tail": (proc.stderr or "")[-800:],
        }
    except subprocess.TimeoutExpired:
        return {"case": case_id, "status": "failed", "reason": "timeout", "timeout_s": timeout_s}
    except Exception as e:
        return {"case": case_id, "status": "failed", "reason": str(e)}


def queue_pass(cases: list[str] | None = None, max_jobs: int = 10,
               retries: int = 2, dry: bool = False) -> dict:
    """Una pasada de la cola. Si dry=True, solo lista qué haría."""
    with open(LOCK_PATH, "w") as lock:
        try:
            fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            return {"status": "locked", "reason": "another queue pass is running"}

        state = load_state()
        q = state.setdefault("queue", {"jobs": {}, "history": []})
        all_cases = cases or list_cases()
        results = []
        executed = 0
        for case_id in all_cases:
            if executed >= max_jobs:
                break
            job = q["jobs"].setdefault(case_id, {"attempts": 0, "status": "pending"})
            if job["status"] == "done":
                continue
            if job["attempts"] > retries:
                continue
            if dry:
                results.append({"case": case_id, "would_run": True,
                                "previous_attempts": job["attempts"]})
                continue
            executed += 1
            r = run_case(case_id)
            job["attempts"] += 1
            job["last_run"] = now_iso()
            job["last_result"] = r
            if r.get("cuda_oom"):
                # reintento inmediato con CPU forzada
                r2 = run_case(case_id, force_cpu=True)
                job["attempts"] += 1
                job["last_run"] = now_iso()
                job["last_result"] = r2
                r["fallback_cpu"] = r2
            job["status"] = r["status"]
            results.append(r)
            save_state(state)
        return {
            "status": "ok",
            "executed": executed,
            "results": results,
            "queue_summary": {
                "pending": sum(1 for j in q["jobs"].values() if j["status"] == "pending"),
                "done": sum(1 for j in q["jobs"].values() if j["status"] == "done"),
                "failed": sum(1 for j in q["jobs"].values() if j["status"] == "failed"),
            },
        }


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--max-jobs", type=int, default=5)
    ap.add_argument("--cases", type=str, default=None,
                    help="Comma-separated case_ids (e.g. 19_caso_acidificacion_oceanica)")
    args = ap.parse_args()
    cs = args.cases.split(",") if args.cases else None
    print(json.dumps(queue_pass(cases=cs, max_jobs=args.max_jobs, dry=args.dry),
                     indent=2, ensure_ascii=False))
