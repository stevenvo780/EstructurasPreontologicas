#!/usr/bin/env python3
"""
CLI para congelar el setup de uno o todos los casos del corpus.

Uso:
    python3 scripts/freeze_setup.py --case 04_caso_energia
    python3 scripts/freeze_setup.py --all
    python3 scripts/freeze_setup.py --verify 04_caso_energia
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from common.preregistration import (
    freeze_case_setup,
    freeze_corpus,
    verify_setup_hash,
)


def list_cases(sims_root: Path) -> list[str]:
    return sorted(
        d.name
        for d in sims_root.iterdir()
        if d.is_dir() and d.name[:2].isdigit() and "_caso_" in d.name
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", help="Caso individual a congelar (e.g. 04_caso_energia)")
    parser.add_argument("--all", action="store_true", help="Congelar todo el corpus")
    parser.add_argument("--verify", help="Verificar setup contra SETUP_HASH.json existente")
    args = parser.parse_args()

    sims_root = ROOT
    if args.verify:
        result = verify_setup_hash(args.verify)
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0 if result.get("match") else 1

    if args.case:
        record = freeze_case_setup(args.case)
        print(f"✓ {args.case} congelado")
        print(f"  files: {record['file_count']}")
        print(f"  aggregate_hash: {record['aggregate_hash'][:16]}...")
        print(f"  git_commit: {record.get('git_commit', '?')}")
        print(f"  git_dirty: {record.get('git_dirty', '?')}")
        return 0

    if args.all:
        cases = list_cases(sims_root)
        print(f"Congelando {len(cases)} casos del corpus...")
        record = freeze_corpus(cases)
        print(f"✓ Corpus congelado: {record['corpus_size']} casos")
        print(f"  corpus_aggregate_hash: {record['corpus_aggregate_hash'][:16]}...")
        print(f"  git_commit: {record.get('git_commit', '?')}")
        print(f"  git_dirty: {record.get('git_dirty', '?')}")
        if record.get("git_dirty"):
            print(
                "  ⚠️  Working tree con cambios sin commitear. Para garantía "
                "criptográfica completa, commitear primero y re-correr."
            )
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
