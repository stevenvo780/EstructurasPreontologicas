# Pipeline V5.3 — Reporte consolidado

Ejecutado: 2026-04-28 22:44:09 UTC

## Etapas ejecutadas

| # | Etapa | Estado |
|--:|-------|--------|
| 1 | 1/9 — FETCH_MANIFEST por caso (Q1 trazabilidad) | ✅ |
| 2 | 2a/9 — SETUP_HASH inter-dominio (Q4) | ✅ |
| 3 | 2b/9 — SETUP_HASH inter-escala (Q4) | ✅ |
| 4 | 3/9 — protocolo_simulacion.md (Q3) | ✅ |
| 5 | 4/9 — Enrichment V5.2 universal (Q7) | ✅ |
| 6 | 5/9 — Sondas independientes B4 (Q5) | ✅ |
| 7 | 6/9 — Análisis de potencia B7 | ✅ |
| 8 | 7/9 — Sensibilidad a umbrales B5 | ✅ |
| 9 | 8/9 — Auditoría QES (Q1-Q7) | ✅ |

## Calificación final del corpus (QES)

| Categoría | Casos |
|-----------|------:|
| ROBUSTO (QES ≥ 0.85) | 3 |
| DEMOSTRATIVO (QES 0.70 - 0.85) | 25 |
| PROGRAMÁTICO (QES 0.55 - 0.70) | 12 |
| PILOTO (QES 0.40 - 0.55) | 0 |
| INADMISIBLE (QES < 0.40) | 0 |

## Top 10 casos por QES

| Caso | QES | Categoría |
|------|----:|-----------|
| 09_caso_finanzas | 0.939 | ROBUSTO |
| 05_caso_epidemiologia | 0.888 | ROBUSTO |
| 11_caso_movilidad | 0.851 | ROBUSTO |
| 15_caso_wikipedia | 0.847 | DEMOSTRATIVO |
| 35_ciclo_celular | 0.840 | DEMOSTRATIVO |
| 36_nfkb | 0.840 | DEMOSTRATIVO |
| 39_cefeidas_ogle | 0.840 | DEMOSTRATIVO |
| 01_caso_clima | 0.834 | DEMOSTRATIVO |
| 32_espin_orbita | 0.830 | DEMOSTRATIVO |
| 37_hrv_cardiaco | 0.830 | DEMOSTRATIVO |

## Política anti-paper-science

Ningún caso entra a afirmación demostrativa si su QES < 0.70. Casos en categoría PROGRAMÁTICO o inferior se declaran explícitamente como modo programático con criterios de elevación.

## Reproducibilidad

Pipeline reproducible bit-a-bit con:

```bash
cd 09-simulaciones-edi
python3 scripts/run_full_pipeline.py
```

## Lectura cruzada

- `09-simulaciones-edi/QES_AUDIT_REPORT.md` — auditoría detallada por caso
- `09-simulaciones-edi/CIERRE_V5_2.md` — síntesis de los ocho bloques V5.2
- `09-simulaciones-edi/HASHES_PRE_EJECUCION.json` — pre-registro inter-dominio
- `09-simulaciones-edi/corpus_multiescala/HASHES_PRE_EJECUCION_INTER_ESCALA.json` — pre-registro inter-escala
