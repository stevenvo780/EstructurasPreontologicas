# Protocolo de simulación — 41_caso_wolfram_extendido

## Sondas EDI sobre autómatas celulares elementales (Rule 30/90/110/184)

**Régimen físico:** sistema computacional discreto con dinámica determinista en grilla unidimensional periódica.

## Ecuación de la sonda

```
state(t+1, i) = rule_table[(state(t,i-1) << 2) | (state(t,i) << 1) | state(t,i+1)]
densidad_macro(t) = mean(state(t, :))

Sonda primaria (logística):  pred(t+1) = pred(t) + α·(forcing(t) - pred(t))
Sonda secundaria (Markov):   transiciones empíricas sobre densidad cuantizada en 5 niveles
```

## Motivación física

Wolfram (2002) define los autómatas celulares elementales como sistemas
computacionalmente irreducibles. Aplicar EDI con sondas simples a
densidades agregadas verifica operativamente si el régimen de
irreducibilidad permite o no compresión macro detectable.

## Origen de parámetros

- Reglas canónicas: 30 (caos), 90 (sierpinski auto-similar), 110 (universal Class IV), 184 (tráfico Class II).
- Grilla: width=200, n_steps=200, periódica.
- Seed: 42 (fijo).
- Forcing exógeno: gradiente lineal con perturbación senoidal.

## Citas disciplinares

- Wolfram, S. (2002). *A New Kind of Science*. Champaign: Wolfram Media.
- Cook, M. (2004). "Universality in Elementary Cellular Automata". *Complex Systems* 15(1).
- Wolfram, S. (2020). *A Project to Find the Fundamental Theory of Physics*.

## Limitaciones declaradas

EDI agregado negativo confirma que sondas simples NO detectan cierre macro
en autómatas de Wolfram. Esto es **consistente con la posición de
Wolfram** (irreducibilidad), no refutación. La discriminación contra él
opera reconociendo su régimen propio.

Ver `INTERPRETACION_FILOSOFICA.md` para discusión filosófica completa.

## Reproducibilidad mecanizada V5.5

- Seed fijo: `seed=42`
- requirements lock: `09-simulaciones-edi/requirements.txt`
- Pre-registro criptográfico: `SETUP_HASH.json`
- Pipeline reproducible bit-a-bit: `scripts/run_full_pipeline.py`

## Lectura cruzada

- `41_caso_wolfram_extendido/INTERPRETACION_FILOSOFICA.md` — discusión filosófica
- `41_caso_wolfram_extendido/data/FETCH_MANIFEST.json` — trazabilidad
- `41_caso_wolfram_extendido/SETUP_HASH.json` — pre-registro criptográfico
- `41_caso_wolfram_extendido/outputs/metrics.json` — outputs canónicos
- `41_caso_wolfram_extendido/outputs/metrics_enriched_v5_2.json` — calibración V5.2
- `41_caso_wolfram_extendido/NARRATIVA_TESIS_V5_5.md` — conexión con tesis central
