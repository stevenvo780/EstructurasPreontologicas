"""Memoria de intentos previos por tarea (qué se intentó, por qué falló)."""
from __future__ import annotations
from typing import Any
from .state import load_state, save_state, now_iso


def record_attempt(task_id: str, action: str, outcome: str, details: dict | None = None) -> None:
    state = load_state()
    t = state["tasks"].setdefault(task_id, {"attempts": [], "status": "open"})
    t["attempts"].append({
        "timestamp": now_iso(),
        "action": action,
        "outcome": outcome,
        "details": details or {},
    })
    if len(t["attempts"]) > 20:
        t["attempts"] = t["attempts"][-20:]
    if outcome == "blocked_human":
        t["status"] = "needs_human"
        if task_id not in state["needs_human"]:
            state["needs_human"].append(task_id)
    elif outcome == "passed":
        t["status"] = "passed"
        if task_id in state["needs_human"]:
            state["needs_human"].remove(task_id)
    save_state(state)


def get_task_history(task_id: str) -> list[dict[str, Any]]:
    state = load_state()
    return state["tasks"].get(task_id, {}).get("attempts", [])


def already_failed_recently(task_id: str, limit: int = 3) -> bool:
    """Evita reintentos infinitos sobre la misma tarea."""
    history = get_task_history(task_id)
    if len(history) < limit:
        return False
    return all(a["outcome"].startswith("fail") for a in history[-limit:])
