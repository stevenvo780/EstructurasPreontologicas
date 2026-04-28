# Protocolo de simulación — 07_caso_falsacion_no_estacionariedad

## Control de falsación: random walk con drift no-estacionario

**Régimen físico:** Control de falsación. El aparato debe rechazar.

## Ecuación de la sonda

```
X(t+1) = X(t) + drift + ε(t)
```

## Motivación física

Hipótesis nula: tendencia espuria sin acoplamiento estructural.

## Origen de parámetros

Sintético.

## Citas disciplinares

- Phipson y Smyth (2010).

## Limitaciones declaradas

Control de falsabilidad.

## Lectura cruzada

- `07_caso_falsacion_no_estacionariedad/data/FETCH_MANIFEST.json` — trazabilidad de datos
- `07_caso_falsacion_no_estacionariedad/SETUP_HASH.json` — pre-registro criptográfico
- `07_caso_falsacion_no_estacionariedad/outputs/metrics.json` — outputs canónicos
- `07_caso_falsacion_no_estacionariedad/outputs/metrics_enriched_v5_2.json` — calibración avanzada V5.2/5.3


## Reproducibilidad mecanizada V5.5

- Seed fijo: `seed=42`
- requirements lock: `09-simulaciones-edi/requirements.txt`
- Pre-registro criptográfico: `SETUP_HASH.json`
- Pipeline reproducible bit-a-bit: `scripts/run_full_pipeline.py`
