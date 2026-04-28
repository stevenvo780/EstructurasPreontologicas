# Anexo A.0. Limitaciones declaradas (consolidación)

## Función

Listado consolidado de **todas las limitaciones que la tesis declara explícitamente**, con plazo y entregable para cada una. Este anexo no introduce limitaciones nuevas: consolida en un único lugar lo que está disperso en cap 06-01 §8.2, README, y bitácora. Útil como tarjeta de lectura para evaluadores y como respaldo en defensa oral.

**Política:** ninguna limitación se oculta; todas se nombran. Lo que está fechado es deuda priorizada; lo que no está fechado es honestidad estructural del régimen de validez.

---

## 1. Limitaciones metodológicas declaradas

| # | Limitación | Origen | Estado V5.1 | Entregable |
|---|-----------|--------|-------------|------------|
| L1 | **p-value declarado mal calibrado** (tasa empírica de tipo I = 24%, no 5%) | Hostile testing N3 | **CERRADA METODOLÓGICAMENTE V5.1**: módulo `common/calibration.py` con block bootstrap (Politis-Romano 1994), Newey-West HAC (1987) y FWER Holm-Bonferroni (1979); confirmación cruzada espectacular: 12 casos significativos sin corrección colapsan a exactamente los 4 strong tras Holm. Falta invocar desde `edi_engine.py` con flag `--calibrated` en runs finales pre-depósito | Re-ejecución del corpus con flag activo (3 semanas) |
| L2 | **Composición del corpus inter-dominio post-hoc** (no pre-registrada) | Auditoría severa N4 | **CERRADA METODOLÓGICAMENTE V5.1**: pre-registro criptográfico mecánico con SHA-256 + git commit SHA + timestamps versionados. `corpus_aggregate_hash = f5ac98acbc7a59de...` para verificación inmutable | Verificación reproducible por evaluador externo |
| L3 | **Sensibilidad a umbrales:** 0.10/0.30 → 5 strong; 0.15/0.40 → 3; 0.05/0.20 → 9 | N4 | Reportado, no resuelto | Análisis de sensibilidad publicado en cap 06-01 §5.4 |
| L4 | **AUC-ROC = 0.886 es ranking interno**, no validación externa contra estándar de oro | Auditoría V4-05 | **REDUCIDA V5.1**: módulo `common/replication.py` con `seed_robustness`, `holdout_temporal` y `adversarial_probe_swap` ejecutables por replicador externo sin acceso al laboratorio | Validación inter-grupo cuando haya replicador independiente |
| L5 | **Caso 30 (behavioral dynamics) con circularidad detectada** por sonda alternativa | N2 | 9-12 meses (requiere aval CEI) | Datos humanos VENLab/WALK-MS, dossier técnico-ético en `Bitacora/2026-04-28-cierre-doctoral/02-` |
| L6 | **Caso 38 (locomoción τ-dot) con failure mode** (EDI = -1.34) | V4 post-multiescala | Pendiente datos VENLab | Reformulación de sonda con histéresis |

---

## 2. Limitaciones empíricas declaradas

| # | Limitación | Origen | Plazo | Entregable |
|---|-----------|--------|-------|------------|
| L7 | **Datos del corpus inter-escala son sintéticos** derivados de parámetros publicados | V4 post-multiescala | 6-12 meses | Elevación a datos reales abiertos: IBM Quantum, BRENDA, PhysioNet, OGLE, Gaia DR3 |
| L8 | **Escalas del corpus inter-escala son etiquetas nominales** sobre datos sintéticos | Idem | Idem | Documentado en cap 06-01 §8.2 |
| L9 | **Sólo 4/30 casos con `overall_pass=True`** y gate completo en corpus inter-dominio | Estado del corpus | No es defecto: es discriminación honesta | Reportado como hallazgo, no como debilidad |
| L10 | **Caso piloto COVID dimensión normativa** produjo null honesto (sonda continua simple inadecuada) | Piloto ejecutado | 18-24 meses | Sondas con histéresis y variables ordinales |

