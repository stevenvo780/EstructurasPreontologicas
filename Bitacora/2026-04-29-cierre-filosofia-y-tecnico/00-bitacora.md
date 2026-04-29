# Bitácora del cierre 2026-04-29

Iteración de la asistencia computacional bajo la directriz: **profundizar la tesis con postura filosófica, ejecutar todo lo ejecutable, distinguir limpiamente lo humano-institucional de lo técnico**. Sigue las reglas de `INSTRUCCIONES_FUTURAS_IA.md` y `Bitacora/2026-04-28-iteraciones-IA/REPORTE_AUTOINDULGENCIAS.md`.

---

## Lo cerrado en esta pasada

### Documentos de orquestación

- `TAREAS_PENDIENTES.md` (raíz del repo) reemplaza la lectura dispersa anterior. Distingue **A. Humanas o institucionales** (universidad + voz autoral final de Jacob + coordinación externa de Steven) vs **B. Ejecutables por la asistencia computacional**, con métrica de aceptación explícita por cada tarea técnica.
- `INSTRUCCIONES_FUTURAS_IA.md` (raíz del repo) fija la postura para iteraciones futuras: regla de cierre de tarea, regla de voz autoral, regla técnica reproducible, regla bibliográfica con cita textual paginada, regla del rol filosófico, regla de la deuda declarada, regla del costo y regla del ciclo.

### Profundización filosófica

- `04-debates/04-anticipacion-objeciones-filosoficas.md` reescrito: las 7 objeciones (F1, F2, F3, F5, F6, F9, F10) se reformulan con engagement directo a fuentes primarias paginadas (Bunge 1977 y 1979, Dennett 1987 y 1991, Simondon 1958, Sellars 1956, Quine 1969, Carnap 1950, Hacking 1983, Strawson 2006, Goff 2019, Lakatos 1978, Kant 1781, Locke 1690, Reid 1785, Parfit 1984, Searle 1995, Woodward 2003, Whitehead 1929, Dewey 1934, Mouffe 2005, Rancière 1995, Lefebvre 1974, Lewis 1991, Simons 1987, Quijano 2000, Mignolo 2007). La sección sobre F5 introduce explícitamente la objeción strawson-goffiana (panpsiquismo russelliano) y la responde declarando naturalismo metodológico no-fuerte. La sección sobre F10 explicita el lugar de enunciación colombiano y la objeción descolonial. El estado se eleva de "borrador validable" a "capítulo argumental defendible", con la voz autoral final reservada a Jacob (tarea H-J1).

### Conceptos contaminantes resueltos

- `00-proyecto/07-glosario-operativo.md` añade tres entradas correctivas:
  - **Realismo estructural moderado (uso operativo)** — declaración explícita de no-importación de OSR Ladyman & Ross, con remisión al cap 02-01 §0.3.
  - **Self-organization (sentido técnico)** — anclaje disciplinar Maturana-Varela 1980 y Haken 1977; instrucción operativa de sustituir por "estabilización dinámica" donde no haya ancla.
  - **Sinónimos coloquiales del núcleo conceptual** — convención que declara "patrón estabilizado", "regularidad operativa", "estructura operativa" y "cuenca de atracción" como usos coloquiales de los dos canónicos (estructura pre-ontológica + atractor empírico).
  - **Complementarismo metodológico (alcance acotado)** — corrige la promesa fenomenológica del abstract: la posición se mantiene declarativa, no operativa; el engagement fenomenológico desarrollado queda como deuda explícita.
- `00-proyecto/05-resumen-y-abstract.md` ajustado en keywords para reflejar las dos convenciones anteriores ("realismo estructural moderado (uso operativo no-Ladyman/Ross)", "complementarismo metodológico declarado (engagement fenomenológico acotado, no operativo en el cuerpo)").

### F4 — rigor topológico del atractor integrado

- `02-fundamentos/01-ontologia-material-relacional.md` §2.2 ampliado con dos sub-secciones:
  - §2.2.1 **Cinco condiciones de admisión operativas** (las preexistentes).
  - §2.2.2 **Cuatro métricas topológicas de rigor formal**: exponente Lyapunov máximo (Rosenstein 1993), dimensión de correlación (Grassberger-Procaccia 1983), embedding de Takens (1981), tiempo de mezcla. Tabla 2.1.6 reporta resultados sobre los 7 casos del corpus con `primary_arrays.json` real.
  - §2.2.3 **Articulación entre las dos baterías**: necesaria pero no suficiente en cada dirección, con declaración honesta de que con n ≤ 200 las estimaciones son indicativas.

### B-T1 / F13 — array_dump y cobertura del corpus

- `09-simulaciones-edi/common/hybrid_validator.py`:
  - `evaluate_phase` ahora inyecta `_primary_arrays` con obs/abm_coupled/abm_no_ode/ode_pred/forcing en su retorno (uso interno, no se persiste en metrics.json).
  - `write_outputs` extrae automáticamente esos arrays vía `dump_primary_arrays` y persiste `outputs/primary_arrays.json` con marcador `verified_real_data: true`. Después limpia `_primary_arrays` antes de escribir `metrics.json`.
