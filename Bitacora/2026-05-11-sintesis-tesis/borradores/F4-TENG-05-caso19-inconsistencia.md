---
borrador: IA
requires: H-J* + B-T (re-ejecutar validate.py caso 19) + B-T (assertion en write_outputs)
propuesta_fecha: 2026-05-11
destino: 04-debates/05-limitaciones-declaradas-consolidacion.md + 06-cierre/03-hoja-de-ruta-para-tesis-final.md
hallazgo: Bitacora/2026-05-04-continuous-run/TENG-05-caso19-edi-inconsistencia-interna.md
tipo: deuda_critica + tarea_B-T_re-ejecucion + tarea_B-T_assertion + auditoria_retroactiva
---

## Diagnóstico

`09-simulaciones-edi/19_caso_acidificacion_oceanica/outputs/metrics.json`, fase **real**, presenta **inconsistencia interna**: `edi.value = 0.7278` es incompatible con sus propios `errors` (que dan `(rmse_no_ode − rmse_abm)/rmse_no_ode = -0.000191`) y con `weighted_value = -0.000115`. El invariante que garantiza el código (`hybrid_validator.py:1744`: `edi_weighted = edi_val * loe_factor`) implica `weighted/loe = value`. En este JSON, `weighted/loe = -0.000191 ≈ rmse-derived`, mientras `value = 0.7278` proviene de **una ejecución distinta** cuyas RMSEs ya no están en el archivo. El metrics.json está **mezclado**. La fase synthetic mantiene coherencia (`value, weighted, errors` concuerdan), por lo que el bug afecta exclusivamente a `phases.real`. Caso 19 figura en `05-aplicaciones/07-mapa-aplicaciones-corpus.md:140` como "Trend Nivel 1*" — promoción ilegítima (cf. F4-F05-10) basada en el `value` stale.

## Verificación

- Lectura directa de `metrics.json`:
  - `phases.real.edi.value = 0.7278020987862708`
  - `phases.real.edi.weighted_value = -0.00011459826047070635`
  - `phases.real.edi.loe_factor = 0.6`
  - `phases.real.errors.rmse_abm = 3.346117183453772`
  - `phases.real.errors.rmse_abm_no_ode = 3.3454782068155327`
- Invariante violado: `weighted/loe = -0.00011/0.6 = -0.0001909... ≠ 0.7278`.
- `(rmse_no_ode − rmse_abm)/rmse_no_ode = (3.34548 − 3.34612)/3.34548 = -0.000191`, coincidente hasta 12 dígitos con `weighted/loe`.
- Coherencia hash MD5 actual = bug se reproduce idéntico bit-a-bit (cf. F4-TENG-12 sobre hash que no detecta inconsistencia interna).

## Texto propuesto (voz autoral filosófica de Jacob)

**Insertar en `04-debates/05-limitaciones-declaradas-consolidacion.md` y/o `06-cierre/03-hoja-de-ruta-para-tesis-final.md` como deuda crítica priorizada:**

> **Deuda crítica fechada: caso 19 metrics.json mezclado.** El archivo `09-simulaciones-edi/19_caso_acidificacion_oceanica/outputs/metrics.json`, fase `real`, presenta inconsistencia interna entre `edi.value = 0.7278` y los campos derivados de `errors` (que dan `(rmse_no_ode − rmse_abm)/rmse_no_ode = -0.000191`), incompatibles bajo el invariante `weighted_value = value * loe_factor` que `hybrid_validator.py:1744` garantiza. La inconsistencia indica un JSON mezclado de dos ejecuciones distintas. Toda afirmación de prosa o tabla que cite `EDI = 0.73` para caso 19 está **inválida** hasta la re-ejecución del caso con `validate.py` bajo perfil canónico y la regeneración íntegra del archivo.
>
> Esto contradice operativamente CLAUDE.md §4 ("gana el JSON"): la regla presupone que el JSON sea internamente coherente, y aquí no lo es. La tesis declara la deuda y suspende cualquier reclamo sobre caso 19 hasta la re-ejecución. El valor reproducible con las RMSEs almacenadas es ≈ −0.0002 con `p = 0.49`; bajo esa cifra, caso 19 es **null** (no Trend Nivel 1\*), coherente con la reclasificación propuesta por F4-F05-10.

## Acciones técnicas derivadas (B-T)

1. **B-T: re-ejecutar caso 19** con perfil canónico:
   ```bash
   cd 09-simulaciones-edi/19_caso_acidificacion_oceanica/src
   python3 validate.py
   ```
   Esto regenera `outputs/metrics.json` coherente.

2. **B-T: añadir assertion en `write_outputs()`** de `hybrid_validator.py`, justo antes del dump JSON de cada fase:
   ```python
   # Invariante: edi.weighted_value == edi.value * edi.loe_factor
   _v = phase_dict["edi"]["value"]
   _w = phase_dict["edi"]["weighted_value"]
   _l = phase_dict["edi"]["loe_factor"]
   assert abs(_v * _l - _w) < 1e-6, (
       f"EDI inconsistency in {phase_name}: value={_v}, "
       f"weighted={_w}, loe={_l}, expected weighted={_v*_l}"
   )
   ```
   Esto previene archivos mezclados a futuro.

3. **B-T: auditoría retroactiva** del invariante sobre los 40 casos del corpus + 10 casos del inter-escala. Script trivial (read-only) que itera y reporta cualquier violación:
   ```python
   for case in cases:
       for phase, pd in m["phases"].items():
           e = pd.get("edi", {})
           if "value" in e and "weighted_value" in e and "loe_factor" in e:
               diff = abs(e["value"] * e["loe_factor"] - e["weighted_value"])
               if diff > 1e-6: print(case, phase, diff)
   ```

4. **B-T cruza F4-TENG-12:** crear `verify_internal_consistency.py` con los tres invariantes (`value == weighted/loe`, `value == (rmse_no_ode−rmse_abm)/rmse_no_ode`, `ci_lo ≤ value ≤ ci_hi`).

## Costo argumentativo declarado

- Caso 19 no puede usarse como evidencia positiva mientras el JSON esté mezclado. La cifra circulante `EDI = 0.73` es artefacto histórico; la cifra reproducible con las RMSEs actuales es ≈ −0.0002, null.
- Si tras re-ejecutar el caso da null reproducible: el corpus pierde un caso "positivo" y suma al bloque de nulls; resultado más honesto que un EDI = 0.73 espurio.
- Si la re-ejecución da `EDI ≈ 0.73` robusto: hay que entender por qué las RMSEs almacenadas implican lo contrario; apunta a bug más profundo (¿errores y EDI calculados sobre series distintas?). Esto sería un fallo más serio que el actual y obliga a auditoría exhaustiva del pipeline.
- No se debe defender ninguna conclusión sobre caso 19 en prosa hasta que el JSON sea internamente coherente.
