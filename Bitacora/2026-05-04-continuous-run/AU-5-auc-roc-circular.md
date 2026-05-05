# AU-5 — AUC-ROC=0.886 vs ARIMA=0.600: circularidad y baseline de paja

**Fecha:** 2026-05-05
**Auditor:** sub-agente harness (modo headless, read-only fuera de Bitacora)
**Estado:** `needs_human` (requiere decisión de Jacob/Steven sobre cómo reformular)

---

## 1. Afirmación auditada

`06-cierre/01-conclusion-demostrativa.md:243`:

> "Discriminación de ranking interno sobre el corpus inter-dominio: AUC-ROC 0.886 vs ARIMA 0.600 (V4-05 reconoce que es interno, no validación externa contra estándar de oro)."

Y `06-cierre/01-conclusion-demostrativa.md:238` (fórmula final):

> "AUC-ROC = 0.886 para discriminación de ranking interno vs ARIMA = 0.600"

## 2. Verificación de la fuente

- **Único productor numérico de la cifra:** `Bitacora/2026-04-28-cierre-severo/N3_auc_roc_discriminacion.py` + `N3_resultados.json` (`auc_edi=0.8857142857`, `auc_arima_diff=0.6`, `auc_arima_ratio=0.6`, `delta=0.2857`, `n_strong=5`, `n_no_strong=7`).
- **No existe** `09-simulaciones-edi/auc_roc/` ni `methodology.md`. La cifra circula en el manuscrito sin documento metodológico canónico bajo `09-simulaciones-edi/`. Esto **viola CLAUDE.md §4** (cada cifra reportada debe poder regenerarse con un comando declarado y trazable; un script en `Bitacora/` de hace una semana no es fuente de verdad metodológica).

## 3. Hallazgos de circularidad y baseline de paja

### 3.1. Circularidad por construcción (CRÍTICO)

En `N3_auc_roc_discriminacion.py:51-64` las etiquetas `label_strong` están **asignadas a mano** y se corresponden 1:1 con los casos cuyo EDI ya superó los umbrales (0.10/0.30) usados para clasificar "strong" en el corpus. Luego se usa **el mismo EDI** como score de un clasificador binario contra esa etiqueta. Es **el mismo número usado dos veces**: como criterio de etiqueta y como score predictor. La AUC-ROC esperada es trivialmente alta (lo sorprendente es que sea 0.886 y no 1.0; la única razón de que no sea 1.0 es que `26_starlink` aparece etiquetado `label_strong=0` con EDI=0.6892, mayor que tres casos `label_strong=1`).

**Diagnóstico:** AUC-ROC sobre etiquetas derivadas del propio score no mide poder discriminativo; mide coherencia interna del umbral. El número 0.886 es **un test de consistencia umbral, no un test de validez externa**.

### 3.2. Baseline ARIMA es de paja (CRÍTICO)

ARIMA es un baseline de **predicción univariada**. La tarea declarada por la tesis es **clasificación de ranking strong vs null por presencia de dependencia ODE→ABM**, una tarea para la cual ARIMA no está diseñado. Compararlos en AUC-ROC es comparar un termómetro con un escarpín. Adicionalmente:

- El "score ARIMA" se construye ad-hoc como `RMSE_rw - RMSE_arima` o `RMSE_rw / RMSE_arima` (`N3_…py:73-80`), una transformación que el manuscrito no justifica como predictor de strong-vs-null en ningún lugar.
- 4 de los 7 nulls no tienen RMSE_arima (`rmse_arima: None` en líneas 60-63), por lo que la AUC ARIMA se computa sobre **n=8** (5 strong + 3 falsación), mientras la AUC EDI se computa sobre n=12. La comparación es **sobre muestras distintas**.

### 3.3. Tamaño muestral

n=12, 5 strong vs 7 null. AUC con esa n tiene varianza enorme. No hay CI bootstrap ni p-value reportados. La diferencia 0.886 vs 0.600 puede no ser significativa; la afirmación "supera por al menos 0.10" es solo aritmética.

## 4. Costo argumentativo declarado

La tesis usa esta cifra en su **fórmula final demostrativa** (sección 8) como evidencia de "valor diferencial" del aparato. Si la cifra cae:

