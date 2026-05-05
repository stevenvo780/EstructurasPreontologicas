---
description: Re-analiza un caso null con sondas alternativas físicamente motivadas.
argument-hint: <case_id>
allowed-tools:
  - Bash
  - Read
---

Inspecciona estado del caso null y, si está listo, lanza `@multi-probe-runner`.

1. Verifica primary_arrays:
   ```bash
   ls 09-simulaciones-edi/$1/outputs/primary_arrays.json 2>/dev/null && echo READY || echo BLOCKED_BY_B-T1
   ```

2. Si `READY`:
   - Lee config: `cat 09-simulaciones-edi/$1/case_config.json | jq .`
   - Pregunta al usuario si quiere lanzar `@multi-probe-runner` (puede tardar horas con varias sondas).

3. Si `BLOCKED_BY_B-T1`:
   - El caso necesita `primary_arrays.json` primero (B-T1).
   - Sugiere: re-ejecutar el caso con `ARRAY_DUMP=1` env var, o invocar `@execution-queue` con esa instrucción.
