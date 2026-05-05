# Hooks Claude Code del harness

Cada hook es un script bash que Claude Code invoca en momentos específicos del lifecycle. Configurados en `.claude/settings.json` → `hooks`.

## Inventario actual

| Script | Evento | Función |
|---|---|---|
| `session_start_load_state.sh` | `SessionStart` | Imprime resumen del state al iniciar sesión |
| `user_prompt_conflict_check.sh` | `UserPromptSubmit` | Si el prompt menciona "cerrar/completar" y hay items en `needs_human`, recuerda al asistente |
| `block_metrics_edit.sh` | `PreToolUse(Edit/Write/MultiEdit)` | Bloquea edición directa a `outputs/metrics.json` |
| `block_tesis_md_edit.sh` | `PreToolUse(Edit/Write/MultiEdit)` | Bloquea edición directa a `TesisFinal/Tesis.md` (es derivado) |
| `block_destructive_git.sh` | `PreToolUse(Bash)` | Bloquea `git reset --hard`, `push --force`, etc. |
| `protect_main_push.sh` | `PreToolUse(Bash)` | Bloquea `git push` directo a `main`/`master` — exige rama+PR o autorización explícita |
| `post_validate_check_drift.sh` | `PostToolUse(Bash)` | Tras `validate.py`, verifica drift de hashes |
| `checkpoint_state.sh` | `Stop` | Snapshot de `harness/state.json` al cerrar sesión |

## Convención de output

Cuando un hook quiere bloquear o inyectar contexto, devuelve JSON por stdout con la estructura que Claude Code interpreta:

```json
{"hookSpecificOutput": {"hookEventName": "<evento>", "additionalContext": "<mensaje>"}}
```

Para bloquear: `exit 2` con stderr explicativo.

## Verificar que están activos

```bash
cat .claude/settings.json | jq '.hooks | keys'
```

Debe listar: `SessionStart`, `UserPromptSubmit`, `PreToolUse`, `PostToolUse`, `Stop`.
