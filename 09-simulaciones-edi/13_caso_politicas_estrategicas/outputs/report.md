# Reporte de Validación — Políticas Estratégicas (Bass Diffusion + Inertia)

- generated_at: 2026-02-15T23:50:17.123760Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0229
- bootstrap_mean: -0.0384
- CI 95%: [-0.9018, 0.5063]
- weighted_value (LoE factor 0.60): 0.0137
- válido (0.30-0.90): False
- detrended_edi: 0.0229
- trend_ratio: 1.000
- trend_r2: 0.794

### Symploké y CR
- internal: 0.9968
- external: 0.9865
- CR: 1.0104
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.1895
- rmse_abm_no_ode: 0.1940
- rmse_ode: 0.5978
- rmse_reduced: 2.5670
- threshold: 0.2856

### Calibración
- forcing_scale: 0.9581
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.8077
- ode_alpha: 0.2951
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2318
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.2972
- bootstrap_mean: 0.2968
- CI 95%: [0.2571, 0.3281]
- weighted_value (LoE factor 0.60): 0.1783
- válido (0.30-0.90): False
- detrended_edi: 0.2972
- trend_ratio: 1.000
- trend_r2: 0.534

### Symploké y CR
- internal: 0.9985
- external: 0.9900
- CR: 1.0087
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.5431
- rmse_abm_no_ode: 0.7728
- rmse_ode: 0.9050
- rmse_reduced: 0.9596
- threshold: 0.1452

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.8889
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.3550
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

