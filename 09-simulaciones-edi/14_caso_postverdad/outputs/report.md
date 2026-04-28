# Reporte de Validación — Postverdad (SIS Infodemic)

- generated_at: 2026-02-15T23:50:33.569747Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0136
- bootstrap_mean: -0.0117
- CI 95%: [-0.0256, 0.0123]
- weighted_value (LoE factor 0.60): -0.0082
- válido (0.30-0.90): False
- detrended_edi: -0.0136
- trend_ratio: 1.000
- trend_r2: 0.760

### Symploké y CR
- internal: 0.9998
- external: 0.9989
- CR: 1.0008
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.5595
- rmse_abm_no_ode: 1.5386
- rmse_ode: 3.0941
- rmse_reduced: 4.1071
- threshold: 1.1574

### Calibración
- forcing_scale: 0.9672
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.7990
- ode_alpha: 0.5000
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5016
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.2428
- bootstrap_mean: 0.2476
- CI 95%: [0.1686, 0.3571]
- weighted_value (LoE factor 0.60): 0.1457
- válido (0.30-0.90): False
- detrended_edi: 0.2428
- trend_ratio: 1.000
- trend_r2: 0.987

### Symploké y CR
- internal: 0.9984
- external: 0.9894
- CR: 1.0091
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.9838
- rmse_abm_no_ode: 1.2993
- rmse_ode: 2.8513
- rmse_reduced: 3.8296
- threshold: 1.1553

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1336
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

