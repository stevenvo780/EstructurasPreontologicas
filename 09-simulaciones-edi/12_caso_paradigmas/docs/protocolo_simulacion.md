# Protocolo de simulación — 12_caso_paradigmas

## Sonda de transición de paradigmas (programático)

**Régimen físico:** Programático: paradigmas con observable indirecto vía proxy bibliográfico.

## Ecuación de la sonda

```
Sistema biestable: dP/dt = -dV/dP, V con doble pozo
```

## Motivación física

Transición de fase orden-desorden en agregados de creencias.

## Origen de parámetros

OWID educación + Google Scholar trends.

## Citas disciplinares

- Kuhn, T. (1962). *Structure of Scientific Revolutions*.

## Limitaciones declaradas

Observable indirecto. Programático.

## Lectura cruzada

- `12_caso_paradigmas/data/FETCH_MANIFEST.json` — trazabilidad de datos
- `12_caso_paradigmas/SETUP_HASH.json` — pre-registro criptográfico
- `12_caso_paradigmas/outputs/metrics.json` — outputs canónicos
- `12_caso_paradigmas/outputs/metrics_enriched_v5_2.json` — calibración avanzada V5.2/5.3


## Reproducibilidad mecanizada V5.5

- Seed fijo: `seed=42`
- requirements lock: `09-simulaciones-edi/requirements.txt`
- Pre-registro criptográfico: `SETUP_HASH.json`
- Pipeline reproducible bit-a-bit: `scripts/run_full_pipeline.py`
