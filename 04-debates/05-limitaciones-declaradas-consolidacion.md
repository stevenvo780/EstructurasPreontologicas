# Limitaciones declaradas (consolidación)

## Función

Listado consolidado de **todas las limitaciones que la tesis declara explícitamente**, con plazo y entregable para cada una. Este capítulo no introduce limitaciones nuevas: consolida en un único lugar lo que está disperso en cap 06-01 §8.2, README, y bitácora. Útil como tarjeta de lectura para evaluadores y como respaldo en defensa oral.

**Política:** ninguna limitación se oculta; todas se nombran. Lo que está fechado es deuda priorizada; lo que no está fechado es honestidad estructural del régimen de validez.

---

## 1. Limitaciones metodológicas declaradas

**Tabla A.0.1.**

**Tabla 4.5.1.**

| # | Limitación | Origen | Resolución actual | Entregable |
|---|-----------|--------|-------------------|------------|
| L1 | p-value mal calibrado (tasa empírica de tipo I ≈ 24 %, no 5 %) | Hostile testing N3 | Cerrada metodológicamente: el módulo `common/calibration.py` implementa block bootstrap (Politis y Romano 1994), Newey-West HAC (Newey y West 1987) y corrección Holm-Bonferroni (Holm 1979, "A simple sequentially rejective multiple test procedure", *Scand. J. Statist.* 6: 65–70; referencia bibliográfica sin PDF en `07-bibliografia/`, paginación verbatim no verificable en esta pasada). Aplicada al corpus inter-dominio, 14 casos del corpus inter-dominio + 8 del corpus multiescala = 22 casos sobreviven Holm-Bonferroni a α=0.05; los 6 casos macro `overall_pass=True` (post-iter-7 B-T2 2026-05-17) están entre los sobrevivientes. La inferencia formal sigue requiriendo invocación desde `edi_engine.py` con flag `--calibrated` en la ejecución final. | Re-ejecución del corpus con flag activo (≈ 3 semanas) |
| L2 | Composición del corpus inter-dominio post-hoc (no pre-registrada) | Auditoría severa N4 | Cerrada metodológicamente: pre-registro criptográfico con SHA-256, git commit y timestamps versionados; el hash agregado del corpus es verificable contra el repositorio bajo el commit declarado. | Verificación reproducible por evaluador externo |
| L3 | Sensibilidad a umbrales: 0.10/0.30 → 5 strong; 0.15/0.40 → 3; 0.05/0.20 → 9 | N4 | Mecanizada: el módulo `common/threshold_sensitivity.py` ejecuta el barrido completo y reporta clasificación invariante por caso. Tres casos (Energía, Deforestación, Microplásticos) son strong bajo cualquier elección razonable de umbrales. | Reporte automatizable por caso |
| L4 | AUC-ROC = 0.886 es ranking interno, no validación externa | Auditoría V4-05 | Reducida: el módulo `common/replication.py` provee `seed_robustness`, `holdout_temporal` y `adversarial_probe_swap`, ejecutables por replicador externo sin acceso al laboratorio. | Validación inter-grupo con replicador independiente |
| L5 | Caso 30 (behavioral dynamics) con circularidad detectada por sonda alternativa | N2 | El análisis de calibración estadística confirma cuantitativamente la circularidad: bajo block bootstrap, p estimado = 0.978 (no significativo). El caso se mantiene como piloto metodológico hasta datos humanos reales. | Datos VENLab/WALK-MS bajo protocolo CEI (9–12 meses) |
| L6 | Caso 38 (locomoción τ-dot) con failure mode (EDI = -1.34) | V4 post-multiescala | Failure declarado y documentado | Reformulación de sonda con histéresis o datos VENLab reales |

---

## 2. Limitaciones empíricas declaradas

**Tabla A.0.2.**

**Tabla 4.5.2.**

