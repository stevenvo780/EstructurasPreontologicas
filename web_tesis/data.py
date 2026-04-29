from __future__ import annotations

import copy
import json
import math
import re
import unicodedata
from collections import Counter
from functools import lru_cache
from pathlib import Path
from typing import Any

from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[1]
SIM_ROOT = ROOT / "09-simulaciones-edi"
THESIS_CASES_ROOT = SIM_ROOT  # In this repo, case docs live alongside metrics
THESIS_FINAL_MD = ROOT / "TesisFinal" / "Tesis.md"
VIS_ROOT = ROOT / "visualizations"  # Optional; created on demand if missing

CHAPTER_DIRS = [
    # Introducción
    ("00-proyecto", "Preliminares, introducción y plan del proyecto"),
    ("01-diagnostico", "Estado del arte y diagnóstico"),
    # Cuerpo argumental principal
    ("02-fundamentos", "Parte I · Fundamentos ontológicos y epistemológicos"),
    ("03-formalizacion", "Parte II · Aparato formal y método"),
    ("05-aplicaciones", "Parte III · Evidencia empírica y aplicaciones"),
    ("09-simulaciones-edi", "Parte III · Corpus EDI inter-dominio + inter-escala"),
    ("04-debates", "Parte IV · Discusión crítica"),
    ("06-cierre", "Parte V · Cierre demostrativo"),
    # Material complementario mínimo al final
    ("07-bibliografia", "Bibliografía consolidada"),
    ("10-apendices-tecnicos", "Apéndices técnicos mínimos"),
    ("08-consistencia-st", "Consistencia ST (validación lógica)"),
]

NIVEL_MAP = {
    "null": 0,
    "trend": 1,
    "suggestive": 2,
    "weak": 3,
    "strong": 4,
    "falsification": None,
}

MD = MarkdownIt("js-default", {"html": True, "linkify": True, "typographer": True})


def _slugify(value: str) -> str:
    slug = re.sub(r"[^\w\s\-]", "", value, flags=re.UNICODE).strip().lower()
    slug = re.sub(r"[\s\_]+", "-", slug)
    return slug or "section"


def _slugify_ascii(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9\s\-]", "", ascii_text).strip().lower()
    slug = re.sub(r"[\s\_]+", "-", slug)
    return slug or "section"


def _without_numeric_prefix(anchor: str) -> str:
    return re.sub(r"^\d+(?:[\-\.]\d+)*[-_]+", "", anchor)


def render_markdown(text: str) -> str:
    return MD.render(text or "")


def render_markdown_with_toc(text: str, max_level: int = 2) -> tuple[str, list[dict[str, Any]]]:
    html = render_markdown(text)
    toc: list[dict[str, Any]] = []
    used: Counter[str] = Counter()

    def _unique_slug(base: str) -> str:
        used[base] += 1
        if used[base] == 1:
            return base
        return f"{base}-{used[base]}"

    def repl(match: re.Match[str]) -> str:
        level = int(match.group(1))
        if level > max_level:
            return match.group(0)
        inner = match.group(2)
        plain = re.sub(r"<[^>]+>", "", inner)
        anchor = _unique_slug(_slugify(plain))
        toc.append({"level": level, "title": plain, "anchor": anchor})

        alias_html = ""
        alias_candidates = []

        primary_no_num = _without_numeric_prefix(anchor)
        if primary_no_num and primary_no_num != anchor:
            alias_candidates.append(primary_no_num)

        fallback = _slugify_ascii(plain)
        alias_candidates.append(fallback)
        fallback_no_num = _without_numeric_prefix(fallback)
        if fallback_no_num and fallback_no_num != fallback:
            alias_candidates.append(fallback_no_num)

        for a in list(alias_candidates):
            if "-" in a:
                alias_candidates.append(a.replace("-", "_"))

        seen = set()
        for alias in alias_candidates:
            if not alias or alias == anchor or alias in seen:
                continue
            seen.add(alias)
            if used[alias] == 0:
                used[alias] += 1
                alias_html += f'<span id="{alias}" class="anchor-alias" aria-hidden="true"></span>'

        return f'{alias_html}<h{level} id="{anchor}">{inner}</h{level}>'

    html = re.sub(r"<h([1-6])>(.*?)</h\1>", repl, html, flags=re.DOTALL)
    return html, toc


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _safe_bool(*values: Any) -> bool | None:
    for value in values:
        if isinstance(value, bool):
            return value
    return None


def _to_float(value: Any) -> float | None:
    if isinstance(value, (int, float)):
        v = float(value)
        if math.isfinite(v):
            return v
    return None


