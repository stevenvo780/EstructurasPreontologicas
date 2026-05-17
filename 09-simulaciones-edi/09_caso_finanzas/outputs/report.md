# Reporte de Validación — Finanzas (SPY)

- generated_at: 2026-05-17T04:49:09.590571Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.6648
- bootstrap_mean: -0.6666
- CI 95%: [-0.7183, -0.6211]
- weighted_value (LoE factor 1.00): -0.6648
- válido (0.30-0.90): False
- detrended_edi: -0.6648
- trend_ratio: 1.000
- trend_r2: 0.632

### Symploké y CR
- internal: 1.0000
- external: 0.9988
- CR: 1.0012
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.9701
- rmse_abm_no_ode: 0.5827
- rmse_ode: 1.2581
- rmse_reduced: 1.5603
- threshold: 0.4260

### Calibración
- forcing_scale: 0.2196
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.2468
- ode_alpha: 0.0351
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.3209
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.1027
- bootstrap_mean: 0.1027
- CI 95%: [0.1006, 0.1052]
- weighted_value (LoE factor 1.00): 0.1027
- válido (0.30-0.90): False
- detrended_edi: 0.1027
- trend_ratio: 1.000
- trend_r2: 0.979

### Symploké y CR
- internal: 0.9997
- external: 0.3770
- CR: 2.6520
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 2.8847
- rmse_abm_no_ode: 3.2147
- rmse_ode: 4.6226
- rmse_reduced: 3.2176
- threshold: 1.1814

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.3401
- ode_coupling_strength: 0.2721
- abm_feedback_gamma: 0.0500
- damping: 0.0284
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.6733
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

