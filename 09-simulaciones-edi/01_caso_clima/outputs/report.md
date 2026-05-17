# Reporte de Validación — Clima Regional (CONUS)

- generated_at: 2026-05-17T04:34:27.278935Z

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
- valor: -0.0007
- bootstrap_mean: -0.0006
- CI 95%: [-0.0044, 0.0033]
- weighted_value (LoE factor 1.00): -0.0007
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9999
- external: 0.9999
- CR: 1.0001
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.9274
- rmse_abm_no_ode: 0.9268
- rmse_ode: 0.9302
- rmse_reduced: 1.4942
- threshold: 0.9458

### Calibración
- forcing_scale: 0.2703
- macro_coupling: 0.1148
- ode_coupling_strength: 0.0919
- abm_feedback_gamma: 0.0500
- damping: 0.1676
- ode_alpha: 0.1465
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.9348
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

