#!/usr/bin/env bash
# PostToolUse hook (matcher: Bash con validate.py): tras re-ejecutar un caso EDI,
# verifica drift de hashes y advierte si la prosa quedó desactualizada.
set -euo pipefail

input="$(cat || true)"

cmd="$(echo "$input" | python3 -c '
import sys, json
try:
    d = json.load(sys.stdin)
    print((d.get("tool_input", {}) or {}).get("command", ""))
except Exception:
    print("")
' 2>/dev/null)"

# Solo actuar si el comando ejecutó validate.py de un caso
if [[ "$cmd" != *"validate.py"* ]] || [[ "$cmd" != *"09-simulaciones-edi"* ]]; then
    exit 0
fi

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$REPO_ROOT"

# Ejecuta verificadores en background y advierte
python3 harness/cli.py verify --replay-hash --json 2>/dev/null > /tmp/_post_validate_hash.json || true
drift=$(python3 -c "
import json
try:
    d = json.load(open('/tmp/_post_validate_hash.json'))
    r = d.get('replay_hash', d) if isinstance(d, dict) else {}
    print(r.get('drift_count', 0))
except Exception:
    print(0)
")

if [[ "$drift" != "0" ]] && [[ -n "$drift" ]]; then
    cat <<EOF
{"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": "WARN: tras validate.py se detectó drift de hashes ($drift casos). Considera /verify-prose-json para revisar si la prosa de la tesis cita cifras viejas. Si el drift es intencional, actualiza HASHES_PRE_EJECUCION.json baseline."}}
EOF
fi

exit 0
