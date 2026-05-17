# Reporte de Validación — Energía (Consumo Per Cápita) — B-T2.1 Refrescado OWID Renovables

- generated_at: 2026-05-17T15:44:48.169728Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.3298
- bootstrap_mean: 0.3318
- CI 95%: [0.2880, 0.3796]
- weighted_value (LoE factor 0.60): 0.1979
- válido (0.30-0.90): True
- detrended_edi: -0.0104
- trend_ratio: -0.032
- trend_r2: 0.852
- ⚠️ **Advertencia**: trend_ratio < 0.5 — la mayor parte del EDI podría provenir de la tendencia lineal

### Symploké y CR
- internal: 0.9994
- external: 0.9934
- CR: 1.0060
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.5253
- rmse_abm_no_ode: 2.2760
- rmse_ode: 5.3403
- rmse_reduced: 4.9588
- threshold: 1.1854

### Calibración
- forcing_scale: 0.8527
- macro_coupling: 0.6000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2866
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.1571
- bootstrap_mean: 0.1597
- CI 95%: [0.1330, 0.1926]
- weighted_value (LoE factor 0.60): 0.0943
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9998
- external: 0.9991
- CR: 1.0006
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.4718
- rmse_abm_no_ode: 1.7462
- rmse_ode: 0.8726
- rmse_reduced: 1.8251
- threshold: 0.2925

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.4014
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6796
- ode_alpha: 0.1364
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2704
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

