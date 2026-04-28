# Reporte de Validación — Urbanización Global

- generated_at: 2026-02-15T23:50:32.814374Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.7102
- bootstrap_mean: 0.7099
- CI 95%: [0.6480, 0.7775]
- weighted_value (LoE factor 0.60): 0.4261
- válido (0.30-0.90): True
- detrended_edi: 0.7102
- trend_ratio: 1.000
- trend_r2: 0.981

### Symploké y CR
- internal: 0.9995
- external: 0.9927
- CR: 1.0068
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.1615
- rmse_abm_no_ode: 0.5574
- rmse_ode: 2.9630
- rmse_reduced: 2.9579
- threshold: 0.5469

### Calibración
- forcing_scale: 0.7800
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.7121
- ode_alpha: 0.0042
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1370
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.2358
- bootstrap_mean: 0.2362
- CI 95%: [0.2315, 0.2429]
- weighted_value (LoE factor 0.60): 0.1415
- válido (0.30-0.90): False
- detrended_edi: 0.2358
- trend_ratio: 1.000
- trend_r2: 0.997

### Symploké y CR
- internal: 0.9999
- external: 0.9981
- CR: 1.0018
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.9050
- rmse_abm_no_ode: 1.1844
- rmse_ode: 2.9353
- rmse_reduced: 3.6324
- threshold: 0.8867

### Calibración
- forcing_scale: 0.7796
- macro_coupling: 0.2017
- ode_coupling_strength: 0.1613
- abm_feedback_gamma: 0.0500
- damping: 0.7108
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.0844
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

