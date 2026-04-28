"""
resource_manager.py — utilidades de cache, offline y timeout para fuentes de datos.

Variables de entorno:
  SIM_SHARED_CACHE   Ruta base de cache compartida (default: repos/Simulaciones/data_cache/shared)
  SIM_CACHE_DIR      Ruta base alternativa para cache (sobre-escribe SIM_SHARED_CACHE)
  SIM_AUTO_CACHE     Si =1, auto-cachea cuando cache_path es None
  SIM_OFFLINE        Si =1, no hace llamadas de red (solo cache o fallback)
  SIM_REFRESH        Si =1, fuerza refresh ignorando cache
  SIM_TIMEOUT        Timeout default (segundos) para requests
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Optional


def _bool_env(name: str, default: bool = False) -> bool:
    val = os.environ.get(name)
    if val is None:
        return default
    return val.strip().lower() in ("1", "true", "yes", "y", "on")


def shared_cache_dir() -> Path:
    base = os.environ.get("SIM_SHARED_CACHE")
    if base:
        return Path(base).expanduser().resolve()
    return (Path(__file__).resolve().parents[1] / "data_cache" / "shared").resolve()


def cache_root() -> Path:
    base = os.environ.get("SIM_CACHE_DIR")
    if base:
        return Path(base).expanduser().resolve()
    return shared_cache_dir()


def auto_cache_enabled() -> bool:
    return _bool_env("SIM_AUTO_CACHE", False)


def resolve_cache_path(
    cache_path: Optional[str],
    filename: str,
    subdir: Optional[str] = None,
    auto: bool = False,
) -> Optional[Path]:
    if cache_path:
        return Path(cache_path).expanduser().resolve()
    if not auto and not auto_cache_enabled():
        return None
    base = cache_root()
    if subdir:
        base = base / subdir
    return (base / filename).resolve()


def ensure_parent(path: Optional[Path]) -> None:
    if path is None:
        return
    path.parent.mkdir(parents=True, exist_ok=True)


def offline_mode(override: Optional[bool] = None) -> bool:
    return override if override is not None else _bool_env("SIM_OFFLINE", False)


def refresh_mode(override: Optional[bool] = None) -> bool:
    return override if override is not None else _bool_env("SIM_REFRESH", False)


def normalize_timeout(timeout: Optional[int], default: int = 30) -> int:
    if timeout is not None:
        return int(timeout)
    raw = os.environ.get("SIM_TIMEOUT")
    if raw:
        try:
            return int(raw)
        except ValueError:
            return default
    return default
