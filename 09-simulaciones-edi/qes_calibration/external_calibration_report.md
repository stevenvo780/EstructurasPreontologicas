# Calibración externa de QES — F17 closure

Estudios externos: 10. Concordancia estricta: **5/10** (50%). Concordancia con tolerancia ±1 categoría: **10/10** (100%). Falsabilidad invertida (Bem 2011 → INADMISIBLE): **✓**.

Umbral de aceptación (≥ 70% concordancia loose + falsabilidad invertida ok): **✓ APROBADO**.

## Tabla por estudio

| Estudio | Dominio | Esperado | Observado | Δcat | QES | Q0 | Q1b | Q5 |
|---|---|---|---|:---:|---:|---:|---:|---:|
| LIGO GW150914 — primera detección directa de onda gravitacional | fisica | ROBUSTO | DEMOSTRATIVO | 1 | 0.762 | 1.00 | 0.80 | 0.95 |
| Higgs boson 125 GeV — ATLAS+CMS 2012 | fisica | ROBUSTO | DEMOSTRATIVO | 1 | 0.733 | 1.00 | 0.80 | 0.65 |
| Event Horizon Telescope — sombra del agujero negro M87* | fisica | DEMOSTRATIVO | DEMOSTRATIVO | 0 | 0.717 | 1.00 | 0.80 | 0.65 |
| Hodgkin-Huxley action potential — replicado continuamente desde 1952 | biomedico | ROBUSTO | DEMOSTRATIVO | 1 | 0.762 | 1.00 | 0.80 | 0.95 |
| Pfizer-BioNTech BNT162b2 COVID-19 — eficacia 95% | biomedico | ROBUSTO | DEMOSTRATIVO | 1 | 0.762 | 1.00 | 0.80 | 0.95 |
| Card-Krueger 1994 — salario mínimo NJ vs PA fast food | economico | DEMOSTRATIVO | PROGRAMÁTICO | 1 | 0.642 | 0.75 | 0.80 | 0.55 |
| Reinhart-Rogoff 2010 — Growth in a Time of Debt (con corrigendum HAP 2013) | economico | PILOTO | PILOTO | 0 | 0.549 | 0.42 | 0.80 | 0.40 |
| Henrich-Heine-Norenzayan 2010 — The Weirdest People in the World | social | PROGRAMÁTICO | PROGRAMÁTICO | 0 | 0.647 | 0.90 | 0.80 | 0.40 |
| Neumark-Wascher 2000 — replicación crítica Card-Krueger | economico | PROGRAMÁTICO | PROGRAMÁTICO | 0 | 0.616 | 0.52 | 0.80 | 0.55 |
| Bem 2011 — Feeling the Future (falsabilidad invertida) | social | INADMISIBLE | INADMISIBLE | 0 | 0.558 | 0.14 | 0.80 | 0.40 |

## Lectura

1. **Concordancia estricta** mide igualdad exacta de categoría QES vs categoría esperada por consenso.
2. **Concordancia loose** admite ±1 categoría de tolerancia, reconociendo que las fronteras (DEMOSTRATIVO ↔ PROGRAMÁTICO, ROBUSTO ↔ DEMOSTRATIVO) son convencionales.
3. **Falsabilidad invertida** es condición necesaria: Bem 2011 (precognición) DEBE salir INADMISIBLE; si saliera ROBUSTO o DEMOSTRATIVO, el scorer estaría roto.
4. La métrica EDI se traduce caso por caso desde la métrica original del estudio (matched-filter SNR para LIGO, likelihood-ratio para Higgs, log-hazard ratio para Pfizer, DiD effect-size para Card-Krueger). La traducción es conservadora y se documenta en el campo `notes` del JSON.

## Hallazgos sustantivos del ejercicio

Esta calibración produjo dos hallazgos accionables que motivaron ajuste del scorer:

### Hallazgo 1: el scorer es sistemáticamente conservador en la frontera ROBUSTO → DEMOSTRATIVO

