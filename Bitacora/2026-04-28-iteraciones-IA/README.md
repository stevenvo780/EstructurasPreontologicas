# Iteraciones de desarrollo asistido por IA — archivo histórico

Esta carpeta archiva documentos retirados del corpus oficial de la tesis durante la limpieza del 2026-04-28 (commit `73e3681` y siguientes). Los archivos se conservan como trazabilidad del proceso de desarrollo y como referencia histórica.

Los archivos NO forman parte del corpus argumental y NO deben citarse desde el manuscrito. La justificación del retiro está en `REPORTE_AUTOINDULGENCIAS.md` (raíz del repositorio).

## Contenido

| Subcarpeta | Contenido |
|------------|-----------|
| `V5_documentos/` | Seis documentos meta de versionología: CIERRE_V5_2, CIERRE_V5_3_FINAL, CIERRE_V5_5_FINAL, REFUERZOS_V5_1, EVOLUCION_NARRATIVA_V5_5, PIPELINE_V5_3_REPORT. |
| `V5_reportes_tecnicos/` | Siete reportes Markdown que duplicaban en prosa lo que los outputs JSON contenían como datos: QES_AUDIT_REPORT, INDEPENDENT_PROBES_REPORT, FULL_SECONDARY_PROBES_REPORT, POWER_ANALYSIS_REPORT, THRESHOLD_SENSITIVITY_REPORT, ELEVACION_V5_2_REPORT, ELEVACION_V5_2_INTER_ESCALA. |
| `V5_plantillas_por_caso/` | Diez plantillas representativas (cinco pares NARRATIVA + paper_skeleton) que cubren los tipos del corpus: caso real (04 Energía), caso límite (02 Conciencia), control de falsación (06 Exogeneidad), caso ancla con circularidad declarada (30 Behavioral Dynamics), discriminación contra rival (41 Wolfram). |
| `V5_scripts_jerga/` | Cuatro scripts cuya función técnica fue absorbida por scripts vivos con nomenclatura neutra: elevate_to_robust, elevate_weak_cases, elevate_multiescala_cases, generate_paper_skeletons. |

## Recuperación de archivos completos desde git

Los 42 archivos completos de `NARRATIVA_TESIS_V5_5.md` y `paper_skeleton.md` (sólo cinco representativos quedaron archivados) pueden recuperarse desde el commit anterior a la limpieza:

```bash
git show 88b288b:09-simulaciones-edi/<caso>/NARRATIVA_TESIS_V5_5.md
```