- §8 pierde un soporte cuantitativo concreto frente a baselines.
- La afirmación de "discriminación de ranking interno" debe sostenerse por otro medio (por ejemplo, declarar simplemente la separación numérica EDI strong vs null, sin invocar AUC ni ARIMA).
- El reconocimiento ya hecho en §8.2 ("AUC-ROC interno no externo") es insuficiente: el problema no es solo internalidad, es **circularidad por construcción** y **baseline impropio**.

## 5. Propuesta de edición — tres opciones (decisión humana)

### Opción A — Eliminar la cifra (recomendada por rigor)

Quitar de `06-cierre/01-conclusion-demostrativa.md` líneas 238 y 243 toda mención a "AUC-ROC 0.886 vs ARIMA 0.600". Sustituir por una afirmación operativa verificable, por ejemplo:

> "Separación cuantitativa de la métrica EDI sobre el corpus inter-dominio: 5 casos strong (EDI ≥ 0.33) vs 3 controles de falsación rechazados (EDI ≤ 0.06), con 0/1500 falsos positivos del gate completo bajo random walk."

Costo: se pierde una "cifra-resumen" atractiva. Beneficio: se evita un argumento circular que un evaluador externo derribará en un párrafo.

### Opción B — Reformular sin invocar ARIMA, con metodología declarada

Mantener una cifra de discriminación interna, pero:

1. Documentarla en `09-simulaciones-edi/auc_roc/methodology.md` con: (i) outcome operativo (strong vs null por umbral declarado **antes** del cómputo), (ii) predictor (EDI), (iii) "gold standard" honesto (etiquetas derivadas del propio criterio EDI, **declarado como test de coherencia umbral, NO de validez externa**), (iv) CI bootstrap, (v) comando regenerador.
2. Eliminar la comparación con ARIMA (no es un baseline pertinente para la tarea).
3. Reescribir la afirmación como: "coherencia interna del umbral EDI: AUC-ROC = X.XX (CI [a,b]) sobre corpus inter-dominio, **interpretable solo como consistencia umbral, no como discriminación externa**".

Costo: pierde retórica comparativa. Beneficio: cifra defendible.

### Opción C — Construir un baseline NO de paja y rehacer el test

Si la tesis quiere sostener "EDI discrimina strong-vs-null mejor que un baseline", el baseline correcto NO es ARIMA. Candidatos pertinentes:

- Surrogate testing con permutación de la sonda ODE (mantener ABM, romper acoplamiento) — ya implementado parcialmente en el motor.
- Granger-causality clásico ABM↔ODE como score escalar.
- Cross-prediction skill (CCM, Sugihara) sobre las series acopladas vs desacopladas.

Y las etiquetas strong-vs-null deben venir de un criterio **independiente del EDI** (por ejemplo: presencia/ausencia conocida de acoplamiento por construcción del caso, lo cual es trivialmente conocido para los 3 casos de falsación pero ambiguo para los demás).

Costo: trabajo técnico nuevo (B-T*), probablemente 1-2 semanas. Beneficio: una cifra de discriminación que sí mide lo que dice medir.

## 6. Acción inmediata propuesta

`needs_human`: Jacob/Steven deben decidir entre A, B o C antes de la siguiente regeneración de `Tesis.md`. La asistencia NO debe editar §8 ni §8.1 hasta firma humana.

Si no hay respuesta antes de cierre de la pasada continua, la opción por defecto **menos dañina** es **A** (eliminar la cifra), porque mantenerla en la fórmula final con la metodología actual es indefendible bajo crítica hostil mínima.

## 7. Deuda residual generada

- **B-T-NEW-AUC**: si se elige B o C, crear `09-simulaciones-edi/auc_roc/methodology.md` + script regenerador con CI bootstrap y, en caso C, baseline pertinente.
- **F-AUC-1**: registrar en `04-debates/05-limitaciones-declaradas-consolidacion.md` que la cifra previa 0.886 vs 0.600 fue retirada/reformulada por circularidad de etiquetado y baseline impropio (independientemente de la opción elegida).

---

RESULT: complete | AU-5-auc-roc-circular | needs_human: circularidad + baseline paja confirmados
