"""
Auditoría criptográfica del setup del corpus.

Honestidad sobre el alcance: este módulo NO constituye pre-registro en el
sentido estricto del término. El pre-registro estricto (e.g., OSF
Registries, AsPredicted) requiere depósito de hipótesis y plan de análisis
ANTES de ver los datos, en una plataforma externa que provee garantía
temporal independiente del autor.

Lo que este módulo provee es **auditoría criptográfica de cambios**:

- Calcula SHA-256 sobre el setup de cada caso (código, sondas, parámetros,
  configuraciones, datos de entrada cuando aplica).
- Versiona ese hash junto con `git_commit_sha` y `timestamp_utc` en
  `SETUP_HASH.json` por caso y en `HASHES_PRE_EJECUCION.json` agregado.
- Permite que un evaluador externo verifique que el setup actual del
  repositorio coincide con el setup que produjo los outputs publicados.

Casos de uso válidos del módulo:
- Detectar modificaciones retroactivas del código o los parámetros
  posteriores a la ejecución reportada.
- Garantizar que un re-run sobre el commit declarado reproduce los
  mismos resultados bit-a-bit.
- Servir como cadena de custodia computacional para revisores.

Casos de uso NO válidos del módulo:
- Sustituir un pre-registro genuino en plataforma externa.
- Demostrar que las hipótesis del análisis se formularon antes de ver
  los datos (eso es imposible de verificar criptográficamente).
- Resolver la composición post-hoc del corpus (que requiere pre-registro
  en plataforma externa antes de la próxima iteración del corpus).

Combinado con la declaración honesta de composición post-hoc en bitácora
(`Bitacora/2026-04-28-cierre-pendientes/05-pre-registro-corpus-honesto.md`),
este módulo cierra la deuda L2 hasta donde es operativamente verificable
sin plataforma externa. La elevación a pre-registro estricto requiere
gestión institucional (OSF u homólogo).

Uso:

    from common.preregistration import freeze_case_setup, verify_setup_hash

    # Antes de correr el caso
    freeze_record = freeze_case_setup("04_caso_energia")

    # Mucho más tarde, para verificar que nada se modificó retroactivamente
    is_valid = verify_setup_hash("04_caso_energia", freeze_record)
"""
from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


# Sub-rutas dentro de la carpeta del caso que SÍ son setup (entran al hash)
_SETUP_PATTERNS = (
    "*.py",
    "*.json",
    "*.yaml",
    "*.yml",
    "*.toml",
    "config*.py",
    "probes/*.py",
    "data/*.csv",
    "data/*.json",
    "docs/protocolo_simulacion.md",
    "docs/arquitectura.md",
    "docs/indicadores_metricas.md",
)

# Sub-rutas dentro de la carpeta del caso que NO entran al hash (son output
# o artefactos generados durante la ejecución).
_OUTPUT_PATTERNS = (
    "outputs/*",
    "**/__pycache__/**",
    "**/*.pyc",
    "**/.cache/**",
    "**/.tmp/**",
    "*.log",
)


