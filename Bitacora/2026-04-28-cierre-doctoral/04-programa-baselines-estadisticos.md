# Programa de comparación con baselines estadísticos puros

## Función

Documento que especifica el plan de comparación del aparato EDI con **modelos puramente estadísticos** (ARIMA, VAR, modelos bayesianos no estructurados) sobre los casos strong y los controles de falsación. La existencia de este programa responde al bloque 6 de la auditoría doctoral interna y a la objeción anticipable: *"si un ARIMA simple sobre las mismas series predice tan bien como tu ABM+ODE con `overall_pass=True`, ¿qué añade tu marco?"*.

## 1. Motivación y aclaración previa

El propósito del aparato EDI no es **predicción óptima** sino **discriminación de cierre operativo bajo intervención ablativa**. Un ARIMA puede predecir bien sin que ello signifique nada sobre el cierre operativo del fenómeno: ARIMA captura autocorrelación temporal, no estructura causal acoplada. Pero el comité doctoral merece una **prueba comparativa explícita** que muestre que:

- la diferencia entre ABM+ODE (con `overall_pass`) y un ARIMA es **medible** y **defendible**;
- los casos null del corpus deberían ser predichos comparativamente bien por ARIMA y por el aparato (porque no hay estructura adicional que el aparato detecte);
- los casos strong deberían mostrar **ventaja del aparato** en alguna dimensión (no necesariamente RMSE absoluto, sino calidad de la discriminación).

## 2. Casos seleccionados para baseline

| Categoría | Casos | Cuenta |
|-----------|-------|-------:|
| Strong (`overall_pass = True`) | 04 Energía, 16 Deforestación, 20 Kessler, 27 Riesgo Bio | 4 |
| Strong sin gate | 24 Microplásticos | 1 |
| Controles de falsación | 06 Exogeneidad, 07 No-estacionariedad, 08 Observabilidad | 3 |

Total: 8 casos.

## 3. Modelos baseline propuestos

### 3.1. ARIMA(p, d, q)

**Naturaleza:** autoregresivo integrado de medias móviles univariado.

**Selección de orden:** AIC + BIC sobre la serie objetivo del caso. Búsqueda en cuadrícula `p ∈ {0..5}, d ∈ {0..2}, q ∈ {0..5}`.

**Implementación:** `statsmodels.tsa.arima.model.ARIMA`.

**Métrica:** RMSE de validación en la misma ventana val_steps que el aparato EDI.

### 3.2. VAR(p)

**Naturaleza:** vector autoregresivo multivariado, captura interacciones lineales entre múltiples series.

**Selección de orden:** AIC sobre `p ∈ {1..5}`.

**Implementación:** `statsmodels.tsa.api.VAR`.

**Métrica:** RMSE multivariado en val_steps.

### 3.3. Random Walk (referencia trivial)

**Naturaleza:** modelo nulo predictivo (próximo valor = valor actual + ruido).

**Propósito:** establecer cota inferior de habilidad predictiva. Cualquier modelo no trivial debe superar al random walk.

### 3.4. Modelo bayesiano no estructurado (opcional)

**Naturaleza:** Gaussian process regression con kernel temporal, sin estructura causal explícita.

**Propósito:** comparar contra alternativa flexible no autoregresiva.

**Esfuerzo:** opcional según tiempo disponible.

## 4. Tabla de comparación a producir

```
| Caso         | RMSE ABM+ODE | RMSE ABM solo | RMSE ARIMA | RMSE VAR | RMSE RW |
|--------------|-------------:|--------------:|-----------:|---------:|--------:|
| 04 Energía   |          ... |           ... |        ... |      ... |     ... |
| 16 Deforest. |          ... |           ... |        ... |      ... |     ... |
| 20 Kessler   |          ... |           ... |        ... |      ... |     ... |
| 27 Riesgo Bio|          ... |           ... |        ... |      ... |     ... |
| 24 Microplást|          ... |           ... |        ... |      ... |     ... |
| 06 Falsac.Ex.|          ... |           ... |        ... |      ... |     ... |
| 07 Falsac.NS |          ... |           ... |        ... |      ... |     ... |
| 08 Falsac.Obs|          ... |           ... |        ... |      ... |     ... |
```

## 5. Hipótesis a verificar

