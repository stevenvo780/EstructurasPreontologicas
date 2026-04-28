# Formalización institucional

## Función

Capítulo de constancia formal del marco institucional de la tesis ante la **Universidad de Antioquia**. Reúne los elementos que el Reglamento Estudiantil de Posgrado y los acuerdos académicos de la institución exigen para que el manuscrito pueda ser sometido a sustentación pública: programa, dirección, comité, ética, propiedad intelectual y co-autoría con IA. Cuando el comité doctoral apruebe formalmente cada uno de estos elementos, este capítulo será firmado y se anexará al expediente del estudiante.

## 1. Programa académico

**Programa de inscripción:** Doctorado en Filosofía, Universidad de Antioquia. Línea de investigación: filosofía de la ciencia y ciencias de la complejidad. La tesis se inscribe explícitamente en filosofía y no en ciencia computacional pura: el aparato cuantitativo (corpus EDI) opera al servicio de una tesis ontológica y epistemológica.

**Modalidad:** investigación doctoral con desarrollo computacional acoplado. La validación empírica multidominio es parte estructural del trabajo, no apéndice.

**Marco normativo aplicable:**

- Reglamento Estudiantil de Posgrado de la Universidad de Antioquia (vigente).
- Acuerdo Académico del Consejo de Facultad correspondiente al programa.
- Política institucional sobre integridad académica y uso de inteligencia artificial en producción intelectual (versión vigente al momento del depósito).
- Resolución sobre propiedad intelectual de la Vicerrectoría de Investigación.

## 2. Dirección de tesis

La tesis se desarrolla bajo asesoría académica institucional dentro del programa doctoral. La dirección verifica el cumplimiento curricular del proyecto, el rigor argumental del manuscrito y la integridad metodológica del corpus EDI.

Los autores entregan el manuscrito en estado **integral defendible**: con arquitectura argumental cerrada, aparato empírico funcional verificado, discriminación pública contra rivales identificables, y trazabilidad documentada de proceso. Cualquier ajuste posterior corresponde al ciclo normal de revisión y sustentación.

## 3. Composición sugerida del comité de evaluación

Para una evaluación equilibrada el manuscrito sugiere al programa un comité que cubra cuatro perfiles:

- evaluador con dominio en filosofía de la mente y filosofía de la complejidad;
- evaluador con dominio en ontología analítica y ontología social;
- evaluador con experiencia en ciencias computacionales aplicadas a sistemas dinámicos (ABM, ODE, validación cuantitativa);
- evaluador externo a la Universidad de Antioquia, con publicación reciente en cualquiera de los tres dominios anteriores.

**Conflictos de interés declarables:** ninguno conocido al cierre de esta versión del manuscrito.

## 4. Cronología institucional

La trayectoria académica del trabajo doctoral, los seminarios cumplidos y el plan de sustentación se gestionan por los canales institucionales del programa (SIIU y sistema académico de posgrados). El manuscrito se ajusta a las exigencias de fondo y forma del Reglamento Estudiantil de Posgrado vigente.

## 5. Aval de comité de ética

La tesis no involucra experimentación con sujetos humanos en su estado actual: todos los datos del corpus EDI son **datos públicos secundarios** o **datos sintéticos generados con parámetros publicados**. Por tanto, en la versión 2026-04-28 del manuscrito **no se requiere aval explícito de comité de ética** para los 30 casos del corpus.

**Excepción reservada:** la elevación del **caso 30 (behavioral dynamics)** al nivel demostrativo con LoE = 4 implica **adquisición o uso secundario de datos de captura de movimiento humano** (candidatos: VENLab Brown, WALK-MS Boston, OpenLocomotionData, MoCap CMU). En ese momento, antes de re-ejecutar el caso con datos humanos, se solicitará:

- aval del Comité de Ética en Investigación de la Universidad de Antioquia (CEI sede Medellín);
- verificación de que cada dataset utilizado tiene consentimiento informado del estudio original y permite reuso académico;
- declaración de protocolo de tratamiento de datos personales según Ley 1581 de 2012 (Colombia) y normativa equivalente en jurisdicciones del dataset.

El procedimiento detallado se documenta en el capítulo `03-formalizacion/05-etica-y-gobernanza-de-datos.md`.

## 6. Propiedad intelectual y autoría

**Autoría conceptual y dirección teórica:** Jacob Agudelo, Universidad de Antioquia. Es la autoría principal: la tesis ontológica del **irrealismo operativo de estructuras pre-ontológicas** y la conjetura del cierre operativo κ son su contribución conceptual original.

