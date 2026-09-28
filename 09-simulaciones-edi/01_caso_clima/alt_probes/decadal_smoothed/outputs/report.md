# Reporte de Validación — Clima Regional (CONUS) — Sonda Suavizado Decadal (alt_probe V)

- generated_at: 2026-07-16T07:13:35.975741Z

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
- valor: 0.5363
- bootstrap_mean: 0.5363
- CI 95%: [0.5226, 0.5513]
- weighted_value (LoE factor 1.00): 0.5363
- válido (0.30-0.90): True
- detrended_edi: 0.1782
- trend_ratio: 0.332
- trend_r2: 0.984
- ⚠️ **Advertencia**: trend_ratio < 0.5 — la mayor parte del EDI podría provenir de la tendencia lineal

### Symploké y CR
- internal: 1.0000
- external: 0.9967
- CR: 1.0033
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.3608
- rmse_abm_no_ode: 2.9349
- rmse_ode: 0.8912
- rmse_reduced: 0.9588
- threshold: 0.7075

### Calibración
- forcing_scale: 0.1503
- macro_coupling: 0.2183
- ode_coupling_strength: 0.1747
- abm_feedback_gamma: 0.0500
- damping: 0.1060
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.5260
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

