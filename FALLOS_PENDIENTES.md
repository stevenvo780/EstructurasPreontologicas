# Fallos sustantivos pendientes

Inventario brutal de los 34 fallos detectados en auditoría profunda con tres lentes (filosófica, científica, formal/institucional). No incluye correcciones cosméticas; lista debilidades de fondo que un comité doctoral exigente o un revisor Q1 señalaría.

Los fallos de auto-indulgencia narrativa de iteraciones anteriores ya fueron corregidos y archivados en `Bitacora/2026-04-28-iteraciones-IA/REPORTE_AUTOINDULGENCIAS.md`.

> **Estado 2026-04-28:** los fallos atendibles por la asistencia computacional (F4, F7, F8, F11–F15, F18–F22, F27–F34) están auditados en `REPORTE_CIERRE_TECNICO.md`. F13 cerrado parcialmente: el método circular fue reemplazado por sondas sobre arrays primarios reales (sólo 7 casos disponibles; convergencia honesta 1/7 bajo |ΔEDI|≤0.10). Permanecen abiertos: F1–F3, F5, F6, F9, F10 (filosóficos de fondo); F16, F17 (datos reales + calibración externa de QES); F23–F26 (institucionales).

---

## A. Fallos filosóficos de fondo (10)

| # | Fallo | Ubicación | Tipo |
|--:|-------|-----------|------|
| F1 | Circularidad κ-pragmática vs κ-ontológica: la "realidad moderada" se define como "lo que el aparato detecta"; la distinción colapsa bajo presión. | Cap 02-01 §0.3 + cap 02-06 §1 | Argumento circular |
| F2 | Petición de principio en identidad-como-cuenca: la cuenca solo se define si la identidad ya existe; no la explica, la renombra. | Cap 02-03 §4 | Petición de principio |
| F3 | Salto lógico de "operador formal multiescalar" a "una sola ontología subyacente": el aparato presupone invarianza y luego la "demuestra" sobre 40 casos tratados con el mismo aparato. | Cap 02-01 §1 | Salto inductivo |
| F4 | "Atractor empírico" sin rigor topológico estándar: cinco condiciones de admisión vagas, sin métrica formal (Lyapunov, dimensión de correlación, espectro de bifurcación). | Cap 02-01 §2.2 | Concepto vago |
| F5 | Naturalismo metafísico adoptado con razones operativas, no filosóficas: "no funciona con el aparato" no refuta dualismo, idealismo, panpsiquismo. | Cap 02-01 §0.1 | Argumento operativo donde se necesita argumento ontológico |
| F6 | Citas decorativas de Simondon, Gibson, Dennett, Searle, Bunge: invocados como autoridad sin engagement con sus argumentos sustantivos. Simondon define lo pre-individual como metaestable (potencia plural); la tesis lo usa como sinónimo de bifurcación de estabilidades — opuestos conceptuales. | Cap 02-01 §11.5; cap 02-04 §10.1 | Apropiación superficial |
| F7 | Dimensión normativa contradictoria: cap 02-06 afirma "normas son atractores reales"; cap 04-02 §4 admite "el aparato no captura la dinámica normativa". | Cap 02-06 §1 vs cap 04-02 §4 | Inconsistencia inter-capítulos |
| F8 | "Información ecológica" usa dos clasificaciones ontológicas incompatibles: realidad fuerte (diferencia materializada) y realidad estructural (tipo 2). | Cap 02-04 §2.3 vs §5 | Inconsistencia conceptual |
| F9 | Asimetría L1↔B↔L3↔S es terminológica, no ontológica: B↔L3 es equivalencia; la "asimetría" sólo opera entre L1 y {B,L3,S}, lo cual es trivial. | Cap 02-04 §8 | Distinción inflada |
| F10 | Dimensiones omitidas que un comité humanista exigirá: estética, política como conflicto de poder, género, descolonialidad, espacio como dimensión ontológica, mereología. | Estructura general | Omisión sistemática |

---

## B. Fallos científicos sustantivos (12)

