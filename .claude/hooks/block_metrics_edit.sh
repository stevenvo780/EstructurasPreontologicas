#!/usr/bin/env bash
# PreToolUse hook para Claude Code: bloquea Edit/Write/MultiEdit sobre metrics.json
# La fuente de verdad numérica solo se regenera vía validate.py (CLAUDE.md §4).
set -euo pipefail

input="$(cat || true)"

# Claude Code envía JSON: {tool_name, tool_input: {file_path, ...}, ...}
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

if [[ -z "$file_path" ]]; then
    exit 0
fi

if [[ "$file_path" == *"/09-simulaciones-edi/"*"/outputs/metrics.json" ]] || \
   [[ "$file_path" == *"/outputs/metrics.json" && "$file_path" == *"/09-simulaciones-edi/"* ]]; then
    cat <<EOF >&2
{"decision": "block", "reason": "Edición directa a metrics.json prohibida por harness. Regenera con: cd 09-simulaciones-edi/<caso>/src && python3 validate.py — CLAUDE.md §4."}
EOF
    exit 2
fi

exit 0
