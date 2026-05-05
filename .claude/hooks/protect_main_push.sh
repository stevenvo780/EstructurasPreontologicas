#!/usr/bin/env bash
# PreToolUse hook (matcher: Bash) — bloquea push directo a main sin confirmación humana.
#
# El harness no debe pushear a main por sí solo: cada cambio sustantivo debería
# pasar por rama+PR para revisión humana antes de fusionar al canon.
#
# Detección: extrae solo los comandos REALES (separados por &&/;/|, ignorando
# heredocs y strings literales) y bloquea si alguno es 'git push' apuntando a main.
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

# Análisis estructural del comando: usamos Python para tokenizar correctamente
# y detectar git push como comando REAL ejecutado, no como substring en heredoc/string.
dangerous="$(python3 - <<'PY' "$cmd"
import sys, re, shlex

cmd = sys.argv[1]

# Quitar heredocs (<<EOF ... EOF) que son contenido literal, no comandos.
cmd = re.sub(r"<<\s*'?(\w+)'?.*?\n\1\s*$", "", cmd, flags=re.DOTALL | re.MULTILINE)
# También quitar contenido entre $(cat <<'EOF' ... EOF)
cmd = re.sub(r"\$\(cat\s+<<\s*'?(\w+)'?.*?\1\s*\)", "", cmd, flags=re.DOTALL)

# Separar en comandos individuales por &&, ||, ;, | (a nivel superficial)
parts = re.split(r"&&|\|\||;|\|", cmd)

def is_dangerous(part: str) -> bool:
    p = part.strip()
    # ¿Empieza con git push?
    if not re.match(r"^\s*git\s+push\b", p):
        return False
    # ¿Apunta explícitamente a main/master, --all, o sin destino con rama actual main?
    if re.search(r"\bmain\b|\bmaster\b", p):
        return True
    if "--all" in p:
        return True
    # Push sin destino → consultar rama actual
    if re.match(r"^\s*git\s+push\s*(-u\s*)?(origin\s*)?$", p):
        import subprocess
        try:
            br = subprocess.check_output(
                ["git", "rev-parse", "--abbrev-ref", "HEAD"],
                text=True, timeout=2,
            ).strip()
            if br in ("main", "master"):
                return True
        except Exception:
            pass
    return False

print("1" if any(is_dangerous(p) for p in parts) else "0")
PY
)"

if [[ "$dangerous" == "1" ]]; then
    cat <<'JSON'
{"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny", "permissionDecisionReason": "Push directo a main bloqueado por el harness. El usuario debe (a) crear rama: git checkout -b harness/<topic> && git push -u origin harness/<topic>, o (b) autorizar explícitamente este push diciendo: 'autorizo push a main'."}}
JSON
    exit 0
fi

exit 0
