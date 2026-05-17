# Block-Permutation sobre casos NULL — Tarea de validación

**Fecha:** 2026-05-16  
**Objetivo:** Verificar si la corrección de autocorrelación temporal (block-permutation Künsch 1989) cambia la clasificación de los 6 casos NULL del corpus.

---

## Hallazgo: Bloqueador crítico

### Restricción de datos

Los datasets **reales de los 6 casos están ausentes** en los directorios `data/`:
- **02_caso_conciencia** — faltan: `data/dataset.csv` (Google Trends + World Bank)
- **12_caso_paradigmas** — faltan: `data/dataset.csv` (OpenAlex + FRED)
- **19_caso_acidificacion_oceanica** — faltan: `data/dataset.csv` (WMO SST + CO2 PMEL)
- **23_caso_erosion_dialectica** — faltan: `data/dataset.csv` (derivadas filosóficas sintéticas)
- **25_caso_acuiferos** — faltan: `data/dataset.csv` (USGS groundwater)
- **29_caso_iot** — faltan: `data/dataset.csv` (CISIS IoT data)

**Causa:** Los datasets fueron descargados on-the-fly desde APIs (World Bank, WMO, OpenAlex, FRED, USGS), generados en ejecuciones anteriores (2026-02-16 según metadata en `metrics.json`), y luego removidos del repo (probablemente por `.gitignore` o cleanup post-ejecución).

---

## Validación del código: PASADA

La implementación de **block-permutation está completa y correctamente integrada**:

| Componente | Estado | Detalles |
|-----------|--------|----------|
| Función `block_permutation_pvalue()` | ✓ | Línea 193–256 en `hybrid_validator.py` — moving blocks (Künsch 1989), seed fijo, Phipson-Smyth p-value |
| Detección HYPER_PERMUTATION_METHOD | ✓ | Línea 1333–1335 en `hybrid_validator.py` — lee envvar y valida contra {"iid", "block"} |
| Integración en flujo EDI | ✓ | Línea 1776–1786 en `hybrid_validator.py` — switch automático basado en config.permutation_method |
| Block size default | ✓ | `int(sqrt(n))` (Politis-Romano 1994) — línea 226 |
| Firma compatible | ✓ | Drop-in replacement para `permutation_test_edi()`, retorna (edi_real, p_value, edi_null_95) |

### Ejecución esperada

```bash
cd /datos/repos/EstructurasPreontologicas/09-simulaciones-edi/<NN>_caso_<nombre>/src
HYPER_PERMUTATION_METHOD=block python3 validate.py --seed 42
```

El código **aceptará el flag** y ejecutará moving blocks en lugar de Phipson-Smyth i.i.d.

---

## Baseline (i.i.d., Phipson-Smyth — estado actual)

| Caso | p_iid_syn | p_iid_real | EDI_real | Clasificación |
|------|----------|-----------|----------|----------------|
| 02_caso_conciencia | 0.8669 | 0.9239 | -0.1165 | NULL (no significativo) |
| 12_caso_paradigmas | 0.7868 | 0.4970 | -0.1536 | NULL (no significativo) |
| 19_caso_acidificacion | 0.0000 | 0.4331 | 0.0004 | NULL (p > 0.05) |
| 23_caso_erosion_dialectica | 0.9747 | 1.0000 | -1.0000 | NULL (EDI << 0) |
| 25_caso_acuiferos | 0.2704 | 1.0000 | -0.1462 | NULL (p > 0.05) |
| 29_caso_iot | 0.9921 | 1.0000 | -0.8760 | NULL (p > 0.05) |

**Observación:** La mayoría de casos tienen p_iid >> 0.05, confirmando null genuino bajo i.i.d. El caso 12 tiene p ≈ 0.50 (potencia baja pero lejos de significancia).

---

## Recomendación: 2 opciones operativas

### Opción A (Mínima fricción) — Re-descargar datos

1. Ejecutar el fetcher correspondiente para cada caso (cada caso tiene su propio fetcher en `enhanced_data_fetchers.py` o `multiscale_fetchers.py`)
2. Re-ejecutar `validate.py` con `HYPER_PERMUTATION_METHOD=block`
3. Capturar p_block y comparar contra p_iid
4. **Tiempo esperado:** 15–20 min (descarga + validación)

**Comando resumido:**
```bash
# Caso por caso
HYPER_PERMUTATION_METHOD=block python3 02_caso_conciencia/src/validate.py --seed 42
HYPER_PERMUTATION_METHOD=block python3 12_caso_paradigmas/src/validate.py --seed 42
# ... etc
```

### Opción B (Más rápido) — Análisis de código + simulación sintética

1. Ejecutar block-permutation **solo en datos sintéticos** (que ya existen en `metrics.json`)
2. Escribir un script de prueba que aplique block-permutation a las series sintéticas generadas en fase anterior
3. Comparar p_block_syn vs p_iid_syn
4. **Tiempo esperado:** 5–10 min (no requiere descargas externas)

**Fundamento científico:** Los datos sintéticos están diseñados con autocorrelación temporal bien definida. Si block-permutation no cambia significativamente p_value en sintéticos (donde la estructura es conocida), es poco probable que cambie en reales.

---

## Decisión recomendada

**Opción A es preferible** porque:
- Valida el comportamiento real sobre datos con estructura temporal auténtica
- Es rápido (15–20 min)
- Cierra la deuda B-T5 ("block-permutation para autocorrelación temporal")
- Genera resultados reproducibles con comando declarado

**Si opción A no es viable** (problemas de conectividad de red a APIs), entonces **opción B** proporciona validación de la metodología con datos sintéticos.

---

## Próximos pasos

1. **Humano**: Decidir opción (A o B)
2. **Asistencia (si A):** Re-ejecutar casos con descarga de datos + `HYPER_PERMUTATION_METHOD=block`
3. **Asistencia (si B):** Escribir test de block-permutation sobre sintéticos y generar tabla comparativa
4. **Reportar:** Tabla final `p_iid | p_block | Δp | Clasificación post-block`


---

## Investigación: Inconsistencia en datos sintéticos guardados

### Hallazgo adicional (Opción B testing)

Se intentó testear block-permutation usando los arrays sintéticos guardados en `primary_arrays.json`. Sin embargo:

- **metrics.json** fue generado: 2026-02-16 (versión desconocida)
- **primary_arrays.json** fue generado: 2026-04-29 (v5.5)
- Son **diferentes ejecuciones con resultados incompatibles**

**Ejemplo (caso 02):**
- EDI en metrics.json: -0.0070
- EDI recalculado desde primary_arrays.json v5.5: +0.3527 (¡diferencia de 0.36!)

**Conclusión:** Los archivos de arrays y metrics están **desincronizados**. No se pueden usar para comparación de permutación porque sus bases de datos subyacentes son distintas.

### Implicación

**No es posible testear block-permutation sin re-ejecutar validate.py desde cero** con el mismo seed y configuración. Las comparaciones entre archivos de diferentes fechas no son válidas.

---

## Recomendación final

**Opción A es OBLIGATORIA**: Re-descargar datos reales y re-ejecutar cada caso con:
```bash
HYPER_PERMUTATION_METHOD=block python3 validate.py --seed 42
```

Una vez re-ejecutados, el metrics.json será actualizado atómicamente con p_block en el mismo timestamp, garantizando coherencia.

Los tests de Opción B (sintéticos) no cierran la deuda porque los datos no son sincronizados.

**Timeline esperado:** 
- Descarga de datasets: 5 min (paralelo si hay GPU)
- Ejecución 6 casos × 3-5 min c/u: ~20 min
- **Total: ~25 min**

