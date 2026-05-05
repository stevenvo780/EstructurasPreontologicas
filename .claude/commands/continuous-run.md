---
description: "Modo continuo del harness — daemon paralelo de N horas reales que sobrevive al cierre de la sesión Claude Code. Uso: `/continuous-run 80` o `/continuous-run 150 6`."
allowed-tools:
  - Bash
  - Read
  - Edit
  - Write
  - Grep
  - Glob
---

# Modo continuo del harness (daemon paralelo)

Sesión auto-orquestada de N horas reales. **Vive como proceso `nohup` independiente de la sesión Claude Code interactiva** — si cierras la terminal o se cae la sesión, el daemon sigue trabajando hasta que se le acaben las horas o lo detengas explícitamente. Lanza hasta K workers en paralelo (`subprocess.Popen` + `claude -p` headless), uno por tarea, con presupuesto cap por worker (`--max-budget-usd 0.50 --max-turns 30`). Cuando la cola de tareas baja de un umbral, **regenera tareas automáticamente** desde la salida de los verificadores (`citation_pagination`, `decorative_citations`).

## Cómo activarlo (lo que debes ejecutar como Bash)

Argumentos del slash command: `$ARGUMENTS` ≈ `<horas> [parallel]`. Default: 80h, 4 workers.

```bash
# Lanzar daemon (sobrevive cierre de terminal)
bash harness/scripts/run_daemon.sh $ARGUMENTS
```

El launcher hace tres cosas:
1. Si no existe sesión continua, llama a `continuous start --hours N`.
2. Llama a `continuous replenish` para generar tareas reales desde los verificadores (~20-200 tareas según hits actuales).
3. Lanza `continuous daemon --hours N --parallel K` con `nohup` y guarda el PID en `harness/state/daemon.pid`.

Tras lanzarlo, reporta al usuario:
- el PID del daemon,
- el archivo de log (`Bitacora/<fecha>-continuous-run/daemon.log`),
- el comando para detenerlo (`bash harness/scripts/stop_daemon.sh`),
- el comando para ver progreso (`python3 harness/cli.py continuous status`).

## Comandos auxiliares

```bash
# Status sin avanzar (puedes correrlo aunque el daemon esté en marcha)
python3 harness/cli.py continuous status

# Tail del log
tail -f Bitacora/$(date +%F)-continuous-run/daemon.log

# Logs por worker individual
ls -lt Bitacora/$(date +%F)-continuous-run/workers/

# Detener (drena workers en vuelo, espera 120s y SIGKILL si persiste)
bash harness/scripts/stop_daemon.sh

# Forzar regeneración manual del plan desde verificadores
python3 harness/cli.py continuous replenish --max-new 500
```

## Qué hace cada worker

Cada tarea claimed se despacha a un subprocess:

| `action.kind` | proceso | flags |
|---|---|---|
| `engagement` | `claude -p` headless | `--permission-mode bypassPermissions --max-turns 120 --max-budget-usd 5.00 --model opus` |
| `audit` | `claude -p` headless | idem; output a `Bitacora/.../<task_id>.md` |
| `shell` | `bash -c <cmd>` directo | sin Claude |
| `verifier` | `python3 harness/verifiers/<...>.py` | sin Claude |

El daemon parsea la última línea `RESULT: <complete\|fail> | <task_id> | <resumen>` del log del worker para marcar el resultado. Si el worker termina con `rc != 0`, se marca `failed`.

## Restricciones duras (no negociables)

- **Hooks PreToolUse + deny rules son la barrera real:** los workers corren con `--permission-mode bypassPermissions` (única forma de evitar que se cuelguen pidiendo confirmación en headless con stdin cerrado). La protección NO desaparece — sigue aplicada por:
  - `deny` rules en `.claude/settings.json` (`Edit/Write` a `TesisFinal/Tesis.md` y `**/outputs/metrics.json`).
  - hooks `PreToolUse` que devuelven `permissionDecision: deny` (`block_metrics_edit`, `block_tesis_md_edit`, `block_destructive_git`, `protect_main_push`).
  - Estos siguen efectivos bajo `bypassPermissions`. `bypassPermissions` sólo elimina los prompts interactivos, NO las barreras de seguridad declaradas.
- **Timeout duro por worker**: `HARNESS_WORKER_TIMEOUT_S` (default 1800s = 30 min). Si un worker se cuelga por cualquier razón, el daemon lo mata (SIGTERM→SIGKILL) y reclama la siguiente tarea. **El daemon NUNCA se para por un worker individual.**
- **No se cierran tareas H-J\***: si una tarea genera un cambio filosófico sustantivo, debe marcarse `BORRADOR-IA` con `requires: H-J*` y dejar la firma a Jacob.
- **Cada cita inyectada DEBE ser verbatim** contra PDF. Si no hay PDF, reformulación secundaria declarada (CLAUDE.md §5).
- **Coste cap por worker**: `--max-budget-usd 5.00` por subprocess (override con env `HARNESS_MAX_BUDGET_USD`).

## Variables de entorno

| Var | Default | Efecto |
|---|---|---|
| `HARNESS_MAX_TURNS` | 120 | Máximo de turnos por worker Claude |
| `HARNESS_MAX_BUDGET_USD` | 5.00 | Cap de coste por worker |
| `HARNESS_WORKER_MODEL` | opus | Modelo del worker (opus/sonnet/haiku) |
| `HARNESS_WORKER_TIMEOUT_S` | 1800 | Timeout duro por worker (SIGTERM→SIGKILL) |
| `CLAUDE_BIN` | claude | Binario de Claude Code |

## Diferencia con el modo `/loop /continuous-run-tick` anterior

El modo `/loop` antiguo dependía de que la sesión Claude Code interactiva siguiera viva entre wakeups, lo cual no se cumplía en sesiones de 80+ horas. El daemon nuevo:

- vive en su propio proceso (no requiere sesión interactiva),
- ejecuta paralelismo real con `subprocess.Popen` (no espera al modelo principal),
- regenera tareas desde verificadores automáticamente (no se queda sin trabajo a los 20 minutos),
- tiene presupuesto y límites de turnos por worker (no hay runaway de costes),
- escribe logs por worker auditables a posteriori.
