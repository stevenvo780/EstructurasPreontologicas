# Sub-agentes Claude Code del harness

Se cargan **automáticamente** al iniciar Claude Code (descubrimiento por ruta `.claude/agents/<name>.md`). No requieren registro manual.

## Cómo se invocan

Tres patrones soportados:

1. **Delegación automática** (el main Claude decide según `description`):
   ```
   audita las citas del capítulo 04
   ```
   → Claude detecta y delega a `@citation-agent`.

2. **@-mention explícito** (garantiza ejecución):
   ```
   @citation-agent verifica las citas del archivo 04-debates/04-anticipacion-objeciones-filosoficas.md
   ```

3. **Slash command** (ver `.claude/commands/`):
   ```
   /verify-citations
   ```

## Inventario actual

| Sub-agente | Modelo | Cuándo usar |
|---|---|---|
| `philosophical-reader` | **opus** | Engagement con fuente primaria (Bunge, Dennett, Simondon, …) |
| `adversarial-reviewer` | **opus** | Red-team contra afirmaciones del manuscrito |
| `process-verifier` | **opus** | Verificar argumentos paso por paso (PRM) |
| `multi-probe-runner` | sonnet | Reanálisis de casos null con sondas alternativas |
| `debt-validator` | sonnet | Auditar secciones "Deuda residual" |
| `bibliography-fetcher` | sonnet | Recuperar papers externos vía MCP |
| `citation-agent` | haiku | Verificar citas con paginación contra PDFs |
| `prose-json-verifier` | haiku | Cifras de prosa vs `metrics.json` |
| `execution-queue` | haiku | Re-ejecutar `validate.py` por caso (CUDA OOM → CPU) |
| `self-indulgence-linter` | haiku | Detectar manierismo / versionología |

## Criterio del modelo

- **opus** — razonamiento profundo: filosofía, red-team, PRM step-by-step.
- **sonnet** — criterio estructurado: audit, búsqueda con criterio, multi-sonda.
- **haiku** — tareas mecánicas: regex, grep, diff JSON↔prosa, invocación de Bash.

## Convenciones del frontmatter

```yaml
---
name: kebab-case
description: Use proactively when… / Use when… / MUST BE USED whenever…
tools:
  - Read
  - Bash
  - …
model: opus | sonnet | haiku
---
```

- `description` debe empezar con disparador claro para que el main Claude delegue sin necesidad de @-mention.
- Usar alias del modelo (`opus`), NO IDs completos (ligados a versiones).
- Cuerpo: rol → protocolo numerado → restricciones duras → output esperado.

## Restricciones de orquestación

- Sub-agentes NO pueden invocar otros sub-agentes. La sesión principal coordina.
- Cada sub-agente tiene contexto propio aislado — no hereda historial ni `CLAUDE.md` del padre. Las reglas duras se inyectan en el cuerpo del agente.
- Para encadenar: el main Claude invoca `@A`, lee el resultado, luego invoca `@B`. O usa el skill `/tesis-pass` que orquesta secuencialmente.
