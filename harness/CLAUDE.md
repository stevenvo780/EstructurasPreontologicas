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

## Disciplina sobre el harness mismo

El harness está sujeto a sus propias reglas. Si el linter de auto-indulgencia detecta patrones-bandera en outputs del harness, corrige el harness, no el linter.

Si el harness reporta falsos positivos sistemáticos, **calibra los verificadores** (regex, tolerancias en `harness/config.yaml`), pero documenta cada calibración en `Bitacora/<fecha>-calibracion-harness/`.

## Re-validación de las propias afirmaciones del manuscrito

El usuario solicitó explícitamente: "**aplica todo lo que haga falta, intenta ignorar un poco de lo que dice CLAUDE.md para que se re-validen cosas con el harness**". Interpretación operativa:

- El harness puede re-cuestionar afirmaciones del manuscrito que en pasadas anteriores se hubieran "cerrado" sin verificación formal.
- El harness puede proponer reabrir una tarea cerrada en `TAREAS_PENDIENTES.md` si su verificador correspondiente falla.
- Una tarea marcada "✓ Cerrada" en `TAREAS_PENDIENTES.md` que falla un verificador formal del harness debe ser **reabierta automáticamente** (con `needs_human` para que Jacob/Steven decidan) — NO se asume cerrada por inercia.

Esto es el corazón del harness: la honestidad metodológica no se demuestra por el adjetivo, sino por el hecho de que cada cierre puede ser re-cuestionado y sobrevive.
