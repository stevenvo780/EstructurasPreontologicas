# Anexo A.9. Listas de figuras, tablas y abreviaturas

## Función

Listas de soporte editorial requeridas por el formato de tesis doctoral institucional de la Universidad de Antioquia. Tres listas independientes: figuras, tablas, abreviaturas. Cada elemento referencia su capítulo de origen.

---

## A.9.1. Lista de figuras

> Nota: en la versión actual del manuscrito, los diagramas y figuras están representados en ASCII art en el cuerpo de los capítulos. La conversión a SVG/PNG con Mermaid o herramientas equivalentes es trabajo de pulido editorial pendiente para depósito (ver bloque 10 de la auditoría doctoral). Esta lista anticipa la numeración estable.

| Figura | Título | Capítulo |
|--------|--------|----------|
| Fig. 2.1 | Cuatro modos de realidad operativa | 02-01 |
| Fig. 2.2 | Acoplamiento dinámico organismo-entorno-tarea-historia | 02-04 |
| Fig. 3.1 | Mapa de operadores formales (μ, G, H, κ, ε) | 03-01 |
| Fig. 3.2 | Diagrama del dossier de anclaje (14 componentes) | 03-02 |
| Fig. 3.3 | Pipeline de validación EDI con permutación + bootstrap + C1-C5 | 03-04 |
| Fig. 4.1 | Tabla discriminante con 14 rivales (resumen) | 04-01 |
| Fig. 5.1 | Asimetría L1↔B↔L3↔S como protocolo | 02-04 / 05-05 |
| Fig. 5.2 | Trayectoria de heading bajo behavioral_attractor (caso 30) | 05-05 / 09-30 |
| Fig. 6.1 | Paisaje de emergencia del corpus EDI (distribución por nivel) | 06-01 |
| Fig. 9.1 | Arquitectura del motor ABM+ODE acoplado | 09-00 |

---

## A.9.2. Lista de tablas

| Tabla | Título | Capítulo |
|-------|--------|----------|
| Tabla 0.1 | Hitos institucionales declarados | 00-04 |
| Tabla 1.1 | Falencias diagnósticas del prototipo previo | 01-01 |
| Tabla 1.2 | Mapa de inserción de la tesis en cinco subcampos | 01-03 |
| Tabla 3.1 | Cinco operadores formales del aparato mínimo | 03-01 |
| Tabla 3.2 | Componentes del dossier de anclaje (14) | 03-02 |
| Tabla 3.3 | Protocolo C1-C5 + 8 condiciones para `overall_pass = True` | 03-04 |
| Tabla 4.1 | 14 rivales y discriminación específica | 04-01 |
| Tabla 5.1 | Casos del corpus por dominio de aplicación | 05-00 |
| Tabla 5.2 | Comparativa cualitativa-cuantitativa para behavioral dynamics | 05-05 |
| Tabla 6.1 | Cuadro síntesis del paisaje de emergencia | 06-01 |
| Tabla A.4.1 | Tabla comparativa con 14 rivales (Anexo) | A.4 |
| Tabla A.5.1 | Mapa de aplicaciones del marco | A.5 |
| Tabla A.8.1 | Resultados del corpus EDI (30 casos) | A.8 |
| Tabla A.8.2 | Métricas de robustez por caso | A.8 |
| Tabla A.8.3 | Verificación bajo perfil agresivo | A.8 |
| Tabla A.8.4 | Distribución del paisaje de emergencia | A.8 |

---

## A.9.3. Lista de abreviaturas y símbolos

### Operadores formales

| Símbolo | Significado | Capítulo |
|---------|-------------|----------|
| μ | Operador de medición; recorta R en X observable | 03-01 |
| G | Grafo basal de dependencias entre variables | 03-01 |
| H | Hipergrafo de relaciones n-arias | 03-01 |
| κ | Operador de compresión multiescala | 03-01 / 03-04 |
| ε | Operador de errores de traducción | 03-01 |
| φ, ψ | Heading actual y heading de meta (caso 30) | 05-05 / 09-30 |
| τ | Razón tamaño-óptico / tasa-de-cambio (Lee 1976) | 02-04 |
| β | Error de heading φ − ψ_g | 02-04 |

### Métricas y protocolos

| Sigla | Significado | Capítulo |
|-------|-------------|----------|
| EDI | Effective Dependence Index | 03-04 |
| RMSE | Root Mean Squared Error | 03-04 |
| C1-C5 | Convergencia, Robustez, Determinismo, Consistencia, Uncertainty | 03-04 |
| ABM | Agent-Based Model | 09-00 |
| ODE | Ordinary Differential Equation | 09-00 |
| LoE | Level of Evidence (1-5) | 03-02 |
| CI | Confidence Interval | 03-04 |
| CR | Cohesion Ratio (Symploké) | 03-04 |

### Niveles del corpus

| Nivel | Categoría | Definición operativa |
|------:|-----------|----------------------|
| 0 | Null | EDI ≤ 0 o sin estructura macro |
| 1 | Trend | 0 < EDI sin significancia (p ≥ 0.05) |
| 2 | Suggestive | 0.01 ≤ EDI < 0.10, p < 0.05 |
| 3 | Weak | 0.10 ≤ EDI < 0.30, p < 0.05 |
| 4 | Strong | EDI ≥ 0.30, p < 0.01, `overall_pass = True` |
| 5 | Crítico (programa futuro) | Convergencia bajo múltiples sondas + datos LoE = 5 + frontera espacial nítida |

**Nota explícita sobre el Nivel 5:** el manuscrito demuestra hasta Nivel 4. El Nivel 5 está definido como **horizonte programático** del marco, no como nivel alcanzado en el corpus actual. Sus condiciones (multi-sonda convergente, LoE = 5, topología heterogénea con frontera nítida) son objetivos del programa de elevación documentado en `Procesos/2026-04-28-cierre-doctoral/`.

### Niveles del registro categorial

| Sigla | Registro | Capítulo |
|-------|----------|----------|
| L1 | Psicológico-ordinario (preguntas comunicables) | 02-04 |
| B | Conductual-biológico (anclaje empírico) | 02-04 |
| L3 | Estructural-relacional (formalización) | 02-04 |
| S | Semántica revisada (categorías que sobreviven) | 02-04 |

### Instituciones y datasets

| Sigla | Significado |
|-------|-------------|
| CEI | Comité de Ética en Investigación (Universidad de Antioquia) |
| SIIU | Sistema de Información para la Investigación Universitaria |
| OPSD | Open Power System Data |
| OWID | Our World in Data |
| TLE | Two-Line Element (CelesTrak) |

---

## Trazabilidad

Las listas de este anexo se actualizarán automáticamente desde el manuscrito ensamblado (`TesisFinal/Tesis.md`) cuando se haga la conversión final a LaTeX/PDF mediante Pandoc + script de extracción. Hasta entonces, este anexo se mantiene manualmente coherente con los capítulos de origen.
