"""Resolución de paths canónicos del repo de tesis."""
from __future__ import annotations
import os
import yaml
from pathlib import Path
from functools import lru_cache


HARNESS_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = HARNESS_DIR / "config.yaml"


@lru_cache(maxsize=1)
def load_config() -> dict:
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def repo_root() -> Path:
    cfg = load_config()
    root = Path(cfg["repo_root"]).resolve()
    if not root.exists():
        # Fallback: subir desde harness/
        root = HARNESS_DIR.parent
    return root


def path(key: str) -> Path:
    """Resuelve un path declarado en config.paths.<key> contra repo_root."""
    cfg = load_config()
    p = cfg["paths"][key]
    if isinstance(p, list):
        raise ValueError(f"path '{key}' es lista; usa paths_list")
    return repo_root() / p


def paths_list(key: str) -> list[Path]:
    cfg = load_config()
    items = cfg["paths"][key]
    if not isinstance(items, list):
        raise ValueError(f"path '{key}' no es lista")
    return [repo_root() / p for p in items]


def glob(key: str) -> list[Path]:
    cfg = load_config()
    pattern = cfg["paths"][key]
    return sorted(repo_root().glob(pattern))


def chapter_md_files() -> list[Path]:
    """Lista todos los .md de los capítulos de la tesis."""
    files: list[Path] = []
    for chapter in paths_list("chapters"):
        if chapter.exists():
            files.extend(sorted(chapter.rglob("*.md")))
    return files