def _git_commit_sha(repo_root: Path) -> str | None:
    """Devuelve el commit SHA actual o None si no es git repo."""
    try:
        result = subprocess.run(
            ["git", "-C", str(repo_root), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=False,
            timeout=5,
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    return None


def _git_dirty(repo_root: Path) -> bool:
    """Devuelve True si el working tree tiene cambios sin commitear."""
    try:
        result = subprocess.run(
            ["git", "-C", str(repo_root), "status", "--porcelain"],
            capture_output=True,
            text=True,
            check=False,
            timeout=5,
        )
        return result.returncode == 0 and bool(result.stdout.strip())
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return True


def _hash_file(path: Path) -> str:
    """SHA-256 de un archivo, en hex."""
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(64 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _collect_setup_files(case_dir: Path) -> list[Path]:
    """
    Lista archivos del directorio del caso que pertenecen al setup.

    Estrategia: incluir todo bajo `case_dir` excluyendo los patterns de
    output. Más permisivo que un whitelist explícito; protege contra que
    un archivo nuevo de configuración no entre al hash por descuido.
    """
    case_dir = case_dir.resolve()
    files: list[Path] = []
    for path in sorted(case_dir.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(case_dir)
        rel_str = str(rel)

        # Excluir outputs / pycache / logs
        if rel_str.startswith("outputs/"):
            continue
        if "__pycache__" in rel.parts:
            continue
        if path.suffix in {".pyc", ".pyo", ".log"}:
            continue
        if any(part.startswith(".") for part in rel.parts):
            continue
        # No incluir el propio marker en el hash (rompería idempotencia)
        if rel.name == "SETUP_HASH.json":
            continue

        files.append(path)
    return files


def freeze_case_setup(
    case_id: str,
    repo_root: Path | None = None,
    write_marker: bool = True,
) -> dict:
    """
    Genera el record de auditoría criptográfica del setup del caso.

    Parameters
    ----------
    case_id : str
        Nombre de carpeta del caso, e.g. "04_caso_energia".
    repo_root : Path, optional
        Raíz del repositorio. Si None, se asume el padre de
        09-simulaciones-edi.
    write_marker : bool
        Si True, escribe el record en
        `<case_dir>/SETUP_HASH.json` para versionarse junto al código.

    Returns
    -------
    record : dict
        - case_id
        - timestamp_utc (ISO 8601)
        - git_commit
        - git_dirty (True si había cambios sin commitear; warning para
          el evaluador externo)
        - file_count
        - file_hashes: dict {relpath: sha256hex} ordenado
        - aggregate_hash: SHA-256 del JSON serializado de file_hashes
        - protocol_version
    """
    if repo_root is None:
        repo_root = Path(__file__).resolve().parent.parent.parent
    repo_root = Path(repo_root)

    sims_root = repo_root / "09-simulaciones-edi"
    case_dir = sims_root / case_id
    if not case_dir.is_dir():
        raise FileNotFoundError(f"caso no encontrado: {case_dir}")

    files = _collect_setup_files(case_dir)
    file_hashes = {
        str(p.relative_to(case_dir)): _hash_file(p) for p in files
    }
    aggregate = hashlib.sha256(
        json.dumps(file_hashes, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()

    record = {
        "case_id": case_id,
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "git_commit": _git_commit_sha(repo_root),
        "git_dirty": _git_dirty(repo_root),
        "file_count": len(file_hashes),
        "aggregate_hash": aggregate,
        "file_hashes": file_hashes,
        "protocol_version": "V5.1",
        "method": "sha256_recursive_with_output_exclusion",
    }

    record["audit_type"] = "cryptographic_setup_audit"
    record["disclaimer"] = (
        "Este record es auditoría criptográfica de cambios sobre el setup del "
        "caso, no pre-registro estricto en plataforma externa. Permite "
        "verificar que el setup actual coincide bit-a-bit con el setup "
        "publicado bajo el commit declarado, pero no garantiza que las "
        "hipótesis del análisis se formularan antes de ver los datos."
    )

    if write_marker:
        marker_path = case_dir / "SETUP_HASH.json"
        marker_path.write_text(
            json.dumps(record, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    return record


def verify_setup_hash(
    case_id: str,
    expected_record: dict | None = None,
    repo_root: Path | None = None,
) -> dict:
    """
    Verifica que el setup actual del caso coincida con el record dado.

    Si no se pasa expected_record, lee SETUP_HASH.json del caso.

    Returns
    -------
    verification : dict
        - match: bool — True si aggregate_hash coincide
        - changed_files: lista de archivos cuyos hashes difieren
        - missing_files: lista de archivos en el record pero no en el
          working tree
        - new_files: archivos en working tree que no estaban en el record
    """
    if repo_root is None:
        repo_root = Path(__file__).resolve().parent.parent.parent
    repo_root = Path(repo_root)

    sims_root = repo_root / "09-simulaciones-edi"
    case_dir = sims_root / case_id

    if expected_record is None:
        marker_path = case_dir / "SETUP_HASH.json"
        if not marker_path.is_file():
            return {
                "match": False,
                "error": "no SETUP_HASH.json found and no expected_record given",
            }
        expected_record = json.loads(marker_path.read_text(encoding="utf-8"))

    current = freeze_case_setup(case_id, repo_root=repo_root, write_marker=False)
    current_hashes = current["file_hashes"]
    expected_hashes = expected_record["file_hashes"]

    expected_set = set(expected_hashes)
    current_set = set(current_hashes)

    changed = sorted(
        f for f in expected_set & current_set
        if current_hashes[f] != expected_hashes[f]
    )
    missing = sorted(expected_set - current_set)
    new = sorted(current_set - expected_set)

    match = bool(
        current["aggregate_hash"] == expected_record.get("aggregate_hash")
    )

    return {
        "match": match,
        "changed_files": changed,
        "missing_files": missing,
        "new_files": new,
        "expected_aggregate_hash": expected_record.get("aggregate_hash"),
        "current_aggregate_hash": current["aggregate_hash"],
        "expected_git_commit": expected_record.get("git_commit"),
        "current_git_commit": current["git_commit"],
    }


def freeze_corpus(
    case_ids: Iterable[str],
    repo_root: Path | None = None,
    write_corpus_index: bool = True,
) -> dict:
    """
    Pre-registra todo un corpus en una sola operación.

    Returns
    -------
    corpus_record : dict
        - corpus_aggregate_hash: hash de los aggregate_hashes
        - cases: dict {case_id: record}
    """
    if repo_root is None:
        repo_root = Path(__file__).resolve().parent.parent.parent
    repo_root = Path(repo_root)

    cases_records = {}
    for cid in case_ids:
        cases_records[cid] = freeze_case_setup(cid, repo_root=repo_root)

    aggregates = {
        cid: r["aggregate_hash"] for cid, r in cases_records.items()
    }
    corpus_hash = hashlib.sha256(
        json.dumps(aggregates, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()

    corpus_record = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "git_commit": _git_commit_sha(repo_root),
        "git_dirty": _git_dirty(repo_root),
        "corpus_size": len(cases_records),
        "corpus_aggregate_hash": corpus_hash,
        "case_aggregates": aggregates,
        "protocol_version": "V5.1",
    }

    if write_corpus_index:
        index_path = repo_root / "09-simulaciones-edi" / "HASHES_PRE_EJECUCION.json"
        index_path.write_text(
            json.dumps(corpus_record, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    return corpus_record


__all__ = [
    "freeze_case_setup",
    "verify_setup_hash",
    "freeze_corpus",
]
