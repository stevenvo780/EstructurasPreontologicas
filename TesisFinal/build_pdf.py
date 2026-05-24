"""build_pdf.py — Generación de PDF a partir de Tesis.md.

Usa la librería markdown-pdf (Python puro, sin pandoc/LaTeX) para producir
un PDF razonablemente bien formateado a partir del manuscrito ensamblado.

Tras la generación, se realiza un post-proceso con PyMuPDF para añadir
paginación (header con título corto + footer con número de página). Se
hace en post-proceso porque markdown-pdf usa `fitz.Story`, que no honra
las reglas CSS `@page { @bottom-center { ... } }` de WeasyPrint.

Uso:
    source 09-simulaciones-edi/.venv/bin/activate
    python3 TesisFinal/build_pdf.py
"""

from pathlib import Path

REPO = Path(__file__).parent.parent

# Constantes de paginación (deben coincidir con los `borders` por defecto
# de markdown_pdf.Section: (36, 36, -36, -36) puntos = 12.7 mm).
HEADER_TEXT = "Estructuras Pre-Ontologicas"  # ASCII puro: helv no tiene tildes
FOOTER_FONT_SIZE = 9
HEADER_FONT_SIZE = 8
MARGIN_PT = 18  # distancia desde el borde de página al texto del header/footer


def _add_pagination(pdf_path: Path) -> None:
    """Añade número de página (footer centrado) y título corto (header
    derecho) a cada página del PDF, in-place.
    """
    import pymupdf  # alias moderno de fitz

    doc = pymupdf.open(str(pdf_path))
    total = doc.page_count
    for i, page in enumerate(doc, start=1):
        w = page.rect.width
        h = page.rect.height

        # Footer: "i / total" centrado abajo.
        footer = f"{i} / {total}"
        tw = pymupdf.get_text_length(
            footer, fontname="helv", fontsize=FOOTER_FONT_SIZE
        )
        page.insert_text(
            (w / 2 - tw / 2, h - MARGIN_PT),
            footer,
            fontname="helv",
            fontsize=FOOTER_FONT_SIZE,
            color=(0.35, 0.35, 0.35),
        )

        # Header: título corto a la derecha, color tenue. Omitido en p.1.
        if i > 1:
            tw_h = pymupdf.get_text_length(
                HEADER_TEXT, fontname="helv", fontsize=HEADER_FONT_SIZE
            )
            page.insert_text(
                (w - MARGIN_PT - tw_h, MARGIN_PT),
                HEADER_TEXT,
                fontname="helv",
                fontsize=HEADER_FONT_SIZE,
                color=(0.6, 0.6, 0.6),
            )

    # Incremental save preserva metadata, outline y enlaces ya generados.
    doc.saveIncr()
    doc.close()


def build():
    from markdown_pdf import MarkdownPdf, Section
    src = REPO / "TesisFinal" / "Tesis.md"
    out = REPO / "TesisFinal" / "Tesis.pdf"

    md = src.read_text(encoding="utf-8")
    pdf = MarkdownPdf(toc_level=2, optimize=True)

    css = """
    h1 { font-size: 24pt; color: #111; margin-top: 1.5em; }
    h2 { font-size: 18pt; color: #222; margin-top: 1.2em; }
    h3 { font-size: 14pt; color: #333; margin-top: 1em; }
    h4 { font-size: 12pt; color: #444; }
    body { font-family: Georgia, serif; font-size: 11pt; line-height: 1.45; }
    p { margin: 0.6em 0; text-align: justify; }
    table { border-collapse: collapse; margin: 1em 0; font-size: 9pt; }
    th, td { border: 1px solid #777; padding: 4px 8px; }
    th { background: #eee; }
    code { font-family: 'Courier New', monospace; font-size: 9pt;
           background: #f4f4f4; padding: 1px 3px; }
    pre { background: #f4f4f4; padding: 8px; font-size: 9pt;
          overflow-x: auto; }
    blockquote { border-left: 4px solid #aaa; margin: 0.5em 0;
                 padding: 0.2em 0.8em; color: #444; }
    """

    pdf.add_section(Section(md, toc=True, root="."), user_css=css)
    # The manuscript TOC uses explicit HTML anchors that PyMuPDF does not
    # always register as PDF destinations. Keep the generated PDF outline, but
    # skip link annotations so PDF generation remains reproducible.
    pdf.hrefs = []

    pdf.meta["title"] = "Estructuras Pre-Ontológicas"
    pdf.meta["author"] = "Jacob Agudelo, Steven Vallejo Ortiz"
    pdf.meta["subject"] = ("Realismo Irrealista Operativo y Compresión "
                          "Multiescala con Validación EDI Multidominio")
    pdf.meta["creator"] = "markdown-pdf"

    pdf.save(str(out))

    # Post-proceso: paginación (footer centrado + header derecho).
    _add_pagination(out)

    size = out.stat().st_size
    print(f"PDF generado: {out}")
    print(f"Tamaño: {size:,} bytes ({size / 1024 / 1024:.2f} MB)")


if __name__ == "__main__":
    build()
