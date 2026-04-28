# Protocolo de simulación — 29_caso_iot

## Sonda de adopción tecnológica con saturación (programático)

**Régimen físico:** Adopción saturable con obsolescencia.

## Ecuación de la sonda

```
dN/dt = β*N*(1-N/K) - obsolescencia
```

## Motivación física

Modelo de Bass adaptado a dispositivos IoT.

## Origen de parámetros

ITU + Statista IoT proxy.

## Citas disciplinares

- Bass, F. M. (1969). *Manage. Sci.* 15(5).

## Limitaciones declaradas

Programático por proxy.

## Lectura cruzada

- `29_caso_iot/data/FETCH_MANIFEST.json` — trazabilidad de datos
- `29_caso_iot/SETUP_HASH.json` — pre-registro criptográfico
- `29_caso_iot/outputs/metrics.json` — outputs canónicos
- `29_caso_iot/outputs/metrics_enriched_v5_2.json` — calibración avanzada V5.2/5.3
