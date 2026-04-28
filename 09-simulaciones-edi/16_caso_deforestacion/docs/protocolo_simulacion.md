# Protocolo de simulación — 16_caso_deforestacion

## Sonda von Thünen + Fisher-KPP

**Régimen físico:** Sistema espacial con frente de avance.

## Ecuación de la sonda

```
Primaria: dF/dt = -α*F*demanda; Secundaria (B4): u_t = D*∇²u + r*u(1-u/K)
```

## Motivación física

von Thünen (1826) económico-espacial; Fisher-KPP (1937) difusión reactiva.

## Origen de parámetros

World Bank forest area annual 1990-2022.

## Citas disciplinares

- von Thünen, J. H. (1826).
- Fisher (1937), Kolmogorov-Petrovsky-Piskunov (1937).

## Lectura cruzada

- `16_caso_deforestacion/data/FETCH_MANIFEST.json` — trazabilidad de datos
- `16_caso_deforestacion/SETUP_HASH.json` — pre-registro criptográfico
- `16_caso_deforestacion/outputs/metrics.json` — outputs canónicos
- `16_caso_deforestacion/outputs/metrics_enriched_v5_2.json` — calibración avanzada V5.2/5.3


## Reproducibilidad mecanizada V5.5

- Seed fijo: `seed=42`
- requirements lock: `09-simulaciones-edi/requirements.txt`
- Pre-registro criptográfico: `SETUP_HASH.json`
- Pipeline reproducible bit-a-bit: `scripts/run_full_pipeline.py`
