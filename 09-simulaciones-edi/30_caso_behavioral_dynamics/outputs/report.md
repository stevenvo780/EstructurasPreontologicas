# Reporte de Validación — Behavioral Dynamics — Locomoción dirigida (Fajen-Warren 2003 vs Google Mobility)

- generated_at: 2026-05-17T14:54:45.258035Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.1327
- bootstrap_mean: 0.1306
- CI 95%: [-0.1644, 0.3639]
- weighted_value (LoE factor 0.40): 0.0531
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9990
- external: -0.0719
- CR: 13.8883
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.6850
- rmse_abm_no_ode: 0.7899
- rmse_ode: 0.9420
- rmse_reduced: 0.7812
- threshold: 0.6046

### Calibración
- forcing_scale: 0.1671
- macro_coupling: 0.5940
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.2783
- ode_alpha: 0.4913
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.6494
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.6143
- bootstrap_mean: 0.6141
- CI 95%: [0.5930, 0.6380]
- weighted_value (LoE factor 0.40): 0.2457
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9978
- external: 0.9636
- CR: 1.0355
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4809
- rmse_abm_no_ode: 1.2468
- rmse_ode: 1.0612
- rmse_reduced: 0.9218
- threshold: 0.3254

### Calibración
- forcing_scale: 0.6353
- macro_coupling: 0.5859
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0017
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5481
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