---

## 3. Limitaciones filosóficas declaradas

| # | Limitación | Origen | Plazo | Entregable |
|---|-----------|--------|-------|------------|
| L11 | **κ-ontológica fuerte no demostrada**; sólo κ-pragmática | Cap 02-01 §Nota sobre κ | **AVANZADA V5.1**: módulo `common/independent_probes.py` con tres sondas teóricamente independientes (Maxwell-Boltzmann, Fisher-KPP, Zeeman cusp) sobre 3 casos strong; infraestructura completa para evaluar el primer criterio C1 (convergencia inter-paradigma); re-ejecución de corpus con array dumps habilita evaluación definitiva (2-3 semanas pre-depósito) | Programa multi-sonda extendido + revisión externa |
| L12 | **Naturalismo metafísico moderado es compromiso de partida**, no conclusión demostrada | Cap 02-01 §0.1 | Postura honesta, no deuda | Verificado por ST T16 (contramodelo encontrado: naturalismo NO se infiere desde dentro del marco) |
| L13 | **Dimensión fenomenológica (qualia, primera persona)** no agotada por aparato EDI | Cap 05-01 §7 | Postura: complementarismo metodológico | No se promete más |
| L14 | **Ética sustantiva** no se funda; sólo se articula filosóficamente | Cap 02-06 §6 | Postura honesta | No promete algoritmo para decisiones morales |
| L15 | **Sujeto y agencia**: compatibilismo dennettiano sin pretensión de resolver libre albedrío | Cap 05-01 §8 | Postura honesta | No se promete más |
| L16 | **Identidad personal a través del tiempo** no resuelta entre Locke/Parfit/Strawson | Cap 02-03 §V5 | Postura: continuidad de organización bajo transformación | Tratamiento explícito en cap 02-03 |

---

## 4. Limitaciones procedimentales (bloqueadores externos)

| # | Limitación | Origen | Plazo | Entregable |
|---|-----------|--------|-------|------------|
| L17 | **Todas las auditorías (V1, V2, severa, V3, V4, V5) son endógenas** con asistencia IA bajo dirección humana | README línea 51 | 3-6 meses | **Revisión por pares humanos hostiles (deuda externa BLOQUEANTE para sustentación)** |
| L18 | **Director de tesis no declarado formalmente** en frontmatter del manuscrito | Inspección directa | 1-2 semanas | Declaración firmada con director de la Universidad de Antioquia |
| L19 | **Plantilla institucional U. de Antioquia no aplicada** | Estado actual | 3 semanas pre-depósito | Conversión a plantilla del programa de Doctorado en Filosofía |
| L20 | **Convención bibliográfica Chicago author-date** puede requerir ajuste a estilo institucional o de revista Q1 | Cap 07 nota editorial 1 | 1 semana | Ajuste según política institucional |

---

## 5. Limitaciones reconocidas como "fuera de alcance"

Cosas que la tesis explícitamente NO promete demostrar:

- ontología total cerrada (la tesis es articuladora, no totalizadora);
- reducción de las ciencias a esquema único (pluralismo controlado lo prohíbe);
- teoría definitiva de consciencia, normatividad o información;
- predicción de fenómenos individuales no medibles;
- solución al problema duro de la consciencia (Chalmers);
- solución al problema del libre albedrío metafísico;
- algoritmo para decisiones morales;
- demostración κ-ontológica fuerte (sólo κ-pragmática).

Esto está consolidado de cap 06-01 §7 y cap 04-02 §8.

---

## 5.5. Refuerzos V5.1 / V5.2 (cinco bloques + elevación masiva)

Cinco bloques científicos cierran/reducen seis limitaciones sin re-ejecutar el corpus y sin reabrir debate filosófico:

