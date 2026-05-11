---
borrador: IA
requires: H-J* + B-T
propuesta_fecha: 2026-05-11
destino: 02-fundamentos/06-protocolo-empirico.md + 06-cierre/Deuda residual + 00-proyecto/07-glosario-operativo.md
hallazgo: Bitacora/2026-05-04-continuous-run/TENG-01-permutacion-iid-temporales.md
tipo: insercion_deuda_residual + tarea_B-T_block_permutation
---

## Diagnóstico

`09-simulaciones-edi/common/hybrid_validator.py:174` implementa el test de permutación del EDI con permutación **iid** sobre los índices observacionales (`rng.permutation(n)`). Aplicado a series con dependencia temporal —y todos los casos del corpus EDI con señal genuina tienen `ACF(lag=1) > 0` por construcción del dominio: clima, deforestación, SIR, Lotka-Volterra, etc.— la permutación iid destruye la autocorrelación y la nula deja de ser la distribución correcta. Resultado estándar (Davison & Hinkley 1997, cap. 8 §8.2; Künsch 1989): bajo ACF > 0 la permutación iid **subestima la varianza** de la nula y por tanto **sesga los p-valores hacia abajo** (optimistas). El remedio canónico es block-permutation con longitud de bloque `ℓ ∝ n^{1/3}` o `ℓ ≈ 1/(1−ρ_1)`. El mismo defecto afecta a `bootstrap_edi` (línea 193, iid sobre índices).

## Verificación

- `09-simulaciones-edi/common/hybrid_validator.py:172-174` — `idx = np.array([rng.permutation(n) for _ in range(n_perm)])`. Confirmado: permutación iid de índices.
- `hybrid_validator.py:193` — `rng.randint(0, n, size=(n_boot, n))`. Confirmado: bootstrap iid.
- No existe `block_permutation_test_edi` ni `block_bootstrap_edi` en el módulo.
- Davison & Hinkley 1997, *Bootstrap Methods and Their Application*, Cambridge UP, cap. 8 §8.2 (pp. 385-396 sobre moving-block bootstrap). PDF **no presente** en `07-bibliografia/`; B-T:fetch-davison-hinkley-1997-cap8. El argumento operativo (iid → p optimista bajo ACF > 0) es resultado estándar; la cita literal sólo es necesaria si se inscribe paginación en el manuscrito.

## Texto propuesto (voz autoral filosófica de Jacob)

**Insertar en `02-fundamentos/06-protocolo-empirico.md` (sección de tests de significancia) y en la "Deuda residual" del cap 06-cierre:**

> **Deuda residual: permutación iid bajo dependencia temporal.** La implementación actual del test de permutación del EDI (`hybrid_validator.py:174`) y del bootstrap percentil (`hybrid_validator.py:193`) opera con permutación iid sobre los índices observacionales. Para series con autocorrelación no trivial —la gran mayoría del corpus EDI por construcción del dominio— la permutación iid destruye la dependencia temporal y la distribución nula deja de ser la correcta. Bajo `ACF(lag=1) > 0`, el resultado estándar (Davison & Hinkley 1997, *Bootstrap Methods and Their Application*, cap. 8 §8.2 — paginación pendiente de verificación tras fetch; resultado conceptual igualmente apoyado por Künsch 1989) es que los `p_perm` reportados están sesgados hacia abajo (optimistas). La corrección canónica es **block-permutation / moving-block bootstrap** con longitud de bloque `ℓ ∝ n^{1/3}` o derivada de la ACF empírica (Politis & White 2004 para selección automática).
>
> La auditoría no demuestra que los 40 casos del corpus tengan `p_perm` inválidos: sólo demuestra que el procedimiento es **inadmisible bajo dependencia temporal** y que el riesgo se concentra en los casos borderline (`p_perm ∈ [0.01, 0.05]`) y en los nulls del corpus, donde la corrección puede mover decisiones. En casos con `EDI ≫ 0` y margen amplio (Energía, Deforestación), `p_block` probablemente seguirá `< 0.01`. Cambiar a block-permutation **no invalida el EDI como métrica**; recalibra la inferencia frecuentista sobre él.

**Añadir entrada en `00-proyecto/07-glosario-operativo.md`:**

> **Block permutation / moving-block bootstrap.** Procedimiento alternativo a la permutación / bootstrap iid para series con dependencia temporal. Permuta o remuestrea **bloques contiguos** en lugar de índices individuales, preservando la autocorrelación dentro de cada bloque. Longitud de bloque sugerida: `ℓ ∝ n^{1/3}` o derivada de la ACF empírica. Su implementación canónica para el corpus EDI es deuda residual fechada (cf. `Bitacora/2026-05-04-continuous-run/TENG-01-permutacion-iid-temporales.md`).

## Acciones técnicas derivadas (B-T)

1. **Diagnóstico read-only inmediato (no requiere firma):** calcular `ACF(lag=1)` de las series `obs_val` de cada caso del corpus para identificar cuáles tienen `ρ_1 > 0.5`. Producir tabla por caso. Esto prioriza qué casos re-correr.
2. **Implementar `block_permutation_test_edi` y `block_bootstrap_edi`** en `hybrid_validator.py`, parámetro `block_length` con default `max(1, int(n ** (1/3)))`. Reportar ambos (`p_iid`, `p_block`) en `metrics.json` durante un período de transición.
3. **Recomputar p en ≥5 casos clima/epi/deforest** y casos null (02, 03, 12, 17, 19, 23, 25, 29). Acceptance: para casos con `ACF(1) > 0.5` reportar `|p_iid − p_block|`; cualquier caso que cruce el umbral 0.05 entre las dos variantes queda declarado como deuda residual o reclasificado.
4. **Actualizar la nota metodológica del cap 02-06** y la prosa de cap 06 con paginación verificada tras fetch.

## Costo argumentativo declarado

- Las afirmaciones de `p_perm < α` en los casos borderline del corpus carecen de garantía estricta bajo la regla actual; declararlo como deuda es mejor que descubrirlo en defensa.
- La corrección (block-permutation) no afecta al signo del EDI ni a la dirección de los hallazgos cualitativos; recalibra la inferencia frecuentista.
- Sin la deuda declarada y la tarea B-T abierta, F03-02 (Duhem-Quine sobre `p_perm` ya señalado en otra parte del triage) queda como flanco adicional.
