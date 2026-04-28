# Protocolo de simulación — 28_caso_fuga_cerebros

## Sonda de migración selectiva (programático)

**Régimen físico:** Sistema migratorio selectivo con net flow.

## Ecuación de la sonda

```
dB/dt = -tasa_migración*incentivo + retorno
```

## Motivación física

Modelo Docquier-Rapoport (2012).

## Origen de parámetros

World Bank net migration tertiary.

## Citas disciplinares

- Docquier, F. y Rapoport, H. (2012). *J. Econ. Lit.* 50(3).

## Limitaciones declaradas

n=18 insuficiente. Programático.

## Lectura cruzada

- `28_caso_fuga_cerebros/data/FETCH_MANIFEST.json` — trazabilidad de datos
- `28_caso_fuga_cerebros/SETUP_HASH.json` — pre-registro criptográfico
- `28_caso_fuga_cerebros/outputs/metrics.json` — outputs canónicos
- `28_caso_fuga_cerebros/outputs/metrics_enriched_v5_2.json` — calibración avanzada V5.2/5.3


## Reproducibilidad mecanizada V5.5

- Seed fijo: `seed=42`
- requirements lock: `09-simulaciones-edi/requirements.txt`
- Pre-registro criptográfico: `SETUP_HASH.json`
- Pipeline reproducible bit-a-bit: `scripts/run_full_pipeline.py`
