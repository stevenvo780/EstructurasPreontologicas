# Protocolo de simulación — 13_caso_politicas_estrategicas

## Sonda de respuesta institucional con histéresis

**Régimen físico:** Sistema con saltos discretos por umbrales.

## Ecuación de la sonda

```
dS/dt = α*(perturbación) - β*S^3 (pozo de potencial)
```

## Motivación física

Catastrophe theory de Zeeman para decisiones discretas.

## Origen de parámetros

World Bank policy indicators.

## Citas disciplinares

- Zeeman, E. C. (1977). *Catastrophe Theory*.

## Lectura cruzada

- `13_caso_politicas_estrategicas/data/FETCH_MANIFEST.json` — trazabilidad de datos
- `13_caso_politicas_estrategicas/SETUP_HASH.json` — pre-registro criptográfico
- `13_caso_politicas_estrategicas/outputs/metrics.json` — outputs canónicos
- `13_caso_politicas_estrategicas/outputs/metrics_enriched_v5_2.json` — calibración avanzada V5.2/5.3


## Reproducibilidad mecanizada V5.5

- Seed fijo: `seed=42`
- requirements lock: `09-simulaciones-edi/requirements.txt`
- Pre-registro criptográfico: `SETUP_HASH.json`
- Pipeline reproducible bit-a-bit: `scripts/run_full_pipeline.py`
