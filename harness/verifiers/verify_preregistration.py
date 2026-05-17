"""Verificador de pre-registros EDI (B-T2).

Cierra el "garden of forking paths" (Gelman & Loken 2014) automáticamente:

  1. Localiza `09-simulaciones-edi/<NN>_caso_<nombre>/docs/PRE_REGISTRO.md`.
  2. Para cada uno parsea:
       - clasificación predicha (Strong | Weak | Trend | Null | Falsificación)
       - EDI esperado (valor de referencia)
       - margen aceptable |ΔEDI| ≤ X
       - commit-sello declarado
  3. Compara contra `outputs/metrics.json::phases.real.edi`:
       - calcula |EDI_observado − EDI_esperado|
       - clasifica observado con los umbrales canónicos (Strong/Weak/Trend/Null/Falsif.)
       - declara MATCH (dentro de margen + misma clase) o DISCREPANCIA HONESTA
  4. Verifica que `case_config.json` no se modificó tras el commit-sello.

Output: dict con `verifier`, `status`, `prereg_count`, `discrepancies_count`,
`validations_count`, `sample`. NO bloquea: discrepancias honestas son virtud,
no fallo. status='warn' solo si hay discrepancia sin reporte en
`outputs/report.md` (cierre incompleto). status='fail' si `case_config.json`
se modificó tras el sello sin firmar pre-registro nuevo.

Reglas duras del repo:
  - Cero LLM (solo regex + JSON + git ls-tree).
  - Maneja casos sin pre-registro grácilmente (los ignora).
  - Tolerante a commits no presentes localmente (se reporta como
    `commit_not_found` sin fallar).
"""
from __future__ import annotations
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from harness.lib.tesis_paths import repo_root, load_config


# Umbrales canónicos (CLAUDE.md §EDI, idénticos a la plantilla PRE_REGISTRO_TEMPLATE.md §3)
THRESHOLDS = [
    # (clase, predicate sobre (edi, p, ci_lo, ci_hi))
    ("Strong",        lambda e, p, lo, hi: e >= 0.33 and p < 0.05),
    ("Weak",          lambda e, p, lo, hi: 0.10 <= e < 0.33 and p < 0.05),
    ("Trend",         lambda e, p, lo, hi: (0.05 <= e < 0.10) or (0.05 <= p < 0.10)),
    ("Falsificacion", lambda e, p, lo, hi: e < 0 and hi < 0),
    ("Null",          lambda e, p, lo, hi: True),  # fallback
]

# Variantes textuales de cada clase en pre-registros (case-insensitive)
CLASS_SYNONYMS = {
    "Strong":        [r"strong"],
    "Weak":          [r"weak"],
    "Trend":         [r"trend"],
    "Null":          [r"null"],
    "Falsificacion": [r"falsificaci[oó]n", r"falsification"],
}

# --- Regex de parsing del pre-registro ---
HEADER_CLASS_RX = re.compile(
    r'\*\*H0\s*\(clasificaci[oó]n\s+predicha\)[:\*]+\s*`?([A-Za-zóé]+)',
    re.IGNORECASE,
)
EDI_REF_RX = re.compile(
    # Soporta menos ASCII (-), menos Unicode (− U+2212) y guion largo (– U+2013)
    r'EDI[_a-zA-Záéíó]*\s*[≈=~]\s*([\-−–]?[0-9]+\.?[0-9]*)',
)
MARGIN_RX = re.compile(
    r'\|\s*[ΔΔ]?EDI[^|]*\|\s*≤\s*([0-9]+\.?[0-9]*)',
)
COMMIT_RX = re.compile(
    r'\*\*Commit[^*]*registro[^*]*\*\*[:\s]*`?([0-9a-f]{7,40})',
    re.IGNORECASE,
)


def classify_observed(edi: float, p: float, ci_lo: float, ci_hi: float) -> str:
    for name, pred in THRESHOLDS:
        if pred(edi, p, ci_lo, ci_hi):
            return name
    return "Null"


def normalize_class(raw: str) -> str | None:
    raw_l = raw.strip().lower()
    for canon, variants in CLASS_SYNONYMS.items():
        for v in variants:
            if re.fullmatch(v, raw_l):
                return canon
    return None


