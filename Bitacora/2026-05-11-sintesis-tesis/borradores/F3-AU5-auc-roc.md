---
borrador: IA
requires: H-J*
propuesta_fecha: 2026-05-11
destino: 06-cierre/01-conclusion-demostrativa.md (líneas ~230, ~235, ~237; eventualmente §8.2)
hallazgo: AU-5
salida_elegida: b
---

# Borrador F3-AU5 — Reformulación del AUC-ROC 0.886 vs ARIMA 0.600

## 1. Verificación de los tres sub-claims del worker huérfano

Antes de proponer reescritura, los tres sub-claims de `AU-5-auc-roc-circular.md` se verificaron leyendo el código y los datos primarios. Resultado: **los tres son correctos** y la circularidad es estructural.

### 1.1. Mismo EDI usado como etiqueta y como score (CONFIRMADO)

Fuente: `Bitacora/2026-04-28-cierre-severo/N3_auc_roc_discriminacion.py`, líneas 51-68.

El diccionario `cases` asigna `label_strong=1` a exactamente cinco casos (`04_energia`, `16_deforestacion`, `20_kessler`, `27_riesgo_biologico`, `24_microplasticos`), que son precisamente los cinco casos con EDI ≥ 0.33 en `metrics.json` (umbral declarado para "strong"). El resto de los siete casos del corpus tiene `label_strong=0`. Acto seguido, el script computa AUC-ROC usando el **mismo EDI** como score predictor contra esa misma etiqueta:

```python
edi_scores = np.array([cases[k]["edi"] for k in keys])
labels     = np.array([cases[k]["label_strong"] for k in keys])
auc_edi    = auc_roc(edi_scores, labels)
```

La única razón aritmética por la que la AUC no es 1.0 es que `26_starlink` tiene EDI=0.6892 con `label_strong=0` (clasificado null por otros criterios del aparato pese al EDI alto), lo que introduce 3 inversiones de ranking sobre 35 pares strong-vs-null. Eso es exactamente lo que la cifra 0.886 mide: **inconsistencia residual entre el umbral 0.33 y la clasificación final del corpus**, no discriminación contra un rival externo.

### 1.2. n=8 (ARIMA) vs n=12 (EDI) (CONFIRMADO)

En el mismo script, líneas 60-63: cuatro de los siete casos null (`01_clima`, `10_justicia`, `26_starlink`, `28_fuga_cerebros`) tienen `rmse_arima: None`. La línea 72 filtra: `keys_with_arima = [k for k in keys if cases[k]["rmse_arima"] is not None]`, dejando n=8 (5 strong + 3 falsación). La AUC EDI se computa sobre n=12; la AUC ARIMA sobre n=8. Son **muestras distintas**, no comparación pareada. La comparación numérica 0.886 vs 0.600 no es metodológicamente válida.

### 1.3. `09-simulaciones-edi/auc_roc/methodology.md` no existe (CONFIRMADO)

`ls 09-simulaciones-edi/auc_roc/` → directorio inexistente. El único documento metodológico vivo sobre el AUC-ROC es `09-simulaciones-edi/baselines/README.md:91-99` ("Aclaración crítica: el AUC-ROC = 0.886 es interno, no externo"), que reconoce internalidad pero **no** reconoce la circularidad por construcción ni el desbalance n=8 vs n=12 ni la ausencia de CI bootstrap. El productor numérico vive en `Bitacora/2026-04-28-cierre-severo/N3_auc_roc_discriminacion.py`, lo cual viola CLAUDE.md §4: la cifra reportada por el manuscrito no tiene comando regenerador bajo `09-simulaciones-edi/` (la ubicación canónica de fuente de verdad numérica).

**Conclusión de verificación:** el worker huérfano tenía razón en los tres puntos. El claim 0.886 vs 0.600 es indefendible bajo crítica hostil mínima en su forma actual.

## 2. Salida elegida: (b) reformulación como "coherencia umbral interna"

Razón:

