# Reporte de Validación — Kessler (Debris Orbital) — B-T2.1 refrescado

- generated_at: 2026-05-17T15:44:19.265975Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.1388
- bootstrap_mean: -0.1369
- CI 95%: [-0.2414, 0.0067]
- weighted_value (LoE factor 0.60): -0.0833
- válido (0.30-0.90): False
- detrended_edi: 0.0256
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
- **overall_pass**: False

### EDI
- valor: -1.0000
- bootstrap_mean: -8.7600
- CI 95%: [-12.2673, -6.0086]
- weighted_value (LoE factor 0.60): -0.6000
- válido (0.30-0.90): False
- detrended_edi: -0.3295
- trend_ratio: 1.000
- trend_r2: 1.000

### Symploké y CR
- internal: 0.9988
- external: 0.9936
- CR: 1.0052
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.6319
- rmse_abm_no_ode: 0.0651
- rmse_ode: 2.5167
- rmse_reduced: 2.1189
- threshold: 0.3248

### Calibración
- forcing_scale: 0.8867
- macro_coupling: 0.4973
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1581
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

