#!/usr/bin/env bash
# SessionStart hook: carga estado del harness al inicio de cada sesión Claude Code.
# Imprime resumen al usuario para que sepa qué dejó pendiente.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
STATE="$REPO_ROOT/harness/state.json"

if [[ ! -f "$STATE" ]]; then
    exit 0
fi

# Output JSON que Claude Code interpreta
python3 - "$STATE" <<'PY'
import json, sys
p = sys.argv[1]
try:
    with open(p) as f:
        s = json.load(f)
except Exception:
    sys.exit(0)

passes = s.get("passes", [])
last = passes[-1] if passes else None
nh = s.get("needs_human", [])

lines = ["# Harness state al iniciar sesión\n"]
if last:
    lines.append(f"- Última pasada: {last.get('timestamp')} (modo {last.get('mode')})")
    fails = [v for v, st in (last.get('verifier_summary') or {}).items() if st in ('fail', 'error')]
    warns = [v for v, st in (last.get('verifier_summary') or {}).items() if st == 'warn']
    if fails:
        lines.append(f"- Verificadores que fallaban: {', '.join(fails)}")
    if warns:
        lines.append(f"- Verificadores con warning: {', '.join(warns)}")
else:
    lines.append("- Sin pasadas previas — ejecutar /harness-pass para baseline.")

if nh:
    lines.append(f"- Items needs_human pendientes: {len(nh)}")
    for item in nh[:5]:
        lines.append(f"  - {item}")

import json as J
out = {"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": "\n".join(lines)}}
print(J.dumps(out))
PY
