"""Extracción de texto de PDFs con caching local.

Estrategia: usar `pdftotext` (poppler-utils) por simplicidad y velocidad.
Cache en .cache_harness/pdftext/<sha1>.txt para no re-extraer.
"""
from __future__ import annotations
import hashlib
import subprocess
from pathlib import Path
from typing import Optional

from .tesis_paths import HARNESS_DIR

CACHE_DIR = HARNESS_DIR.parent / ".cache_harness" / "pdftext"
CACHE_DIR.mkdir(parents=True, exist_ok=True)


def _hash_file(path: Path) -> str:
    h = hashlib.sha1()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()[:16]


def have_pdftotext() -> bool:
    try:
        subprocess.run(["pdftotext", "-v"], capture_output=True, check=False, timeout=5)
        return True
    except (FileNotFoundError, subprocess.SubprocessError):
        return False


def extract_text(pdf_path: Path, max_pages: Optional[int] = None) -> Optional[str]:
    """Devuelve texto del PDF, o None si pdftotext no está disponible o falla."""
    if not pdf_path.exists():
        return None
    if not have_pdftotext():
        return None
    h = _hash_file(pdf_path)
    cache_file = CACHE_DIR / f"{h}.txt"
    if cache_file.exists():
        return cache_file.read_text(encoding="utf-8", errors="replace")
    cmd = ["pdftotext", "-layout"]
    if max_pages:
        cmd += ["-l", str(max_pages)]
    cmd += [str(pdf_path), str(cache_file)]
    try:
        subprocess.run(cmd, capture_output=True, check=True, timeout=180)
        return cache_file.read_text(encoding="utf-8", errors="replace")
    except subprocess.SubprocessError:
        return None


def search_passage(text: str, query: str, window: int = 200) -> Optional[tuple[int, str]]:
    """Busca query en text, normalizando espacios. Devuelve (offset, snippet) o None."""
    if not text or not query:
        return None
    norm_text = " ".join(text.split())
    norm_query = " ".join(query.split())
    if len(norm_query) < 8:
        return None
    idx = norm_text.lower().find(norm_query.lower())
    if idx < 0:
        return None
    start = max(0, idx - window // 2)
    end = min(len(norm_text), idx + len(norm_query) + window // 2)
    return idx, norm_text[start:end]
