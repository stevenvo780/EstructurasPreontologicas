# Reporte de Validación — Kessler (Debris Orbital)

- generated_at: 2026-02-15T23:50:26.419829Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.1943
- bootstrap_mean: -0.1895
- CI 95%: [-0.4161, 0.1025]
- weighted_value (LoE factor 0.60): -0.1166
- válido (0.30-0.90): False
- detrended_edi: -0.1943
- trend_ratio: 1.000
- trend_r2: 0.851

### Symploké y CR
- internal: 0.9985
- external: 0.9963
- CR: 1.0022
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.6723
- rmse_abm_no_ode: 0.5629
- rmse_ode: 0.7473
- rmse_reduced: 1.9713
- threshold: 0.8260

### Calibración
- forcing_scale: 0.6516
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.7079
- ode_alpha: 0.2323
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4365
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.3527
- bootstrap_mean: 0.3694
- CI 95%: [0.3083, 0.5198]
- weighted_value (LoE factor 0.60): 0.2116
- válido (0.30-0.90): True
- detrended_edi: 0.3527
- trend_ratio: 1.000
- trend_r2: 0.872

### Symploké y CR
- internal: 0.9992
- external: 0.9958
- CR: 1.0034
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.6760
- rmse_abm_no_ode: 1.0443
- rmse_ode: 3.6242
- rmse_reduced: 3.2710
- threshold: 0.9270

### Calibración
- forcing_scale: 0.6977
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.7108
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1673
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

