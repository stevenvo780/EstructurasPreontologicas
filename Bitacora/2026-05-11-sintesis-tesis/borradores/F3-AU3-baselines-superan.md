---
borrador: IA
requires: H-J*
propuesta_fecha: 2026-05-11
destino: 06-cierre/01-conclusion-demostrativa.md §3 (Hallazgos honestos)
hallazgo: AU-3
fuente_numerica: 09-simulaciones-edi/baselines/baselines_report.json (generado 2026-04-29T01:45:01Z)
manuscrito_actual_contradictorio: 06-cierre/01-conclusion-demostrativa.md:85-87 (anuncia el escenario de fracaso pero §3 no lo activa)
---

# Borrador IA — Reconocimiento del Escenario 1 parcialmente activado por baselines lineales

Este borrador rescata el hallazgo `Bitacora/2026-05-04-continuous-run/AU-3-baselines-superan-modelo.md`, verificado contra la fuente numérica canónica `09-simulaciones-edi/baselines/baselines_report.json`. Propone inyectar un nuevo apartado §3.6 en `06-cierre/01-conclusion-demostrativa.md` y, en consecuencia, reformular el Escenario 1 de §2 y añadir una entrada a §4 (Deuda residual). NO sustituye la voz autoral de Jacob: este texto vive como borrador-IA hasta firma H-J*.

---

## 1. Verificación numérica (cifras canónicas, 4 decimales)

Lectura literal de `09-simulaciones-edi/baselines/baselines_report.json` (campo `results[*].rmse`), restringida a los **4 casos con `phases.real.overall_pass = True`** en `outputs/metrics.json`:

| Caso | val_len | RMSE acoplado (val) | RMSE ARIMA(1,1,1) | RMSE VAR(1)+forcing | ¿ARIMA gana? | ¿VAR gana? |
|------|---:|---:|---:|---:|:---:|:---:|
| 04_caso_energia          | 20 | 0.4058 | 0.4830 | 0.5846 | no | no |
| 16_caso_deforestacion    | 13 | 0.5652 | 0.2807 | 0.2465 | **sí** | **sí** |
| 20_caso_kessler          |  8 | 0.5576 | 1.5887 | 1.6105 | no | no |
| 27_caso_riesgo_biologico |  8 | 0.2393 | 0.1820 | 0.2257 | **sí** | **sí** |

Cifras `edi_vs_baseline = 1 - RMSE_coupled / RMSE_baseline` (mismo JSON, signo negativo = el baseline supera al acoplado):

- 16_caso_deforestacion: vs ARIMA = **−1.0135**, vs VAR = **−1.2925**.
- 27_caso_riesgo_biologico: vs ARIMA = **−0.3149**, vs VAR = **−0.0603**.
- 04_caso_energia: vs ARIMA = +0.1598, vs VAR = +0.3058 (acoplado gana).
- 20_caso_kessler: vs ARIMA = +0.6490, vs VAR = +0.6538 (acoplado gana).

**Resultado verificado:** en 2 de los 4 casos con `overall_pass=True`, los dos baselines no-estructurales (ARIMA y VAR) superan al modelo acoplado EDI en RMSE de validación held-out.

## 2. Salvedades metodológicas honestas (no atenuantes)

Antes de inyectar el hallazgo en el manuscrito conviene declarar tres salvedades, porque ocultarlas sería un nuevo capa de auto-indulgencia (CLAUDE.md §1):

1. **El RMSE de validación reportado en `baselines_report.json` (`abm_coupled_val`) no es el RMSE de la métrica EDI canónica.** El EDI canónico se calcula sobre serie completa con calibración (`errors.rmse_abm` en `outputs/metrics.json`), mientras los baselines ARIMA/VAR se evaluán sobre held-out con `val_steps` ∈ {8, 13, 20}. Los dos números difieren para el mismo caso (Deforestación: RMSE_abm completo = 0.4894 vs RMSE_coupled_val = 0.5652). La comparación con baselines es **inferencialmente válida solo bajo la métrica held-out**, no bajo el EDI completo. Declarar esto evita conflar dos pretensiones.
2. **El tamaño de validación es pequeño** (val_len ∈ {8, 13} en los dos casos donde el baseline gana). Una comparación de RMSE sobre 8–13 puntos no es estadísticamente robusta; **no** se calculó intervalo de confianza ni test de Diebold-Mariano sobre la diferencia. Por tanto, la frase honesta no es "ARIMA es mejor predictor que el acoplado" sino "el acoplado **no produce ganancia predictiva detectable** sobre ARIMA/VAR en estos dos casos bajo la métrica y la ventana usadas". La fortaleza del hallazgo está limitada por el tamaño muestral.
3. **`overall_pass` no se reduce a RMSE.** Combina C1-C5 (convergencia, robustez, replicación, validez, incertidumbre) y la significancia de la métrica EDI definida como `1 − RMSE_coupled / RMSE_no_ode`. El EDI compara coupled vs ablación interna (`abm_no_ode`), no coupled vs baselines lineales. Por tanto, los 2/4 casos siguen siendo internamente válidos en su pretensión específica —"el acoplamiento ODE→ABM es estructuralmente necesario para reproducir la dinámica"— y solo fallan la pretensión adicional —"el aparato produce mejor pronóstico que cualquier baseline razonable"— que la propia tesis declara como condición de fracaso §1 en `06-cierre/01-conclusion-demostrativa.md:85-87`.

