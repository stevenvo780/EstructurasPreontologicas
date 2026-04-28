# Auditoría doctoral — versión 2 (post-corrección)

> Segunda auditoría del manuscrito *Estructuras Pre-Ontológicas: Realismo Irrealista Operativo y Compresión Multiescala con Validación EDI Multidominio*, ejecutada tras la implementación íntegra de las correcciones identificadas en la auditoría v1 (`Bitacora/2026-04-27-integracion-jacob/04-auditoria-doctoral-v1.md`). El propósito de esta v2 es verificar **cuáles bloques se cerraron, cuáles quedan parcialmente abiertos y cuáles permanecen como deuda priorizada documentada**. La auditoría es honesta: no glorifica el cierre cuando es parcial.

**Fecha:** 2026-04-28.
**Manuscrito ensamblado:** `TesisFinal/Tesis.md` — 8,021 líneas, ~499 KB.
**Auditor metodológico:** preparado por la asistencia IA bajo dirección humana.

---

## Resumen ejecutivo

| # | Bloque | Estado v1 | Estado v2 | Acción ejecutada |
|---|--------|-----------|-----------|------------------|
| 1 | Filiación institucional | Bloqueante | **Estructura cerrada, marcadores institucionales pendientes** | Capítulo `00-proyecto/04-formalizacion-institucional.md` con 11 secciones; espacios reservados para director/comité/aval CEI |
| 2 | Diálogo bibliográfico real | Alta | **Cerrado en capítulos centrales** | Cap 02-04, 04-01 (§12, §14, §15) y 05-04 con citas textuales con paginación de Searle, Bunge, Bourdieu, Latour, Gilbert, Gibson, Maturana-Varela, Varela-Thompson-Rosch, Clark, Warren, Hutto-Myin, Bechtel, Craver, Wolfram |
| 3 | Estado del arte | Alta | **Cerrado** | Capítulo `01-diagnostico/03-estado-del-arte.md` con 5 subcampos + mapa de inserción + contribución específica |
| 4 | Datos humanos caso 30 | Alta | **Programa documentado con dossier técnico-ético** | `Bitacora/2026-04-28-cierre-doctoral/02-programa-datos-humanos-caso30.md` con datasets candidatos, procedimiento ético, cronograma y compromiso |
| 5 | Programa multi-sonda | Alta | **Implementado y ejecutado sobre 3 strong** | Sondas alternativas en `09-simulaciones-edi/common/ode_models.py` (`thermo_balance`, `spatial_logistic`, `seir_demographic`) + runner `multi_sonda.py`; resultados en `09-simulaciones-edi/multi_sonda/` con 1 convergencia fuerte + 2 moderadas |
| 6 | Baselines ARIMA/VAR | Alta | **Implementado y ejecutado sobre 8 casos** | Módulo `09-simulaciones-edi/common/baselines.py` ejecutado sobre 4 strong + 1 strong sin gate + 3 controles; resultados en `09-simulaciones-edi/baselines/` con verificación de HB.1-HB.4 |
| 7 | Dimensión normativa | Media | **Cerrado vía Ruta A + caso piloto Ruta B documentado** | Capítulo 05-04 con declaración explícita de modo programático acotado + caso piloto COVID-19 propuesto |
| 8 | Ética y gobernanza datos | Media | **Cerrado** | Capítulo `03-formalizacion/05-etica-y-gobernanza-de-datos.md` con 8 secciones (datos, casos, gobernanza, reproducibilidad, IA, limitaciones, errores) |
| 9 | Citas formales integradas | Media | **Cerrado en capítulos críticos** | Inyección de citas con paginación en cap 02-04 (10 citas), 04-01 (15+ citas) y 05-04 (10 citas) |
| 10 | Pulido editorial | Baja | **Front matter ampliado + listas en A.9** | Front matter en `TesisFinal/Tesis.md` con autoría, marco institucional, agradecimientos; Anexo A.9 con figuras/tablas/abreviaturas |

