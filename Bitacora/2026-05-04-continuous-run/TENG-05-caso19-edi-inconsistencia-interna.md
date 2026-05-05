# TENG-05 — Caso 19: inconsistencia interna en `edi` del `metrics.json`

**Fecha:** 2026-05-04
**Origen:** process-verifier engine 2026-05-05
**Archivo:** `09-simulaciones-edi/19_caso_acidificacion_oceanica/outputs/metrics.json`
**Código relevante:** `09-simulaciones-edi/common/hybrid_validator.py:1740-1944`

## (a) Verificación de la afirmación

Confirmado. La inconsistencia está en la fase **`real`** (no en `synthetic`, que es coherente):

```
phases.real.edi.value           = 0.7278020987862708
phases.real.edi.bootstrap_mean  = 0.7275240669174086
phases.real.edi.weighted_value  = -0.00011459826047070635
phases.real.edi.loe_factor      = 0.6
phases.real.edi.permutation_pvalue   = 0.49
phases.real.edi.trend_bias.detrended_edi = -0.0002
phases.real.errors.rmse_abm          = 3.346117183453772
phases.real.errors.rmse_abm_no_ode   = 3.3454782068155327
```

Invariante que el código garantiza en `hybrid_validator.py:1744`:

```python
loe_factor = config.loe / 5.0
edi_weighted = edi_val * loe_factor
```

Por tanto debe cumplirse `weighted_value / loe_factor == value`. En `real`:

- `weighted_value / loe_factor = -0.00011459826 / 0.6 = -0.000190997…`
- Cómputo desde `errors`: `1 - rmse_abm / rmse_abm_no_ode = 1 - 3.346117183/3.345478207 = -0.000190997…`

Ambas cifras coinciden hasta 12 dígitos. Es decir: `weighted_value`, `permutation_*`, `trend_bias.detrended_edi` y el bloque `errors` provienen de **una misma ejecución** cuyo EDI real es ≈ −1.9·10⁻⁴ (no significativo, p=0.49).

`edi.value = 0.7278` y `bootstrap_mean = 0.7275` son **incompatibles con el resto del archivo** y por tanto provienen de una ejecución anterior cuyas RMSEs ya no están en el archivo. El `metrics.json` está mezclado.

Para fase `synthetic` la coherencia se mantiene (`value = 4.279e-05`, `weighted_value = 2.567e-05`, `4.279e-05 * 0.6 = 2.567e-05` ✓).

## (b) Implicaciones para la tesis

1. **Afirmaciones derivadas de `edi.value=0.73` para caso 19 son inválidas.** El valor real reproducible con las RMSEs almacenadas es ≈ −0.0002 con p=0.49 → caso null, no positivo.
2. La taxonomía y las tablas que importen `edi.value` directamente desde este JSON están sesgadas. Cualquier cifra de caso 19 en prosa (Tesis.md, README, tablas 002) debe regenerarse tras la re-ejecución.
3. Esto contradice CLAUDE.md §4 — la regla "gana el JSON" presupone que el JSON es internamente coherente; aquí no lo es.

## (c) Propuesta de edición concreta

**Bloqueante: no es un edit textual.** Requiere:

1. **B-T (humano-técnico) — re-ejecutar `validate.py` caso 19 completo** con perfil canónico:
   ```bash
   cd 09-simulaciones-edi/19_caso_acidificacion_oceanica/src
   python3 validate.py
   ```
   Esto regenera `outputs/metrics.json` coherente y `outputs/report.md`.

2. **B-T (defensa contra regresión) — añadir assertion en `write_outputs()`** (o al cierre de cada fase en `hybrid_validator.py`, justo antes del dump JSON):

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

   Esto previene archivos mezclados a futuro (escritura parcial, merges manuales, etc.).

3. **Auditoría retroactiva**: ejecutar el mismo invariante sobre los 40 casos del corpus (`outputs/metrics.json` de cada uno) para detectar otros archivos mezclados. Esto es un script trivial:

   ```python
   for case in cases:
       for phase, pd in m["phases"].items():
           e = pd.get("edi", {})
           if "value" in e and "weighted_value" in e and "loe_factor" in e:
               diff = abs(e["value"]*e["loe_factor"] - e["weighted_value"])
               if diff > 1e-6: print(case, phase, diff)
   ```

## (d) Costo argumentativo declarado

- Caso 19 (acidificación oceánica) **no puede usarse como evidencia positiva** mientras el JSON esté mezclado. La cifra circulante `EDI=0.73` es probablemente artefacto histórico; la cifra reproducible con las RMSEs actuales es ≈ −0.0002, **null**.
- Si tras re-ejecutar el caso da null reproducible, el corpus pierde un caso "positivo" — se suma a los nulls 02/03/12/17/23/25/29 y, eventualmente, es resultado más honesto que un EDI=0.73 espurio.
- Si la re-ejecución da EDI≈0.73 robusto, hay que entender por qué las RMSEs almacenadas implican lo contrario; eso apunta a un bug más profundo (¿errores y EDI calculados sobre series distintas?).
- No se debe defender ninguna conclusión sobre caso 19 en prosa hasta que el JSON sea internamente coherente.

## Estado

- **needs_human / B-T**: re-ejecución de `validate.py` caso 19 (decisión y firma de Steven/Jacob; tarda horas y modifica `metrics.json` que está protegido por hooks).
- **B-T**: parche del assertion en `hybrid_validator.py` (puede prepararse como PR independiente; no toca `Tesis.md` ni `metrics.json`).
- **B-T**: script de auditoría retroactiva del invariante sobre los 40 casos (read-only, puede ejecutarse sin firma humana — propuesta de seguimiento).

RESULT: complete | TENG-05-caso19-edi-inconsistencia-interna | JSON mezclado: real.value=0.73 stale; weighted/loe=-1.9e-4 actual. needs_human re-run.