def parse_prereg(path: Path) -> dict:
    """Extrae los campos verificables de un PRE_REGISTRO.md."""
    text = path.read_text(encoding="utf-8")
    out: dict = {
        "path": str(path),
        "predicted_class_raw": None,
        "predicted_class": None,
        "edi_reference": None,
        "margin": None,
        "commit_seal": None,
        "parse_errors": [],
    }
    m = HEADER_CLASS_RX.search(text)
    if m:
        out["predicted_class_raw"] = m.group(1)
        out["predicted_class"] = normalize_class(m.group(1))
        if out["predicted_class"] is None:
            out["parse_errors"].append(f"clase '{m.group(1)}' no reconocida")
    else:
        out["parse_errors"].append("no se encontró H0 (clasificación predicha)")

    # EDI de referencia: primera ocurrencia tras 'previo' o tras H0
    edi_section = text[m.end():m.end() + 600] if m else text[:800]
    me = EDI_REF_RX.search(edi_section)
    if me:
        raw = me.group(1).replace("−", "-").replace("–", "-")
        try:
            out["edi_reference"] = float(raw)
        except ValueError:
            out["parse_errors"].append("EDI de referencia no parseable")
    else:
        out["parse_errors"].append("no se encontró EDI de referencia")

    mm = MARGIN_RX.search(text)
    if mm:
        try:
            out["margin"] = float(mm.group(1))
        except ValueError:
            out["parse_errors"].append("margen no parseable")
    else:
        out["parse_errors"].append("no se encontró margen aceptable")

    mc = COMMIT_RX.search(text)
    if mc:
        out["commit_seal"] = mc.group(1)
    else:
        out["parse_errors"].append("no se encontró commit-sello")

    return out


def read_observed_metrics(case_dir: Path) -> dict | None:
    metrics_path = case_dir / "outputs" / "metrics.json"
    if not metrics_path.exists():
        return None
    try:
        data = json.loads(metrics_path.read_text(encoding="utf-8"))
    except Exception as e:
        return {"_error": f"metrics.json ilegible: {e}"}
    real = (data.get("phases") or {}).get("real") or {}
    edi_block = real.get("edi") or {}
    if not edi_block:
        return {"_error": "phases.real.edi no presente"}
    return {
        "edi": edi_block.get("value"),
        "p_perm": edi_block.get("permutation_pvalue"),
        "ci_lo": edi_block.get("ci_lo"),
        "ci_hi": edi_block.get("ci_hi"),
        "permutation_significant": edi_block.get("permutation_significant"),
    }


def case_config_modified_after_commit(case_dir: Path, commit: str) -> dict:
    """Verifica si case_config.json fue tocado tras el commit-sello.

    Retorna dict con `modified` (bool|None), `status` (ok|modified|commit_not_found|...)
    y `last_commit_after_seal` si aplica. Tolerante a commits no presentes
    localmente (pre-registros recientes aún no pusheados)."""
    cfg = case_dir / "case_config.json"
    if not cfg.exists():
        return {"modified": None, "status": "no_case_config"}
    rel = str(cfg.relative_to(repo_root()))
    # ¿Existe el commit-sello?
    r = subprocess.run(
        ["git", "-C", str(repo_root()), "cat-file", "-e", commit],
        capture_output=True,
    )
    if r.returncode != 0:
        return {"modified": None, "status": "commit_not_found", "commit": commit}
    # Commits que tocaron case_config.json desde el sello (excluido el sello)
    r2 = subprocess.run(
        ["git", "-C", str(repo_root()), "log", "--format=%H", f"{commit}..HEAD", "--", rel],
        capture_output=True, text=True,
    )
    if r2.returncode != 0:
        return {"modified": None, "status": "git_error", "stderr": r2.stderr.strip()}
    commits_after = [c for c in r2.stdout.strip().split("\n") if c]
    if commits_after:
        return {
            "modified": True,
            "status": "modified",
            "commits_after_seal": commits_after[:5],
            "count_after_seal": len(commits_after),
        }
    return {"modified": False, "status": "unchanged_since_seal"}


def report_mentions_discrepancy(case_dir: Path) -> bool:
    """Heurística: ¿el report.md menciona contraevidencia / discrepancia?"""
    rep = case_dir / "outputs" / "report.md"
    if not rep.exists():
        return False
    try:
        txt = rep.read_text(encoding="utf-8").lower()
    except Exception:
        return False
    for marker in ("contraevidencia", "discrepanc", "no coincide", "downgrade",
                   "upgrade", "pre-registro", "preregistro"):
        if marker in txt:
            return True
    return False


