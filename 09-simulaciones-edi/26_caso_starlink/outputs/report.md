# Reporte de Validación — Constelaciones Satelitales Starlink (Saturation Growth)

- generated_at: 2026-02-15T23:50:23.439412Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.4566
- bootstrap_mean: -0.4570
- CI 95%: [-0.4781, -0.4376]
- weighted_value (LoE factor 0.60): -0.2740
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9986
- CR: 1.0014
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0969
- rmse_abm_no_ode: 0.7530
- rmse_ode: 1.2168
- rmse_reduced: 0.8690
- threshold: 0.1419

### Calibración
- forcing_scale: 0.1806
- macro_coupling: 0.4980
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.1845
- ode_alpha: 0.0380
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.3266
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.6892
- bootstrap_mean: 0.6892
- CI 95%: [0.6892, 0.6892]
- weighted_value (LoE factor 0.60): 0.4135
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9999
- external: 0.5756
- CR: 1.7371
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.2275
- rmse_abm_no_ode: 0.7318
- rmse_ode: 2.1003
- rmse_reduced: 0.9172
- threshold: 0.1000

### Calibración
- forcing_scale: 0.6090
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.2010
- ode_alpha: 0.0069
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5051
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

