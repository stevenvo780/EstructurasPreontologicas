"""Estado persistente del harness entre pasadas."""
from __future__ import annotations
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .tesis_paths import HARNESS_DIR

STATE_PATH = HARNESS_DIR / "state.json"

DEFAULT_STATE: dict[str, Any] = {
    "version": 1,
    "created_at": None,
    "updated_at": None,
    "passes": [],
    "tasks": {},          # task_id -> {attempts, last_error, last_run, status, needs_human}
    "verifiers": {},      # verifier_name -> {last_run, last_status, fail_count}
    "needs_human": [],    # cola de items que requieren firma humana
    "deuda_index": {},    # chapter -> [{fecha, descripcion, prioridad}]
}


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def load_state() -> dict[str, Any]:
    if not STATE_PATH.exists():
        s = DEFAULT_STATE.copy()
        s["created_at"] = now_iso()
        s["updated_at"] = now_iso()
        save_state(s)
        return s
    with open(STATE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_state(state: dict[str, Any]) -> None:
    state["updated_at"] = now_iso()
    tmp = STATE_PATH.with_suffix(".json.tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)
    tmp.replace(STATE_PATH)


def record_pass(state: dict, summary: dict) -> None:
    state["passes"].append({"timestamp": now_iso(), **summary})
    if len(state["passes"]) > 50:
        state["passes"] = state["passes"][-50:]


def record_verifier_run(state: dict, name: str, status: str, details: dict) -> None:
    v = state["verifiers"].setdefault(name, {"fail_count": 0})
    v["last_run"] = now_iso()
    v["last_status"] = status
    v["last_details"] = details
    if status != "pass":
        v["fail_count"] = v.get("fail_count", 0) + 1
    else:
        v["fail_count"] = 0
