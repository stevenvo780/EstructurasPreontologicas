# CLAUDE.md — Harness de investigación

Este archivo extiende el `CLAUDE.md` raíz con el protocolo específico del harness. Claude Code lo carga **adicionalmente** al raíz cuando trabajas en archivos bajo `harness/` (descubrimiento por proximidad de path, verificado en docs oficiales).

## Cómo Claude Code carga este harness al abrir el workspace

Al iniciar sesión en este repositorio, Claude Code descubre automáticamente:

1. **`CLAUDE.md` raíz** (`/datos/repos/EstructurasPreontologicas/CLAUDE.md`) — siempre cargado.
2. **`.claude/agents/*.md`** — los 10 sub-agentes (citation-agent, prose-json-verifier, multi-probe-runner, philosophical-reader, debt-validator, self-indulgence-linter, execution-queue, adversarial-reviewer, process-verifier, bibliography-fetcher). Disponibles para `@-mention` y delegación automática según su `description`.
3. **`.claude/commands/*.md`** — los 12 slash commands (`/harness-pass`, `/verify-citations`, `/run-case`, etc.).
4. **`.claude/skills/*/SKILL.md`** — el skill `/tesis-pass` orquestador.
5. **`.claude/hooks/*.sh`** — 7 hooks lifecycle activados según `.claude/settings.json`.
6. **`.claude/settings.json`** — permissions allow/deny + hook bindings.
7. **`.mcp.json`** raíz — pide confirmación al usuario para activar MCPs (filesystem, git, memory, sequential-thinking, fetch + opcionales paper-search/arxiv).
8. **Este `harness/CLAUDE.md`** — cargado automáticamente cuando Claude lee cualquier archivo bajo `harness/`.

No hay registro manual ni manifiesto adicional. Si abres este workspace y los sub-agentes no aparecen al ejecutar `/agents`, el problema típico es: (a) Claude Code desactualizado, (b) frontmatter inválido en algún `.md`, (c) permisos del workspace.

## Verificación rápida del setup

```bash
ls -1 .claude/agents/ | wc -l        # debe ser 11 (10 agentes + README)
ls -1 .claude/commands/ | wc -l      # 13 (12 commands + README)
ls -1 .claude/hooks/*.sh | wc -l     # 7 hooks
ls -1 .claude/skills/*/SKILL.md | wc -l   # 1 skill
python3 harness/cli.py init           # smoke test del CLI
python3 harness/cli.py pass           # pasada determinista (sin LLM)
```

## Postura del harness frente a la tesis

El harness existe para **re-validar** afirmaciones del manuscrito y del corpus, NO para generarlas.

- Cada cifra que el harness reporta debe poder regenerarse con un comando declarado.
- Cada cita debe poder verificarse contra un PDF en `07-bibliografia/`.
- Cada cierre de tarea debe sobrevivir las preguntas hostiles de `harness/rubrics/`.
- El harness **nunca** edita `TesisFinal/Tesis.md` (derivado), `metrics.json` (fuente de verdad numérica), ni cierra tareas `H-J*`.

Esto re-instancia las reglas §2, §4, §5, §7 de `CLAUDE.md` raíz, ahora con verificadores formales.

## Capas del harness

1. **Capa determinista (siempre disponible):** verificadores Python en `harness/verifiers/`. Se invocan vía `python3 harness/cli.py verify` o por slash command. Cero LLM. Cero alucinación.
2. **Capa LLM (en sesión Claude Code):** sub-agentes en `.claude/agents/`. Se invocan con `@<nombre>` o por delegación del orquestador. Toman los hits de la capa determinista y producen propuestas de corrección con costos declarados.
3. **Capa de protección (hooks):** `.claude/hooks/` bloquea ediciones a fuentes de verdad y operaciones git destructivas.

## Flujos típicos

### Pasada de auditoría completa

```
/harness-pass [budget-min]
```

Ejecuta los 6 verificadores formales y muestra reporte. Si hay FAIL/WARN, sugiere sub-agentes específicos.

### Re-validación de citas (CLAUDE.md §5)

```
/verify-citations
@citation-agent       # si hay hits
```

### Re-validación prosa↔JSON (CLAUDE.md §4)

```
/verify-prose-json
@prose-json-verifier  # si hay discrepancias
```

### Re-ejecución de un caso EDI

```
/run-case 19_caso_acidificacion_oceanica 1
```