| # | Limitación | Origen | Plazo | Entregable |
|---|-----------|--------|-------|------------|
| L7 | **Datos del corpus inter-escala son sintéticos** derivados de parámetros publicados | V4 post-multiescala | 6-12 meses | Elevación a datos reales abiertos: IBM Quantum, BRENDA, PhysioNet, OGLE, Gaia DR3 |
| L8 | **Escalas del corpus inter-escala son etiquetas nominales** sobre datos sintéticos | Idem | Idem | Documentado en cap 06-01 §8.2 |
| L9 | **6/30 casos con `overall_pass=True`** y gate completo en corpus inter-dominio (tras iter 7 B-T2 2026-05-17: 4 históricos + Urbanización iter 5 + Microplásticos iter 7) | Estado del corpus | No es defecto: es discriminación honesta | Reportado como hallazgo, no como debilidad |
| L10 | **Caso piloto COVID dimensión normativa** produjo null honesto (sonda continua simple inadecuada) | Piloto ejecutado | 18-24 meses | Sondas con histéresis y variables ordinales |

---

## 3. Limitaciones filosóficas declaradas

**Tabla A.0.3.**

**Tabla 4.5.3.**

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

**Tabla A.0.4.**

**Tabla 4.5.4.**

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

**Nota sobre el sistema QES (Quality of Evidence Score):** la métrica QES de auditoría interna es construcción del proyecto, no estándar reconocido en literatura externa de calidad de evidencia. No es GRADE ni AMSTAR. Sirve como filtro interno para distinguir casos con infraestructura adecuada y contenido empírico sustantivo de casos con sólo infraestructura. La afirmación "ningún caso del corpus es paper-science según QES" debe interpretarse como "ningún caso cae bajo el umbral interno de QES = 0.40"; la clasificación contra criterios externos (revisión por pares, GRADE) es deuda explícita L17.



Los siguientes módulos resuelven o reducen seis limitaciones sin re-ejecutar el corpus:

**Tabla A.0.5.**

**Tabla 4.5.5.**

| Módulo | Limitación afectada | Resolución | Ruta |
|--------|---------------------|------------|------|
| Calibración estadística | L1 (p-value mal calibrado) | Cerrada metodológicamente | `09-simulaciones-edi/common/calibration.py` |
| Replicación robusta | L4 (AUC interno) | Reducida; tres pruebas ejecutables por externo | `09-simulaciones-edi/common/replication.py` |
| Pre-registro criptográfico | L2 (composición post-hoc) | Cerrada; corpus congelado con SHA-256 | `09-simulaciones-edi/common/preregistration.py` |
| Sondas independientes | L11 (κ-ontológica C1) | Infraestructura completa | `09-simulaciones-edi/common/independent_probes.py`, `full_secondary_probes.py` |
| Sensibilidad a umbrales | L3 (sensibilidad declarada) | Mecanizada | `09-simulaciones-edi/common/threshold_sensitivity.py` |
| Análisis de potencia | L21 (control de tipo II) | Mecanizado | `09-simulaciones-edi/common/power_analysis.py` |

La corrección FWER Holm-Bonferroni sobre los 30 casos del corpus inter-dominio preserva 14 casos inter-dominio (más 8 inter-escala) tras Holm; los 6 casos macro `overall_pass=True` (post-iter-7 B-T2 2026-05-17) están entre los sobrevivientes: la clasificación strong sobrevive a la corrección por comparaciones múltiples.

### Reclasificación de casos bajo régimen calibrado

La aplicación caso por caso de los módulos a los casos no invariantes produce los siguientes veredictos:

**Tabla A.0.6.**

**Tabla 4.5.6.**

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

**Tabla A.0.7.**

**Tabla 4.5.7.**

| Categoría | n | Implicación |
|-----------|--:|-------------|
| No null (EDI > 0.10) | 23 | Casos con señal detectable |
| Null real (potencia ≥ 0.80) | 4 | Honestamente null bajo régimen actual |
| Null por potencia insuficiente | 13 | Falta de resolución; no afirmación de ausencia |

Esto introduce una distinción crítica que el manuscrito antes no tenía: **null estadístico ≠ ausencia ontológica**. Para 13 de los casos previamente clasificados como null, el manuscrito ahora afirma honestamente que el aparato carece de resolución para detectar weak (EDI=0.10) con potencia 0.80; necesitaría n ≥ 124 vs n actual entre 8 y 19.

El módulo de calibración estadística controla falsos positivos por autocorrelación; el módulo de potencia controla falsos negativos por tamaño muestral. Ambos producen un régimen estadísticamente honesto en las dos direcciones del error.

## 6. Cuadro síntesis para defensa oral

Si en defensa una limitación es señalada por el tribunal, la respuesta canónica del manuscrito es:

**Tabla A.0.8.**

**Tabla 4.5.8.**

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

## 8. Deuda residual (integración 2026-05-11)

