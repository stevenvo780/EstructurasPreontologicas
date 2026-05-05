---
description: "Mira qué hace el daemon de modo continuo en este momento — status compacto, últimas N líneas del log, y workers vivos. Read-only."
allowed-tools:
  - Bash
  - Read
---

# Watch del daemon de modo continuo

Inspección rápida de un daemon `harness/scripts/run_daemon.sh` en marcha. No modifica nada, no detiene nada — solo reporta.

## Pasos a ejecutar

Ejecutar **en este orden** y reportar al usuario un resumen humano (no volcar logs crudos enteros):

```bash
# 1. ¿Vive el daemon?
PID=$(cat harness/state/daemon.pid 2>/dev/null || echo "")
if [[ -n "$PID" ]] && kill -0 "$PID" 2>/dev/null; then
  echo "DAEMON: vivo pid=$PID"
  ps -o pid,etime,pcpu,pmem,cmd -p "$PID"
else
  echo "DAEMON: NO ACTIVO (no hay pidfile o pid muerto)"
fi

# 2. Status del state
python3 harness/cli.py continuous status | head -25

# 3. Últimas 30 líneas del log estructurado
LOG="Bitacora/$(date +%F)-continuous-run/daemon.log"
echo "--- tail $LOG ---"
tail -30 "$LOG" 2>/dev/null || echo "(sin log hoy)"

# 4. Workers Claude vivos (subprocesos hijos del daemon)
if [[ -n "$PID" ]] && kill -0 "$PID" 2>/dev/null; then
  echo "--- workers vivos ---"
  pgrep -P "$PID" -a 2>/dev/null | head -20 || echo "(sin hijos)"
fi

# 5. Logs de worker más recientes
echo "--- últimos 5 logs de worker ---"
ls -lt Bitacora/$(date +%F)-continuous-run/workers/*.log 2>/dev/null | head -5
```

## Reporte al usuario

Sintetizar en ≤8 líneas:
- daemon vivo/muerto, pid, tiempo desde arranque
- pending / in_progress / done / failed (de `continuous status`)
- última actividad significativa del log (último spawn, último complete/fail)
- N workers Claude actualmente corriendo
- si `failed` >> `done`, advertir y sugerir leer un worker.log concreto

Si el daemon está muerto pero hay pidfile, sugerir `bash harness/scripts/stop_daemon.sh` para limpiar y relanzar.
