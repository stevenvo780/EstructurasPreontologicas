# Reporte de Validación — Conciencia Colectiva

- generated_at: 2026-05-17T14:55:14.410341Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0070
- bootstrap_mean: 0.0361
- CI 95%: [-0.1249, 0.3051]
- weighted_value (LoE factor 0.60): -0.0042
- válido (0.30-0.90): False
- detrended_edi: -0.0070
- trend_ratio: 1.000
- trend_r2: 0.606

### Symploké y CR
- internal: 0.6176
- external: 0.7148
- CR: 0.8641
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.2021
- rmse_abm_no_ode: 0.2007
- rmse_ode: 1.2629
- rmse_reduced: 0.4364
- threshold: 0.1933

### Calibración
- forcing_scale: 0.1879
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.9127
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0121
- bootstrap_mean: -0.0125
- CI 95%: [-0.0164, -0.0099]
- weighted_value (LoE factor 0.60): -0.0073
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.3285
- external: 0.4089
- CR: 0.8034
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.9071
- rmse_abm_no_ode: 1.8842
- rmse_ode: 2.4844
- rmse_reduced: 1.7862
- threshold: 0.8482

### Calibración
- forcing_scale: 0.4659
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.0084
- ode_alpha: 0.5000
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 1.2575
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

