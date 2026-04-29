# Anexo A.0. Limitaciones declaradas (consolidación)

## Función

Listado consolidado de **todas las limitaciones que la tesis declara explícitamente**, con plazo y entregable para cada una. Este anexo no introduce limitaciones nuevas: consolida en un único lugar lo que está disperso en cap 06-01 §8.2, README, y bitácora. Útil como tarjeta de lectura para evaluadores y como respaldo en defensa oral.

**Política:** ninguna limitación se oculta; todas se nombran. Lo que está fechado es deuda priorizada; lo que no está fechado es honestidad estructural del régimen de validez.

---

## 1. Limitaciones metodológicas declaradas

| # | Limitación | Origen | Resolución actual | Entregable |
|---|-----------|--------|-------------------|------------|
| L1 | p-value mal calibrado (tasa empírica de tipo I ≈ 24 %, no 5 %) | Hostile testing N3 | Cerrada metodológicamente: el módulo `common/calibration.py` implementa block bootstrap (Politis y Romano 1994), Newey-West HAC (Newey y West 1987) y corrección Holm-Bonferroni (Holm 1979). Aplicada al corpus inter-dominio, los 12 casos significativos sin corrección colapsan a 4 tras Holm, coincidiendo con los 4 casos `overall_pass=True`. La inferencia formal sigue requiriendo invocación desde `edi_engine.py` con flag `--calibrated` en la ejecución final. | Re-ejecución del corpus con flag activo (≈ 3 semanas) |
| L2 | Composición del corpus inter-dominio post-hoc (no pre-registrada) | Auditoría severa N4 | Cerrada metodológicamente: pre-registro criptográfico con SHA-256, git commit y timestamps versionados; el hash agregado del corpus es verificable contra el repositorio bajo el commit declarado. | Verificación reproducible por evaluador externo |
| L3 | Sensibilidad a umbrales: 0.10/0.30 → 5 strong; 0.15/0.40 → 3; 0.05/0.20 → 9 | N4 | Mecanizada: el módulo `common/threshold_sensitivity.py` ejecuta el barrido completo y reporta clasificación invariante por caso. Tres casos (Energía, Deforestación, Microplásticos) son strong bajo cualquier elección razonable de umbrales. | Reporte automatizable por caso |
| L4 | AUC-ROC = 0.886 es ranking interno, no validación externa | Auditoría V4-05 | Reducida: el módulo `common/replication.py` provee `seed_robustness`, `holdout_temporal` y `adversarial_probe_swap`, ejecutables por replicador externo sin acceso al laboratorio. | Validación inter-grupo con replicador independiente |
| L5 | Caso 30 (behavioral dynamics) con circularidad detectada por sonda alternativa | N2 | El análisis de calibración estadística confirma cuantitativamente la circularidad: bajo block bootstrap, p estimado = 0.978 (no significativo). El caso se mantiene como piloto metodológico hasta datos humanos reales. | Datos VENLab/WALK-MS bajo protocolo CEI (9–12 meses) |
| L6 | Caso 38 (locomoción τ-dot) con failure mode (EDI = -1.34) | V4 post-multiescala | Failure declarado y documentado | Reformulación de sonda con histéresis o datos VENLab reales |

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
| L11 | κ-ontológica fuerte no demostrada; sólo κ-pragmática | Cap 02-01 §Nota sobre κ | El módulo `common/independent_probes.py` provee sondas teóricamente independientes (Maxwell-Boltzmann, Fisher-KPP, Zeeman cusp y otras) para evaluar el primer criterio de convergencia inter-paradigma. La verificación definitiva con datos primarios requiere re-ejecución del corpus con dump de arrays. | Programa multi-sonda con datos reales + revisión externa |
| L12 | **Naturalismo metafísico moderado es compromiso de partida**, no conclusión demostrada | Cap 02-01 §0.1 | Postura honesta, no deuda | Verificado por ST T16 (contramodelo encontrado: naturalismo NO se infiere desde dentro del marco) |
| L13 | **Dimensión fenomenológica (qualia, primera persona)** no agotada por aparato EDI | Cap 05-01 §7 | Postura: complementarismo metodológico | No se promete más |
| L14 | **Ética sustantiva** no se funda; sólo se articula filosóficamente | Cap 02-06 §6 | Postura honesta | No promete algoritmo para decisiones morales |
| L15 | **Sujeto y agencia**: compatibilismo dennettiano sin pretensión de resolver libre albedrío | Cap 05-01 §8 | Postura honesta | No se promete más |
| L16 | **Identidad personal a través del tiempo** no resuelta entre Locke/Parfit/Strawson | Cap 02-03 §V5 | Postura: continuidad de organización bajo transformación | Tratamiento explícito en cap 02-03 |

---

## 4. Limitaciones procedimentales (bloqueadores externos)

| # | Limitación | Origen | Plazo | Entregable |
|---|-----------|--------|-------|------------|
| L17 | Todas las auditorías internas son endógenas, con asistencia computacional bajo dirección humana | README línea 51 | 3-6 meses | Revisión por pares humanos externos (deuda externa bloqueante para sustentación) |
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