def _case_sort_key(path: Path) -> tuple[int, str]:
    m = re.match(r"^(\d+)_", path.name)
    return (int(m.group(1)) if m else 9999, path.name)


def _extract_title(case_name: str) -> str:
    readme = THESIS_CASES_ROOT / case_name / "README.md"
    if readme.exists():
        for line in readme.read_text(encoding="utf-8", errors="ignore").splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    m = re.match(r"^\d+_caso_(.+)$", case_name)
    return (m.group(1).replace("_", " ").title() if m else case_name)


def _extract_criteria(phase: dict[str, Any]) -> dict[str, bool | None]:
    criteria = phase.get("criteria", {}) if isinstance(phase.get("criteria"), dict) else {}
    return {
        "c1": _safe_bool(criteria.get("c1_convergence"), phase.get("c1_convergence")),
        "c2": _safe_bool(criteria.get("c2_robustness"), phase.get("c2_robustness")),
        "c3": _safe_bool(criteria.get("c3_replication"), phase.get("c3_replication")),
        "c4": _safe_bool(criteria.get("c4_validity"), phase.get("c4_validity")),
        "c5": _safe_bool(criteria.get("c5_uncertainty"), phase.get("c5_uncertainty")),
        "sym": _safe_bool(criteria.get("symploke_pass"), phase.get("symploke_pass")),
        "non_local": _safe_bool(criteria.get("non_locality_pass"), phase.get("non_locality_pass")),
        "persist": _safe_bool(criteria.get("persistence_pass"), phase.get("persistence_pass")),
        "coupling": _safe_bool(criteria.get("coupling_ok"), phase.get("coupling_ok")),
    }


def _criteria_gate_list(criteria: dict[str, Any]) -> list[dict[str, Any]]:
    ordered = [
        ("c1_convergence", "C1 Convergencia"),
        ("c2_robustness", "C2 Robustez"),
        ("c3_replication", "C3 Replicación"),
        ("c4_validity", "C4 Validez"),
        ("c5_uncertainty", "C5 Incertidumbre"),
        ("symploke_pass", "Symploke"),
        ("non_locality_pass", "No local"),
        ("persistence_pass", "Persistencia"),
        ("emergence_pass", "Emergencia"),
        ("coupling_ok", "Acoplamiento"),
        ("rmse_fraud_check", "RMSE-fraud"),
    ]
    gates: list[dict[str, Any]] = []
    for key, label in ordered:
        val = criteria.get(key)
        gates.append({"key": key, "label": label, "pass": bool(val) if isinstance(val, bool) else None})
    return gates


