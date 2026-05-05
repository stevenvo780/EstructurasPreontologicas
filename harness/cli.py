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
    print("Sub-agentes filosóficos/técnicos: invoca con @<nombre> en Claude Code")
    print("(/harness-pass, /verify-citations, /verify-prose-json, /run-case, etc.)")


def cmd_audit(args):
    r = orchestrator.run_pass("dry", args.budget_min, 0)
    out = Path(args.output) if args.output else Path(r["report_path"])
    if args.output:
        Path(r["report_path"]).rename(out)
    print(f"Auditoría completa: {out}")


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
    p_v.add_argument("--citations", action="store_true")
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

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