| H | Enunciado | Lectura |
|---|-----------|---------|
| HB.1 | RMSE_ABM+ODE < RMSE_ARIMA en al menos 3 de 5 casos strong | El aparato no es solo ablación trivial |
| HB.2 | RMSE_ABM+ODE ≈ RMSE_ARIMA en los 3 controles de falsación | Coherente: en falsación, ARIMA y aparato están al mismo nivel porque no hay estructura adicional |
| HB.3 | Si RMSE_ARIMA gana en algún caso strong, identificar por qué | Posibilidad legítima en casos donde la dinámica es dominantemente estacionaria |
| HB.4 | Discriminación cualitativa: el aparato distingue strong vs. null mejor que la diferencia ARIMA-RW | Valor diferencial del aparato es discriminación, no predicción |

## 6. Aclaración interpretativa central

El aparato EDI no se justifica por **mejor predicción puntual**. Se justifica por:

- **discriminación bajo intervención ablativa** (la propia métrica EDI = 1 − RMSE_coupled / RMSE_no_ode mide exactamente esto);
- **clasificación robusta del corpus en niveles** (4 strong, 7 weak, 2 suggestive, 4 trend, 8 null);
- **falsación correcta de los controles** (3/3 rechazados);
- **interpretabilidad ontológica** (la sonda ODE encarna una hipótesis teórica, ARIMA no);
- **transferibilidad multidominio** (la misma metodología EDI atraviesa 30 dominios heterogéneos sin reentrenar arquitectura).

Si ARIMA empata o supera al aparato en RMSE absoluto en algún caso, **eso no invalida la tesis**: invalidaría la tesis si el aparato no discriminara mejor entre strong y null que ARIMA. Esto es lo que la tabla comparativa de la sección 4 prueba o refuta.

## 7. Procedimiento de implementación

| Paso | Acción | Responsable |
|------|--------|-------------|
| 1 | Crear módulo `09-simulaciones-edi/common/baselines.py` con ARIMA, VAR, RW | autor técnico |
| 2 | Para cada caso, extraer la serie objetivo y la ventana val_steps | autor técnico |
| 3 | Ajustar ARIMA con búsqueda AIC+BIC, reportar orden seleccionado | autor técnico |
| 4 | Ajustar VAR si el caso tiene múltiples series | autor técnico |
| 5 | Computar RMSE de validación en la ventana val_steps | autor técnico |
| 6 | Comparar con RMSE_coupled del aparato (ya disponible en `metrics.json`) | autor técnico |
| 7 | Producir tabla comparativa consolidada | autor técnico |
| 8 | Análisis: ¿se cumplen HB.1-HB.4? Discutir | ambos autores |
| 9 | Documentar resultado en `09-simulaciones-edi/baselines/README.md` | autor técnico |
| 10 | Integrar la conclusión interpretativa en el manuscrito (capítulo 09 y 06-01) | ambos autores |

## 8. Cronograma estimado

- **Semana 1:** módulo `baselines.py` con ARIMA + VAR + RW.
- **Semana 2:** ejecución sobre los 8 casos seleccionados.
- **Semana 3:** análisis, reporte, integración en manuscrito.

Total: 3 semanas de dedicación parcial.

## 9. Extensiones futuras

- comparación contra modelos bayesianos no estructurados (Gaussian processes, state-space bayesiano);
- comparación contra LSTM / Transformer puramente predictivos sobre las mismas series, una vez establecida la línea base estadística clásica;
- discusión filosófica sobre la diferencia entre **predicción** y **explicación** (referencia: Shmueli 2010, Breiman 2001 sobre las dos culturas de modelado), pero solo si los resultados de la comparación lo ameritan.

## 10. Limitación reconocida

- ARIMA y VAR son modelos lineales; pueden estar en desventaja en casos no lineales por construcción. La comparación es justa solo en la dimensión declarada (predicción puntual univariada/multivariada);
- la métrica RMSE no es la única dimensión de comparación; el aparato EDI compara estructuras causales acopladas, ARIMA no las modela. La tabla de la sección 4 es **suficiente para responder al comité**, no exhaustiva.

## 11. Compromiso

Este programa se ejecuta como **deuda alta** del cierre doctoral. Su no-ejecución implica declarar explícitamente en el manuscrito final que la comparación con baselines estadísticos puros es deuda priorizada de trabajo posterior. Su ejecución parcial se reporta con la cuenta exacta de casos cubiertos.

## 12. Lectura cruzada

- Auditoría que motivó este programa: `Bitacora/2026-04-27-integracion-jacob/04-auditoria-doctoral-v1.md` §6.
- Programa complementario multi-sonda: `03-programa-multi-sonda.md`.
- Aparato formal y métrica EDI: capítulo `03-formalizacion/04-operacionalizacion-de-kappa.md`.
- Resultados consolidados del corpus: `09-simulaciones-edi/README.md`.
