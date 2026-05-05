#!/usr/bin/env bash
# Stop hook: snapshot de state.json al cerrar sesión / detener.
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SNAP_DIR="$REPO_ROOT/.cache_harness/checkpoints"
mkdir -p "$SNAP_DIR"

if [[ -f "$REPO_ROOT/harness/state.json" ]]; then
    ts="$(date +%Y%m%d-%H%M%S)"
    cp "$REPO_ROOT/harness/state.json" "$SNAP_DIR/state-$ts.json" 2>/dev/null || true
    # Mantener solo los 20 más recientes
    ls -1t "$SNAP_DIR"/state-*.json 2>/dev/null | tail -n +21 | xargs -r rm -f
fi

exit 0
