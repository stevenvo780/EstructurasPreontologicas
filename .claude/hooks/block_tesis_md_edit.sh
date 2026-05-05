#!/usr/bin/env bash
# PreToolUse hook: bloquea Edit/Write/MultiEdit sobre TesisFinal/Tesis.md (es derivado).
set -euo pipefail

input="$(cat || true)"
file_path="$(echo "$input" | python3 -c '
import sys, json
try:
    d = json.load(sys.stdin)
    ti = d.get("tool_input", {}) or {}
    p = ti.get("file_path") or ti.get("notebook_path") or ti.get("path") or ""
    print(p)
except Exception:
    print("")
' 2>/dev/null)"

if [[ "$file_path" == *"/TesisFinal/Tesis.md" ]]; then
    cat <<EOF >&2
{"decision": "block", "reason": "TesisFinal/Tesis.md es derivado. Edita el capítulo fuente (00-…/ a 08-…/) y luego: python3 TesisFinal/build.py"}
EOF
    exit 2
fi

exit 0
