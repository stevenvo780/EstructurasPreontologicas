# TENG-08 — C1 OR-fallback permite EDI negativo

Fecha: 2026-05-04
Contexto: Hallazgo de `process-verifier` 2026-05-05 sobre `09-simulaciones-edi/common/hybrid_validator.py:892`.

## (a) Verificación de la afirmación

**Afirmación:** `evaluate_c1` aprueba C1 si se cumple AL MENOS UNA de dos condiciones (`c1_relative OR c1_absolute`). La rama (B) `c1_absolute` solo exige `RMSE_abm < 2·obs_std AND corr_abm > 0.3`, **sin requerir que el ODE aporte información**. Por tanto un caso puede tener `c1_pass=True` con `EDI<0` (el ODE empeora la predicción).

**Verificación textual** (hybrid_validator.py:892–926):

```
913    if reduced_val is not None:
914        err_reduced = rmse(reduced_val, obs_val)
915        relative_improvement = err_reduced - err_abm
916        c1_relative = relative_improvement > 0  # cualquier mejora cuenta
...
922    # Condición (B): absoluta relajada (2× threshold, corr 0.3)
923    c1_absolute = (err_abm < 2.0 * threshold and corr_abm > 0.3)
924
925    # C1 pasa si cumple (A) o (B)
926    c1 = c1_relative or c1_absolute
```

Confirmado literal. La docstring (líneas 895–905) reconoce explícitamente la disyunción.

**Caso ejemplar — 23 erosión dialéctica fase real** (`metrics.json`):

| Métrica | Valor |
|---|---|
| `c1_convergence` | **True** |
| `c1_relative` | False (`relative_improvement=-0.237`, ODE empeora) |
| `c1_absolute` | True (`rmse_abm=0.404 < 2·0.367=0.734`, `corr_abm=0.994 > 0.3`) |
| `edi.value` | **-1.0** |
| `edi.permutation_significant` | False |
| `overall_pass` | False (rescatado por otros gates, no por EDI) |

El ABM solo replica los datos por correlación temporal; añadir el ODE *empeora* el RMSE (`rmse_abm_no_ode=0.167` vs `rmse_abm=0.404`). C1=True es **falso positivo de convergencia**: el modelo acoplado no converge mejor que el reducido — al contrario.

## Casos del corpus con `c1=True` y `EDI<0` (8 fases)

| Caso | Fase | EDI | rel_improv | corr_abm | c1_relative | c1_absolute |
|---|---|---|---|---|---|---|
| 02 conciencia | synthetic | -0.007 | -0.0014 | 0.479 | F | T |
| 02 conciencia | real | -0.116 | -0.091 | 0.437 | F | T |
| 03 contaminación | real | -0.090 | -0.011 | 0.614 | F | T |
| 09 finanzas | synthetic | -0.405 | -0.236 | 0.794 | F | T |
| 14 postverdad | synthetic | -0.014 | -0.021 | 0.860 | F | T |
| 20 Kessler | synthetic | -0.194 | -0.109 | 0.917 | F | T |
| 23 erosión dial. | real | **-1.000** | -0.237 | 0.994 | F | T |
| 25 acuíferos | real | -0.146 | **-2.858** | 0.994 | F | T |

En **todos** los casos la rama (B) absoluta se activa con `c1_relative=False` y `relative_improvement<0`. Patrón sistemático, no anomalía aislada.

## (b) Propuesta de edición

Tres salidas posibles, con costos:

**Salida 1 — C1 estricto (AND):**
```python
c1 = c1_relative and c1_absolute
```
- Costo: invalida muchos casos que actualmente cierran C1 vía ajuste absoluto cuando el reducido no es comparable (p. ej., cuando `reduced_val=None`). Requiere reauditoría completa del corpus.
- Beneficio: alinea C1 con la semántica fuerte de "convergencia ABM+ODE → datos".

**Salida 2 — Bandera separada (recomendada por process-verifier):** dejar `c1_absolute` como diagnóstico (`c1_fallback`) que NO contribuye a `overall_pass`. C1 estructural = `c1_relative` (cuando hay reducido) o `c1_absolute` solo si `reduced_val=None` documentadamente.
```python
if reduced_val is not None:
    c1 = c1_relative          # estricto: ODE debe aportar
    c1_fallback = c1_absolute # diagnóstico, no pasa C1
else:
    c1 = c1_absolute          # único disponible
    c1_fallback = None
```
- Costo: requiere actualizar el agregador `overall_pass` y la prosa de §03/§09 que cita C1=True en estos 8 casos.
- Beneficio: preserva información diagnóstica sin permitir falsos positivos.

**Salida 3 — Guardia anti-EDI-negativo:** mantener OR pero invalidar C1 si `edi_val < 0` con `permutation_significant=False`.
- Costo: acopla C1 a EDI (que es post-C1 en el pipeline); inversión de orden lógico.
- Beneficio: parche local mínimo.

**Recomendación:** Salida 2. La salida 1 es defensible pero invasiva; la 3 confunde criterios. La 2 preserva la docstring actual ("(B) absoluta relajada") como diagnóstico legítimo cuando no hay reducido, y bloquea el falso positivo cuando sí lo hay.

**Estado:** `needs_human` — la elección entre (1), (2), (3) toca semántica del protocolo C1-C5+ que está documentada en cap. 03 y citada en §09 análisis. Requiere firma de Jacob (decisión filosófica/metodológica) y posterior reauditoría del corpus (B-T*) tras el cambio.

## (c) Costo argumentativo declarado

- 8 fases (de ~80 fases del corpus, ~10%) cambiarán C1=True → C1=False bajo Salida 1 o 2. La afirmación general "el corpus pasa C1 ampliamente" debe re-cualificarse.
- En particular, el caso 23 (erosión dialéctica fase real) ya está documentado como null en el manuscrito; el cambio refuerza esa lectura, no la contradice.
- El caso 25 acuíferos fase real (`relative_improvement=-2.86`, ODE catastróficamente mal) es el más preocupante: actualmente reportado como C1=True. Bajo Salida 2 caería a C1=False y la prosa de §03 ó §05 que lo invoque debe revisarse.
- La docstring actual reconoce que el umbral previo "1·obs_std y corr>0.7" era "demasiado estricto"; relajar a 2·obs_std y 0.3 fue una decisión deliberada. Salida 2 mantiene esa relajación pero le quita poder de cierre formal.

No edito código ni `metrics.json`. No edito `Tesis.md`.

RESULT: complete | TENG-08-c1-or-fallback-permite-edi-negativo | 8 fases c1=T con EDI<0; needs_human salida 1/2/3
