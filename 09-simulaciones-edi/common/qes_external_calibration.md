# Calibración externa de QES — F17

## Problema

QES (`09-simulaciones-edi/common/quality_scorer.py`) tiene 9 componentes con pesos y umbrales elegidos por el equipo. Los "8 ROBUSTO" del corpus son artefacto de esa calibración interna; sin validación externa es métrica circular.

## Propuesta

Aplicar el scorer a un corpus externo de **5–10 estudios publicados en revistas Q1 con datos abiertos** y verificar que produce categorías razonables. La pregunta empírica es: ¿el scorer reproduce el ordenamiento de credibilidad que la comunidad científica ya estableció?

## Corpus candidato

Estudios con (a) datos primarios públicos, (b) método publicado y (c) consenso sobre su robustez. La selección debe atravesar dominios para evitar sesgo disciplinario.

### Dominios físicos

| # | Estudio | Dataset | Esperado | DOI / fuente |
|---|---------|---------|----------|--------------|
| 1 | LIGO GW150914 (primera detección onda gravitacional) | gw-openscience.org/events/GW150914/ | ROBUSTO ≥0.85 | doi:10.1103/PhysRevLett.116.061102 |
| 2 | Higgs ATLAS+CMS 2012 (Higgs boson 125 GeV) | hepdata.net | ROBUSTO ≥0.85 | doi:10.1016/j.physletb.2012.08.020 |
| 3 | EHT M87* shadow (Event Horizon Telescope) | eventhorizontelescope.org/data | DEMOSTRATIVO 0.70-0.85 | doi:10.3847/2041-8213/ab0ec7 |

### Dominios biomédicos

| # | Estudio | Dataset | Esperado | DOI |
|---|---------|---------|----------|-----|
| 4 | Hodgkin-Huxley action potential (1952, replicated continuously) | physionet | ROBUSTO ≥0.85 | doi:10.1113/jphysiol.1952.sp004764 |
| 5 | Pfizer-BioNTech COVID-19 vaccine RCT (NEJM 2020) | clinicaltrials.gov NCT04368728 | ROBUSTO ≥0.85 | doi:10.1056/NEJMoa2034577 |
| 6 | Anil Seth IIT consciousness predictions (Nat Neurosci 2022) | github IIT-toolbox | PROGRAMÁTICO 0.55-0.70 | doi:10.1038/s41583-022-00587-4 |

### Dominios sociales/económicos

| # | Estudio | Dataset | Esperado | DOI |
|---|---------|---------|----------|-----|
| 7 | Card-Krueger 1994 minimum wage (NJ vs PA fast food) | Card data archive | DEMOSTRATIVO 0.70-0.85 | doi:10.3386/w4509 |
| 8 | Reinhart-Rogoff 2010 debt-growth (with HAP corrigendum) | UMass replication | PILOTO 0.40-0.55 | (replicado y refutado) |
| 9 | Henrich WEIRD samples (2010 BBS) | meta-análisis | PROGRAMÁTICO 0.55-0.70 | doi:10.1017/S0140525X0999152X |

### Casos esperados de falsación

| # | Estudio | Dataset | Esperado | DOI |
|---|---------|---------|----------|-----|
| 10 | Bem 2011 precognition (Feeling the Future) | osf.io replications | INADMISIBLE <0.40 | doi:10.1037/a0021524 |

## Procedimiento

```
para cada estudio en corpus externo:
  1. Construir dossier de anclaje (Anexo A.3) sobre el estudio
  2. Computar EDI con los datos primarios disponibles
     (si el estudio no admite EDI directo, usar análogo cuantitativo)
  3. Aplicar quality_scorer.score() con los 9 componentes Q0-Q7
  4. Comparar categoría QES asignada vs categoría esperada por consenso
```

## Métrica de calibración

- **Concordancia categorial**: % de estudios donde QES coincide con la categoría esperada (tolerancia ±1 categoría).
- **Falsabilidad invertida**: el caso #10 (Bem 2011) **debe** salir INADMISIBLE; si sale ROBUSTO, el scorer está roto.
- **Discriminación interna**: la varianza inter-categoría debe ser > intra-categoría (ANOVA simple).

## Umbral de aceptación

- Concordancia ≥ 70% → scorer calibrado externamente.
- Concordancia 50-70% → revisión de pesos/umbrales.
- Concordancia < 50% → rediseño del scorer.

## Implementación esquemática

Implementación parcial en `09-simulaciones-edi/scripts/qes_external_validation.py` (a desarrollar). Requiere:
- Acceso programático a los 10 datasets (varios requieren registro académico).
- Adaptación del módulo EDI a estudios no-temporales (LIGO usa stacking; Higgs usa likelihood ratio; vaccines usan supervivencia Kaplan-Meier).
- Sesión de 2-3 días de trabajo focal.

## Limitación honesta

Esta calibración externa **no la he ejecutado** porque requiere descarga + adaptación caso por caso. Lo que entrego aquí es:

1. La identificación del problema (F17).
2. El corpus candidato curado.
3. El procedimiento operativo.
4. Las métricas de aceptación.

La ejecución requiere decisión técnica de Steven sobre prioridad y asignación de tiempo (estimado: 3-5 sesiones de trabajo focal).

## Trazabilidad

- Origen de la propuesta: auditoría doctoral 2026-04-28, F17 en `FALLOS_PENDIENTES.md`.
- Implementación pendiente: `09-simulaciones-edi/scripts/qes_external_validation.py`.
- Discusión: cap 03-04 §calibración del scorer.
