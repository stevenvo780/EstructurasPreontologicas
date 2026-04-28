# Protocolo de simulación — 34_michaelis_menten

## Sonda Michaelis-Menten enzimática

**Régimen físico:** Enzima-sustrato en estado pseudo-estacionario.

## Ecuación de la sonda

```
v = V_max*S/(K_m + S)
```

## Motivación física

Cinética enzimática clásica (Michaelis-Menten 1913).

## Origen de parámetros

Parámetros BRENDA.

## Citas disciplinares

- Michaelis, L. y Menten, M. L. (1913). *Biochem. Z.* 49.

## Lectura cruzada

- `34_michaelis_menten/data/FETCH_MANIFEST.json` — trazabilidad de datos
- `34_michaelis_menten/SETUP_HASH.json` — pre-registro criptográfico
- `34_michaelis_menten/outputs/metrics.json` — outputs canónicos
- `34_michaelis_menten/outputs/metrics_enriched_v5_2.json` — calibración avanzada V5.2/5.3


## Reproducibilidad mecanizada V5.5

- Seed fijo: `seed=42`
- requirements lock: `09-simulaciones-edi/requirements.txt`
- Pre-registro criptográfico: `SETUP_HASH.json`
- Pipeline reproducible bit-a-bit: `scripts/run_full_pipeline.py`
