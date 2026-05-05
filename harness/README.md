# Harness de investigación científico-filosófica

Infraestructura de **re-validación** y auditoría para esta tesis. Diseñado para **Claude Code** (sub-agentes nativos, slash commands, hooks de protección), no para invocar la API directamente.

**Propuesta firmada:** [`Bitacora/2026-05-04-harness-investigacion/PROPUESTA_HARNESS.md`](../Bitacora/2026-05-04-harness-investigacion/PROPUESTA_HARNESS.md)
**Protocolo de uso:** [`harness/CLAUDE.md`](CLAUDE.md)

---

## Idea central

El harness tiene tres capas:

1. **Capa determinista** — `harness/verifiers/`. Python puro. Cero LLM. Cero alucinación. Detecta:
   - Citas sin paginación o sin match en PDF.
   - Cifras de prosa que divergen de `metrics.json`.
   - Capítulos sin sección "Deuda residual" fechada.
   - Patrones de auto-indulgencia (versionología, manierismo, plantillas spam).
   - Disonancias entre `Evaluacion_Modelos_Dominio.md` y `case_config.json`.
   - Drift de hashes de outputs.

2. **Capa LLM (Claude Code)** — `.claude/agents/`. Sub-agentes que toman los hits de la capa determinista y producen propuestas de corrección. NUNCA cierran tareas; solo proponen con costos declarados.

3. **Capa de protección** — `.claude/hooks/` + `.claude/settings.json`. Bloquea ediciones a `metrics.json` y `TesisFinal/Tesis.md`, y operaciones git destructivas.

---

## Estructura

```
.claude/
├── settings.json             ← permissions + hooks (Claude Code)
├── settings.local.json       ← (existente, no tocado)
├── agents/                   ← sub-agentes invocables con @<nombre>
│   ├── citation-agent.md
│   ├── prose-json-verifier.md
│   ├── multi-probe-runner.md
│   ├── philosophical-reader.md
│   ├── debt-validator.md
│   ├── self-indulgence-linter.md
│   └── execution-queue.md
├── commands/                 ← slash commands /<nombre>
│   ├── harness-pass.md
│   ├── harness-status.md
│   ├── verify-citations.md
│   ├── verify-prose-json.md
│   ├── verify-debt.md
│   ├── lint-indulgence.md
│   ├── run-case.md
│   ├── multi-probe-null.md
│   └── engage-author.md
└── hooks/                    ← gates de protección
    ├── block_metrics_edit.sh
    ├── block_tesis_md_edit.sh
    ├── block_destructive_git.sh
    └── checkpoint_state.sh

harness/
├── README.md                 ← este archivo
├── CLAUDE.md                 ← protocolo de uso (extiende CLAUDE.md raíz)
├── cli.py                    ← punto de entrada Python
├── orchestrator.py           ← pipeline de verificadores
├── config.yaml               ← parámetros operativos
├── state.json                ← estado persistente
├── lib/                      ← biblioteca interna
│   ├── state.py
│   ├── memory.py
│   ├── budget.py
│   ├── pdftext.py
│   ├── tesis_paths.py
│   ├── execution_queue.py
│   └── multi_probe.py
├── verifiers/                ← verificadores formales
│   ├── verify_citation_pagination.py
│   ├── verify_prose_against_json.py
│   ├── verify_replay_hash.py
│   ├── verify_debt_index.py
│   ├── verify_self_indulgence.py
│   └── verify_consistency_doc_config.py
├── rubrics/                  ← rubrics hostiles para cierres
│   ├── philosophical_close.yaml
│   ├── technical_close.yaml
│   ├── bibliographic_close.yaml
│   └── debt_declaration.yaml
└── reports/                  ← outputs de cada pasada
```

---

## Uso

### Desde Claude Code (recomendado)

Slash commands:
- `/harness-pass [budget-min]` — pasada completa de verificadores
- `/harness-status` — estado del harness
- `/verify-citations` — solo citas
- `/verify-prose-json` — solo prosa↔JSON
- `/verify-debt` — solo deuda residual
- `/lint-indulgence` — solo auto-indulgencia
- `/run-case <case_id> [max-jobs]` — re-ejecutar caso EDI
- `/multi-probe-null <case_id>` — multi-sonda sobre caso null
- `/engage-author <apellido> [obra]` — engagement filosófico

Sub-agentes invocables con `@<nombre>` desde cualquier conversación:
- `@citation-agent`
- `@prose-json-verifier`
- `@multi-probe-runner`
- `@philosophical-reader`
- `@debt-validator`
- `@self-indulgence-linter`
- `@execution-queue`

### Desde shell (sin Claude Code)

```bash
python3 harness/cli.py init                    # primera vez
python3 harness/cli.py status
python3 harness/cli.py verify --all
python3 harness/cli.py verify --citations
python3 harness/cli.py pass --budget-min 30
python3 harness/cli.py queue --list-cases
python3 harness/cli.py queue --cases 19_caso_acidificacion_oceanica --max-jobs 1 --dry
python3 harness/cli.py multi-probe --cases 19_caso_acidificacion_oceanica
```

---

## Dependencias

**Obligatorias:**
- Python ≥3.10
- `pyyaml` (`pip install pyyaml`)

**Opcionales (recomendadas):**
- `pdftotext` (poppler-utils): `sudo apt install poppler-utils`. Sin esto, el verificador de citas opera en modo degradado (solo verifica forma, no contenido del PDF).

**No requeridas:**
- Anthropic SDK Python: el harness está diseñado para Claude Code, no para llamar a la API directamente. Los sub-agentes corren dentro de la sesión de Claude Code.

---

## Reglas duras (re-validan CLAUDE.md raíz)

| Regla CLAUDE.md | Verificador formal | Sub-agente complementario |
|---|---|---|
| §1 — auto-indulgencia | `verify_self_indulgence` | `@self-indulgence-linter` |
| §4 — prosa vs JSON | `verify_prose_against_json` | `@prose-json-verifier` |
| §4 — reproducibilidad | `verify_replay_hash` | `@execution-queue` |
| §5 — citas con paginación | `verify_citation_pagination` | `@citation-agent` |
| §7 — deuda declarada | `verify_debt_index` | `@debt-validator` |
| B-T6 — doc↔config | `verify_consistency_doc_config` | (revisión humana) |

---

## Lo que el harness NO hace

- NO genera prosa filosófica final (voz autoral de Jacob, §3).
- NO cierra tareas `H-J*`.
- NO edita `TesisFinal/Tesis.md` (derivado, hook bloquea).
- NO edita `metrics.json` (fuente de verdad numérica, hook bloquea).
- NO ejecuta git destructivo sin confirmación (hook bloquea).
- NO marca tareas como completas — solo reporta.

---

## Estado actual

Ver `harness/state.json` (auto-generado, legible). Reportes en `harness/reports/`.