def _extract_phase_metrics(phase_name: str, phase: dict[str, Any]) -> dict[str, Any]:
    edi_obj = phase.get("edi") if isinstance(phase.get("edi"), dict) else {}
    errors = phase.get("errors", {}) if isinstance(phase.get("errors"), dict) else {}
    correlations = phase.get("correlations", {}) if isinstance(phase.get("correlations"), dict) else {}
    sym = phase.get("symploke", {}) if isinstance(phase.get("symploke"), dict) else {}
    taxonomy = phase.get("emergence_taxonomy", {}) if isinstance(phase.get("emergence_taxonomy"), dict) else {}
    calibration = phase.get("calibration", {}) if isinstance(phase.get("calibration"), dict) else {}
    criteria_full = phase.get("criteria", {}) if isinstance(phase.get("criteria"), dict) else {}

    rmse_abm = _to_float(errors.get("rmse_abm"))
    rmse_abm_no_ode = _to_float(errors.get("rmse_abm_no_ode"))
    rmse_gain = None
    if rmse_abm is not None and rmse_abm_no_ode not in (None, 0.0):
        rmse_gain = (rmse_abm_no_ode - rmse_abm) / rmse_abm_no_ode

    criteria = _extract_criteria(phase)
    crit_vals = [v for v in criteria.values() if isinstance(v, bool)]
    crit_pass_count = sum(1 for v in crit_vals if v)
    crit_total = len(crit_vals)

    category = taxonomy.get("category") or "unknown"
    nivel = taxonomy.get("nivel")
    if nivel is None:
        nivel = NIVEL_MAP.get(category)

    cr_value = _to_float(sym.get("cr"))
    if cr_value is None:
        internal = _to_float(sym.get("internal"))
        external = _to_float(sym.get("external"))
        if internal is not None and external not in (None, 0.0):
            cr_value = abs(internal / external)

    return {
        "phase": phase_name,
        "overall_pass": bool(phase.get("overall_pass", False)),
        "edi": {
            "value": _to_float(edi_obj.get("value")),
            "weighted": _to_float(edi_obj.get("weighted_value")),
            "bootstrap_mean": _to_float(edi_obj.get("bootstrap_mean")),
            "ci_lo": _to_float(edi_obj.get("ci_lo")),
            "ci_hi": _to_float(edi_obj.get("ci_hi")),
            "pvalue": _to_float(edi_obj.get("permutation_pvalue")),
            "significant": bool(edi_obj.get("permutation_significant")) if isinstance(edi_obj.get("permutation_significant"), bool) else None,
            "valid": bool(edi_obj.get("valid")) if isinstance(edi_obj.get("valid"), bool) else None,
            "loe_factor": _to_float(edi_obj.get("loe_factor")),
            "null_95": _to_float(edi_obj.get("permutation_null_95")),
            "detrended": _to_float((edi_obj.get("trend_bias") or {}).get("detrended_edi")) if isinstance(edi_obj.get("trend_bias"), dict) else None,
            "trend_ratio": _to_float((edi_obj.get("trend_bias") or {}).get("trend_ratio")) if isinstance(edi_obj.get("trend_bias"), dict) else None,
            "trend_r2": _to_float((edi_obj.get("trend_bias") or {}).get("trend_r2")) if isinstance(edi_obj.get("trend_bias"), dict) else None,
        },
        "errors": {
            "rmse_abm": rmse_abm,
            "rmse_abm_no_ode": rmse_abm_no_ode,
            "rmse_ode": _to_float(errors.get("rmse_ode")),
            "rmse_reduced": _to_float(errors.get("rmse_reduced")),
            "threshold": _to_float(errors.get("threshold")),
            "rmse_gain": rmse_gain,
        },
        "correlations": {
            "abm_obs": _to_float(correlations.get("abm_obs")),
            "ode_obs": _to_float(correlations.get("ode_obs")),
        },
        "symploke": {
            "internal": _to_float(sym.get("internal")),
            "external": _to_float(sym.get("external")),
            "cr": cr_value,
            "pass": _safe_bool(sym.get("pass")),
            "cr_valid": _safe_bool(sym.get("cr_valid")),
        },
        "criteria": criteria,
        "criteria_full": {k: bool(v) if isinstance(v, bool) else None for k, v in criteria_full.items()},
        "criteria_pass_count": crit_pass_count,
        "criteria_total": crit_total,
        "criteria_pass_ratio": (crit_pass_count / crit_total) if crit_total else None,
        "gates": _criteria_gate_list(criteria_full),
        "taxonomy": {
            "category": category,
            "nivel": nivel,
            "interpretation": taxonomy.get("interpretation", ""),
        },
        "calibration": {
            "forcing_scale": _to_float(calibration.get("forcing_scale")),
            "macro_coupling": _to_float(calibration.get("macro_coupling")),
            "ode_coupling_strength": _to_float(calibration.get("ode_coupling_strength")),
            "abm_feedback_gamma": _to_float(calibration.get("abm_feedback_gamma")),
            "damping": _to_float(calibration.get("damping")),
            "ode_alpha": _to_float(calibration.get("ode_alpha")),
            "ode_beta": _to_float(calibration.get("ode_beta")),
            "assimilation_strength": _to_float(calibration.get("assimilation_strength")),
            "calibration_rmse": _to_float(calibration.get("calibration_rmse")),
            "ode_rolling": calibration.get("ode_rolling"),
        },
        "details": {
            "c1": phase.get("c1_detail", {}) if isinstance(phase.get("c1_detail"), dict) else {},
            "c2": phase.get("c2_detail", {}) if isinstance(phase.get("c2_detail"), dict) else {},
            "c3": phase.get("c3_detail", {}) if isinstance(phase.get("c3_detail"), dict) else {},
            "c4": phase.get("c4_detail", {}) if isinstance(phase.get("c4_detail"), dict) else {},
            "c5": phase.get("c5_detail", {}) if isinstance(phase.get("c5_detail"), dict) else {},
        },
        "noise": phase.get("noise_sensitivity", {}) if isinstance(phase.get("noise_sensitivity"), dict) else {},
        "non_locality": phase.get("non_locality", {}) if isinstance(phase.get("non_locality"), dict) else {},
        "persistence": phase.get("persistence", {}) if isinstance(phase.get("persistence"), dict) else {},
        "viscosity": phase.get("viscosity", {}) if isinstance(phase.get("viscosity"), dict) else {},
        "emergence": phase.get("emergence", {}) if isinstance(phase.get("emergence"), dict) else {},
        "effective_information": _to_float(phase.get("effective_information")),
        "coupling_check": _safe_bool(phase.get("coupling_check")),
        "rmse_fraud_check": _safe_bool(phase.get("rmse_fraud_check")),
        "gated_by_synthetic": _safe_bool(phase.get("gated_by_synthetic")),
        "data": phase.get("data", {}) if isinstance(phase.get("data"), dict) else {},
        "bias_correction": phase.get("bias_correction", {}) if isinstance(phase.get("bias_correction"), dict) else {},
        "forcing": phase.get("forcing", {}) if isinstance(phase.get("forcing"), dict) else {},
        "synthetic_meta": phase.get("synthetic_meta", {}) if isinstance(phase.get("synthetic_meta"), dict) else {},
    }


