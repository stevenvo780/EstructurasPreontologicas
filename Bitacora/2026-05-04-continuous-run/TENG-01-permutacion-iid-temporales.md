# TENG-01 — Permutación iid sobre series temporales

**Fecha:** 2026-05-04
**Origen:** process-verifier engine 2026-05-05
**Tipo:** auditoría técnica (read-only); produce propuesta, no edita código.

## Hallazgo verificado

`09-simulaciones-edi/common/hybrid_validator.py:174` implementa el test de
permutación del EDI con **permutación iid** de las observaciones:

```python
# línea 172-174
rng = np.random.RandomState(seed)
# Matriz de índices de permutación: (n_perm, n)
idx = np.array([rng.permutation(n) for _ in range(n_perm)])
obs_perms = obs_a[idx]  # (n_perm, n)
```

`rng.permutation(n)` reordena los índices de manera uniforme sin restricción
temporal. Aplicado a series con dependencia temporal (clima, epi, deforest,
SIR, Lotka-Volterra acoplados), **destruye la autocorrelación**: la nula
"intercambiable bajo permutación" presupone i.i.d., supuesto falso para los
casos del corpus EDI cuya señal proviene precisamente de la dinámica acoplada.

Consecuencia teórica conocida (Davison & Hinkley 1997, *Bootstrap Methods and
Their Application*, cap. 8 §8.2; Künsch 1989, *Annals of Statistics*
17(3):1217–1241): cuando la serie tiene ACF(lag=1) alta, la permutación iid
genera nulos con varianza **subestimada**, lo que sesga p-values hacia abajo
(optimistas). El remedio canónico es **block-permutation / moving-block
bootstrap** con longitud de bloque ℓ ≈ orden del tiempo de mezcla del proceso
(rule-of-thumb ℓ ∝ n^{1/3} ó ℓ ≈ 1/(1−ρ₁)).

Verificación adicional: en `hybrid_validator.py` no existe ninguna
implementación block-based; `bootstrap_edi` (l. 193) también es iid sobre
índices (`rng.randint(0, n, size=(n_boot, n))`). El mismo problema afecta el
CI bootstrap, no solo el p-value.

## Citación primaria

Davison, A.C. & Hinkley, D.V. (1997). *Bootstrap Methods and Their
Application*. Cambridge University Press, cap. 8 "Complex Dependent Data
Structures", §8.2 "Time Series", pp. 385–396 (introducción del moving-block
bootstrap; discusión explícita de p. 386–388 sobre invalidez de iid bajo
dependencia y elección de ℓ).

**Estado de la cita:** el PDF NO está confirmado en `07-bibliografia/`. La
afirmación operativa (iid → p optimista bajo ACF>0) es resultado estándar y se
puede defender sin la cita textual; pero si Jacob quiere inscribir la corrección
en el manuscrito con paginación, requiere obtener el capítulo. Marcado
`needs_human` por §5 de CLAUDE.md.

## Costo argumentativo

- La auditoría **no demuestra** que los 40 casos del corpus tengan p-values
  inválidos: solo demuestra que el procedimiento es **inadmisible bajo
  dependencia temporal**, lo cual es un requisito procedimental.
- En casos donde EDI≫0 con margen amplio (clima, deforest), p_block
  probablemente seguirá <0.01 aun con corrección. El riesgo real está en casos
  borderline (p_iid ∈ [0.01, 0.05]) y en los nulls del corpus, donde la
  corrección puede mover decisiones.
- Cambiar a block-permutation **no invalida el EDI como métrica**; solo
  recalibra la inferencia frecuentista sobre él.

## Propuesta de edición (needs_human, B-T*)

No editado — la modificación toca el núcleo del validador y debe re-ejecutar
el corpus. Requiere firma de Jacob/Steven:

1. **Implementar `block_permutation_test_edi`** en `hybrid_validator.py`:
   - parámetro `block_length` (default: `max(1, int(n ** (1/3)))` ó derivado
     de ACF empírica; ver Politis & White 2004 para selección automática);
   - permutación de bloques contiguos en lugar de índices individuales;
   - mismo n_perm=999.
2. **Implementar `block_bootstrap_edi`** análogo (moving-block bootstrap).
3. **Reportar ambos** (`p_iid`, `p_block`) en `metrics.json` durante un periodo
   de transición; `p_block` pasa a ser la cifra canónica.
4. **Recomputar p en ≥5 casos** clima/epi/deforest y casos null (02, 03, 12,
   17, 19, 23, 25, 29) para medir |p_iid − p_block|. Acceptance del task: para
   casos con ACF(1)>0.5 la diferencia <0.05 (criterio de no-cambio
   sustantivo); cualquier caso que cruce el umbral de 0.05 entre las dos
   variantes debe quedar declarado como deuda residual o re-clasificado.
5. **Actualizar `00-proyecto/07-glosario-operativo.md`** y la nota
   metodológica del cap. 02 de fundamentos para citar Davison-Hinkley §8.2 con
   paginación verificada (depende del paso de bibliografía).

## Acciones que sí son ejecutables ahora (sin firma)

- Calcular ACF(lag=1) de las series `obs_val` por caso para identificar cuáles
  realmente tienen dependencia fuerte (`ρ₁>0.5`). Esto es diagnóstico
  read-only y prioriza qué casos re-correr cuando se implemente block-perm.
- Auditar si algún caso ya **sub-muestrea** la serie a paso suficientemente
  grande como para aproximar independencia (algunos casos clima/epi tienen
  resolución anual: ρ₁ puede ser bajo). Eso reduciría el universo afectado.

Estas dos acciones se proponen como nuevas tareas B-T (no se ejecutan en este
reporte por scope).

## Veredicto

`needs_human` — **B-T pendiente:** "Reemplazar permutación/bootstrap iid por
variantes block-based en `hybrid_validator.py` y recomputar corpus".

La afirmación del process-verifier es **correcta y verificable en el código
fuente**. La corrección es no-trivial (toca núcleo del validador, requiere
re-correr corpus, posible cambio de p-values reportados en manuscrito) y debe
ser autorizada por Jacob/Steven antes de editar.

RESULT: complete | TENG-01-permutacion-iid-temporales | hallazgo confirmado, propuesta needs_human (B-T)
