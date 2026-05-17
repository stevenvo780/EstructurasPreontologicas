# Reporte de Validación — Depleción de Acuíferos (Darcy-Theis)

- generated_at: 2026-05-17T15:16:44.586161Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0608
- bootstrap_mean: -0.0642
- CI 95%: [-0.1004, -0.0467]
- weighted_value (LoE factor 0.60): -0.0365
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9452
- external: 0.8680
- CR: 1.0889
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.3743
- rmse_abm_no_ode: 1.2954
- rmse_ode: 1.5150
- rmse_reduced: 0.9439
- threshold: 0.8250

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8258
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0035
- bootstrap_mean: 0.0035
- CI 95%: [0.0016, 0.0054]
- weighted_value (LoE factor 0.60): 0.0021
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9771
- external: 0.9159
- CR: 1.0668
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0037
- rmse_abm_no_ode: 1.0072
- rmse_ode: 0.9980
- rmse_reduced: 0.9904
- threshold: 0.9792

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.9189
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

