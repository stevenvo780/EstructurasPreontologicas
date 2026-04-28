# Protocolo de simulación — 26_caso_starlink

## Sonda exploratoria de constelación LEO

**Régimen físico:** Sistema dominado por planificación humana exógena.

## Ecuación de la sonda

```
dN/dt = lanzamiento_planificado - desorbita - Kessler_local
```

## Motivación física

Crecimiento exógeno con feedback de colisiones.

## Origen de parámetros

CelesTrak Starlink launches 2019-2024.

## Citas disciplinares

- Kessler (1978).
- CelesTrak.

## Limitaciones declaradas

n=1 (caso exploratorio extremo). Solo apto para tendencia.

## Lectura cruzada

- `26_caso_starlink/data/FETCH_MANIFEST.json` — trazabilidad de datos
- `26_caso_starlink/SETUP_HASH.json` — pre-registro criptográfico
- `26_caso_starlink/outputs/metrics.json` — outputs canónicos
- `26_caso_starlink/outputs/metrics_enriched_v5_2.json` — calibración avanzada V5.2/5.3
