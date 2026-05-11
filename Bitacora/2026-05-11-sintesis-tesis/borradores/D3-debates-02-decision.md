---
borrador: IA
requires: H-J*
propuesta_fecha: 2026-05-11
afecta: 04-debates/02-limitaciones-y-puntos-de-presion.md
alternativa_elegida: (b) reducir 02 a sección compacta de contenido único; NO eliminar.
ahorro_lineas_estimado: ~135 (de 200 a ~65)
preserva: §7 Riesgos heredados, §9 tabla "lo que sí puede prometer con fuerza", §10 diálogo Searle/Varela-Thompson/Bourdieu/Latour, §11 filtro de objeciones futuras, §12 fórmula de honestidad filosófica.
elimina_por_duplicacion_con_05: §1-§6 (subsumidos en L1-L20), §8 "fuera de alcance" (duplica 05 §5), §13 cierre (redundante con 05 §8).
referencias_cruzadas_a_02: 1 sola desde el manuscrito vivo (cap 04-01 línea 429, que este borrador D.2 ya reescribe). Detalle en §3.
---

# D.3 — Decisión sobre `04-debates/02-limitaciones-y-puntos-de-presion.md`

## 1. Verificación del claim del reporte 01-redundancia

El reporte `01-redundancia-inter-capitulos.md §D.3` afirma:

> "Las 6 limitaciones genéricas de `02` están todas en las L1-L20 de `05`."

**Verificación lectura-en-mano:**

| `02 §` | Límite declarado | Cobertura en `05` | Veredicto |
|---|---|---|---|
| §1 Alcance asimétrico entre dominios | L9 (4/30 overall_pass), L5 (caso 30 piloto), L7-L8 (corpus inter-escala sintético) | **Cubierto.** `05` lo desagrega en tres limitaciones más precisas con plazo. |
| §2 Dependencia del caso ancla | L5 (caso 30 marginal post-calibración) + L6 (caso 38 failure mode) | **Parcialmente cubierto.** `05` trata el caso ancla específico; `02` lo trata como *dependencia estructural de la tesis*. La diferencia es de framing, no de contenido. |
| §3 Vigilancia permanente del propio léxico | No aparece en `05` | **No cubierto.** Es contenido único de `02`. |
| §4 Tratamiento programático de la dimensión normativa | L10 (caso piloto COVID, sondas con histéresis) | **Cubierto.** L10 es operacional; `02 §4` es filosófico. La diferencia es de framing. |
| §5 Dependencia de prácticas científicas externas para κ | L11 (κ-ontológica fuerte no demostrada; sondas independientes) | **Parcialmente cubierto.** L11 trata la κ; `02 §5` trata la dependencia metodológica de PCA, Lyapunov, dimensión de correlación. La diferencia es de granularidad. |
| §6 Deuda con la fenomenología y experiencia vivida | L13 (dimensión fenomenológica) | **Cubierto.** L13 lo dice más corto. |
| §7 Riesgos heredados (7.1 inmunización por nivel, 7.2 hipertrofia metodológica, 7.3 asimetría desigual entre dominios) | No aparece en `05` | **No cubierto.** Contenido único: tres riesgos operativos con antídotos declarados. |
| §8 Tabla "lo que la tesis NO debe prometer" (4.2.1) | `05 §5` "Fuera de alcance" cubre el mismo material. Auditoría C.7 ya lo marca como duplicado. | **Cubierto. Eliminable.** |
| §9 Tabla "lo que la tesis sí puede prometer con fuerza" (4.2.2) | No aparece en `05` | **No cubierto.** Contenido único: contraparte positiva de §8, declaración pública del estado del manuscrito. |
| §10 Diálogo con interlocutores (Searle, Varela-Thompson, Bourdieu, Latour) | No aparece en `05` | **No cubierto.** Contenido único: posicionamiento filosófico explícito. |
| §11 Filtro de objeciones futuras (matriz de 6 preguntas) | No aparece en `05` | **No cubierto.** Contenido único: protocolo de evaluación de objeciones. |
| §12 Fórmula de honestidad filosófica | No aparece en `05` | **No cubierto.** Contenido único: cita-marco autoral. |

**Conclusión empírica:** el claim del reporte 01-redundancia es **parcialmente correcto**. Sí: §1, §4, §6, §8 están cubiertos por `05`. No: §3, §7, §9, §10, §11, §12 contienen material único que `05` no contiene. La salida "eliminar `02` completo" pierde contenido sustantivo no recuperable de `05`.

