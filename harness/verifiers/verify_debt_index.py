r"""Verificador: cada capítulo cerrado debe tener sección 'Deuda residual' fechada.

CLAUDE.md §7: 'la deuda declarada es virtud; la deuda oculta es fraude'.

Operación:
  1. Recorre capítulos.
  2. Para cada uno, busca regex ``^##\s+Deuda residual`` o variantes.
  3. Verifica que la sección tenga fecha (YYYY-MM-DD) y al menos un ítem.
  4. Construye índice JSON de toda la deuda declarada.
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from harness.lib.tesis_paths import paths_list, repo_root, load_config


DEBT_HEADING_RX = re.compile(r'^##+\s+Deuda\s+residual', re.IGNORECASE | re.MULTILINE)
DATE_RX = re.compile(r'\b(\d{4}-\d{2}-\d{2})\b')


def extract_debt_section(text: str) -> str | None:
    m = DEBT_HEADING_RX.search(text)
    if not m:
        return None
    start = m.start()
    # corta hasta el siguiente heading del mismo nivel o fin
    rest = text[m.end():]
    next_heading = re.search(r'^##\s+', rest, re.MULTILINE)
    end = m.end() + (next_heading.start() if next_heading else len(rest))
    return text[start:end]


def main() -> dict:
    cfg = load_config()
    required = set(cfg["debt_validation"]["required_chapters"])
    chapters = paths_list("chapters")
    index = {}
    missing = []
    no_date = []

    for ch in chapters:
        if not ch.exists():
            continue
        ch_name = ch.name
        # Buscar en todos los .md del capítulo
        ch_debts = []
        for md in sorted(ch.rglob("*.md")):
            try:
                text = md.read_text(encoding="utf-8")
            except Exception:
                continue
            section = extract_debt_section(text)
            if section is None:
                continue
            dates = DATE_RX.findall(section)
            items = [
                ln.strip("- *").strip()
                for ln in section.splitlines()
                if ln.strip().startswith(("-", "*"))
            ]
            entry = {
                "file": str(md.relative_to(repo_root())),
                "dates_found": dates,
                "items_count": len(items),
                "items_sample": items[:5],
            }
            ch_debts.append(entry)
            if not dates:
                no_date.append(entry)
        if ch_debts:
            index[ch_name] = ch_debts
        elif ch_name in required:
            missing.append(ch_name)

    status = "pass"
    if missing:
        status = "fail"
    elif no_date:
        status = "warn"

    return {
        "verifier": "debt_index",
        "status": status,
        "chapters_with_debt_section": list(index.keys()),
        "required_chapters_missing_debt": missing,
        "debt_sections_without_date_count": len(no_date),
        "debt_sections_without_date_sample": no_date[:5],
        "debt_index": index,
        "interpretation": (
            "CLAUDE.md §7: la deuda declarada es virtud, la oculta es fraude. "
            "Cada capítulo cerrado debe declarar su deuda residual con fecha."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, ensure_ascii=False))