| # | Fallo | Ubicación | Tipo |
|--:|-------|-----------|------|
| F11 | EDI sin fundamento normativo de rangos: matemáticamente correcto pero sin justificación de por qué 0.30 es "strong" y no 0.20 o 0.40. Sensible al rango/normalización. Las series no se estandarizan. | `hybrid_validator.py:137`; cap 03-04 | Métrica ad-hoc |
| F12 | FWER Holm-Bonferroni anunciado pero no aplicado al corpus: los `metrics.json` reportan p-values sin corrección. Caso 16 con p=0.7167 (no significativo) clasifica ROBUSTO. | `quality_scorer.py` Q0; outputs caso 16 | Inconsistencia anuncio/implementación |
| F13 | Sondas secundarias evaluadas sobre proxys sintéticos derivados del EDI publicado, no sobre arrays primarios. El criterio C1 de κ-ontológica fuerte queda sin verificar. | `full_secondary_probes.py`; `run_full_secondary_probes.py` | Validación circular |
| F14 | Block bootstrap no es Politis-Romano auténtico: el código implementa moving block con tamaño √n; el docstring afirma stationary bootstrap. Cita técnica falsa. | `calibration.py:64-135` | Cita técnica incorrecta |
| F15 | Baselines competitivos ausentes: no hay comparación contra ARIMA, VAR, SARIMA, RNN, modelos de espacio de estado. El "baseline" es `rmse_abm_no_ode`, una versión truncada del propio modelo. | Cap 03-04; corpus completo | Comparación contra paja |
| F16 | Datos del corpus inter-dominio mayormente sintéticos pese a declarar fuentes públicas. FETCH_MANIFEST con sha256 pero archivos pre-generados sin descarga real verificable. | Casos 1-30; FETCH_MANIFEST.json | Trazabilidad empírica débil |
| F17 | QES con umbrales auto-instalados: pesos y umbrales elegidos por el equipo. Los "8 ROBUSTO" son artefacto de la calibración interna, no validación externa. | `quality_scorer.py:51-60` | Métrica circular |
| F18 | Q0 puntúa por valor de EDI sin gate de significancia estadística: caso con EDI=0.04 y p=0.72 obtiene Q0=1.00. Viola convención estadística. | `quality_scorer.py:108-120` | Lógica estadística rota |
| F19 | Caso 30 con dos clasificaciones contradictorias: PROGRAMÁTICO en QES_AUDIT, PILOTO en Anexo A.0. | QES_AUDIT_REPORT.md vs Anexo A.0 | Inconsistencia entre reportes |
| F20 | Paneles `extend_*.py` son pseudo-replicación: simulaciones idénticas con ruido aleatorio distinto, no datos de unidades reales independientes. n_effective inflado. | `scripts/extend_03_*.py`, `extend_12_*.py`, `extend_19_*.py`, `extend_30_*.py` | Inflación de potencia |
| F21 | Q5 simétrica: penaliza divergencia inter-paradigma sin distinguir cuál sonda falla. Si la primaria es la motivada teóricamente y la secundaria es de prueba, la divergencia indica que la secundaria es inadecuada — pero el sistema penaliza ambas igual. | `quality_scorer.py:292-330` | Asimetría no modelada |
| F22 | "Pre-registro criptográfico" es post-hoc: el SETUP_HASH se calcula después de ejecutar e incluye archivos generados durante la ejecución. Es auditoría criptográfica de cambios, no pre-registro. | `common/preregistration.py` | Cita procedimental falsa |

---

## C. Fallos formales / institucionales (12)

| # | Fallo | Ubicación | Tipo |
|--:|-------|-----------|------|
| F23 | Director de tesis no declarado (BLOQUEADOR PROCEDIMENTAL ÚNICO). Sin esto, depósito imposible. | Frontmatter del manuscrito | Bloqueador institucional |
| F24 | Portada no cumple formato institucional U. de Antioquia (logo, grado, tribunal, firmas). | Frontmatter | Formato institucional |
| F25 | Falta declaración de originalidad firmada. | Frontmatter | Requisito institucional |
| F26 | Falta página formal de conflicto de interés. La declaración de co-autoría con IA está dispersa, no consolidada en página formal. | Frontmatter | Requisito institucional |
| F27 | Referencias decorativas: Kant, Psillos, van Fraassen, Harman aparecen 0 veces en el cuerpo argumental. | `07-bibliografia/01-bibliografia-orientativa.md` | Bibliografía inflada |
| F28 | Duplicación de interlocutores principales: Bunge es interlocutor principal en cap 02-01, 03-02 y 03-03 (viola la promesa de "3 fuentes nucleares distintas por capítulo"). | Cap 07 + asignaciones | Inconsistencia editorial |
| F29 | Inconsistencia de formato Chicago author-date: mezcla "&" y "y", "et al." sin estandarizar, "1781/1998" vs reediciones sin justificación. | Cuerpo del manuscrito | Formato bibliográfico |
| F30 | 23 anexos cuando el estándar doctoral colombiano es 5–7. Sugiere falta de síntesis editorial. | Anexos A.0–A.12 + B.1–B.9 | Sobreproducción de anexos |
| F31 | 30–40 % de tablas sin numeración formal (Tabla 1.1, Tabla 5.2, etc.). | Cuerpo del manuscrito | Formato de tablas |
| F32 | Figuras Mermaid no son calidad Q1: serían rechazadas por revistas exigentes. Requieren conversión a TikZ/Graphviz/SVG vectorial. | Anexo A.10 | Calidad gráfica |
| F33 | Falta visualización del corpus de 42 casos: no hay scatter plot por escala/dominio, ni espacio de fase del caso ancla, ni curvas comparativas EDI vs baselines. | Cap 09 + Anexo A.10 | Visualización ausente |
| F34 | Glosario A.1 incompleto: faltan 8–10 términos clave usados en el cuerpo (flecha termodinámica, eternalismo moderado, mutual manipulability, intervención ablativa, downward constitution explícita, exclusion argument de Kim). | Anexo A.1 | Glosario incompleto |

---

## Síntesis cuantitativa

| Categoría | n | Severidad típica |
|-----------|--:|------------------|
| Filosóficos de fondo | 10 | 3 críticos, 4 graves, 3 serios |
| Científicos sustantivos | 12 | 5 críticos, 4 graves, 3 serios |
| Formales/institucionales | 12 | 1 crítico (BLOQUEADOR único), 4 graves, 7 menores |

**Bloqueador procedimental único:** F23 (director). Sin esto, depósito imposible.

**Tiempo realista para cierre completo:** 4–6 meses de trabajo serio (no 2–3 semanas). Antes de sustentación institucional U. de Antioquia con estándar más permisivo: 6–8 semanas si se priorizan los bloqueadores procedimentales y los fallos formales más visibles.

La asignación de quién puede cerrar cada fallo está en `TAREAS_POR_RESPONSABLE.md`.