## 2. Salida elegida

**Salida (b)** — reducir `02` a sección compacta que preserve el contenido único, eliminando lo subsumido por `05`.

**Justificación bajo criterio de defendibilidad** (no de pereza):

1. Los §7, §9, §10, §11 de `02` no están en `05` y aportan valor argumentativo distintivo: el §7 (riesgos heredados con antídotos) es la salvaguarda operativa contra inmunización del propio marco; el §10 (diálogo con Searle, Varela-Thompson, Bourdieu, Latour) es posicionamiento filosófico explícito que en `05` solo aparece como deuda bibliográfica; el §11 (filtro de objeciones futuras) es protocolo defendible en defensa oral. Eliminarlos sin migración es regresión.
2. La diferencia de framing entre `02` y `05` no es accidental. `05` es **inventario consolidado con plazos** (formato para defensa: "está fechado, está declarado, está priorizado"). `02` es **discurso filosófico sobre el régimen de validez** (formato para argumentación: "esto es lo que la tesis NO promete y POR QUÉ no debilita la tesis declararlo"). Las dos voces son legítimas y se complementan; eliminar `02` colapsa la voz argumentativa en la voz de inventario. La regla §3 del CLAUDE.md raíz ("la voz autoral filosófica de la tesis es de Jacob Agudelo... ofrecer opciones, no decisiones") aconseja preservar la voz argumentativa.
3. La salida (a) (eliminar `02`) ahorra ~200 líneas. La salida (b) ahorra ~135. La diferencia (~65 líneas) es el precio de preservar voz filosófica única. **El criterio no es máximo ahorro; es máxima defendibilidad por línea conservada.**
4. Migrar §1-§6 a `05` como "L21-L26" duplicaría el inventario sin valor añadido: las L1-L20 ya son específicas y operacionales; los §1-§6 de `02` son **genéricos**. La granularidad correcta vive en `05`.
5. Mover `02` a `_extendido/` no es opción adecuada: §7, §9, §10, §11 contienen carga argumental que `_extendido/` no debe alojar (regla `00-proyecto/_extendido/README.md`).

## 3. Referencias cruzadas a `04-debates/02-*.md`

Búsqueda con `grep -rn "04-debates/02" --include="*.md"`:

| Origen | Línea | Referencia | Acción |
|---|---|---|---|
| `04-debates/01-debates-con-posiciones-rivales.md` | 429 | "queda como punto de presión legítimo y se trata en `04-debates/02-limitaciones-y-puntos-de-presion.md`" (Glennan 2017) | El borrador D.2 (`Bitacora/2026-05-11-sintesis-tesis/borradores/D2-debates-01-consolidado.md` §3.6) ya reescribe esta referencia apuntando a `04-debates/05-...` §3 (L11) en lugar de `04-debates/02`. **Cerrado en D.2.** |
| `TesisFinal/Tesis.md` | 6876 | Misma frase, propagada por `TesisFinal/build.py`. | Se regenera al ejecutar `python3 TesisFinal/build.py` después de aplicar D.2. **Automático.** |
| `Bitacora/2026-05-05-continuous-run/C4-glossary-coverage.md` | 16, 34, 50 | Tres menciones a "04-debates/02" como ubicación de "Exponente de Lyapunov" y "dimensión de correlación". | Estas son **anotaciones de auditoría** sobre glosario, no carga argumental. La sección reducida de `02` conserva la mención técnica si Jacob lo decide; si no, las anotaciones se actualizan al cerrar el harness pass. **No bloquea la decisión.** |
| `Bitacora/2026-05-11-sintesis-tesis/...` | varias | Auto-referencias del propio reporte de redundancia. | Trivial. |
| `Bitacora/2026-05-11-sintesis-tesis/02-triage-bitacora-huerfana.md` | varias | Anotaciones de auditoría de tabla de rivales. | Trivial. |

**Total de referencias del manuscrito vivo (no bitácora):** 1 sola (`04-debates/01` línea 429), ya reescrita en el borrador D.2. **No hay bloqueador estructural para reducir `02`.**