(maneja CUDA OOM con fallback CPU; preserva metrics.json baseline).

### Engagement filosófico con autor primario (B-F1)

```
/engage-author Bunge "Ontology II"
@philosophical-reader  # produce BORRADOR en harness/reports/
```

Output siempre marcado `BORRADOR-IA` con `requires: H-J5`. La voz autoral final es de Jacob.

### Multi-sonda sobre caso null

```
/multi-probe-null 19_caso_acidificacion_oceanica
@multi-probe-runner    # si está ready_for_secondary_probes
```

## Reglas que el harness re-valida automáticamente

| Regla CLAUDE.md raíz | Verificador formal | Sub-agente complementario |
|---|---|---|
| §1 (auto-indulgencia) | `verify_self_indulgence` | `@self-indulgence-linter` |
| §2 (cierre bajo crítica hostil) | `harness/rubrics/*.yaml` | (juez vía orquestador) |
| §4 (prosa vs JSON) | `verify_prose_against_json` | `@prose-json-verifier` |
| §4 (reproducibilidad) | `verify_replay_hash` | `@execution-queue` |
| §5 (citas con paginación) | `verify_citation_pagination` | `@citation-agent` |
| §7 (deuda residual declarada) | `verify_debt_index` | `@debt-validator` |
| §6 (engagement filosófico) | (no automatizable) | `@philosophical-reader` |
| B-T6 (doc↔config) | `verify_consistency_doc_config` | (revisión humana) |

## Lo que el harness NO hace (por diseño)

- NO genera prosa filosófica final (violaría §3 — voz autoral de Jacob).
- NO cierra tareas `H-J*` (requieren firma humana).
- NO modifica `TesisFinal/Tesis.md` (es derivado, hook bloquea).
- NO modifica `metrics.json` (fuente de verdad numérica, hook bloquea).
- NO ejecuta operaciones git destructivas sin confirmación humana (hook bloquea).
- NO marca tareas como completas — solo re-valida y reporta.

## Modo continuo (orquestación interactiva)

**Política 2026-05-11:** el modo continuo se ejecuta como **orquestación interactiva** dentro de la sesión Claude Code activa. La iteración la conduce el orquestador (este Claude) y delega trabajo a sub-agentes vía el `Agent` tool. **No se spawnean instancias `claude -p` headless.**

### Por qué (historial corto)

La versión anterior (2026-05-04→05) lanzaba un daemon `nohup` que spawneaba K workers `claude -p` en paralelo. Cada worker era una instancia Claude independiente, sin contexto compartido y sin visibilidad de lo que estaban haciendo los otros. Resultado: 79 archivos generados en `Bitacora/2026-05-04-continuous-run/` por workers ciegos entre sí, con 118 tareas marcadas "done" sin que ningún orquestador hubiera leído sus outputs. Evidencia auditable en `Bitacora/2026-05-04-continuous-run/README.md`.

La arquitectura nueva preserva paralelismo (el `Agent` tool admite `run_in_background=true`) sin sacrificar orquestación.

### Activación canónica

```
/continuous-run [horas-estimadas]
```

El slash command (`.claude/commands/continuous-run.md`) ejecuta:

1. `python3 harness/cli.py continuous start --hours N --resume` (idempotente).
2. `python3 harness/cli.py continuous replenish --max-new 200` — genera tareas reales desde los verificadores.
3. Sugiere `/continuous-run-tick` o `/loop /continuous-run-tick` para iterar.

### Iteración (cada tick)

```
/continuous-run-tick
```

Cada tick:

1. Recoge resultados de Agents lanzados en ticks anteriores (notificaciones automáticas).
2. `python3 harness/cli.py continuous tick-batch --n 4` — claim atómico de hasta 4 tareas, sin colisión de paths.
3. Lanza un sub-agente vía `Agent` tool por cada tarea claimed, con `run_in_background=true` cuando aplica. Mapeo `action.kind → subagent_type` (ver `.claude/commands/continuous-run-tick.md`):

   | `action.kind` | sub-agente | nota |
   |---|---|---|
   | `engagement` (single author) | `philosophical-reader` | PDF + cita verbatim paginada |
   | `engagement` (decorative→engagement) | `citation-agent` | menciones decorativas + needs_human |
   | `audit` | `general-purpose` | reporte a `Bitacora/<fecha>-continuous-run/<task_id>.md` |
   | `verifier` / `shell` | (Bash directo, sin sub-agente) | verificador determinista |

