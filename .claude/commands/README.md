# Slash commands del harness

Comandos `/<name>` invocables desde el chat de Claude Code en este workspace. El **main Claude** orquesta; cada comando suele delegar a un sub-agente especializado (`.claude/agents/`) según el dominio.

## Inventario

| Comando | Qué hace | Sub-agente delegado | Modelo |
|---|---|---|---|
| `/harness-pass [budget-min]` | Pasada determinista completa de los 8 verificadores | (capa formal, sin LLM) | — |
| `/harness-status` | Muestra `harness/state.json` resumido | (ninguno) | — |
| `/verify-citations` | Verificador formal de citas con paginación | `@citation-agent` si hay hits | haiku |
| `/verify-prose-json` | Verificador formal prosa↔JSON | `@prose-json-verifier` si hay hits | haiku |
| `/verify-debt` | Verificador formal de deuda residual | `@debt-validator` si hay hits | sonnet |
| `/lint-indulgence` | Linter de auto-indulgencia | `@self-indulgence-linter` si hay hits | haiku |
| `/run-case <id> [perfil]` | Re-ejecutar caso EDI (CUDA OOM → fallback CPU) | `@execution-queue` | haiku |
| `/multi-probe-null <id>` | Multi-sonda sobre caso null | `@multi-probe-runner` | sonnet |
| `/engage-author <apellido>` | Engagement con autor primario | `@philosophical-reader` | opus |
| `/adversarial <file:line> "<claim>"` | Red-team contra una afirmación | `@adversarial-reviewer` | opus |
| `/process-verify <archivo>` | Verificar argumento paso por paso (PRM) | `@process-verifier` | opus |
| `/fetch-biblio <autor> [tema]` | Recuperar paper externo vía MCP | `@bibliography-fetcher` | sonnet |

## Iteración continua

No hay slash command propio para "modo continuo". Usa el skill nativo `/loop`:

```text
/loop /tesis-pass         # auto-paced
/loop 1h /harness-pass    # cada hora
```

(La iteración auto-orquestada con state persistente fue eliminada el 2026-05-16; el nativo es suficiente y más simple.)

## Convención

Cada slash command es un archivo markdown en `.claude/commands/<name>.md` con frontmatter:

```yaml
---
description: <qué hace, en 1 línea — Claude usa esto para sugerir el comando>
argument-hint: <args esperados>
allowed-tools: <lista corta>
---
```

El cuerpo describe los pasos del orquestador: usualmente "corre verificador determinista → si hay hits → delega a `@sub-agente`".
