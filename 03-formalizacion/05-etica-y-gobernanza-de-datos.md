# Ética de investigación y gobernanza de datos

## Función

Capítulo metodológico que documenta la política de manejo de datos del corpus EDI multidominio, las consideraciones éticas específicas por caso, la gobernanza de datos abiertos vs. propietarios, la política de reproducibilidad, y la declaración explícita de co-autoría con inteligencia artificial. Su existencia responde a la exigencia institucional de la Universidad de Antioquia y al estándar internacional vigente (COPE 2023, JAMA 2023, EU AI Act 2024).

## 1. Naturaleza de los datos del corpus

El corpus EDI consta de **30 casos**. Por su naturaleza de datos, se clasifican en cuatro categorías:

| Categoría | Cuenta | Casos | Implicaciones éticas |
|-----------|-------:|-------|----------------------|
| Datos públicos secundarios verificables | 22 | Energía, Deforestación, Kessler, Riesgo Bio, Microplásticos, Políticas, Postverdad, Urbanización, Fósforo, Wikipedia, Epidemiología, Movilidad, Finanzas, Salinización, Justicia, Starlink, Fuga cerebros, Clima, Contaminación, Océanos, Acidificación, Acuíferos | Mínimas: solo trazabilidad de fuente y cumplimiento de licencias |
| Datos públicos con sensibilidad media | 2 | Conciencia (proxy especulativo), IoT (telemetría agregada) | Bajas: agregación previa anula identificación |
| Datos sintéticos generados con parámetros publicados | 4 | Caso 30 (behavioral dynamics), Erosión, Paradigmas, los 3 controles de falsación | Ninguna: sin sujetos humanos directos |
| Datos humanos directos (futuro) | 0 actualmente / 1 planeado | Caso 30 elevado a LoE = 4 | **Significativas:** requiere aval CEI |

**Implicación clave:** en la versión actual del manuscrito (2026-04-28), **no hay manejo de datos personales identificables ni experimentación con sujetos humanos**. Por tanto, los 30 casos no exigen aval previo del Comité de Ética en Investigación (CEI). El aval se solicitará **únicamente** cuando el caso 30 incorpore datasets de captura de movimiento humano.

## 2. Política por caso del corpus

### 2.1. Casos con datos públicos secundarios

**Política:** trazabilidad completa de la fuente, cita de la institución que publica, cumplimiento de la licencia de cada dataset, reproducción mediante URLs documentadas o caché versionado.

**Fuentes principales y sus licencias:**

| Fuente | Licencia | Casos asociados |
|--------|----------|-----------------|
| World Bank Open Data | CC BY 4.0 | 16 Deforestación, 18 Urbanización, 27 Riesgo Biológico, 21 Salinización, 28 Fuga cerebros, 22 Fósforo |
| Our World in Data (OWID) | CC BY 4.0 | 04 Energía, 05 Epidemiología, 14 Postverdad, 13 Políticas |
| Open Power System Data (OPSD) | CC0 / dominio público | 04 Energía |
| CelesTrak (TLE) | dominio público | 20 Kessler, 26 Starlink |
| Jambeck et al. 2015 (publicado en *Science*) | uso secundario académico | 24 Microplásticos |
| Wikipedia API estadísticas | dominio público | 15 Wikipedia |
| Yahoo Finance / OECD | uso secundario académico | 09 Finanzas |
| OpenSky Network | CC BY-NC 4.0 | 11 Movilidad aérea |

**Trazabilidad:** cada caso documenta su fuente exacta en `09-simulaciones-edi/<caso>/case_config.json` y en su README específico.

### 2.2. Casos con datos sintéticos

**Política:** parámetros publicados en literatura revisada por pares + semilla determinística (`seed=42` por defecto) + reproducibilidad bit-a-bit verificada.

**Casos:**

- **Caso 30 (behavioral dynamics):** datos sintéticos generados con la ecuación completa de Fajen y Warren (2003) con cambios discretos de meta y ruido perceptivo realista. Los parámetros (b=3.25, k_g=7.50, c1=0.40, c2=0.40) son los publicados en la fuente original. La elección de generar datos sintéticos del sistema completo (no de la sonda EDI simplificada) evita la circularidad ABM ≡ ODE.
- **Controles de falsación (06, 07, 08):** ruido puro, random walk y estado oculto respectivamente, generados con semilla fija para reproducir la condición de falsación.
- **Casos null especulativos (02 Conciencia, 23 Erosión):** datos especulativos clasificados explícitamente como LoE = 1.

