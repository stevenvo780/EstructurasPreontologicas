# Reporte de Validación — Salinización de Suelos (Richards Bilineal)

- generated_at: 2026-09-28T03:25:14.177689Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0029
- bootstrap_mean: -0.0028
- CI 95%: [-0.0050, -0.0001]
- weighted_value (LoE factor 0.60): -0.0018
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9946
- external: 0.9955
- CR: 0.9991
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.9551
- rmse_abm_no_ode: 1.9494
- rmse_ode: 2.7022
- rmse_reduced: 2.3702
- threshold: 0.9285

### Calibración
- forcing_scale: 0.9507
- macro_coupling: 0.1291
- ode_coupling_strength: 0.1033
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8811
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.5152
- bootstrap_mean: 0.5186
- CI 95%: [0.3367, 0.6681]
- weighted_value (LoE factor 0.60): 0.3091
- válido (0.30-0.90): True
- detrended_edi: 0.0007
- trend_ratio: 0.001
- trend_r2: 0.893
- ⚠️ **Advertencia**: trend_ratio < 0.5 — la mayor parte del EDI podría provenir de la tendencia lineal

### Symploké y CR
- internal: 0.9996
- external: 0.9984
- CR: 1.0013
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.1279
- rmse_abm_no_ode: 0.2639
- rmse_ode: 1.2550
- rmse_reduced: 2.3958
- threshold: 0.3817

### Calibración
- forcing_scale: 0.9821
- macro_coupling: 0.3787
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.2514
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1393
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Discrepancia con pre-registro (generada automáticamente)

- **Predicción pre-registro:** Null (EDI esperado ≈ 0.0180, margen |ΔEDI| ≤ 0.05).
- **Resultado real (phases.real):** Strong — EDI = 0.5152, p_perm = 0.0000, CI 95% = [0.3367, 0.6681].
- **Diferencia:** |ΔEDI| = 0.4972; dirección: upgrade (Null → Strong).
- **Declaración:** DISCREPANCIA RECONOCIDA. Contraevidencia declarada según PRE_REGISTRO.md §6: la discrepancia honesta es virtud, no fallo.

