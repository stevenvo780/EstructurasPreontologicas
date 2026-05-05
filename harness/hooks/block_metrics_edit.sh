#!/usr/bin/env bash
# PreToolUse hook: bloquea edición directa a outputs/metrics.json.
# La fuente de verdad numérica solo se regenera vía validate.py.
#
# Uso: invocado por Claude Agent SDK con stdin = JSON {tool, params}.
# Sale con código != 0 si la edición está prohibida.
set -euo pipefail

input="$(cat || true)"
file_path="$(echo "$input" | python3 -c 'import sys, json
try:
    d = json.load(sys.stdin)
    p = d.get("file_path") or d.get("params", {}).get("file_path") or ""
    print(p)
except Exception:
    print("")
' 2>/dev/null || true)"

if [[ -z "$file_path" ]]; then
    exit 0
fi

# Bloquear si edita metrics.json bajo 09-simulaciones-edi/
if [[ "$file_path" == *"/09-simulaciones-edi/"*"/outputs/metrics.json" ]]; then
    echo "BLOCKED: edición directa a metrics.json prohibida." >&2
    echo "Regenera con: cd 09-simulaciones-edi/<caso>/src && python3 validate.py" >&2
    echo "Razón: CLAUDE.md §4 — cada cifra debe ser regenerable con su comando." >&2
    exit 2
fi

exit 0
