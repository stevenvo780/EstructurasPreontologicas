"""Self-test de prereg_section.py (solo stdlib).

Oráculo independiente: `harness/verifiers/verify_preregistration.py`.
Para cada caso con PRE_REGISTRO.md, la sección generada debe coincidir con
el veredicto del verificador (misma clase predicha/observada, mismo outcome).

Ejecutar:  python3 09-simulaciones-edi/common/test_prereg_section.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

COMMON = Path(__file__).resolve().parent
ROOT = COMMON.parent.parent  # repo root
if str(COMMON) not in sys.path:
    sys.path.insert(0, str(COMMON))
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from prereg_section import (  # noqa: E402
    classify_observed,
    parse_prereg,
    render_prereg_section,
)
from harness.verifiers.verify_preregistration import (  # noqa: E402
    evaluate_case as verifier_evaluate,
)


def _real_edi(case_dir: Path) -> dict:
    data = json.loads((case_dir / "outputs" / "metrics.json").read_text(encoding="utf-8"))
    return (data.get("phases") or {}).get("real", {}).get("edi", {}) or {}


def test_agrees_with_verifier_on_all_prereg_cases():
    preregs = sorted((ROOT / "09-simulaciones-edi").glob("*_caso_*/docs/PRE_REGISTRO.md"))
    assert preregs, "no se encontraron PRE_REGISTRO.md"
    checked = 0
    for pr in preregs:
        case_dir = pr.parent.parent
        verdict = verifier_evaluate(pr)
        if verdict.get("outcome") == "indeterminate":
            continue  # sin métricas: el verificador también lo ignora
        edi = _real_edi(case_dir)
        section = render_prereg_section(
            str(case_dir), edi.get("value"), edi.get("permutation_pvalue"),
            edi.get("ci_lo"), edi.get("ci_hi"),
        )
        assert section, f"{case_dir.name}: sección vacía con pre-registro parseable"
        outcome = verdict["outcome"]
        if outcome == "match":
            assert "MATCH" in section, f"{case_dir.name}: match sin marca MATCH"
            assert "Discrepancia" not in section, f"{case_dir.name}: falso positivo"
        else:
            assert outcome.startswith("discrepancy"), outcome
            low = section.lower()
            for marker in ("discrepancia", "contraevidencia", "pre-registro"):
                assert marker in low, f"{case_dir.name}: falta marcador {marker!r}"
            assert verdict["predicted_class"] in section, f"{case_dir.name}: predicha ausente"
            assert verdict["observed_class"] in section, f"{case_dir.name}: observada ausente"
        checked += 1
    assert checked >= 10, f"solo {checked} casos comparados, se esperaban >= 10"
    print(f"OK: {checked} casos coinciden con el verificador")


def test_canonical_thresholds():
    assert classify_observed(0.50, 0.01, 0.3, 0.6) == "Strong"
    assert classify_observed(0.20, 0.01, 0.1, 0.3) == "Weak"
    assert classify_observed(0.07, 0.20, 0.0, 0.1) == "Trend"
    assert classify_observed(-0.01, 0.30, -0.02, -0.005) == "Falsificacion"
    assert classify_observed(0.02, 0.50, -0.01, 0.05) == "Null"
    print("OK: umbrales canónicos")


def test_graceful_without_prereg(tmp_path=None):
    import tempfile
    d = tmp_path or tempfile.mkdtemp()
    assert render_prereg_section(str(d), 0.5, 0.01, 0.3, 0.6) == ""
    print("OK: sin pre-registro → sección vacía")


def test_unparseable_prereg(tmp_path=None):
    import tempfile
    d = Path(tmp_path or tempfile.mkdtemp())
    (d / "docs").mkdir(exist_ok=True)
    (d / "docs" / "PRE_REGISTRO.md").write_text("# vacío\n", encoding="utf-8")
    assert render_prereg_section(str(d), 0.5, 0.01, 0.3, 0.6) == ""
    # EDI ausente también es fail-open
    assert render_prereg_section(str(d), None, None, None, None) == ""
    print("OK: pre-registro ilegible → sección vacía")


def test_parse_prereg_spot_check():
    text = (ROOT / "09-simulaciones-edi/21_caso_salinizacion/docs/PRE_REGISTRO.md").read_text()
    parsed = parse_prereg(text)
    assert parsed is not None
    assert parsed["predicted"] == "Null", parsed
    print("OK: parse spot-check caso 21")


if __name__ == "__main__":
    test_canonical_thresholds()
    test_graceful_without_prereg()
    test_unparseable_prereg()
    test_parse_prereg_spot_check()
    test_agrees_with_verifier_on_all_prereg_cases()
    print("TODOS LOS TESTS PASAN")
