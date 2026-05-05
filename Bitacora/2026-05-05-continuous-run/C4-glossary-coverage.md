# C4 — Auditoría de cobertura del glosario operativo

**Fecha:** 2026-05-05
**Tarea:** C4-glossary-coverage (continuous-run, kind=audit)
**Archivo objetivo:** `00-proyecto/07-glosario-operativo.md`
**Constraint:** este informe NO edita el glosario. Cualquier inserción requiere revisión de Jacob.

---

## 1. Resumen ejecutivo

Cuatro términos técnicos fueron auditados:

| Término | ¿En glosario? | Uso en cuerpo | Acción propuesta |
|---|---|---|---|
| Exponente de Lyapunov | **NO** | 02-fundamentos/01 §, 04-debates/02, 04-debates/04, 06-cierre/01, 06-cierre/03 | Añadir entrada (DRAFT-IA abajo) |
| Grassberger-Procaccia (D₂) | **NO** | 02-fundamentos/01 §, 04-debates/04, 06-cierre/01, 06-cierre/03 | Añadir entrada |
| Embedding de Takens | **NO** | 02-fundamentos/01 § | Añadir entrada |
| Slaving principle (Haken) | **NO explícitamente** (Haken 1977 sí está bajo "Self-organization") | 02-fundamentos/04 §, 04-debates/04 (referencia indirecta) | Añadir sub-entrada bajo "Self-organization" o entrada propia |

**Veredicto:** los cuatro términos circulan por el cuerpo del manuscrito como conceptos técnicos con consecuencias inferenciales (firma topológica del atractor, justificación de reconstrucción de espacio de fase, modelo positivo de la emergencia). Ninguno está definido en el glosario operativo. Esto es **deuda menor pero no trivial**: un evaluador externo que entre por el glosario no encontrará la operacionalización de "firma topológica" usada en cap 02-01 §, 04-04 §, 06-01 §.

---

## 2. Hallazgos por término

### 2.1 Exponente de Lyapunov (λ_max)

**No aparece en el glosario.**

**Apariciones en el cuerpo (con archivos absolutos):**

- `/datos/repos/EstructurasPreontologicas/02-fundamentos/01-ontologia-material-relacional.md:215` — definición técnica más completa del manuscrito: algoritmo de Rosenstein, Collins y De Luca (1993, *Physica D* 65: 117-134), tasa de divergencia local, criterio de signo (>0 caos / ≈0 marginal / <0 convergencia).
- `/datos/repos/EstructurasPreontologicas/04-debates/02-limitaciones-y-puntos-de-presion.md:85` — declarado como método externo al marco filosófico.
- `/datos/repos/EstructurasPreontologicas/04-debates/04-anticipacion-objeciones-filosoficas.md:88` y `:174` — invocado como firma topológica del atractor en respuesta a objeción goffiana.
- `/datos/repos/EstructurasPreontologicas/06-cierre/01-conclusion-demostrativa.md:142` — reportado como ejecutado sobre 7 casos con valores numéricos concretos (caso 41 wolfram λ_max=+0.017; caso 42 histéresis λ_max=−0.052).
- `/datos/repos/EstructurasPreontologicas/06-cierre/03-hoja-de-ruta-para-tesis-final.md:34` — listado como parte del análisis topológico ejecutado.

**Propuesta DRAFT-IA (no insertada):**

> ### Exponente de Lyapunov máximo (λ_max)
> Tasa media de divergencia exponencial de trayectorias inicialmente cercanas en el espacio de fase reconstruido. Calculado por el algoritmo de Rosenstein, Collins y De Luca (1993, *Physica D* 65: 117-134). Convención de signo: λ_max > 0 indica sensibilidad a condiciones iniciales (caos determinista compatible con atractor extraño); λ_max ≈ 0 indica régimen marginal o cuasi-periódico; λ_max < 0 indica convergencia a punto fijo o ciclo límite. Junto con D₂ (Grassberger-Procaccia) constituye la **firma topológica** del atractor reportada en cap 02-01 §, cap 06-01 §. Implementación: `09-simulaciones-edi/common/topology.py`. Capítulo 02-01 §[verificar §exacto].

**Cita primaria:** disponible textualmente en cap 02-01 §; PDF Rosenstein 1993 NO presente en `07-bibliografia/` (el manuscrito cita por referencia bibliográfica sin paginación verbatim — coherente con uso de fórmula técnica, no de argumento filosófico).

---

### 2.2 Dimensión de correlación de Grassberger-Procaccia (D₂)

**No aparece en el glosario.** (Aparece la frase "dimensión de correlación" como método citado al pasar en 04-debates/02 §85, sin definición.)

