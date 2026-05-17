# Reporte de Validación — Océanos (OHC proxy)

- generated_at: 2026-05-17T11:02:46.945829Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.1374
- bootstrap_mean: 0.1412
- CI 95%: [0.1212, 0.1744]
- weighted_value (LoE factor 0.60): 0.0824
- válido (0.30-0.90): False
- detrended_edi: 0.1374
- trend_ratio: 1.000
- trend_r2: 0.982

### Symploké y CR
- internal: 0.9986
- external: 0.9988
- CR: 0.9998
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.6088
- rmse_abm_no_ode: 1.8651
- rmse_ode: 1.1530
- rmse_reduced: 4.5140
- threshold: 1.2593

### Calibración
- forcing_scale: 0.9591
- macro_coupling: 0.4973
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.5000
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2560
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.1902
- bootstrap_mean: 0.1989
- CI 95%: [0.1574, 0.2800]
- weighted_value (LoE factor 0.60): 0.1141
- válido (0.30-0.90): False
- detrended_edi: 0.1902
- trend_ratio: 1.000
- trend_r2: 0.871

### Symploké y CR
- internal: 0.9994
- external: 0.9994
- CR: 1.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.5441
- rmse_abm_no_ode: 0.6719
- rmse_ode: 0.4036
- rmse_reduced: 3.0191
- threshold: 0.7153

### Calibración
- forcing_scale: 0.8846
- macro_coupling: 0.3986
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.4410
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2780
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

