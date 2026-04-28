# Protocolo de simulación — 19_caso_acidificacion_oceanica

## Sonda de equilibrio carbonato-bicarbonato (programático)

**Régimen físico:** Equilibrio químico oceano-atmosfera lento.

## Ecuación de la sonda

```
[H+] ↔ [HCO3-] + CO2_atmosférico
```

## Motivación física

Equilibrio químico carbonato con perturbación atmosférica.

## Origen de parámetros

PMEL pH proxy.

## Citas disciplinares

- Caldeira, K. y Wickett, M. E. (2003). *Nature* 425.

## Limitaciones declaradas

n=11 insuficiente. Programático.

## Lectura cruzada

- `19_caso_acidificacion_oceanica/data/FETCH_MANIFEST.json` — trazabilidad de datos
- `19_caso_acidificacion_oceanica/SETUP_HASH.json` — pre-registro criptográfico
- `19_caso_acidificacion_oceanica/outputs/metrics.json` — outputs canónicos
- `19_caso_acidificacion_oceanica/outputs/metrics_enriched_v5_2.json` — calibración avanzada V5.2/5.3


## Reproducibilidad mecanizada V5.5

- Seed fijo: `seed=42`
- requirements lock: `09-simulaciones-edi/requirements.txt`
- Pre-registro criptográfico: `SETUP_HASH.json`
- Pipeline reproducible bit-a-bit: `scripts/run_full_pipeline.py`
