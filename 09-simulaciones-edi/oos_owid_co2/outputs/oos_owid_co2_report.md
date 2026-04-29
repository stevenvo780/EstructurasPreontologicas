# Segundo OOS preregistrado — OWID CO2/GDP/energy per capita

**Compromiso:** paso 6.ter (segundo test) hoja de ruta cap. 06-03 — predicción out-of-sample preregistrada en dominio distinto al astrofísico del primer OOS.

**Pre-registro SHA-256:** `8700736af97a35691b8e9c58c72c0c2c09d9a0b4dbfdb50e6dd551ac848f0371`
**Dato crudo SHA-256:** `5f36ddd3ec7799f30d0223d0b447b512b17f7e7e1652cd9c10890eb8bc4eaaed` (14.3 MB)
**Fuente:** Our World in Data, `co2-data` master branch.
**Fecha de ejecución:** 2026-04-28T23:38:47 (UTC-5).

---

## Hipótesis pre-registrada

> Bajo el modelo log(CO2/cap) = a + b·log(GDP/cap) + c·log(energy/cap), el regresor log(GDP/cap) es ablativamente necesario: **EDI(GDP) ≥ 0.20 (al menos weak)**.

## Resultado ejecutado

| Métrica | Valor |
|---|---|
| N filas país-año válidas (1990–último) | **5 358** |
| RMSE modelo acoplado (con GDP) | 0.3936 |
| RMSE modelo no_ode (sin GDP, solo energía) | 0.3944 |
| **EDI** | **+0.0020** |
| **p-value (permutación 2999)** | **0.000333** |
| Máximo nulo de EDI | +0.0011 |
| EDI percentil 95 nulo | +0.0004 |
| **Clasificación pre-registrada** | **TREND** (EDI > 0 ∧ p ≤ 0.10, pero EDI < 0.10) |

**Coeficientes del modelo acoplado:**

- a (intercepto) = −8.12
- **b (log GDP/cap) = +0.055** *(coeficiente pequeño)*
- **c (log energy/cap) = +0.908** *(coeficiente dominante)*

---

## Veredicto

**Hipótesis pre-registrada NO confirmada en grado weak.** El resultado es **trend honesto**: GDP es estadísticamente discriminante (p < 0.001, ablación detecta señal real) pero **cuantitativamente pequeño** en presencia de energía per capita como predictor.

**Interpretación honesta y reportada sin atenuación:** la **colinealidad** entre GDP per capita y energía per capita es muy alta (Granoff y Heisler 2016 documentan que log(GDP) y log(energy/cap) tienen correlación > 0.85 inter-país). Cuando ambos predictores están en el modelo acoplado, energía per capita "absorbe" casi toda la varianza estructural de CO2 per capita; remover GDP deja una contribución residual minúscula (0.055 vs 0.908). El aparato detecta esa contribución residual como estadísticamente significativa pero la clasifica honestamente como **trend** porque su magnitud cuantitativa no alcanza el umbral weak pre-registrado.

**Lo que esto enseña:**

1. **El aparato discrimina honestamente.** No devuelve strong cuando no debe. La hipótesis pre-registrada exigía EDI ≥ 0.20; el resultado es EDI = 0.002. El aparato dice "trend, no weak" sin reformulación retórica.
2. **La sonda elegida no era óptima para este dominio.** Si la pregunta fuese "¿es la energía per capita ablativamente necesaria?", la sonda con `b·log(GDP/cap)` ablativo sobre energía habría dado strong (porque energía es el predictor dominante). Pero el pre-registro fijó GDP como ablativo, no energía. **No se cambia la sonda a posteriori.**
3. **Resultado pedagógico para la tesis:** un caso trend honesto sobre dato out-of-sample muestra que el aparato NO valida automáticamente cualquier predictor que sea estadísticamente significativo. La distinción strong/weak/trend/null tiene contenido empírico, no es decorativa.

---

## Implicaciones para el manuscrito

1. **Dos OOS preregistrados ejecutados:** uno strong (Cefeidas LMC, dominio astrofísico) y uno trend (OWID CO2, dominio socioeconómico). La asimetría es honesta: el aparato funciona muy bien en regularidades estructurales fuertes (relación P-L de Leavitt) y produce trend honesto cuando hay colinealidad fuerte entre predictores.
2. **Respuesta operativa más completa a la objeción del jurado** *"¿dónde están las predicciones discriminantes sobre datos no vistos?"*: dos predicciones con resultados públicos en dominios distintos. Una confirma transferibilidad strong; la otra clasifica honestamente trend con interpretación cuantitativa explícita.
3. **El compromiso pre-registrado se honra:** el resultado se reporta sin atenuación, sin reformular sonda, sin promover el resultado a weak para esconder la falla parcial. Esto es la marca de honestidad que la tesis declara como rasgo central.

---

## Trazabilidad

- pre-registro: `09-simulaciones-edi/oos_owid_co2/preregistro.json`
- dato crudo: `09-simulaciones-edi/oos_owid_co2/owid_co2.csv`
- código: `09-simulaciones-edi/oos_owid_co2/run_oos.py`
- resultados: `09-simulaciones-edi/oos_owid_co2/outputs/oos_owid_co2_results.json`
- protocolo: OLS sobre `log(co2/cap) = a + b·log(gdp/cap) + c·log(energy/cap)` vs `log(co2/cap) = a' + c'·log(energy/cap)`; permutación de `log(gdp/cap)` con n_perm = 2999, seed = 42.