**Autoría técnica y de ingeniería:** Steven Vallejo Ortiz. Aporta la implementación del aparato EDI computacional (corpus, motor ABM+ODE, infraestructura de validación canónica), la ejecución del corpus multidominio y el ensamblado del repositorio.

**Co-autoría con inteligencia artificial:** Anthropic Claude (Opus 4.7). Su rol es **instrumento de implementación bajo dirección humana**, no autoría conceptual. Específicamente:

- la IA opera como asistente de redacción, refactorización de código y ensamblado documental;
- ninguna decisión ontológica, epistemológica o metodológica fundamental fue tomada por la IA sin revisión humana explícita;
- los criterios C1-C5, el aparato formal, las hipótesis del corpus y el contenido filosófico son humanos;
- la IA no aparece como autora en el sentido legal ni epistémico: aparece como herramienta declarada, igual que cualquier software estadístico.

Esta declaración se ajusta a las recomendaciones de COPE (Committee on Publication Ethics, 2023), las pautas del *Journal of the American Medical Association* (2023), y las versiones publicadas hasta el 2026 de las políticas de la Universidad de Antioquia sobre uso de IA en producción académica.

**Propiedad intelectual del manuscrito:** según la política vigente de la Universidad de Antioquia, la propiedad intelectual de la tesis pertenece al estudiante y, conjuntamente, a la institución en lo que respecta a su uso académico. La cesión específica de derechos se firma en el momento del depósito, según formato del programa.

**Licencia del repositorio computacional:** los archivos del repositorio (capítulos del manuscrito, código del aparato EDI, datos cacheados secundarios) se publican bajo licencia compatible con uso académico abierto (a definir en consulta con la Vicerrectoría de Investigación: típicamente CC BY-NC-SA 4.0 para texto, MIT o Apache 2.0 para código).

## 7. Declaración de conflictos de interés

Los autores declaran no tener conflictos de interés financieros con los datasets o herramientas computacionales empleados en el corpus EDI multidominio. La infraestructura de cómputo (2 GPUs RTX 5070 Ti / RTX 2060, 32 hilos CPU, 123 GB RAM) es propia del colaborador técnico (Steven Vallejo Ortiz). No hay financiamiento externo dirigido a la tesis salvo, eventualmente, becas doctorales y programas institucionales de la Universidad de Antioquia que se declararán formalmente en el momento del depósito.

## 8. Disponibilidad de código y datos (open science)

Compromiso público:

- el repositorio del manuscrito y del aparato EDI está disponible en repositorio público controlado por los autores;
- la trazabilidad histórica del proyecto (Bitacora/) permite reproducción del crecimiento del corpus paso a paso;
- los `metrics.json` versionados en cada caso son la fuente de verdad numérica;
- los datos públicos secundarios (World Bank, OWID, OPSD, CelesTrak, etc.) están cacheados o reproducibles vía URLs documentadas;
- los datos sintéticos del caso 30 son reproducibles bit-a-bit con `seed=42`.

**Compromiso de archivado largo plazo:** depósito en Zenodo o equivalente con DOI antes de la sustentación.

## 9. Estado del manuscrito

El manuscrito se entrega en estado **integral defendible**:

- arquitectura argumental cerrada (capítulos 02 a 06);
- aparato formal completo (capítulo 03);
- corpus EDI multidominio con resultados verificables (`09-simulaciones-edi/`, `Anexos/A8`);
- programa multi-sonda y baselines estadísticos ejecutados (`Bitacora/2026-04-28-cierre-doctoral/`);
- caso 30 (behavioral dynamics) con dossier técnico-ético para elevación documentada;
- bibliografía consolidada (`07-bibliografia/01-bibliografia-orientativa.md`);
- trazabilidad de proceso documentada (`Bitacora/`).

## 10. Lectura cruzada

- Política de manejo de datos por caso: `03-formalizacion/05-etica-y-gobernanza-de-datos.md`.
- Hoja de ruta del cierre doctoral: `06-cierre/03-hoja-de-ruta-para-tesis-final.md`.
- Trazabilidad del proceso de construcción: `Bitacora/`.
- Auditorías doctorales internas: `Bitacora/2026-04-27-integracion-jacob/04-auditoria-doctoral-v1.md` y `Auditoria_Doctoral.md` (v2).