def _build_case_insights(case_name: str, phases: dict[str, Any]) -> list[str]:
    insights: list[str] = []
    real = phases.get("real")
    synth = phases.get("synthetic")
    if not real:
        return insights

    r_edi = real["edi"].get("value")
    r_sig = real["edi"].get("significant")
    if isinstance(r_edi, float):
        if real.get("overall_pass"):
            insights.append(f"{case_name}: pasa el protocolo completo con EDI={r_edi:.3f}.")
        elif r_sig:
            insights.append(f"{case_name}: hay señal EDI significativa ({r_edi:.3f}) pero falla alguna compuerta C1–C5+.")
        else:
            insights.append(f"{case_name}: no hay evidencia robusta de cierre operativo (EDI={r_edi:.3f}).")

    failed = [g["label"] for g in real.get("gates", []) if g.get("pass") is False]
    if failed:
        insights.append("Compuertas que bloquean `overall_pass`: " + ", ".join(failed) + ".")

    rmse_gain = real.get("errors", {}).get("rmse_gain")
    if isinstance(rmse_gain, float):
        if rmse_gain >= 0:
            insights.append(f"El acoplamiento macro reduce RMSE ABM en {rmse_gain * 100:.1f}% frente al baseline sin ODE.")
        else:
            insights.append(f"El acoplamiento macro empeora RMSE ABM en {abs(rmse_gain) * 100:.1f}% frente al baseline sin ODE.")

    cr = real.get("symploke", {}).get("cr")
    if isinstance(cr, float):
        insights.append(f"CR (symploke) = {cr:.3f}; valores cercanos a 1 sugieren frontera macro/micro tenue.")

    if synth and isinstance(synth.get("edi", {}).get("value"), float) and isinstance(r_edi, float):
        delta = r_edi - synth["edi"]["value"]
        insights.append(f"Diferencia EDI real - sintético: {delta:+.3f}.")

    return insights


def _extract_case_metrics(metrics: dict[str, Any]) -> dict[str, Any]:
    phases = metrics.get("phases", {})
    real = phases.get("real") or phases.get("synthetic") or {}

    edi_obj = real.get("edi")
    edi_value = _to_float(edi_obj.get("value")) if isinstance(edi_obj, dict) else _to_float(edi_obj)
    pvalue = _to_float(edi_obj.get("permutation_pvalue")) if isinstance(edi_obj, dict) else None
    significant = edi_obj.get("permutation_significant") if isinstance(edi_obj, dict) else None

    sym = real.get("symploke", {}) if isinstance(real.get("symploke"), dict) else {}
    cr_value = _to_float(sym.get("cr"))
    if cr_value is None:
        internal = _to_float(sym.get("internal"))
        external = _to_float(sym.get("external"))
        if internal is not None and external not in (None, 0.0):
            cr_value = abs(internal / external)

    taxonomy = real.get("emergence_taxonomy", {}) if isinstance(real.get("emergence_taxonomy"), dict) else {}
    category = taxonomy.get("category") or "unknown"
    nivel = taxonomy.get("nivel")
    if nivel is None:
        nivel = NIVEL_MAP.get(category)

    errors = real.get("errors", {}) if isinstance(real.get("errors"), dict) else {}
    correlations = real.get("correlations", {}) if isinstance(real.get("correlations"), dict) else {}

    criteria = _extract_criteria(real)
    criteria_values = [v for v in criteria.values() if isinstance(v, bool)]
    criteria_pass_count = sum(1 for v in criteria_values if v)
    criteria_total = len(criteria_values)

    rmse_abm = _to_float(errors.get("rmse_abm"))
    rmse_abm_no_ode = _to_float(errors.get("rmse_abm_no_ode"))
    rmse_reduction = None
    if rmse_abm is not None and rmse_abm_no_ode not in (None, 0.0):
        rmse_reduction = (rmse_abm_no_ode - rmse_abm) / rmse_abm_no_ode

    return {
        "overall_pass": bool(real.get("overall_pass", False)),
        "edi": edi_value,
        "pvalue": pvalue,
        "significant": bool(significant) if significant is not None else False,
        "cr": cr_value,
        "category": category,
        "nivel": nivel,
        "interpretation": taxonomy.get("interpretation", ""),
        "criteria": criteria,
        "criteria_pass_count": criteria_pass_count,
        "criteria_total": criteria_total,
        "criteria_pass_ratio": (criteria_pass_count / criteria_total) if criteria_total else None,
        "rmse_abm": rmse_abm,
        "rmse_abm_no_ode": rmse_abm_no_ode,
        "rmse_reduction": rmse_reduction,
        "corr_abm": _to_float(correlations.get("abm_obs")),
        "corr_ode": _to_float(correlations.get("ode_obs")),
    }


