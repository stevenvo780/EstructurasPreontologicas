# AU-1 — Caso 26 Starlink: cuarentena heredada de B-T5

**Fecha:** 2026-05-04
**Auditor:** sub-agente harness (continuous-run)
**Estado:** `needs_human` (requiere firma de Jacob para reclasificación final)

## (a) Verificación de la afirmación

La afirmación citada por adversarial-reviewer (2026-05-05) es factualmente correcta y, peor aún, sub-reportada en gravedad.

Fuente: `09-simulaciones-edi/26_caso_starlink/outputs/metrics.json`, fase `real` (líneas 679–765):

| Campo | Valor | Implicación |
|---|---:|---|
| `data.val_steps` | **1** | Una sola observación de validación. |
| `edi.value` | 0.6891705119737255 | EDI numéricamente alto. |
| `edi.ci_lo` == `edi.ci_hi` == `edi.value` | 0.6891705… | **CI bootstrap colapsado** (sin variabilidad — esperable con n=1). |
| `edi.permutation_pvalue` | 1.0 | Permutación no significativa. |
| `edi.permutation_significant` | false | El propio aparato lo declara no significativo. |
| `correlations.abm_obs` / `ode_obs` | 0.0 / 0.0 | Correlaciones nulas con la observación. |
| `viscosity.pass` | false; `recovered`: false | Falla criterio de viscosidad. |

Con `val_steps=1`, RMSE_coupled y RMSE_no_ode son cada uno una distancia escalar entre dos puntos; el cociente carece de contenido estadístico. La permutación sobre n=1 no tiene grados de libertad, y el bootstrap no puede remuestrear (de ahí el CI colapsado). El EDI=0.689 reportado es **un artefacto numérico, no una medición**.

Esto es estructuralmente idéntico a la patología B-T5 del caso 19, ya en cuarentena.

### Cómo aparece en prosa actualmente

- `05-aplicaciones/07-mapa-aplicaciones-corpus.md:124` — bloque "Trend (Nivel 1)", con comentario "val_steps=1 — exploratorio". El comentario es honesto pero la **clasificación como Nivel 1 no se sostiene**: un EDI con CI degenerado y p=1.000 no es "trend", es estadísticamente inválido.
- `06-cierre/04-versiones-cortas-defensa.md:110` — Starlink listado entre los "4 trend" del corpus inter-dominio. Si se reclasifica a cuarentena, el conteo agregado del corpus cambia (4 trend → 3 trend; añadir a la lista de casos en cuarentena junto a 19).

## (b) Propuesta de edición concreta

**No editable desde la asistencia** porque toca el conteo agregado del corpus (40 casos) que aparece en defensas cortas firmadas por Jacob. Tres salidas posibles, con costos:

1. **Cuarentena explícita (preferida por simetría con B-T5).**
   - Mover caso 26 de "Trend (Nivel 1)" a una sub-sección "Casos en cuarentena por val_steps insuficiente" junto con caso 19.
   - Re-ejecutar con `val_steps>=8` y `n_perm=2999` (acceptance criterion declarado).
   - Costo: rompe el lema "4 trend" en defensas cortas; obliga a actualizar 06-cierre/04, 05-aplicaciones/07 y agregados.

2. **Re-ejecución antes de reclasificar.**
   - Ejecutar `python3 09-simulaciones-edi/26_caso_starlink/src/validate.py` con dataset extendido o reconfiguración del split real (actual `real_start=2019-01-01`, `real_split=2022-01-01`, `real_end=2024-06-01` — el problema es que el dataset real `data/dataset.csv` parece tener una sola observación post-split).
   - Costo: requiere verificar si el CSV admite extensión a más puntos validables, o si el caso es estructuralmente N=1 (en cuyo caso no es "exploratorio", es null por insuficiencia de datos).

3. **Aceptar como deuda declarada sin reclasificar.**
   - Mantener el bloque V pero marcar el caso con asterisco visible y nota: "EDI no interpretable bajo val_steps=1; resultado retenido sólo como evidencia de pipeline operativo, no como medición".
   - Costo: dejar prosa que el lector hostil leerá como autoindulgencia (CLAUDE.md §1).

**Recomendación técnica:** combinar (1)+(2) — cuarentena explícita + intento de re-ejecución con `val_steps>=8`. La salida (3) es la más débil y debe rechazarse.

## (c) Costo argumentativo declarado

- El corpus pierde un caso del bloque "Trend"; el lema "4 strong + 8 weak + 2 suggestive + 4 trend + 8 null + 3 falsación" en `06-cierre/04` cambia a "… 3 trend + 9 cuarentena/null".
- La narrativa de "40 casos justifican operativamente el marco" no se daña: el caso queda dentro del corpus, sólo se reclasifica.
- Riesgo de no hacerlo: en defensa pública un revisor que abra `metrics.json` ve `val_steps=1` y `ci_lo==ci_hi` y la afirmación "Starlink trend EDI=0.69" es inmediatamente rechazable. **El costo de mantenerlo es mayor que el de reclasificar.**

## Acción operativa pendiente (`needs_human`)

- [ ] **H-J / B-T:** Jacob decide salida (1), (2) o combinación.
- [ ] **B-T (técnica):** si se elige re-ejecución, comprobar viabilidad de `val_steps>=8` en dataset real Starlink (datos de lanzamientos/debris); si no es viable, reclasificar a null.
- [ ] **B-E (prosa):** actualizar 05-aplicaciones/07-mapa-aplicaciones-corpus.md y 06-cierre/04-versiones-cortas-defensa.md tras decisión.
- [ ] Vincular a B-T5 (caso 19) como tarea hermana — misma patología, mismo tratamiento.

## Archivos consultados

- `09-simulaciones-edi/26_caso_starlink/case_config.json` (split real 2022-01 → 2024-06, freq mensual ⇒ ~29 meses; val_steps=1 sugiere pérdida masiva de puntos por preprocesado, no por dataset).
- `09-simulaciones-edi/26_caso_starlink/outputs/metrics.json` (líneas 679–765).
- `05-aplicaciones/07-mapa-aplicaciones-corpus.md:124`.
- `06-cierre/04-versiones-cortas-defensa.md:110`.

No se editó `Tesis.md` ni `metrics.json` (CLAUDE.md §4, hooks del harness).
