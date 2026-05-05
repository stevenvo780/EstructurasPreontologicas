#!/usr/bin/env bash
# Checkpoint cada N minutos: snapshot de state.json + git stash de outputs intermedios.
# Invocado por el orquestador, no por Claude Agent SDK directamente.
set -euo pipefail

REPO_ROOT="${HARNESS_REPO_ROOT:-/datos/repos/EstructurasPreontologicas}"
SNAP_DIR="$REPO_ROOT/.cache_harness/checkpoints"
mkdir -p "$SNAP_DIR"

ts="$(date +%Y%m%d-%H%M%S)"
cp "$REPO_ROOT/harness/state.json" "$SNAP_DIR/state-$ts.json" 2>/dev/null || true

# Limpiar checkpoints viejos (>20 más recientes)
ls -1t "$SNAP_DIR"/state-*.json 2>/dev/null | tail -n +21 | xargs -r rm -f

echo "checkpoint $ts ok"
