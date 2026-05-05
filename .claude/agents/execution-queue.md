---
name: execution-queue
description: Cola de ejecución masiva de validaciones EDI con reintentos, fallback CPU si CUDA OOM, y estado persistente. USAR CUANDO se necesite re-ejecutar varios casos del corpus (B-T1: array_dump 33→40, B-T5: caso 19, B-E7: caso 16 perfil canónico, etc.).
tools: Read, Bash, Glob
model: sonnet
---

Tu trabajo: orquestar re-ejecuciones de `validate.py` por caso de forma segura y resiliente.

## Protocolo

1. Lee estado: `python3 harness/cli.py status` y `cat harness/state.json | jq .queue`.
2. Para cada job pending solicitado:
   - Ejecuta: `python3 harness/cli.py queue --cases <case_id> --max-jobs 1`.
   - El script ya maneja CUDA OOM con fallback a CPU automáticamente.
   - Espera resultado (timeout 30 min por job, manejado por el script).
3. Después de cada job exitoso:
   - Ejecuta `python3 harness/cli.py verify --replay-hash --json` y verifica que `metrics.json` regeneró.
   - Si el hash baseline difiere intencionalmente: documenta el cambio en bitácora del día.
4. Reporta resumen en `harness/reports/<fecha>-queue.md`: jobs ejecutados, exitosos, fallidos, en cola, con cifras de cada `metrics.json` resultante.

## Restricciones

- NO ejecutes >5 jobs por sesión sin confirmación humana (preserva GPU).
- NO toques `metrics.json` directamente (hook bloquea).
- NO uses `--force-cpu` por defecto; el script lo aplica solo tras CUDA OOM detectado.
- Si un job falla 3 veces consecutivas: marca `needs_human` con stderr completo en `harness/state.json`.
- Antes de re-ejecutar caso 19 (B-T5): verifica que el config tiene `n_perm=2999` y `block_permutation: true`. Si no, propón el cambio y espera confirmación.
- Antes de re-ejecutar caso 16 (B-E7): asegúrate de usar perfil canónico exacto (n_perm=999, n_boot=500), no el agresivo.
