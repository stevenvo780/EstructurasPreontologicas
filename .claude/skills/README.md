# Skills locales del harness

Skills se cargan bajo demanda cuando Claude detecta que su `description` aplica a la tarea actual. Definidos en `.claude/skills/<name>/SKILL.md`.

## Inventario

| Skill | Cuándo se activa |
|---|---|
| `tesis-pass` | Cuando el usuario pide "audita la tesis", "tesis pass", "pasada del harness completa con red-team". Orquesta capa determinista + sub-agentes dirigidos + adversarial. |

## Diferencia entre skill, sub-agente y slash command

| Aspecto | Skill | Sub-agente | Slash command |
|---|---|---|---|
| Contexto | Inline en conversación actual | Aislado (sub-contexto propio) | Sesión principal |
| Invocación | `/skill-name` o disparada por description | `@nombre` o lenguaje natural | `/comando` |
| Cuándo usar | Procedimiento reutilizable que enriquece la conversación | Tarea paralela que no necesita el contexto principal | Acción predefinida con args |
| Costo en tokens | Bajo (carga al invocar) | Moderado-alto (nuevo contexto) | Negligible |

Para más, ver docs oficiales: <https://code.claude.com/docs/en/skills>.