**Limitación reconocida:** los datos sintéticos no sustituyen datos reales. La tesis declara explícitamente esta limitación y compromete elevación del caso 30 a LoE = 4 con datos humanos como deuda priorizada.

### 2.3. Caso 30 elevado a LoE = 4 (ruta planeada)

Cuando el caso 30 se eleve con datos humanos:

**Datasets candidatos:**

| Dataset | Institución | Naturaleza | Licencia / Acceso |
|---------|-------------|------------|-------------------|
| VENLab (Brown University) | Warren Lab | Captura de movimiento en steering tasks | Acceso académico previa solicitud |
| WALK-MS Boston | Boston University | Locomoción humana en interiores | Académico, disponible |
| OpenLocomotionData | Consorcio académico | Locomoción dirigida múltiples laboratorios | Open Access bajo CC BY 4.0 |
| MoCap CMU | Carnegie Mellon | Captura general | Académico, disponible |

**Procedimiento ético:**

1. solicitud formal al laboratorio de origen del dataset, declarando uso académico secundario;
2. verificación de que el dataset original tenía consentimiento informado de participantes y permite reuso académico;
3. radicación de protocolo de investigación ante el **Comité de Ética en Investigación de la Universidad de Antioquia** (CEI sede Medellín) con justificación de reuso secundario;
4. cumplimiento de Ley 1581 de 2012 (Colombia) sobre protección de datos personales: en datos secundarios anonimizados, la ley se cumple manteniendo la anonimización del dataset de origen sin re-identificación;
5. declaración del cumplimiento en el manuscrito final;
6. archivado de la documentación del proceso ético en `Procesos/`.

**Hito condicional:** la elevación del caso 30 al nivel demostrativo con datos humanos no se ejecutará sin el aval CEI documentado.

## 3. Gobernanza de datos: abiertos vs. propietarios

**Compromiso institucional:** todos los datos primarios usados en el corpus son **abiertos** o **académicos con reuso permitido**. No se usan datos propietarios ni datos comerciales restringidos.

**Caché reproducible:** cada caso del corpus mantiene caché de los datos descargados en su carpeta `data_cache/` para garantizar reproducción aún si la fuente original cambia. La política de caché:

- caché versionado con fecha de descarga;
- hash SHA-256 verificable;
- compromiso de **no modificar el caché** una vez establecido;
- si la fuente original se actualiza, se anota en el log de caso pero el caché se preserva para reproducir el resultado publicado.

**Trazabilidad histórica:** la carpeta `Procesos/` documenta cada hito relevante de adquisición y procesamiento de datos.

## 4. Reproducibilidad

**Compromiso público:**

- código completo del aparato EDI publicado en repositorio (`09-simulaciones-edi/`);
- documentación de dependencias en `requirements.txt`;
- entorno aislado documentado (`.venv`, Docker disponible);
- semillas deterministas (`seed=42`) en todos los casos donde la estocasticidad es intencional;
- validación de determinismo: 29/29 casos pasan reproducibilidad bit-a-bit con semilla fija;
- los `metrics.json` de cada caso son la fuente de verdad numérica del manuscrito.

**Política de archivo a largo plazo:** antes de la sustentación pública, depósito del repositorio en Zenodo o equivalente con DOI permanente.

## 5. Declaración de co-autoría con inteligencia artificial

### 5.1. Marco normativo

La declaración se ajusta a:

- **COPE (Committee on Publication Ethics).** Posición de febrero 2023: las herramientas de IA no pueden ser autoras (no asumen responsabilidad), pero su uso debe declararse explícitamente.
- **JAMA Network (2023).** Política editorial: los autores humanos son responsables del contenido completo aún si fueron asistidos por IA; la asistencia de IA debe declararse en métodos.
- **Universidad de Antioquia.** Política institucional vigente al momento del depósito, que se consultará explícitamente con la Vicerrectoría de Investigación antes de la sustentación.
- **EU AI Act (2024).** Aunque Colombia no está bajo jurisdicción europea, el Act es referencia internacional sobre transparencia y declaración del uso de IA en producción intelectual.

