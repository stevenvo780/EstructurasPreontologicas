---
description: "Avanza UNA iteración del modo continuo del harness. Lanza hasta N sub-agentes en paralelo VÍA EL AGENT TOOL (en esta sesión, contexto compartido). No spawnea `claude -p`. Invocable suelto o desde `/loop /continuous-run-tick`."
allowed-tools:
  - Bash
  - Read
  - Edit
  - Write
  - Grep
  - Glob
  - Agent
  - ScheduleWakeup
---

# Tick del modo continuo (orquestación interactiva)

Una iteración del modo continuo. **MODO CANÓNICO** (2026-05-11): tú (este Claude) orquestas hasta `MAX_PARALLEL=4` sub-agentes en background simultáneamente **vía el `Agent` tool**. NO se spawnean instancias `claude -p` headless — eso es la arquitectura vieja del daemon, neutralizada.

Cada sub-agente que lances:
- Recibe contexto explícito en el prompt (task_id, archivo, autor, estrategia).
- Hereda los hooks de la sesión (no puede editar `Tesis.md` ni `metrics.json`).
- Devuelve su resultado a TU hilo (tú lo ves, no escribe a oscuras).
- Está enumerado en `.claude/agents/` (citation-agent, philosophical-reader, etc.).

Diseñado para `/loop /continuous-run-tick` (autoritmado) o invocación suelta.

## Flujo del tick

### 1. Recolectar resultados de agentes lanzados en ticks anteriores

En esta sesión, las notificaciones de "Agent <id> completed" llegan automáticamente entre ticks. Para cada notificación nueva:

```bash
# Si el agente reportó éxito y la edición sobrevivió hooks:
/usr/bin/python3 harness/cli.py continuous complete <task_id> --result "<resumen ≤80 chars>"

# Si el agente falló (PDF no disponible, hook bloqueó, edit no aplicable):
/usr/bin/python3 harness/cli.py continuous fail <task_id> --reason "<razón concreta>"
```

Si en este tick no hay notificaciones nuevas, saltar este paso.

### 2. Claim atómico de hasta MAX_PARALLEL tareas

```bash
/usr/bin/python3 harness/cli.py continuous tick-batch --n 4
```

Output JSON:
- `stop: true` → escribir reporte final a `Bitacora/<fecha>-continuous-run/REPORTE_FINAL.md`. NO programar wakeup. Fin.
- `stop: false, claimed: []` → todas las tareas restantes ya están en vuelo o colisionan. Programar wakeup corto (300s) y esperar.
- `claimed: [task1, task2, ...]` → lanzar un Agent en background por cada una.

El `tick-batch` ya garantiza:
- No claim duplicado (atómico, marca `in_progress`).
- No colisión de paths (dos tareas no claimean si comparten algún `touches`).
- Respeta budget.

### 3. Lanzar Agents en paralelo (background)

**En UN SOLO mensaje, lanzar todos los agents claimed con `run_in_background=true`**.

Mapeo de `action.kind` → `subagent_type`:

| action.kind | subagent_type | descripción |
|---|---|---|
| `engagement` (single author) | `philosophical-reader` | lee PDF, extrae cita textual paginada, edita capítulo |
| `engagement` (decorative→engagement) | `citation-agent` | audita menciones, marca needs_human o agrega pp. |
| `audit` | `general-purpose` | produce reporte en `Bitacora/<fecha>-continuous-run/<task_id>.md` |
| `verifier` | (no subagent — Bash directo) | ejecuta verificador formal |
| `shell` | (no subagent — Bash directo) | ejecuta comando declarado |

Prompt para cada Agent: incluir literal `task_id`, `target_file`, `target_line`, `author`, `year`, `strategy`, restricción dura ("NO editar Tesis.md ni metrics.json — hooks bloquearán"), y firma de retorno: `RESULT: <complete|fail> | <task_id> | <≤80 chars resumen>`.

### 3.5. Auto-indulgencia checkpoint (cada 10 ticks)

Si el JSON de `tick-batch` trae `lint_due: true`, ejecutar **antes** del wakeup:

```bash
/usr/bin/python3 harness/verifiers/verify_self_indulgence.py
```

Si reporta hits nuevos vs el último reporte: registrar en `Bitacora/<fecha>-continuous-run/lint-tick<N>.md` con el patrón detectado y el archivo. NO corregir desde el loop continuo (eso es trabajo de `@self-indulgence-linter` con engagement humano).

### 4. Programar siguiente wakeup

`ScheduleWakeup` con `next_delay_s` del JSON de tick-batch (típicamente 120-300s). Prompt literal `/continuous-run-tick`.

Si `next_delay_s == 0`: NO programar.

## Restricciones duras (no negociables)

- NO `Tesis.md`, NO `metrics.json`, NO H-J*, NO git destructivo. Los hooks bloquearán y el agent debe reportar `fail`.
- Cada cita inyectada DEBE ser verbatim contra PDF. Si el PDF no existe, el agent reformula como mención secundaria declarada (CLAUDE.md §5) o reporta `fail`.
- Una tarea `failed` NO se reintenta automáticamente.
- Anti-colisión la garantiza `tick-batch` (vía `touches`).

## Comandos auxiliares

```bash
# Status sin avanzar
/usr/bin/python3 harness/cli.py continuous status

# Liberar manualmente una tarea atascada
/usr/bin/python3 harness/cli.py continuous fail <task_id> --reason "agent perdido"

# Detener
/usr/bin/python3 harness/cli.py continuous stop
```