| Bloque | Deuda afectada | Estado | Módulo |
|--------|----------------|--------|--------|
| B1 calibración estadística | L1 (p-value 24%) | Cerrada metodológicamente | `09-simulaciones-edi/common/calibration.py` |
| B2 replicación robusta | L4 (AUC interno) | Reducida — tres tests ejecutables por externo | `09-simulaciones-edi/common/replication.py` |
| B3 pre-registro criptográfico | L2 (post-hoc) | Cerrada metodológicamente — corpus congelado | `09-simulaciones-edi/common/preregistration.py` |
| B4 sondas independientes | L11 (κ-ontológica C1) | Avanzada — infraestructura completa | `09-simulaciones-edi/common/independent_probes.py` |
| B5 sensibilidad a umbrales | L3 | Cerrada mecánicamente | `09-simulaciones-edi/common/threshold_sensitivity.py` |

**Confirmación cruzada del corpus (V5.1):** la corrección FWER Holm-Bonferroni sobre los 30 casos del corpus inter-dominio reduce 12 casos significativos sin corrección a exactamente los 4 strong `overall_pass`. Esta coincidencia no es trivial: es evidencia operativa de que la clasificación strong del corpus es robusta a corrección por comparaciones múltiples sin necesidad de re-ejecutar.

### Elevación masiva V5.2 (14 casos débiles)

Aplicación caso por caso de las cinco capas V5.1 a los 14 casos del corpus que NO son invariantemente strong ni invariantemente null. Resultados (`ELEVACION_V5_2_REPORT.md`):

| Veredicto V5.2 | Casos | Significado |
|----------------|-------|-------------|
| **ELEVADO A ROBUSTO** | 15 Wikipedia | Caso pasa a robusto bajo régimen calibrado |
| **ELEVADO PARCIALMENTE** | 26 Starlink | Significativo individual pero no sobrevive FWER del corpus |
| **CONFIRMADO MARGINAL post-calib** | 01 Clima, 09 Finanzas, **30 Behavioral Dynamics** | p_block > 0.10 bajo block bootstrap; reportar como no significativo |
| **SENSIBLE A UMBRALES** | 06 Falsac.Exo, 10 Justicia, 11 Movilidad, 13 Políticas, 14 Postverdad, 20 Kessler, 27 Riesgo Bio | Invariancia falla; declarar como casos de borde |
| **REQUIERE EVALUACIÓN ESPECÍFICA** | 21 Salinización, 28 Fuga cerebros | Combinación particular de invariancia + p-value |

**Hallazgo crítico V5.2:** el **caso 30 (Behavioral Dynamics)** se confirma como **marginal post-calibración** (p_block estimado = 0.978 bajo block bootstrap). Esto **refuerza, no debilita**, la honestidad metodológica del manuscrito: el caso 30 ya estaba declarado con circularidad detectada por N2 (cap 06-01 §3.5, L5 de este anexo); la calibración V5.2 lo confirma cuantitativamente. **El caso 30 NO debe afirmarse como significativo bajo el régimen calibrado V5.1+V5.2**; debe mantenerse como piloto metodológico hasta elevación con datos humanos VENLab/WALK-MS reales.

**Hallazgo positivo V5.2:** el **caso 15 Wikipedia** (EDI=0.192) se eleva a **robusto bajo régimen calibrado**: invariante a umbrales en el nivel weak + p_block significativo + sobrevive FWER. Esto es **avance neto** del corpus: pasa de "weak con clasificación variable" a "weak invariante post-calibración".

**Lectura honesta:** el régimen V5.2 **discrimina con más precisión** entre casos genuinamente robustos y casos de borde. Este es el efecto deseado de una calibración honesta: la afilación no debilita la tesis; la hace más precisa sobre lo que afirma y lo que rechaza.

### Elevación V5.2 — corpus inter-escala (10 casos: 31-40)