def _find_visual(slug: str, suffix: str) -> str | None:
    if not VIS_ROOT.exists():
        return None
    matches = sorted(VIS_ROOT.glob(f"*{slug}*{suffix}.png"))
    if not matches:
        return None
    return f"/visualizations/{matches[0].name}"


def _collect_case_entry(case_dir: Path) -> dict[str, Any] | None:
    case_name = case_dir.name
    outputs = case_dir / "outputs"
    metrics_path = outputs / "metrics.json"
    report_path = outputs / "report.md"
    if not metrics_path.exists():
        return None

    metrics = _load_json(metrics_path)
    extracted = _extract_case_metrics(metrics)

    raw_phases = metrics.get("phases", {}) if isinstance(metrics.get("phases"), dict) else {}
    phases: dict[str, Any] = {}
    for phase_name, phase_data in raw_phases.items():
        if isinstance(phase_data, dict):
            phases[phase_name] = _extract_phase_metrics(phase_name, phase_data)

    phase_order = [x for x in ("real", "synthetic") if x in phases]
    phase_order.extend(sorted([x for x in phases.keys() if x not in {"real", "synthetic"}]))
    insights = _build_case_insights(case_name, phases)

    m = re.match(r"^(\d+)_caso_(.+)$", case_name)
    case_num = int(m.group(1)) if m else None
    slug = m.group(2) if m else case_name

    docs_dir = case_dir / "docs"
    docs = []
    if docs_dir.exists():
        for doc in sorted(docs_dir.glob("*.md")):
            docs.append(
                {
                    "name": doc.name,
                    "path": doc.relative_to(ROOT).as_posix(),
                    "url": f"/sim_files/{case_name}/docs/{doc.name}",
                }
            )

    return {
        "case_name": case_name,
        "case_num": case_num,
        "slug": slug,
        "title": _extract_title(case_name),
        "meta": {
            "generated_at": metrics.get("generated_at"),
            "git": metrics.get("git") if isinstance(metrics.get("git"), dict) else {},
            "falsification_success": _safe_bool(metrics.get("falsification_success")),
        },
        "phase_order": phase_order,
        "phases": phases,
        "insights": insights,
        "metrics": extracted,
        "generated_at": metrics.get("generated_at"),
        "metrics_path": metrics_path.relative_to(ROOT).as_posix(),
        "report_path": report_path.relative_to(ROOT).as_posix() if report_path.exists() else None,
        "report_url": f"/sim_files/{case_name}/outputs/report.md" if report_path.exists() else None,
        "metrics_url": f"/sim_files/{case_name}/outputs/metrics.json",
        "thesis_readme_url": f"/sim_files/{case_name}/README.md"
        if (case_dir / "README.md").exists()
        else None,
        "docs": docs,
        "heatmap_image_url": _find_visual(slug, "_heatmap"),
        "metrics_image_url": _find_visual(slug, "_metrics"),
        "interpretation": extracted["interpretation"],
    }


