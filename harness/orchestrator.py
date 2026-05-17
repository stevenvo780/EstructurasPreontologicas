"""Orquestador del harness: lead-agent que planifica y ejecuta una pasada.

Modo dry: solo verificadores formales (puro Python, siempre seguro).
Modo live: invoca sub-agentes vía Anthropic SDK si ANTHROPIC_API_KEY está.
"""
from __future__ import annotations
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from harness.lib.state import load_state, save_state, record_pass, record_verifier_run, now_iso
from harness.lib.budget import Budget
from harness.lib.tesis_paths import HARNESS_DIR, repo_root, load_config

from harness.verifiers import (
    verify_citation_pagination,
    verify_prose_against_json,
    verify_replay_hash,
    verify_debt_index,
    verify_self_indulgence,
    verify_consistency_doc_config,
    verify_decorative_citations,
    verify_harness_compliance,
    verify_preregistration,
)


VERIFIERS = {
    "harness_compliance": verify_harness_compliance.main,
    "citation_pagination": verify_citation_pagination.main,
    "decorative_citations": verify_decorative_citations.main,
    "prose_against_json": verify_prose_against_json.main,
    "replay_hash": verify_replay_hash.main,
    "debt_index": verify_debt_index.main,
    "self_indulgence": verify_self_indulgence.main,
    "consistency_doc_config": verify_consistency_doc_config.main,
    "preregistration": verify_preregistration.main,
}


def run_all_verifiers(budget: Budget) -> dict:
    """Ejecuta todos los verificadores formales. Siempre seguro.

    Cada verificador es independiente: pass/warn/fail son resultados válidos
    y no afectan a los siguientes. El budget se respeta solo por tiempo/tokens.
    El conteo de no-progress está reservado a iteraciones LLM (fuera de aquí).
    """
    results = {}
    state = load_state()
    for name, fn in VERIFIERS.items():
        stop, why = budget.stop_required()
        if stop:
            results[name] = {"status": "skipped", "reason": why}
            continue
        t0 = time.time()
        try:
            r = fn()
            r["elapsed_s"] = round(time.time() - t0, 2)
            results[name] = r
            record_verifier_run(state, name, r.get("status", "unknown"), {
                "elapsed_s": r["elapsed_s"],
                **{k: v for k, v in r.items() if not isinstance(v, (list, dict))},
            })
        except Exception as e:
            results[name] = {"status": "error", "error": str(e)}
            record_verifier_run(state, name, "error", {"error": str(e)})
    save_state(state)
    return results


def plan_pass(state: dict, mode: str) -> dict:
    """Construye plan declarado de pasada. Persiste en state.

    Esta capa es DETERMINISTA: solo invoca verificadores formales.
    La capa LLM (sub-agentes) vive en .claude/agents/ y se invoca desde Claude Code.
    """
    plan = {
        "mode": mode,
        "started_at": now_iso(),
        "verifiers_to_run": list(VERIFIERS.keys()),
        "wont_touch": [
            "TesisFinal/Tesis.md (es derivado, hook bloquea)",
            "**/outputs/metrics.json (fuente de verdad numérica, hook bloquea)",
            "Tareas H-J* (requieren firma de Jacob)",
        ],
        "next_step_for_claude_code": (
            "tras esta pasada, Claude Code puede invocar sub-agentes "
            "(.claude/agents/) para resolver los needs_human detectados."
        ),
    }
    state["current_plan"] = plan
    save_state(state)
    return plan


