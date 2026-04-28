# Protocolo de simulación — 11_caso_movilidad

## Sonda de movilidad urbana con saturación logística

**Régimen físico:** Sistema vehículo-infraestructura con saturación.

## Ecuación de la sonda

```
dM/dt = r*M*(1-M/K) - costo_congestión*M^2
```

## Motivación física

Crecimiento logístico con saturación por congestión.

## Origen de parámetros

World Bank vehicle ownership + road density.

## Citas disciplinares

- World Bank Urban Mobility Indicators.

## Lectura cruzada

- `11_caso_movilidad/data/FETCH_MANIFEST.json` — trazabilidad de datos
- `11_caso_movilidad/SETUP_HASH.json` — pre-registro criptográfico
- `11_caso_movilidad/outputs/metrics.json` — outputs canónicos
- `11_caso_movilidad/outputs/metrics_enriched_v5_2.json` — calibración avanzada V5.2/5.3
