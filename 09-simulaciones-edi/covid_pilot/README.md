# Caso piloto COVID-19 — dimensión normativa institucional

Ejecución del caso piloto para la dimensión normativa propuesto en el bloque 7 de la auditoría doctoral (`05-aplicaciones/04-instituciones-mercado-y-estado.md` §7.1). Aplica el aparato EDI con ablación real a la dinámica de adopción de medidas no farmacéuticas durante la pandemia COVID-19, usando datos públicos del Oxford COVID-19 Government Response Tracker (vía OWID).

**Fuente de verdad numérica:** `09-simulaciones-edi/covid_pilot/outputs/metrics_covid_pilot.json`.

**Código:** `09-simulaciones-edi/covid_pilot/run_covid_pilot.py`.

**Datos primarios:** OWID `owid-covid-data.csv` (cache local en `data_cache/owid-covid.csv`).

**Ejecución:**

```bash
source 09-simulaciones-edi/.venv/bin/activate
python3 09-simulaciones-edi/covid_pilot/run_covid_pilot.py
```

## Diseño

- **Variable observable:** `stringency_index` (Oxford OXCGRT, escala 0-100).
- **Forcing exógeno:** `new_cases_smoothed` normalizado.
- **Sonda macro:** `institutional_inertia` (cuenca de atracción AR(1) con damping + alpha + beta forcing).
- **Modelo coupled:** `Stringency_{t+1} = damping*S_t + alpha*(target − S_t) + beta*forcing_t`.
- **Control (ablación real):** mismo modelo con `forcing = 0` (desacoplamiento exógeno).
- **EDI:** `1 − rmse_modeled / rmse_control` con permutación 999 + bootstrap 500.
- **Países evaluados:** COL, MEX, ARG, ESP, DEU, USA, BRA, CHL, PER, ITA (n=1087 cada uno, ventana 2020-2023).

## Resultados ejecutados

| País | n obs | EDI | p-value | CI 95% |
|------|------:|----:|--------:|--------|
| COL | 1087 | −0.029 | 1.000 | [−0.030, −0.028] |
| MEX | 1087 | −0.004 | 1.000 | [−0.005, −0.004] |
| ARG | 1087 | −0.005 | 1.000 | [−0.005, −0.005] |
| ESP | 1087 | −0.003 | 1.000 | [−0.003, −0.003] |
| DEU | 1087 | +0.009 | 1.000 | [+0.007, +0.011] |
| USA | 1087 | −0.004 | 1.000 | [−0.006, −0.002] |
| BRA | 1087 | −0.037 | 1.000 | [−0.041, −0.033] |
| CHL | 1087 | +0.000 | 1.000 | [−0.000, +0.000] |
| PER | 1087 | −0.001 | 0.993 | [−0.003, +0.002] |
| ITA | 1087 | +0.010 | 1.000 | [+0.008, +0.013] |

**Resumen:** 0/10 países con EDI > 0.10 y p < 0.05. EDI medio = −0.006.

## Lectura

### Hallazgo central honesto

Bajo la sonda institutional_inertia AR(1), **el forcing exógeno (casos COVID) tiene constricción nula sobre la dinámica institucional medida por stringency_index**. EDI ≈ 0 en los diez países con p = 1.0. La sonda no necesita el forcing para predecir la observada; la stringency tiene autocorrelación interna suficiente para ser modelada sin ablación significativa.

### Qué significa este resultado

Tres lecturas posibles:

1. **La sonda es insuficiente.** Una sonda AR(1) con damping + alpha + beta forcing es demasiado simple para capturar la complejidad de la respuesta institucional. La stringency está sostenida por dinámicas que esta sonda no modela: presión política, opinión pública, coordinación regional, decisiones discretas no continuas.
2. **El forcing es inadecuado.** Casos COVID por sí solos no es la perturbación correcta. La respuesta institucional puede estar acoplada a hospitalizaciones, muertes, disponibilidad de UCI, opinión pública, presión partisana — variables no incluidas en este modelo.
3. **La dimensión normativa no es directamente operacionalizable por sonda continua.** La stringency es una variable ordinal con saltos discretos (decisiones políticas) que no admite modelado por ecuación diferencial continua simple.

### Implicación para la tesis

Este resultado **confirma operativamente la cláusula del capítulo 05-04**: la dimensión normativa queda explícitamente fuera del alcance demostrativo del manuscrito y se documenta en modo programático acotado. La ejecución del caso piloto produjo evidencia empírica de que la sonda continua simple no basta. El programa futuro debe explorar:

- sondas con variables ordinales (procesos de decisión discreta);
- forcing multivariado (casos + opinión pública + factores económicos);
- modelos institucionales con histéresis y umbral (stringency cambia con eventos discretos, no continuamente);
- comparación cross-country como replicación, no como agregado.

### Coherencia con el aparato

Este es un ejemplo de **falsación honesta del aparato cuando se aplica fuera de su régimen de validez**. La sonda apropiada para institutional dynamics no es AR(1); el resultado nulo refuerza, no debilita, la posición filosófica del manuscrito: el aparato no glorifica ni rechaza arbitrariamente; **clasifica con precisión cuando la sonda es adecuada y reporta nulidad cuando no lo es**.

## Limitaciones reconocidas

1. Sonda única simplificada (AR(1) con un forcing); no se exploran sondas alternativas en este piloto.
2. Forcing univariado (solo casos); ignora hospitalizaciones, muertes, opinión pública.
3. Variable observable (stringency_index) tratada como continua aunque tiene saltos discretos.
4. No se diferencia por régimen institucional (autoritarios vs. democráticos vs. federales).
5. Ventana 2020-2023 incluye varias olas; el comportamiento heterogéneo entre olas no se modela.

## Veredicto del piloto

**Resultado:** caso piloto **EJECUTADO** con resultado **null** (EDI ≈ 0, p = 1.0).

Esto cierra la deuda del bloque 7 de la auditoría doctoral en su forma de **piloto ejecutado con resultado honesto**, no en forma de demostración positiva. La dimensión normativa permanece en modo programático acotado en el manuscrito; el aparato la trataría sólo bajo desarrollo metodológico adicional.

## Lectura cruzada

- Capítulo programático: `05-aplicaciones/04-instituciones-mercado-y-estado.md`.
- Programa documental original: `Bitacora/2026-04-28-cierre-doctoral/...` (cubre el contexto auditorial).
- Auditoría v2: bloque 7.

## Referencias

- Hale, T., Angrist, N., Goldszmidt, R., et al. (2021). "A global panel database of pandemic policies (Oxford COVID-19 Government Response Tracker)". *Nature Human Behaviour* 5, 529-538.
- Cheng, C., Barceló, J., Hartnett, A. S., Kubinec, R., y Messerschmidt, L. (2020). "COVID-19 Government Response Event Dataset (CoronaNet v.1.0)". *Nature Human Behaviour* 4, 756-768.
- Our World in Data (2025). *COVID-19 Data Explorer*. https://ourworldindata.org/covid (acceso 2026-04-28).
