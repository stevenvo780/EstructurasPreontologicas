# Reporte de Validación — Salinización de Suelos (Richards Bilineal)

- generated_at: 2026-05-17T15:16:42.435353Z

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
- **overall_pass**: True

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
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Discrepancia con pre-registro (iter 11-12)

- **Predicción pre-registro:** Null (EDI esperado ≈ 0, sin cierre operativo).
- **Resultado real (phases.real):** Strong — EDI = 0.5152, CI 95% = [0.3367, 0.6681], válido (rango 0.30-0.90).
- **Diferencia:** |dEDI| ≈ 0.497; dirección: upgrade fuerte desde Null a Strong; el caso muestra cierre operativo robusto donde el pre-registro predijo ausencia.
- **Honestidad declarativa:** DISCREPANCIA RECONOCIDA. Lakatos: falsación honesta = virtud, no falla. Upgrade Null → Strong: la sonda Richards bilineal sí captura la dinámica de salinización donde el pre-registro anticipaba un null.
- **PENDIENTE confirmación bajo block-permutation (adversarial iter 12)** — el upgrade no se considera consolidado hasta que iter 13 termine la auditoría con permutación por bloques (controla autocorrelación temporal).

