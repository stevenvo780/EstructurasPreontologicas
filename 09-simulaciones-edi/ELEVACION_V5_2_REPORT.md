# Elevación masiva V5.2 — casos débiles del corpus

Aplicación de las cinco capas V5.1 (calibración avanzada, replicación robusta, pre-registro criptográfico, sensibilidad a umbrales, sondas independientes) a los 14 casos del corpus inter-dominio que NO son invariantemente strong ni invariantemente null.

## Síntesis

- **Total casos elevados:** 14
- **Elevados a ROBUSTO** (invariante + p_block sig + sobrevive FWER): 1
- **Elevados PARCIALMENTE** (invariante + p_block sig pero no sobrevive FWER): 1
- **CONFIRMADOS MARGINAL** post-calibración: 3
- **SENSIBLES a umbrales** (declarados como casos de borde): 6
- **CONFIRMADOS NULL** post-calibración: 0

## Tabla por caso

| Caso | EDI | p_naive | p_block | SE HAC | p_Holm | Inv? | Lvl Inv | Veredicto |
|------|----:|---------:|---------:|--------:|--------:|:----:|---------|-----------|
| 01_caso_clima | +0.011 | 0.9990 | 0.0003 | 0.0121 | 1.0000 | ✓ | suggestive | **REQUIERE EVALUACIÓN ESPECÍFICA** |
| 06_caso_falsacion_exogeneidad | +0.055 | 1.0000 | 0.3873 | 0.0153 | 1.0000 | ✗ | — | **CONFIRMADO COMO MARGINAL** |
| 09_caso_finanzas | +0.081 | 0.0000 | 0.0103 | 0.0038 | 0.0000 | ✗ | — | **SENSIBLE A UMBRALES** |
| 10_caso_justicia | +0.227 | 0.4775 | 1.0000 | 0.0606 | 1.0000 | ✗ | — | **CONFIRMADO COMO MARGINAL** |
| 11_caso_movilidad | +0.128 | 0.0020 | 0.0003 | 0.1244 | 0.0340 | ✗ | — | **SENSIBLE A UMBRALES** |
| 13_caso_politicas_estrategicas | +0.297 | 0.0015 | 0.0010 | 0.0272 | 0.0270 | ✗ | — | **SENSIBLE A UMBRALES** |
| 14_caso_postverdad | +0.243 | 0.0000 | 0.0003 | 0.0721 | 0.0000 | ✗ | — | **SENSIBLE A UMBRALES** |
| 15_caso_wikipedia | +0.192 | 0.0000 | 0.0003 | 0.1488 | 0.0000 | ✓ | weak | **ELEVADO A ROBUSTO** |
| 20_caso_kessler | +0.353 | 0.0000 | 0.0003 | 0.0809 | 0.0000 | ✗ | — | **SENSIBLE A UMBRALES** |
| 21_caso_salinizacion | +0.018 | 0.0028 | 0.0003 | 0.0611 | 0.0420 | ✓ | suggestive | **REQUIERE EVALUACIÓN ESPECÍFICA** |
| 26_caso_starlink | +0.689 | 1.0000 | 0.0010 | 0.0038 | 1.0000 | ✓ | strong | **ELEVADO PARCIALMENTE** |
| 27_caso_riesgo_biologico | +0.333 | 0.0022 | 0.0003 | 0.3237 | 0.0352 | ✗ | — | **SENSIBLE A UMBRALES** |
| 28_caso_fuga_cerebros | +0.025 | 0.9975 | 0.0010 | 0.1306 | 1.0000 | ✓ | suggestive | **REQUIERE EVALUACIÓN ESPECÍFICA** |
| 30_caso_behavioral_dynamics | +0.262 | 0.0440 | 0.9783 | 0.0116 | 0.6166 | ✗ | — | **CONFIRMADO COMO MARGINAL** |

## Lectura

Esta elevación NO modifica los outputs canónicos. Cada caso recibe un `metrics_enriched_v5_2.json` paralelo con la calibración avanzada aplicada sobre los datos derivables del `metrics.json` canónico.

**Veredictos posibles:**

- **ELEVADO A ROBUSTO:** caso pasa de borde/débil a robusto bajo régimen V5.1 calibrado. La afirmación inferencial se sostiene tras corrección por autocorrelación + comparaciones múltiples.
- **ELEVADO PARCIALMENTE:** significancia individual robusta tras calibración pero NO sobrevive FWER del corpus completo. Honestidad: el caso aporta señal pero la familia colectiva requiere atención.
- **CONFIRMADO MARGINAL:** post-calibración, p_block > 0.10. El caso debe declararse como no significativo bajo el régimen calibrado.
- **SENSIBLE A UMBRALES:** clasificación canónica era variable según umbrales; permanece sensible. Reportar como caso de borde explícitamente.
- **CONFIRMADO NULL post-calibración:** caso era trend/suggestive marginal; bajo régimen calibrado se confirma como honestamente null.

## Limitación reconocida

Las estimaciones de `p_block`, `SE Newey-West` y `seed_robustness` son DERIVADAS del `metrics.json` publicado (que no expone los arrays obs/abm/forcing). La verificación definitiva requiere re-ejecutar el corpus con dump de arrays habilitado. Esto es deuda metodológica fechada de 2-3 semanas pre-depósito, no deuda externa.

## Lectura cruzada

- `Anexos/A0-limitaciones-declaradas.md` — limitaciones declaradas con estado V5.1/V5.2.
- `09-simulaciones-edi/REFUERZOS_V5_1.md` — los cinco bloques V5.1 en detalle.
- `09-simulaciones-edi/<case>/outputs/metrics_enriched_v5_2.json` — enriquecimiento por caso.