def evaluate_case(prereg_path: Path) -> dict:
    case_dir = prereg_path.parent.parent  # docs/PRE_REGISTRO.md -> caso
    case_name = case_dir.name
    parsed = parse_prereg(prereg_path)
    observed = read_observed_metrics(case_dir)

    record: dict = {
        "case": case_name,
        "prereg_path": str(prereg_path.relative_to(repo_root())),
        "predicted_class": parsed["predicted_class"],
        "edi_reference": parsed["edi_reference"],
        "margin": parsed["margin"],
        "commit_seal": parsed["commit_seal"],
        "parse_errors": parsed["parse_errors"],
    }

    if observed is None:
        record["status"] = "no_metrics"
        record["outcome"] = "indeterminate"
        return record
    if "_error" in observed:
        record["status"] = "metrics_error"
        record["outcome"] = "indeterminate"
        record["metrics_error"] = observed["_error"]
        return record

    edi_obs = observed["edi"]
    p_obs = observed["p_perm"]
    ci_lo = observed.get("ci_lo") or 0.0
    ci_hi = observed.get("ci_hi") or 0.0
    record["observed"] = {
        "edi": edi_obs, "p_perm": p_obs,
        "ci_lo": observed.get("ci_lo"), "ci_hi": observed.get("ci_hi"),
    }
    record["observed_class"] = classify_observed(
        edi_obs if edi_obs is not None else 0.0,
        p_obs if p_obs is not None else 1.0,
        ci_lo, ci_hi,
    )

    # MATCH vs DISCREPANCIA HONESTA
    if (parsed["edi_reference"] is not None and parsed["margin"] is not None
            and edi_obs is not None):
        delta = abs(edi_obs - parsed["edi_reference"])
        record["delta_edi"] = round(delta, 6)
        within_margin = delta <= parsed["margin"]
        same_class = (parsed["predicted_class"] is not None
                      and parsed["predicted_class"] == record["observed_class"])
        record["within_margin"] = within_margin
        record["same_class"] = same_class
        if within_margin and same_class:
            record["outcome"] = "match"
        elif same_class and not within_margin:
            record["outcome"] = "discrepancy_magnitude"
        elif within_margin and not same_class:
            # casi imposible pero documentado
            record["outcome"] = "discrepancy_classification"
        else:
            record["outcome"] = "discrepancy_full"
    else:
        record["outcome"] = "indeterminate"

    # Verificar no-modificación de case_config tras commit-sello
    if parsed["commit_seal"]:
        record["config_integrity"] = case_config_modified_after_commit(
            case_dir, parsed["commit_seal"],
        )
    else:
        record["config_integrity"] = {"status": "no_seal_declared"}

    # ¿El report.md reconoce la discrepancia?
    if record["outcome"].startswith("discrepancy"):
        record["report_mentions_discrepancy"] = report_mentions_discrepancy(case_dir)

    return record


def find_pre_registros() -> list[Path]:
    edi = repo_root() / "09-simulaciones-edi"
    if not edi.exists():
        return []
    return sorted(edi.glob("*_caso_*/docs/PRE_REGISTRO.md"))


def main() -> dict:
    pregistros = find_pre_registros()
    records = [evaluate_case(p) for p in pregistros]

    matches = [r for r in records if r.get("outcome") == "match"]
    discrepancies = [r for r in records if r.get("outcome", "").startswith("discrepancy")]
    indeterminate = [r for r in records if r.get("outcome") == "indeterminate"]
    config_modified = [
        r for r in records
        if r.get("config_integrity", {}).get("status") == "modified"
    ]
    discrepancies_unreported = [
        r for r in discrepancies
        if r.get("report_mentions_discrepancy") is False
    ]

    # Política de status:
    #   - fail si case_config.json se modificó tras el sello sin nuevo pre-registro
    #     (viola §6 del template — compromiso de no-modificación).
    #   - warn si hay discrepancia sin reporte en outputs/report.md
    #     (cierre incompleto: la discrepancia honesta debe declararse).
    #   - pass en el resto, incluyendo discrepancias DECLARADAS
    #     (la discrepancia honesta es virtud, no fallo).
    if config_modified:
        status = "fail"
    elif discrepancies_unreported:
        status = "warn"
    else:
        status = "pass"

    sample = records[:10]

    return {
        "verifier": "preregistration",
        "status": status,
        "prereg_count": len(records),
        "validations_count": len(matches),
        "discrepancies_count": len(discrepancies),
        "indeterminate_count": len(indeterminate),
        "discrepancies_unreported_count": len(discrepancies_unreported),
        "config_modified_count": len(config_modified),
        "matches": [r["case"] for r in matches],
        "discrepancies": [
            {
                "case": r["case"],
                "outcome": r["outcome"],
                "predicted": r.get("predicted_class"),
                "observed_class": r.get("observed_class"),
                "delta_edi": r.get("delta_edi"),
                "margin": r.get("margin"),
                "report_mentions_discrepancy": r.get("report_mentions_discrepancy"),
            }
            for r in discrepancies
        ],
        "indeterminate": [
            {"case": r["case"], "reason": r.get("status") or "parse_incomplete",
             "parse_errors": r.get("parse_errors", [])}
            for r in indeterminate
        ],
        "config_integrity_violations": [
            {"case": r["case"], "details": r["config_integrity"]}
            for r in config_modified
        ],
        "sample": sample,
        "interpretation": (
            "Verificador de pre-registros (B-T2): compara la predicción "
            "pre-registrada (clase, EDI esperado, margen) con phases.real.edi de "
            "metrics.json. Una DISCREPANCIA HONESTA declarada en outputs/report.md "
            "es virtud (Lakatos: ciencia que reconoce su falsación), no fallo. El "
            "verificador SOLO falla si case_config.json fue modificado tras el "
            "commit-sello (viola §6 del template). Advierte (warn) si hay "
            "discrepancia que el report.md no reconoce. Casos sin pre-registro se "
            "ignoran. Commits-sello no encontrados localmente (pushed después o "
            "uncommitted) se reportan como commit_not_found sin fallar."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, ensure_ascii=False))