### 5.2. Rol específico de la IA en esta tesis

Anthropic Claude (Opus 4.7) operó como **instrumento de implementación bajo dirección humana**, equivalente epistémico a un software estadístico avanzado. Específicamente:

| Tarea | Rol IA | Rol humano |
|-------|--------|------------|
| Tesis ontológica del irrealismo operativo | — | Jacob Agudelo (concepto original) |
| Conjetura del cierre operativo κ | — | Jacob Agudelo |
| Aparato formal (μ, G, H, κ, ε) | refactorización de redacción | Jacob Agudelo (concepto), Steven Vallejo (formalización) |
| Diseño del protocolo C1-C5 | sugerencias de redacción | Jacob Agudelo + Steven Vallejo |
| Implementación del corpus EDI computacional | asistente de codificación | Steven Vallejo (autoría técnica) |
| Selección de los 30 casos del corpus | sugerencias acotadas | Jacob Agudelo + Steven Vallejo |
| Sondas ODE específicas | implementación bajo guía | Steven Vallejo |
| Ejecución del corpus y producción de `metrics.json` | ejecución supervisada | Steven Vallejo |
| Redacción del manuscrito | asistencia activa de redacción | Jacob Agudelo + Steven Vallejo (revisión y aprobación) |
| Decisiones ontológicas, epistemológicas, metodológicas finales | — | autores humanos |
| Auditorías doctorales internas | redacción asistida | autores humanos (revisión final) |

### 5.3. Lo que la IA no hizo

- no decidió ninguna tesis ontológica, epistemológica o metodológica fundamental;
- no produjo ningún resultado del corpus EDI sin revisión humana de los `metrics.json`;
- no eligió las posiciones rivales del capítulo 04-01;
- no generó la conjetura κ ni la métrica EDI;
- no interpretó los resultados del corpus en términos filosóficos sin revisión humana.

### 5.4. Responsabilidad

La responsabilidad académica completa del manuscrito reside en los autores humanos: Jacob Agudelo (autoría principal) y Steven Vallejo Ortiz (colaborador técnico). La IA es declarada herramienta, no autora.

## 6. Limitaciones honestas en gobernanza

- **Datos cacheados:** algunos casos del corpus dependen de fuentes con políticas de actualización que pueden cambiar; el caché protege la reproducibilidad pero no garantiza acceso futuro a datos vivos. La tesis acepta esta limitación.
- **Versiones de software:** las dependencias en `requirements.txt` están pineadas a versiones específicas. Cambios futuros en bibliotecas pueden requerir adaptación. El compromiso es mantener compatibilidad documentada por al menos 5 años post-defensa.
- **Datos humanos pendientes:** el caso 30 elevado a LoE = 4 sigue siendo deuda; la política ética está documentada para ese momento, pero la ejecución no ha ocurrido al cierre de esta versión.
- **Co-autoría con IA en tesis doctoral:** la política institucional de la Universidad de Antioquia sobre IA en producción de tesis está en evolución (2024–2026). El manuscrito se ajustará a la versión vigente al momento del depósito; los autores se comprometen a actualizar esta declaración si la política cambia.

## 7. Política de errores y correcciones

**Compromiso público:** si tras la sustentación se detecta error en datos, código o cálculo del corpus, los autores se comprometen a:

- publicar erratum en el repositorio público con fecha y naturaleza del error;
- recalcular las cifras afectadas;
- revisar si el error afecta conclusiones del manuscrito;
- en caso de impacto material, publicar versión corregida con nota de modificación.

## 8. Lectura cruzada

- Formalización institucional: capítulo `00-proyecto/04-formalizacion-institucional.md`.
- Política de adquisición de datos humanos para caso 30: `Procesos/2026-04-28-cierre-doctoral/02-programa-datos-humanos-caso30.md`.
- Trazabilidad de procesos: `Procesos/`.
- Bibliografía completa: capítulo `07-bibliografia/01-bibliografia-orientativa.md`.
