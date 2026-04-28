# Protocolo de simulación — 04_caso_energia

## Sonda Lotka-Volterra ecológica + Maxwell-Boltzmann termodinámica

**Régimen físico:** Sistema acoplado oferta-demanda con conservación de masa energética.

## Ecuación de la sonda

```
dE/dt = r*E*(1-E/K) + acoplamiento_demanda
```

## Motivación física

Lotka-Volterra ecológica (consumo agregado como recurso); Maxwell-Boltzmann termodinámica (sonda secundaria B4).

## Origen de parámetros

OPSD para series reales 2010-2020.

## Citas disciplinares

- Volterra (1926).
- Maxwell, J. C. (1860). *Phil. Mag.* 19.

## Lectura cruzada

- `04_caso_energia/data/FETCH_MANIFEST.json` — trazabilidad de datos
- `04_caso_energia/SETUP_HASH.json` — pre-registro criptográfico
- `04_caso_energia/outputs/metrics.json` — outputs canónicos
- `04_caso_energia/outputs/metrics_enriched_v5_2.json` — calibración avanzada V5.2/5.3


## Reproducibilidad mecanizada V5.5

- Seed fijo: `seed=42`
- requirements lock: `09-simulaciones-edi/requirements.txt`
- Pre-registro criptográfico: `SETUP_HASH.json`
- Pipeline reproducible bit-a-bit: `scripts/run_full_pipeline.py`
