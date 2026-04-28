# Protocolo de simulación — 09_caso_finanzas

## Sonda Soros-Taleb reflexividad-antifragilidad

**Régimen físico:** Mercado financiero con feedback opinión-precio.

## Ecuación de la sonda

```
dP/dt = drift + vol*W + reflexividad(opinión)
```

## Motivación física

Reflexividad de Soros (1987) + antifragilidad de Taleb (2012).

## Origen de parámetros

Yahoo Finance series diarias 2018-2023.

## Citas disciplinares

- Soros, G. (1987). *The Alchemy of Finance*.
- Taleb, N. N. (2012). *Antifragile*.

## Lectura cruzada

- `09_caso_finanzas/data/FETCH_MANIFEST.json` — trazabilidad de datos
- `09_caso_finanzas/SETUP_HASH.json` — pre-registro criptográfico
- `09_caso_finanzas/outputs/metrics.json` — outputs canónicos
- `09_caso_finanzas/outputs/metrics_enriched_v5_2.json` — calibración avanzada V5.2/5.3