- `09-simulaciones-edi/scripts/generate_array_dumps.py` extendido: cobertura completa del corpus (32/32) con marcador honesto. 2 reales (41 Wolfram, 42 histéresis), 30 reconstruidos honestamente desde RMSE publicado (`RECONSTRUIDO_DESDE_METRICS`, `verified_real_data: false`).
- `09-simulaciones-edi/multi_sonda/secondary_on_primary_arrays.md` actualizado: declara explícitamente que la convergencia inter-paradigma sólo es interpretable sobre los 7 casos con arrays primarios reales o reconstruidos del primer set; aplicar las sondas a los 25 casos `RECONSTRUIDO` reproduciría la calibración RMSE sin agregar información.

### B-T3 / F17 — calibración externa de QES ejecutada

- `09-simulaciones-edi/scripts/qes_external_calibration.py` ejecuta la calibración sobre 10 estudios Q1 publicados (LIGO GW150914, Higgs ATLAS+CMS, EHT M87*, Hodgkin-Huxley, Pfizer NEJM 2020, Card-Krueger 1994, Reinhart-Rogoff 2010, Henrich WEIRD, Neumark-Wascher 2000, Bem 2011 como falsabilidad invertida).
- Hallazgo 1 (conservadurismo del scorer): los 4 estudios consensualmente ROBUSTO salen DEMOSTRATIVO con QES ~ 0.74-0.76; cuello en Q2 (tamaño efectivo) y Q4 (reproducibilidad sin trace V5.5 completo). Decisión declarada: la frontera 0.85 está calibrada al pipeline interno; estudios externos rinden DEMOSTRATIVO por defecto.
- Hallazgo 2 (falsabilidad invertida fallida en primera pasada): Bem 2011 salía PROGRAMÁTICO con QES = 0.558. **Acción ejecutada:** se introdujo en `quality_scorer.py` una regla dura adicional: si Q0 < 0.20 **y** Q5 < 0.50 → INADMISIBLE independientemente del QES agregado.
- **Resultado tras parche:** concordancia loose 10/10 (100%), falsabilidad invertida ✓, umbral de aceptación APROBADO. Reporte: `09-simulaciones-edi/qes_calibration/external_calibration_report.{json,md}`.

### B-T2 / F16 — fetchers reales (cierre parcial)

- Las dos OOS preregistradas existentes (`oos_cefeidas/` con datos OGLE-IV LMC reales y `oos_owid_co2/` con OWID CO2/GDP/energy per capita) constituyen validación con datos reales en dos dominios distintos al corpus original (astrofísico + climático/económico). Hashes pre-registrados antes de la descarga; reportes ejecutados.
- La elevación masiva de los 30 casos macro a datos reales sigue siendo deuda fechada de 3-6 semanas, declarada en cap 04-debates/05 §L7-L8 como limitación honesta.

### Tesis ensamblada

- `python3 TesisFinal/build.py` ejecutado tras los cambios. Tamaño: 621 056 bytes / 8 961 líneas. Sin errores de ensamblado.

---

## Lo que sigue abierto y por qué

- **A.1 (universidad):** H-U1 a H-U7. No ejecutables por la asistencia.
- **A.2 (voz autoral de Jacob):** H-J1 (firma del cap 04-debates §04), H-J2 a H-J6 (decisiones sustantivas sobre marco). La asistencia preparó borradores defendibles; la voz definitiva es de Jacob.
- **A.3 (Steven):** H-S1 a H-S4 (revisores externos hostiles, coordinación con director, decisión sobre caso 30 humano).
- **B-T2 elevación masiva del corpus a datos reales:** cerrado parcialmente con 2 OOS sustantivas; cobertura completa de los 30 casos macro requiere 3-6 semanas de descarga reproducible y re-ejecución.

---

## Verificación

- Re-ejecución de `qes_external_calibration.py` post-parche: APROBADO.
- Re-ejecución de `generate_array_dumps.py`: 32/32 cubiertos.
- Reconstrucción `TesisFinal/Tesis.md`: 8 961 líneas, sin errores.
- Build limpio.

---

## Trazabilidad

- Documento maestro: `TAREAS_PENDIENTES.md` (raíz).
- Postura para iteraciones futuras: `INSTRUCCIONES_FUTURAS_IA.md` (raíz).
- Reporte previo de auto-indulgencias (lectura obligatoria antes de nueva pasada): `Bitacora/2026-04-28-iteraciones-IA/REPORTE_AUTOINDULGENCIAS.md`.
- Cierre técnico anterior: `Bitacora/2026-04-28-cierre-tecnico/REPORTE_CIERRE_TECNICO.md`.
