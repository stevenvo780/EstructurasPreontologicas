# Sub-agentes Claude Code del harness

Estos sub-agentes se cargan **automáticamente** al iniciar Claude Code en este workspace (descubrimiento por ruta `.claude/agents/<name>.md`). No requieren registro manual.

## Cómo se invocan

Tres patrones soportados:

1. **Lenguaje natural** (Claude decide delegar según `description` del agente):
   ```
   audita las citas del capítulo 04
   ```
   → Claude detecta y propone usar `@citation-agent`.

2. **@-mention explícito** (garantiza ejecución):
   ```
   @citation-agent verifica las citas del archivo 04-debates/04-anticipacion-objeciones-filosoficas.md
   ```

3. **Slash command** que delega a un sub-agente (ver `.claude/commands/`):
   ```
   /verify-citations
   ```

## Inventario actual

| Sub-agente | Modelo | Cuándo usar | Disparador en description |
|---|---|---|---|
| `citation-agent` | sonnet | Auditar citas con paginación contra PDFs | "Use proactively to verify…" |
| `prose-json-verifier` | sonnet | Cifras de prosa vs `metrics.json` | "Use proactively when prose drift…" |
| `decorative-citations` | (verificador formal, no agente) | Detectar invocación de autoridad sin engagement | — |
| `multi-probe-runner` | sonnet | Reanálisis de casos null con sondas alternativas | "Use when reanalyzing null cases…" |
| `philosophical-reader` | opus | Engagement con fuente primaria (B-F1) | "Use when working on B-F1…" |
| `debt-validator` | sonnet | Auditar secciones "Deuda residual" | "Use proactively when closing…" |
| `self-indulgence-linter` | haiku | Detectar manierismo / versionología | "Use proactively after every…" |
| `execution-queue` | sonnet | Re-ejecutar `validate.py` por caso | "Use when re-running EDI…" |
| `adversarial-reviewer` | opus | Red-team contra afirmaciones | "Use proactively when closing…" |
| `process-verifier` | sonnet | Verificar argumentos paso por paso (PRM) | "Use when a section/pipeline…" |
| `bibliography-fetcher` | sonnet | Recuperar papers externos vía MCP | "Use when the user wants engagement…" |

## Convenciones del frontmatter

Todos los sub-agentes siguen estas reglas (verificado contra docs oficiales Claude Code 2026-05):

- `name`: kebab-case obligatorio.
- `description`: empieza con "Use proactively when..." / "Use when..." / "MUST BE USED..." para que Claude principal delegue automáticamente.
- `tools`: lista comma-separated en string, sin newlines.
- `model`: alias `sonnet`/`opus`/`haiku` (NO IDs completos como `claude-sonnet-4-6` — quedan ligados a versiones específicas).
- Cuerpo: rol → protocolo numerado → restricciones duras → output esperado. Idealmente 200-500 palabras.

## Restricciones de orquestación

- Sub-agentes NO pueden invocar otros sub-agentes (limitación arquitectónica de Claude Code v2.1+). La sesión principal coordina.
- Para encadenar: pide al usuario "primero `@A`, luego `@B`", o usa el skill `/tesis-pass` que orquesta secuencialmente.
- Cada sub-agente tiene contexto propio aislado — no hereda historial conversacional ni `CLAUDE.md` del padre. Por eso el cuerpo del prompt incluye reglas explícitas.
