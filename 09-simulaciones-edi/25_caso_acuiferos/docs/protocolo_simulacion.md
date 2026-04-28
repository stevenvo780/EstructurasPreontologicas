# Protocolo de simulación — 25_caso_acuiferos

## Sonda de balance acuífero con extracción (programático)

**Régimen físico:** Sistema con stock no-renovable a corto plazo.

## Ecuación de la sonda

```
dV/dt = recarga - extracción - evaporación
```

## Motivación física

Balance hídrico con extracción no-renovable.

## Origen de parámetros

USGS GRACE proxy.

## Citas disciplinares

- Konikow, L. F. y Kendy, E. (2005). *Hydrogeol. J.* 13.

## Limitaciones declaradas

n=19 insuficiente. Programático.

## Lectura cruzada

- `25_caso_acuiferos/data/FETCH_MANIFEST.json` — trazabilidad de datos
- `25_caso_acuiferos/SETUP_HASH.json` — pre-registro criptográfico
- `25_caso_acuiferos/outputs/metrics.json` — outputs canónicos
- `25_caso_acuiferos/outputs/metrics_enriched_v5_2.json` — calibración avanzada V5.2/5.3


## Reproducibilidad mecanizada V5.5

- Seed fijo: `seed=42`
- requirements lock: `09-simulaciones-edi/requirements.txt`
- Pre-registro criptográfico: `SETUP_HASH.json`
- Pipeline reproducible bit-a-bit: `scripts/run_full_pipeline.py`
