# Reporte de Validación — Wikipedia (Conocimiento Colectivo)

- generated_at: 2026-02-15T23:51:07.653690Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.1967
- bootstrap_mean: 0.1968
- CI 95%: [0.1925, 0.2014]
- weighted_value (LoE factor 0.60): 0.1180
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9999
- external: 0.9983
- CR: 1.0016
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.4132
- rmse_abm_no_ode: 3.0040
- rmse_ode: 1.6758
- rmse_reduced: 1.6761
- threshold: 1.1374

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6919
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.5048
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.1916
- bootstrap_mean: 0.2424
- CI 95%: [0.1247, 0.5135]
- weighted_value (LoE factor 0.60): 0.1150
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9988
- external: 0.9512
- CR: 1.0500
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.0420
- rmse_abm_no_ode: 2.5261
- rmse_ode: 2.5193
- rmse_reduced: 3.3523
- threshold: 2.2194

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.4982
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.7146
- ode_alpha: 0.0985
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8453
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

