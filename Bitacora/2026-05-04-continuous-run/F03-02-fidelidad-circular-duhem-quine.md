# F03-02 — Fidelidad relacional: circularidad y Duhem-Quine

**Fecha:** 2026-05-05
**Origen:** Hallazgo `adversarial-reviewer` cap03 (2026-05-05).
**Archivo señalado:** `03-formalizacion/02-criterios-de-legitimidad-y-metodo.md:26`
**Acceptance:** Dossier §10 (Intervención discriminante) requiere banda predictiva pre-registrada con τ explícita antes de la prueba interventiva.

---

## (a) Verificación de la afirmación citada

Texto literal en línea 26 (criterio 2.3 *Fidelidad relacional*):

> "La fidelidad se prueba con intervención: si manipular una variable supuestamente comprimida produce **diferencia inferencial inesperada**, la compresión ocultaba estructura relevante."

**Verificado.** El criterio formula el test interventivo en términos de *"diferencia inferencial inesperada"* sin definir respecto a qué expectativa, y sin exigir banda predictiva pre-registrada ni umbral τ.

Inspección del Dossier de anclaje (§3.1, líneas 64-79):

- Componente 9: "Predicción discriminante — contra rival explícito".
- Componente 10: "Intervención discriminante — experimento que la falsaría".

Ninguno de los dos componentes obliga a **declarar antes de la intervención** la banda predictiva (rango cuantitativo de la "diferencia esperada" bajo H0 modelo-acoplado y bajo H1 modelo-desacoplado) ni el umbral τ que separa "compatible" de "falsado". §3.3 (criterio de fallo) dice "la intervención discriminante se evita" pero no "la intervención discriminante carece de banda pre-registrada".

## (b) Diagnóstico filosófico

**La objeción es sólida y válida.** Tal como está, el criterio 2.3 admite tres patologías:

1. **Circularidad model-relativa.** "Inesperada" se mide contra la predicción del propio modelo comprimido. Si la diferencia observada cae fuera, el autor puede (i) declarar que la compresión ocultaba estructura, **o** (ii) re-ajustar el modelo *post hoc* hasta que la diferencia deje de ser "inesperada". La elección entre (i) y (ii) no está reglada por el texto actual.

2. **Evasión Duhem-Quine.** Sin τ pre-registrado, cualquier resultado interventivo puede absorberse modificando hipótesis auxiliares (régimen de medición R, dimensionalidad efectiva de κ, condiciones de frontera del ABM, hiperparámetros de la sonda ODE). El holismo confirmacional queda libre.

3. **Asimetría con el motor EDI.** El propio aparato empírico de la tesis (cap. 03-04, métrica EDI con permutación 999, bootstrap 500, p < 0.05) **sí** pre-registra estructura inferencial: H0 nula, estadístico (RMSE_coupled vs RMSE_no_ode), distribución de referencia, umbral. Es decir: la metodología técnica del corpus es más estricta que el criterio filosófico que pretende justificarla. Esa asimetría es síntoma de la deuda.

## (c) Propuesta de edición concreta

**Reescritura mínima del criterio 2.3 (línea 26)** — aporta operatividad sin cambiar la doctrina:

> ### 2.3. Fidelidad relacional
>
> La compresión no debe borrar dependencias que cambian el fenómeno bajo Q. La fidelidad se prueba con **intervención pre-registrada**: antes de manipular la variable supuestamente comprimida, el dossier debe declarar (i) la banda predictiva del modelo bajo la intervención, (ii) un umbral τ y un estadístico explícitos bajo los cuales la diferencia observada cuenta como falsación, y (iii) qué hipótesis auxiliares quedan fijadas durante el test (cláusula anti-Duhem-Quine). Si la diferencia observada cae fuera de la banda con τ violado y las auxiliares fijadas no fueron modificadas *post hoc*, la compresión ocultaba estructura relevante.

**Adición correspondiente al Dossier §3.1, componente 10** (línea 74) — sustituir:

> 10. Intervención discriminante       experimento que la falsaría

por:

> 10. Intervención discriminante       experimento que la falsaría, con banda predictiva pre-registrada (estadístico, distribución de referencia, umbral τ) y lista explícita de hipótesis auxiliares fijadas durante el test

**Adición a §3.3 (Criterio de fallo del dossier)** — añadir viñeta:

> - la intervención discriminante carece de banda predictiva pre-registrada o de τ explícito, o se modifican hipótesis auxiliares *post hoc* para absorber el resultado;

## Costo argumentativo declarado

- **Costo positivo (asumido):** la tesis se compromete a que cualquier aplicación futura del marco aporte pre-registro cuantitativo; aplicaciones publicadas previamente sin banda pre-registrada quedan bajo deuda metodológica explícita y deben re-someterse.
- **Costo de auditoría retrospectiva:** los 40 casos del corpus EDI deben revisarse uno a uno para verificar si su `case_config.json` incluye la banda y τ antes del run canónico. Hipótesis fundada (no verificada en este reporte): el motor sí lo hace (n_perm=999 y umbral p<0.05 son pre-registrados en código), pero hay que documentarlo en cada `case_config.json` con campo explícito `pre_registered_band` y `tau`.
- **Costo filosófico residual (no eliminable):** el holismo Duhem-Quine no se elimina por ningún criterio de admisión; solo se acota. Reconocerlo es honesto. La cláusula "auxiliares fijadas" reduce el margen de evasión, no lo cierra.

## Estado y firma requerida

`needs_human` — **B-T*** y **H-J***:
- **H-J (Jacob):** firma filosófica de la reescritura del criterio 2.3 y de las adiciones al Dossier §3.1 / §3.3. Decisión sobre si el ajuste va en este capítulo o se difiere a §10 (Intervención discriminante) del dossier desplegado.
- **B-T (Steven, técnica):** auditoría de los 40 `case_config.json` para verificar/añadir campos `pre_registered_band` y `tau`. Probablemente trivial donde el código ya pre-registra; declarar deuda donde no.

No edito `Tesis.md` ni `metrics.json`. No edito el capítulo 03-02 sin firma de Jacob.
