# Reporte de Validación — Riesgo Biológico Global (Woolhouse Bilineal)

- generated_at: 2026-02-15T23:50:17.847190Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0028
- bootstrap_mean: -0.0027
- CI 95%: [-0.0046, -0.0004]
- weighted_value (LoE factor 0.60): -0.0017
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9951
- external: 0.9962
- CR: 0.9989
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.9400
- rmse_abm_no_ode: 1.9347
- rmse_ode: 2.7015
- rmse_reduced: 2.3900
- threshold: 0.9305

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8803
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.3326
- bootstrap_mean: 0.3096
- CI 95%: [-0.1975, 0.6484]
- weighted_value (LoE factor 0.60): 0.1995
- válido (0.30-0.90): True
- detrended_edi: 0.3326
- trend_ratio: 1.000
- trend_r2: 0.661

### Symploké y CR
- internal: 0.9998
- external: 0.9952
- CR: 1.0046
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.3252
- rmse_abm_no_ode: 0.4872
- rmse_ode: 2.8892
- rmse_reduced: 2.9797
- threshold: 0.3368

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.2503
- ode_coupling_strength: 0.2003
- abm_feedback_gamma: 0.0500
- damping: 0.8619
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1528
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