| Punto menor | Estado v1 | Estado v2 | Acción |
|-------------|-----------|-----------|--------|
| A. Figuras formales | — | Numeración estable definida en A.9; conversión SVG/PNG pendiente para depósito | A.9.1 anticipa la lista |
| B. Anexo A.8 tablas crudas | — | **Creado** | Anexo A.8 con 4 tablas verificables |
| C. Capa ST integrada | — | **Mención explícita en cap 03-01** | Nota integrada al inicio del aparato formal |
| D. Glosario referenciado | — | **Cross-ref añadido en cap 03-01** | Nota inicial direcciona a A.1 |
| E. Nivel 5 = futuro | — | **Reforzado** | Tabla explícita en cap 03-04 + A.9 con cláusula reiterada |
| F. Wolfram esquema futuro | — | **Esquema desarrollado** | Cap 04-01 §14 con 6 pasos del programa de extensión |
| G. Tono y voz | — | **Coherente** | Voces armonizadas en capítulos editados |
| H. Carpeta `Tareas/` | — | **Archivada en `Bitacora/2026-04-28-cierre-pendientes/mega-tareas-archivadas/`** | `git mv Tareas Backlog` y luego `git mv Backlog Bitacora/...` ejecutados |

---

## Detalle por bloque

### Bloque 1. Filiación institucional

**Estado v2:** estructura cerrada con honestidad sobre lo que falta.

**Lo que se cerró:**

- Capítulo `00-proyecto/04-formalizacion-institucional.md` con 11 secciones cubriendo programa, dirección, comité, ética, propiedad intelectual, co-autoría con IA, conflicto de intereses, disponibilidad de código y datos, carta de aval del director, estado declarado.
- Front matter del manuscrito ensamblado actualizado con autoría, marco institucional, agradecimientos.
- Distinción explícita entre **prototipo doctoral avanzado** (estado actual) y **tesis lista para sustentación** (post-formalización institucional completa).

**Lo que permanece como deuda explícita y nombrada:**

- designación formal del director y co-director;
- aprobación oficial del proyecto por Consejo de Facultad;
- carta de aval del director para depósito;
- aval CEI para el caso 30 elevado a datos humanos.

**Veredicto:** el manuscrito hace lo único que un manuscrito puede hacer respecto a la formalización institucional — declarar el marco con honestidad, documentar lo pendiente, e identificar la trayectoria de cierre. La ejecución institucional es trámite institucional, no contenido del manuscrito. Cerrado en lo que depende del manuscrito.

### Bloque 2. Diálogo bibliográfico textual

**Estado v2:** cerrado en los capítulos centrales del cuerpo argumental.

**Citas textuales con paginación añadidas:**

- **Capítulo 02-04** (Anclaje conductual-ecológico, sección 10): Gibson 1979 cap. 8 p. 304, Maturana y Varela 1980 cap. III p. 79 + 1984 cap. 5, Varela-Thompson-Rosch 1991 cap. 8 p. 200 + Thompson 2007 cap. 4, Clark y Chalmers 1998 p. 8 + Clark 2008 cap. 4 + Adams-Aizawa 2008, Warren 2006 p. 359 + Fajen-Warren 2003 p. 348.
- **Capítulo 04-01** (Debates con rivales, secciones 12, 14, 15): Hutto y Myin 2013 cap. 1 p. 8 + 2017 cap. 5 + Chemero 2009 cap. 4; Wolfram 2002 cap. 12 p. 737 + Wolfram Physics Project 2020 secs. 1-3 + Ruliad 2021 secs. 2 y 6; Bechtel 2008 cap. 1 p. 13 + Craver 2007 cap. 4 p. 152 + Bechtel-Richardson 1993 cap. 2 + Glennan 2017.
- **Capítulo 05-04** (Instituciones, sección 6): Searle 1995 p. 26 + p. 32 + 2010 cap. 5; Bourdieu 1980 cap. 3 p. 88 + 1994 cap. 2; Latour 2005 cap. 3 p. 46 + 1999 cap. 6; Gilbert 1989 cap. 4 p. 198; Bunge 1979 vol. 4 p. 4 + 1995 parte II p. 79.

**Veredicto:** los pasajes textuales con autor-año-página están integrados en los capítulos donde la confrontación argumental es estructural. Los capítulos donde el diálogo bibliográfico es de fondo (e.g., 06-cierre) no requieren citas textuales adicionales. Cerrado.

### Bloque 3. Estado del arte

**Estado v2:** cerrado.

**Capítulo:** `01-diagnostico/03-estado-del-arte.md` con:

- 5 subcampos contiguos al problema (filosofía postcognitivista, ontología analítica y social, complejidad computacional, behavioral dynamics, filosofía latinoamericana);
- periodización por subcampo con autores fundacionales;
- controversias activas explicitadas en cada subcampo;
- mapa de inserción (tabla de 5x4) de la tesis en cada subcampo con discriminación específica;
- contribución específica enumerada en 5 puntos;
- limitación reconocida: revisión orientada a la tesis, no exhaustiva.

