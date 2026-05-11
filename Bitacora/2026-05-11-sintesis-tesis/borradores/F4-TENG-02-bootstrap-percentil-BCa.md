---
borrador: IA
requires: H-J* + B-T
propuesta_fecha: 2026-05-11
destino: 02-fundamentos/06-protocolo-empirico.md + 06-cierre/Deuda residual
hallazgo: Bitacora/2026-05-04-continuous-run/TENG-02-bootstrap-percentil-sesgo-pequenas.md
tipo: insercion_deuda_residual + tarea_B-T_BCa
---

## Diagnóstico

`09-simulaciones-edi/common/hybrid_validator.py:193,216-219` implementa el CI bootstrap como **percentil simple** (sin corrección de sesgo z₀ ni de aceleración a). El bootstrap percentil tiene sesgo `O(n^{-1/2})` frente al BCa `O(n^{-1})` (DiCiccio & Efron 1996). El corpus EDI tiene **21/32 casos con `val_steps < 30`** y **12 casos con `val_steps = 8`** — régimen donde el sesgo del percentil es **material**, no cosmético. Para `n = 8` el sesgo puede ser ≈ 35 % del intervalo en el peor caso. Los CIs reportados en el manuscrito como "95 %" tienen cobertura nominal sólo aproximada al orden `O(n^{-1/2})`.

## Verificación

- `hybrid_validator.py:193,216-219` — bootstrap percentil simple: `samples_sorted = np.sort(samples); lo = samples_sorted[int(alpha*n_boot)]; hi = samples_sorted[int((1-alpha)*n_boot)]`. Confirmado.
- No hay corrección z₀, no hay aceleración a, no hay campo `ci_method` en `metrics.json`.
- Conteo de `val_steps` sobre los 32 casos del corpus inter-dominio: 21 con `val_steps < 30`, 12 con `val_steps = 8`, 1 con `val_steps = 9`, 11 con `val_steps ≥ 30` (verificación en F4-TENG-02 origen §A).
- DiCiccio & Efron 1996, "Bootstrap confidence intervals", *Statistical Science* 11(3):189-228, esp. §2.3 (percentil) y §3 (BCa). PDF **no presente** en `07-bibliografia/`; B-T:fetch-diciccio-efron-1996. El argumento operativo (sesgo `O(n^{-1/2})` del percentil para n pequeño) es consenso estadístico estándar y sostiene la deuda declarada sin cita literal.

## Texto propuesto (voz autoral filosófica de Jacob)

**Insertar en `02-fundamentos/06-protocolo-empirico.md` (sección sobre intervalos de confianza) y en la "Deuda residual" del cap 06-cierre:**

> **Deuda residual: bootstrap percentil simple en régimen de pocas muestras.** El CI bootstrap del EDI se computa actualmente como **percentil simple** sobre 500 remuestreos (`hybrid_validator.py:193`). El bootstrap percentil tiene sesgo `O(n^{-1/2})` frente a BCa `O(n^{-1})` (DiCiccio & Efron 1996, *Statistical Science* 11(3):189-228 — paginación pendiente de verificación tras fetch). El corpus EDI cuenta con 21/32 casos con `val_steps < 30` y 12 casos con `val_steps = 8`, régimen donde el sesgo del percentil es **material**. La afirmación de "CI 95 %" en esos casos tiene cobertura nominal sólo aproximada al orden `O(n^{-1/2})`.
>
> Lo que la tesis puede defender hoy sin BCa: los `p_perm` (test de permutación, no afectado por este hallazgo, aunque sujeto a F4-TENG-01) y la dirección/signo del EDI puntual. Lo que **no puede defender sin BCa o sin declarar la limitación**: la anchura precisa de los CI en casos con `val_steps ≤ 15` (15/32 casos del corpus inter-dominio).
>
> Mitigación inmediata declarada (sin re-correr casos): el campo `val_steps` se reportará explícitamente junto a cada CI para que el lector calibre el orden de cobertura. Mitigación completa (deuda B-T): implementar BCa en `bootstrap_edi` activado cuando `n < 30`, añadir campo `ci_method` (`"percentile"` o `"BCa"`) y campos `bca_z0`, `bca_a` en `metrics.json` para trazabilidad, ejecutar simulación de cobertura empírica con EDI conocido en `n ∈ {8, 15, 30, 100}` y re-correr los 21 casos con `val_steps < 30` reportando el delta de CI antes de tocar la prosa del manuscrito.

## Acciones técnicas derivadas (B-T)

1. Implementar BCa en `bootstrap_edi` con corrección de sesgo (`z₀` por fracción de muestras bootstrap menores que el estimador puntual) y aceleración (`a` por jackknife conjunto sobre `obs, abm, red`).
2. Añadir `ci_method`, `bca_z0`, `bca_a`, `n_val` en `metrics.json`.
3. Validación de cobertura empírica con EDI conocido en `n ∈ {8, 15, 30, 100}` comparando cobertura 95 % nominal de percentil vs BCa.
4. Re-correr los 21 casos con `val_steps < 30`; reportar el delta de CIs en bitácora antes de modificar la prosa.

## Costo argumentativo declarado

- 21 CIs del corpus tienen sesgo de orden `O(n^{-1/2})` sin declararlo, vulnerabilidad clara ante un revisor estadístico.
- Coste de actuar: rompe hashes de `metrics.json` en ≥21 casos; re-validar cada uno; ajuste potencial de prosa en `05-aplicaciones/` y tablas en `02-fundamentos/`. Trabajo ≈1 jornada técnica si se hace bien.
- Coste de no actuar: si un revisor aplica BCa por su cuenta y los CIs no replican, el caso es defendible declarando "percentil" pero pierde fuerza inferencial; con la deuda declarada y la B-T abierta, la posición queda mantenible.
