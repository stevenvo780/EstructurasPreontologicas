# Programa de topologías heterogéneas para Nivel 5

## Función

Documento técnico-formal del programa de elevación a Nivel 5 mediante topologías heterogéneas (scale-free, small-world) anunciado en `06-cierre/01-conclusion-demostrativa.md` y `09-simulaciones-edi/common/topology_generator.py`. Cierra el hallazgo 6 de la auditoría exhaustiva del 2026-04-28.

## Motivación

El Nivel 5 del paisaje de emergencia se define por tres condiciones simultáneas (cap 03-04 §"Niveles del paisaje"):

1. convergencia bajo **múltiples sondas** independientes;
2. **LoE = 5** (datos físicos directos de alta calidad);
3. **frontera espacial nítida** entre regiones del sistema.

La condición (3) requiere **topologías heterogéneas** (no la grilla 50×50 homogénea por defecto). El módulo `09-simulaciones-edi/common/topology_generator.py` implementa generadores scale-free y small-world; este programa formaliza su aplicación a casos candidatos.

## Casos candidatos

Selección por criterio de relevancia para frontera espacial:

| # | Caso | Razón | CR canónico esperado |
|---|------|-------|---------------------|
| 16 | Deforestación | frontera agrícola/forestal nítida en datos satelitales | > 1.5 |
| 18 | Urbanización | frontera urbano/rural nítida en datasets World Bank + remote sensing | > 1.5 |
| 22 | Fósforo | concentración heterogénea en cuencas hidrográficas | > 1.2 |
| 21 | Salinización | parche-mosaico en datos de irrigación | > 1.2 |
| 11 | Movilidad aérea | red scale-free de aeropuertos (hubs) | > 2.0 |

**Umbral CR > 2.0 para Nivel 5:** la condición de frontera nítida exige ratio de cohesión Symploké ≥ 2.0, indicando estructura jerárquica con núcleos densos y periferia.

## Procedimiento ejecutivo

### Paso 1. Adaptación del ABM a topología heterogénea

`abm_core.py` actualmente opera sobre grilla regular. Adaptación requerida:

```python
# Pseudo-código de la modificación
from topology_generator import generate_scale_free, generate_small_world

if cfg.get("topology") == "scale_free":
    network = generate_scale_free(n_agents=200, gamma=2.5)
elif cfg.get("topology") == "small_world":
    network = generate_small_world(n_agents=200, k=4, p_rewire=0.1)
else:
    network = grid_50x50()  # default
```

### Paso 2. Re-ejecución de los 5 casos candidatos

Para cada caso candidato, ejecutar bajo perfil canónico (n_perm=999, n_boot=500):
- topología grilla (línea base existente);
- topología scale-free (γ = 2.5);
- topología small-world (k=4, p=0.1).

### Paso 3. Comparación cross-topología

Reportar tabla:
- EDI por topología;
- CR Symploké por topología;
- ¿se cumple condición (3) Nivel 5? (CR > 2.0 + frontera identificable).

### Paso 4. Combinación con multi-sonda

Si algún caso pasa Paso 3 (CR > 2.0 con topología heterogénea), aplicar el aparato multi-sonda ya implementado (`09-simulaciones-edi/common/multi_sonda.py`) para satisfacer la condición (1) del Nivel 5.

### Paso 5. Verificación LoE = 5

Confirmar que el caso elevado tiene datos LoE = 5 (físicos directos, > 30 años de cobertura). Casos candidatos satisfacen LoE 4-5 según `case_config.json`.

### Paso 6. Reporte de elevación a Nivel 5

Si pasos 3-5 se satisfacen para algún caso:
- producir dossier de elevación en `09-simulaciones-edi/<caso>/dossier_nivel5.md`;
- actualizar `Anexos/A8-tablas-crudas-corpus.md` con clasificación Nivel 5;
- actualizar `06-cierre/01-conclusion-demostrativa.md`.

## Cronograma estimado

| Mes | Hito |
|-----|------|
| 1 | Adaptación ABM a topologías heterogéneas (Paso 1) |
| 2 | Re-ejecución cross-topología en 5 casos (Paso 2) |
| 3 | Análisis comparativo CR (Paso 3) + selección de candidato Nivel 5 |
| 4–5 | Aplicación multi-sonda + verificación LoE = 5 (Pasos 4-5) |
| 6 | Reporte de elevación o reporte negativo (Paso 6) |

**Total programa:** 6 meses post-defensa.

## Hipótesis a verificar

| H | Enunciado | Verificación |
|---|-----------|--------------|
| HT.1 | Topología scale-free aumenta CR en al menos 2 de 5 casos | Paso 3 |
| HT.2 | Al menos 1 caso alcanza CR > 2.0 con topología heterogénea | Paso 3 |
| HT.3 | El caso con CR > 2.0 satisface las 3 condiciones Nivel 5 | Pasos 4-5 |
| HT.4 | Si HT.1-HT.3 fallan, Nivel 5 queda como horizonte programático verificado | reporte negativo |

## Resultado adverso documentado

Si ningún caso alcanza Nivel 5 tras el programa, esto **no debilita** la tesis: confirma que el corpus EDI actual está **honestamente clasificado hasta Nivel 4**, y el Nivel 5 permanece como horizonte programático verificado por ejecución, no como promesa abstracta. Esto sería **falsación honesta del Nivel 5 en su régimen propuesto**, alineada con la posición filosófica del manuscrito (cap 03-04 cláusula explícita Nivel 5 = futuro).

## Limitación declarada

- el programa requiere adaptación del aparato existente, no extensión radical;
- la condición (3) "frontera espacial nítida" es la más exigente y puede no satisfacerse en ningún caso del corpus actual;
- en ese caso, el Nivel 5 quedaría documentado como condición teórica falsable pero no instanciada.

## Lectura cruzada

- Definición de Nivel 5: `03-formalizacion/04-operacionalizacion-de-kappa.md` §"Niveles del paisaje".
- Generador de topologías existente: `09-simulaciones-edi/common/topology_generator.py`.
- Hoja de ruta general: `06-cierre/03-hoja-de-ruta-para-tesis-final.md`.
- Auditoría exhaustiva: hallazgo 6.
