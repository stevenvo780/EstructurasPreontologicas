# Protocolo de simulación — 05_caso_epidemiologia

## Sonda SIR (Kermack-McKendrick)

**Régimen físico:** Población cerrada, contactos homogéneos, periodo infeccioso fijo.

## Ecuación de la sonda

```
dS/dt = -β*S*I; dI/dt = β*S*I - γ*I; dR/dt = γ*I
```

## Motivación física

Modelo compartimental epidemiológico clásico (Kermack-McKendrick 1927).

## Origen de parámetros

OWID COVID-19 con calibración por país.

## Citas disciplinares

- Kermack, W. O. y McKendrick, A. G. (1927). *Proc. R. Soc. A* 115(772).

## Lectura cruzada

- `05_caso_epidemiologia/data/FETCH_MANIFEST.json` — trazabilidad de datos
- `05_caso_epidemiologia/SETUP_HASH.json` — pre-registro criptográfico
- `05_caso_epidemiologia/outputs/metrics.json` — outputs canónicos
- `05_caso_epidemiologia/outputs/metrics_enriched_v5_2.json` — calibración avanzada V5.2/5.3


## Reproducibilidad mecanizada V5.5

- Seed fijo: `seed=42`
- requirements lock: `09-simulaciones-edi/requirements.txt`
- Pre-registro criptográfico: `SETUP_HASH.json`
- Pipeline reproducible bit-a-bit: `scripts/run_full_pipeline.py`
