"""Linter de auto-indulgencia: detecta patrones que CLAUDE.md §1 prohíbe.

Patrones:
  - Versionología: V5_FINAL, v3-final, BREAKTHROUGH, etc.
  - Manierismo: 'brutalmente honesto', 'anti-paper-science', etc.
  - Plantillas spam: frases largas idénticas en >2 archivos.
  - Ratios sospechosos: 'X/X verdes' como totem.

Reporte advisory (no bloqueante por sí solo).
"""
from __future__ import annotations
import fnmatch
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from harness.lib.tesis_paths import (
    chapter_md_files, repo_root, load_config, paths_list
)


def _is_excluded(rel_path: str, patterns: list[str]) -> bool:
    """fnmatch con glob '**' soportado vía Path.match (que acepta dobles asteriscos)."""
    p = Path(rel_path)
    for pat in patterns:
        # fnmatch trata '**' como '*'; usamos PurePath.match para precisión
        if fnmatch.fnmatch(rel_path, pat):
            return True
        try:
            if p.match(pat):
                return True
        except (ValueError, IndexError):
            pass
    return False


def main() -> dict:
    cfg = load_config()
    flag_terms = cfg["self_indulgence"]["flag_terms"]
    min_phrase_len = cfg["self_indulgence"]["template_signatures"]["min_phrase_length"]
    exclude_globs = cfg["self_indulgence"].get("exclude_globs", []) or []

    # También escanear bitácora y harness mismo
    files = chapter_md_files()
    bit_dir = repo_root() / "Bitacora"
    if bit_dir.exists():
        files += sorted(bit_dir.rglob("*.md"))

    flag_hits = []
    phrase_locations: dict[str, list] = defaultdict(list)

    flag_regex = [(t, re.compile(t, re.IGNORECASE)) for t in flag_terms]

    excluded_count = 0
    for f in files:
        rel = str(f.relative_to(repo_root()))
        if _is_excluded(rel, exclude_globs):
            excluded_count += 1
            continue
        try:
            text = f.read_text(encoding="utf-8")
        except Exception:
            continue
        # Banderas léxicas
        for term, rx in flag_regex:
            for m in rx.finditer(text):
                line_no = text[:m.start()].count("\n") + 1
                flag_hits.append({
                    "file": str(f.relative_to(repo_root())),
                    "line": line_no,
                    "term": term,
                    "raw": text[max(0, m.start()-30):m.end()+30].replace("\n", " "),
                })
        # Plantilla: tomar frases largas (paragraphs ~80+ chars), normalizar
        for para in re.split(r'\n\s*\n', text):
            para = " ".join(para.split())
            if len(para) >= min_phrase_len:
                key = para[:200]  # firma por prefijo
                phrase_locations[key].append(str(f.relative_to(repo_root())))

    template_dupes = [
        {"prefix": k[:120], "files": list(set(v)), "count": len(set(v))}
        for k, v in phrase_locations.items()
        if len(set(v)) >= 3
    ]
    template_dupes.sort(key=lambda x: -x["count"])

    status = "pass"
    if flag_hits:
        status = "warn"
    if len(flag_hits) > 30 or any(d["count"] >= 5 for d in template_dupes):
        status = "fail"

    return {
        "verifier": "self_indulgence",
        "status": status,
        "files_scanned": len(files) - excluded_count,
        "files_excluded": excluded_count,
        "flag_hits_count": len(flag_hits),
        "flag_hits_sample": flag_hits[:25],
        "template_duplicates_count": len(template_dupes),
        "template_duplicates_sample": template_dupes[:10],
        "interpretation": (
            "Banderas indican manierismo / versionología / plantillas spam (CLAUDE.md §1). "
            "Cada hit debe revisarse y borrarse si no aporta contenido sustantivo. "
            "Archivos que documentan los patrones (REPORTE_AUTOINDULGENCIAS.md, V5_documentos/) "
            "están excluidos vía self_indulgence.exclude_globs."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, ensure_ascii=False))