def _build_summary(cases: list[dict[str, Any]]) -> dict[str, Any]:
    stats = {
        "total_cases": len(cases),
        "overall_pass": sum(1 for c in cases if c["metrics"]["overall_pass"]),
        "significant": sum(1 for c in cases if c["metrics"]["significant"]),
        "nivel_4": sum(1 for c in cases if c["metrics"]["nivel"] == 4),
    }

    edi_values = [c["metrics"]["edi"] for c in cases if c["metrics"]["edi"] is not None]
    stats["edi_avg"] = (sum(edi_values) / len(edi_values)) if edi_values else None
    stats["edi_max"] = max(edi_values) if edi_values else None
    stats["edi_min"] = min(edi_values) if edi_values else None

    rmse_reduction_values = [c["metrics"]["rmse_reduction"] for c in cases if c["metrics"]["rmse_reduction"] is not None]
    stats["rmse_reduction_avg"] = (
        sum(rmse_reduction_values) / len(rmse_reduction_values)
        if rmse_reduction_values
        else None
    )

    category_counter: Counter[str] = Counter(c["metrics"]["category"] for c in cases)
    level_counter: Counter[str] = Counter(
        "falsificacion" if c["metrics"]["nivel"] is None else str(c["metrics"]["nivel"]) for c in cases
    )

    categories = [
        {"category": cat, "count": count}
        for cat, count in sorted(category_counter.items(), key=lambda x: (-x[1], x[0]))
    ]

    level_order = ["4", "3", "2", "1", "0", "falsificacion"]
    levels = [
        {
            "level": key,
            "label": "Control/Falsación" if key == "falsificacion" else f"Nivel {key}",
            "count": level_counter.get(key, 0),
        }
        for key in level_order
    ]

    criteria_order = ["c1", "c2", "c3", "c4", "c5", "sym", "non_local", "persist", "coupling"]
    criteria_labels = {
        "c1": "C1",
        "c2": "C2",
        "c3": "C3",
        "c4": "C4",
        "c5": "C5",
        "sym": "Symploke",
        "non_local": "NoLocal",
        "persist": "Persist",
        "coupling": "Coupling",
    }

    case_rows = []
    criteria_pass_rates = []
    for key in criteria_order:
        vals = [c["metrics"]["criteria"].get(key) for c in cases]
        usable = [v for v in vals if isinstance(v, bool)]
        passed = sum(1 for v in usable if v)
        rate = (passed / len(usable)) if usable else None
        criteria_pass_rates.append(
            {
                "key": key,
                "label": criteria_labels.get(key, key),
                "passed": passed,
                "total": len(usable),
                "rate": rate,
            }
        )

    edi_bins = [
        {"label": "< -0.5", "min": float("-inf"), "max": -0.5, "count": 0},
        {"label": "-0.5 a 0.0", "min": -0.5, "max": 0.0, "count": 0},
        {"label": "0.0 a 0.1", "min": 0.0, "max": 0.1, "count": 0},
        {"label": "0.1 a 0.3", "min": 0.1, "max": 0.3, "count": 0},
        {"label": "0.3 a 0.6", "min": 0.3, "max": 0.6, "count": 0},
        {"label": ">= 0.6", "min": 0.6, "max": float("inf"), "count": 0},
    ]
    for case in cases:
        value = case["metrics"]["edi"]
        if value is None:
            continue
        for item in edi_bins:
            if item["min"] <= value < item["max"]:
                item["count"] += 1
                break

    timeline = []
    for c in cases:
        case_row = {
            "case_name": c["case_name"],
            "case_num": c["case_num"],
            "slug": c["slug"],
            "title": c["title"],
            "edi": c["metrics"]["edi"],
            "cr": c["metrics"]["cr"],
            "pvalue": c["metrics"]["pvalue"],
            "overall_pass": c["metrics"]["overall_pass"],
            "significant": c["metrics"]["significant"],
            "category": c["metrics"]["category"],
            "nivel": c["metrics"]["nivel"],
            "criteria": c["metrics"]["criteria"],
            "criteria_pass_count": c["metrics"]["criteria_pass_count"],
            "criteria_total": c["metrics"]["criteria_total"],
            "criteria_pass_ratio": c["metrics"]["criteria_pass_ratio"],
            "corr_abm": c["metrics"]["corr_abm"],
            "corr_ode": c["metrics"]["corr_ode"],
            "rmse_abm": c["metrics"]["rmse_abm"],
            "rmse_abm_no_ode": c["metrics"]["rmse_abm_no_ode"],
            "rmse_reduction": c["metrics"]["rmse_reduction"],
        }
        case_rows.append(case_row)

        timeline.append(
            {
                "case_num": c["case_num"],
                "case_name": c["case_name"],
                "edi": c["metrics"]["edi"],
                "cr": c["metrics"]["cr"],
                "rmse_reduction": c["metrics"]["rmse_reduction"],
                "corr_abm": c["metrics"]["corr_abm"],
            }
        )

    top_edi = [
        {"case_name": x["case_name"], "title": x["title"], "edi": x["edi"], "nivel": x["nivel"]}
        for x in sorted(
            [row for row in case_rows if isinstance(row["edi"], (int, float))],
            key=lambda x: x["edi"],
            reverse=True,
        )[:5]
    ]
    bottom_edi = [
        {"case_name": x["case_name"], "title": x["title"], "edi": x["edi"], "nivel": x["nivel"]}
        for x in sorted(
            [row for row in case_rows if isinstance(row["edi"], (int, float))],
            key=lambda x: x["edi"],
        )[:5]
    ]

    return {
        "stats": stats,
        "categories": categories,
        "levels": levels,
        "criteria_order": criteria_order,
        "criteria_pass_rates": criteria_pass_rates,
        "edi_bins": [{"label": x["label"], "count": x["count"]} for x in edi_bins],
        "timeline": sorted(timeline, key=lambda x: (x["case_num"] or 9999, x["case_name"])),
        "top_edi": top_edi,
        "bottom_edi": bottom_edi,
        "cases": case_rows,
    }


