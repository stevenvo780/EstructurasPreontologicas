# TENG-11 — Viscosidad: umbral trivial y exclusión silenciosa de overall_pass

**Fecha:** 2026-05-04
**Origen:** process-verifier engine 2026-05-05
**Archivo:** `09-simulaciones-edi/common/hybrid_validator.py`
**Estado:** `needs_human` (B-T*) — requiere decisión técnica de Steven sobre umbral y firma de Jacob sobre semántica

## (a) Verificación de la afirmación

**Afirmación:** `relaxation_time > 1` es trivialmente satisfecho por cualquier sistema con damping<1; `c_visc` no está en `overall_pass`.

**Verificación literal:**

1. `hybrid_validator.py:1167` — `pass_viscosity = relaxation_time > 1`. Confirmado.
   El umbral `> 1` significa: basta que la diferencia con la base caiga bajo el 5% del shock inicial **a partir del paso shock_step+2** para pasar. Cualquier sistema con amortiguamiento mínimo lo cumple. No discrimina "alta viscosidad/inercia estructural" (la hipótesis del docstring, líneas 1119-1120) de "transiente corto trivial". El test reduce su semántica a "el shock fue absorbido en algún momento", lo cual es vacío frente a la hipótesis declarada.

2. `hybrid_validator.py:1831-1833` — `overall = all([c1, c2, c3, c4, c5, sym_ok, non_local_ok, persist_ok, emergence_ok, coupling_ok, not rmse_fraud, edi_valid, edi_significant])`. **`c_visc` NO aparece** en la conjunción. Sí se reporta en `results["viscosity"]` (líneas 1950-1953) pero como informe paralelo, no como criterio. El comentario en 1827-1830 declara la exclusión de `cr_valid` con justificación; **no existe** justificación análoga documentada para la exclusión de `c_visc`. Hay, por tanto, dos defectos compuestos:
   - umbral trivial que no opera como filtro,
   - exclusión silenciosa del único filtro existente respecto al gate de validación.

**Veredicto:** la afirmación del process-verifier es correcta en ambos puntos.

## (b) Propuesta de edición

Tres opciones, en orden creciente de costo:

**Opción 1 — Mínima (declarativa):** documentar la exclusión en docstring de `evaluate_viscosity` y dejar el test como informativo. Requiere agregar líneas a docstring explicando: "test informativo, no entra a overall_pass; semántica débil bajo umbral actual". Costo: cero ejecución, declara la deuda en código, no rehace métricas.

**Opción 2 — Parametrizar umbral:** sustituir `relaxation_time > 1` por `relaxation_time > val_steps * 0.2` (acceptance criterion del ticket), o por un parámetro configurable `case_config.viscosity_min_relaxation`. Re-ejecución de los 40 casos para verificar que algunos pasen y otros no — actualmente todos pasan trivialmente o quedan ocultos. Costo: re-correr corpus; pueden cambiar reportes de viscosidad por caso (no `overall_pass` mientras `c_visc` no entre al gate).

**Opción 3 — Incorporar `c_visc` a overall_pass con umbral parametrizado:** combina opción 2 y agrega `c_visc` a la lista de la línea 1831. Esto es invasivo: cambia `overall_pass` de casos previamente positivos. Requiere firma humana porque modifica el criterio de éxito declarado en la tesis.

**Recomendación neutral:** Opción 1 + 2 sin tocar `overall_pass`. Documentar en docstring por qué se excluye, parametrizar umbral para que sea informativo no trivial, dejar la inclusión en gate como decisión de Jacob (H-J).

## (c) Costo argumentativo declarado

- Si se mantiene status quo: la tesis reporta un "test de viscosidad" cuya pasada no significa nada operativamente. Riesgo F6 (citación/criterio decorativo) en clave estadística: criterio que se invoca sin engagement real con la hipótesis que dice testear. Vulnerable a objeción del tipo "su métrica de inercia estructural no distingue inercia de relajación trivial".
- Si se adopta Opción 2 sin Opción 3: gana honestidad metodológica (test deja de ser trivial) pero la tesis admite que `c_visc` es indicador no requisito; debe declararse en `02-objeciones-y-riesgos.md` o glosario.
- Si se adopta Opción 3: cambian resultados publicados; se requiere re-ejecutar corpus, actualizar `metrics.json` por caso, regenerar tablas. Costo alto y firma `H-J` obligatoria.

## Marcado

`needs_human` — B-T* (decisión técnica sobre umbral) + H-J (si se incorpora a `overall_pass`). No se edita `Tesis.md` ni `metrics.json`.

RESULT: complete | TENG-11-viscosidad-umbral-trivial | confirmado: umbral trivial + c_visc fuera de overall_pass; needs_human
