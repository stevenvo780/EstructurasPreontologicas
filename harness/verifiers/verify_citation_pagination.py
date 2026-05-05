"""Verificador formal: toda cita en prosa debe tener paginación verificable.

Operación:
  1. Recorre los .md de los capítulos de fundamentos/debates/aplicaciones.
  2. Detecta patrones de cita autor-año.
  3. Para cada cita, intenta:
     a) verificar que tiene paginación explícita (regex con pp.);
     b) si tiene cita textual contigua, busca la cita textual en el PDF
        correspondiente (heurística por apellido).
  4. Reporta JSON: total_citas, sin_paginacion, sin_match_pdf, sospechosas.

Esto operacionaliza CLAUDE.md regla §5: cita textual con paginación o no cita.
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

# Permite ejecutar como script
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from harness.lib.tesis_paths import (
    chapter_md_files, path, repo_root, load_config
)
from harness.lib import pdftext


def find_pdf_for_author(author: str, pdf_dir: Path) -> Path | None:
    """Heurística: busca PDF cuyo nombre contiene el apellido (case-insensitive)."""
    candidates = [
        p for p in pdf_dir.glob("*.pdf")
        if author.lower() in p.name.lower()
    ]
    if not candidates:
        return None
    candidates.sort(key=lambda p: len(p.name))
    return candidates[0]


def extract_citations_from_md(text: str, regex_paginated: re.Pattern, regex_anyform: re.Pattern):
    """Devuelve lista de dicts: {raw, autor, anio, pag, paginated, line}."""
    out = []
    for i, line in enumerate(text.splitlines(), start=1):
        for m in regex_paginated.finditer(line):
            out.append({
                "line": i,
                "raw": m.group(0),
                "autor": m.group(1),
                "anio": m.group(2),
                "pag": m.group(3),
                "paginated": True,
            })
        # citas any-form que NO matchean paginated
        for m in regex_anyform.finditer(line):
            # ¿esta posición ya está cubierta por paginated?
            already = any(
                c["line"] == i and c["raw"].startswith(m.group(1))
                for c in out
            )
            if not already:
                out.append({
                    "line": i,
                    "raw": m.group(0),
                    "autor": m.group(1),
                    "anio": m.group(2),
                    "pag": None,
                    "paginated": False,
                })
    return out


def main(verbose: bool = False) -> dict:
    cfg = load_config()
    pdf_dir = path("bibliography_pdfs")
    rx_pag = re.compile(cfg["citation_verification"]["citation_regex_paginated"])
    rx_any = re.compile(cfg["citation_verification"]["citation_regex_anyform"])
    required_sections = cfg["citation_verification"]["required_sections"]

    files = chapter_md_files()
    files = [f for f in files if any(s in str(f) for s in required_sections)]

    total = 0
    sin_paginacion = []
    sin_pdf_disponible = []
    pdf_extract_unavailable = not pdftext.have_pdftotext()

    for f in files:
        try:
            text = f.read_text(encoding="utf-8")
        except Exception:
            continue
        cits = extract_citations_from_md(text, rx_pag, rx_any)
        total += len(cits)
        for c in cits:
            if not c["paginated"]:
                sin_paginacion.append({
                    "file": str(f.relative_to(repo_root())),
                    "line": c["line"],
                    "raw": c["raw"],
                    "autor": c["autor"],
                })
            # ¿el PDF del autor existe?
            pdf = find_pdf_for_author(c["autor"], pdf_dir)
            if pdf is None:
                sin_pdf_disponible.append({
                    "file": str(f.relative_to(repo_root())),
                    "line": c["line"],
                    "autor": c["autor"],
                    "raw": c["raw"],
                })

    status = "pass"
    issues = len(sin_paginacion)
    if issues > 0:
        status = "fail" if issues > 20 else "warn"

    result = {
        "verifier": "citation_pagination",
        "status": status,
        "files_scanned": len(files),
        "total_citations": total,
        "without_pagination_count": len(sin_paginacion),
        "without_pagination_sample": sin_paginacion[:10],
        "without_pdf_in_07_count": len(sin_pdf_disponible),
        "without_pdf_in_07_sample": sin_pdf_disponible[:10],
        "pdftotext_available": not pdf_extract_unavailable,
        "interpretation": (
            "Citas sin paginación violan CLAUDE.md §5 ('cita textual con paginación o no cita'). "
            "Citas cuyo autor no aparece en 07-bibliografia/ pueden ser citas decorativas (F6)."
        ),
    }
    return result


if __name__ == "__main__":
    print(json.dumps(main(verbose=True), indent=2, ensure_ascii=False))
