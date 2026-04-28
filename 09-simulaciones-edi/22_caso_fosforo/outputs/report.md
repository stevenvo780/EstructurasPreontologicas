# Reporte de Validación — Ciclo del Fósforo (Carpenter Biogeoquímico)

- generated_at: 2026-02-15T23:50:26.553748Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.1253
- bootstrap_mean: 0.1269
- CI 95%: [0.1047, 0.1575]
- weighted_value (LoE factor 0.60): 0.0752
- válido (0.30-0.90): False
- detrended_edi: 0.1253
- trend_ratio: 1.000
- trend_r2: 0.534

### Symploké y CR
- internal: 0.9987
- external: 0.9948
- CR: 1.0040
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.4686
- rmse_abm_no_ode: 1.6789
- rmse_ode: 2.3936
- rmse_reduced: 2.5775
- threshold: 0.9097

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0401
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8042
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.1924
- bootstrap_mean: 0.1989
- CI 95%: [-0.2214, 0.5502]
- weighted_value (LoE factor 0.60): 0.1154
- válido (0.30-0.90): False
- detrended_edi: 0.1924
- trend_ratio: 1.000
- trend_r2: 0.774

### Symploké y CR
- internal: 0.9996
- external: 0.9973
- CR: 1.0023
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.2397
- rmse_abm_no_ode: 0.2968
- rmse_ode: 1.5766
- rmse_reduced: 2.3362
- threshold: 0.4564

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.3498
- ode_coupling_strength: 0.2798
- abm_feedback_gamma: 0.0500
- damping: 0.8965
- ode_alpha: 0.0114
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2804
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

