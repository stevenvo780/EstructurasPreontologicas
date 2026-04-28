# Protocolo de simulación — 03_caso_contaminacion

## Sonda Lotka-Volterra adaptada a contaminación-respuesta

**Régimen físico:** Sistema acoplado emisor-receptor con feedback regulatorio.

## Ecuación de la sonda

```
dC/dt = α*S - β*C*R; dR/dt = -γ*R + δ*C
```

## Motivación física

Acoplamiento depredador-presa adaptado a presión-respuesta (Volterra 1926).

## Origen de parámetros

Calibrado contra series AQICN.

## Citas disciplinares

- Volterra, V. (1926). Variazioni e fluttuazioni. *Mem. Accad. Lincei*.

## Lectura cruzada

- `03_caso_contaminacion/data/FETCH_MANIFEST.json` — trazabilidad de datos
- `03_caso_contaminacion/SETUP_HASH.json` — pre-registro criptográfico
- `03_caso_contaminacion/outputs/metrics.json` — outputs canónicos
- `03_caso_contaminacion/outputs/metrics_enriched_v5_2.json` — calibración avanzada V5.2/5.3
