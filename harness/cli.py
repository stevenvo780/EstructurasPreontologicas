"""CLI única del harness.

Subcomandos:
  init        Inicializa state.json y verifica dependencias.
  status      Muestra estado actual del harness y la tesis.
  verify      Ejecuta verificadores (todos o individuales).
  pass        Pasada completa (dry/live).
  audit       Verify + reporte detallado a archivo.
  queue       Operaciones sobre la cola de ejecución de validaciones.
  multi-probe Re-análisis de casos null con sondas alternativas.
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
from harness import orchestrator
from harness.lib import execution_queue, multi_probe


def cmd_init(args):
    state = load_state()
    cfg = load_config()
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
    queue = state.get("queue", {}).get("jobs", {})
    if queue:
        done = sum(1 for j in queue.values() if j["status"] == "done")
        failed = sum(1 for j in queue.values() if j["status"] == "failed")
        pending = sum(1 for j in queue.values() if j["status"] == "pending")
        print(f"\nCola de ejecución: done={done} failed={failed} pending={pending}")


def cmd_verify(args):
    if args.all or not any([args.citations, args.prose_json, args.replay_hash,
                            args.debt, args.self_indulgence, args.doc_config]):
        targets = list(orchestrator.VERIFIERS.keys())
    else:
        targets = []
        if args.citations: targets.append("citation_pagination")
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
    print("Para invocar sub-agentes filosóficos/técnicos: usa Claude Code")
    print("(/harness-pass, /verify-citations, /verify-prose, etc.)")


def cmd_audit(args):
    r = orchestrator.run_pass("dry", args.budget_min, 0)
    out = Path(args.output) if args.output else Path(r["report_path"])
    if args.output:
        Path(r["report_path"]).rename(out)
    print(f"Auditoría completa: {out}")


def cmd_queue(args):
    if args.list_cases:
        for c in execution_queue.list_cases():
            print(c)
        return
    cs = args.cases.split(",") if args.cases else None
    r = execution_queue.queue_pass(cases=cs, max_jobs=args.max_jobs, dry=args.dry)
    print(json.dumps(r, indent=2, ensure_ascii=False))


def cmd_multi_probe(args):
    cs = args.cases.split(",") if args.cases else None
    r = multi_probe.main(cases=cs, dry=not args.execute)
    print(json.dumps(r, indent=2, ensure_ascii=False))


def main():
    ap = argparse.ArgumentParser(prog="harness", description="Harness de investigación científico-filosófica para la tesis.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("init", help="Inicializa state.json y verifica dependencias").set_defaults(func=cmd_init)
    sub.add_parser("status", help="Estado del harness").set_defaults(func=cmd_status)

    p_v = sub.add_parser("verify", help="Ejecuta verificadores formales")
    p_v.add_argument("--all", action="store_true")
    p_v.add_argument("--citations", action="store_true")
    p_v.add_argument("--prose-json", action="store_true")
    p_v.add_argument("--replay-hash", action="store_true")
    p_v.add_argument("--debt", action="store_true")
    p_v.add_argument("--self-indulgence", action="store_true")
    p_v.add_argument("--doc-config", action="store_true")
    p_v.add_argument("--json", action="store_true", help="Output como JSON")
    p_v.set_defaults(func=cmd_verify)

    p_p = sub.add_parser("pass", help="Pasada determinista (todos los verificadores formales)")
    p_p.add_argument("--budget-min", type=int, default=30)
    p_p.add_argument("--max-tokens", type=int, default=100000)
    p_p.set_defaults(func=cmd_pass)

    p_a = sub.add_parser("audit", help="Auditoría completa con reporte")
    p_a.add_argument("--output", type=str, default=None)
    p_a.add_argument("--budget-min", type=int, default=30)
    p_a.set_defaults(func=cmd_audit)

    p_q = sub.add_parser("queue", help="Cola de ejecución de validaciones EDI")
    p_q.add_argument("--list-cases", action="store_true")
    p_q.add_argument("--cases", type=str, default=None)
    p_q.add_argument("--max-jobs", type=int, default=3)
    p_q.add_argument("--dry", action="store_true")
    p_q.set_defaults(func=cmd_queue)

    p_m = sub.add_parser("multi-probe", help="Multi-sonda sobre casos null")
    p_m.add_argument("--cases", type=str, default=None)
    p_m.add_argument("--execute", action="store_true", help="Ejecuta sondas reales (largas)")
    p_m.set_defaults(func=cmd_multi_probe)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