def _doc_title_from_md(text: str, fallback: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def _collect_chapter(slug: str, title: str) -> dict[str, Any] | None:
    chapter_dir = ROOT / slug
    if not chapter_dir.exists():
        return None

    docs: list[dict[str, Any]] = []
    md_files = sorted([p for p in chapter_dir.rglob("*.md") if "node_modules" not in p.parts])
    seen_anchors: Counter[str] = Counter()
    for md in md_files:
        rel = md.relative_to(ROOT).as_posix()
        text = md.read_text(encoding="utf-8", errors="ignore")
        doc_title = _doc_title_from_md(text, md.stem)
        base_anchor = _slugify_ascii(md.relative_to(chapter_dir).as_posix())
        seen_anchors[base_anchor] += 1
        anchor = base_anchor if seen_anchors[base_anchor] == 1 else f"{base_anchor}-{seen_anchors[base_anchor]}"
        docs.append(
            {
                "name": md.relative_to(chapter_dir).as_posix(),
                "title": doc_title,
                "anchor": anchor,
                "url": f"/repo_files/{rel}",
                "html": render_markdown(text),
            }
        )

    code_match = re.match(r"^(\d+)", slug)
    code = code_match.group(1) if code_match else slug

    return {
        "slug": slug,
        "title": title,
        "code": code,
        "docs": docs,
    }


def _collect_chapters() -> list[dict[str, Any]]:
    out = []
    for slug, title in CHAPTER_DIRS:
        ch = _collect_chapter(slug, title)
        if ch is not None:
            out.append(ch)
    return out


_DATASET_CACHE: dict[str, Any] = {}
_DATASET_MTIME: float = 0.0


def _compute_thesis_mtime() -> float:
    """mtime del archivo Tesis.md para invalidación automática del caché."""
    try:
        return THESIS_FINAL_MD.stat().st_mtime if THESIS_FINAL_MD.exists() else 0.0
    except OSError:
        return 0.0


def get_dataset() -> dict[str, Any]:
    """Carga el dataset, recargando automáticamente si Tesis.md cambió."""
    global _DATASET_CACHE, _DATASET_MTIME
    current_mtime = _compute_thesis_mtime()
    if _DATASET_CACHE and abs(current_mtime - _DATASET_MTIME) < 1e-3:
        return _DATASET_CACHE

    thesis_text = THESIS_FINAL_MD.read_text(encoding="utf-8") if THESIS_FINAL_MD.exists() else ""
    thesis_html, thesis_toc = render_markdown_with_toc(thesis_text)

    cases = []
    for case_dir in sorted(SIM_ROOT.glob("*_caso_*"), key=_case_sort_key):
        case_entry = _collect_case_entry(case_dir)
        if case_entry is not None:
            cases.append(case_entry)

    summary = _build_summary(cases)
    chapters = _collect_chapters()

    _DATASET_CACHE = {
        "thesis_html": thesis_html,
        "thesis_toc": thesis_toc,
        "summary": summary,
        "cases": cases,
        "case_map": {c["case_name"]: c for c in cases},
        "chapters": chapters,
        "chapter_map": {c["slug"]: c for c in chapters},
    }
    _DATASET_MTIME = current_mtime
    return _DATASET_CACHE


def refresh_dataset() -> dict[str, Any]:
    """Fuerza recarga (vaciar caché)."""
    global _DATASET_CACHE, _DATASET_MTIME
    _DATASET_CACHE = {}
    _DATASET_MTIME = 0.0
    return get_dataset()


def resolve_case(case_id: str, refresh: bool = False) -> dict[str, Any] | None:
    dataset = refresh_dataset() if refresh else get_dataset()
    direct = dataset["case_map"].get(case_id)
    if direct:
        return copy.deepcopy(direct)

    q = case_id.lower().strip()
    matched = []
    for case in dataset["cases"]:
        if q in case["case_name"].lower() or q in case["slug"].lower():
            matched.append(case)

    if len(matched) == 1:
        return copy.deepcopy(matched[0])

    return None


def resolve_chapter(slug: str, refresh: bool = False) -> dict[str, Any] | None:
    dataset = refresh_dataset() if refresh else get_dataset()
    direct = dataset["chapter_map"].get(slug)
    if direct:
        return copy.deepcopy(direct)
    return None


def case_report_html(case: dict[str, Any]) -> str:
    report_rel = case.get("report_path")
    if not report_rel:
        return ""
    report_abs = ROOT / report_rel
    if not report_abs.exists():
        return ""
    return render_markdown(report_abs.read_text(encoding="utf-8", errors="ignore"))


def case_readme_html(case: dict[str, Any]) -> str:
    readme_abs = ROOT / SIM_ROOT.name / case["case_name"] / "README.md"
    if not readme_abs.exists():
        return ""
    return render_markdown(readme_abs.read_text(encoding="utf-8", errors="ignore"))


def case_docs_rendered(case: dict[str, Any]) -> list[dict[str, str]]:
    rendered: list[dict[str, str]] = []
    for doc in case.get("docs", []):
        rel_path = doc.get("path")
        if not rel_path:
            continue
        doc_abs = ROOT / rel_path
        if not doc_abs.exists():
            continue

        text = doc_abs.read_text(encoding="utf-8", errors="ignore")
        title = doc.get("name", doc_abs.name)
        for line in text.splitlines():
            if line.startswith("# "):
                title = line[2:].strip()
                break

        rendered.append(
            {
                "name": doc.get("name", doc_abs.name),
                "title": title,
                "url": doc.get("url", ""),
                "html": render_markdown(text),
            }
        )
    return rendered


def case_math_explainer_html(case: dict[str, Any]) -> str:
    phases = case.get("phases", {})
    if not isinstance(phases, dict) or not phases:
        return ""

    phase_order = case.get("phase_order", [])
    if not isinstance(phase_order, list) or not phase_order:
        phase_order = sorted(phases.keys())

    def _label(phase_key: str) -> str:
        if phase_key == "real":
            return "Real"
        if phase_key == "synthetic":
            return "Sintético"
        return phase_key

    def _fmt(value: Any, digits: int = 4) -> str:
        fv = _to_float(value)
        if fv is None:
            return "n/a"
        return f"{fv:.{digits}f}"

    lines = [
        "### Explicación Matemática del Caso",
        "",
        "Las métricas principales se interpretan con las siguientes relaciones:",
        "",
        r"$$ \mathrm{EDI} = 1 - \frac{\mathrm{RMSE}_{ABM}}{\mathrm{RMSE}_{ABM,\;sin\;ODE}} $$",
        r"$$ \mathrm{CR} = \left|\frac{I_{internal}}{I_{external}}\right| $$",
        "",
        "- EDI alto: mayor constricción macro sobre la dinámica micro.",
        "- CR cercano a 1: frontera macro/micro tenue.",
        "",
        "| Fase | RMSE ABM | RMSE ABM sin ODE | EDI (reportado) | EDI (recalculado) | CR |",
        "|---|---:|---:|---:|---:|---:|",
    ]

    for phase_key in phase_order:
        phase = phases.get(phase_key, {})
        if not isinstance(phase, dict):
            continue
        errors = phase.get("errors", {}) if isinstance(phase.get("errors"), dict) else {}
        edi = phase.get("edi", {}) if isinstance(phase.get("edi"), dict) else {}
        sym = phase.get("symploke", {}) if isinstance(phase.get("symploke"), dict) else {}
        rmse_abm = _to_float(errors.get("rmse_abm"))
        rmse_base = _to_float(errors.get("rmse_abm_no_ode"))
        edi_calc = None
        if rmse_abm is not None and rmse_base not in (None, 0.0):
            edi_calc = 1 - (rmse_abm / rmse_base)

        lines.append(
            f"| {_label(phase_key)} | {_fmt(rmse_abm)} | {_fmt(rmse_base)} | {_fmt(edi.get('value'))} | {_fmt(edi_calc)} | {_fmt(sym.get('cr'))} |"
        )

    lines.extend(
        [
            "",
            "Además, la evidencia estadística del cierre operativo usa prueba de permutación:",
            "",
            r"$$ p = \Pr\left(\mathrm{EDI}_{perm} \geq \mathrm{EDI}_{obs}\right) $$",
            "",
            "y se contrasta con umbral nulo (`permutation_null_95`) y bandas bootstrap (`ci_lo`, `ci_hi`).",
        ]
    )

    return render_markdown("\n".join(lines))
