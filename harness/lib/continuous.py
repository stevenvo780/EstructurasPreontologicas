"""Modo continuo del harness — gestión de estado para sesiones de N horas.

Diseño:
  - Una sesión continua se inicia con start(hours).
  - Cada tick lee el state, escoge la tarea con mayor prioridad disponible,
    la marca in_progress, ejecuta su acción declarada en autonomous_workplan.yaml,
    registra resultado, vuelve a state pending o done.
  - El loop dynamic de Claude Code orquesta los wakeups con ScheduleWakeup.
  - El estado vive en harness/state/continuous_run.json — sobrevive entre
    sesiones; un cron de respaldo puede reactivar el loop si la sesión cae.

Uso desde CLI:
  python3 harness/cli.py continuous start --hours 80
  python3 harness/cli.py continuous tick
  python3 harness/cli.py continuous status
  python3 harness/cli.py continuous stop

Uso desde Claude Code:
  /continuous-run 80          (slash command que invoca start + primer tick)
  /loop /continuous-run-tick  (modo dinámico — Claude programa wakeups)
"""
from __future__ import annotations
import json
import os
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from harness.lib.tesis_paths import HARNESS_DIR, repo_root


STATE_PATH = HARNESS_DIR / "state" / "continuous_run.json"
PLAN_PATH = HARNESS_DIR / "plans" / "autonomous_workplan.yaml"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")


def now_epoch() -> float:
    return time.time()


def load_plan() -> dict:
    if not PLAN_PATH.exists():
        raise FileNotFoundError(f"Plan no encontrado: {PLAN_PATH}")
    with PLAN_PATH.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_state() -> Optional[dict]:
    if not STATE_PATH.exists():
        return None
    with STATE_PATH.open(encoding="utf-8") as f:
        return json.load(f)