- **(a) eliminación pura** pierde información: la AUC=0.886 sí mide algo real (coherencia entre el umbral EDI 0.33 y la clasificación final del corpus). Eliminar sin sustituto deja un hueco evidencial que la sección 8 ya no puede cubrir desde la cifra "0/2000 falsos positivos" sola, porque esa cifra mide robustez del gate contra ruido, no consistencia umbral.
- **(c) defensa con `methodology.md` honesto** no es viable: la circularidad es **estructural** (mismo EDI usado dos veces), no un defecto documental. Ningún documento puede convertir un test de consistencia interna en un test de discriminación contra rivales. Producir un `methodology.md` que defienda la cifra como "discriminación" sería auto-indulgencia bajo CLAUDE.md §1.
- **(b) reformulación** preserva la cifra como lo que efectivamente mide (coherencia umbral interna), elimina la comparación con ARIMA (baseline impropio sobre n distinto), y exige producir el `methodology.md` canónico bajo `09-simulaciones-edi/auc_roc/` para cumplir CLAUDE.md §4.

## 3. Borradores de reescritura para `06-cierre/01-conclusion-demostrativa.md`

> Estos borradores son propuestas para Jacob. La firma final es suya. No se ha editado el capítulo.

### 3.1. Reescritura de la línea 230 (Fórmula final demostrativa, §8)

**Texto actual (fragmento problemático):**

> "...hostile testing aplicado al motor (0/2000 falsos positivos en gate completo bajo random walk masivo, Wilson 95 % CI [0, 0.00191]) y al test cruzado de sondas inter-escala (0/12 circularidad detectada), **AUC-ROC = 0.886 para discriminación de ranking interno vs ARIMA = 0.600**, y discriminación pública contra catorce rivales..."

**Reescritura propuesta:**

> "...hostile testing aplicado al motor (0/2000 falsos positivos en gate completo bajo random walk masivo, Wilson 95 % CI [0, 0.00191]) y al test cruzado de sondas inter-escala (0/12 circularidad detectada), **coherencia interna del umbral EDI sobre el corpus inter-dominio (AUC-ROC = 0.886, n=12, interpretada como consistencia entre el umbral declarado 0.33 y la clasificación final del corpus, NO como discriminación externa contra un baseline rival)**, y discriminación pública contra catorce rivales..."

Y eliminar de §8.2 (limitación reconocida) "AUC-ROC interno no externo", sustituyéndola por:

> "No afirma que el AUC-ROC = 0.886 mida discriminación contra un baseline rival: la AUC se computa con el mismo EDI como score y como etiqueta (vía umbral 0.33), por lo que es un test de **consistencia umbral interna**, no de validez externa. La comparación previa contra ARIMA (0.600) se retira: ARIMA no es un baseline pertinente para clasificación strong/null y se computaba sobre n=8 mientras EDI se computaba sobre n=12, lo que invalida la comparación."

### 3.2. Reescritura de la línea 235 (§8.1)

**Texto actual:**

> "**Discriminación de ranking interno** sobre el corpus inter-dominio: AUC-ROC 0.886 vs ARIMA 0.600 (V4-05 reconoce que es interno, no validación externa contra estándar de oro)."

**Reescritura propuesta:**

> "**Coherencia interna del umbral EDI** sobre el corpus inter-dominio: AUC-ROC = 0.886 (n=12), entendida como consistencia entre el umbral declarado a priori (EDI ≥ 0.33 → strong) y la clasificación final del corpus tras todas las verificaciones del aparato. Esta cifra **no mide discriminación contra un rival externo**: el predictor y la etiqueta son funciones del mismo EDI. La validación discriminativa externa (etiquetas asignadas por especialistas de cada dominio sin acceso al EDI, replicación independiente del cómputo, comparación de rankings) es deuda bloqueante post-defensa."

### 3.3. Reescritura de la línea 237 (final del bullet sobre 0/2000 FP)

**Texto actual (fragmento final del bullet):**

> "...El gate filtra ruido sin acoplamiento ODE→ABM por construcción (§3.4): el resultado certifica integridad de implementación, no discriminación contra rivales con estructura — **esa carga la sostienen AUC-ROC = 0.886 vs ARIMA y 3/3 controles de falsación rechazados**."

**Reescritura propuesta:**

> "...El gate filtra ruido sin acoplamiento ODE→ABM por construcción (§3.4): el resultado certifica integridad de implementación, no discriminación contra rivales con estructura — esa carga la sostienen **los 3/3 controles de falsación rechazados (06-exoplanetas, 07-noticias-shanghai, 08-observacional-control) con EDI ≤ 0.06 y gate=false en los tres**, y la coherencia interna del umbral EDI (AUC-ROC = 0.886 como medida de consistencia umbral, no de discriminación contra baseline)."

## 4. Costo argumental declarado

La reescritura **debilita la retórica comparativa** de la sección 8: ya no se puede afirmar "EDI domina ARIMA en AUC". Esto es deliberado y necesario. El costo se compensa así:

