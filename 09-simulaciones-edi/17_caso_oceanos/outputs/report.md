# Reporte de Validación — Océanos (OHC proxy)

- generated_at: 2026-02-15T23:50:31.163069Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.1495
- bootstrap_mean: 0.1533
- CI 95%: [0.1307, 0.1928]
- weighted_value (LoE factor 0.60): 0.0897
- válido (0.30-0.90): False
- detrended_edi: 0.1495
- trend_ratio: 1.000
- trend_r2: 0.982

### Symploké y CR
- internal: 0.9994
- external: 0.9993
- CR: 1.0001
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.5416
- rmse_abm_no_ode: 1.8125
- rmse_ode: 1.1440
- rmse_reduced: 4.5141
- threshold: 1.2593

### Calibración
- forcing_scale: 0.7990
- macro_coupling: 0.4747
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.7084
- ode_alpha: 0.5000
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2741
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0154
- bootstrap_mean: -0.0187
- CI 95%: [-0.0308, -0.0109]
- weighted_value (LoE factor 0.60): -0.0092
- válido (0.30-0.90): False
- detrended_edi: -0.0154
- trend_ratio: 1.000
- trend_r2: 0.615

### Symploké y CR
- internal: 0.9998
- external: 0.9988
- CR: 1.0011
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 4.2517
- rmse_abm_no_ode: 4.1872
- rmse_ode: 4.5681
- rmse_reduced: 2.7605
- threshold: 2.7353

### Calibración
- forcing_scale: 0.7595
- macro_coupling: 0.1131
- ode_coupling_strength: 0.0904
- abm_feedback_gamma: 0.0500
- damping: 0.6913
- ode_alpha: 0.2690
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2765
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