Entradas operativas declaradas tras triage de bitácora huérfana del modo continuo. Cada deuda enlaza a código fuente versionado en `09-simulaciones-edi/common/`.

- **[TENG-05 2026-05-11 — caso 19 re-ejecutado; clasificación corregida]** El `metrics.json` previo del caso 19 (fase real) contenía `phases.real.edi.value=0.7278` mientras `(rmse_no_ode-rmse_abm)/rmse_no_ode = -0.000191` y `weighted_value = -0.000115` (JSON mezclado entre dos ejecuciones). **Re-ejecutado con perfil canónico (`HYPER_N_PERM=2999 HYPER_N_BOOT=1500 python3 validate.py`)** el 2026-05-11: nuevas cifras coherentes son EDI=0.00044, p_perm=0.433, CI=[0.00023, 0.00065], `overall_pass=False`. Caso 19 se reclasifica de "Trend Nivel 1*" a **null genuino** en `05-aplicaciones/07-mapa-aplicaciones-corpus.md:140`. **Caveats permanentes:** (i) `data/dataset.csv` PMEL/NOAA no estaba versionado, se usó proxy sintético calibrado a las estadísticas del run original — reproducción bit-a-bit exige fetch del CSV NOAA real; (ii) block-permutation no implementada en `hybrid_validator.py` (i.i.d. Phipson-Smyth), aunque con EDI≈0 y p=0.43 la conclusión null tiene margen amplio. **Deudas técnicas restantes (abiertas):** añadir assertion en `write_outputs()` de `hybrid_validator.py` que garantice `abs(value - (rmse_no_ode-rmse)/rmse_no_ode) < ε`; auditoría retroactiva sobre los 40 casos del corpus; implementar block-permutation. Origen: `Bitacora/2026-05-04-continuous-run/TENG-05-caso19-edi-inconsistencia-interna.md`; re-ejecución: `Bitacora/2026-05-11-sintesis-tesis/F5-A-caso19-reejecucion.md`.
- **[TENG-08 2026-05-11]** En `09-simulaciones-edi/common/hybrid_validator.py:892-926`, el criterio C1 está implementado como `c1 = c1_relative OR c1_absolute` con la rama (B) (absoluta) **sin requerir aporte ODE** sobre la baseline no-ODE. Esto permite C1=True con EDI<0 (8 fases del corpus listadas en el archivo de origen). Acción: cambiar la lógica a `c1_fallback` diagnóstico (Salida 2 con flag explícito), no a `c1=True` directo; re-correr corpus con la corrección. Origen: `Bitacora/2026-05-04-continuous-run/TENG-08-c1-or-fallback-permite-edi-negativo.md`.
- **[TENG-09 2026-05-11]** En `hybrid_validator.py:1560-1681`, la corrección de sesgo (BC) se calibra sobre train y se aplica a la serie completa (incluido val). El guarda actual sólo detecta degradación catastrófica; **no detecta sesgo bajo no-estacionariedad** del residuo BC en val. Acción: añadir test ADF (Augmented Dickey-Fuller) sobre el residuo BC en val con `α=0.05`; emitir warning en `metrics.json` cuando el residuo no sea estacionario. Origen: `Bitacora/2026-05-04-continuous-run/TENG-09-bias-correction-no-estacionariedad.md`.
- **[TENG-11 2026-05-11]** En `hybrid_validator.py:1167` y :1831-1833, el umbral de "viscosidad" del atractor es `relaxation_time > 1`, que es trivialmente verdadero salvo en degeneración numérica; además `c_visc` NO está en `overall_pass`. Defectos compuestos: criterio trivial + no incorporado al gate. Acción: parametrizar el umbral relativo a la escala temporal del caso (`relaxation_time > k · dt`) y decidir si `c_visc` se incorpora a `overall_pass` o se documenta como diagnóstico secundario. Origen: `Bitacora/2026-05-04-continuous-run/TENG-11-viscosidad-umbral-trivial.md`.

## 9. Cierre

Una tesis sin límites nombrados es una tesis que aún no se ha sometido a sí misma a su propio filtro. Esta tesis nombra 20 limitaciones explícitas con entregable. Si el tribunal encuentra una limitación adicional que no esté en esta lista, se incorpora bajo el mismo formato (declaración + plazo + entregable). La política es: **nada se oculta; todo se fecha.**
