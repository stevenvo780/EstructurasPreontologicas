# Reporte de Validación — Salinización de Suelos (Richards Bilineal)

- generated_at: 2026-02-15T23:50:26.664656Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0022
- bootstrap_mean: -0.0021
- CI 95%: [-0.0040, 0.0002]
- weighted_value (LoE factor 0.60): -0.0013
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9949
- external: 0.9960
- CR: 0.9989
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.9363
- rmse_abm_no_ode: 1.9321
- rmse_ode: 2.6814
- rmse_reduced: 2.3702
- threshold: 0.9285

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8823
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0184
- bootstrap_mean: 0.0142
- CI 95%: [-0.0771, 0.0825]
- weighted_value (LoE factor 0.60): 0.0111
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9998
- external: 0.9998
- CR: 1.0001
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.3283
- rmse_abm_no_ode: 0.3344
- rmse_ode: 1.1643
- rmse_reduced: 2.1959
- threshold: 0.4144

### Calibración
- forcing_scale: 0.9534
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.8834
- ode_alpha: 0.4828
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.3609
- ode_rolling: None

### Interpretación
**Nivel 2 — Cierre operativo suggestive.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

