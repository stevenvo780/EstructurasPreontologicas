# Pre-Registro B-T2.1 — Caso 26 Starlink Block-Permutation Post-Fix

**Fecha:** 2026-05-17
**Caso:** 26_caso_starlink (Constelaciones Satelitales LEO)
**Investigadores:** Jacob Agudelo, Steven Vallejo
**Protocolo:** Block-permutation (permutación temporal respetando autocorrelación)

## Antecedentes

- **Iteración 12 (Canonical permutation):** EDI=0.5127, p_perm=0.079 (Weak, umbral 0.05)
- **Status actual:** Caso sobreviviente único candidato a Strong post-cierre de loop
- **Riesgo:**  Permutación canonical asumió independencia temporal. Autocorrelación en lanzamientos Starlink (planificación por campañas) puede invalidar p-value.

## Predicción Previa

Bajo block-permutation (respeta bloques temporales):

| Hipótesis | Predicción | Confianza | Justificación |
|-----------|-----------|-----------|-----------|
| **P(EDI↓ < 0.05)** | **Null** (p > 0.05) | 55% | Autocorrelación intra-campaña absorbe varianza; permutación naive sobre-infló significancia. |
| **P(EDI↓ ≥ 0.05, < 0.10)** | **Weak** (0.05–0.10) | 35% | Si bloque subsana pero EDI degrada, p_perm marginal. Robustez limitada. |
| **P(EDI↓ ≥ 0.10)** | **Strong** (p < 0.05) | 10% | Improbable dado datos SATCAT. Implicaría acoplamiento ODE robusto post-block. |

## Configuración Ejecución

```bash
cd /datos/repos/EstructurasPreontologicas/09-simulaciones-edi/26_caso_starlink/src
HYPER_PERMUTATION_METHOD=block \
  HYPER_N_PERM=999 \
  HYPER_N_BOOT=500 \
  timeout 1800 python3 validate.py --seed 42
```

## Datos

- **Fuente:** CelesTrak SATCAT (fetch realizado 2026-05-17)
- **Ventana:** 2019-01-01 a 2024-06-01 (mismo que iter 12)
- **Drivers:** `launches`, `debris_new` (exógeno real)

## Aceptancia

- **Criterio Strong:** p_perm ≤ 0.05, EDI ≥ 0.40
- **Criterio Weak:** 0.05 < p_perm ≤ 0.10, EDI ≥ 0.30
- **Criterio Null:** p_perm > 0.10 o EDI < 0.30
- **Corpus decision:** Si Null → Caso 26 removido; corpus termina sin Strong-robustos post-cierre.

## Registro

Ejecutado por: Claude Code (Orquestador)
Hashes baseline: pre-calculated via SETUP_HASH.json