def synthesize_report(verifier_results: dict, plan: dict, budget: Budget) -> str:
    """Genera reporte markdown honesto."""
    out = []
    out.append(f"# Pasada del harness — {plan['started_at']}")
    out.append("")
    out.append(f"**Modo:** {plan['mode']}  |  **Tiempo total:** {budget.elapsed():.1f}s")
    out.append("")
    out.append("## Plan declarado")
    out.append(f"- Verificadores deterministas: {', '.join(plan['verifiers_to_run'])}")
    out.append(f"- Capa LLM: {plan.get('next_step_for_claude_code', '')}")
    out.append("")
    out.append("**No se tocó:**")
    for w in plan["wont_touch"]:
        out.append(f"- {w}")
    out.append("")
    out.append("## Resultados de verificadores")
    out.append("")
    out.append("| Verificador | Status | Detalle |")
    out.append("|---|---|---|")
    for name, r in verifier_results.items():
        status = r.get("status", "?")
        detail_parts = []
        for k in ("total_citations", "without_pagination_count",
                  "discrepancies_count", "discordances_count",
                  "flag_hits_count", "drift_count",
                  "required_chapters_missing_debt", "ready_count",
                  "prereg_count", "validations_count",
                  "config_modified_count"):
            v = r.get(k)
            if v is not None:
                detail_parts.append(f"{k}={v if not isinstance(v, list) else len(v)}")
        detail = "; ".join(detail_parts) or "—"
        emoji = {"pass": "OK", "warn": "WARN", "fail": "FAIL", "error": "ERR",
                 "skipped": "—"}.get(status, status)
        out.append(f"| {name} | {emoji} | {detail} |")
    out.append("")
    out.append("## Items needs_human")
    state = load_state()
    nh = state.get("needs_human", [])
    if not nh:
        out.append("(ninguno)")
    else:
        for item in nh:
            out.append(f"- {item}")
    out.append("")
    out.append("## Honestidad sobre lo no logrado")
    failures = [n for n, r in verifier_results.items() if r.get("status") in ("fail", "error")]
    warnings = [n for n, r in verifier_results.items() if r.get("status") == "warn"]
    if failures:
        out.append(f"- Verificadores que **fallaron**: {', '.join(failures)}.")
    if warnings:
        out.append(f"- Verificadores con **warning**: {', '.join(warnings)}. Revisar reporte JSON completo.")
    if not failures and not warnings:
        out.append("- Todos los verificadores pasaron. Esto NO significa que la tesis esté cerrada — solo que las invariantes verificables formalmente se sostienen.")
    out.append("")
    out.append("## Comandos para reproducir")
    out.append("```bash")
    out.append("python3 harness/cli.py verify --all")
    for v in verifier_results:
        out.append(f"python3 harness/verifiers/verify_{v}.py")
    out.append("```")
    return "\n".join(out)


def run_pass(mode: str = "dry", budget_minutes: int = 30,
             max_tokens: int = 100000) -> dict:
    """Ejecuta una pasada determinista (solo verificadores formales).

    Para capa LLM, Claude Code invoca sub-agentes desde .claude/agents/.
    """
    budget = Budget(max_seconds=budget_minutes * 60, max_tokens=max_tokens)
    state = load_state()
    plan = plan_pass(state, mode)

    print(f"[orchestrator] modo={mode} budget={budget_minutes}min plan_persistido", file=sys.stderr)
    verifier_results = run_all_verifiers(budget)

    report = synthesize_report(verifier_results, plan, budget)
    out_dir = HARNESS_DIR / "reports"
    out_dir.mkdir(exist_ok=True)
    ts = datetime.utcnow().strftime("%Y-%m-%d-%H%M%S")
    report_path = out_dir / f"pass-{ts}.md"
    report_path.write_text(report, encoding="utf-8")
    json_path = out_dir / f"pass-{ts}.json"
    full = {
        "plan": plan,
        "budget": {"max_s": budget.max_seconds, "elapsed_s": budget.elapsed()},
        "verifier_results": verifier_results,
    }
    json_path.write_text(json.dumps(full, indent=2, ensure_ascii=False), encoding="utf-8")

    record_pass(state, {
        "mode": mode,
        "report": str(report_path.relative_to(repo_root())),
        "verifier_summary": {n: r.get("status") for n, r in verifier_results.items()},
    })
    save_state(state)

    print(f"[orchestrator] reporte: {report_path}", file=sys.stderr)
    return {"report_path": str(report_path), "json_path": str(json_path), "summary": full}


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--budget-min", type=int, default=30)
    args = ap.parse_args()
    r = run_pass("dry", args.budget_min)
    print(f"\nReporte generado: {r['report_path']}")