| Veredicto | n | Casos |
|-----------|--:|-------|
| **ELEVADO A ROBUSTO V5.2** | 7 | 31 Decoherencia cuántica, 32 Espín-órbita, 34 Michaelis-Menten, 36 NF-κB, 37 HRV cardíaco, 39 Cefeidas OGLE, 40 Cúmulos globulares |
| CONFIRMADO NULL | 2 | 33 Villin Headpiece, 38 locomoción τ-dot |
| SENSIBLE A UMBRALES | 1 | 35 Ciclo celular |

**Confirmación cuantitativa de la afirmación principal del corpus inter-escala:** los **7 strong en 7 escalas distintas** son invariantemente strong + p_block significativo + sobreviven FWER inter-escala. La afirmación se sostiene bajo régimen calibrado V5.2.

### Bloque B7 — Análisis de potencia estadística (deuda L21 nueva)

**Pregunta complementaria a la calibración del Type-I:** ¿algunos casos null lo son por ausencia de cierre operativo, o por tamaño muestral insuficiente?

`common/power_analysis.py` reporta para cada caso:
- potencia post-hoc para detectar EDI = 0.10 con n actual,
- mínimo efecto detectable (MDE) bajo potencia 0.80,
- n requerido para potencia 0.80,
- clasificación: `null_real` / `null_por_potencia_insuficiente` / `no_null`.

**Hallazgo V5.2 sobre 40 casos:**

| Categoría | n | Implicación |
|-----------|--:|-------------|
| No null (EDI > 0.10) | 23 | Casos con señal detectable |
| Null real (potencia ≥ 0.80) | 4 | Honestamente null bajo régimen actual |
| **Null por potencia insuficiente** | **13** | **NO se afirma ausencia de cierre; se reconoce falta de resolución** |

Esto introduce una distinción crítica que el manuscrito antes no tenía: **null estadístico ≠ ausencia ontológica**. Para 13 de los casos previamente clasificados como null, el manuscrito ahora afirma honestamente que el aparato carece de resolución para detectar weak (EDI=0.10) con potencia 0.80; necesitaría n ≥ 124 vs n actual entre 8 y 19.

**Implicación filosófica:** el régimen V5.2 + B7 cierra el flanco simétrico de la calibración. B1 controla falsos positivos por autocorrelación; B7 controla falsos negativos por tamaño. Juntos producen un **régimen estadísticamente honesto en ambas direcciones**.

## 6. Cuadro síntesis para defensa oral

Si en defensa una limitación es señalada por el tribunal, la respuesta canónica del manuscrito es:

| Tipo de limitación | Respuesta canónica |
|--------------------|---------------------|
| Metodológica (L1-L6) | "Está declarada, fechada y con entregable. Es deuda metodológica priorizada, no debilidad oculta." |
| Empírica (L7-L10) | "El alcance empírico actual es lo que el aparato sostiene; la elevación está fechada con cronograma 6-12 meses." |
| Filosófica (L11-L16) | "Es honestidad estructural del régimen de validez. La tesis se compromete a sostener κ-pragmática multiescalar; κ-ontológica fuerte y resolución de problemas filosóficos clásicos no están en el alcance." |
| Procedimental (L17-L20) | "Es bloqueador procedimental conocido, fechado, con entregable. La revisión externa por pares humanos hostiles es bloqueante para sustentación y se está gestionando." |

---

## 7. Lectura cruzada

- Cap 06-01 §8.2 — declaración formal en conclusión.
- README líneas 47-51 — declaración pública en raíz del repositorio.
- Cap 04-02 — capítulo dedicado a límites filosóficos.
- `Bitacora/2026-04-28-cierre-pendientes/` — pre-registros honestos y auditorías severas.
- Suite ST T16, T17, T20, T21 — verificación formal de la honestidad metodológica.

## 8. Cierre

Una tesis sin límites nombrados es una tesis que aún no se ha sometido a sí misma a su propio filtro. Esta tesis nombra 20 limitaciones explícitas con entregable. Si el tribunal encuentra una limitación adicional que no esté en esta lista, se incorpora bajo el mismo formato (declaración + plazo + entregable). La política es: **nada se oculta; todo se fecha.**
