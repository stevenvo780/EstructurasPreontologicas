# Protocolo de simulación — 40_cumulos_globulares

## Sonda Plummer para cúmulos globulares

**Régimen físico:** Sistema gravitacionalmente ligado en equilibrio.

## Ecuación de la sonda

```
ρ(r) = (3M/4π/a^3)*(1+r^2/a^2)^(-5/2)
```

## Motivación física

Modelo de Plummer (1911) para sistemas estelares.

## Origen de parámetros

Gaia DR3 GC parameters.

## Citas disciplinares

- Plummer, H. C. (1911). *MNRAS* 71.

## Lectura cruzada

- `40_cumulos_globulares/data/FETCH_MANIFEST.json` — trazabilidad de datos
- `40_cumulos_globulares/SETUP_HASH.json` — pre-registro criptográfico
- `40_cumulos_globulares/outputs/metrics.json` — outputs canónicos
- `40_cumulos_globulares/outputs/metrics_enriched_v5_2.json` — calibración avanzada V5.2/5.3


## Reproducibilidad mecanizada V5.5

- Seed fijo: `seed=42`
- requirements lock: `09-simulaciones-edi/requirements.txt`
- Pre-registro criptográfico: `SETUP_HASH.json`
- Pipeline reproducible bit-a-bit: `scripts/run_full_pipeline.py`