- la cifra 0/2000 FP (gate vs random walk) **sí es discriminación contra una hipótesis nula no trivial** (ruido sin estructura) y carga el peso evidencial que antes cargaba la falsa comparación con ARIMA;
- los 3/3 controles de falsación rechazados son discriminación operativa contra rivales de paja construidos a propósito;
- la coherencia umbral interna (AUC=0.886) sigue siendo informativa: dice que el umbral 0.33 no genera contradicciones masivas con la clasificación final del corpus.

Lo que se pierde es la ilusión de un "test de superioridad sobre baseline establecido". Esa ilusión es exactamente lo que CLAUDE.md §1 prohíbe.

## 5. Acción técnica obligatoria si Jacob acepta (b)

Producir `09-simulaciones-edi/auc_roc/methodology.md` con:

1. Definición operativa del outcome (coherencia umbral interna, NO discriminación externa).
2. Predictor: EDI canónico de `outputs/metrics.json`.
3. Etiqueta: `label_strong = 1 ⇔ EDI ≥ 0.33` (umbral declarado en cap 02-fundamentos antes del cómputo del corpus).
4. Interpretación honesta: lo que la AUC mide es cuántas inversiones de ranking existen entre el umbral 0.33 y la clasificación final del corpus tras todas las verificaciones (gate completo, p-value, C1-C5, hostile testing). AUC < 1.0 indica inconsistencia residual; en este corpus, viene de `26_starlink` (EDI=0.6892, clasificado null por gate=false pese al EDI alto).
5. CI bootstrap (B=2000) sobre la AUC para reportar incertidumbre (no está hecho; pendiente).
6. Comando regenerador con `seed=42` (a producir tras decisión humana).
7. Retiro explícito de la comparación contra ARIMA, con justificación: (i) ARIMA es predicción univariada, no clasificación binaria; (ii) la comparación se hacía sobre n=8 mientras EDI sobre n=12, lo que invalida la comparación pareada.

Adicionalmente: actualizar `09-simulaciones-edi/baselines/README.md:91-99` para reflejar el retiro de la comparación con ARIMA y el cambio de marco (coherencia umbral interna en vez de "ranking interno vs ARIMA").

## 6. Deuda residual generada

- **B-T-NEW-AUC-METH**: crear `09-simulaciones-edi/auc_roc/methodology.md` + script regenerador con CI bootstrap (B≥2000) y comando declarado bajo `09-simulaciones-edi/`. Sin esto, la cifra 0.886 sigue violando CLAUDE.md §4 aunque la reescritura prosaica esté hecha.
- **F-AUC-RETIRADA**: registrar en `04-debates/05-limitaciones-declaradas-consolidacion.md` el retiro de la comparación EDI vs ARIMA en AUC-ROC por circularidad de etiquetado y baseline impropio sobre n desigual.
- **B-T-AUC-EXTERNA** (deuda post-defensa, ya existente como L4): validación externa con etiquetas asignadas por especialistas sin acceso al EDI.

## 7. Decisiones que requieren firma de Jacob (H-J*)

1. **Aprobar (b) reformulación** frente a (a) eliminación pura. La asistencia recomienda (b) por preservar información honesta; (a) es defensiva pero pierde el dato de coherencia umbral.
2. **Aprobar la redacción exacta** de las tres reescrituras en §3 de este borrador (líneas 230, 235, 237 y la limitación de §8.2). La asistencia ofrece texto, Jacob firma.
3. **Aprobar el retiro de la comparación con ARIMA en cap 06-cierre y en `09-simulaciones-edi/baselines/README.md`**. Esto es coherente con la justificación de §3 pero implica reescribir un párrafo del README de baselines también.
4. **Aprobar la creación de `09-simulaciones-edi/auc_roc/methodology.md`** como deuda técnica bloqueante para regenerar la cifra 0.886 con CI bootstrap antes de que el manuscrito pueda re-citarla bajo régimen CLAUDE.md §4.
5. **Decidir si reportar también CI bootstrap de la AUC** en §8.1 (recomendado) o dejarlo solo en `methodology.md` (más limpio para la prosa demostrativa).

## 8. Naturaleza del aporte de este borrador

100% asistencia técnica bajo dirección humana. La voz autoral filosófica de §8 es de Jacob; este borrador propone una reescritura defensiva metodológicamente, no una reformulación filosófica del cierre. La decisión de aceptar, modificar o rechazar es de Jacob.
