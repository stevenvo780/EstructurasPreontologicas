# Reporte de Validación — Constelaciones Satelitales Starlink (Saturation Growth)

- generated_at: 2026-05-17T15:16:29.352845Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.4248
- bootstrap_mean: -0.4254
- CI 95%: [-0.4433, -0.4085]
- weighted_value (LoE factor 0.60): -0.2549
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9987
- CR: 1.0013
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0939
- rmse_abm_no_ode: 0.7678
- rmse_ode: 1.2155
- rmse_reduced: 0.8691
- threshold: 0.1419

### Calibración
- forcing_scale: 0.1884
- macro_coupling: 0.4821
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.1909
- ode_alpha: 0.0380
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.3264
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.7575
- bootstrap_mean: 0.7573
- CI 95%: [0.7406, 0.7747]
- weighted_value (LoE factor 0.60): 0.4545
- válido (0.30-0.90): True
- detrended_edi: 0.5127
- trend_ratio: 0.677
- trend_r2: 0.976

### Symploké y CR
- internal: 1.0000
- external: 0.0000
- CR: inf
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 0.3002
- rmse_abm_no_ode: 1.2380
- rmse_ode: 2.6808
- rmse_reduced: 1.2382
- threshold: 0.1580

### Calibración
- forcing_scale: 0.1340
- macro_coupling: 0.4877
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.1559
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.6356
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

