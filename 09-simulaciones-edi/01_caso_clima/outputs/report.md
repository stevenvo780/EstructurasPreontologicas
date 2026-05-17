# Reporte de Validación — Clima Regional (CONUS)

- generated_at: 2026-05-17T15:16:41.385907Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0689
- bootstrap_mean: 0.0692
- CI 95%: [0.0626, 0.0760]
- weighted_value (LoE factor 1.00): 0.0689
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9998
- external: 0.9699
- CR: 1.0309
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.5248
- rmse_abm_no_ode: 1.6377
- rmse_ode: 1.6466
- rmse_reduced: 1.9038
- threshold: 1.0649

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.3456
- ode_coupling_strength: 0.2765
- abm_feedback_gamma: 0.0500
- damping: 0.6579
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
- valor: 0.2690
- bootstrap_mean: 0.2691
- CI 95%: [0.2572, 0.2826]
- weighted_value (LoE factor 1.00): 0.2690
- válido (0.30-0.90): False
- detrended_edi: 0.3968
- trend_ratio: 1.475
- trend_r2: 0.998

### Symploké y CR
- internal: 0.9999
- external: 0.9663
- CR: 1.0348
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.5665
- rmse_abm_no_ode: 2.1429
- rmse_ode: 1.1228
- rmse_reduced: 0.9242
- threshold: 0.6950

### Calibración
- forcing_scale: 0.0463
- macro_coupling: 0.3607
- ode_coupling_strength: 0.2886
- abm_feedback_gamma: 0.0500
- damping: 0.0455
- ode_alpha: 0.0010
- ode_beta: 0.6762
- assimilation_strength: 0.0000
- calibration_rmse: 0.5420
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