Estas salvedades acotan el hallazgo; **no lo cancelan**: el segundo disyunto del Escenario 1 (autodeclarado por la tesis) sí se cumple, parcialmente, en 2 de 4 casos `overall_pass`. Reconocerlo es lo que CLAUDE.md §7 llama "deuda declarada como virtud".

## 3. Propuesta de párrafo para §3 ("Hallazgos honestos no triviales")

Destino: insertar como **§3.6** después de "3.5. El caso 30 como confirmación de la disciplina del aparato" en `06-cierre/01-conclusion-demostrativa.md` (entre líneas 125 y 127).

> **3.6. Los baselines lineales superan al modelo acoplado en 2 de los 4 casos `overall_pass`.**
>
> La comparación canónica frente a baselines no-estructurales se ejecutó sobre los 7 casos con `primary_arrays.json` y se reporta en `09-simulaciones-edi/baselines/baselines_report.json`. Restringida a los 4 casos con `overall_pass=True`, la lectura literal del RMSE held-out muestra que ARIMA(1,1,1) y VAR(1)+forcing **superan al modelo acoplado en Deforestación y Riesgo Biológico**: para 16_caso_deforestacion, RMSE_acoplado(val) = 0.5652 frente a RMSE_ARIMA = 0.2807 y RMSE_VAR = 0.2465 (val_len = 13); para 27_caso_riesgo_biologico, RMSE_acoplado(val) = 0.2393 frente a RMSE_ARIMA = 0.1820 y RMSE_VAR = 0.2257 (val_len = 8). Energía y Kessler, en cambio, mantienen ventaja del acoplado sobre ambos baselines.
>
> Esto **activa parcialmente el segundo disyunto del Escenario 1 de §2** ("si son superados por baselines puramente estadísticos (ARIMA, VAR), la tesis pierde su demostración multidominio principal"). La tesis no reclama derrota global por tres razones que se declaran sin atenuar el hallazgo: (i) `overall_pass` no se reduce a RMSE held-out, sino que integra los criterios C1-C5 y la significancia de EDI definido sobre ablación interna `abm_no_ode`, no sobre baselines lineales; (ii) la diferencia se mide sobre val_len ∈ {8, 13}, sin intervalo de confianza ni Diebold-Mariano, por lo que la afirmación honesta es "el acoplado **no produce ganancia predictiva detectable** sobre ARIMA/VAR" más que "ARIMA es estrictamente superior"; (iii) el EDI sigue siendo significativo por permutación en los dos casos afectados, lo que sostiene la pretensión interna de necesidad estructural del acoplamiento ODE→ABM.
>
> **Costo argumental asumido.** La demostración multidominio queda restringida a Energía y Kessler como casos donde el aparato supera tanto la ablación interna como los baselines no-estructurales. Deforestación y Riesgo Biológico se reclasifican como casos donde el aparato detecta acoplamiento estructural significativo pero **no exhibe ganancia predictiva frente a modelos estadísticos lineales** bajo la ventana de validación disponible. Esta es **reducción de alcance, no derrota**: la tesis defiende que el acoplamiento ODE→ABM es estructuralmente identificable (sostenido por EDI vs `abm_no_ode`), no que el aparato sea el mejor predictor posible (no sostenido uniformemente). Fusionar ambas pretensiones, como hoy hace el manuscrito en §2 Escenario 1, oculta el costo; separarlas es lo que aquí se declara como deuda.

## 4. Edición de soporte propuesta en §2 (Escenarios)

Reformular Escenario 1 en `06-cierre/01-conclusion-demostrativa.md:83-85` separando dos subescenarios falsables, uno ya parcialmente activo:

> **Escenario 1. Los 4 casos `overall_pass` pierden alguna de sus dos pretensiones.**
>
> *1.a (no activo al 2026-05-11):* si Energía, Deforestación, Kessler o Riesgo Biológico **dejan de pasar `overall_pass`** bajo perfiles de alto rendimiento (n_perm ≥ 2999, n_boot ≥ 1500), la tesis pierde su pretensión de necesidad estructural del acoplamiento ODE→ABM en esos dominios.
>
> *1.b (parcialmente activo al 2026-05-11):* si dichos casos **son superados por baselines puramente estadísticos** (ARIMA, VAR, RW, GP) en RMSE de validación held-out, la tesis pierde su pretensión adicional de ganancia predictiva sobre baselines no-estructurales. Esta condición está **parcialmente activada en Deforestación y Riesgo Biológico** (`09-simulaciones-edi/baselines/baselines_report.json`, val_len ∈ {8, 13}; ver §3.6). Energía y Kessler la satisfacen.

