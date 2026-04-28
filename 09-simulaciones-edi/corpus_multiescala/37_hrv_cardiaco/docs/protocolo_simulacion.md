# Protocolo de simulación — 37_hrv_cardiaco

## Sonda Mackey-Glass para HRV

**Régimen físico:** Variabilidad cardíaca con feedback retrasado.

## Ecuación de la sonda

```
dx/dt = β*x(t-τ)/(1+x(t-τ)^n) - γ*x
```

## Motivación física

Sistema con retraso (Mackey-Glass 1977).

## Origen de parámetros

PhysioNet HRV typical.

## Citas disciplinares

- Mackey, M. C. y Glass, L. (1977). *Science* 197(4300).

## Lectura cruzada

- `37_hrv_cardiaco/data/FETCH_MANIFEST.json` — trazabilidad de datos
- `37_hrv_cardiaco/SETUP_HASH.json` — pre-registro criptográfico
- `37_hrv_cardiaco/outputs/metrics.json` — outputs canónicos
- `37_hrv_cardiaco/outputs/metrics_enriched_v5_2.json` — calibración avanzada V5.2/5.3


## Reproducibilidad mecanizada V5.5

- Seed fijo: `seed=42`
- requirements lock: `09-simulaciones-edi/requirements.txt`
- Pre-registro criptográfico: `SETUP_HASH.json`
- Pipeline reproducible bit-a-bit: `scripts/run_full_pipeline.py`
