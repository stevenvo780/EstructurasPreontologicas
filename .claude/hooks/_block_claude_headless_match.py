#!/usr/bin/env python3
"""Detector de spawn `claude -p` headless. Usado por block_claude_headless.sh.

Lee JSON del hook por stdin, imprime un label si el comando dispara
la política, o nada si pasa.

Patrones bloqueados (solo en posición de comando, no como argumento):
  - bash harness/scripts/run_daemon.sh ...
  - ./harness/scripts/run_daemon.sh ...
  - python3 harness/cli.py continuous daemon ...
  - claude -p / claude --print / claude --output-format ...
"""
from __future__ import annotations
import json
import re
import sys


def main() -> int:
    try:
        d = json.load(sys.stdin)
    except Exception:
        return 0
    cmd = (d.get("tool_input", {}) or {}).get("command", "")
    if not cmd:
        return 0

    # "Posición de comando": inicio, o tras separador shell.
    # Incluye opcional VAR=valor en prefijo.
    sep = r"(?:^|[\s;&|`\n]|\$\()"
    var_prefix = r"(?:[A-Za-z_][A-Za-z0-9_]*=\S+\s+)*"

    patterns: list[tuple[str, str]] = [
        (
            sep + r"\s*bash\s+\S*run_daemon\.sh\b",
            "bash harness/scripts/run_daemon.sh",
        ),
        (
            sep + r"\s*\./?harness/scripts/run_daemon\.sh\b",
            "./harness/scripts/run_daemon.sh",
        ),
        # Sólo bloquear `continuous daemon` cuando aparece tras cli.py
        # (es decir, una invocación real del CLI, no un grep/sed literal).
        (
            r"cli\.py\s+continuous\s+daemon\b",
            "python3 harness/cli.py continuous daemon",
        ),
        (
            sep + r"\s*" + var_prefix + r"claude\s+(?:-p\b|--print\b|--output-format\b)",
            "claude -p / --print / --output-format",
        ),
    ]
    for pat, label in patterns:
        if re.search(pat, cmd):
            print(label)
            return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
