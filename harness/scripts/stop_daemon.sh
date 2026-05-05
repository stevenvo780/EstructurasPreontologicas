#!/usr/bin/env bash
# Detiene el daemon de modo continuo (drena workers en vuelo).
set -euo pipefail
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$REPO"
PIDFILE="harness/state/daemon.pid"
if [[ ! -f "$PIDFILE" ]]; then
  echo "[stop_daemon] no hay pidfile — daemon no activo (o ya detenido)."
  exit 0
fi
PID=$(cat "$PIDFILE")
if kill -0 "$PID" 2>/dev/null; then
  echo "[stop_daemon] enviando SIGTERM a $PID (drenará workers)…"
  kill -TERM "$PID"
  for _ in {1..60}; do
    sleep 2
    kill -0 "$PID" 2>/dev/null || break
  done
  if kill -0 "$PID" 2>/dev/null; then
    echo "[stop_daemon] persistió — SIGKILL"
    kill -KILL "$PID" || true
  fi
  echo "[stop_daemon] daemon detenido."
else
  echo "[stop_daemon] pid $PID no vivo — limpiando pidfile."
fi
rm -f "$PIDFILE"
