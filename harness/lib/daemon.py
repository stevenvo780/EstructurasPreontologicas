"""Daemon de modo continuo — paralelismo real con headless `claude -p`.

Diseño:
  - Vive como proceso Python independiente (no depende de la sesión interactiva).
  - Mantiene N workers en paralelo (subprocess.Popen). Cada worker es:
      * `claude -p` headless para tareas engagement / audit
      * subprocess.run directo para tareas shell / verifier
  - Auto-replenish: cuando pending baja de un umbral, llama a plan_generator
    y agrega tareas frescas desde verificadores.
  - Stop bajo (a) deadline horario, (b) señal SIGTERM/SIGINT, (c) plan agotado
    sin replenish posible.
  - Logs estructurados a Bitacora/<fecha>-continuous-run/daemon-*.log.
  - Cada worker recibe presupuesto cap (--max-budget-usd, --max-turns) para
    evitar runaway costos.

Hooks: cuando spawneamos `claude -p` desde la raíz del repo, los hooks declarados
en `.claude/settings.json` (block_tesis_md_edit, block_metrics_edit, etc.) se
activan automáticamente. El daemon no bypasea hooks.

Uso:
  python3 harness/cli.py continuous daemon --hours 80 --parallel 4
  # o nohup para sobrevivir cierre de terminal:
  nohup python3 harness/cli.py continuous daemon --hours 80 --parallel 4 \
        > harness/state/daemon.out 2>&1 &
"""
from __future__ import annotations
import json
import os
import shlex
import signal
import subprocess
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from harness.lib import continuous as cont
from harness.lib import plan_generator
from harness.lib.tesis_paths import HARNESS_DIR, repo_root


CLAUDE_BIN = os.environ.get("CLAUDE_BIN", "claude")
DEFAULT_MAX_TURNS = int(os.environ.get("HARNESS_MAX_TURNS", "120"))
DEFAULT_MAX_BUDGET = float(os.environ.get("HARNESS_MAX_BUDGET_USD", "5.00"))
DEFAULT_MODEL = os.environ.get("HARNESS_WORKER_MODEL", "opus")
# Timeout duro por worker (segundos). Salvaguarda final: si por cualquier razón
# un worker se cuelga (red, race en hooks, modelo en bucle), el daemon lo mata
# y reclaman la siguiente. Default 30 min, override con env.
WORKER_TIMEOUT_S = int(os.environ.get("HARNESS_WORKER_TIMEOUT_S", "1800"))
LOG_DIR = repo_root() / "Bitacora" / f"{datetime.now().strftime('%Y-%m-%d')}-continuous-run"
DAEMON_LOG = LOG_DIR / "daemon.log"
WORKER_LOG_DIR = LOG_DIR / "workers"


def _ensure_dirs() -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    WORKER_LOG_DIR.mkdir(parents=True, exist_ok=True)


def _log(msg: str) -> None:
    _ensure_dirs()
    ts = datetime.now(timezone.utc).strftime("%H:%M:%S")
    line = f"[{ts}] {msg}\n"
    sys.stdout.write(line)
    sys.stdout.flush()
    with DAEMON_LOG.open("a", encoding="utf-8") as f:
        f.write(line)


def _build_engagement_prompt(task: dict, action: dict) -> str:
    """Prompt headless para tareas engagement. Voz = asistencia técnica acotada."""
    target = action.get("target_file", "")
    line = action.get("target_line", "?")
    author = action.get("author") or ", ".join(action.get("authors", [])) or "?"
    strategy = action.get("strategy", "")
    snippet = action.get("snippet", "")
    return f"""Eres un sub-agente del harness de re-validación de la tesis doctoral de Jacob Agudelo (concepto) y Steven Vallejo (técnica). Operas en modo headless dentro de un loop autónomo.

TAREA: {task['id']} — {task['subject']}

Archivo objetivo: {target}:{line}
Autor(es): {author}
Snippet del párrafo (si aplica): {snippet[:300]}

Estrategia declarada: {strategy}

REGLAS DURAS (de CLAUDE.md raíz):
- NO editar TesisFinal/Tesis.md (hook bloquea — es derivado).
- NO editar **/outputs/metrics.json (hook bloquea — fuente de verdad numérica).
- NO ejecutar git destructivo, NO push.
- NO inventar paginación. Si no encuentras la cita verbatim en el PDF, declara deuda en lugar de inventar.
- Toda cita inyectada debe ser literal del PDF correspondiente en 07-bibliografia/.
- Si el PDF no está, reformular como mención secundaria declarada (CLAUDE.md §5) explícitamente, no como cita primaria.
- Marca cualquier output sustantivo filosófico como `BORRADOR-IA` con `requires: H-J*` — la voz autoral final es de Jacob.

PROCESO:
1. Leer {target} alrededor de la línea {line}.
2. Si la estrategia exige PDF: localizarlo en 07-bibliografia/, extraer cita verbatim con `pdftotext` o Read pages, verificar paginación.
3. Editar {target} con `Edit` para insertar cita paginada O reformular como mención secundaria.
4. Si no se puede (PDF ausente, hook bloquea, hit ambiguo): NO forzar — reportar fail con razón concreta.

ÚLTIMA LÍNEA DE TU RESPUESTA (obligatorio, parsearé esto):
RESULT: <complete|fail> | {task['id']} | <≤80 chars resumen del cambio o de la razón>
"""


