# Protocolo de simulación — 27_caso_riesgo_biologico

## Sonda SIR + Zeeman cusp (B4)

**Régimen físico:** Sistema biológico-poblacional con saltos posibles.

## Ecuación de la sonda

```
Primaria: SIR; Secundaria (B4): catástrofe cusp.
```

## Motivación física

Compartimental epidemiológico + topología catastrófica.

## Origen de parámetros

WHO mortality + World Bank.

## Citas disciplinares

- Kermack-McKendrick (1927).
- Zeeman (1977).

## Lectura cruzada

- `27_caso_riesgo_biologico/data/FETCH_MANIFEST.json` — trazabilidad de datos
- `27_caso_riesgo_biologico/SETUP_HASH.json` — pre-registro criptográfico
- `27_caso_riesgo_biologico/outputs/metrics.json` — outputs canónicos
- `27_caso_riesgo_biologico/outputs/metrics_enriched_v5_2.json` — calibración avanzada V5.2/5.3


## Reproducibilidad mecanizada V5.5

- Seed fijo: `seed=42`
- requirements lock: `09-simulaciones-edi/requirements.txt`
- Pre-registro criptográfico: `SETUP_HASH.json`
- Pipeline reproducible bit-a-bit: `scripts/run_full_pipeline.py`
