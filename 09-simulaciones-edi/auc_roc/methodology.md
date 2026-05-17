# Metodología del AUC-ROC = 0.886 sobre el corpus inter-dominio

**Versión:** 2026-05-11
**Origen del cómputo numérico canónico:** `Bitacora/2026-04-28-cierre-severo/N3_auc_roc_discriminacion.py` (script primario) y `N3_resultados.json` (output).
**Estado del documento:** primer documento canónico bajo `09-simulaciones-edi/auc_roc/` que cumple CLAUDE.md §4 (cifra reportada con comando regenerador). Hasta este documento, la cifra 0.886 circulaba en `06-cierre/01-conclusion-demostrativa.md` sin path canónico.

---

## 1. Qué mide esta cifra (alcance honesto)

**Outcome operativo:** coherencia interna del umbral EDI sobre el corpus inter-dominio de 12 casos. Mide cuántas inversiones de ranking existen entre el umbral declarado a priori (EDI ≥ 0.33 → `label_strong = 1`) y la clasificación final del corpus tras gate completo + C1-C5 + hostile testing.

**Outcome que NO mide:** discriminación contra un baseline rival externo. La AUC se computa con el mismo EDI como **score** y como **etiqueta** (vía umbral 0.33), por lo que es estructuralmente un test de **consistencia umbral**, no de validez externa. La cifra `AUC-ROC = 0.886` no certifica que el aparato discrimine mejor que ARIMA, mejor que cualquier baseline, ni mejor que la asignación de etiquetas por un especialista de dominio sin acceso al EDI.

**Lectura correcta:** una AUC < 1.0 indica inconsistencia residual entre el umbral 0.33 y la clasificación final. En este corpus la inconsistencia viene del caso `26_starlink` (EDI = 0.6892, clasificado null por gate=false pese al EDI alto), lo que introduce inversiones de ranking sobre los pares strong-vs-null. Eso es exactamente lo que la cifra mide: **inconsistencia residual entre el umbral 0.33 y la clasificación operativa del corpus**.

## 2. Datos primarios (12 casos)

Lectura literal de `N3_auc_roc_discriminacion.py:51-68`. El diccionario `cases` define:

| Caso | EDI | label_strong | `rmse_arima` |
|---|---:|:---:|:---:|
| 04_caso_energia | 0.6503 | 1 | 0.3905 |
| 16_caso_deforestacion | 0.5802 | 1 | 0.0616 |
| 20_caso_kessler | 0.3527 | 1 | 0.4075 |
| 27_caso_riesgo_biologico | 0.3326 | 1 | 0.3328 |
| 24_caso_microplasticos | 0.7819 | 1 | 0.1146 |
| 06_falsacion_exo | 0.0551 | 0 | 0.5150 |
| 07_falsacion_ns | -0.8819 | 0 | 0.5150 |
| 08_falsacion_obs | -1.0000 | 0 | 0.5150 |
| 01_clima | 0.0111 | 0 | None |
| 10_justicia | 0.2274 | 0 | None |
| 26_starlink | 0.6892 | 0 | None |
| 28_fuga_cerebros | 0.0249 | 0 | None |

**n = 12 totales** (5 strong + 7 no-strong). La definición operativa de `label_strong = 1` es **EDI ≥ 0.33** declarada a priori en cap 02-fundamentos antes del cómputo del corpus.

## 3. Score y etiqueta

- **Predictor (score):** EDI canónico de `outputs/metrics.json` de cada caso (campo `phases.real.edi.value`).
- **Etiqueta binaria:** `label_strong = 1 ⇔ EDI ≥ 0.33` (umbral declarado a priori).
- **Circularidad estructural:** el score y la etiqueta son funciones determinísticas del mismo EDI. La AUC mide exclusivamente la consistencia entre umbral declarado y clasificación final tras verificaciones del aparato; no compara el EDI contra un score independiente.

## 4. Cómputo (algoritmo)

Implementación manual de AUC-ROC en `N3_auc_roc_discriminacion.py:19-42` (sin sklearn). Orden descendente por score, recorrido secuencial con incremento (`fp_prev`, `tp_prev`) → trapecio sobre TPR/FPR. Equivale a la definición Mann-Whitney U normalizada cuando no hay empates de score.

**Resultado canónico:** `AUC-ROC con EDI como score = 0.8857` (redondeado en prosa a `0.886`).

## 5. CI bootstrap (B = 2000, seed = 42)

**Esquema:** bootstrap estratificado preservando las cuentas de cada clase (5 strong, 7 no-strong) para evitar muestras con clase vacía (que producirían `NaN` en AUC). Esta es la convención estándar para AUC sobre muestras pequeñas (Carpenter & Bithell 2000, "Bootstrap confidence intervals: when, which, what?", *Statistics in Medicine* 19, 1141-1164).

**Cifras (reproducibles):**

