# Reporte de Validación — Postverdad (SIS Infodemic)

- generated_at: 2026-05-17T15:28:50.276970Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0119
- bootstrap_mean: -0.0099
- CI 95%: [-0.0234, 0.0171]
- weighted_value (LoE factor 0.60): -0.0071
- válido (0.30-0.90): False
- detrended_edi: 0.0101
- trend_ratio: 1.000
- trend_r2: 0.760

### Symploké y CR
- internal: 0.9998
- external: 0.9989
- CR: 1.0009
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.5764
- rmse_abm_no_ode: 1.5579
- rmse_ode: 3.0951
- rmse_reduced: 4.1071
- threshold: 1.1574

### Calibración
- forcing_scale: 0.9456
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.7852
- ode_alpha: 0.5000
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5018
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0022
- bootstrap_mean: 0.0024
- CI 95%: [0.0011, 0.0050]
- weighted_value (LoE factor 0.60): 0.0013
- válido (0.30-0.90): False
- detrended_edi: -0.0004
- trend_ratio: 1.000
- trend_r2: 0.761

### Symploké y CR
- internal: 0.9973
- external: 0.9880
- CR: 1.0094
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 72.5762
- rmse_abm_no_ode: 72.7360
- rmse_ode: 73.9716
- rmse_reduced: 74.9359
- threshold: 27.2964

### Calibración
- forcing_scale: 0.9455
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0283
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.3187
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

