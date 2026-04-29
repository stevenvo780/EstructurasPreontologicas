# Reporte de baselines (F15)

Comparación del modelo acoplado EDI (`abm_coupled`) contra baselines no-estructurales: persistencia, random walk con drift, ARIMA(1,1,1)/(1,0,1), VAR(1) con forcing exógeno.

**Casos procesados:** 7
**Generado:** 2026-04-29T01:45:01.399990+00:00Z

## Tabla de RMSE en validación
| Caso | n | train | val | RMSE acoplado | RMSE sin-ODE | RMSE persist | RMSE RW | RMSE ARIMA | RMSE VAR | EDI(val) |
|------|--:|------:|----:|--------------:|-------------:|-------------:|--------:|-----------:|---------:|---------:|
| 04_caso_energia | 100 | 80 | 20 | 0.4058 | 3.1083 | 0.5689 | 0.4527 | 0.4830 | 0.5846 | 0.8694 |
| 16_caso_deforestacion | 100 | 87 | 13 | 0.5652 | 4.7085 | 0.2814 | 0.5868 | 0.2807 | 0.2465 | 0.8800 |
| 20_caso_kessler | 100 | 92 | 8 | 0.5576 | 2.9586 | 1.5829 | 1.2208 | 1.5887 | 1.6105 | 0.8115 |
| 24_caso_microplasticos | 100 | 92 | 8 | 0.3055 | 2.0539 | 0.3751 | 0.6145 | 0.3656 | 0.2595 | 0.8513 |
| 27_caso_riesgo_biologico | 100 | 92 | 8 | 0.2393 | 4.1624 | 0.1817 | 0.6067 | 0.1820 | 0.2257 | 0.9425 |
| 41_caso_wolfram_extendido | 200 | 140 | 60 | 0.0532 | 0.0774 | 0.0800 | 0.0959 | 0.0287 | 0.0482 | 0.3124 |
| 42_caso_histeresis_institucional | 156 | 110 | 46 | 0.0000 | 0.5002 | 0.0521 | 0.3147 | 0.0521 | 0.2018 | 1.0000 |

## EDI vs baselines (1 - RMSE_acoplado / RMSE_baseline)

Si EDI_vs_baseline > 0, el modelo acoplado supera al baseline.

| Caso | vs persist | vs RW | vs ARIMA | vs VAR | vs sin-ODE |
|------|----------:|------:|---------:|-------:|-----------:|
| 04_caso_energia | +0.2867 | +0.1035 | +0.1598 | +0.3058 | +0.8694 |
| 16_caso_deforestacion | -1.0084 | +0.0368 | -1.0135 | -1.2925 | +0.8800 |
| 20_caso_kessler | +0.6477 | +0.5433 | +0.6490 | +0.6538 | +0.8115 |
| 24_caso_microplasticos | +0.1855 | +0.5028 | +0.1643 | -0.1772 | +0.8513 |
| 27_caso_riesgo_biologico | -0.3167 | +0.6056 | -0.3149 | -0.0603 | +0.9425 |
| 41_caso_wolfram_extendido | +0.3347 | +0.4449 | -0.8533 | -0.1044 | +0.3124 |
| 42_caso_histeresis_institucional | +1.0000 | +1.0000 | +1.0000 | +1.0000 | +1.0000 |

## Lectura

1. **Persistencia / RW** son baselines triviales. Que el modelo acoplado los supere es necesario pero insuficiente.
2. **ARIMA(1,1,1)** captura autocorrelación + tendencia sin estructura física. Si el acoplado lo supera, hay valor más allá de regularidad temporal.
3. **VAR(1) con forcing** captura linealmente la dependencia con el exógeno. Si el acoplado lo supera, hay no-linealidad estructural justificable.
4. **EDI(val)** recalculado en held-out usando los mismos arrays. Discrepancias con el `metrics.json` original indican efecto de longitud de ventana (los `metrics.json` usan ventana completa con calibración).

## Trazabilidad

- Generado por: `scripts/baselines_arima_var.py`
- Fuente: `09-simulaciones-edi/<caso>/outputs/primary_arrays.json`
- Splits: usa `val_steps` del `metrics.json` cuando está disponible; si no, 30% del final.
