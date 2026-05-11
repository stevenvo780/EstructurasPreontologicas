#!/usr/bin/env bash
# PreToolUse hook (matcher: Bash) — bloquea spawn de instancias `claude -p`
# headless desde Bash.
#
# Política 2026-05-11: la iteración del harness se ejecuta como orquestación
# interactiva dentro de la sesión actual, usando el `Agent` tool. NO se
# spawnean instancias `claude -p` headless (perdían contexto y producían
# archivos sin orquestar; evidencia en Bitacora/2026-05-04-continuous-run/).
#
# Detecta sólo invocaciones reales del binario `claude` con flags headless;
# NO bloquea cuando "claude -p" aparece como argumento de grep/cat/find.
set -euo pipefail

input="$(cat || true)"
label="$(printf '%s' "$input" | python3 "$(dirname "$0")/_block_claude_headless_match.py" 2>/dev/null || true)"

if [[ -n "$label" ]]; then
    safe="${label//\"/\\\"}"
    cat <<JSON
{"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny", "permissionDecisionReason": "Bloqueado: '${safe}' lanza una instancia Claude headless sin orquestación. Política 2026-05-11: el modo continuo se ejecuta en la sesión interactiva vía Agent tool (/continuous-run, /continuous-run-tick)."}}
JSON
fi
exit 0
