#!/usr/bin/env bash
# UserPromptSubmit hook: si el prompt del usuario menciona cerrar/marcar/completar
# alguna tarea que está en needs_human, recuerda al asistente que requiere firma.
set -euo pipefail

input="$(cat || true)"
prompt="$(echo "$input" | python3 -c '
import sys, json
try:
    d = json.load(sys.stdin)
    print(d.get("prompt", ""))
except Exception:
    print("")
' 2>/dev/null)"

# Si el prompt no contiene palabras de cierre, salir
if ! echo "$prompt" | grep -qiE 'cerr|complet|marc|close|done|merge|deposit|firm'; then
    exit 0
fi

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
STATE="$REPO_ROOT/harness/state.json"

if [[ ! -f "$STATE" ]]; then
    exit 0
fi

nh_count=$(python3 -c "
import json
try:
    s = json.load(open('$STATE'))
    print(len(s.get('needs_human', [])))
except Exception:
    print(0)
")

if [[ "$nh_count" != "0" ]] && [[ -n "$nh_count" ]]; then
    cat <<EOF
{"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": "Recordatorio del harness: hay $nh_count items en needs_human (ver /harness-status). Antes de marcar tareas como completas, verifica que no estén en esa lista. CLAUDE.md §2: una tarea solo se cierra si sobrevive a pregunta crítica hostil — los items needs_human son los que esperan precisamente esa firma humana."}}
EOF
fi

exit 0
