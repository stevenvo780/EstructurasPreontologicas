---
description: "Inspección rápida del estado del modo continuo del harness (sesión interactiva). Reporta state, último log, y detecta procesos `claude -p` huérfanos del daemon viejo. Read-only."
allowed-tools:
  - Bash
  - Read
---

# Watch del modo continuo

Inspección rápida y read-only del estado del modo continuo. **Importante (2026-05-11):** el daemon paralelo viejo (`claude -p` headless) está neutralizado. El modo continuo correcto vive **dentro de esta sesión Claude Code** — orquestación vía `Agent` tool. Este comando reporta tanto el state legítimo como cualquier residuo del daemon viejo (pidfile huérfano, procesos `claude -p` rezagados).

## Pasos a ejecutar

```bash
# 1. ¿Hay residuos del daemon viejo?
PIDFILE="harness/state/daemon.pid"
if [[ -f "$PIDFILE" ]]; then
  OLD_PID=$(cat "$PIDFILE")
  if kill -0 "$OLD_PID" 2>/dev/null; then
    echo "AVISO: PID $OLD_PID vive según pidfile. El daemon está neutralizado;"
    echo "       investiga qué es ese proceso y, si es realmente el daemon viejo,"
    echo "       detenlo con: bash harness/scripts/stop_daemon.sh"
    ps -o pid,etime,pcpu,pmem,cmd -p "$OLD_PID"
  else
    echo "pidfile huérfano (pid=$OLD_PID muerto). Limpia con: rm $PIDFILE"
  fi
fi

# 2. Procesos `claude -p` huérfanos (no deberían existir bajo la nueva política)
ORPH=$(pgrep -fa "claude -p" 2>/dev/null | grep -v "$$" || true)
if [[ -n "$ORPH" ]]; then
  echo "AVISO: procesos `claude -p` activos (la política los prohíbe):"
  echo "$ORPH"
fi

# 3. State de la sesión continua
python3 harness/cli.py continuous status 2>/dev/null | head -25 || \
  echo "(no hay sesión continua activa)"

# 4. Últimas 30 líneas del log si existe
LOG="Bitacora/$(date +%F)-continuous-run/daemon.log"
if [[ -f "$LOG" ]]; then
  echo "--- tail $LOG ---"
  tail -30 "$LOG"
fi
```

## Reporte al usuario

Sintetizar en ≤8 líneas:
- residuos del daemon viejo (pidfile vivo / huérfano / ninguno)
- procesos `claude -p` rezagados (debería ser cero)
- pending / in_progress / done / failed del state continuo
- última actividad del log estructurado (si existe)
- si hay residuos, sugerir limpiar antes de continuar