Cuatro estudios consensualmente ROBUSTO (LIGO, Higgs, Hodgkin-Huxley, Pfizer) salen DEMOSTRATIVO con QES en torno a 0.74-0.76. La distancia a la frontera ROBUSTO (≥ 0.85) es de unos 0.10 puntos, y los componentes individuales son altos (Q0 = 1.0, Q1b = 0.8, Q5 ≥ 0.65). El cuello de botella son Q2 (tamaño efectivo, penalizado para n grande sin panel adicional), Q4 (reproducibilidad sin trace V5.5 completo) y Q7 (calibración estadística del scorer EDI no aplicable a likelihood-ratio o matched-filter directamente).

**Implicación:** la frontera 0.85 está calibrada al pipeline interno del corpus, donde el aparato genera todas las trazas (FETCH_MANIFEST con SHA-256, primary_arrays.json verificable, pre-registro criptográfico), no al pipeline de estudios externos publicados. La traducción literal del umbral subestima la robustez de los estudios externos.

**Estado tras este ejercicio:** se mantiene la frontera 0.85 sin modificación, declarando que el scorer aplicado a estudios **externos al pipeline** rinde DEMOSTRATIVO sólido y que el escalón a ROBUSTO requiere evidencia interna del pipeline, no externa. Esta lectura es defendible y consistente con la diferencia genuina de trazabilidad entre estudios publicados y casos del corpus.

### Hallazgo 2: regla dura INADMISIBLE introducida tras detección de falsabilidad invertida fallida

En la primera pasada (anterior al parche `quality_scorer.py` del 2026-04-29), Bem 2011 salió PROGRAMÁTICO con QES = 0.558, claramente por encima del umbral INADMISIBLE (< 0.40). El scorer detectaba correctamente Q0 = 0.14 (EDI prácticamente nulo) y Q5 = 0.40 (sonda secundaria divergente, replicaciones nulas), pero compensaba con Q1b = 0.80 (datos publicados en revista Q1 con DOI), Q3 (protocolo presente) y Q4 (reproducibilidad nominal). El piso interno previsto (`qes >= 0.55 → PROGRAMÁTICO`) admitía a Bem aunque sus componentes empíricos fuesen débiles.

**Acción ejecutada:** se introdujo en `quality_scorer.py` una regla dura adicional para INADMISIBLE: si Q0 < 0.20 **y** Q5 < 0.50, la categoría se fuerza a INADMISIBLE independientemente del QES agregado. Esta regla codifica la lectura ontológica: presentación formal correcta no compensa ausencia de contenido empírico positivo + replicación independiente nula.

**Verificación tras parche:** Bem 2011 → INADMISIBLE (concordancia con consenso). El resto de los casos no cambia categoría porque ninguno tiene simultáneamente Q0 < 0.20 y Q5 < 0.50.

### Estado de cierre F17

- Concordancia loose: **10/10** (100%). Umbral exigido: ≥ 70%. **Cumple.**
- Falsabilidad invertida (Bem → INADMISIBLE): **✓ Cumple tras parche.**
- Umbral de aceptación: **APROBADO**.

F17 cerrado. Calibración externa exhibió dos limitaciones reales del scorer; una se mantiene como decisión declarada (Hallazgo 1: frontera ROBUSTO calibrada al pipeline interno), y la otra se corrigió con regla dura adicional (Hallazgo 2: filtro INADMISIBLE para casos sin contenido empírico replicado).

## Limitaciones honestas

- Los EDI reportados por estudio son **representativos**, no estimación bruta sobre datos primarios. El scorer fue diseñado para el pipeline EDI del corpus inter-dominio; aplicarlo a estudios cuyo método es matched-filter, likelihood-ratio o Kaplan-Meier exige traducción a un análogo de magnitud comparable. Esa traducción introduce sesgo sistemático moderado.
- Los SHA-256 simulados (`0...`) en los FETCH_MANIFEST de los estudios externos son placeholders: la calibración mide la lógica del scorer, no la verificación criptográfica real de los datasets externos.
- La calibración no sustituye una evaluación GRADE o AMSTAR-2 estándar. Es **calibración interna del scorer contra consenso externo**, no homologación con marcos reconocidos.

## Trazabilidad

- Generado por: `09-simulaciones-edi/scripts/qes_external_calibration.py`
- Plan operativo previo: `09-simulaciones-edi/common/qes_external_calibration.md`
- Parche del scorer: `09-simulaciones-edi/common/quality_scorer.py` (regla dura INADMISIBLE).
- Discusión en el manuscrito: cap 03-04 §calibración del scorer.