**Apariciones:**

- `/datos/repos/EstructurasPreontologicas/02-fundamentos/01-ontologia-material-relacional.md:216` — definición canónica: Grassberger y Procaccia (1983, *Physica D* 9: 189-208); cuantifica complejidad del atractor en espacio de fase reconstruido; valor no entero = atractor fractal/extraño; valor próximo a 0 = punto fijo.
- `/datos/repos/EstructurasPreontologicas/04-debates/04-anticipacion-objeciones-filosoficas.md:88` — firma topológica del atractor.
- `/datos/repos/EstructurasPreontologicas/06-cierre/01-conclusion-demostrativa.md:142` — valores reportados: caso 41 D₂=2.82 (firma fractal), caso 42 D₂≈0 (atractor convergente puntual).
- `/datos/repos/EstructurasPreontologicas/06-cierre/03-hoja-de-ruta-para-tesis-final.md:34`.

**Propuesta DRAFT-IA:**

> ### Dimensión de correlación (D₂, Grassberger-Procaccia)
> Estimador de la dimensión fractal del atractor en el espacio de fase reconstruido vía la integral de correlación `C(r) = (1/N²) · #{(i,j) : ‖x_i − x_j‖ < r}`, ajustando `D₂ = lim_{r→0} log C(r) / log r`. Algoritmo: Grassberger y Procaccia (1983, *Physica D* 9: 189-208). Lectura: D₂ no entero indica atractor extraño/fractal; D₂ ≈ entero pequeño indica atractor regular (punto fijo D₂≈0, ciclo límite D₂≈1, toro D₂≈2); D₂ alta y no saturante puede indicar ruido o ausencia de atractor de baja dimensionalidad. Junto con λ_max constituye la firma topológica del atractor. Implementación: `09-simulaciones-edi/common/topology.py`. Capítulo 02-01 §.

**PDF en bibliografía:** NO presente en `07-bibliografia/`.

---

### 2.3 Embedding de Takens

**No aparece en el glosario.**

**Apariciones:**

- `/datos/repos/EstructurasPreontologicas/02-fundamentos/01-ontologia-material-relacional.md:217` — única aparición. Cita: Takens, F., "Detecting strange attractors in turbulence", en *Dynamical Systems and Turbulence, Warwick 1980* (Springer LNM 898, 1981, pp. 366-381). Parámetros: dim=5, retardo τ por primer cero de la autocorrelación. **Nota declarada en el propio manuscrito:** "PDF no disponible en `07-bibliografia/`, paginación verbatim pendiente — el teorema de embedding de retardos enunciado en ese trabajo justifica la reconstrucción".

**Observación crítica:** este término es **load-bearing** para la legitimidad de toda la sección topológica. Sin Takens, λ_max y D₂ calculados sobre series escalares observadas no se justifican (porque ambos requieren un espacio de fase, y Takens es lo que garantiza que la reconstrucción por retardos lo proporciona). Que aparezca solo una vez en el cuerpo y nunca en el glosario es un punto débil estructural.

**Propuesta DRAFT-IA:**

> ### Embedding de Takens (reconstrucción por retardos)
> Teorema de Takens (1981, *Dynamical Systems and Turbulence, Warwick 1980*, Springer LNM 898, pp. 366-381): para una serie temporal escalar `s(t)` observada de un sistema dinámico, el espacio de fase del sistema completo puede reconstruirse mediante vectores de retardo `x(t) = (s(t), s(t-τ), s(t-2τ), ..., s(t-(d-1)τ))` con dimensión de embedding `d` suficientemente grande (regla práctica: `d ≥ 2·D + 1` donde D es la dimensión del atractor). Justifica el cálculo de λ_max y D₂ sobre series observadas cuando el sistema completo no es directamente medible. En el aparato: `dim=5`, `τ` por primer cero de la autocorrelación. Capítulo 02-01 §. **Cita primaria con paginación verbatim pendiente** (PDF no presente en `07-bibliografia/`); si no se localiza, declarar como referencia secundaria.

**Acción asociada:** Tarea fetch-biblio de Takens 1981 (Springer LNM 898) — pendiente para Jacob/Steven.

---

### 2.4 Slaving principle (Haken)

**Estado mixto.** Haken 1977 *Synergetics* sí se cita en la entrada **"Self-organization (sentido técnico)"** del glosario (línea 39), pero el **slaving principle como tal — el mecanismo técnico — no está definido**. La única formulación técnica aparece en:

