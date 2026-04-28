# Programa de convergencia EDI ↔ Wolfram Physics Project

## Función

Documento técnico-formal del programa de convergencia entre el aparato EDI y el Wolfram Physics Project anunciado en `04-debates/01-debates-con-posiciones-rivales.md` §14 y `06-cierre/01-conclusion-demostrativa.md`. Cierra el hallazgo 5 de la auditoría exhaustiva del 2026-04-28.

## Estado actual: piloto ya ejecutado

**Piloto en producción:** `09-simulaciones-edi/wolfram_pilot/` con 200 corridas sobre **CA elemental Rule 110** (Wolfram 2002 cap. 3, irreducibilidad computacional).

**Resultados ejecutados al 2026-04-28:**

| Sonda macro | EDI medio | EDI std | n corridas válidas | Veredicto |
|-------------|----------:|--------:|-------------------:|-----------|
| Densidad de celdas activas | 0.5511 | 0.1022 | 200 | Cierre operativo macro detectable |
| Curvatura discreta de frontera | 0.5455 | 0.0970 | 200 | Cierre operativo macro detectable |

**Lectura:** la dinámica computacional de Rule 110, aunque computacionalmente irreducible al nivel micro (Wolfram 2002, p. 737), **admite descripción macro EDI-significativa** bajo dos sondas independientes con motivación distinta. Esto valida operativamente el esquema de los 6 pasos propuestos en cap 04-01 §14.

## Programa de extensión (post-piloto)

### Etapa A: Replicación con reglas adicionales (3 meses)

**Objetivo:** confirmar que el cierre operativo macro detectado en Rule 110 se extiende a otras reglas representativas con propiedades emergentes documentadas.

**Reglas candidatas:**

| Regla | Naturaleza | Justificación |
|-------|-----------|---------------|
| Rule 30 | Caos clase 3 (Wolfram 2002 p. 27) | Probar el opuesto de Rule 110 (orden vs. caos); espera EDI bajo |
| Rule 90 | Fractal Sierpinski determinista | Estructura determinista pero no Turing-completa |
| Rule 184 | Tráfico de partículas | Dinámica conservada; sonda macro de densidad debería tener cierre alto |
| Rule 22 | Caos clase 3 simétrico | Comparar con Rule 30 |

**Procedimiento por regla:**
1. ejecutar 200 corridas con condiciones iniciales perturbadas;
2. aplicar las dos sondas macro (densidad, curvatura) con permutación 999 + bootstrap 500;
3. clasificar resultado: cierre fuerte, débil, irreducibilidad confirmada.

**Hipótesis de la etapa:** las reglas con clase Wolfram 2 (orden) tienen EDI medio ≥ 0.30; las reglas clase 3 (caos) tienen EDI < 0.10. Esto operacionalizaría la clasificación de Wolfram en términos del marco EDI.

### Etapa B: Extensión a hipergrafos 2D (6 meses)

**Objetivo:** elevar de CA 1D a hypergraph rewriting genuino siguiendo la formulación del Wolfram Physics Project.

**Fuente de reglas:** Wolfram Physics Project Repository (https://www.wolframphysics.org/), reglas con curvatura emergente documentada.

**Sondas macro propuestas:**
- densidad media de aristas;
- curvatura escalar discreta de Forman;
- distribución de grados (potencial Pareto si scale-free);
- diámetro espacial efectivo del grafo.

**Esfuerzo computacional:** factor 50–200 sobre Rule 110 (hipergrafos crecen exponencialmente). Hardware actual (2 GPUs) lo soporta.

### Etapa C: Programa filosófico de convergencia (3 meses)

**Objetivo:** publicación conjunta o intercambio académico con Wolfram Institute. Antes: producir reporte técnico que el Institute pueda evaluar. El reporte debe:

- presentar el aparato EDI como herramienta complementaria, no rival;
- demostrar que cierre macro y irreducibilidad micro son compatibles;
- ofrecer las reglas testadas como dataset compartible.

## Cronograma agregado

| Mes | Etapa | Hito | Entregable |
|-----|-------|------|-----------|
| 1–3 | A | Replicación 4 reglas adicionales | Tabla EDI por regla, clasificación operacional Wolfram |
| 4–9 | B | Extensión a hipergrafos 2D | EDI sobre 2-3 reglas de Wolfram Physics Project |
| 10–12 | C | Reporte técnico para Wolfram Institute | PDF académico con dataset compartible |

**Total programa post-defensa:** 12 meses.

## Hipótesis a verificar

| H | Enunciado | Verificación |
|---|-----------|--------------|
| HW.1 | Rule 110 tiene cierre operativo macro detectable | **EJECUTADA** y **CONFIRMADA** (EDI 0.55, n=200) |
| HW.2 | Reglas clase 2 Wolfram tienen EDI ≥ 0.30 | Etapa A |
| HW.3 | Reglas clase 3 Wolfram tienen EDI < 0.10 | Etapa A |
| HW.4 | Hipergrafos con curvatura emergente tienen EDI ≥ 0.30 | Etapa B |
| HW.5 | Wolfram + EDI son complementarios, no rivales | Etapa C |

## Posición filosófica del programa

El piloto ejecutado ya **valida operativamente** la posición declarada en cap 04-01: *"Wolfram fundamenta; la tesis disciplina"*. La irreducibilidad computacional al nivel micro y el cierre operativo significativo al nivel macro **conviven** en Rule 110. Las etapas A-C amplían esta convivencia a un dataset más rico y producen contribución académica conjunta posible.

## Limitación declarada

- el programa post-piloto requiere acceso a las reglas hypergraph del Wolfram Physics Project (públicas) y tiempo de cómputo (estimable en GPU-días, no GPU-meses);
- la publicación conjunta con Wolfram Institute es deseable pero no condicionante; el resultado técnico se publicará independientemente si el intercambio académico no se produce.

## Lectura cruzada

- Piloto ejecutado: `09-simulaciones-edi/wolfram_pilot/`.
- Esquema en cap 04-01: `04-debates/01-debates-con-posiciones-rivales.md` §14.
- Posición teórica: `06-cierre/01-conclusion-demostrativa.md` (sección 6 deudas residuales).
- Auditoría exhaustiva: hallazgo 5.
