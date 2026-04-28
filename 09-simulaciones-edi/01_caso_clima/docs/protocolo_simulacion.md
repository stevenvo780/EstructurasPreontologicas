# Protocolo de simulación — 01_caso_clima

## Sonda Budyko-Sellers para temperatura global

**Régimen físico:** Sistema acoplado atmósfera-superficie con feedback de albedo.

## Ecuación de la sonda

```
dT/dt = (1/C) * [Q*(1-α(T)) - σ*T^4 - feedbacks]
```

## Motivación física

Balance energético planetario (Budyko 1969, Sellers 1969).

## Origen de parámetros

Parámetros canónicos de Budyko-Sellers (1969) actualizados con IPCC AR6.

## Citas disciplinares

- Budyko, M. I. (1969). The Effect of Solar Radiation Variations. *Tellus* 21(5).
- Sellers, W. D. (1969). A Global Climatic Model. *J. Appl. Meteorol.* 8(3).

## Lectura cruzada

- `01_caso_clima/data/FETCH_MANIFEST.json` — trazabilidad de datos
- `01_caso_clima/SETUP_HASH.json` — pre-registro criptográfico
- `01_caso_clima/outputs/metrics.json` — outputs canónicos
- `01_caso_clima/outputs/metrics_enriched_v5_2.json` — calibración avanzada V5.2/5.3


## Reproducibilidad mecanizada V5.5

- Seed fijo: `seed=42`
- requirements lock: `09-simulaciones-edi/requirements.txt`
- Pre-registro criptográfico: `SETUP_HASH.json`
- Pipeline reproducible bit-a-bit: `scripts/run_full_pipeline.py`
