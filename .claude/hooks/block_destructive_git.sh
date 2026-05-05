#!/usr/bin/env bash
# PreToolUse hook sobre Bash: bloquea operaciones git destructivas sin confirmación humana.
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

if [[ -z "$cmd" ]]; then
    exit 0
fi

# Patrones bloqueados
patterns=(
    "git reset --hard"
    "git push --force"
    "git push -f"
    "git branch -D"
    "git checkout -- "
    "git restore --staged --worktree"
    "git clean -f"
    "rm -rf .git"
)

for p in "${patterns[@]}"; do
    if [[ "$cmd" == *"$p"* ]]; then
        cat <<EOF >&2
{"decision": "block", "reason": "Operación git destructiva bloqueada: '$p'. Si el usuario lo pidió explícitamente, ejecutarlo manualmente fuera del harness."}
EOF
        exit 2
    fi
done

exit 0
