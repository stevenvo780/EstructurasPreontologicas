# TENG-04 — C2 sensibilidad: semillas divergentes CPU vs GPU

**Fecha:** 2026-05-04
**Origen:** process-verifier engine 2026-05-05
**Estado:** `needs_human` (toca semántica de C2 → afecta `metrics.json` de varios casos)

## (a) Verificación de la afirmación

La afirmación se confirma textualmente. En `09-simulaciones-edi/common/hybrid_validator.py`, dentro de `evaluate_c2` (función que decide el booleano C2 = robustez ante perturbación paramétrica), las dos ramas de ejecución usan esquemas de semilla incompatibles:

**Rama GPU/batch (línea 977):**
```python
preds = _batch_fn(bp, param_variants, steps, seed=seed_base,
                  series_key=series_key,
                  init_range=float(bp.get("init_range", 0.5)))
```
Una única `seed=seed_base` para las `n_pert` simulaciones del batch. La firma de `simulate_abm_batch` (`abm_core_gpu.py:326-394`) confirma que ese `seed` es escalar y se reutiliza para todo el batch (incluso en su fallback CPU interno: línea 380, `seed=seed` para cada variante).

**Rama CPU paralela (línea 997):**
```python
sim = simulate_abm_fn(p, steps, seed=2 + i + 10)
```
Cada réplica `i ∈ [0, n_pert)` recibe una semilla **distinta** (12, 13, 14, …), independiente de `seed_base`.

**Consecuencia operativa:**
- En GPU, las `n_pert` réplicas comparten ruido estocástico interno; sólo varían los parámetros perturbados (`perturb_params(..., seed=seed_base+i)` ya difiere por réplica). La dispersión observada en `deltas_m`, `deltas_v` mide **únicamente** sensibilidad paramétrica.
- En CPU, las réplicas combinan perturbación paramétrica **+** ruido estocástico distinto por réplica. La dispersión es estrictamente mayor (en expectación), por lo que `avg_dm/base_scale` puede cruzar el umbral 0.5 hacia C2=False en CPU mientras GPU reporta C2=True.

El booleano C2 publicado en `metrics.json` no es invariante a la plataforma. La afirmación de la tarea es correcta.

Adicionalmente, el literal `2 + i + 10` (= `12 + i`) está hardcoded sin referencia a `seed_base` y sin documentación de por qué se desplaza desde 12. Apariencia de leftover de convención antigua.

## (b) Propuesta de edición

La acceptance pide "Unificar CPU path a `seed=seed_base`". Esto reproduce la semántica GPU exactamente (todas las réplicas comparten ruido; sólo el parámetro perturbado varía).

**Edición concreta propuesta** (`hybrid_validator.py:997`):

```python
# Antes
sim = simulate_abm_fn(p, steps, seed=2 + i + 10)
# Después
sim = simulate_abm_fn(p, steps, seed=seed_base)
```

**Alternativa más conservadora:** `seed=seed_base + i` (cada réplica con semilla distinta pero derivada de `seed_base`). Esto NO unifica con GPU pero sí elimina el literal mágico `12+i` y hace la CPU reproducible bajo cambios de `seed_base`. **Costo:** sigue divergiendo de GPU.

**Recomendación para Jacob/Steven:** la opción del acceptance (`seed=seed_base`) es la única que cumple el criterio de "C2 booleano idéntico CPU vs GPU". Consecuencia: la métrica C2 medirá **sólo** sensibilidad paramétrica, no ruido estocástico. Esto es metodológicamente más limpio (C3 ya cubre persistencia bajo distintas semillas en `evaluate_c3`, líneas 1019-1025).

## (c) Costo argumentativo declarado

1. **Re-ejecución obligatoria.** Cambiar la semilla CPU re-genera todos los `metrics.json` de los 40 casos (más corpus multi-escala). El acceptance exige verificar identidad CPU↔GPU en 5 casos con C2=True. Esto requiere `./tesis run --cpu --case <NN>` y `./tesis run --gpu --case <NN>` y diff de `metrics.json`. Coste de cómputo no despreciable.

2. **Algunos C2 publicados pueden flipear.** Casos cuyo C2=True actual en CPU dependa del ruido inter-réplica (no de robustez paramétrica genuina) pasarían a C2=False, o viceversa. La prosa del manuscrito que citaba C2=True para esos casos requeriría rewrite. Imposible saber cuántos sin re-ejecutar.

3. **Decisión metodológica de fondo (H-J).** ¿C2 debe medir robustez paramétrica pura (GPU semantics) o robustez paramétrica + estocástica (CPU semantics actual)? La tesis defiende C2 como sensibilidad paramétrica (cap 02 §protocolo C1-C5), por lo que la unificación a GPU es coherente con la definición declarada. Pero esto debe firmarlo Jacob, no la asistencia, porque cambia retroactivamente la interpretación de cifras ya publicadas en bitácoras anteriores.

4. **CHANGELOG y trazabilidad.** El cambio debe registrarse en un CHANGELOG con commit hash y fecha; todos los `metrics.json` regenerados deben actualizar `engine_version`/`hash`. Si no se hace, `replay_hash.py` reportará divergencia falsa positiva en cualquier auditoría futura.

## Marca

`needs_human` — requiere firma de Jacob (decisión metodológica sobre semántica de C2) y compromiso de re-ejecución del corpus completo. La asistencia NO debe aplicar el patch unilateralmente.

## Referencias

- `09-simulaciones-edi/common/hybrid_validator.py:977` (rama GPU)
- `09-simulaciones-edi/common/hybrid_validator.py:997` (rama CPU)
- `09-simulaciones-edi/common/abm_core_gpu.py:326-394` (firma batch confirma seed escalar)
- `09-simulaciones-edi/common/hybrid_validator.py:1019-1025` (`evaluate_c3` usa seeds distintas a propósito; refuerza que C2 NO debe variarlas)
