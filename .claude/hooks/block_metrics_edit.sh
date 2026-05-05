#!/usr/bin/env bash
# PreToolUse hook (matcher: Edit|Write|MultiEdit) — bloquea ediciones a metrics.json.
# La fuente de verdad numérica solo se regenera vía validate.py (CLAUDE.md §4).
#
# Output canónico Claude Code: JSON a stdout con permissionDecision="deny".
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

if [[ -z "$file_path" ]]; then
    exit 0
fi

if [[ "$file_path" == *"/09-simulaciones-edi/"*"/outputs/metrics.json" ]]; then
    cat <<'JSON'
{"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny", "permissionDecisionReason": "Edición directa a metrics.json prohibida por harness. Regenera con: cd 09-simulaciones-edi/<caso>/src && python3 validate.py — CLAUDE.md §4 (cada cifra debe ser regenerable con su comando)."}}
JSON
    exit 0
fi

exit 0