- Punto: **0.8857**.
- Media bootstrap: **0.8861**.
- IC 95 % percentil: **[0.6571, 1.0000]**.

**Lectura honesta del IC:** el límite superior tocando 1.0000 y el inferior bajando a 0.66 indican que con `n = 12` la incertidumbre de la AUC es muy amplia. El IC NO refuta la cifra 0.886, pero impide cualquier afirmación de superioridad fina sobre alternativas cuyas AUCs caigan dentro del intervalo.

**Comando regenerador (CLAUDE.md §4):**

```bash
cd /datos/repos/EstructurasPreontologicas/09-simulaciones-edi
source .venv/bin/activate
python3 - <<'PY'
import numpy as np
np.random.seed(42)

def auc_roc(scores, labels):
    n = len(scores)
    pos = np.sum(labels == 1); neg = np.sum(labels == 0)
    if pos == 0 or neg == 0: return float('nan')
    order = np.argsort(scores)[::-1]
    sl = labels[order]
    tpr_prev = fpr_prev = auc = 0.0; tp = fp = 0
    for lab in sl:
        if lab == 1: tp += 1
        else: fp += 1
        tpr = tp / pos; fpr = fp / neg
        auc += (fpr - fpr_prev) * (tpr + tpr_prev) / 2
        tpr_prev, fpr_prev = tpr, fpr
    return float(auc)

edi = np.array([0.6503, 0.5802, 0.3527, 0.3326, 0.7819,
                0.0551, -0.8819, -1.0000, 0.0111, 0.2274, 0.6892, 0.0249])
lab = np.array([1,1,1,1,1, 0,0,0,0,0,0,0])
print(f'AUC point: {auc_roc(edi, lab):.4f}')

ip, ineg = np.where(lab==1)[0], np.where(lab==0)[0]
aucs = []
for _ in range(2000):
    rp = np.random.choice(ip, size=len(ip), replace=True)
    rn = np.random.choice(ineg, size=len(ineg), replace=True)
    idx = np.concatenate([rp, rn])
    aucs.append(auc_roc(edi[idx], lab[idx]))
aucs = np.array(aucs)
print(f'CI 95% percentile: [{np.percentile(aucs,2.5):.4f}, {np.percentile(aucs,97.5):.4f}]')
PY
```

Salida esperada (verificada 2026-05-11):

```
AUC point: 0.8857
CI 95% percentile: [0.6571, 1.0000]
```

## 6. Por qué se retira la comparación contra ARIMA

El script original computaba también `AUC ARIMA = 0.6000` sobre `n = 8` (filtrando los 4 nulls sin `rmse_arima`). Esa comparación se retira de la prosa demostrativa (06-cierre/01 §8.1) por dos razones que se declaran sin atenuar:

1. **ARIMA no es un baseline pertinente para clasificación binaria strong/null.** ARIMA produce predicción univariada con RMSE; convertir `RMSE_rw / RMSE_arima` en score binario para AUC es construcción ad hoc, no comparación canónica.
2. **n distinto:** EDI sobre n = 12, ARIMA sobre n = 8. La comparación pareada exige misma muestra; aquí no la hay.

La cifra 0.886 sobrevive como **coherencia umbral interna** con sus salvedades; la comparación 0.886 vs 0.600 se retira como evidencia discriminativa.

## 7. Caveats permanentes

- **Internalidad estructural:** ningún re-cálculo, ningún CI bootstrap, ningún subsampleo convierte un test de consistencia interna en un test de discriminación externa. La AUC = 0.886 mide lo que mide; no más.
- **Tamaño muestral:** `n = 12` produce IC bootstrap muy ancho ([0.66, 1.00]). Cualquier afirmación de superioridad fina contra otra clasificación queda fuera del alcance.
- **Validación externa pendiente:** etiquetas asignadas por especialistas de cada dominio sin acceso al EDI, replicación independiente del cómputo, comparación de rankings — todo ello es deuda bloqueante post-defensa (entrada L4 de `04-debates/05-limitaciones-declaradas-consolidacion.md`).

## 8. Estado del documento y deuda asociada

- **Hecho:** documento canónico bajo `09-simulaciones-edi/auc_roc/` con comando regenerador y CI bootstrap.
- **Hecho (2026-05-16):** script autocontenido `09-simulaciones-edi/auc_roc/compute_auc_ci.py` (no dependiente de `Bitacora/`). Reproduce bit-a-bit `AUC=0.8857`, `mean=0.8861`, `CI95=[0.6571,1.0000]`. Ejecutar: `python3 09-simulaciones-edi/auc_roc/compute_auc_ci.py --seed 42`.
- **Pendiente:**
  - validación externa con etiquetas por especialistas (deuda H-J*/B-T futuro);
  - actualizar `09-simulaciones-edi/baselines/README.md` §"Aclaración crítica" para reflejar el retiro de la comparación contra ARIMA y reenviar a este documento.
