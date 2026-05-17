# Reporte de Validación — Justicia Algorítmica

- generated_at: 2026-05-17T15:28:32.824459Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0452
- bootstrap_mean: 0.0460
- CI 95%: [0.0402, 0.0553]
- weighted_value (LoE factor 1.00): 0.0452
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9982
- external: 0.9985
- CR: 0.9996
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.7508
- rmse_abm_no_ode: 1.8338
- rmse_ode: 1.0240
- rmse_reduced: 0.7984
- threshold: 0.7086

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8863
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0579
- bootstrap_mean: 0.0460
- CI 95%: [-0.1513, 0.3451]
- weighted_value (LoE factor 1.00): 0.0579
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9983
- external: 0.9976
- CR: 1.0007
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.6601
- rmse_abm_no_ode: 0.7007
- rmse_ode: 0.7429
- rmse_reduced: 1.7559
- threshold: 1.0277

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6590
- ode_alpha: 0.5000
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.3754
- ode_rolling: None

### Interpretación
**Nivel 2 — Cierre operativo suggestive.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

