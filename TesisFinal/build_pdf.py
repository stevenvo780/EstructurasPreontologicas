"""Genera y verifica el PDF del manuscrito con Pandoc + XeLaTeX.

Uso:
    python3 TesisFinal/build.py
    python3 TesisFinal/build_pdf.py
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import pymupdf


REPO = Path(__file__).resolve().parent.parent
SOURCE = REPO / "TesisFinal" / "Tesis.md"
OUTPUT = REPO / "TesisFinal" / "Tesis.pdf"
DELIVERY = REPO / "output" / "pdf" / "Estructuras_Pre_Ontologicas_2026-07-17.pdf"


def _verify_pdf(path: Path) -> tuple[int, int]:
    """Verifica estructura básica y ausencia de texto fuera de página."""
    doc = pymupdf.open(path)
    if doc.page_count == 0:
        raise RuntimeError("El PDF no contiene páginas")

    clipped_pages: set[int] = set()
    for page_index, page in enumerate(doc):
        width = page.rect.width
        for x0, _y0, x1, _y1, _text, *_ in page.get_text("words"):
            if x0 < 0 or x1 > width + 0.2:
                clipped_pages.add(page_index + 1)
                break

    pages = doc.page_count
    doc.close()
    if clipped_pages:
        values = ", ".join(map(str, sorted(clipped_pages)))
        raise RuntimeError(f"Texto fuera del área de página en: {values}")
    return pages, path.stat().st_size


def build() -> None:
    if not SOURCE.exists():
        raise FileNotFoundError(SOURCE)

    command = [
        "pandoc",
        str(SOURCE),
        "--from=gfm+tex_math_dollars",
        f"--lua-filter={REPO / 'TesisFinal' / 'pdf_sanitize.lua'}",
        f"--include-in-header={REPO / 'TesisFinal' / 'pdf_header.tex'}",
        "--pdf-engine=xelatex",
        "-V", "documentclass=report",
        "-V", "papersize=a4",
        "-V", "geometry:margin=1.8cm",
        "-V", "mainfont=DejaVu Serif",
        "-V", "sansfont=DejaVu Sans",
        "-V", "monofont=DejaVu Sans Mono",
        "-V", "fontsize=10pt",
        "-V", "colorlinks=true",
        "-V", "linkcolor=blue",
        "-V", "urlcolor=blue",
        "-V", "lang=es-CO",
        "-M", "title=Estructuras Pre-Ontológicas",
        "-M", "author=Jacob Agudelo; Steven Vallejo Ortiz",
        f"--resource-path={REPO}",
        "-o", str(OUTPUT),
    ]
    subprocess.run(command, cwd=REPO, check=True)

    pages, size = _verify_pdf(OUTPUT)
    DELIVERY.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(OUTPUT, DELIVERY)

    print(f"PDF generado: {OUTPUT}")
    print(f"Entrega: {DELIVERY}")
    print(f"Páginas: {pages}")
    print(f"Tamaño: {size:,} bytes ({size / 1024 / 1024:.2f} MB)")
    print("Verificación geométrica: 0 páginas con texto recortado")


if __name__ == "__main__":
    build()
