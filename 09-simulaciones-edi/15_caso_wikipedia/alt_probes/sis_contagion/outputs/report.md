# Reporte de Validación — Wikipedia (Conocimiento Colectivo) — SIS Contagion

- generated_at: 2026-05-17T15:03:51.863806Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0730
- bootstrap_mean: 0.0731
- CI 95%: [0.0713, 0.0751]
- weighted_value (LoE factor 0.60): 0.0438
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9998
- external: 0.9959
- CR: 1.0039
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.7828
- rmse_abm_no_ode: 3.0021
- rmse_ode: 2.4865
- rmse_reduced: 1.6761
- threshold: 1.1374

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6929
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.5048
- ode_rolling: None

### Interpretación
**Nivel 2 — Cierre operativo suggestive.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0001
- bootstrap_mean: -0.0005
- CI 95%: [-0.0055, 0.0011]
- weighted_value (LoE factor 0.60): 0.0001
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9843
- external: 0.9627
- CR: 1.0225
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.9391
- rmse_abm_no_ode: 3.9395
- rmse_ode: 3.9075
- rmse_reduced: 3.8775
- threshold: 3.4561

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.7729
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

