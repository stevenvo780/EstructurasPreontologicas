# Reporte de Validación — Behavioral Dynamics — Locomoción dirigida (Fajen-Warren 2003)

- generated_at: 2026-04-28T02:27:35.770212Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0558
- bootstrap_mean: 0.0559
- CI 95%: [0.0362, 0.0730]
- weighted_value (LoE factor 0.40): 0.0223
- válido (0.30-0.90): False
- detrended_edi: 0.0558
- trend_ratio: 1.000
- trend_r2: 0.835

### Symploké y CR
- internal: 1.0000
- external: 0.9997
- CR: 1.0003
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4285
- rmse_abm_no_ode: 0.4538
- rmse_ode: 0.6996
- rmse_reduced: 2.2802
- threshold: 0.6137

### Calibración
- forcing_scale: 0.3939
- macro_coupling: 0.1855
- ode_coupling_strength: 0.1484
- abm_feedback_gamma: 0.0500
- damping: 0.6111
- ode_alpha: 0.4753
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.3068
- ode_rolling: None

### Interpretación
**Nivel 2 — Cierre operativo suggestive.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0020
- bootstrap_mean: 0.0017
- CI 95%: [-0.0044, 0.0083]
- weighted_value (LoE factor 0.40): 0.0008
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9974
- external: 0.9942
- CR: 1.0032
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0948
- rmse_abm_no_ode: 1.0970
- rmse_ode: 1.0930
- rmse_reduced: 1.1031
- threshold: 1.0896

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.6000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6973
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.4848
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

