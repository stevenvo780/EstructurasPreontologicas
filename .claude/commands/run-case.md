---
description: Re-ejecuta uno o varios casos EDI del corpus con cola persistente y reintentos.
argument-hint: <case_id_o_lista> [max-jobs]
allowed-tools: Bash, Read
---

Re-ejecuta caso(s) del corpus EDI usando la cola del harness (con reintentos y fallback CPU si CUDA OOM).

1. Si `$1` es vacío, primero muestra: `python3 harness/cli.py queue --list-cases`
2. Si no: `python3 harness/cli.py queue --cases $1 --max-jobs ${2:-1} --dry`
   - Muestra al usuario qué se va a ejecutar.
3. Pide confirmación.
4. Si confirma: re-ejecuta sin `--dry`.
5. Tras ejecución:
   - Verifica con `python3 harness/cli.py verify --replay-hash`
   - Si el hash difiere del baseline, advierte y pregunta si actualizar baseline.
6. Para casos críticos (19, 16) recuerda los perfiles obligatorios:
   - Caso 19 (B-T5): `n_perm=2999` + bloque-permutación.
   - Caso 16 (B-E7): perfil canónico estricto `n_perm=999, n_boot=500`.
