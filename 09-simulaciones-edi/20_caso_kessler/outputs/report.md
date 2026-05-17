# Reporte de Validación — Kessler (Debris Orbital)

- generated_at: 2026-05-17T04:28:21.059077Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.1388
- bootstrap_mean: -0.1369
- CI 95%: [-0.2414, 0.0067]
- weighted_value (LoE factor 0.60): -0.0833
- válido (0.30-0.90): False
- detrended_edi: -0.1388
- trend_ratio: 1.000
- trend_r2: 0.851

### Symploké y CR
- internal: 0.9981
- external: 0.9968
- CR: 1.0013
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.7454
- rmse_abm_no_ode: 0.6545
- rmse_ode: 0.7637
- rmse_reduced: 1.9713
- threshold: 0.8260

### Calibración
- forcing_scale: 0.8573
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.2323
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4019
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.6936
- bootstrap_mean: 0.6924
- CI 95%: [0.6617, 0.7174]
- weighted_value (LoE factor 0.60): 0.4162
- válido (0.30-0.90): True
- detrended_edi: 0.6936
- trend_ratio: 1.000
- trend_r2: 1.000

### Symploké y CR
- internal: 0.9995
- external: 0.9966
- CR: 1.0029
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.1770
- rmse_abm_no_ode: 0.5775
- rmse_ode: 2.9807
- rmse_reduced: 3.0157
- threshold: 0.4881

### Calibración
- forcing_scale: 0.8885
- macro_coupling: 0.4429
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1177
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