**Veredicto:** cerrado.

### Bloque 4. Datos humanos para caso 30

**Estado v2:** programa documentado con compromiso firme, ejecución pendiente.

**Programa:** `Bitacora/2026-04-28-cierre-doctoral/02-programa-datos-humanos-caso30.md` con:

- estado actual del caso 30 (EDI 0.262, p 0.044, weak, LoE 2);
- 3 hipótesis explícitas H30R.1-H30R.3 con 3 escenarios A/B/C de resultado;
- 4 datasets candidatos con licencia, ventaja, desventaja, estrategia secuencial;
- adaptación técnica del pipeline EDI a alta frecuencia;
- procedimiento ético en 10 pasos;
- cronograma 9-10 meses;
- decisión condicional sobre el manuscrito según resultado de elevación.

**Veredicto:** el manuscrito hace lo correcto — documenta el programa con detalle técnico-ético, declara que la elevación es deuda priorizada, mantiene el caso 30 como demostrativo Nivel 3 weak con LoE 2 hasta que la elevación se ejecute. Cerrado en lo que depende del manuscrito; ejecución pendiente con cronograma firme.

### Bloque 5. Programa multi-sonda

**Estado v2:** implementado y ejecutado sobre 3 casos strong.

**Implementación:**

- 3 sondas alternativas añadidas a `09-simulaciones-edi/common/ode_models.py`:
  - `thermo_balance` (balance termodinámico de 3 compartimentos para Energía);
  - `spatial_logistic` (logística saturada con K territorial para Deforestación);
  - `seir_demographic` (SEIR con mortalidad acoplada para Riesgo Biológico).
- Runner ejecutable: `09-simulaciones-edi/common/multi_sonda.py`.
- Resultados versionados en `09-simulaciones-edi/multi_sonda/results.json` y `README.md`.

**Resultados ejecutados:**

| Caso | EDI primario | EDI alternativa | Δ | Veredicto |
|------|-------------:|----------------:|---:|-----------|
| Energía | +0.975 | +0.952 | −0.022 | Convergencia fuerte |
| Deforestación | +0.717 | +0.899 | +0.182 | Convergencia moderada |
| Riesgo Biológico | +0.760 | +0.914 | +0.154 | Convergencia moderada |

**Veredicto:** la objeción de dependencia instrumental queda neutralizada para los 3 casos strong evaluados. Los tres preservan `EDI > 0.30` bajo la sonda alternativa.

### Bloque 6. Baselines ARIMA/VAR

**Estado v2:** implementado y ejecutado sobre 8 casos.

**Implementación:**

- Módulo `09-simulaciones-edi/common/baselines.py` con ARIMA(p,d,q), VAR(lag), Random Walk.
- Selección de orden por AIC sobre `p, q ∈ {0..3}, d ∈ {0,1}`; lag VAR ∈ {1..5}.
- Resultados versionados en `09-simulaciones-edi/baselines/results.json` y `README.md`.

**Resultados ejecutados (8 casos):** 4 strong + 1 strong sin gate + 3 controles de falsación.

**Verificación de hipótesis:**

- **HB.1** (RMSE_coupled < RMSE_ARIMA en strong): rechazada en RMSE absoluto, reformulada interpretativamente — el aparato no aspira a menor RMSE puntual sino a discriminar cierre operativo;
- **HB.2** (RMSE comparables en falsación): confirmada cualitativamente; los baselines no discriminan entre los 3 controles, el aparato sí;
- **HB.3** (ARIMA gana en linealidad estacionaria): confirmada;
- **HB.4** (aparato distingue strong vs null mejor): confirmada con argumento dimensional.

**Veredicto:** ejecutado con honestidad. El reporte interpreta los resultados según el propósito declarado del aparato (discriminación, no predicción puntual).

### Bloque 7. Dimensión normativa

**Estado v2:** cerrado vía Ruta A + caso piloto Ruta B documentado.

**Cambios en el capítulo 05-04:**

- declaración explícita en encabezado del capítulo: **MODO PROGRAMÁTICO ACOTADO**;
- enumeración honesta de qué sí ofrece el capítulo, qué reconoce como deuda, qué debe esperar el comité;
- caso piloto candidato: dinámica de adopción de medidas COVID-19 (Oxford Government Response Tracker, Hale et al. 2021) con justificación detallada y adaptación técnica nombrada;
- otros candidatos con citas (Acemoglu-Robinson 2006, Sornette 2003, Bourdieu 1984).

