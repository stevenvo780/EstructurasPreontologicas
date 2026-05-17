# Reporte de Validación — Microplásticos Oceánicos (Jambeck Accumulation-Decay)

- generated_at: 2026-05-17T15:44:38.298674Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0760
- bootstrap_mean: 0.0771
- CI 95%: [0.0693, 0.0920]
- weighted_value (LoE factor 0.60): 0.0456
- válido (0.30-0.90): False
- detrended_edi: -0.0143
- trend_ratio: -0.189
- trend_r2: 0.820
- ⚠️ **Advertencia**: trend_ratio < 0.5 — la mayor parte del EDI podría provenir de la tendencia lineal

### Symploké y CR
- internal: 0.9992
- external: 0.9992
- CR: 1.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.4408
- rmse_abm_no_ode: 1.5592
- rmse_ode: 2.5636
- rmse_reduced: 3.1418
- threshold: 0.8551

### Calibración
- forcing_scale: 0.7902
- macro_coupling: 0.1899
- ode_coupling_strength: 0.1519
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.1920
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.6168
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: -1.0000
- bootstrap_mean: -2.7351
- CI 95%: [-3.0461, -2.3410]
- weighted_value (LoE factor 0.60): -0.6000
- válido (0.30-0.90): False
- detrended_edi: 0.3254
- trend_ratio: 1.000
- trend_r2: 0.998

### Symploké y CR
- internal: 0.9981
- external: 0.9974
- CR: 1.0008
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.1363
- rmse_abm_no_ode: 0.3033
- rmse_ode: 4.0632
- rmse_reduced: 3.6610
- threshold: 1.1070

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.7594
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1238
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

