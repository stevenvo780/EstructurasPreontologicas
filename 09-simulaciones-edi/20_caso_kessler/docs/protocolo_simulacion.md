# Protocolo de simulación — 20_caso_kessler

## Sonda de Kessler para basura espacial

**Régimen físico:** Sistema con feedback cuadrático.

## Ecuación de la sonda

```
dN/dt = α*N - β*N² (cascada cuadrática)
```

## Motivación física

Cascada de colisiones cuadrática (Kessler 1978).

## Origen de parámetros

CelesTrak debris counts annual 2000-2024.

## Citas disciplinares

- Kessler, D. J. y Cour-Palais, B. G. (1978). *J. Geophys. Res.* 83(A6).

## Lectura cruzada

- `20_caso_kessler/data/FETCH_MANIFEST.json` — trazabilidad de datos
- `20_caso_kessler/SETUP_HASH.json` — pre-registro criptográfico
- `20_caso_kessler/outputs/metrics.json` — outputs canónicos
- `20_caso_kessler/outputs/metrics_enriched_v5_2.json` — calibración avanzada V5.2/5.3


## Reproducibilidad mecanizada V5.5

- Seed fijo: `seed=42`
- requirements lock: `09-simulaciones-edi/requirements.txt`
- Pre-registro criptográfico: `SETUP_HASH.json`
- Pipeline reproducible bit-a-bit: `scripts/run_full_pipeline.py`