def _build_audit_prompt(task: dict, action: dict) -> str:
    return f"""Eres un sub-agente del harness en modo headless. Tarea de AUDITORÍA (read-only o write-only-to-Bitacora).

TAREA: {task['id']} — {task['subject']}

Estrategia: {action.get('strategy','')}
Touches declarados: {action.get('touches', [])}
Acceptance: {task.get('acceptance', '')}

REGLAS:
- NO editar Tesis.md ni metrics.json.
- Output: archivo `Bitacora/{LOG_DIR.name}/{task['id']}.md` con hallazgos honestos.
- Si los hallazgos requieren acción humana (B-T*, H-J*), márcalos `needs_human`.

ÚLTIMA LÍNEA: RESULT: <complete|fail> | {task['id']} | <≤80 chars>
"""


def _spawn_claude_worker(task: dict, action: dict, kind: str) -> subprocess.Popen:
    if kind == "engagement":
        prompt = _build_engagement_prompt(task, action)
    else:
        prompt = _build_audit_prompt(task, action)

    log_path = WORKER_LOG_DIR / f"{task['id']}.log"
    # CRÍTICO: workers headless NUNCA deben colgarse esperando confirmación de
    # permisos (stdin está cerrado). La protección real son los hooks PreToolUse
    # (block_metrics_edit, block_tesis_md_edit, block_destructive_git,
    # protect_main_push) que devuelven permissionDecision="deny" y los `deny`
    # rules en .claude/settings.json — ambos siguen aplicándose con
    # bypassPermissions. El modo bypassPermissions sólo elimina los prompts
    # interactivos, no las barreras de seguridad declaradas.
    cmd = [
        CLAUDE_BIN,
        "-p",
        "--permission-mode", "bypassPermissions",
        "--max-turns", str(DEFAULT_MAX_TURNS),
        "--max-budget-usd", str(DEFAULT_MAX_BUDGET),
        "--model", DEFAULT_MODEL,
        "--output-format", "text",
        "--no-session-persistence",
        prompt,
    ]
    f = log_path.open("w", encoding="utf-8")
    f.write(f"# worker {task['id']}\n# cmd: {' '.join(shlex.quote(c) for c in cmd[:-1])} <prompt>\n# started: {datetime.now().isoformat()}\n\n")
    f.flush()
    proc = subprocess.Popen(
        cmd,
        cwd=str(repo_root()),
        stdout=f,
        stderr=subprocess.STDOUT,
        stdin=subprocess.DEVNULL,
        env={**os.environ, "CLAUDE_NONINTERACTIVE": "1"},
    )
    proc._log_file = f  # type: ignore
    proc._log_path = log_path  # type: ignore
    proc._spawn_epoch = time.time()  # type: ignore
    return proc


def _spawn_shell_worker(task: dict, action: dict) -> subprocess.Popen:
    cmd_str = action.get("cmd", "echo '(no cmd)'")
    log_path = WORKER_LOG_DIR / f"{task['id']}.log"
    f = log_path.open("w", encoding="utf-8")
    f.write(f"# worker {task['id']} (shell)\n# cmd: {cmd_str}\n# started: {datetime.now().isoformat()}\n\n")
    f.flush()
    proc = subprocess.Popen(
        cmd_str,
        shell=True,
        cwd=str(repo_root()),
        stdout=f,
        stderr=subprocess.STDOUT,
        stdin=subprocess.DEVNULL,
    )
    proc._log_file = f  # type: ignore
    proc._log_path = log_path  # type: ignore
    proc._spawn_epoch = time.time()  # type: ignore
    return proc


