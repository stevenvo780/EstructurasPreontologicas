# Análisis topológico del corpus EDI (F4)

Métricas estándar para validar carácter atractor de las trayectorias `obs` del corpus:
exponente de Lyapunov máximo (Rosenstein 1993), dimensión de correlación (Grassberger-Procaccia 1983),
tiempo de mezcla (ACF < 1/e). Embedding Takens con dim=5 y τ por primer cero de ACF.

**Casos analizados:** 7 (sólo los que tienen `primary_arrays.json`).

## Tabla resumen

| Caso | n | τ | λ_max (Rosenstein) | r² fit | D₂ (Grass-Proc) | r² scaling | mixing time |
|------|--:|--:|------------------:|------:|---------------:|----------:|------------:|
| 04_caso_energia | 100 | 22 | -0.0014 | 0.004 | 1.38 | 0.996 | 14 |
| 16_caso_deforestacion | 100 | 25 | -0.0224 | 0.693 | 1.65 | 0.988 | 24 |
| 20_caso_kessler | 100 | 18 | 0.0064 | 0.238 | 1.61 | 0.999 | 9 |
| 24_caso_microplasticos | 100 | 14 | 0.0067 | 0.096 | 1.65 | 1.000 | 8 |
| 27_caso_riesgo_biologico | 100 | 25 | -0.0261 | 0.786 | 1.43 | 0.999 | 17 |
| 41_caso_wolfram_extendido | 200 | 2 | 0.0167 | 0.257 | 2.82 | 0.989 | 1 |
| 42_caso_histeresis_institucional | 156 | 20 | -0.0515 | 0.813 | 0.05 | 0.767 | 13 |

## Lectura

1. **λ_max > 0** indica sensibilidad a condiciones iniciales (caos determinista) — compatible con atractor extraño.
2. **λ_max ≈ 0** indica régimen marginal o cuasi-periódico — compatible con atractor en el borde del caos.
3. **λ_max < 0** indica convergencia a punto fijo o ciclo límite — compatible con atractor convergente.
4. **D₂ no entera** (ej. 2.4) es firma de atractor fractal/extraño.
5. **r² alto** del fit log-log (D₂) o lineal (λ) indica que la métrica es interpretable; r² bajo indica que la serie no admite tratamiento topológico estándar.

## Limitaciones declaradas

- Con n ≤ 200 puntos las estimaciones son **indicativas, no concluyentes**.
- Rosenstein supone que los pares cercanos divergen exponencialmente al menos en una ventana inicial.
- Grassberger-Procaccia es sensible al ruido aditivo: D₂ inflada si el ruido domina sobre la dinámica determinista.
- La correspondencia entre estas métricas y el concepto operativo de "atractor empírico" del cap 02-01 §2.2 es **necesaria pero no suficiente**: una serie con λ_max > 0 admite tratamiento topológico, pero el dossier de anclaje exige además identificación material y especificación dinámica.

## Trazabilidad

- Generado por: `scripts/run_topology_analysis.py`
- Implementación: `09-simulaciones-edi/common/topology.py`
- Fuente de datos: `09-simulaciones-edi/<caso>/outputs/primary_arrays.json` (campo `arrays.obs`)
