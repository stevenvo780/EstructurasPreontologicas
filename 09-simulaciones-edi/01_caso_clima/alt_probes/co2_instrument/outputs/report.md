# Reporte de Validación — Clima Regional (CONUS) — Sonda CO2 (alt_probe V)

- generated_at: 2026-07-16T07:13:23.939653Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0116
- bootstrap_mean: 0.0117
- CI 95%: [0.0109, 0.0125]
- weighted_value (LoE factor 1.00): 0.0116
- válido (0.30-0.90): False
- detrended_edi: -0.0024
- trend_ratio: -0.204
- trend_r2: 0.983
- ⚠️ **Advertencia**: trend_ratio < 0.5 — la mayor parte del EDI podría provenir de la tendencia lineal

### Symploké y CR
- internal: 1.0000
- external: 0.9998
- CR: 1.0002
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.8858
- rmse_abm_no_ode: 3.9316
- rmse_ode: 2.8675
- rmse_reduced: 6.9508
- threshold: 2.7339

### Calibración
- forcing_scale: 0.4913
- macro_coupling: 0.3005
- ode_coupling_strength: 0.2404
- abm_feedback_gamma: 0.0500
- damping: 0.4766
- ode_alpha: 0.1789
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1715
- ode_rolling: None

### Interpretación
**Nivel 2 — Cierre operativo suggestive.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.1833
- bootstrap_mean: 0.1835
- CI 95%: [0.1637, 0.2067]
- weighted_value (LoE factor 1.00): 0.1833
- válido (0.30-0.90): False
- detrended_edi: -0.6581
- trend_ratio: -3.591
- trend_r2: 0.810
- ⚠️ **Advertencia**: trend_ratio < 0.5 — la mayor parte del EDI podría provenir de la tendencia lineal

### Symploké y CR
- internal: 1.0000
- external: 0.7014
- CR: 1.4256
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.4010
- rmse_abm_no_ode: 2.9397
- rmse_ode: 3.6510
- rmse_reduced: 2.6131
- threshold: 0.2975

### Calibración
- forcing_scale: 0.0598
- macro_coupling: 0.1102
- ode_coupling_strength: 0.0882
- abm_feedback_gamma: 0.0500
- damping: 0.0309
- ode_alpha: 0.0061
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.4223
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