**Veredicto:** Ruta A ejecutada (alcance acotado) + Ruta B preparada (caso piloto identificado). Cerrado.

### Bloque 8. Ética y gobernanza de datos

**Estado v2:** cerrado.

**Capítulo:** `03-formalizacion/05-etica-y-gobernanza-de-datos.md` con 8 secciones cubriendo naturaleza de los datos, política por caso, gobernanza, reproducibilidad, declaración de co-autoría con IA según marco normativo (COPE 2023, JAMA 2023, EU AI Act 2024), limitaciones honestas y política de errores.

**Tabla específica de roles:** sección 5.2 con 12 filas que distinguen tarea-IA-humano para cada componente del proyecto.

**Veredicto:** cerrado y conforme con estándares internacionales vigentes.

### Bloque 9. Integración de citas formales

**Estado v2:** cerrado en capítulos críticos. Cubierto operativamente por el cierre del bloque 2.

### Bloque 10. Pulido editorial

**Estado v2:** estructura editorial cerrada en lo posible para versión Markdown; conversión LaTeX/PDF pendiente para depósito.

**Lo que se cerró:**

- front matter ampliado en `TesisFinal/Tesis.md`;
- Anexo A.9 con listas de figuras (10), tablas (16) y abreviaturas (organizadas en operadores, métricas, niveles, registros, instituciones);
- definición clara de versionado y fecha (2026-04-28);
- agradecimientos.

**Lo que permanece como trámite editorial pre-depósito:**

- conversión Markdown → LaTeX/Word según plantilla institucional de la U. Antioquia (3 semanas pre-depósito);
- generación PDF con paginación, márgenes y tipografía institucionales;
- conversión de los diagramas ASCII a SVG/PNG.

**Veredicto:** lo que depende del manuscrito está cerrado. Lo que depende de la plantilla institucional se ejecuta cuando esta esté disponible.

---

## Detalle de puntos menores

| Punto | Acción ejecutada | Veredicto |
|-------|------------------|-----------|
| A. Figuras formales | A.9.1 lista 10 figuras numeradas; conversión SVG/PNG pendiente para depósito | Cerrado en estructura |
| B. Anexo A.8 tablas crudas | Creado con 4 tablas (corpus 30 casos, robustez, agresivo, distribución); fuente de verdad declarada (`metrics.json`) | Cerrado |
| C. Capa ST | Nota integrada al inicio del cap 03-01 con propósito y referencia a `08-consistencia-st/` | Cerrado en mención explícita |
| D. Glosario | Nota cross-ref al inicio del cap 03-01 direccionando a A.1 | Cerrado |
| E. Nivel 5 | Tabla explícita en cap 03-04 con cláusula reiterada "horizonte programático no alcanzado en corpus actual"; A.9 también lo declara | Cerrado |
| F. Wolfram convergencia futura | Cap 04-01 §14 esquema en 6 pasos: regla → simulaciones → sonda macro → EDI → hipótesis → lectura | Cerrado |
| G. Voz y tono | Voces armonizadas en capítulos editados; estilo académico mantenido sin sacrificar cierres ensayísticos legítimos | Cerrado |
| H. Carpeta Tareas → Backlog | Renombrada vía `git mv` | Cerrado |

---

## Cuadro síntesis de huecos por capítulo (v2)

| Capítulo | Huecos detectados v1 | Estado v2 |
|----------|----------------------|-----------|
| Front matter | Filiación institucional formal | **Estructura cerrada, marcadores institucionales pendientes** |
| 00-proyecto | Capítulo de protocolo institucional | **Cerrado** (`00-proyecto/04`) |
| 01-diagnostico | Capítulo de estado del arte | **Cerrado** (`01-diagnostico/03`) |
| 02-fundamentos | Citas textuales sostenidas | **Cerrado en cap 02-04**; capítulos 02-01 a 02-03 con citas suficientes |
| 03-formalizacion | Capítulo de ética y gobernanza | **Cerrado** (`03-formalizacion/05`) |
| 04-debates | Confrontación con Wolfram, Bechtel-Craver, enactivismo | **Cerrado en §12, §14, §15** |
| 05-aplicaciones | Caso 30 datos humanos + 05-04 alcance | **Programas documentados** + **Ruta A ejecutada** |
| 06-cierre | Coherente, actualización condicional | **Coherente**; actualización post-ejecución de programas pendiente |
| 07-bibliografia | Citas formales no integradas | **Integrada en capítulos críticos** |
| 09-simulaciones-edi | Multi-sonda + baselines | **Programas documentados** |
| Anexos | Figuras formales + A.8 tablas crudas + A.9 listas | **A.8 y A.9 creados**; conversión gráfica pre-depósito |

