# Protocolo de simulación — 14_caso_postverdad

## Sonda de viralidad con saturación informacional

**Régimen físico:** Difusión viral con población saturable.

## Ecuación de la sonda

```
dV/dt = β*V*(1-V/K) - γ*V (epidemia informacional)
```

## Motivación física

Modelo SIR adaptado a difusión de información (Daley-Kendall 1965).

## Origen de parámetros

Google Trends + Wikipedia stats.

## Citas disciplinares

- Daley, D. J. y Kendall, D. G. (1965). *Stochastic rumors*. JIMA 1.

## Limitaciones declaradas

n bajo por ventana corta. Programático.

## Lectura cruzada

- `14_caso_postverdad/data/FETCH_MANIFEST.json` — trazabilidad de datos
- `14_caso_postverdad/SETUP_HASH.json` — pre-registro criptográfico
- `14_caso_postverdad/outputs/metrics.json` — outputs canónicos
- `14_caso_postverdad/outputs/metrics_enriched_v5_2.json` — calibración avanzada V5.2/5.3
