#!/usr/bin/env bash
# Launcher del daemon de modo continuo.
#
# Uso:
#   harness/scripts/run_daemon.sh <horas> [parallel]
#
# Ejemplos:
#   harness/scripts/run_daemon.sh 80         # 80h, 4 workers
#   harness/scripts/run_daemon.sh 150 6      # 150h, 6 workers paralelos
#
# Sobrevive cierre de terminal (nohup), survives Claude Code session crash.
# Stop:  kill $(cat harness/state/daemon.pid)
# Logs:  Bitacora/<fecha>-continuous-run/daemon.log
# Outs:  harness/state/daemon.out (stdout/stderr crudos)

set -euo pipefail

HOURS="${1:-80}"
PARALLEL="${2:-4}"
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$REPO"

mkdir -p harness/state
PIDFILE="harness/state/daemon.pid"

if [[ -f "$PIDFILE" ]]; then
  OLD_PID=$(cat "$PIDFILE")
  if kill -0 "$OLD_PID" 2>/dev/null; then
    echo "[run_daemon] daemon ya activo (pid=$OLD_PID). Detenlo primero:"
    echo "    kill $OLD_PID"
    exit 1
  else
    echo "[run_daemon] pidfile huérfano — limpiando"
    rm -f "$PIDFILE"
  fi
fi

# Si no hay sesión continua activa, iniciarla
if [[ ! -f harness/state/continuous_run.json ]]; then
  /usr/bin/python3 harness/cli.py continuous start --hours "$HOURS"
fi

# Replenish inicial: tareas frescas desde verificadores
/usr/bin/python3 harness/cli.py continuous replenish --max-new 200 || true

OUT="harness/state/daemon.out"
echo "[run_daemon] arrancando daemon: hours=$HOURS parallel=$PARALLEL"
echo "[run_daemon] stdout/stderr → $OUT"
echo "[run_daemon] log estructurado → Bitacora/$(date +%F)-continuous-run/daemon.log"

nohup /usr/bin/python3 harness/cli.py continuous daemon \
      --hours "$HOURS" \
      --parallel "$PARALLEL" \
      --replenish-threshold 2 \
      --poll-seconds 5 \
      > "$OUT" 2>&1 &

DPID=$!
echo "$DPID" > "$PIDFILE"
disown
sleep 1

if kill -0 "$DPID" 2>/dev/null; then
  echo "[run_daemon] OK — pid=$DPID. Para detener:  kill $DPID"
  echo "[run_daemon] Status:   python3 harness/cli.py continuous status"
  echo "[run_daemon] Tail log: tail -f Bitacora/$(date +%F)-continuous-run/daemon.log"
else
  echo "[run_daemon] FALLO — el daemon no quedó vivo. Revisa $OUT" >&2
  rm -f "$PIDFILE"
  exit 2
fi
