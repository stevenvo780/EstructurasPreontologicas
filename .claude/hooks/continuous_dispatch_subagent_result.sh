#!/usr/bin/env bash
# SubagentStop hook: si hay sesión continua activa, parsea la última línea
# `RESULT: <complete|fail> | <task_id> | <resumen>` del transcript del sub-agente
# y llama al CLI para marcar la tarea. Auto-dispatcher zero-latency.
#
# Restricciones:
# - No falla nunca (exit 0 siempre): si no hay sesión, si el transcript no tiene
#   RESULT:, si el task_id no existe, simplemente registra y sale.
# - Lee transcript_path del JSON stdin del hook (Claude Code lo provee).
# - Append-only a .cache_harness/continuous_dispatch.log para auditoría.

set -uo pipefail
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
LOG_DIR="$REPO_ROOT/.cache_harness"
LOG="$LOG_DIR/continuous_dispatch.log"
mkdir -p "$LOG_DIR"
ts() { date -u +"%Y-%m-%dT%H:%M:%SZ"; }

# Sesión continua activa?
STATE="$REPO_ROOT/harness/state/continuous_run.json"
if [[ ! -f "$STATE" ]]; then exit 0; fi
status=$(jq -r '.status // "none"' "$STATE" 2>/dev/null || echo none)
if [[ "$status" != "running" && "$status" != "paused" ]]; then exit 0; fi

# Stdin JSON del hook
hook_input=$(cat || true)
if [[ -z "$hook_input" ]]; then
    echo "$(ts) [skip] no stdin" >> "$LOG"; exit 0
fi
transcript=$(echo "$hook_input" | jq -r '.transcript_path // empty' 2>/dev/null || true)
if [[ -z "$transcript" || ! -f "$transcript" ]]; then
    echo "$(ts) [skip] no transcript_path" >> "$LOG"; exit 0
fi

# Última línea RESULT: del transcript JSONL
result_line=$(grep -oE 'RESULT: (complete|fail) \| [A-Za-z0-9._-]+ \| [^"\\]+' "$transcript" 2>/dev/null | tail -n 1 || true)
if [[ -z "$result_line" ]]; then
    echo "$(ts) [skip] sin RESULT: en $transcript" >> "$LOG"; exit 0
fi

verdict=$(echo "$result_line" | awk -F' \\| ' '{print $1}' | sed 's/^RESULT: //')
task_id=$(echo "$result_line" | awk -F' \\| ' '{print $2}')
summary=$(echo "$result_line" | awk -F' \\| ' '{for(i=3;i<=NF;i++) printf "%s%s", $i, (i==NF?"":" | ")}')

if [[ -z "$verdict" || -z "$task_id" ]]; then
    echo "$(ts) [skip] parse failed: $result_line" >> "$LOG"; exit 0
fi

# Marca solo si la tarea existe y está in_progress (idempotencia)
current=$(jq -r --arg id "$task_id" '.tasks[] | select(.id==$id) | .status' "$STATE" 2>/dev/null || true)
if [[ "$current" != "in_progress" ]]; then
    echo "$(ts) [skip] $task_id status=$current (no in_progress)" >> "$LOG"; exit 0
fi

if [[ "$verdict" == "complete" ]]; then
    /usr/bin/python3 "$REPO_ROOT/harness/cli.py" continuous complete "$task_id" --result "$summary" >> "$LOG" 2>&1 || true
    echo "$(ts) [auto-complete] $task_id :: $summary" >> "$LOG"
elif [[ "$verdict" == "fail" ]]; then
    /usr/bin/python3 "$REPO_ROOT/harness/cli.py" continuous fail "$task_id" --reason "$summary" >> "$LOG" 2>&1 || true
    echo "$(ts) [auto-fail] $task_id :: $summary" >> "$LOG"
fi
exit 0
