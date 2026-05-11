---
borrador: IA
requires: H-J* + B-T
propuesta_fecha: 2026-05-11
destino: 00-proyecto/07-glosario-operativo.md (entrada C2) + 04-debates/05-limitaciones-declaradas-consolidacion.md o nota de deuda en cap 06
hallazgo: Bitacora/2026-05-04-continuous-run/TENG-04-c2-cpu-vs-gpu-semillas-divergentes.md
tipo: insercion_deuda + tarea_B-T_unificar_semillas
---

## Diagnóstico

`evaluate_c2` en `hybrid_validator.py` usa esquemas de semilla **incompatibles** entre la rama GPU/batch y la rama CPU paralela:

- **GPU/batch (línea 977):** `_batch_fn(..., seed=seed_base, ...)` — única `seed=seed_base` compartida por todas las `n_pert` simulaciones; sólo varían los parámetros perturbados. Mide **sólo sensibilidad paramétrica**.
- **CPU paralela (línea 997):** `simulate_abm_fn(p, steps, seed=2 + i + 10)` — cada réplica `i ∈ [0, n_pert)` recibe semilla distinta `12 + i`. Combina perturbación paramétrica **+** ruido estocástico distinto por réplica.

El booleano C2 publicado en `metrics.json` **no es invariante a la plataforma**: la dispersión `avg_dm/base_scale` es estrictamente mayor (en expectación) en CPU, lo que puede mover C2 de True a False entre GPU y CPU para casos borderline. Adicionalmente, el literal mágico `2 + i + 10` (`= 12 + i`) está hardcoded sin documentación y sin referencia a `seed_base`.

## Verificación

- `hybrid_validator.py:977` (rama GPU) — `seed=seed_base` único.
- `hybrid_validator.py:997` (rama CPU) — `seed=2 + i + 10`.
- `abm_core_gpu.py:326-394` (firma `simulate_abm_batch`) — confirma seed escalar reutilizado en todo el batch.
- `hybrid_validator.py:1019-1025` (`evaluate_c3`) — sí usa semillas distintas a propósito; refuerza que C2 NO debe variarlas.

## Texto propuesto (voz autoral filosófica de Jacob)

**Añadir entrada en `00-proyecto/07-glosario-operativo.md` (en la sección sobre el protocolo C1-C5+):**

> **C2 (sensibilidad paramétrica).** Mide la robustez del modelo acoplado ante perturbaciones de parámetros, manteniendo fija la realización estocástica del ABM. La semántica canónica es **sensibilidad paramétrica pura**, no sensibilidad paramétrica + estocástica.
>
> Deuda técnica fechada: la implementación actual (`hybrid_validator.py:977,997`) viola esta semántica en la rama CPU paralela, que usa semillas estocásticas distintas (`seed=12+i`) en lugar de la semilla única (`seed=seed_base`) usada por la rama GPU batch. C2 booleano publicado en `metrics.json` no es por tanto invariante a la plataforma. La unificación a `seed=seed_base` en ambas ramas es B-T abierta; requiere re-ejecución del corpus completo (`./tesis run --cpu --case <NN>` y `./tesis run --gpu --case <NN>` con diff de `metrics.json`) y actualización de cualquier prosa que cite C2 en los casos borderline donde el booleano podría cambiar.

**Insertar nota en `04-debates/05-limitaciones-declaradas-consolidacion.md` o en la "Deuda residual" del cap 06:**

> **Deuda residual: invariancia CPU/GPU de C2.** La condición C2 del protocolo de validación (`hybrid_validator.py:evaluate_c2`) está implementada con esquemas de semilla incompatibles entre la rama GPU batch (semilla única, sensibilidad paramétrica pura) y la rama CPU paralela (semilla por réplica, mide paramétrica + estocástica). El booleano C2 publicado puede flipear entre plataformas para casos borderline. La unificación a semilla única (`seed=seed_base`) en CPU está propuesta como B-T y supone re-ejecución del corpus completo con actualización de cualquier afirmación de prosa que cite C2.

## Acciones técnicas derivadas (B-T)

- Aplicar el cambio en `hybrid_validator.py:997` de `seed=2 + i + 10` a `seed=seed_base`.
- Re-ejecutar 5 casos representativos en CPU y GPU; verificar identidad bit-a-bit de C2 booleano.
- Re-ejecutar corpus completo (40 inter-dominio + 10 inter-escala) y actualizar `engine_version`/`hash` en cada `metrics.json` para que `replay_hash.py` no reporte divergencia falsa positiva.
- Registrar el cambio en CHANGELOG del harness.

## Costo argumentativo declarado

- Algunos C2 publicados pueden cambiar al unificar; cualquier prosa que cite C2 = True para casos borderline debe revisarse en cascada.
- Coste de no actuar: dependencia oculta entre plataforma y resultado, vulnerable a auditoría adversarial.
- Coste recuperable: la unificación CPU↔GPU es el camino natural; C3 ya cubre persistencia bajo distintas semillas (líneas 1019-1025), por lo que C2 puede dedicarse sin pérdida a sensibilidad paramétrica pura.
