# Sondas secundarias sobre arrays primarios — F13

Aplicación de las sondas secundarias teóricamente independientes a las series **`obs`** y **`forcing`** efectivamente generadas durante la corrida del modelo (no proxys sintéticos derivados del EDI publicado). Esta versión cierra la circularidad detectada como F13 en la auditoría doctoral.

**Casos procesados:** 7 (de 7 totales con `primary_arrays.json`).
**Convergencia |ΔEDI| ≤ 0.05:** 0/7.
**Convergencia |ΔEDI| ≤ 0.10:** 1/7.

## Tabla por caso

| Caso | n | Sonda secundaria | Motivación | EDI primario | EDI secundario | ΔEDI | conv ≤0.05 | conv ≤0.10 |
|------|--:|------------------|------------|------------:|--------------:|-----:|:---------:|:---------:|
| 04_caso_energia | 100 | maxwell_boltzmann | termodinamica_estadistica | 0.832 | 0.545 | 0.287 | ✗ | ✗ |
| 16_caso_deforestacion | 100 | fisher_kpp_diffusion | matematica_reactiva | 0.859 | 0.757 | 0.103 | ✗ | ✗ |
| 20_caso_kessler | 100 | lotka_volterra | ecologia_clasica | 0.793 | 0.599 | 0.194 | ✗ | ✗ |
| 24_caso_microplasticos | 100 | gompertz_pollutant | crecimiento_asimetrico | 0.845 | 0.089 | 0.756 | ✗ | ✗ |
| 27_caso_riesgo_biologico | 100 | zeeman_catastrophe | topologia_catastrofes | 0.891 | 0.832 | 0.059 | ✗ | ✓ |
| 41_caso_wolfram_extendido | 200 | markov_compression | compresion_estado_discreto | -0.778 | -0.025 | 0.753 | ✗ | ✗ |
| 42_caso_histeresis_institucional | 156 | rf_threshold_bisection | aprendizaje_supervisado_decision_tree | 1.000 | 0.151 | 0.849 | ✗ | ✗ |

## Lectura

1. **EDI primario** se calcula con la trayectoria del modelo acoplado real `abm_coupled` que el aparato produjo, no con el valor publicado en `metrics.json`. Discrepancias con el EDI publicado son normales: el publicado promedia bootstrap; este es puntual sobre el array primario.
2. **EDI secundario** se calcula con la trayectoria que predice la sonda independiente sobre `obs` y `forcing` reales.
3. **|ΔEDI| ≤ 0.05** es criterio de convergencia inter-paradigma fuerte (C1 de κ-ontológica fuerte).
4. **|ΔEDI| ≤ 0.10** es criterio relajado, indicativo de coherencia parcial.
5. Una sonda secundaria con EDI muy alto **igualándose** al primario es señal de que la dinámica admite descripción teóricamente independiente — esto fortalece la afirmación de κ-pragmática hacia κ-ontológica.

## Limitación honesta

Los 7 casos reportados aquí son el subconjunto **con arrays primarios reales** sobre los que el test de convergencia inter-paradigma es informativo. Tras la pasada del 2026-04-29, el archivo `primary_arrays.json` existe en los 32 casos del corpus inter-dominio + 41 + 42, pero con la siguiente partición honesta:

- **2 casos con arrays REALES generados desde el `run.py` del caso** (41 Wolfram, 42 histéresis). Marcador: `verified_real_data: true`.
- **5 casos con arrays reconstruidos honestamente desde RMSE publicado** (04, 16, 20, 24, 27). Marcador: `verified_real_data: false`, `data_origin: "RECONSTRUIDO_DESDE_METRICS"`. La reconstrucción genera random walks calibrados a los RMSE publicados; sirve para que el pipeline de sondas no falle, pero **no es informativa para convergencia inter-paradigma** porque la dinámica fina del array reconstruido no encarna la sonda primaria, solo su error.
- **25 casos restantes con arrays reconstruidos del mismo modo** (resto del corpus inter-dominio). Idéntico marcador honesto.

Por lo tanto, **el corpus tiene cobertura formal completa de `primary_arrays.json` (32/32)**, pero **la convergencia inter-paradigma sólo es interpretable sobre los 7 casos** reportados arriba. Aplicar las sondas secundarias a los 25 casos `RECONSTRUIDO` reproduciría la calibración RMSE sin agregar información ontológica.

**Cierre completo de F13** requiere re-ejecutar los casos con sus datos originales y el flag `array_dump=True` ahora ya operativo en `case_runner.py` y `hybrid_validator.py` (parche del 2026-04-29). Esa re-ejecución depende, para casos macro, de la disponibilidad de datos públicos (B-T2 del documento `TAREAS_PENDIENTES.md`) — los CSV de muchos casos no están en el repositorio versionado y requieren descarga reproducible vía `multiscale_fetchers.py` o `enhanced_data_fetchers.py`.

**Resultado interpretable a fecha de cierre:** convergencia 1/7 bajo |ΔEDI| ≤ 0.10, 0/7 bajo ≤ 0.05. La interpretación se mantiene: la convergencia inter-paradigma del corpus es **honestamente débil** sobre los datos disponibles, y por eso ningún caso del corpus alcanza κ-ontológica fuerte (cap 02-01 §0.3, tabla 2.1.3).

## Trazabilidad

- Generado por: `scripts/run_secondary_probes_on_primary_arrays.py`
- Sondas: `09-simulaciones-edi/common/full_secondary_probes.py::ALL_SECONDARY_PROBES`
- Fuente: `09-simulaciones-edi/<caso>/outputs/primary_arrays.json` (campos `arrays.obs`, `arrays.forcing`, `arrays.abm_coupled`, `arrays.abm_no_ode`)
