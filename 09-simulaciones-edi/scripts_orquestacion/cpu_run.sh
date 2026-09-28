#!/usr/bin/env bash
# Compat wrapper. Usa scripts_orquestacion/run/cpu_run.sh.
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
exec "$SCRIPT_DIR/run/cpu_run.sh" "$@"
