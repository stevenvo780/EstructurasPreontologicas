---
description: "Inicia el modo continuo INTERACTIVO del harness — tú (este Claude) orquestas sub-agentes vía el Agent tool dentro de esta sesión. NO spawnea `claude -p`. Uso: `/continuous-run [horas]` (default: hasta que el usuario detenga)."
allowed-tools:
  - Bash
  - Read
  - Edit
  - Write
  - Grep
  - Glob
  - Agent
  - TaskCreate
  - TaskUpdate
  - TaskList
  - ScheduleWakeup
---

# Modo continuo del harness (orquestación interactiva)

**Política (2026-05-11):** el modo continuo se ejecuta **dentro de esta sesión Claude Code**, NO como daemon `nohup` que spawnea `claude -p` headless.

Razón: los workers `claude -p` independientes pierden contexto, no se ven entre sí y producen archivos descoordinados en el repo (ver `Bitacora/2026-05-04-continuous-run/README.md` para evidencia del problema con el daemon viejo). La orquestación correcta es:

- **Tú (este Claude)** mantienes el plan en memoria y la `TaskList`.
- **Sub-agentes** se invocan vía el `Agent` tool (`.claude/agents/*.md`) — heredan tu contexto y devuelven su resultado a tu hilo, no escriben a oscuras.
- **Verificadores deterministas** se invocan vía `Bash` directo (sin LLM).

## Flujo de activación

Argumento opcional del slash: `$ARGUMENTS` = horas estimadas (sólo informativo; no es un deadline duro).

### 1. Cargar estado y arrancar/reanudar sesión continua

```bash
# Si no existe state, iniciar (horas es target informativo)
python3 harness/cli.py continuous status 2>/dev/null || \
  python3 harness/cli.py continuous start --hours ${ARGUMENTS:-24} --resume
```

### 2. Reabastecer cola desde verificadores

```bash
python3 harness/cli.py continuous replenish --max-new 200
```

Esto regenera tareas frescas a partir de los hits de los verificadores (`citation_pagination`, `decorative_citations`, `debt_index`, `self_indulgence`, `consistency_doc_config`).

### 3. Iterar

Para cada iteración invocar `/continuous-run-tick`. Si el usuario quiere autoritmado, sugerir `/loop /continuous-run-tick`.

### 4. Detener

El usuario detiene escribiendo "detén el modo continuo" o cerrando la sesión. NO hay daemon detrás que siga corriendo: cerrar la sesión cierra el modo continuo. Para marcarlo explícito:

```bash
python3 harness/cli.py continuous stop
```

## Lo que el modo continuo NO hace

- **NO** lanza `bash harness/scripts/run_daemon.sh` — está neutralizado.
- **NO** invoca `python3 harness/cli.py continuous daemon ...` — devuelve error de deprecación.
- **NO** spawnea `claude -p` directa ni indirectamente (hay un hook `block_claude_headless` que bloquea cualquier `Bash` que contenga `claude -p` o `claude --print`).
- **NO** edita `TesisFinal/Tesis.md` ni `**/outputs/metrics.json` (hooks bloquean).
- **NO** cierra tareas `H-J*` (firma humana).

## Antipatrones detectados (no repetir)

El daemon viejo (2026-05-04→05) lanzaba 4-12 workers `claude -p` en paralelo sin que ninguno viera lo que los otros estaban editando. Resultado: 79 archivos generados en `Bitacora/2026-05-04-continuous-run/` por workers ciegos entre sí. Si en una pasada futura alguien sugiere "relanzar el daemon" o "spawnear claude -p en background", responde **no**, y apunta a este archivo.

## Diferencia con sesiones largas reales

Si el usuario pide "déjalo corriendo 80 horas y vete", la respuesta honesta es: **no es posible sin sacrificar orquestación**. Las opciones son:

1. **Sesión interactiva larga**: el usuario deja la terminal abierta, `/loop /continuous-run-tick` autoritma iteraciones, y tú mantienes el contexto. Si la sesión se cae, el state en `harness/state/continuous_run.json` permite reanudar manualmente.
2. **Tickets discretos**: el usuario corre `/continuous-run-tick` N veces a mano. Más control, menos automatización.
3. **Solo verificadores deterministas**: `python3 harness/cli.py pass` o `verify --all` corren sin LLM en segundos y producen reporte JSON — eso sí puede ir en cron sin daemon Claude.
