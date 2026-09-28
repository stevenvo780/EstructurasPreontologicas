# Reporte de Validación — Clima Regional (CONUS)

- generated_at: 2026-07-16T07:06:58.026505Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0624
- bootstrap_mean: 0.0626
- CI 95%: [0.0566, 0.0688]
- weighted_value (LoE factor 1.00): 0.0624
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9998
- external: 0.9702
- CR: 1.0305
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.5357
- rmse_abm_no_ode: 1.6379
- rmse_ode: 1.6466
- rmse_reduced: 1.9038
- threshold: 1.0649

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.2983
- ode_coupling_strength: 0.2386
- abm_feedback_gamma: 0.0500
- damping: 0.6584
- ode_alpha: 0.1977
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8022
- ode_rolling: None

### Interpretación
**Nivel 2 — Cierre operativo suggestive.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.2581
- bootstrap_mean: 0.2583
- CI 95%: [0.2468, 0.2712]
- weighted_value (LoE factor 1.00): 0.2581
- válido (0.30-0.90): False
- detrended_edi: 0.3845
- trend_ratio: 1.490
- trend_r2: 0.998

### Symploké y CR
- internal: 0.9999
- external: 0.9653
- CR: 1.0358
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.5898
- rmse_abm_no_ode: 2.1430
- rmse_ode: 1.0926
- rmse_reduced: 0.9241
- threshold: 0.6950

### Calibración
- forcing_scale: 0.0463
- macro_coupling: 0.3107
- ode_coupling_strength: 0.2486
- abm_feedback_gamma: 0.0500
- damping: 0.0455
- ode_alpha: 0.0010
- ode_beta: 0.6762
- assimilation_strength: 0.0000
- calibration_rmse: 0.5419
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

