#!/usr/bin/env bash
# PreToolUse hook: bloquea edición directa a TesisFinal/Tesis.md (es derivado).
# Las fuentes son los capítulos 00-…/ a 08-…/.
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

if [[ "$file_path" == *"/TesisFinal/Tesis.md" ]]; then
    echo "BLOCKED: edición directa a TesisFinal/Tesis.md prohibida (es derivado)." >&2
    echo "Edita el capítulo fuente (00-…/ a 08-…/) y luego: python3 TesisFinal/build.py" >&2
    exit 2
fi

exit 0
