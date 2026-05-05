# TENG-06 — np.random.seed(42) global antes de joblib fork

**Fecha:** 2026-05-04
**Hallazgo origen:** process-verifier engine 2026-05-05
**Archivo señalado:** `09-simulaciones-edi/common/hybrid_validator.py:1278`
**Estado:** `needs_human` (ver §c)

## (a) Verificación de la afirmación

Confirmado parcialmente. Líneas 1275-1279 de `hybrid_validator.py`:

```python
# Fix reproducibilidad: fijar estado global de RNG al inicio de cada fase.
# Esto garantiza que resultados no varíen entre ejecuciones dado los mismos
# datos de entrada. Cada función interna usa su propio seed local además.
np.random.seed(42)
random.seed(42)
```

`evaluate_phase` ejecuta este seed global **antes** de invocar `Parallel(backend="loky")` en cuatro puntos (calibración grid `:719`, refinamiento `:810`, C2 `:1003`, C5 `:1095`). `loky` usa procesos hijos; en Linux con `fork`, cada worker hereda el estado RNG global del padre justo después de `np.random.seed(42)`.

**Mitigación parcial existente:** los closures `_eval_one_grid`, `_eval_one_c2`, `_eval_one_c5` pasan `seed=` explícito a `simulate_abm_fn(..., seed=seed)` y a `perturb_params(seed=seed_base + i)`. Si el ABM y `perturb_params` usan **exclusivamente** `np.random.RandomState(seed)` local (no `np.random.<func>` global), la correlación inter-worker se elimina en la práctica.

**Riesgo residual:** cualquier ruta interna que llame `np.random.normal()`, `np.random.choice()`, etc. **sin** RandomState explícito heredará el estado fijado por el padre — y todos los workers verán el **mismo** estado inicial → outputs estocásticos correlacionados aunque las semillas explícitas difieran. No audité ABM/ODE/perturb_params línea por línea para descartarlo.

**Costo declarado:** la afirmación del comentario "Cada función interna usa su propio seed local además" es una **promesa de la implementación**, no una garantía verificada. El comentario debe sustituirse por una auditoría que liste exactamente qué funciones usan global RNG.

## (b) Propuesta de edición

La acción operativa propuesta por el hallazgo (eliminar seed global; depender de `RandomState(seed)` locales; verificar `|Δrmse_calib| < 0.01` en casos 01,16,05) requiere:

1. **Auditoría previa** — grep `np.random\.(normal|choice|uniform|randint|rand|randn|standard_normal|permutation|shuffle)` en `common/abm_*.py`, `common/ode_models.py`, `common/topology*.py` y reemplazar usos globales por `rng = np.random.default_rng(seed)` local.
2. **Eliminar líneas 1278-1279** una vez la auditoría garantice que ninguna ruta depende del estado global.
3. **Test diferencial** — re-ejecutar casos 01 (clima), 16 (deforestación), 05 (mente) sin seed global y comparar `rmse_calib` y `edi`.

Edit concreto sugerido (post-auditoría):

```python
# Antes (líneas 1275-1279):
# Fix reproducibilidad: fijar estado global de RNG al inicio de cada fase.
np.random.seed(42)
random.seed(42)

# Después:
# Reproducibilidad: cada función interna recibe seed explícito y usa
# np.random.default_rng(seed) local. NO fijar estado global aquí porque
# loky-fork lo replica idéntico en todos los workers (correlación espuria).
```

## (c) Costo argumentativo y veredicto

**`needs_human`** porque:

- La auditoría sistemática del uso de `np.random` global en `common/abm_*.py` (~varias miles de líneas con backends CPU/GPU/NumPy) excede el alcance de un sub-agente de verificación.
- El test diferencial `|Δrmse_calib| < 0.01` requiere ejecutar `validate.py` en 3 casos × 2 condiciones (con/sin seed global) → 6 corridas con `n_perm=999`, lo cual es trabajo de `@execution-queue` con firma de Jacob/Steven, no decisión de auditoría.
- Si la auditoría revela usos de RNG global no triviales (p.ej. en inicialización ABM), eliminar el seed global **sin** convertirlos a RandomState locales **degradaría reproducibilidad**, no la mejoraría.

**Costo argumentativo declarado:** el comentario actual ("cada función interna usa su propio seed local además") es una afirmación no verificada que vive en el código. Si es falsa, los workers loky producen outputs correlacionados y los CIs bootstrap están subestimados. Si es verdadera, el seed global es redundante pero inocuo. El harness no puede distinguir cuál sin la auditoría + test diferencial.

**Acción humana requerida:** B-T (técnica) — Steven debe (i) ejecutar grep+auditoría sobre `common/abm_*.py` y módulos relacionados, (ii) si encuentra usos globales, convertirlos a `default_rng(seed)` local, (iii) ejecutar test diferencial en casos 01/16/05.

**No editar `metrics.json` ni `Tesis.md`** desde esta auditoría.

RESULT: complete | TENG-06-np-random-seed-global-correlaciona-workers | needs_human: auditoría+test diferencial 01/16/05