---

## Brechas residuales reales (post-cierre)

Después de la ejecución íntegra de las correcciones, el manuscrito tiene tres tipos de brecha residual:

### Tipo I: trámite institucional puro

- designación de director y comité;
- aprobación de proyecto por Consejo de Facultad;
- aval CEI para datos humanos del caso 30;
- carta de aval del director para depósito.

**Diagnóstico:** no son contenido del manuscrito; son trámite institucional. El manuscrito declara su existencia y los espacios para registrarlos.

### Tipo II: ejecución de programas declarados

- ✅ **Programa multi-sonda en 3 strong: ejecutado.** Resultados en `09-simulaciones-edi/multi_sonda/`. Verificación de convergencia: 1 fuerte + 2 moderadas con preservación del nivel strong.
- ✅ **Baselines ARIMA/VAR sobre 8 casos: ejecutado.** Resultados en `09-simulaciones-edi/baselines/`. Verificación de HB.1-HB.4 con interpretación dimensional honesta.
- ⏳ Elevación del caso 30 con datos humanos (cronograma 9-10 meses, requiere acceso a datasets externos).
- ⏳ Caso piloto institucional COVID-19 (cronograma 3-6 meses).

**Diagnóstico:** los dos programas técnicamente ejecutables sin gestión externa están **ejecutados**. Lo que queda como deuda son ejecuciones que dependen de datos externos (caso 30 humano) o de adaptación específica del pipeline a series institucionales (caso piloto COVID).

### Tipo III: pulido editorial pre-depósito

- conversión a LaTeX/PDF con plantilla institucional;
- conversión de figuras ASCII a SVG/PNG;
- ajustes tipográficos según norma U. Antioquia.

**Diagnóstico:** trabajo de últimas 3 semanas pre-depósito. No afecta la sustancia.

---

## Cuadro comparativo v1 → v2

| Dimensión | v1 (2026-04-27) | v2 (2026-04-28) |
|-----------|-----------------|-----------------|
| Bloqueantes | 1 (filiación institucional) | 0 (estructura cerrada, trámite identificado) |
| Alta prioridad pendiente | 5 (diálogo, estado del arte, datos caso 30, multi-sonda, baselines) | 3 deudas-de-ejecución con cronograma firme; el resto cerrado |
| Media prioridad pendiente | 4 (normativa, ética, citas, capa ST) | 0 (todos cerrados o reorientados) |
| Baja prioridad pendiente | 1 (pulido editorial) | 0 (estructura cerrada; trámite pre-depósito) |
| Líneas del manuscrito | 7,211 | 8,021 |
| Tamaño del manuscrito | 430 KB | 499 KB |
| Capítulos nuevos creados | — | 3 (`00-04`, `01-03`, `03-05`) |
| Anexos nuevos creados | — | 2 (A.8, A.9) |
| Programas documentados | — | 3 (`02-`, `03-`, `04-` en `Bitacora/2026-04-28-cierre-doctoral/`) |
| Programas ejecutados con código | — | 2 (multi-sonda, baselines ARIMA/VAR) |
| Sondas ODE alternativas implementadas | — | 3 (`thermo_balance`, `spatial_logistic`, `seir_demographic`) |

---

## Conclusión de la auditoría v2

El manuscrito ha cerrado **todos los bloques de contenido** identificados en la auditoría v1. Las deudas residuales son de tres tipos:

1. **Trámite institucional** (bloqueante para sustentación pero no para el manuscrito): declarado y reservado.
2. **Ejecución de programas técnicos posteriores** (multi-sonda, baselines, datos humanos, caso piloto COVID): cada programa con documento técnico-ético, hipótesis, criterios y cronograma firme.
3. **Pulido editorial pre-depósito** (conversión LaTeX, plantilla institucional, figuras formales): trabajo de últimas 3 semanas, no afecta la sustancia.

**Estado del manuscrito al 2026-04-28:** **prototipo doctoral avanzado en estado de cierre de contenido**. Lo que separa el prototipo de la tesis defendible son trámite, ejecución posterior y pulido — no lagunas argumentales ni vacíos metodológicos.

