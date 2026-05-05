---
description: Pasada completa del harness — ejecuta todos los verificadores formales (citas, prosa↔JSON, hashes, deuda, auto-indulgencia, doc↔config) y muestra reporte honesto.
argument-hint: [budget-min]
allowed-tools: Bash, Read
---

Ejecuta una pasada determinista del harness sobre el repositorio de tesis.

**Pasos:**

1. Ejecuta: `python3 harness/cli.py pass --budget-min ${1:-30}`
2. Lee el reporte generado en `harness/reports/pass-<timestamp>.md`.
3. Resume los hallazgos al usuario con HONESTIDAD ESTRICTA:
   - Verificadores que pasaron, advirtieron, fallaron.
   - Items en `needs_human`.
   - Lo que NO se logró (no inventes éxitos).
4. Para cada FAIL o WARN, sugiere el sub-agente apropiado:
   - `citation_pagination` falla → invoca `@citation-agent`.
   - `prose_against_json` falla → invoca `@prose-json-verifier`.
   - `debt_index` falla → invoca `@debt-validator`.
   - `self_indulgence` warn → invoca `@self-indulgence-linter`.
   - `consistency_doc_config` falla → revisa B-T6 manualmente con usuario.
   - `replay_hash` warn → invoca `@execution-queue` para re-ejecutar.

NO marques nada como "completado" — el harness re-valida, no cierra. Solo el humano cierra.
