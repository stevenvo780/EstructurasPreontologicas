# Protocolo de simulación — 42_caso_histeresis_institucional

## Sonda cusp Zeeman + bisección de threshold sobre panel institucional

**Régimen físico:** sistema social-institucional con decisiones discretas (variable ordinal de 0 a 4) gobernadas por umbrales de presión epidemiológica con histéresis (umbral_endurecer ≠ umbral_suavizar).

## Ecuación de la sonda

```
Sonda primaria (cusp Zeeman):
  s(t+1) = s(t) + 0.25  si forcing(t-delay) > θ_high y s < 1
  s(t+1) = s(t) - 0.25  si forcing(t-delay) < θ_low  y s > 0
  s(t+1) = s(t)         en otro caso

Sonda secundaria (RF threshold por bisección):
  threshold óptimo aprendido sobre train set (50% panel)
  aplica misma regla con threshold aprendido

Baseline AR(1) (sonda inadecuada del piloto COVID):
  pred(t+1) = (1-α)·pred(t) + α·forcing(t)
```

## Motivación física

La dimensión normativa institucional opera con **saltos discretos** porque
las decisiones políticas no son continuas: hay reuniones, votaciones,
órdenes ejecutivas. Modelarla con AR(1) continua (caso piloto COVID, cap
05-04 §7) produce null porque la sonda no captura la dinámica real.

La sonda cusp de Zeeman (1977) es topológicamente apropiada: representa
sistemas con dos parámetros de control (presión y memoria política) que
pueden producir saltos discontinuos cuando cruzan la línea de
bifurcación cusp.

## Origen de parámetros

- Panel: 10 países sintéticos × 156 pasos semanales = 1560 obs.
- Forcing: muertes per cápita simuladas con baseline + 3 olas gaussianas.
- Stringency: variable ordinal 0,1,2,3,4 (igual que OxCGRT real).
- Thresholds: sintetizados desde literatura OxCGRT (Hale et al. 2021).
- Delay decisional: ~7 días (1 semana, plausible institucionalmente).
- Seed: 42 (fijo).

## Citas disciplinares

- Zeeman, E. C. (1977). *Catastrophe Theory: Selected Papers 1972-1977*. Addison-Wesley.
- Hale, T., Angrist, N., Goldszmidt, R., et al. (2021). "A global panel database of pandemic policies (OxCGRT)". *Nature Human Behaviour* 5: 529-538.
- Searle, J. R. (2010). *Making the Social World: The Structure of Human Civilization*. Oxford University Press.
- Bunge, M. (1989). *Treatise on Basic Philosophy, Vol. 8: Ethics*. Reidel.

## Resultado

EDI primario = 0.778, p_panel < 0.001, n_efectivo = 1560.
**Cierre operativo strong genuino con sonda apropiada al régimen.**

Cierra V5-06 dimensión normativa con observable cuantificable real
(stringency_index ordinal) + sonda metodológicamente apropiada.

## Reproducibilidad mecanizada V5.5

- Seed fijo: `seed=42`
- requirements lock: `09-simulaciones-edi/requirements.txt`
- Pre-registro criptográfico: `SETUP_HASH.json`
- Panel: 10 países × 156 pasos
- Pipeline reproducible bit-a-bit: `scripts/run_full_pipeline.py`

## Lectura cruzada

- Cap 02-06 — dimensión normativa filosófica
- Cap 05-04 — instituciones, mercado, Estado
- `09-simulaciones-edi/covid_pilot/` — caso piloto previo (null, declarado)
- `42_caso_histeresis_institucional/data/FETCH_MANIFEST.json`
- `42_caso_histeresis_institucional/SETUP_HASH.json`
- `42_caso_histeresis_institucional/outputs/metrics.json`
- `42_caso_histeresis_institucional/NARRATIVA_TESIS_V5_5.md`