## 5. Edición de soporte propuesta en §4 (Deuda residual)

Añadir entrada a Tabla 6.1.2 (`06-cierre/01-conclusion-demostrativa.md:131-146`):

| Deuda | Descripción | Plazo | Entregable | Estado al 2026-05-11 |
|---|---|---|---|---|
| Baselines no-lineales sobre `overall_pass` afectados | Ejecutar GP, LSTM, ESN sobre Deforestación y Riesgo Biológico; reportar; si siguen ganando los baselines, reclasificar el corpus demostrativo en 06-01 §5.4 | 2 meses | Reporte comparativo con Diebold-Mariano + CI bootstrap | Pendiente — abierto por hallazgo AU-3 (2026-05-04). |

Razón de añadir esta deuda en lugar de "limpiar" el resultado actual: la entrada existente "Baselines estadísticos puros" (línea 138) declara EJECUTADO sobre 7 casos, pero **no reporta** la asimetría de resultados; cerrar la deuda equivale a ocultarla. La nueva entrada concreta el siguiente paso falsable y deja la deuda anterior cerrada solo en su literalidad ("se ejecutó la comparación"), no en su consecuencia inferencial.

## 6. Citas verbatim del JSON (auditoría)

Fragmentos literales de `09-simulaciones-edi/baselines/baselines_report.json` (campo `results`, índices 1 y 4):

```json
{
  "case_id": "16_caso_deforestacion",
  "n": 100, "train_len": 87, "val_len": 13,
  "rmse": {
    "arima_1_1_1": 0.2806844911289528,
    "var_obs_forcing": 0.24652917032745342,
    "abm_coupled_val": 0.5651696622348304
  },
  "edi_vs_baseline": {
    "arima_1_1_1": -1.0135407551790196,
    "var_obs_forcing": -1.2925062437201302
  }
}
```

```json
{
  "case_id": "27_caso_riesgo_biologico",
  "n": 100, "train_len": 92, "val_len": 8,
  "rmse": {
    "arima_1_1_1": 0.18198008490127354,
    "var_obs_forcing": 0.22568275659372156,
    "abm_coupled_val": 0.23929162356020883
  },
  "edi_vs_baseline": {
    "arima_1_1_1": -0.3149330251715594,
    "var_obs_forcing": -0.060300871771901576
  }
}
```

Comando regenerador (CLAUDE.md §4): el JSON fue producido por `scripts/baselines_arima_var.py` el 2026-04-29T01:45:01Z; re-ejecución requiere `python3 09-simulaciones-edi/scripts/baselines_arima_var.py` con `primary_arrays.json` presentes en cada `outputs/`.

## 7. Decisiones que requieren firma de Jacob (H-J*)

1. **Tono filosófico** del nuevo §3.6: el borrador adopta voz medida con concesión declarada y costo argumental. Jacob puede preferir formulación más fuerte ("la tesis reconoce un fracaso parcial sin atenuante") o más reservada ("la diferencia es no significativa dado val_len pequeño"). Decisión filosófica.
2. **Si se separa o no el Escenario 1 en 1.a / 1.b** (§2 reformulado): la separación clarifica qué disyunto está parcialmente activo, pero rompe la numeración existente (Escenarios 2–5 quedarían 3–6 o conservarían número con sub-índice).
3. **Compromiso sobre baselines no-lineales** (GP/LSTM/ESN): el borrador asume plazo de 2 meses. Plazo, alcance y compromiso de reclasificación dependen de la decisión de Jacob sobre prioridades del cronograma.
4. **Reciprocidad con cap 05-aplicaciones**: si §3.6 se acepta, la tabla 5.7.5/5.7.6 de `05-aplicaciones/07-mapa-aplicaciones-corpus.md` y la cifra "4 strong" en `06-cierre/04-versiones-cortas-defensa.md:25,60,114` requieren nota cruzada para no quedar inconsistentes con la nueva reclasificación. Esto excede el alcance de este borrador.

## 8. Lo que este borrador NO toca

- No edita `06-cierre/01-conclusion-demostrativa.md` (firma autoral de Jacob).
- No edita `metrics.json` ni `baselines_report.json` (hook bloquea).
- No reclasifica Deforestación/Riesgo Biológico en otras tablas hasta que Jacob firme el cambio en 06-01.
- No abre ni cierra entradas en `TAREAS_PENDIENTES.md`; la apertura formal de la deuda B-T/H-J corresponde a la siguiente pasada del harness.
