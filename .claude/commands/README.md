# Slash commands del harness

Comandos `/<name>` invocables desde el chat de Claude Code en este workspace.

## Inventario

| Comando | Qué hace | Sub-agente delegado |
|---|---|---|
| `/harness-pass [budget-min]` | Pasada determinista completa de los 7 verificadores | (ninguno; capa formal) |
| `/harness-status` | Muestra `harness/state.json` resumido | (ninguno) |
| `/verify-citations` | Solo verificador formal de citas | `@citation-agent` si hay hits |
| `/verify-prose-json` | Solo verificador formal prosa↔JSON | `@prose-json-verifier` si hay hits |
| `/verify-debt` | Solo verificador formal de deuda | `@debt-validator` si hay hits |
| `/lint-indulgence` | Solo linter de auto-indulgencia | `@self-indulgence-linter` si hay hits |
| `/run-case <id> [perfil]` | Re-ejecutar caso EDI | `@execution-queue` |
| `/multi-probe-null <id>` | Multi-sonda sobre caso null | `@multi-probe-runner` |
| `/engage-author <apellido>` | Engagement con autor primario | `@philosophical-reader` |
| `/adversarial <file:line> "<claim>"` | Red-team contra una afirmación | `@adversarial-reviewer` |
| `/process-verify <archivo>` | Verificar argumento paso por paso | `@process-verifier` |
| `/fetch-biblio <autor> [tema]` | Recuperar paper externo vía MCP | `@bibliography-fetcher` |
| `/continuous-run [horas]` | Inicia modo continuo (orquestación interactiva) | sub-agentes vía `Agent` tool |
| `/continuous-run-tick` | Una iteración del modo continuo | `Agent` tool con `run_in_background=true` |
| `/daemon-watch` | Inspección read-only del state continuo y residuos | (ninguno) |

## Convención

Cada slash command es un archivo markdown en `.claude/commands/<name>.md` con frontmatter:

```yaml
---
description: <qué hace, en 1 línea>
argument-hint: <args esperados>
allowed-tools: <herramientas permitidas>
---
```

El cuerpo describe los pasos que Claude principal ejecuta al invocar el comando — usualmente: corre verificador determinista → si hay hits → delega a `@sub-agente`.
