"""Verificador formal: detecta posibles 'citas decorativas' (CLAUDE.md §5, F6).

Heurística:
  Una cita es 'decorativa' si:
    - Aparece en un párrafo SIN ninguna comilla (")  ni cita en bloque (>) ni
      mención del argumento del autor (verbos como 'sostiene', 'argumenta',
      'rechaza', 'concede', 'plantea', 'distingue', 'afirma', 'critica').
    - O aparece en una lista de >3 autores agrupados sin engagement individual.

No es decisión final — flagea para revisión humana o sub-agente philosophical-reader.
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from harness.lib.tesis_paths import chapter_md_files, repo_root, load_config


ENGAGEMENT_VERBS = [
    "sostiene", "argumenta", "rechaza", "concede", "plantea", "distingue",
    "afirma", "critica", "cuestiona", "defiende", "objeta", "refuta",
    "propone", "muestra", "demuestra", "señala", "reconoce", "admite",
    "niega", "discute", "matiza", "amplía", "refina", "extiende",
    "contradice", "complementa", "completa", "reformula",
]
ENGAGEMENT_RX = re.compile(
    r'\b(' + '|'.join(ENGAGEMENT_VERBS) + r')\b',
    re.IGNORECASE,
)
QUOTE_RX = re.compile(r'["""].{20,}["""]')
BLOCKQUOTE_RX = re.compile(r'^\s*>\s+', re.MULTILINE)
CITATION_RX = re.compile(
    r'\(([A-ZÁÉÍÓÚÑ][a-záéíóúñ\-]+)(?:\s+et\s+al\.?)?[\s,]+(\d{4})',
)
LIST_OF_AUTHORS_RX = re.compile(
    r'\b((?:[A-ZÁÉÍÓÚÑ][a-záéíóúñ\-]+,?\s*){4,})',
)


def split_paragraphs(text: str) -> list[tuple[int, str]]:
    """Devuelve (line_start, paragraph_text)."""
    paragraphs = []
    line_no = 1
    current_lines = []
    current_start = 1
    for line in text.split("\n"):
        if line.strip() == "":
            if current_lines:
                paragraphs.append((current_start, "\n".join(current_lines)))
                current_lines = []
            current_start = line_no + 1
        else:
            if not current_lines:
                current_start = line_no
            current_lines.append(line)
        line_no += 1
    if current_lines:
        paragraphs.append((current_start, "\n".join(current_lines)))
    return paragraphs


def main() -> dict:
    files = chapter_md_files()
    decorative_suspect = []
    list_dump = []
    total_citations_in_text = 0

    for f in files:
        try:
            text = f.read_text(encoding="utf-8")
        except Exception:
            continue
        for line_start, para in split_paragraphs(text):
            cits = CITATION_RX.findall(para)
            if not cits:
                continue
            total_citations_in_text += len(cits)
            has_quote = bool(QUOTE_RX.search(para)) or bool(BLOCKQUOTE_RX.search(para))
            has_engagement = bool(ENGAGEMENT_RX.search(para))
            # Lista de autores agrupados (Bunge, Dennett, Simondon, Chalmers...)
            list_match = LIST_OF_AUTHORS_RX.search(para)
            if list_match and len(cits) >= 3:
                list_dump.append({
                    "file": str(f.relative_to(repo_root())),
                    "line": line_start,
                    "authors_count": len(cits),
                    "snippet": para[:200].replace("\n", " "),
                })
                continue
            if not has_quote and not has_engagement:
                decorative_suspect.append({
                    "file": str(f.relative_to(repo_root())),
                    "line": line_start,
                    "citations": [f"{a} {y}" for a, y in cits],
                    "snippet": para[:200].replace("\n", " "),
                    "reason": "sin cita textual entre comillas y sin verbo de engagement",
                })

    status = "pass"
    if decorative_suspect:
        status = "warn" if len(decorative_suspect) < 10 else "fail"

    return {
        "verifier": "decorative_citations",
        "status": status,
        "files_scanned": len(files),
        "total_citations_in_paragraphs": total_citations_in_text,
        "decorative_suspect_count": len(decorative_suspect),
        "decorative_suspect_sample": decorative_suspect[:15],
        "list_dump_count": len(list_dump),
        "list_dump_sample": list_dump[:10],
        "interpretation": (
            "Citas en párrafos SIN comillas ni verbos de engagement (CLAUDE.md §5, F6). "
            "Listas de >3 autores agrupados (\"X, Y, Z, W sostienen…\") sin engagement individual "
            "son sospechosas de invocación de autoridad sin argumento."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, ensure_ascii=False))
