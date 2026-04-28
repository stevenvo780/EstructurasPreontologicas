# Reporte de Validación — Depleción de Acuíferos (Darcy-Theis)

- generated_at: 2026-02-15T23:50:21.122042Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0216
- bootstrap_mean: -0.0230
- CI 95%: [-0.0373, -0.0156]
- weighted_value (LoE factor 0.60): -0.0130
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9824
- external: 0.9647
- CR: 1.0183
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.3335
- rmse_abm_no_ode: 1.3054
- rmse_ode: 1.4191
- rmse_reduced: 0.9439
- threshold: 0.8250

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.2634
- ode_coupling_strength: 0.2107
- abm_feedback_gamma: 0.0500
- damping: 0.9174
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8286
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.1462
- bootstrap_mean: -0.1453
- CI 95%: [-0.1649, -0.1240]
- weighted_value (LoE factor 0.60): -0.0877
- válido (0.30-0.90): False
- detrended_edi: -0.1462
- trend_ratio: 1.000
- trend_r2: 0.984

### Symploké y CR
- internal: 0.9999
- external: 0.9975
- CR: 1.0024
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 22.4152
- rmse_abm_no_ode: 19.5569
- rmse_ode: 28.5565
- rmse_reduced: 35.7619
- threshold: 14.8563

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.5504
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

