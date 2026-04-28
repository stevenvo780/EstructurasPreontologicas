# Protocolo de simulación — 17_caso_oceanos

## Sonda termohaline con relajación lenta (programático)

**Régimen físico:** Sistema con muy alta inercia. n bajo limita inferencia.

## Ecuación de la sonda

```
dT/dt = ε*(T* - T) + acoplamiento_atmosférico
```

## Motivación física

Circulación termohaline con tiempo de relajación de décadas.

## Origen de parámetros

PMEL/NOAA proxy.

## Citas disciplinares

- Stommel, H. (1961). *Tellus* 13(2).

## Limitaciones declaradas

n=14 insuficiente. Programático.

## Lectura cruzada

- `17_caso_oceanos/data/FETCH_MANIFEST.json` — trazabilidad de datos
- `17_caso_oceanos/SETUP_HASH.json` — pre-registro criptográfico
- `17_caso_oceanos/outputs/metrics.json` — outputs canónicos
- `17_caso_oceanos/outputs/metrics_enriched_v5_2.json` — calibración avanzada V5.2/5.3
