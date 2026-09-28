"""Sección pre-registro para outputs/report.md (B-T2).

Emitida automáticamente por `hybrid_validator.write_outputs` cuando el caso
tiene `docs/PRE_REGISTRO.md`. Evita que las re-ejecuciones de `validate.py`
borren la declaración de discrepancia honesta (lo ocurrido en iter 13→14 con
5 de 7 secciones manuales).

Cero dependencias (solo stdlib) para que el validador lo importe sin riesgo.
Los umbrales y regex son idénticos a `harness/verifiers/verify_preregistration.py`
— si cambian allá, cambiar acá (y viceversa).

Contrato con el verificador:
  - discrepancia → la sección contiene "discrepancia", "contraevidencia" y
    "pre-registro" (marcadores de `report_mentions_discrepancy`).
  - match → sección breve de validación (documentación; el verificador no la exige).
  - sin PRE_REGISTRO.md o error de parseo → "" (el verificador ignora esos casos).
"""
from __future__ import annotations

import os
import re

# --- Umbrales canónicos (idénticos al verificador) ---
_THRESHOLDS = [
    ("Strong",        lambda e, p, lo, hi: e >= 0.33 and p < 0.05),
    ("Weak",          lambda e, p, lo, hi: 0.10 <= e < 0.33 and p < 0.05),
    ("Trend",         lambda e, p, lo, hi: (0.05 <= e < 0.10) or (0.05 <= p < 0.10)),
    ("Falsificacion", lambda e, p, lo, hi: e < 0 and hi < 0),
    ("Null",          lambda e, p, lo, hi: True),  # fallback
]

_CLASS_SYNONYMS = {
    "Strong":        [r"strong"],
    "Weak":          [r"weak"],
    "Trend":         [r"trend"],
    "Null":          [r"null"],
    "Falsificacion": [r"falsificaci[oó]n", r"falsification"],
}

HEADER_CLASS_RX = re.compile(
    r'\*\*H0\s*\(clasificaci[oó]n\s+predicha\)[:\*]+\s*`?([A-Za-zóé]+)',
    re.IGNORECASE,
)
EDI_REF_RX = re.compile(
    r'EDI[_a-zA-Záéíó]*\s*[≈=~]\s*([\-−–]?[0-9]+\.?[0-9]*)',
)
MARGIN_RX = re.compile(
    r'\|\s*[ΔΔ]?EDI[^|]*\|\s*≤\s*([0-9]+\.?[0-9]*)',
)

_RANK = {"Falsificacion": 0, "Null": 1, "Trend": 2, "Weak": 3, "Strong": 4}


def classify_observed(edi: float, p: float, ci_lo: float, ci_hi: float) -> str:
    for name, pred in _THRESHOLDS:
        if pred(edi, p, ci_lo, ci_hi):
            return name
    return "Null"


def _normalize_class(raw: str) -> str | None:
    raw_l = raw.strip().lower()
    for canon, variants in _CLASS_SYNONYMS.items():
        for v in variants:
            if re.fullmatch(v, raw_l):
                return canon
    return None


def parse_prereg(text: str) -> dict | None:
    """Extrae (clase predicha, EDI ref, margen) o None si incompleto."""
    m = HEADER_CLASS_RX.search(text)
    if not m:
        return None
    predicted = _normalize_class(m.group(1))
    if predicted is None:
        return None
    edi_section = text[m.end():m.end() + 600]
    me = EDI_REF_RX.search(edi_section)
    mm = MARGIN_RX.search(text)
    if not me or not mm:
        return None
    try:
        edi_ref = float(me.group(1).replace("−", "-").replace("–", "-"))
        margin = float(mm.group(1))
    except ValueError:
        return None
    return {"predicted": predicted, "edi_ref": edi_ref, "margin": margin}


def _fmt(x, ndigits: int = 4) -> str:
    if x is None:
        return "N/A"
    try:
        return f"{float(x):.{ndigits}f}"
    except (TypeError, ValueError):
        return "N/A"


def render_prereg_section(case_dir: str, edi_value, p_perm, ci_lo, ci_hi) -> str:
    """Sección markdown de comparación pre-registro, o "" si no aplica."""
    prereg_path = os.path.join(str(case_dir), "docs", "PRE_REGISTRO.md")
    if not os.path.exists(prereg_path):
        return ""
    try:
        with open(prereg_path, encoding="utf-8") as fh:
            parsed = parse_prereg(fh.read())
    except OSError:
        return ""
    if parsed is None:
        return ""
    if edi_value is None:
        return ""
    try:
        e = float(edi_value)
    except (TypeError, ValueError):
        return ""
    p = float(p_perm) if p_perm is not None else 1.0
    lo = float(ci_lo) if ci_lo is not None else 0.0
    hi = float(ci_hi) if ci_hi is not None else 0.0

    observed = classify_observed(e, p, lo, hi)
    predicted = parsed["predicted"]
    ref, margin = parsed["edi_ref"], parsed["margin"]
    delta = abs(e - ref)
    within_margin = delta <= margin
    same_class = predicted == observed

    head = ("- **Predicción pre-registro:** {pred} (EDI esperado ≈ {ref}, "
            "margen |ΔEDI| ≤ {margin}).\n"
            "- **Resultado real (phases.real):** {obs} — EDI = {e}, "
            "p_perm = {p}, CI 95% = [{lo}, {hi}].\n").format(
        pred=predicted, ref=_fmt(ref), margin=_fmt(margin, 2),
        obs=observed, e=_fmt(e), p=_fmt(p), lo=_fmt(lo), hi=_fmt(hi))

    if within_margin and same_class:
        return ("## Pre-registro: validación confirmada (generada automáticamente)\n\n"
                + head +
                f"- **Diferencia:** |ΔEDI| = {_fmt(delta)} dentro de margen. MATCH.\n\n")

    direction = ("upgrade" if _RANK.get(observed, 1) > _RANK.get(predicted, 1)
                 else "downgrade" if _RANK.get(observed, 1) < _RANK.get(predicted, 1)
                 else "misma clase, fuera de margen")
    return ("## Discrepancia con pre-registro (generada automáticamente)\n\n"
            + head +
            f"- **Diferencia:** |ΔEDI| = {_fmt(delta)}; dirección: {direction} "
            f"({predicted} → {observed}).\n"
            "- **Declaración:** DISCREPANCIA RECONOCIDA. Contraevidencia declarada "
            "según PRE_REGISTRO.md §6: la discrepancia honesta es virtud, no fallo.\n\n")
