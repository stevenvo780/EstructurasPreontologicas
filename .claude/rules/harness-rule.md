---
paths:
  - "harness/**"
  - ".claude/**"
---

# Reglas del harness y configuración Claude Code

Estás modificando el harness o la configuración de Claude Code.

## Disciplina sobre el harness mismo

El harness está sujeto a sus propias reglas:

- Si el linter de auto-indulgencia detecta patrones en outputs del harness → **corrige el harness, no el linter**.
- Si reporta falsos positivos sistemáticos → calibra los verificadores (regex, tolerancias en `harness/config.yaml`) y documenta en `Bitacora/<fecha>-calibracion-harness/`.
- Nunca silencies un verificador para hacer pasar una pasada. Si un caso es legítimamente excepción, la lista blanca va con justificación en `config.yaml`.

## Capa LLM vs capa determinista

| Pertenece a determinista (Python, sin LLM) | Pertenece a LLM (sub-agentes) |
|---|---|
| `harness/verifiers/` | `.claude/agents/` |
| `harness/cli.py verify` | `Agent` tool |
| Regex, hashes, JSON diff | Engagement con autor, prosa, redacción |
| Reporta hits | Propone correcciones con costos |

Si tienes la tentación de meter un LLM en `harness/`, **no lo hagas**. El harness produce JSON; los sub-agentes lo consumen.

## Frontmatter de sub-agentes

Cada `.claude/agents/*.md` requiere:

```yaml
---
name: <slug-kebab>
description: <cuándo Claude debe delegar a este agente, con triggers>
tools: [lista corta de tools]
model: opus | sonnet | haiku
---
```

**Criterio del modelo:**

- `opus` — razonamiento profundo: filosofía, red-team, PRM step-by-step.
- `sonnet` — criterio estructurado: audit, multi-sonda, fetch externo.
- `haiku` — tareas mecánicas: regex, grep, diff, invocación de Bash.

## Hooks activos (no añadir sin necesidad)

`SessionStart` debe ser **rápido**. No bloquear arranque con verificadores pesados.

`PreToolUse` bloqueante (matcher: `Edit|Write|MultiEdit`):
- `block_metrics_edit.sh` — protege `**/outputs/metrics.json`
- `block_tesis_md_edit.sh` — protege `TesisFinal/Tesis.md`

`PreToolUse` bloqueante (matcher: `Bash`):
- `block_destructive_git.sh` — git reset --hard, force push, branch -D
- `protect_main_push.sh` — git push origin main sin confirmación

`PostToolUse` (matcher: `Bash`):
- `post_validate_check_drift.sh` — tras `validate.py`, advierte si hashes cambiaron

`Stop`:
- `checkpoint_state.sh` — snapshot del state al cerrar turno

`UserPromptSubmit`:
- `user_prompt_conflict_check.sh` — si el usuario pide cerrar tarea y hay items `needs_human`, advierte

## Antipatrones eliminados (2026-05-16)

No re-introducir:

- **Daemon `claude -p` headless** (`run_daemon.sh`): producía workers ciegos entre sí.
- **`harness/lib/memory.py`**: duplicaba auto memory nativo (`~/.claude/projects/<repo>/memory/`).
- **`harness/lib/continuous.py` + `plan_generator.py`**: re-implementaban TaskCreate/TaskUpdate nativos sin ventaja real. El skill nativo `/loop` cubre el caso.
- **Hooks `block_claude_headless.sh` + `continuous_dispatch_subagent_result.sh`**: solo existían para parchear los antipatrones anteriores.

Si vuelve a aparecer la tentación de spawnear `claude -p` en background o reimplementar el modo continuo: **NO**. Usa `/loop /tesis-pass` (nativo) o `Agent` tool con `run_in_background=true`.
