# TENG-03 — GPU batch: init_noise compartido entre candidatos

**Fecha:** 2026-05-05
**Archivo auditado:** `09-simulaciones-edi/common/abm_core_gpu.py:583-584`
**Origen:** Hallazgo de `process-verifier` engine 2026-05-05
**Status:** `needs_human`

## (a) Verificación textual de la afirmación

Confirmado. Línea 583:

```python
init_noise = rng.uniform(-init_range, init_range, (n, n))  # (n, n) en GPU
grids = _xp.full((B, n, n), grid_center, dtype=_xp.float64) + init_noise[None, :, :]
```

Los B candidatos del grid search en modo `macro_mode == "mean"` arrancan con
**la misma realización de ruido inicial**, broadcast vía `[None, :, :]`. El
comentario en línea 582 lo declara explícitamente:

> "Usamos la misma perturbación para todas (reproducibilidad determinista)"

El mismo patrón se repite en línea 619 para el ruido temporal (`noise_base` es
`(n, n)` y se difunde a todos los candidatos), con justificación adicional en
líneas 616-618: la ruta CPU asigna **el mismo `seed` por candidato**, así que
todos comparten la realización base y solo difieren en escala/parámetro.

## (b) Costo argumentativo

Esto **no es un bug aislado** — es una decisión de diseño cuyo objetivo
declarado es mantener paridad CPU↔GPU. Cambiarlo a `(B, n, n)` con subseeds por
candidato (lo que pide el acceptance) **rompería esa paridad**, no la
restauraría. La afirmación del verificador de que esto induce "sesgo
exploratorio del grid search" es **parcialmente correcta pero
mal-direccionada**:

- **Verdadero:** el grid search no explora el espacio inicial; explora solo el
  espacio de parámetros condicionado a una única condición inicial.
- **Falso (implícito):** que el GPU haga lo mismo que el CPU sea una anomalía
  del GPU. El CPU ya tenía esta semántica.

Si la objeción real es "el grid search debería marginalizar sobre condición
inicial", la corrección debe aplicarse **en CPU y GPU simultáneamente**, y el
costo es:

1. Pierde reproducibilidad bit-exacta entre candidatos (deja de ser un control
   de varianza limpio sobre parámetros).
2. Aumenta varianza del estimador RMSE de calibración → puede degradar la
   selección de hiperparámetros si `B` es pequeño.
3. Re-calibración de los 40 casos del corpus (las cifras EDI publicadas
   asumen la semántica actual).

## (c) Propuesta concreta

**No editar** sin firma de Jacob/Steven. Requiere decisión sobre:

1. ¿La intención del grid search es marginal sobre IC o condicional a una IC
   fija? La literatura ABM admite ambas; la tesis no declara cuál asume.
2. Si se opta por marginal: implementar `init_noise = rng.uniform(..., (B, n, n))`
   con subseeds derivados de `SeedSequence(seed).spawn(B)` en CPU **y** GPU.
   Re-correr corpus completo y comparar EDI antes/después.
3. Si se opta por condicional (status quo): documentarlo en
   `00-proyecto/07-glosario-operativo.md` como decisión metodológica
   declarada, no como detalle de implementación oculto.

El acceptance criterion como está formulado (`|rmse_calib_cpu -
rmse_calib_gpu|/rmse_calib_cpu < 0.05`) no discrimina entre las dos opciones
porque CPU y GPU actualmente coinciden en ambas semánticas posibles.

## Marcadores

- `needs_human`: decisión metodológica (Jacob)
- Etiqueta sugerida en `TAREAS_PENDIENTES.md`: **H-J** (no B-T) — porque la
  acción correcta no es un fix técnico, es una declaración filosófico-metodológica.
- No tocar Tesis.md ni metrics.json hasta resolver (1).
