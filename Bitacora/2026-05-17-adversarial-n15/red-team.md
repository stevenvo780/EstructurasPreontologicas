# Adversarial iter 8 — corrección filosófica forking paths

**Fecha:** 2026-05-17
**Pasada:** adversarial iter 8 (n=15) sobre el aparato BORRADOR-IA bidireccional consolidado iter 7.

## Hallazgo crítico

La frase "la calibración bidireccional refuta la objeción Ioannidis" (5 lugares BORRADOR-IA del manuscrito) es **filosóficamente incorrecta**.

**Razón (Gelman & Loken 2014, p. 460):**

> "data analysis whose details are highly contingent on data, invalidating published p-values"

La objeción *forking paths* describe los grados de libertad analíticos que el investigador ejerce — incluso sin malicia — al elegir sondas, ventanas, criterios de inclusión y umbrales después de ver los datos. Es **ruido direccionalmente neutro** que infla varianza en ambas direcciones. Una calibración bidireccional (downgrades + upgrades + reclasificaciones + confirmaciones) **debilita la hipótesis de sesgo unidireccional simple** (cherry-picking pro-tesis), pero **no controla los grados de libertad** ni demuestra que las elecciones analíticas estén fijadas con anterioridad a ver los datos.

## Reformulación aplicada en los 5 lugares BORRADOR-IA

1. `06-cierre/01-conclusion-demostrativa.md` §1 blockquote.
2. `00-proyecto/05-resumen-y-abstract.md` (ES + EN).
3. `06-cierre/02-guia-de-defensa.md` §3 P7-bis.
4. `Correspondencia_Ricardo/06-resumen-ejecutivo-para-ricardo.md` §4-bis.
5. `Correspondencia_Ricardo/05-borrador-respuesta-al-profesor.md` (versión larga).

La nueva formulación:

- Sustituye "modula la lectura Ioannidis Corolario 4 (calibración bidireccional)" por "**debilita la hipótesis de sesgo unidireccional simple** pero **NO neutraliza la objeción forking paths**".
- Cita verbatim paginada de Gelman & Loken 2014, p. 460 (PDF en `07-bibliografia/Gelman Loken - Statistical Crisis in Science (2014).pdf`).
- Declara explícitamente el **sesgo de cobertura instrumental** de la muestra B-T2 (seleccionada por disponibilidad de fetcher público, no por muestreo aleatorio ni estratificado).
- Apunta al **pre-registro de las próximas 5 ejecuciones B-T2** como bloqueo operativo del forking path para casos futuros, con la plantilla `09-simulaciones-edi/PRE_REGISTRO_TEMPLATE.md` ya aplicada a casos 10 (Justicia) y 15 (Wikipedia).
- Reclasifica los 14 casos B-T2 ya ejecutados como evidencia *post-hoc* honesta con sesgo de cobertura declarado, no como falsación de Ioannidis Corolario 4.

## Estado de cobertura B-T2

Pre-registros firmados antes de re-ejecución (2026-05-17):

- `09-simulaciones-edi/10_caso_justicia/docs/PRE_REGISTRO.md` (H0: Weak; sesgo declarado: corrida previa observada).
- `09-simulaciones-edi/15_caso_wikipedia/docs/PRE_REGISTRO.md` (H0: Weak; sesgo declarado: corrida previa observada).

Resultados pos-pre-registro: **2 discrepancias honestas vs predicción Weak**.

- Caso 10 Justicia: `edi_mean ∈ [0.045, 0.058]` → Trend/Null (vs predicción Weak).
- Caso 15 Wikipedia: `edi_mean ∈ [-0.070, -0.004]` → Null/falsificación local (vs predicción Weak).

Ambas discrepancias quedan declaradas en `outputs/report.md` de los respectivos casos como contraevidencia, conforme al compromiso §6 de cada pre-registro.

## Verificación pasada

- `python3 TesisFinal/build.py` → OK (791,616 bytes, 9,167 líneas).
- `python3 harness/cli.py verify --all` → 8/8 pass (decorative_citations warn pre-existente, no relacionado).

## Próximos pre-registros B-T2 pendientes

Para completar el bloqueo del forking path en las próximas 5 ejecuciones:

1. Pre-registrar y re-ejecutar 3 casos B-T2 adicionales antes de defensa, sin observar resultados.
2. Reportar honestamente discrepancias vs predicción como contraevidencia, no como exploración post-hoc.
3. Auditoría externa hostil (deuda bloqueante L20) sobre la cobertura instrumental como sesgo de selección.

## Deuda residual abierta

- Sesgo de cobertura instrumental B-T2 sigue declarado pero **no resuelto** (requiere muestreo aleatorio o estratificado sobre dominios sin fetcher público).
- Pre-registro de los próximos 5 casos B-T2 **pendiente de firma autoral**.
- Reformulación de los 5 bloques BORRADOR-IA queda como advertencia hasta firma Jacob H-J5/H-J6/H-J7.
