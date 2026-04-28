# Protocolo de simulación — 10_caso_justicia

## Sonda institucional con histéresis (programático)

**Régimen físico:** Sistema institucional formal con inercia y respuesta a perturbaciones.

## Ecuación de la sonda

```
dJ/dt = α*(J* - J) + β*Δ_perturbación
```

## Motivación física

Sistema institucional con relajación a estado de equilibrio.

## Origen de parámetros

World Bank governance indicators.

## Citas disciplinares

- North, D. C. (1990). *Institutions, Institutional Change*.

## Limitaciones declaradas

Programático. Datos cortos por país.

## Lectura cruzada

- `10_caso_justicia/data/FETCH_MANIFEST.json` — trazabilidad de datos
- `10_caso_justicia/SETUP_HASH.json` — pre-registro criptográfico
- `10_caso_justicia/outputs/metrics.json` — outputs canónicos
- `10_caso_justicia/outputs/metrics_enriched_v5_2.json` — calibración avanzada V5.2/5.3
