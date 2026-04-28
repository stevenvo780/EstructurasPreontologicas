# Reporte de Validación — Behavioral Dynamics — Locomoción dirigida (Fajen-Warren 2003, segundo orden)

- generated_at: 2026-04-28T02:49:09.311623Z

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
- **overall_pass**: False

### EDI
- valor: 0.2622
- bootstrap_mean: 0.2625
- CI 95%: [0.2494, 0.2798]
- weighted_value (LoE factor 0.40): 0.1049
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9948
- external: 0.9128
- CR: 1.0898
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.2462
- rmse_abm_no_ode: 1.6890
- rmse_ode: 1.0585
- rmse_reduced: 1.0855
- threshold: 1.0848

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.6000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.7647
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5487
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