def _resolve_action(task_id: str) -> dict | None:
    a = cont.find_task_action(task_id)
    if a:
        return a
    return plan_generator.task_action_for(task_id)


def _spawn_worker(task: dict, dry_run: bool) -> subprocess.Popen | None:
    action_decl = _resolve_action(task["id"])
    if not action_decl:
        _log(f"[{task['id']}] sin action declarado — skip")
        return None
    action = action_decl.get("action", {}) if "action" in action_decl else action_decl.get("action", {})
    kind = action.get("kind", "audit")

    if dry_run:
        _log(f"[{task['id']}] DRY kind={kind} subject={task['subject'][:60]}")
        # simular éxito inmediato
        return subprocess.Popen(["true"])

    if kind in ("engagement", "audit"):
        return _spawn_claude_worker(task, action, kind)
    elif kind in ("shell", "verifier"):
        return _spawn_shell_worker(task, action)
    else:
        _log(f"[{task['id']}] kind desconocido: {kind}")
        return None


def _parse_worker_result(log_path: Path) -> tuple[str, str]:
    """Lee la última línea RESULT: del log. Devuelve (status, summary)."""
    try:
        text = log_path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return "fail", "log no legible"
    # buscar última línea que empiece con 'RESULT:'
    last = None
    for line in text.splitlines():
        if line.strip().startswith("RESULT:"):
            last = line.strip()
    if not last:
        return "fail", "no RESULT line"
    parts = [p.strip() for p in last[len("RESULT:"):].split("|")]
    if len(parts) >= 3:
        status = parts[0].lower()
        summary = parts[2][:120]
        if status in ("complete", "ok", "done"):
            return "complete", summary
        return "fail", summary
    return "fail", last[:120]


def _finalize_worker(task_id: str, proc: subprocess.Popen, dry_run: bool) -> None:
    log_file = getattr(proc, "_log_file", None)
    log_path = getattr(proc, "_log_path", None)
    if log_file:
        try:
            log_file.write(f"\n# finished: {datetime.now().isoformat()} rc={proc.returncode}\n")
            log_file.close()
        except Exception:
            pass

    state = cont.load_state()
    if state is None:
        return

    rc = proc.returncode

    if dry_run:
        cont.mark_done(state, task_id, "dry-run ok")
        cont.append_log(state, f"complete {task_id} (dry)")
        cont.save_state(state)
        return

    if rc != 0:
        cont.mark_failed(state, task_id, f"worker rc={rc}")
        cont.append_log(state, f"failed {task_id}: rc={rc}")
        cont.save_state(state)
        _log(f"[{task_id}] FAIL rc={rc}")
        return

    if log_path and log_path.exists():
        status, summary = _parse_worker_result(log_path)
        if status == "complete":
            cont.mark_done(state, task_id, summary)
            cont.append_log(state, f"complete {task_id}")
            _log(f"[{task_id}] OK — {summary[:60]}")
        else:
            cont.mark_failed(state, task_id, summary)
            cont.append_log(state, f"failed {task_id}: {summary}")
            _log(f"[{task_id}] FAIL — {summary[:60]}")
        cont.save_state(state)
    else:
        cont.mark_done(state, task_id, f"rc=0 (sin log parseable)")
        cont.append_log(state, f"complete {task_id} (rc=0)")
        cont.save_state(state)


_stop_requested = False


def _signal_handler(signum, frame):
    global _stop_requested
    _stop_requested = True
    _log(f"señal {signum} recibida — drenando workers")


