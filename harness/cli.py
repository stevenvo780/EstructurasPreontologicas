"""CLI única del harness — solo verificadores deterministas.

Subcomandos:
  init        Inicializa state.json y verifica dependencias.
  status      Muestra estado actual del harness y la tesis.
  verify      Ejecuta verificadores (todos o individuales).
  pass        Pasada completa de verificadores deterministas.
  audit       Verify + reporte detallado a archivo.

Re-ejecución de casos EDI y multi-sonda los hace Claude Code directamente
vía sub-agentes (.claude/agents/execution-queue.md, multi-probe-runner.md)
invocando `python3 09-simulaciones-edi/<caso>/src/validate.py` y
`./tesis run --case <id>`. No hay wrapper Python aquí.
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from harness.lib.state import load_state, save_state, now_iso
from harness.lib.tesis_paths import HARNESS_DIR, repo_root, load_config
from harness.lib import pdftext
from harness.lib import continuous as cont
from harness.lib import plan_generator
from harness import orchestrator


def cmd_init(args):
    state = load_state()
    load_config()
    print(f"[init] state.json en {HARNESS_DIR / 'state.json'}")
    print(f"[init] repo_root = {repo_root()}")
    print(f"[init] pdftotext disponible = {pdftext.have_pdftotext()}")
    if not pdftext.have_pdftotext():
        print("       (instala con: sudo apt install poppler-utils)")
    try:
        import yaml  # noqa
        print("[init] pyyaml = ok")
    except ImportError:
        print("[init] pyyaml FALTA (pip install pyyaml)")
    print(f"[init] verificadores disponibles: {', '.join(orchestrator.VERIFIERS)}")
    print(f"[init] sub-agentes Claude Code: ver .claude/agents/")
    print(f"[init] slash commands: ver .claude/commands/")
    save_state(state)


def cmd_status(args):
    state = load_state()
    print(f"# Estado del harness — {now_iso()}")
    print(f"\nÚltima actualización: {state.get('updated_at')}")
    print(f"Pasadas registradas: {len(state.get('passes', []))}")
    if state.get("passes"):
        last = state["passes"][-1]
        print(f"Última pasada: {last.get('timestamp')} (modo {last.get('mode')})")
        for v, s in (last.get("verifier_summary") or {}).items():
            print(f"  - {v}: {s}")
    nh = state.get("needs_human", [])
    print(f"\nItems needs_human ({len(nh)}):")
    for item in nh:
        print(f"  - {item}")


def cmd_verify(args):
    if args.all or not any([args.citations, args.prose_json, args.replay_hash,
                            args.debt, args.self_indulgence, args.doc_config,
                            args.decorative, args.compliance]):
        targets = list(orchestrator.VERIFIERS.keys())
    else:
        targets = []
        if args.compliance: targets.append("harness_compliance")
        if args.citations: targets.append("citation_pagination")
        if args.decorative: targets.append("decorative_citations")
        if args.prose_json: targets.append("prose_against_json")
        if args.replay_hash: targets.append("replay_hash")
        if args.debt: targets.append("debt_index")
        if args.self_indulgence: targets.append("self_indulgence")
        if args.doc_config: targets.append("consistency_doc_config")

    out = {}
    for name in targets:
        fn = orchestrator.VERIFIERS[name]
        try:
            r = fn()
        except Exception as e:
            r = {"status": "error", "error": str(e)}
        out[name] = r
        status = r.get("status", "?")
        print(f"  [{status:5s}] {name}", file=sys.stderr)

    if args.json:
        print(json.dumps(out, indent=2, ensure_ascii=False))
    else:
        for name, r in out.items():
            print(f"\n## {name}: {r.get('status')}")
            print(f"   {r.get('interpretation', '')}")
            for k in ("total_citations", "without_pagination_count",
                      "discrepancies_count", "discordances_count",
                      "flag_hits_count", "drift_count", "ready_count"):
                if k in r:
                    print(f"   {k}: {r[k]}")


def cmd_pass(args):
    r = orchestrator.run_pass("dry", args.budget_min, args.max_tokens)
    print(f"\nReporte: {r['report_path']}")
    print("Sub-agentes filosóficos/técnicos: invoca con @<nombre> en Claude Code")
    print("(/harness-pass, /verify-citations, /verify-prose-json, /run-case, etc.)")


def cmd_audit(args):
    r = orchestrator.run_pass("dry", args.budget_min, 0)
    out = Path(args.output) if args.output else Path(r["report_path"])
    if args.output:
        Path(r["report_path"]).rename(out)
    print(f"Auditoría completa: {out}")


def cmd_continuous(args):
    """Modo continuo del harness — sesión de N horas auto-orquestada."""
    sub = args.cont_cmd
    if sub == "start":
        try:
            state = cont.start(args.hours, resume=args.resume)
        except RuntimeError as e:
            print(f"[continuous] error: {e}", file=sys.stderr)
            sys.exit(2)
        print(cont.status_report(state))
        print()
        print(f"[continuous] iniciado por {args.hours:.1f} h. "
              f"Próximo paso: invocar `continuous tick` o `/loop /continuous-run-tick` "
              f"desde Claude Code para activar wakeups dinámicos.")
    elif sub == "tick":
        state = cont.load_state()
        if state is None:
            print("[continuous] no hay sesión activa. Inicia con `continuous start --hours N`.",
                  file=sys.stderr)
            sys.exit(1)
        stop, why = cont.should_stop(state)
        if stop:
            print(f"[continuous] STOP: {why}")
            print(cont.final_report(state))
            sys.exit(0)
        task = cont.select_next_task(state)
        if task is None:
            print("[continuous] no hay tareas pending; cerrando sesión.")
            sys.exit(0)
        # Esta CLI sólo MARCA la tarea como in_progress y muestra su action.
        # La ejecución real la hace Claude Code (o un wrapper externo): el LLM lee
        # el action declarado en autonomous_workplan.yaml y opera bajo los hooks.
        # Si no estás dentro de Claude Code, igualmente puedes hacer marca manual.
        cont.mark_in_progress(state, task["id"])
        state["ticks"] += 1
        cont.append_log(state, f"tick {state['ticks']}: in_progress={task['id']}")
        cont.save_state(state)
        action_decl = cont.find_task_action(task["id"])
        delay = cont.recommend_delay_seconds(state)
        print(f"# Tick {state['ticks']} → tarea {task['id']}")
        print(f"# subject:   {task['subject']}")
        print(f"# priority:  {task['priority']}  est_min: {task['est_minutes']}")
        print(f"# action:    {json.dumps(action_decl.get('action', {}), ensure_ascii=False)}")
        print(f"# touches:   {action_decl.get('touches', [])}")
        print(f"# acceptance:{action_decl.get('acceptance', '')}")
        print(f"# next_delay_s: {delay}  (recomendación para ScheduleWakeup)")
    elif sub == "tick-batch":
        state = cont.load_state()
        if state is None:
            print(json.dumps({"error": "no active session"})); sys.exit(1)
        stop, why = cont.should_stop(state)
        if stop:
            print(json.dumps({"stop": True, "reason": why,
                              "in_progress": cont.count_in_progress(state)}))
            sys.exit(0)
        max_parallel = args.n
        already_in_flight = cont.count_in_progress(state)
        slots = max(0, max_parallel - already_in_flight)
        reserved = cont.in_progress_paths(state)
        picked = cont.select_next_n_tasks(state, slots, reserved_paths=reserved)
        claimed = []
        for task in picked:
            cont.mark_in_progress(state, task["id"])
            action_decl = cont.find_task_action(task["id"])
            claimed.append({
                "id": task["id"],
                "subject": task["subject"],
                "priority": task["priority"],
                "est_minutes": task["est_minutes"],
                "action": (action_decl or {}).get("action", {}),
                "touches": (action_decl or {}).get("touches", []),
                "acceptance": (action_decl or {}).get("acceptance", ""),
            })
        if claimed:
            state["ticks"] += 1
            cont.append_log(state, f"tick-batch {state['ticks']}: claimed={[t['id'] for t in claimed]}")
            cont.save_state(state)
        delay = cont.recommend_delay_seconds(state)
        lint_due = (state["ticks"] > 0 and state["ticks"] % 10 == 0)
        print(json.dumps({
            "stop": False,
            "tick": state["ticks"],
            "claimed": claimed,
            "in_flight_total": cont.count_in_progress(state),
            "max_parallel": max_parallel,
            "next_delay_s": delay,
            "remaining_h": cont.time_remaining_seconds(state) / 3600,
            "lint_due": lint_due,
            "lint_cmd": ("/usr/bin/python3 harness/verifiers/verify_self_indulgence.py"
                         if lint_due else None),
        }, ensure_ascii=False, indent=2))
    elif sub == "complete":
        state = cont.load_state()
        if state is None:
            print("[continuous] no hay sesión activa.", file=sys.stderr); sys.exit(1)
        cont.mark_done(state, args.task_id, args.result or "ok", args.notes or [])
        cont.append_log(state, f"complete {args.task_id}")
        cont.save_state(state)
        print(f"[continuous] tarea {args.task_id} marcada done.")
    elif sub == "fail":
        state = cont.load_state()
        if state is None:
            print("[continuous] no hay sesión activa.", file=sys.stderr); sys.exit(1)
        cont.mark_failed(state, args.task_id, args.reason or "")
        cont.append_log(state, f"failed {args.task_id}: {args.reason}")
        cont.save_state(state)
        print(f"[continuous] tarea {args.task_id} marcada failed.")
    elif sub == "status":
        state = cont.load_state()
        if state is None:
            print("(sin sesión activa)")
            return
        print(cont.status_report(state))
    elif sub == "stop":
        state = cont.stop()
        print(f"[continuous] sesión detenida en {state['stopped_at']}.")
    elif sub == "replenish":
        state = cont.load_state()
        if state is None:
            print("[continuous] no hay sesión activa.", file=sys.stderr); sys.exit(1)
        added = plan_generator.replenish(state, max_new=args.max_new)
        cont.save_state(state)
        print(f"[continuous] +{added} tareas generadas desde verificadores")
    elif sub == "daemon":
        print(
            "[continuous] sub-comando `daemon` DEPRECADO Y NEUTRALIZADO (2026-05-11).\n"
            "  Razón: spawneaba `claude -p` headless sin orquestación.\n"
            "  Uso correcto:\n"
            "    /continuous-run              → orquestación interactiva (Agent tool)\n"
            "    /continuous-run-tick         → una iteración\n"
            "    /loop /continuous-run-tick   → loop autoritmado\n",
            file=sys.stderr,
        )
        sys.exit(2)
    else:
        print(f"sub-comando desconocido: {sub}", file=sys.stderr); sys.exit(2)


def main():
    ap = argparse.ArgumentParser(
        prog="harness",
        description="Harness de re-validación científico-filosófica. "
                    "Solo verificadores deterministas — la capa LLM vive en Claude Code.",
    )
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("init", help="Inicializa state.json y verifica dependencias").set_defaults(func=cmd_init)
    sub.add_parser("status", help="Estado del harness").set_defaults(func=cmd_status)

    p_v = sub.add_parser("verify", help="Ejecuta verificadores formales")
    p_v.add_argument("--all", action="store_true")
    p_v.add_argument("--compliance", action="store_true",
                     help="Audita el propio harness (frontmatters, settings, mcp)")
    p_v.add_argument("--citations", action="store_true")
    p_v.add_argument("--decorative", action="store_true")
    p_v.add_argument("--prose-json", action="store_true")
    p_v.add_argument("--replay-hash", action="store_true")
    p_v.add_argument("--debt", action="store_true")
    p_v.add_argument("--self-indulgence", action="store_true")
    p_v.add_argument("--doc-config", action="store_true")
    p_v.add_argument("--json", action="store_true", help="Output como JSON")
    p_v.set_defaults(func=cmd_verify)

    p_p = sub.add_parser("pass", help="Pasada determinista (todos los verificadores)")
    p_p.add_argument("--budget-min", type=int, default=30)
    p_p.add_argument("--max-tokens", type=int, default=100000)
    p_p.set_defaults(func=cmd_pass)

    p_a = sub.add_parser("audit", help="Auditoría completa con reporte")
    p_a.add_argument("--output", type=str, default=None)
    p_a.add_argument("--budget-min", type=int, default=30)
    p_a.set_defaults(func=cmd_audit)

    # ---- modo continuo ----
    p_c = sub.add_parser("continuous", help="Modo continuo de N horas")
    p_c.set_defaults(func=cmd_continuous)
    csub = p_c.add_subparsers(dest="cont_cmd", required=True)
    p_cs = csub.add_parser("start", help="Inicia sesión continua")
    p_cs.add_argument("--hours", type=float, required=True,
                      help="Duración objetivo en horas reales")
    p_cs.add_argument("--resume", action="store_true",
                      help="Reanuda sesión existente en lugar de fallar")
    csub.add_parser("tick", help="Avanza una iteración (escoge próxima tarea)")
    p_ctb = csub.add_parser("tick-batch",
                            help="Claim hasta N tareas pending atómicamente; emite JSON")
    p_ctb.add_argument("--n", type=int, default=4,
                       help="Máximo de tareas en vuelo simultáneas (default 4)")
    p_cc = csub.add_parser("complete", help="Marca tarea como done")
    p_cc.add_argument("task_id")
    p_cc.add_argument("--result", default=None)
    p_cc.add_argument("--notes", nargs="*", default=None)
    p_cf = csub.add_parser("fail", help="Marca tarea como failed")
    p_cf.add_argument("task_id")
    p_cf.add_argument("--reason", default="")
    csub.add_parser("status", help="Status actual de la sesión continua")
    csub.add_parser("stop", help="Detiene la sesión continua")
    p_cr = csub.add_parser("replenish",
                           help="Genera tareas frescas desde verificadores y las añade al state")
    p_cr.add_argument("--max-new", type=int, default=200)
    # Sub-comando `daemon` DEPRECADO Y NEUTRALIZADO (2026-05-11).
    # Conservamos el parser para que `continuous daemon ...` produzca un
    # error claro en lugar de "sub-comando desconocido". Spawneaba
    # `claude -p` headless sin orquestación; ahora la iteración va por el
    # Agent tool dentro de la sesión interactiva.
    p_cd = csub.add_parser("daemon",
                           help="DEPRECADO (2026-05-11). Usa /continuous-run o /continuous-run-tick.")
    p_cd.add_argument("--hours", type=float, default=0)
    p_cd.add_argument("--parallel", type=int, default=0)
    p_cd.add_argument("--dry-run", action="store_true")
    p_cd.add_argument("--replenish-threshold", type=int, default=0)
    p_cd.add_argument("--poll-seconds", type=float, default=0.0)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
