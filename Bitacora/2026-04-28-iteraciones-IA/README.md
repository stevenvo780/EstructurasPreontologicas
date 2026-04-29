# Iteraciones de desarrollo asistido por IA — archivo histórico

Esta carpeta archiva los documentos generados durante el desarrollo
asistido por IA (Claude Opus 4.7) que fueron retirados del cuerpo
oficial de la tesis en la limpieza del 2026-04-28 (commit `73e3681`).

**Política:** estos archivos NO forman parte del corpus argumental de la
tesis y NO deben citarse desde el manuscrito. Se conservan únicamente
como trazabilidad del proceso de desarrollo y como referencia histórica
para futuras iteraciones del proyecto.

El motivo del retiro está documentado en `REPORTE_AUTOINDULGENCIAS.md`
(raíz del repositorio): los documentos exhibían patrones de
auto-indulgencia inducidos por la generación automática (versionología,
numeración celebratoria, categorías inventadas, frases manieristas,
plantillas spam). El **trabajo técnico subyacente** descrito en estos
documentos sí permanece en el repositorio: módulos en
`09-simulaciones-edi/common/`, scripts en `09-simulaciones-edi/scripts/`,
outputs JSON canónicos por caso, suite ST de validación lógica formal.
Lo que se archivó aquí es la **narrativa**, no la implementación.

---

## Contenido

### `V5_documentos/`

Documentos meta sobre la "evolución de versiones" del aparato. Cada
uno se autodefinía como cierre o resumen ejecutivo de un nivel de
maduración del proyecto.

| Archivo | Función original | Razón del retiro |
|---------|------------------|------------------|
| `CIERRE_V5_2.md` | Síntesis de los ocho bloques científicos B1-B7 | Versionología; dos archivos posteriores se autodefinen como cierre |
| `CIERRE_V5_3_FINAL.md` | "Cierre final" del sistema QES anti-paper-science | Marcador "FINAL" inválido (seguido por V5.4 y V5.5) |
| `CIERRE_V5_5_FINAL.md` | "Cierre final" tras la introducción de los casos 41-42 | Idem |
| `REFUERZOS_V5_1.md` | Documentación operativa de los cinco bloques V5.1 | Información técnica ya disponible en `common/*.py` con docstrings |
| `EVOLUCION_NARRATIVA_V5_5.md` | Evolución conceptual de hiperobjetos a estructuras pre-ontológicas | Reformulación retórica del trabajo histórico ya documentado en cap 02-01 |
| `PIPELINE_V5_3_REPORT.md` | Reporte numerado de las nueve etapas del pipeline | Dato derivable del propio script `run_full_pipeline.py` |

### `V5_reportes_tecnicos/`

Reportes en lenguaje natural que duplicaban en prosa los datos ya
disponibles en outputs JSON. Cada uno se mantiene en versión Markdown
aquí; los archivos JSON correspondientes permanecen vivos en
`09-simulaciones-edi/` como fuente de verdad.

| Archivo | Datos JSON correspondientes (vivos) |
|---------|-------------------------------------|
| `QES_AUDIT_REPORT.md` | `09-simulaciones-edi/QES_AUDIT_REPORT.json` (regenerable con `scripts/audit_corpus_quality.py`) |
| `INDEPENDENT_PROBES_REPORT.md` | `09-simulaciones-edi/INDEPENDENT_PROBES_REPORT.json` |
| `FULL_SECONDARY_PROBES_REPORT.md` | `09-simulaciones-edi/FULL_SECONDARY_PROBES_REPORT.json` |
| `POWER_ANALYSIS_REPORT.md` | `09-simulaciones-edi/POWER_ANALYSIS_REPORT.json` |
| `THRESHOLD_SENSITIVITY_REPORT.md` | `09-simulaciones-edi/THRESHOLD_SENSITIVITY_REPORT.json` |
| `ELEVACION_V5_2_REPORT.md` | (corpus inter-dominio: reclasificaciones bajo régimen calibrado) |
| `ELEVACION_V5_2_INTER_ESCALA.md` | (corpus inter-escala: análogo) |

