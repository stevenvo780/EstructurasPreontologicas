"""Tests unitarios de los verificadores formales contra fixtures conocidas.

Cada test:
  1. Aplica las funciones internas del verificador a una fixture conocida.
  2. Verifica que detecta lo que debe detectar.
  3. Verifica que NO levanta falsos positivos sobre fixtures limpias.

Ejecuta sin pytest: `python3 harness/tests/test_verifiers.py`
Con pytest: `python3 -m pytest harness/tests/ -v`
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from harness.verifiers import (
    verify_decorative_citations as v_dec,
    verify_self_indulgence as v_ind,
    verify_debt_index as v_debt,
    verify_citation_pagination as v_cit,
    verify_harness_compliance as v_compl,
)
from harness.lib.tesis_paths import load_config

FIXTURES = Path(__file__).parent / "fixtures"


# ----- helpers -----------------------------------------------------------

def _load(name: str) -> str:
    return (FIXTURES / name).read_text(encoding="utf-8")


# ----- decorative_citations ---------------------------------------------

def test_decorative_citations_detects_authority_invocation():
    text = _load("chapter_with_decorative_citation.md")
    paragraphs = v_dec.split_paragraphs(text)
    decorative_found = False
    list_dump_found = False
    for line_no, para in paragraphs:
        cits = v_dec.CITATION_RX.findall(para)
        if not cits:
            continue
        has_quote = bool(v_dec.QUOTE_RX.search(para)) or bool(v_dec.BLOCKQUOTE_RX.search(para))
        has_engagement = bool(v_dec.ENGAGEMENT_RX.search(para))
        list_match = v_dec.LIST_OF_AUTHORS_RX.search(para)
        if list_match and len(cits) >= 3:
            list_dump_found = True
        elif not has_quote and not has_engagement:
            decorative_found = True
    assert list_dump_found or decorative_found, \
        "fixture should trigger either list-dump or decorative detection"


def test_decorative_citations_passes_paginated_engagement():
    text = _load("chapter_with_paginated_citation.md")
    paragraphs = v_dec.split_paragraphs(text)
    decoratives = []
    for line_no, para in paragraphs:
        cits = v_dec.CITATION_RX.findall(para)
        if not cits:
            continue
        has_quote = bool(v_dec.QUOTE_RX.search(para)) or bool(v_dec.BLOCKQUOTE_RX.search(para))
        has_engagement = bool(v_dec.ENGAGEMENT_RX.search(para))
        list_match = v_dec.LIST_OF_AUTHORS_RX.search(para)
        if not (list_match and len(cits) >= 3):
            if not has_quote and not has_engagement:
                decoratives.append((line_no, para))
    assert not decoratives, \
        f"fixture with quotes + engagement should not flag decoratives: {decoratives}"


# ----- self_indulgence ---------------------------------------------------

def test_self_indulgence_detects_versionology_and_mannerism():
    text = _load("chapter_with_indulgence.md")
    cfg = load_config()
    flag_terms = cfg["self_indulgence"]["flag_terms"]
    flag_regex = [(t, re.compile(t, re.IGNORECASE)) for t in flag_terms]
    hits = []
    for term, rx in flag_regex:
        if rx.search(text):
            hits.append(term)
    assert "brutalmente honesto" in hits, "should detect 'brutalmente honesto'"
    assert any("8/8 verdes" in h for h in hits), "should detect '8/8 verdes'"
    assert any("BREAKTHROUGH" in h or "breakthrough" in h.lower() for h in hits), \
        "should detect BREAKTHROUGH"


def test_self_indulgence_passes_clean_text():
    text = _load("chapter_with_paginated_citation.md")
    cfg = load_config()
    flag_terms = cfg["self_indulgence"]["flag_terms"]
    flag_regex = [(t, re.compile(t, re.IGNORECASE)) for t in flag_terms]
    hits = [t for t, rx in flag_regex if rx.search(text)]
    assert not hits, f"clean fixture should not trigger self-indulgence: {hits}"


# ----- debt_index --------------------------------------------------------

def test_debt_index_detects_section_with_date():
    text = _load("chapter_with_debt_section.md")
    section = v_debt.extract_debt_section(text)
    assert section is not None, "fixture has Deuda residual section"
    dates = v_debt.DATE_RX.findall(section)
    assert dates, f"section should contain date: {section[:200]}"
    assert dates[0] == "2026-05-04"


def test_debt_index_returns_none_when_section_absent():
    text = _load("chapter_with_paginated_citation.md")
    section = v_debt.extract_debt_section(text)
    assert section is None, "this fixture has no Deuda residual section"


# ----- citation_pagination ----------------------------------------------

def test_citation_pagination_extracts_paginated():
    text = _load("chapter_with_paginated_citation.md")
    cfg = load_config()
    rx_pag = re.compile(cfg["citation_verification"]["citation_regex_paginated"])
    rx_any = re.compile(cfg["citation_verification"]["citation_regex_anyform"])
    cits = v_cit.extract_citations_from_md(text, rx_pag, rx_any)
    paginated = [c for c in cits if c["paginated"]]
    assert paginated, "fixture has paginated citations"
    bunge = [c for c in paginated if c["autor"] == "Bunge"]
    assert bunge, "should extract Bunge with page"
    assert bunge[0]["pag"] == "245"


def test_citation_pagination_flags_unpaginated():
    text = _load("chapter_with_decorative_citation.md")
    cfg = load_config()
    rx_pag = re.compile(cfg["citation_verification"]["citation_regex_paginated"])
    rx_any = re.compile(cfg["citation_verification"]["citation_regex_anyform"])
    cits = v_cit.extract_citations_from_md(text, rx_pag, rx_any)
    unpaginated = [c for c in cits if not c["paginated"]]
    assert unpaginated, "decorative fixture should have unpaginated citations"


# ----- harness_compliance (auto-auditoría) ------------------------------

def test_compliance_runs_without_error():
    r = v_compl.main()
    assert "status" in r
    assert "issues_by_severity" in r
    # Estado debe ser pass/warn/fail (no error)
    assert r["status"] in ("pass", "warn", "fail")


def test_compliance_finds_all_agents():
    r = v_compl.main()
    # Debe haber auditado al menos 10 agentes
    assert r["agents_audited"] >= 10, \
        f"expected >=10 agents, got {r['agents_audited']}"


# ----- runner sin pytest -------------------------------------------------

def _run_all():
    """Ejecuta todos los tests sin pytest."""
    failed = []
    passed = []
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                passed.append(name)
                print(f"  PASS  {name}")
            except AssertionError as e:
                failed.append((name, str(e)))
                print(f"  FAIL  {name}: {e}")
            except Exception as e:
                failed.append((name, f"{type(e).__name__}: {e}"))
                print(f"  ERROR {name}: {type(e).__name__}: {e}")
    print(f"\n{len(passed)} passed, {len(failed)} failed")
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(_run_all())