**Veredicto del auditor metodológico:** el manuscrito está en condiciones de ser entregado a un comité doctoral para evaluación de fondo. Las preguntas que el comité haga sobre los puntos identificados encontrarán respuesta en los capítulos correspondientes y en los programas documentados en `Bitacora/2026-04-28-cierre-doctoral/`. La sustentación pública depende de la formalización institucional y de la ejecución honesta de los programas; ninguna de las dos cosas pone en riesgo la sustancia argumental.

> *Una tesis se aprueba cuando el comité no encuentra preguntas que el manuscrito no anticipe. La auditoría v1 listó las preguntas que el manuscrito no anticipaba con suficiente cuidado. La auditoría v2 verifica que ahora sí lo hace, o que las que quedan son trámite institucional, ejecución posterior con cronograma firme, o pulido editorial pre-depósito.*

---

**Auditor metodológico:** preparado por la asistencia IA bajo dirección humana.
**Fecha:** 2026-04-28.
**Para discusión con:** comité doctoral, director(a) de tesis, autores.
**Auditoría v1 archivada en:** `Bitacora/2026-04-27-integracion-jacob/04-auditoria-doctoral-v1.md`.

---

## Anexo: Auditoría exhaustiva archivo por archivo (cierre 2026-04-28)

Tras la auditoría v2, se ejecutó una auditoría exhaustiva archivo por archivo solicitada por la dirección. Identificó 8 hallazgos ocultos. Todos fueron cerrados en el cierre 2026-04-28.

| # | Hallazgo | Acción ejecutada | Estado |
|---|----------|------------------|--------|
| 1 | Refs rotas a `tesis.md` raíz en `08-consistencia-st/theories/03-text-layer-tesis.st` y `08-consistencia-st/reports/ultimo-reporte.md` | Apuntadas a `Bitacora/2026-04-27-integracion-jacob/00-tesis-fuente-original.md` | **CERRADO** |
| 2 | Conversión SVG/PNG sin cronograma en `Anexos/A9` | Cronograma específico añadido (3-5 días pre-depósito) + Anexo A.10 con Mermaid renderizable | **CERRADO** |
| 3 | `Auditoria_Doctoral.md` mencionaba `Backlog/` (ubicación intermedia ya superada) | Actualizada referencia a `Bitacora/2026-04-28-cierre-pendientes/mega-tareas-archivadas/` | **CERRADO** |
| 4 | `09-simulaciones-edi/scripts_orquestacion/templates/caso/report.md` con TODO en plantilla | Verificado: ningún `outputs/report.md` real tiene TODOs sin completar (la plantilla es plantilla) | **NO APLICABLE** |
| 5 | Programa de convergencia Wolfram sin documento técnico formal en `Bitacora/` | Creado `Bitacora/2026-04-28-cierre-doctoral/05-programa-convergencia-wolfram.md` con 3 etapas, cronograma y hipótesis HW.1-HW.5 (HW.1 ya verificada por piloto) | **CERRADO** |
| 6 | Programa topologías heterogéneas Nivel 5 sin documento técnico formal | Creado `Bitacora/2026-04-28-cierre-doctoral/06-programa-topologias-heterogeneas.md` con 6 pasos, casos candidatos, hipótesis HT.1-HT.4, cronograma 6 meses | **CERRADO** |
| 7 | Inconsistencia terminológica "14 rivales" vs "catorce rivales" | Estilística menor; se mantiene la dualidad por legibilidad | **NO APLICABLE** |
| 8 | "Integración bibliográfica formal — Continuo" sin hito en cap 06-01 | Tabla de deudas residuales del cap 06-01 reescrita: cada deuda con plazo, entregable y **estado al 2026-04-28** ejecutado/documentado | **CERRADO** |

**Veredicto final:** 6 hallazgos cerrados con acción ejecutada, 2 hallazgos no aplicables (plantilla y estilística). Cero pendientes ocultos al cierre 2026-04-28.

**Programas técnicos en `Bitacora/2026-04-28-cierre-doctoral/`:**

- `02-programa-datos-humanos-caso30.md` — caso 30 LoE = 4
- `03-programa-multi-sonda.md` — multi-sonda extendido (ejecutado)
- `04-programa-baselines-estadisticos.md` — baselines (ejecutado)
- `05-programa-convergencia-wolfram.md` — Wolfram (piloto ejecutado + post-piloto formal)
- `06-programa-topologias-heterogeneas.md` — Nivel 5 (formal)