Adicional: `TesisFinal/build.py` línea 104 incluye explícitamente `04-debates/02-limitaciones-y-puntos-de-presion.md` como "Capítulo 28: Limitaciones y puntos de presión" del PARTS. La salida (b) **no requiere modificar** `build.py` (el archivo sigue existiendo, solo más corto). La salida (a) **sí requeriría** eliminar la línea 104 y renumerar capítulos 28-29 a 28 (28 actual = `02` desaparece, 29 actual = `05` pasa a 28). Esto es razón adicional para preferir (b): salida (b) es menos invasiva sobre `build.py`.

## 4. Borrador del `02` reducido (~65 líneas)

```markdown
# Riesgos heredados y posicionamiento filosófico declarado

## Tesis del capítulo

> Bajo el aparato corregido, la tesis sostiene tres riesgos operativos que requieren vigilancia permanente, una contraparte positiva de lo que sí promete con fuerza, un diálogo declarado con cuatro interlocutores prioritarios (Searle, Varela-Thompson, Bourdieu, Latour), un filtro para evaluar objeciones futuras, y una fórmula de honestidad filosófica. Este capítulo no inventaria limitaciones operativas (esa función la cumple `04-debates/05-limitaciones-declaradas-consolidacion.md` con L1-L20 fechadas); aquí se declara la postura argumentativa que sostiene la lista.

## 1. Riesgos heredados que sobreviven

Tres riesgos quedan abiertos como vigilancia permanente y se documentan aquí para evitar olvido durante la redacción final. No son limitaciones cerrables con entregable: son patrones de degradación que el marco debe controlar mientras esté en uso.

### 1.1. Inmunización por nivel

La cláusula "el nivel correcto depende de la pregunta" puede convertirse en escudo retórico. Antídoto fijado en `03-formalizacion/02-...`: Q se fija fechada antes del intento; cambiar Q después del fallo invalida el ciclo.

### 1.2. Hipertrofia metodológica

Una tesis que se concentra demasiado en sus propios protocolos pierde de vista el explanandum. Antídoto: el caso ancla canónico es el centro fenomenológico; los protocolos solo se justifican mientras mejoran el tratamiento del caso ancla o un dominio análogo.

### 1.3. Asimetría desigual entre dominios

El caso ancla es asimétricamente más sólido que cualquier otro dominio del manuscrito. Antídoto: la asimetría no se disimula. `06-cierre/` la nombra y la convierte en programa de investigación posterior. (Cf. L5, L7-L9 en `04-debates/05-...` para el detalle fechado del inventario operativo correspondiente.)

## 2. Lo que la tesis sí puede prometer con fuerza

Para que la declaración honesta de los límites (`04-debates/05-limitaciones-declaradas-consolidacion.md`) no se lea como abdicación, este capítulo declara la contraparte positiva: aquello que la tesis sostiene con fuerza demostrativa, no programática.

**Tabla 4.2.1.**

| Promesa sostenida | Estado |
|---|---|
| Ontología material-relacional sobria | Sostenida en cap 02 |
| Epistemología de compresión controlada | Sostenida en cap 02-02 y 03-04 |
| Criterios explícitos de legitimidad categorial | Sostenidos en cap 03-02 |
| Metodología de auditoría ontológica | Sostenida en cap 03-03 |
| Mejor articulación entre niveles, modelos y categorías | Demostrada en cap 05-05 |
| Discriminación pública contra rivales identificables | Sostenida en cap 04-01 y 04-03 |

La tabla 4.2.2 original ("Lo que la tesis NO debe prometer") se elimina por duplicación con `04-debates/05-limitaciones-declaradas-consolidacion.md §5` ("Fuera de alcance"). Ese inventario es la fuente única de las promesas rechazadas; la promesa positiva queda aquí.

## 3. Diálogo declarado con interlocutores filosóficos

Cuatro interlocutores reciben tratamiento posicional explícito en este capítulo porque ninguno se reduce a entrada de inventario L1-L20:

**Searle — ontología social y dimensión normativa.** Searle insiste en intencionalidad colectiva y reglas constitutivas como rasgos irreductibles de lo institucional. La tesis lo recoge parcialmente: la dimensión normativa es real pero su operacionalización empírica está pendiente (cf. L10 en `04-debates/05-...`). Searle es interlocutor obligado del programa posterior sobre instituciones.

**Varela y Thompson — fenomenología naturalizada.** Varela y Thompson proponen una fenomenología naturalizada que articule descripción en primera persona con neurociencia y dinámica. La tesis se inscribe en ese horizonte programático para la dimensión vivida (cf. L13 en `04-debates/05-...`).

**Bourdieu — espesor histórico y práctico.** Bourdieu insiste en que las prácticas sociales tienen historia incorporada (*habitus*) que no se reduce a regla actual. La tesis recoge la advertencia y la incluye como variable histórica del nivel B.

**Latour — controversia con el inventario.** Latour propone redes con actantes humanos y no-humanos. La tesis admite la red pero exige filtro de admisión: no todo lo que se nombra como actante es patrón estabilizado en el sentido del marco.

## 4. Filtro de objeciones futuras

Toda objeción nueva al manuscrito se evalúa con esta matriz antes de respuesta:

1. ¿es objeción a inflación ontológica?
2. ¿es a pérdida de estructura relevante?
3. ¿es a vaguedad metodológica?
4. ¿es a falta de anclaje empírico?
5. ¿es a exceso de abstracción?
6. ¿es a redundancia con marcos vecinos?

Si no cae en ninguna, probablemente está mal formulada. Si cae en alguna, la respuesta debe ser por compromiso verificable, no por reformulación retórica.

## 5. Fórmula de honestidad filosófica

> La tesis no pretende clausurar la complejidad de lo real. Pretende ofrecer mejores reglas para no empeorarla con malas categorías, dossier de anclaje verificable, asimetría L1↔B↔L3↔S como protocolo, y caso paradigmático trabajado a fondo. Sus límites son nombrados, sus deudas son fechadas, sus promesas son delimitadas.

## 6. Lectura cruzada

- Inventario operativo de limitaciones fechadas con entregable: `04-debates/05-limitaciones-declaradas-consolidacion.md` (L1-L20).
- Anticipación de objeciones filosóficas con F1-F10: `04-debates/04-anticipacion-objeciones-filosoficas.md`.
- Confrontación con rivales discursivos: `04-debates/01-debates-con-posiciones-rivales.md`.
- Matriz síntesis 14×6 de rivales: `04-debates/03-tabla-comparativa-rivales.md`.
```

