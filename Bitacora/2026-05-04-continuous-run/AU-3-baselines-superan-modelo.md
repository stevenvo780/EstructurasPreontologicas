# AU-3 — Baselines ARIMA/VAR superan al modelo acoplado en casos clave

Fecha: 2026-05-05
Estado: `needs_human` (requiere firma de Jacob para reformular pretensión multidominio en cap 06-01)

## 1. Verificación literal de la afirmación

Lectura directa de `09-simulaciones-edi/baselines/baselines_report.md` (líneas 23-31, columnas "vs ARIMA" y "vs VAR"; signo negativo = baseline supera al modelo acoplado):

| Caso | vs persist | vs RW | vs ARIMA | vs VAR | ¿superado por ARIMA o VAR? |
|------|-----------:|------:|---------:|-------:|:--------------------------:|
| 04_caso_energia            | +0.2867 | +0.1035 | +0.1598 | +0.3058 | NO |
| 16_caso_deforestacion      | **-1.0084** | +0.0368 | **-1.0135** | **-1.2925** | **SÍ (ARIMA y VAR)** |
| 20_caso_kessler            | +0.6477 | +0.5433 | +0.6490 | +0.6538 | NO |
| 24_caso_microplasticos     | +0.1855 | +0.5028 | +0.1643 | **-0.1772** | **SÍ (sólo VAR)** |
| 27_caso_riesgo_biologico   | **-0.3167** | +0.6056 | **-0.3149** | -0.0603 | **SÍ (ARIMA y VAR)** |
| 41_caso_wolfram_extendido  | +0.3347 | +0.4449 | **-0.8533** | -0.1044 | **SÍ (ARIMA y VAR; control)** |
| 42_caso_histeresis         | +1.0000 | +1.0000 | +1.0000 | +1.0000 | NO |

**Hecho verificado:** en al menos un baseline estadístico no estructural (ARIMA o VAR), el modelo acoplado es **superado en 4 de los 7 casos procesados**: Deforestación, Microplásticos, Riesgo Biológico y Wolfram extendido.

Restringido a los **4 casos `overall_pass=True`** (Energía, Deforestación, Kessler, Riesgo Biológico):
- Energía: coupled supera ARIMA y VAR.
- Kessler: coupled supera ARIMA y VAR.
- **Deforestación: ARIMA y VAR superan al coupled (RMSE_VAR=0.2465 vs RMSE_acoplado=0.5652).**
- **Riesgo Biológico: ARIMA y VAR superan al coupled (RMSE_ARIMA=0.1820 vs RMSE_acoplado=0.2393; VAR=0.2257).**

→ **2 de los 4 `overall_pass` están dominados por baselines lineales en RMSE de validación held-out.**

## 2. Cotejo con la condición de fracaso autodeclarada

`06-cierre/01-conclusion-demostrativa.md:85-87`:

> «Si Energía, Deforestación, Kessler, Riesgo Biológico no replican bajo perfiles de alto rendimiento o son superados por baselines puramente estadísticos (ARIMA, VAR), la tesis pierde su demostración multidominio principal.»

El segundo disyunto se cumple para 2 de 4 casos. Esta es la **condición de fracaso parcial autodeclarada por la propia tesis** (Escenario 1). El manuscrito actual no la reconoce en §3 («Hallazgos honestos no triviales»), ni la incorpora a §1 («Verificación de las 7 condiciones»), ni a §4 («Deuda residual»).

Matiz importante (no atenuante): EDI compara el coupled contra **`abm_no_ode`** (ablación interna), no contra ARIMA/VAR. Que ARIMA/VAR ganen en RMSE no invalida automáticamente el EDI como métrica de sensibilidad al acoplamiento ODE→ABM, **pero sí invalida la pretensión de que el aparato produce ganancia predictiva sobre baselines no estructurales** — una pretensión que la condición de fracaso §2 sí asume.

## 3. Propuesta de edición (requiere firma humana)

**No se edita `Tesis.md` ni capítulos por iniciativa de la asistencia.** Propuesta para Jacob:

(a) Insertar en §3 («Hallazgos honestos») un nuevo apartado:

> **3.X. Baselines lineales superan al coupled en 2 de 4 casos `overall_pass`.**
> Lectura literal de `09-simulaciones-edi/baselines/baselines_report.md`: Deforestación (vs ARIMA −1.0135, vs VAR −1.2925) y Riesgo Biológico (vs ARIMA −0.3149, vs VAR −0.0603) son superados por modelos estadísticos no estructurales en RMSE de validación held-out. Esto **activa parcialmente la condición de fracaso del Escenario 1** (§2). El EDI mide sensibilidad al acoplamiento ODE→ABM (ablación interna) y sigue siendo significativo en ambos casos, pero la pretensión de ganancia predictiva multidominio sobre baselines no-estructurales **no se sostiene de manera uniforme**. Costo argumentativo asumido: la demostración multidominio queda restringida a Energía y Kessler como casos donde el aparato supera tanto la ablación interna como los baselines lineales; Deforestación y Riesgo Biológico se reclasifican como casos donde el aparato detecta acoplamiento estructural significativo pero **no produce mejor pronóstico que ARIMA/VAR**.

(b) Reformular el Escenario 1 en §2 reconociendo que la condición ya está parcialmente activada y separar dos subescenarios falsables: (1.a) overall_pass colapsa bajo perfiles agresivos; (1.b) baselines lineales superan al coupled — ya activo en 2/4.

(c) Añadir entrada en §4 «Deuda residual»: ejecutar baselines no lineales (GP, LSTM) sobre los 4 `overall_pass` y reportar; en caso de que sigan ganando los baselines, reclasificar el corpus demostrativo.

## 4. Costo argumentativo declarado

- **No es un fracaso global** (la métrica EDI sigue significativa por permutación en los casos afectados); es **fracaso de una pretensión específica autodeclarada**: ganancia predictiva sobre baselines lineales en los 4 casos `overall_pass`.
- La defensa honesta es separar dos afirmaciones que el manuscrito hoy fusiona: (i) «el acoplamiento ODE→ABM es estructuralmente necesario para reproducir la dinámica» (sostenida por EDI vs sin-ODE) y (ii) «el aparato produce mejor pronóstico que cualquier baseline razonable» (NO sostenida en Deforestación y Riesgo Biológico).
- Mantener (i) y retirar (ii) es **reducción de alcance, no derrota**. Pero ocultar (ii) sería violación de §1 y §7 de `CLAUDE.md`.

## 5. Acción

`needs_human` — la reformulación del Escenario 1 y la reclasificación de Deforestación/Riesgo Biológico tocan voz autoral filosófica de Jacob (cap 06-01) y la pretensión central «multidominio». Marcar como **B-T** o **H-J** según decida Jacob; no se cierra desde la asistencia.

**Archivos consultados:**
- `06-cierre/01-conclusion-demostrativa.md:85-87` (condición de fracaso autodeclarada).
- `09-simulaciones-edi/baselines/baselines_report.md:23-31` (tabla numérica fuente).
