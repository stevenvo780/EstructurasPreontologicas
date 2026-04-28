# Protocolo de simulación — 15_caso_wikipedia

## Sonda de crecimiento de conocimiento con saturación

**Régimen físico:** Sistema saturable de contenido digital.

## Ecuación de la sonda

```
dW/dt = r*W*(1-W/K) (logística pura)
```

## Motivación física

Crecimiento logístico de un repositorio de conocimiento.

## Origen de parámetros

Wikimedia stats serie mensual 2007-2024.

## Citas disciplinares

- Wikimedia Statistics. https://stats.wikimedia.org

## Lectura cruzada

- `15_caso_wikipedia/data/FETCH_MANIFEST.json` — trazabilidad de datos
- `15_caso_wikipedia/SETUP_HASH.json` — pre-registro criptográfico
- `15_caso_wikipedia/outputs/metrics.json` — outputs canónicos
- `15_caso_wikipedia/outputs/metrics_enriched_v5_2.json` — calibración avanzada V5.2/5.3


## Reproducibilidad mecanizada V5.5

- Seed fijo: `seed=42`
- requirements lock: `09-simulaciones-edi/requirements.txt`
- Pre-registro criptográfico: `SETUP_HASH.json`
- Pipeline reproducible bit-a-bit: `scripts/run_full_pipeline.py`