### `V5_plantillas_por_caso/`

Ejemplos representativos de las plantillas que se generaban por caso
(80–85 % contenido idéntico, 15–20 % campos inyectados). Se conservan
cinco pares (`NARRATIVA` y `paper_skeleton`) que cubren los tipos
representativos: caso real con datos públicos (04 Energía), caso
límite del aparato (02 Conciencia), control de falsación (06
Exogeneidad), caso ancla con circularidad declarada (30 Behavioral
Dynamics), caso de discriminación contra rival (41 Wolfram extendido).

Los 42 archivos completos de cada plantilla pueden recuperarse desde
git en el commit `88b288b` (anterior a la limpieza `73e3681`).

| Caso | Tipo |
|------|------|
| 04_caso_energia | Caso real con datos públicos OPSD |
| 02_caso_conciencia | Caso límite (ausencia de observable fenoménico cuantificable) |
| 06_caso_falsacion_exogeneidad | Control de falsación (debe ser rechazado por diseño) |
| 30_caso_behavioral_dynamics | Caso ancla canónico con circularidad declarada |
| 41_caso_wolfram_extendido | Discriminación contra rival (Wolfram) |

### `V5_scripts_jerga/`

Scripts cuya función técnica era genuina pero cuya nomenclatura usaba
"elevación V5.X" y categorías ROBUSTO inventadas. La función operativa
(reclasificación bajo régimen calibrado, generación de paneles
multi-unidad) está absorbida por los scripts vivos en
`09-simulaciones-edi/scripts/` con nomenclatura técnica neutra.

| Archivo | Función | Reemplazo en scripts vivos |
|---------|---------|----------------------------|
| `elevate_to_robust.py` | Subía Q1, Q2, Q4, Q6 sistemáticamente con paneles | Funcionalidad absorbida por `enrich_all_cases.py` y los `extend_*.py` específicos |
| `elevate_weak_cases.py` | Reclasificaba 14 casos del corpus inter-dominio | Idem |
| `elevate_multiescala_cases.py` | Análogo para el corpus inter-escala | Idem |
| `generate_paper_skeletons.py` | Generaba 42 plantillas IMRaD | Eliminado; las plantillas no aportaban contenido específico |

---

## Cómo recuperar archivos completos

Si en el futuro se necesita uno de los 42 archivos completos de
`NARRATIVA_TESIS_V5_5.md` o `paper_skeleton.md`:

```bash
# Listar archivos del commit anterior a la limpieza
git show 88b288b --stat

# Recuperar archivo específico
git show 88b288b:09-simulaciones-edi/<caso>/NARRATIVA_TESIS_V5_5.md > /tmp/recuperado.md
```

---

## Lectura conjunta

Esta carpeta debe leerse junto con:

- `REPORTE_AUTOINDULGENCIAS.md` (raíz del repositorio): cataloga los
  ocho patrones de auto-indulgencia inducidos por la generación
  automática, con la acción correctiva aplicada en cada caso.
- `Bitacora/2026-04-28-cierre-pendientes/` y subdirectorios paralelos:
  documentación del proceso iterativo del proyecto (auditorías,
  programas de elevación, pre-registro honesto).

---

## Compromiso a futuro

Las próximas iteraciones del proyecto evitan los siguientes patrones:

1. Versiones intermedias documentadas como archivos meta (en su lugar:
   git log).
2. Categorías ad-hoc inventadas para forzar uniformidad métrica.
3. Numeración celebratoria como totem de completud.
4. Plantillas con alto porcentaje de contenido idéntico por instancia.
5. Frases auto-elogiosas que sustituyen argumentación.
6. Marcadores de versión como sustituto retórico del método.
7. Documentos meta que duplican en prosa lo que los datos ya contienen.
8. Sufijo "final" en nombres de archivo hasta que efectivamente lo sean.

Estos patrones quedan archivados aquí como evidencia histórica del
proceso de desarrollo, no como modelo a seguir.
