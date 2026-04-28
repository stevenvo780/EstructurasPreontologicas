# Reporte de Validación — Fuga de Cerebros Global (Docquier-Rapoport)

- generated_at: 2026-02-15T23:50:17.920300Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0056
- bootstrap_mean: 0.0014
- CI 95%: [-0.0890, 0.1145]
- weighted_value (LoE factor 0.60): -0.0034
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9934
- external: 0.9665
- CR: 1.0279
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.1359
- rmse_abm_no_ode: 1.1295
- rmse_ode: 1.2387
- rmse_reduced: 1.4319
- threshold: 1.1459

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.4629
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.7887
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0249
- bootstrap_mean: 0.0250
- CI 95%: [-0.1537, 0.1875]
- weighted_value (LoE factor 0.60): 0.0149
- válido (0.30-0.90): False
- detrended_edi: 0.0249
- trend_ratio: 1.000
- trend_r2: 0.794

### Symploké y CR
- internal: 0.9992
- external: 0.9923
- CR: 1.0069
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 4.2052
- rmse_abm_no_ode: 4.3125
- rmse_ode: 4.2985
- rmse_reduced: 6.7010
- threshold: 5.6455

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6572
- ode_alpha: 0.5000
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4602
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

