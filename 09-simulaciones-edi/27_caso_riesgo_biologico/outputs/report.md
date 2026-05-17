# Reporte de Validación — Riesgo Biológico Global (Woolhouse Bilineal)

- generated_at: 2026-05-17T04:20:36.055676Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0035
- bootstrap_mean: -0.0034
- CI 95%: [-0.0055, -0.0007]
- weighted_value (LoE factor 0.60): -0.0021
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9948
- external: 0.9957
- CR: 0.9991
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.9603
- rmse_abm_no_ode: 1.9535
- rmse_ode: 2.7220
- rmse_reduced: 2.3900
- threshold: 0.9305

### Calibración
- forcing_scale: 0.9489
- macro_coupling: 0.1275
- ode_coupling_strength: 0.1020
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8791
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.2160
- bootstrap_mean: -1.1124
- CI 95%: [-20.0495, 0.3226]
- weighted_value (LoE factor 0.60): 0.1296
- válido (0.30-0.90): False
- detrended_edi: 0.2160
- trend_ratio: 1.000
- trend_r2: 0.547

### Symploké y CR
- internal: 0.9952
- external: 0.9958
- CR: 0.9993
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.9643
- rmse_abm_no_ode: 1.2300
- rmse_ode: 2.2089
- rmse_reduced: 1.5950
- threshold: 0.8154

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1123
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

