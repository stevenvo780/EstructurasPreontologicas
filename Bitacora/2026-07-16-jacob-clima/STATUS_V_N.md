# STATUS — Stubs runnables ejes V y N (IHO)

Fecha: 2026-07-16. Log completo de todas las corridas: `/tmp/vn-stubs.log` (host ws-personal).

## Que corre de verdad (no es maqueta)

### Eje V — Viscosidad (dependencia instrumento-fenomeno)

`09-simulaciones-edi/01_caso_clima/alt_probes/` — 3 sondas nuevas + la sonda base
(caso original), todas corriendo sobre el pipeline real (`case_runner.py` /
`hybrid_validator.py`, sin tocarlos):

| Sonda | Que varia | EDI (fase real) |
|---|---|---|
| `base_temperatura_mensual` (caso 01 original) | referencia: temperatura, mensual interpolado | +0.2581 |
| `co2_instrument` | observable = CO2 (en vez de temperatura); temp pasa a driver | +0.1833 |
| `annual_window` | mismo observable (temperatura), resolucion nativa anual (sin interpolar) | +0.4485 |
| `decadal_smoothed` | mismo observable, suavizado con media movil de 120 meses | +0.5363 |

Las 3 sondas nuevas tienen su propio `case_config.json` + `src/{data,ode,abm,validate}.py`
siguiendo el MISMO patron que `15_caso_wikipedia/alt_probes/*` y
`16_caso_deforestacion/alt_probes/*` (case_dir/alt_probes/<sonda>/src/validate.py
llama a `case_runner.run_case`). `ode.py`/`abm.py` son copia exacta del caso base
(no se toco la mecanica ABM/ODE); solo `data.py` cambia — cada uno reusa
`01_caso_clima/src/fetch_real.py` (mismo fetch OWID + cache) y solo cambia que
columna se lee como "value" (el instrumento) o aplica una transformacion de
ventana/suavizado antes de entregarsela al validador.

Runner: `01_caso_clima/alt_probes/run_probes.py` — corre las 3 sondas (subprocess,
timeout 600s), lee `outputs/metrics.json` de cada una + del caso base, y agrega:

```
edi_spread = max(edi) - min(edi) = 0.3531
V_axis     = stdev poblacional del EDI entre las 4 sondas = 0.1419
```

Emitido en `01_caso_clima/alt_probes/V_dispersion.json`.

**Lectura**: el EDI del "mismo" hiperobjeto clima se mueve entre +0.18 y +0.54
segun el instrumento con que se lo mira (CO2 vs temperatura vs distintas
ventanas temporales) — evidencia empirica directa de la viscosidad mortoniana:
"no hay vista sin sonda".

### Eje N — No-localidad (acoplamiento inter-estructura)

`09-simulaciones-edi/_coupling/` — 2 pares, cada uno con su propio `run_coupling.py`:

- `deforestacion_clima/`: 16_caso_deforestacion (% cobertura forestal, World Bank)
  -> 01_caso_clima (temperatura regional anual, mismo fetch OWID que el caso 01).
  Series superpuestas 1992-2022 (n=31).
- `acidificacion_fosforo/`: 19_caso_acidificacion_oceanica (pH oceanico) ->
  22_caso_fosforo (consumo de fertilizante, World Bank). Series superpuestas
  1990-2020 (n=31).

**Metodo (proxy honesto, documentado y etiquetado como tal en `common_coupling.py`)**:
NO se reusa `hybrid_validator.py` tal cual porque esta disenado para UN caso
(una serie + su ABM/ODE calibrado), no para dos estructuras cruzadas. En vez de
forzar el aparato de permutacion+bootstrap sobre un par para el que no fue
pensado, se mide la **reduccion de RMSE fuera de muestra** (split cronologico,
70/30) de un modelo OLS que predice B(t) desde:
  - baseline: solo B(t-1) (autorregresion)
  - acoplado: B(t-1) + A(t-1) (driver cruzado, rezagado para evitar fuga)

```
edi_coupling = (rmse_baseline - rmse_coupled) / rmse_baseline
```

Resultados reales (no simulados):

| Par | n | edi_coupling |
|---|---|---|
| deforestacion -> clima(temp regional) | 31 | +0.0046 |
| acidificacion -> fosforo | 31 | -0.0024 |

`N_axis` = media de los edi_coupling = **+0.0011**. Emitido en `_coupling/N_coupling.json`.

Runner agregador: `_coupling/run_pairs.py` (corre ambos `run_coupling.py` via
subprocess, agrega, escribe `N_coupling.json`).

