# Protocolo de simulación — 18_caso_urbanizacion

## Sonda de migración rural-urbana con saturación

**Régimen físico:** Sistema de flujo migratorio con saturación.

## Ecuación de la sonda

```
dU/dt = α*R*incentivo - β*U*saturación
```

## Motivación física

Modelo de Harris-Todaro (1970) con saturación urbana.

## Origen de parámetros

World Bank urban population annual 1960-2022.

## Citas disciplinares

- Harris, J. R. y Todaro, M. P. (1970). *Am. Econ. Rev.* 60.

## Lectura cruzada

- `18_caso_urbanizacion/data/FETCH_MANIFEST.json` — trazabilidad de datos
- `18_caso_urbanizacion/SETUP_HASH.json` — pre-registro criptográfico
- `18_caso_urbanizacion/outputs/metrics.json` — outputs canónicos
- `18_caso_urbanizacion/outputs/metrics_enriched_v5_2.json` — calibración avanzada V5.2/5.3


## Reproducibilidad mecanizada V5.5

- Seed fijo: `seed=42`
- requirements lock: `09-simulaciones-edi/requirements.txt`
- Pre-registro criptográfico: `SETUP_HASH.json`
- Pipeline reproducible bit-a-bit: `scripts/run_full_pipeline.py`