## 5. Acciones requeridas si Jacob firma la salida (b)

1. **Reemplazar el contenido actual de `04-debates/02-limitaciones-y-puntos-de-presion.md`** (200 líneas) por la versión reducida del §4 anterior (~65 líneas).
2. **No modificar `TesisFinal/build.py`** (línea 104 sigue válida; el archivo sigue existiendo).
3. **Re-ejecutar `python3 TesisFinal/build.py`** para regenerar `TesisFinal/Tesis.md` con la versión reducida + la corrección de la referencia cruzada introducida por el borrador D.2 (línea 429 de `04-debates/01` → ahora apunta a `04-debates/05` para Glennan).
4. **Renumerar tablas** con `scripts/number_tables.py`: la tabla 4.2.2 desaparece, la 4.2.1 sobreviviente se renombra si el script lo decide canónicamente.
5. **Actualizar `Bitacora/2026-05-05-continuous-run/C4-glossary-coverage.md`** (3 menciones a `04-debates/02` que ya no apuntan a las líneas declaradas): tarea menor, no bloqueante.
6. **Registrar en `TAREAS_PENDIENTES.md`** la decisión cerrada con su entregable.

## 6. Decisiones que requieren firma de Jacob

1. **¿Salida (a) o (b)?** Este borrador defiende (b). Si Jacob considera que el contenido de §7, §9, §10, §11 está suficientemente protegido por otros capítulos (`06-cierre/`, `04-debates/04`), puede preferir (a) con ahorro adicional de ~65 líneas. El borrador no toma esa decisión.
2. **Si (b): ¿el título "Riesgos heredados y posicionamiento filosófico declarado" es adecuado?** El título original "Limitaciones y puntos de presión" sería engañoso después de la reducción (las limitaciones operativas ya no viven aquí). El borrador propone el nuevo título; Jacob decide.
3. **¿Mantener `02` en su posición canónica del PARTS (capítulo 28) o moverlo después de `05` (capítulo 29 → 28, `02` → 29)?** El borrador no reordena. Si se conserva `02` reducido, la lógica narrativa sería: el lector primero consulta el inventario completo (`05`), luego la postura argumentativa (`02` reducido). Eso sugiere reordenar `02` después de `05`. Decisión H-J*.
