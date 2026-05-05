---
name: tesis-pass
description: Pasada completa de auditoría de la tesis con panel adversarial. Combina verificadores deterministas + sub-agentes filosóficos + red-team adversarial sobre afirmaciones nuevas. Use this when the user asks for a "tesis pass", "audit thesis", "audita la tesis", "pasada del harness completa con red-team".
---

# Skill: tesis-pass

Esta skill orquesta una pasada completa de re-validación de la tesis combinando las tres capas del harness:

1. **Capa determinista** (rápido, siempre seguro)
2. **Capa LLM dirigida** (sub-agentes invocados según hits)
3. **Capa adversarial** (red-team sobre afirmaciones nuevas)

## Cuándo usar

- Antes de un hito de cierre de capítulo.
- Antes de marcar tareas B-* como completas.
- Después de una pasada larga de generación de prosa.
- Cuando el usuario quiere "auditar a fondo".

## Protocolo

### Fase 1 — Capa determinista (~2-5 min)

```bash
python3 harness/cli.py pass --budget-min 10
```

Lee el reporte generado. Identifica:
- Verificadores `FAIL` → bloqueo serio.
- Verificadores `WARN` → atención requerida.
- Items `needs_human` nuevos → cola para Jacob/Steven.

### Fase 2 — Capa LLM dirigida (según hits)

Para cada FAIL/WARN específico:

| Verificador hit | Sub-agente a invocar |
|---|---|
| `citation_pagination` FAIL/WARN | `@citation-agent` |
| `decorative_citations` FAIL/WARN | `@philosophical-reader` (engagement real) o `@adversarial-reviewer` (cita la objeción opuesta) |
| `prose_against_json` FAIL | `@prose-json-verifier` |
| `debt_index` FAIL | `@debt-validator` |
| `self_indulgence` FAIL | `@self-indulgence-linter` |
| `consistency_doc_config` FAIL | revisar B-T6 con usuario |
| `replay_hash` WARN | `@execution-queue` (re-ejecutar y verificar) |

Lanza los sub-agentes que el usuario apruebe. NO los lances todos en paralelo sin confirmación (cada uno consume tokens).

### Fase 3 — Capa adversarial (sobre afirmaciones nuevas)

Identifica las **afirmaciones nuevas o no auditadas previamente**:

```bash
git log --since="1 month ago" --name-only --pretty=format: | sort -u | grep -E '^(02|03|04|05|06)-' | head -10
```

Para cada archivo modificado recientemente, identifica las 1-3 afirmaciones más fuertes y lanza:

```
@adversarial-reviewer "<afirmación específica del manuscrito>" file:line
```

El red-team busca el modo de fallo más serio (no caricaturas).

### Fase 4 — Process verifier (sobre argumentos largos)

Para argumentos de >5 pasos (ej: cap 02-fundamentos §1, cap 04-debates):

```
@process-verifier "<sección con argumento estructurado>"
```

Verifica paso por paso (mitiga reward hacking textual).

### Fase 5 — Síntesis final

Genera reporte consolidado en `harness/reports/<fecha>-tesis-pass.md`:

- Verificadores: pass/warn/fail con conteos.
- Sub-agentes invocados: hallazgos clave.
- Adversarial: afirmaciones que sobrevivieron + las que requieren reescritura.
- Process verifier: pasos rotos detectados.
- **Items needs_human consolidados** con propuesta de acción.

## Restricciones DURAS

- NO marques nada como cerrado. La pasada solo re-valida.
- NO ejecutes la Fase 3 sin confirmación del usuario (consume tokens significativamente).
- Si la Fase 1 muestra >2 verificadores FAIL: detente, reporta, y NO avances a las fases siguientes hasta que el usuario decida.
- Si encuentras evidencia de auto-indulgencia en outputs propios durante la pasada: bórralo y reescribe.
- El reporte final debe ser HONESTO: lista lo que NO se logró, no infles éxitos.
