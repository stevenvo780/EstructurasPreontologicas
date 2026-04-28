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

## 2. Dirección y co-dirección

**Director(a) de tesis:** [pendiente de designación formal por el Consejo de Facultad].

**Co-director(a) de tesis (si aplica):** [pendiente de designación].

**Asesores externos en la línea técnica (consulta no oficial):** [a documentar].

> Esta sección queda con marcador explícito para ser completada cuando el Comité Doctoral del programa haga la designación formal. Mientras eso no ocurra, el manuscrito se circula como **prototipo doctoral avanzado**, no como tesis lista para sustentación. El paso de prototipo a tesis depende del aval institucional explícito.

## 3. Comité de evaluación

**Comité de tesis (designación formal pendiente):** [a llenar].

**Criterios de composición sugeridos al programa:**

- al menos un evaluador con dominio en filosofía de la mente y filosofía de la complejidad;
- al menos un evaluador con dominio en ontología analítica y ontología social;
- al menos un evaluador con experiencia en ciencias computacionales aplicadas a sistemas dinámicos (ABM, ODE, validación cuantitativa);
- al menos un evaluador externo a la Universidad de Antioquia, internacional si es posible, con publicación reciente en cualquiera de los tres dominios anteriores.

**Conflictos de interés declarables:** ninguno conocido al momento de redactar esta versión del manuscrito. La declaración formal se entregará en el formato institucional cuando proceda.

## 4. Cronología institucional declarada

| Hito | Estado | Fecha estimada |
|------|--------|----------------|
| Inscripción al programa | [pendiente / completado] | [fecha] |
| Aprobación del proyecto de tesis por Consejo de Facultad | [pendiente] | — |
| Designación de director(a) y co-director(a) | [pendiente] | — |
| Examen de candidatura | [pendiente] | — |
| Seminarios doctorales requeridos | [pendiente] | — |
| Aval de comité de ética (cuando aplique) | [pendiente] | — |
| Carta de aval del director para depósito | [pendiente] | — |
| Sustentación pública | [pendiente] | — |

> La fuente de verdad de estos hitos es el sistema institucional (SIIU, sistema académico de posgrados). Esta tabla es resumen orientativo, no documento sustitutivo.

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
- la trazabilidad histórica del proyecto (Procesos/) permite reproducción del crecimiento del corpus paso a paso;
- los `metrics.json` versionados en cada caso son la fuente de verdad numérica;
- los datos públicos secundarios (World Bank, OWID, OPSD, CelesTrak, etc.) están cacheados o reproducibles vía URLs documentadas;
- los datos sintéticos del caso 30 son reproducibles bit-a-bit con `seed=42`.

**Compromiso de archivado largo plazo:** depósito en Zenodo o equivalente con DOI antes de la sustentación.

## 9. Carta de aval del director para depósito

> Sección reservada para la inclusión de la carta firmada por el director(a) de tesis avalando el manuscrito para sustentación pública. Esta carta, junto con el acta de comité, son requisito de admisibilidad institucional.

## 10. Estado de la formalización al cierre de esta versión

A la fecha **2026-04-28**, la formalización institucional de la tesis está **incompleta** en los siguientes puntos:

- designación formal de director y comité;
- aprobación oficial del proyecto por Consejo de Facultad;
- carta de aval del director;
- aval específico del Comité de Ética (relevante solo para la elevación del caso 30 con datos humanos).

Estos elementos son **bloqueantes** para sustentación, pero no para la consolidación del manuscrito como **prototipo doctoral avanzado**. La trayectoria de cierre se documenta en el capítulo `06-cierre/03-hoja-de-ruta-para-tesis-final.md`.

## 11. Lectura cruzada

- Política de manejo de datos por caso: `03-formalizacion/05-etica-y-gobernanza-de-datos.md`.
- Hoja de ruta hacia depósito y sustentación: `06-cierre/03-hoja-de-ruta-para-tesis-final.md`.
- Trazabilidad del proceso de construcción: `Procesos/`.
- Auditorías doctorales internas: `Procesos/2026-04-27-integracion-jacob/04-auditoria-doctoral-v1.md` y la auditoría v2 al cierre del manuscrito.