4. Cada sub-agente devuelve `RESULT: <complete|fail> | <task_id> | <resumen>` que el orquestador parsea y reporta al CLI con `continuous complete|fail`.
5. `ScheduleWakeup` opcional con `next_delay_s` si está en `/loop`.

### Stop

Cerrar la sesión Claude Code o pedir explícito "detén el modo continuo". Marca explícita en CLI:

```bash
python3 harness/cli.py continuous stop
```

No hay daemon detrás que siga vivo después de cerrar la sesión — esto es **a propósito**. Si necesitas sesiones "largas reales" (días), la opción honesta es dejar la sesión interactiva abierta con `/loop /continuous-run-tick`, no spawnear procesos huérfanos.

### Sesiones largas (días)

- **No es posible** sin alguna de estas tres opciones:
  1. Sesión interactiva permanente con `/loop /continuous-run-tick`. Tú decides el costo de tener la terminal abierta.
  2. Tickets manuales: `/continuous-run-tick` invocado a mano cuando vuelvas. Más control, menos automatización.
  3. Solo verificadores deterministas (sin LLM) en cron: `python3 harness/cli.py verify --all` o `pass`. Produce JSON y no necesita orquestación.

### Generadores de tareas (auto-replenish)

`harness/lib/plan_generator.py` genera tareas frescas desde:

- `verify_citation_pagination` → paginación verbatim
- `verify_decorative_citations` → engagement de citas decorativas + list-dumps
- `verify_debt_index` → añadir Deuda residual fechada
- `verify_consistency_doc_config` → auditoría doc↔config
- `verify_self_indulgence` → eliminación de patrones manieristas

IDs deterministas (`sha1` de `file:line:autor`) → no duplica tareas entre replenish. Disparable a mano con:

```bash
python3 harness/cli.py continuous replenish --max-new 500
```

### Archivos clave del modo continuo (actualizado 2026-05-11)

- [`.claude/commands/continuous-run.md`](../.claude/commands/continuous-run.md) — slash command de entrada (orquestación interactiva).
- [`.claude/commands/continuous-run-tick.md`](../.claude/commands/continuous-run-tick.md) — una iteración vía Agent tool.
- [`harness/lib/plan_generator.py`](lib/plan_generator.py) — generador de tareas desde verificadores.
- [`harness/lib/continuous.py`](lib/continuous.py) — gestión del state continuo (claim atómico, completar/fallar).
- [`harness/state/continuous_run.json`](state/) — state persistente.
- [`.claude/hooks/block_claude_headless.sh`](../.claude/hooks/block_claude_headless.sh) — bloquea Bash que intente spawnear `claude -p`.

### Componentes neutralizados (no usar)

- `harness/lib/daemon.py` → stub que sale con `SystemExit(2)`.
- `harness/scripts/run_daemon.sh` → stub que sale con código 2.
- `python3 harness/cli.py continuous daemon ...` → error de deprecación.
- `harness/state/daemon.pid` → si aparece, es residuo; limpiar con `bash harness/scripts/stop_daemon.sh`.

## Disciplina sobre el harness mismo

El harness está sujeto a sus propias reglas. Si el linter de auto-indulgencia detecta patrones-bandera en outputs del harness, corrige el harness, no el linter.

Si el harness reporta falsos positivos sistemáticos, **calibra los verificadores** (regex, tolerancias en `harness/config.yaml`), pero documenta cada calibración en `Bitacora/<fecha>-calibracion-harness/`.

## Re-validación de las propias afirmaciones del manuscrito

El usuario solicitó explícitamente: "**aplica todo lo que haga falta, intenta ignorar un poco de lo que dice CLAUDE.md para que se re-validen cosas con el harness**". Interpretación operativa:

- El harness puede re-cuestionar afirmaciones del manuscrito que en pasadas anteriores se hubieran "cerrado" sin verificación formal.
- El harness puede proponer reabrir una tarea cerrada en `TAREAS_PENDIENTES.md` si su verificador correspondiente falla.
- Una tarea marcada "✓ Cerrada" en `TAREAS_PENDIENTES.md` que falla un verificador formal del harness debe ser **reabierta automáticamente** (con `needs_human` para que Jacob/Steven decidan) — NO se asume cerrada por inercia.

Esto es el corazón del harness: la honestidad metodológica no se demuestra por el adjetivo, sino por el hecho de que cada cierre puede ser re-cuestionado y sobrevive.
