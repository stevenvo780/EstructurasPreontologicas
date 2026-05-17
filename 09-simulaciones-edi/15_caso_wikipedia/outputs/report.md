# Reporte de Validación — Wikipedia (Conocimiento Colectivo)

- generated_at: 2026-05-17T14:55:46.236309Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.1964
- bootstrap_mean: 0.1964
- CI 95%: [0.1924, 0.2008]
- weighted_value (LoE factor 0.60): 0.1178
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9999
- external: 0.9983
- CR: 1.0016
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.4126
- rmse_abm_no_ode: 3.0021
- rmse_ode: 1.6758
- rmse_reduced: 1.6761
- threshold: 1.1374

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6929
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.5048
- ode_rolling: None

### Interpretación
**Nivel 1 — Tendencia no confirmada.** Se detecta EDI positivo pero sin significancia estadística. El fenómeno no muestra cierre operativo verificable.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0038
- bootstrap_mean: -0.0067
- CI 95%: [-0.0227, -0.0016]
- weighted_value (LoE factor 0.60): -0.0023
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9832
- external: 0.9624
- CR: 1.0216
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.9546
- rmse_abm_no_ode: 3.9395
- rmse_ode: 3.9784
- rmse_reduced: 3.8775
- threshold: 3.4561

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.7729
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Discrepancia con pre-registro (iter 11-12)

- **Predicción pre-registro:** Weak (EDI esperado en rango 0.10-0.33 con p < 0.05).
- **Resultado real (phases.real):** Null — EDI = -0.0038, CI 95% = [-0.0227, -0.0016].
- **Diferencia:** |dEDI| ≈ 0.196; dirección: el observado cae por debajo del umbral Weak (0.10) e incluso del umbral Trend (0.05); efecto efectivamente nulo (CI rozando cero).
- **Honestidad declarativa:** DISCREPANCIA RECONOCIDA. Lakatos: falsación honesta = virtud, no falla. El caso Wikipedia no replica el efecto Weak pre-registrado: downgrade Weak → Null documentado. La sonda macro empleada no captura la dinámica del corpus editorial real.

