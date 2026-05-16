# CLAUDE.md — Harness de re-validación

Extiende el `CLAUDE.md` raíz con el protocolo específico del harness. Claude Code lo carga al trabajar en archivos bajo `harness/`.

## Postura

El harness existe para **re-validar** afirmaciones del manuscrito y el corpus, NO para generarlas. La capa LLM (sub-agentes, redacción) vive en Claude Code; aquí solo hay verificadores deterministas en Python.

- Cada cifra que reporta se regenera con un comando declarado.
- Cada cita se verifica contra PDF en `07-bibliografia/`.
- Cada cierre de tarea sobrevive las preguntas de `harness/rubrics/`.
- El harness **nunca** edita `TesisFinal/Tesis.md` ni `metrics.json` (hooks bloquean).

## Capas

1. **Determinista (siempre):** verificadores Python en `harness/verifiers/`. `python3 harness/cli.py verify`. Cero LLM. Cero alucinación.
2. **LLM (en sesión Claude Code):** sub-agentes en `.claude/agents/` invocados vía `Agent` tool. Toman los hits de los verificadores y producen propuestas de corrección con costos declarados.
3. **Protección (hooks):** `.claude/hooks/` bloquea edits a fuentes de verdad y git destructivo.

## Mapeo verificador ↔ sub-agente ↔ modelo

| Regla raíz | Verificador | Sub-agente | Modelo |
|---|---|---|---|
| §2 cita con paginación | `verify_citation_pagination` | `@citation-agent` | haiku |
| §2 cita decorativa→engagement | `verify_decorative_citations` | `@citation-agent` + `@philosophical-reader` | haiku / opus |
| §4 JSON vs prosa | `verify_prose_against_json` | `@prose-json-verifier` | haiku |
| §3 reproducibilidad / hashes | `verify_replay_hash` | `@execution-queue` | haiku |
| §4 deuda declarada | `verify_debt_index` | `@debt-validator` | sonnet |
| §5 auto-indulgencia | `verify_self_indulgence` | `@self-indulgence-linter` | haiku |
| §1 (cierre bajo crítica hostil) | `harness/rubrics/*.yaml` | `@adversarial-reviewer` | opus |
| (doc↔config) | `verify_consistency_doc_config` | (humano) | — |
| engagement filosófico | — | `@philosophical-reader` | opus |
| caso null → multi-sonda | — | `@multi-probe-runner` | sonnet |
| pipeline >5 pasos | — | `@process-verifier` | opus |
| paper externo | — | `@bibliography-fetcher` | sonnet |

**Criterio del modelo:** opus para razonamiento profundo (filosofía, red-team, PRM); sonnet para tareas con criterio estructurado; haiku para tareas mecánicas (regex, grep, diff JSON↔prosa, invocación de Bash).

## Flujos típicos

```text
/harness-pass [budget-min]            # 8 verificadores; sugiere sub-agente para FAIL/WARN
/verify-citations    → @citation-agent si hits
/verify-prose-json   → @prose-json-verifier si discrepancias
/verify-debt         → @debt-validator si chapters sin deuda
/run-case 19_caso_acidificacion_oceanica 1   # CUDA OOM → fallback CPU
/multi-probe-null 19_caso_acidificacion_oceanica   # alt_probes/ con sondas físicamente motivadas
/engage-author Bunge "Ontology II"    → @philosophical-reader (DRAFT-AI, requires H-J5)
/adversarial "<afirmación>"            → @adversarial-reviewer (no caricatura)
/process-verify <archivo>             → @process-verifier (paso a paso)
/lint-indulgence                       → @self-indulgence-linter
```

## Iteración continua

No hay daemon. Si quieres iteración prolongada usa el skill `/loop` nativo:

```text
/loop /tesis-pass         # auto-paced: el modelo decide el wakeup tras cada pasada
/loop 1h /harness-pass    # cada hora
```

Cierra el loop con cualquier interrupción del usuario. No hay procesos huérfanos detrás.

Política anterior (modo continuo con state y tick-batch) fue eliminada el 2026-05-16. Era una reimplementación parcial de lo que `TaskCreate` nativo + sub-agentes vía `Agent` tool ya hacen mejor. El skill `/loop /tesis-pass` cubre el caso de uso real.

## Lo que el harness NO hace

- NO genera prosa filosófica final (viola la voz autoral de Jacob).
- NO cierra tareas H-J* (firma humana).
- NO modifica `TesisFinal/Tesis.md` ni `metrics.json` (hooks bloquean).
- NO ejecuta git destructivo sin confirmación (hook bloquea).
- NO marca tareas como completas — solo re-valida y reporta.

## Disciplina sobre el harness mismo

El harness está sujeto a sus reglas. Si el linter de auto-indulgencia detecta patrones en outputs del harness, corrige el harness, no el linter.

Si el harness reporta falsos positivos sistemáticos, calibra los verificadores (regex, tolerancias en `harness/config.yaml`), y documenta cada calibración en `Bitacora/<fecha>-calibracion-harness/`.

## Re-cuestionar cierres "completados"

Una tarea marcada "✓ Cerrada" en `TAREAS_PENDIENTES.md` que falla un verificador del harness debe **reabrirse automáticamente** (con `needs_human` para que Jacob/Steven decidan). El cierre no se asume por inercia — se demuestra por verificación.
