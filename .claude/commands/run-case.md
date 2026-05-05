---
description: Re-ejecuta uno o varios casos EDI del corpus invocando directamente validate.py.
argument-hint: <case_id_o_lista> [perfil:canonico|agresivo]
allowed-tools:
  - Bash
  - Read
---

Re-ejecuta caso(s) del corpus EDI. La ejecución la hace `@execution-queue`, NO un wrapper Python.

1. Si `$1` es vacío:
   ```bash
   ls 09-simulaciones-edi/ | grep '_caso_'
   ```
   y muestra al usuario para que elija.

2. Si `$1` está dado:
   - Verifica que existe `09-simulaciones-edi/$1/src/validate.py`.
   - Lee `09-simulaciones-edi/$1/case_config.json` y muéstralo.
   - Recuerda perfiles obligatorios:
     * **Caso 19 (B-T5):** `HYPER_N_PERM=2999 HYPER_N_BOOT=1500` + bloque-permutación.
     * **Caso 16 (B-E7):** perfil canónico estricto `HYPER_N_PERM=999 HYPER_N_BOOT=500`.

3. Pide confirmación al usuario antes de ejecutar (puede tardar 5-30 min).

4. Si confirma: invoca `@execution-queue` con el caso para que orqueste la ejecución (con manejo de CUDA OOM, timeout, reintentos).

5. Tras ejecución exitosa:
   - `python3 harness/cli.py verify --replay-hash`
   - Si `drift_count > 0`: pregunta al usuario si actualizar el baseline.