**Lectura honesta**: con este proxy simple (AR1 lineal + 1 driver rezagado, n=31
anual) el acoplamiento medido es debil/nulo en ambos pares — no hay evidencia
fuerte de no-localidad con esta implementacion minima. Esto es un resultado
real, no un bug: el proxy es deliberadamente simple (para ser honesto sobre
sus limites, ver "Que queda como programa" abajo) y candidatos mas fuertes
(mas lags, series no lineales, mas pares) podrian mover el numero.

## Integracion en iho.py

`Bitacora/2026-07-16-jacob-clima/iho.py` ahora lee, si existen,
`01_caso_clima/alt_probes/V_dispersion.json` y `_coupling/N_coupling.json`, y
completa V y N en el perfil (antes decian "PENDIENTE"). Confirmado corriendo
`python3 iho.py` desde `09-simulaciones-edi/` — salida real:

```
PERFIL IHO (vector, NO colapsar a escalar):
  P Fasing/Retiro   = +0.180
  I Interobjetiv.   = 0.67
  T Ondulacion~     = 87.5 meses (approx, mediana tau ODE)
  V Viscosidad      = 0.1419  (stdev EDI entre 4 sondas, spread=0.3531)
  N No-localidad    = +0.0011  (media edi_coupling de 2 pares, proxy RMSE OLS AR1)
```

Si `V_dispersion.json` o `N_coupling.json` no existen (p.ej. en un checkout
limpio antes de correr los runners), `iho.py` sigue imprimiendo "PENDIENTE"
para ese eje en vez de romperse — degrada con gracia.

## Que queda como programa (honesto, no fingido)

1. **N — proxy simple**: el modelo de acoplamiento es OLS lineal con 1 lag.
   No captura no-linealidades, no prueba mas de 1 lag, y n=31 anual es chico
   para un split 70/30 confiable (n_test=9). Un programa mas fuerte:
   bootstrap del edi_coupling para banda de confianza, probar 2-3 lags,
   agregar 1-2 pares mas (p.ej. urbanizacion->salinizacion) para que
   `N_axis` sea un promedio mas robusto que 2 puntos.
2. **V — solo 1 fenomeno cubierto (clima)**: el roadmap del IHO habla de
   viscosidad como propiedad general del aparato; aca solo se instrumento
   el sub-corpus clima. Extender `alt_probes/run_probes.py` a otros casos
   (ej. wikipedia, deforestacion, que YA tienen alt_probes de OTRO tipo —
   variacion de modelo ODE, no de instrumento) requeriria una sonda
   "instrumento" nueva ahi tambien si se quiere V por caso, no solo V-clima.
3. **tsi/ohc declarados en case_config.json pero no poblados**: el dataset
   OWID real solo trae co2 + temperatura; los otros dos drivers declarados en
   `01_caso_clima/case_config.json` (`tsi`, `ohc`) nunca tuvieron datos reales
   detras (ya asi en el caso base, no se toco). Las sondas V usan lo que
   SI existe (co2, temp, ventana/suavizado) en vez de inventar tsi/ohc
   sinteticos, para no mezclar "instrumento real distinto" con "dato inventado".

## Reproducir

```bash
ssh ws-personal
cd /workspace/EstructurasPreontologicas/09-simulaciones-edi

# Eje V: corre las 3 sondas + agrega dispersion
cd 01_caso_clima/alt_probes && python3 run_probes.py && cd ../..

# Eje N: corre los 2 pares + agrega acoplamiento
cd _coupling && python3 run_pairs.py && cd ..

# IHO completo (P, I, T, V, N)
python3 ../Bitacora/2026-07-16-jacob-clima/iho.py
```

Cada sonda/par tambien corre sola, p.ej.:
```bash
cd 01_caso_clima/alt_probes/annual_window && python3 src/validate.py
cd _coupling/deforestacion_clima && python3 run_coupling.py
```

## Commit

NO se hizo commit (working tree queda para revision de Stev). Archivos nuevos:
- `09-simulaciones-edi/01_caso_clima/alt_probes/{co2_instrument,annual_window,decadal_smoothed}/` (case_config.json + src/{data,ode,abm,validate}.py + outputs/metrics.json de cada corrida)
- `09-simulaciones-edi/01_caso_clima/alt_probes/run_probes.py` + `V_dispersion.json`
- `09-simulaciones-edi/_coupling/` completo (common_coupling.py, 2 pares, run_pairs.py, N_coupling.json)
- `Bitacora/2026-07-16-jacob-clima/iho.py` modificado (lee V_dispersion.json/N_coupling.json)