- `/datos/repos/EstructurasPreontologicas/02-fundamentos/04-anclaje-conductual-ecologico.md:117` — cita verbatim de Haken 1977 cap. 1 p. 1; **el slaving principle se ubica en cap. 7, p. 191-204** según el manuscrito; descripción: "reduce la dinámica de muchos modos a unos pocos modos colectivos cuando el sistema cruza un umbral crítico — operacionalización de la emergencia sin sustancia añadida".

- `/datos/repos/EstructurasPreontologicas/02-fundamentos/04-anclaje-conductual-ecologico.md:123` y `:131` — invocaciones consecuentes.
- `/datos/repos/EstructurasPreontologicas/04-debates/04-anticipacion-objeciones-filosoficas.md:178` — referencia indirecta vía Haken 1977 sin nombrar el principio.

**Diagnóstico:** el slaving principle hace **trabajo argumental** (justifica que la emergencia sea "self-organization sin sustancia"), pero un lector que entre por el glosario solo encuentra la etiqueta "Maturana-Varela + Haken" sin el mecanismo técnico. Esto debilita la entrada "Self-organization" frente a una crítica que pregunte: ¿*qué mecanismo formal* permite reducir muchos grados de libertad a unos pocos modos?

**Propuesta DRAFT-IA (sub-entrada bajo "Self-organization" o entrada nueva):**

> ### Slaving principle (Haken)
> Mecanismo formal de la sinergética (Haken 1977, *Synergetics: An Introduction*, cap. 7, pp. 191-204): cerca de un punto crítico, los modos rápidos del sistema (variables con relajación rápida) son "esclavizados" por los modos lentos (parámetros de orden), de modo que la dinámica de alta dimensionalidad colapsa adiabáticamente sobre una variedad de baja dimensionalidad parametrizada por los modos lentos. Es la **operacionalización formal** de la afirmación "self-organization sin sustancia añadida" del cap 02-01 y 02-04 §4: la reducción dimensional no es postulado filosófico, es teorema dinámico bajo separación de escalas temporales. Conexión empírica con la tesis: la baja dimensionalidad de correlación (D₂ pequeño no entero) reportada en los casos del corpus es la firma observable del esclavizamiento adiabático sobre la variedad central. Capítulo 02-04 §4.

**Cita primaria:** disponible verbatim en cap 02-04 §117 (Haken cap. 1, p. 1); paginación cap. 7, p. 191-204 declarada por el manuscrito y atribuida implícitamente a copia consultada por Jacob — **no presente como PDF en `07-bibliografia/`** (búsqueda local sin coincidencias para "haken" / "synergetics"). Si la copia consultada por Jacob no se anexa, la cita p. 191-204 corre el riesgo de quedar sin verificación independiente; recomendar a Jacob anexar al menos la portada y el índice de la edición usada.

---

## 3. Recomendaciones para Jacob (no ejecutadas)

1. **Insertar las cuatro entradas DRAFT-IA arriba** en `00-proyecto/07-glosario-operativo.md`, en una sección nueva **"Términos del análisis topológico"** ubicada tras "Otros términos del aparato" y antes de "Términos de la teoría conductual". Esta agrupación es coherente con la estructura existente (el glosario ya separa "Operadores formales", "Niveles de emergencia", "Protocolo C1-C5", etc.).
2. **Localizar Takens 1981 (Springer LNM 898)** vía fetch-biblio o biblioteca universitaria; sin paginación verbatim, el manuscrito ya declara la deuda en cap 02-01 §217, pero el glosario debería declararla también si el término entra.
3. **Anexar Haken 1977 a `07-bibliografia/`** o sustituir la paginación cap. 7 p. 191-204 por una fuente secundaria fiable (por ejemplo, Kelso 1995 *Dynamic Patterns* cita el slaving con su propia paginación). Sin PDF anexo, la cita queda como reporte de Jacob, no como cita verificable.
4. **Decisión filosófica H-J**: si Jacob acepta que el slaving principle entre como entrada propia en el glosario, eso **eleva** el status técnico de la afirmación "self-organization sin sustancia" — es bueno argumentalmente, pero carga la prueba de defenderlo bajo crítica. Si lo deja como referencia indirecta dentro de "Self-organization", protege la prosa pero deja el mecanismo formal sin definir. Esta es una decisión de equilibrio entre rigor y carga de prueba que no debe cerrarse desde la asistencia.

---

## 4. Constraints respetados

- No se editó `00-proyecto/07-glosario-operativo.md`.
- No se editó `TesisFinal/Tesis.md`.
- No se tocaron `metrics.json`.
- No se ejecutó git destructivo.
- Paginaciones verbatim no inventadas; donde el PDF no estaba se declaró deuda.

---

RESULT: complete | C4-glossary-coverage | 4 términos auditados, 4 ausentes en glosario, DRAFT-IA propuesto
