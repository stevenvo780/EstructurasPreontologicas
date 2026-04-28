# Protocolo de simulación — 21_caso_salinizacion

## Sonda de balance hídrico-salino (programático)

**Régimen físico:** Sistema lento con feedbacks múltiples.

## Ecuación de la sonda

```
dS/dt = aporte_irrigación - drenaje + evapoconcentración
```

## Motivación física

Balance de masa con evapoconcentración secular.

## Origen de parámetros

World Bank irrigated land + USGS proxy.

## Citas disciplinares

- Ghassemi, F. et al. (1995). *Salinisation of Land and Water*.

## Limitaciones declaradas

Programático.

## Lectura cruzada

- `21_caso_salinizacion/data/FETCH_MANIFEST.json` — trazabilidad de datos
- `21_caso_salinizacion/SETUP_HASH.json` — pre-registro criptográfico
- `21_caso_salinizacion/outputs/metrics.json` — outputs canónicos
- `21_caso_salinizacion/outputs/metrics_enriched_v5_2.json` — calibración avanzada V5.2/5.3
