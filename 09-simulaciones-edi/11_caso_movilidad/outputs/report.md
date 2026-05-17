# Reporte de Validación — Movilidad Urbana (Vehículos)

- generated_at: 2026-05-17T15:28:36.548073Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.3629
- bootstrap_mean: 0.3491
- CI 95%: [0.1207, 0.4867]
- weighted_value (LoE factor 1.00): 0.3629
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9931
- external: 0.9876
- CR: 1.0056
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4083
- rmse_abm_no_ode: 0.6409
- rmse_ode: 1.9174
- rmse_reduced: 1.2431
- threshold: 0.3283

### Calibración
- forcing_scale: 0.8741
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5527
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0599
- bootstrap_mean: 0.0212
- CI 95%: [-0.3923, 0.2048]
- weighted_value (LoE factor 1.00): 0.0599
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9994
- external: 0.9986
- CR: 1.0008
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.6302
- rmse_abm_no_ode: 3.8617
- rmse_ode: 6.4171
- rmse_reduced: 6.9981
- threshold: 3.2166

### Calibración
- forcing_scale: 0.9645
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2876
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

