# Protocolo de simulación — 22_caso_fosforo

## Sonda de eutrofización (Carpenter 2005)

**Régimen físico:** Sistema biestable con histéresis.

## Ecuación de la sonda

```
dP/dt = entrada - sedimentación + reciclaje*hysteresis
```

## Motivación física

Bistabilidad por hysteresis de fósforo en lagos.

## Origen de parámetros

World Bank fertilizer use.

## Citas disciplinares

- Carpenter, S. R. (2005). *PNAS* 102(29).

## Lectura cruzada

- `22_caso_fosforo/data/FETCH_MANIFEST.json` — trazabilidad de datos
- `22_caso_fosforo/SETUP_HASH.json` — pre-registro criptográfico
- `22_caso_fosforo/outputs/metrics.json` — outputs canónicos
- `22_caso_fosforo/outputs/metrics_enriched_v5_2.json` — calibración avanzada V5.2/5.3


## Reproducibilidad mecanizada V5.5

- Seed fijo: `seed=42`
- requirements lock: `09-simulaciones-edi/requirements.txt`
- Pre-registro criptográfico: `SETUP_HASH.json`
- Pipeline reproducible bit-a-bit: `scripts/run_full_pipeline.py`
