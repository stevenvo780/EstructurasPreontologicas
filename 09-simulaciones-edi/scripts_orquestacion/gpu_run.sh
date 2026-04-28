#!/usr/bin/env bash
# Compat wrapper. Usa repos/scripts/run/gpu_run.sh.
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
exec "$SCRIPT_DIR/run/gpu_run.sh" "$@"