## 5.5. Módulos metodológicos implementados

Los siguientes módulos resuelven o reducen seis limitaciones sin re-ejecutar el corpus:

| Módulo | Limitación afectada | Resolución | Ruta |
|--------|---------------------|------------|------|
| Calibración estadística | L1 (p-value mal calibrado) | Cerrada metodológicamente | `09-simulaciones-edi/common/calibration.py` |
| Replicación robusta | L4 (AUC interno) | Reducida; tres pruebas ejecutables por externo | `09-simulaciones-edi/common/replication.py` |
| Pre-registro criptográfico | L2 (composición post-hoc) | Cerrada; corpus congelado con SHA-256 | `09-simulaciones-edi/common/preregistration.py` |
| Sondas independientes | L11 (κ-ontológica C1) | Infraestructura completa | `09-simulaciones-edi/common/independent_probes.py`, `full_secondary_probes.py` |
| Sensibilidad a umbrales | L3 (sensibilidad declarada) | Mecanizada | `09-simulaciones-edi/common/threshold_sensitivity.py` |
| Análisis de potencia | L21 (control de tipo II) | Mecanizado | `09-simulaciones-edi/common/power_analysis.py` |

La corrección FWER Holm-Bonferroni sobre los 30 casos del corpus inter-dominio reduce 12 casos significativos sin corrección a 4 tras Holm, que coinciden con los 4 casos `overall_pass=True`: la clasificación strong sobrevive a la corrección por comparaciones múltiples.

### Reclasificación de casos bajo régimen calibrado

La aplicación caso por caso de los módulos a los casos no invariantes produce los siguientes veredictos:

| Veredicto | Casos | Significado |
|-----------|-------|-------------|
| Pasa a robusto | 15 Wikipedia | Invariante a umbrales + significativo bajo block bootstrap + sobrevive FWER |
| Significativo individual sin FWER | 26 Starlink | Inferencia individual robusta; familia no sobrevive |
| Marginal post-calibración | 01 Clima, 09 Finanzas, 30 Behavioral Dynamics | p estimado > 0.10 bajo block bootstrap |
| Sensible a umbrales | 06 Exogeneidad, 10 Justicia, 11 Movilidad, 13 Políticas, 14 Postverdad, 20 Kessler, 27 Riesgo bio | Invariancia falla bajo grilla razonable |
| Evaluación específica | 21 Salinización, 28 Fuga de cerebros | Combinación particular de invariancia y p-value |

El caso 30 (Behavioral Dynamics) se confirma como marginal post-calibración (p estimado ≈ 0.978). El reconocimiento previo de circularidad en N2 (cap 06-01 §3.5) se sostiene cuantitativamente: el caso permanece como piloto metodológico hasta datos VENLab/WALK-MS reales. El caso 15 Wikipedia (EDI = 0.19) sí pasa a robusto bajo el régimen calibrado.

### Aplicación al corpus inter-escala

Los 7 casos strong del corpus inter-escala (31 Decoherencia cuántica, 32 Espín-órbita, 34 Michaelis-Menten, 36 NF-κB, 37 HRV cardíaco, 39 Cefeidas, 40 Cúmulos globulares) son invariantes a la grilla de umbrales y sobreviven la corrección FWER inter-escala. Los 2 nulls honestos (33 Villin Headpiece, 38 locomoción τ-dot) se confirman bajo régimen calibrado. El caso 35 (ciclo celular Tyson-Novak) queda sensible a umbrales.

### Distinción del error de tipo II

Bajo `common/power_analysis.py` se distingue entre `null_real` (potencia ≥ 0.80 para detectar EDI = 0.10) y `null por potencia insuficiente`. De los 17 casos null en el corpus, 4 son null reales y 13 carecen de potencia: requieren n ≥ 124 frente a n actual entre 8 y 19. El manuscrito no afirma ausencia de cierre operativo en esos 13 casos; afirma falta de resolución estadística.

| Categoría | n | Implicación |
|-----------|--:|-------------|
| No null (EDI > 0.10) | 23 | Casos con señal detectable |
| Null real (potencia ≥ 0.80) | 4 | Honestamente null bajo régimen actual |
| Null por potencia insuficiente | 13 | Falta de resolución; no afirmación de ausencia |

Esto introduce una distinción crítica que el manuscrito antes no tenía: **null estadístico ≠ ausencia ontológica**. Para 13 de los casos previamente clasificados como null, el manuscrito ahora afirma honestamente que el aparato carece de resolución para detectar weak (EDI=0.10) con potencia 0.80; necesitaría n ≥ 124 vs n actual entre 8 y 19.

El módulo de calibración estadística controla falsos positivos por autocorrelación; el módulo de potencia controla falsos negativos por tamaño muestral. Ambos producen un régimen estadísticamente honesto en las dos direcciones del error.

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