def save_state(state: dict) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    state["updated_at"] = now_iso()
    with STATE_PATH.open("w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)


def start(hours: float, resume: bool = False) -> dict:
    """Inicia (o reanuda) una sesión continua de `hours` horas."""
    plan = load_plan()
    existing = load_state()

    if existing and existing.get("status") in ("running", "paused") and not resume:
        raise RuntimeError(
            f"Ya existe sesión activa iniciada {existing['started_at']}. "
            f"Usa `continuous stop` o pasa --resume para reanudarla."
        )

    if resume and existing:
        state = existing
        state["resumed_at"] = now_iso()
        state["status"] = "running"
        state["target_hours"] = hours  # permite ajustar
        # Re-cargar tareas no presentes en plan actualizado
        existing_ids = {t["id"] for t in state["tasks"]}
        for t in plan["tasks"]:
            if t["id"] not in existing_ids:
                state["tasks"].append({
                    "id": t["id"],
                    "subject": t["subject"],
                    "priority": t.get("priority", 3),
                    "est_minutes": t.get("est_minutes", 30),
                    "status": "pending",
                    "started_at": None,
                    "finished_at": None,
                    "result": None,
                    "notes": [],
                })
    else:
        tasks = []
        for t in plan["tasks"]:
            tasks.append({
                "id": t["id"],
                "subject": t["subject"],
                "priority": t.get("priority", 3),
                "est_minutes": t.get("est_minutes", 30),
                "status": "pending",
                "started_at": None,
                "finished_at": None,
                "result": None,
                "notes": [],
            })
        state = {
            "version": 1,
            "status": "running",
            "started_at": now_iso(),
            "started_epoch": now_epoch(),
            "target_hours": hours,
            "ticks": 0,
            "tasks": tasks,
            "log": [],
        }
    save_state(state)
    return state


def stop() -> dict:
    """Detiene la sesión continua actual."""
    state = load_state()
    if not state:
        raise RuntimeError("No hay sesión continua para detener.")
    state["status"] = "stopped"
    state["stopped_at"] = now_iso()
    save_state(state)
    return state


def time_remaining_seconds(state: dict) -> float:
    elapsed = now_epoch() - state["started_epoch"]
    return max(0.0, state["target_hours"] * 3600 - elapsed)


def time_elapsed_seconds(state: dict) -> float:
    return now_epoch() - state["started_epoch"]


def should_stop(state: dict) -> tuple[bool, str]:
    if state.get("status") not in ("running", "paused"):
        return True, f"status={state.get('status')}"
    if time_remaining_seconds(state) <= 0:
        return True, "time budget exhausted"
    pending = [t for t in state["tasks"] if t["status"] == "pending"]
    if not pending:
        return True, "no pending tasks"
    return False, ""


def select_next_task(state: dict) -> Optional[dict]:
    """Selecciona próxima tarea: priority asc, est_minutes asc dentro de prio."""
    pending = [t for t in state["tasks"] if t["status"] == "pending"]
    if not pending:
        return None
    pending.sort(key=lambda t: (t["priority"], t["est_minutes"]))
    return pending[0]


def select_next_n_tasks(state: dict, n: int,
                        reserved_paths: Optional[set] = None) -> list[dict]:
    """Selecciona hasta n próximas tareas pending sin colisión de touches.

    `reserved_paths`: paths ya bloqueados por tareas in_progress (no claimear
    nada que comparta path con ellas). Dentro del batch, dos tareas que
    comparten algún touch no se claiman juntas — la de menor prioridad espera.
    """
    pending = [t for t in state["tasks"] if t["status"] == "pending"]
    pending.sort(key=lambda t: (t["priority"], t["est_minutes"]))
    plan_actions = {t["id"]: t for t in load_plan()["tasks"]}
    locked = set(reserved_paths or [])
    chosen = []
    for t in pending:
        if len(chosen) >= n:
            break
        touches = set((plan_actions.get(t["id"], {}) or {}).get("touches", []))
        if touches & locked:
            continue
        chosen.append(t)
        locked |= touches
    return chosen


def in_progress_paths(state: dict) -> set:
    plan_actions = {t["id"]: t for t in load_plan()["tasks"]}
    paths = set()
    for t in state["tasks"]:
        if t["status"] == "in_progress":
            paths |= set((plan_actions.get(t["id"], {}) or {}).get("touches", []))
    return paths


def count_in_progress(state: dict) -> int:
    return sum(1 for t in state["tasks"] if t["status"] == "in_progress")


def mark_in_progress(state: dict, task_id: str) -> None:
    for t in state["tasks"]:
        if t["id"] == task_id:
            t["status"] = "in_progress"
            t["started_at"] = now_iso()
            return


def mark_done(state: dict, task_id: str, result: str, notes: list[str] = None) -> None:
    for t in state["tasks"]:
        if t["id"] == task_id:
            t["status"] = "done"
            t["finished_at"] = now_iso()
            t["result"] = result
            if notes:
                t["notes"].extend(notes)
            return


def mark_failed(state: dict, task_id: str, reason: str) -> None:
    for t in state["tasks"]:
        if t["id"] == task_id:
            t["status"] = "failed"
            t["finished_at"] = now_iso()
            t["result"] = f"failed: {reason}"
            return


def append_log(state: dict, entry: str) -> None:
    state["log"].append({"at": now_iso(), "entry": entry})


def recommend_delay_seconds(state: dict) -> int:
    """Recomienda delay para el próximo wakeup en /loop dynamic.

    Heurística:
      - Si quedan muchas tareas y mucho budget: 60-180s (cache caliente).
      - Si la queue es estrecha: 600-1800s (idle apropiado).
      - Si está cerca de cierre: 60s para apurar.
    """
    remaining_s = time_remaining_seconds(state)
    pending = sum(1 for t in state["tasks"] if t["status"] == "pending")
    if pending == 0 or remaining_s <= 0:
        return 0  # no schedule
    if remaining_s < 600:
        return 30
    if pending > 5:
        return 45
    if pending > 2:
        return 60
    return 120


def status_report(state: dict) -> str:
    out = []
    out.append(f"# Modo continuo — status {now_iso()}")
    out.append("")
    out.append(f"- iniciado: {state['started_at']}")
    out.append(f"- target: {state['target_hours']:.1f} h ({state['target_hours']*3600:.0f} s)")
    elapsed_h = time_elapsed_seconds(state) / 3600
    remaining_h = time_remaining_seconds(state) / 3600
    out.append(f"- elapsed: {elapsed_h:.2f} h")
    out.append(f"- remaining: {remaining_h:.2f} h")
    out.append(f"- ticks: {state['ticks']}")
    out.append(f"- status: {state['status']}")
    out.append("")
    counts = {"pending": 0, "in_progress": 0, "done": 0, "failed": 0}
    for t in state["tasks"]:
        counts[t["status"]] = counts.get(t["status"], 0) + 1
    out.append(f"## Tareas: pending={counts['pending']} done={counts['done']} "
               f"failed={counts['failed']} in_progress={counts['in_progress']}")
    out.append("")
    out.append("### Done")
    for t in state["tasks"]:
        if t["status"] == "done":
            out.append(f"- [{t['id']}] {t['subject']} → {t['result'][:80] if t['result'] else ''}")
    out.append("")
    out.append("### Pending (top 5 por prioridad)")
    pending = sorted([t for t in state["tasks"] if t["status"] == "pending"],
                     key=lambda t: (t["priority"], t["est_minutes"]))
    for t in pending[:5]:
        out.append(f"- [{t['id']}] (p{t['priority']}, ~{t['est_minutes']}m) {t['subject']}")
    out.append("")
    out.append("### Failed")
    for t in state["tasks"]:
        if t["status"] == "failed":
            out.append(f"- [{t['id']}] {t['subject']} → {t['result']}")
    return "\n".join(out)


def final_report(state: dict) -> str:
    out = [status_report(state), ""]
    out.append("## Log de eventos")
    for entry in state["log"][-50:]:
        out.append(f"- {entry['at']}: {entry['entry']}")
    return "\n".join(out)


def find_task_action(task_id: str) -> Optional[dict]:
    """Devuelve el `action` declarado en autonomous_workplan.yaml para `task_id`."""
    plan = load_plan()
    for t in plan["tasks"]:
        if t["id"] == task_id:
            return t
    return None
