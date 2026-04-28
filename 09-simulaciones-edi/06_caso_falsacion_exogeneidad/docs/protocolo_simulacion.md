# Protocolo de simulación — 06_caso_falsacion_exogeneidad

## Control de falsación: random walk independiente del forcing

**Régimen físico:** Control: el aparato debe rechazar EDI > 0.30 sobre datos sin acoplamiento.

## Ecuación de la sonda

```
X(t+1) = X(t) + ε(t), ε ~ N(0,1)
```

## Motivación física

Hipótesis nula: serie sin acoplamiento causal real al forcing.

## Origen de parámetros

Sintético — diseño anti-falsabilidad.

## Citas disciplinares

- Phipson y Smyth (2010). *Stat. Appl. Genet. Mol. Biol.* 9(1).

## Limitaciones declaradas

NO es caso real; es control para verificar que el aparato no glorifica.

## Lectura cruzada

- `06_caso_falsacion_exogeneidad/data/FETCH_MANIFEST.json` — trazabilidad de datos
- `06_caso_falsacion_exogeneidad/SETUP_HASH.json` — pre-registro criptográfico
- `06_caso_falsacion_exogeneidad/outputs/metrics.json` — outputs canónicos
- `06_caso_falsacion_exogeneidad/outputs/metrics_enriched_v5_2.json` — calibración avanzada V5.2/5.3
