#!/usr/bin/env python3
"""
Congela criptográficamente los 10 casos del corpus inter-escala.

Análogo a freeze_setup.py pero apunta a corpus_multiescala/ y emite
HASHES_PRE_EJECUCION_INTER_ESCALA.json en esa carpeta.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MULTI = ROOT / "corpus_multiescala"


def _hash_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(64 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _git_sha(repo: Path) -> str | None:
    try:
        r = subprocess.run(
            ["git", "-C", str(repo), "rev-parse", "HEAD"],
            capture_output=True, text=True, timeout=5
        )
        return r.stdout.strip() if r.returncode == 0 else None
    except Exception:
        return None


def _collect(case_dir: Path) -> list[Path]:
    files = []
    for p in sorted(case_dir.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(case_dir)
        if rel.parts[0] == "outputs":
            continue
        if "__pycache__" in rel.parts:
            continue
        if p.suffix in {".pyc", ".pyo", ".log"}:
            continue
        if rel.name == "SETUP_HASH.json":
            continue
        files.append(p)
    return files


def freeze_case(case_dir: Path, repo: Path) -> dict:
    files = _collect(case_dir)
    fh = {str(p.relative_to(case_dir)): _hash_file(p) for p in files}
    aggregate = hashlib.sha256(
        json.dumps(fh, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    record = {
        "case_id": case_dir.name,
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "git_commit": _git_sha(repo),
        "file_count": len(fh),
        "aggregate_hash": aggregate,
        "file_hashes": fh,
        "protocol_version": "V5.3 (inter-escala)",
    }
    (case_dir / "SETUP_HASH.json").write_text(
        json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    return record


def main() -> int:
    repo = ROOT.parent
    cases = sorted([d for d in MULTI.iterdir() if d.is_dir() and d.name[:2].isdigit()])
    aggregates = {}
    for cd in cases:
        rec = freeze_case(cd, repo)
        aggregates[cd.name] = rec["aggregate_hash"]
        print(f"  ✓ {cd.name}: {rec['aggregate_hash'][:12]}...")
    corpus_hash = hashlib.sha256(
        json.dumps(aggregates, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    out = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "git_commit": _git_sha(repo),
        "corpus_size": len(aggregates),
        "corpus_aggregate_hash": corpus_hash,
        "case_aggregates": aggregates,
        "protocol_version": "V5.3 (inter-escala)",
    }
    (MULTI / "HASHES_PRE_EJECUCION_INTER_ESCALA.json").write_text(
        json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"\n✓ Corpus inter-escala congelado: {corpus_hash[:16]}...")
    return 0


if __name__ == "__main__":
    sys.exit(main())