def run_daemon(hours: float, parallel: int = 4, dry_run: bool = False,
               replenish_threshold: int = 2, poll_seconds: float = 5.0) -> None:
    """Bucle principal del daemon."""
    _ensure_dirs()
    signal.signal(signal.SIGTERM, _signal_handler)
    signal.signal(signal.SIGINT, _signal_handler)

    state = cont.load_state()
    if state is None:
        _log("no hay sesión continua — iniciando con --resume implícito")
        state = cont.start(hours, resume=False)
    else:
        # actualizar target_hours si difiere y status no es running
        if state.get("status") != "running":
            state["status"] = "running"
        state["target_hours"] = hours
        state["started_epoch"] = state.get("started_epoch", time.time())
        cont.save_state(state)

    _log(f"daemon iniciado: hours={hours} parallel={parallel} dry={dry_run} pid={os.getpid()}")
    _log(f"logs por worker en: {WORKER_LOG_DIR}")

    workers: dict[str, subprocess.Popen] = {}
    # deadline relativo al lanzamiento del daemon (no al started_epoch del state).
    # Esto permite relanzar el daemon con --hours nuevo sobre una sesión vieja.
    daemon_start = time.time()
    deadline = daemon_start + hours * 3600
    _log(f"deadline en {hours:.2f}h ({datetime.fromtimestamp(deadline).isoformat()})")

    last_replenish = 0.0

    while True:
        # 1. reap workers terminados o que excedieron WORKER_TIMEOUT_S
        for tid in list(workers.keys()):
            proc = workers[tid]
            if proc.poll() is not None:
                _finalize_worker(tid, proc, dry_run)
                del workers[tid]
                continue
            # timeout duro: protege contra cualquier cuelgue (incluido permisos)
            spawned = getattr(proc, "_spawn_epoch", time.time())
            if time.time() - spawned > WORKER_TIMEOUT_S:
                _log(f"[{tid}] TIMEOUT >{WORKER_TIMEOUT_S}s — SIGTERM")
                try:
                    proc.terminate()
                    proc.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    _log(f"[{tid}] persistió tras SIGTERM — SIGKILL")
                    proc.kill()
                    proc.wait(timeout=5)
                _finalize_worker(tid, proc, dry_run)
                del workers[tid]

        # 2. condiciones de parada
        if _stop_requested:
            _log("stop solicitado — esperando workers en vuelo")
            for tid, proc in list(workers.items()):
                try:
                    proc.wait(timeout=120)
                except subprocess.TimeoutExpired:
                    proc.terminate()
                _finalize_worker(tid, proc, dry_run)
            break
        if time.time() >= deadline:
            _log("budget horario agotado — drenando workers")
            for tid, proc in list(workers.items()):
                try:
                    proc.wait(timeout=300)
                except subprocess.TimeoutExpired:
                    proc.terminate()
                _finalize_worker(tid, proc, dry_run)
            break

        # 3. replenish cuando queda poco pending
        state = cont.load_state()
        if state is None:
            _log("state perdido — saliendo"); break
        pending = sum(1 for t in state["tasks"] if t["status"] == "pending")
        now = time.time()
        if pending <= replenish_threshold and (now - last_replenish) > 300:
            added = plan_generator.replenish(state, max_new=200)
            cont.save_state(state)
            last_replenish = now
            if added:
                _log(f"replenish: +{added} tareas generadas desde verificadores")
                pending += added

        # 4. dispatch
        free = parallel - len(workers)
        if free > 0 and pending > 0:
            reserved = cont.in_progress_paths(state)
            picked = cont.select_next_n_tasks(state, free, reserved_paths=reserved)
            for task in picked:
                cont.mark_in_progress(state, task["id"])
                cont.append_log(state, f"daemon-claim {task['id']}")
                proc = _spawn_worker(task, dry_run)
                if proc is None:
                    cont.mark_failed(state, task["id"], "spawn null")
                    continue
                workers[task["id"]] = proc
                _log(f"[{task['id']}] spawned ({len(workers)}/{parallel})")
            if picked:
                state["ticks"] = state.get("ticks", 0) + 1
                cont.save_state(state)

        # 5. idle: forzar replenish ya (ignorar cooldown) y esperar corto
        if not workers and pending == 0:
            added = plan_generator.replenish(state, max_new=500)
            cont.save_state(state)
            last_replenish = now
            if added:
                _log(f"idle-replenish: +{added} tareas generadas")
                continue
            _log("idle: queue vacía y sin hits nuevos — esperando 30s")
            time.sleep(30)
            continue

        time.sleep(poll_seconds)

    state = cont.load_state()
    if state:
        state["status"] = "stopped"
        state["stopped_at"] = cont.now_iso()
        cont.save_state(state)
        _write_final_report(state)
    _log("daemon terminado")


def _write_final_report(state: dict) -> None:
    out = LOG_DIR / "REPORTE_FINAL.md"
    txt = cont.final_report(state)
    out.write_text(txt, encoding="utf-8")
    _log(f"reporte final: {out}")


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description="Daemon de modo continuo")
    ap.add_argument("--hours", type=float, required=True)
    ap.add_argument("--parallel", type=int, default=4)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    run_daemon(args.hours, args.parallel, dry_run=args.dry_run)
