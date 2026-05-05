---
description: Re-analiza un caso null con sondas alternativas físicamente motivadas.
argument-hint: <case_id>
allowed-tools: Bash, Read
---

Inspecciona estado del caso null y, si está listo, lanza `@multi-probe-runner`.

1. `python3 harness/cli.py multi-probe --cases $1`
2. Si `ready_for_secondary_probes: true`:
   - Pregunta al usuario si quiere lanzar `@multi-probe-runner` para ejecutar sondas alternativas (puede tardar horas).
3. Si `ready_for_secondary_probes: false`:
   - El caso necesita primero `primary_arrays.json` (B-T1). Sugiere ejecutar `/run-case $1` primero con env `ARRAY_DUMP=1`.
