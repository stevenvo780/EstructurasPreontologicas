# F02-02 — Cita Craver 2007 p.153 mediada vía críticos

**Fecha:** 2026-05-04
**Tipo:** Auditoría bibliográfica + filosófica
**Estado:** `needs_human` (parcial)
**Origen:** Hallazgo adversarial-reviewer cap02 (2026-05-05)
**Archivo afectado:** `02-fundamentos/05-temporalidad-y-causalidad.md:90-92`

---

## 1. Verificación del hallazgo

El adversarial señala una circularidad bibliográfica: la tesis cita a **Craver 2007** (p. 153, criterio de manipulabilidad mutua) **mediada por** dos fuentes secundarias —Romero 2015 y Baumgartner & Gebharter 2016— que **precisamente refutan** ese criterio (la objeción de *fat-handedness* y la insuficiencia lógica de la doble manipulabilidad para fijar relevancia constitutiva). Es decir: el manuscrito invoca como autoridad la formulación canónica del criterio, sin engagement con que las fuentes que la transmiten sostienen que ese criterio **falla**.

Estado verificado en `02-fundamentos/05-temporalidad-y-causalidad.md:90-92`:

- Línea 90 cita verbatim a Craver 2007 §4.4 p. 153.
- Línea 92 declara explícitamente la mediación por Romero 2015 y Baumgartner-Gebharter 2016 (cumple CLAUDE.md §5 *formalmente*).
- **Pero**: la tesis usa la formulación de Craver de modo *afirmativo* (línea 104: "Esto es exactamente la noción de Craver (*mutual manipulability*) operacionalizada por intervención ablativa") sin reconocer que las dos fuentes mediadoras impugnan que la doble manipulabilidad baste para distinguir constitución genuina de artefactos de intervención (*fat-handedness*: una intervención sobre φ que también altera ψ por vías no constitutivas).

**Diagnóstico:** La cita es formalmente honesta (declarada como mediada) pero **sustantivamente débil**: importa el aparato Craver sin enfrentar la objeción que las propias fuentes mediadoras formulan **contra** ese aparato. Esto es exactamente el patrón "cita decorativa" de CLAUDE.md §5, sólo que mediado por una capa de cobertura formal.

## 2. Acceso a PDFs

Búsqueda en `07-bibliografia/`:

- **Craver 2007** *Explaining the Brain* — **NO presente**. Verificado por `find` con patrones `craver`, `explaining*brain`. Ningún match.
- **Baumgartner & Gebharter 2016** *BJPS* 67:731-756 — **NO presente**.
- **Romero 2015** *Synthese* 192:3731-3755 — **NO presente**.

Sin acceso primario a estos tres textos, **no puedo cumplir** el acceptance criterion "PDF Craver 2007 verificado p.152-153". Requiere:

1. `/fetch-biblio` para Craver 2007, Baumgartner-Gebharter 2016, Romero 2015.
2. Verificación posterior con `@citation-agent` sobre los PDFs descargados.

## 3. Propuesta de edición concreta

La edición sustantiva requiere **firma filosófica de Jacob** (CLAUDE.md §3 — voz autoral filosófica). Lo que sí puedo aportar es la **estructura argumental** de la respuesta, marcada DRAFT-IA, para que Jacob la corte/reescriba:

### 3.1. Edición mínima a línea 92 (aceptable sin firma filosófica)

Añadir al final del párrafo de "Nota de acceso bibliográfico" la cláusula:

> Las fuentes mediadoras (Romero 2015; Baumgartner & Gebharter 2016) reproducen verbatim la formulación de Craver **en el contexto de impugnarla**: ambas argumentan que la manipulabilidad mutua, aislada, no fija relevancia constitutiva por la objeción de *fat-handedness*. La tesis adopta la formulación de Craver pero **debe** responder a esa objeción en §2.4.5; mientras la respuesta no se inserte y verifique con PDFs primarios, esta cita queda como **deuda metodológica activa**, no como soporte cerrado.

### 3.2. Sub-sección nueva §2.4.5 (REQUIERE FIRMA JACOB — DRAFT-IA)

Estructura propuesta (no prosa final):

**§2.4.5. Respuesta a la objeción de *fat-handedness* (Baumgartner-Gebharter 2016)**

1. **Enunciado de la objeción:** una intervención sobre φ (componente) puede alterar ψ (actividad) por dos vías distinguibles: (a) porque φ es constitutivamente parte de ψ (lo que Craver quiere capturar) o (b) porque la intervención es "fat-handed" — toca causalmente otros componentes que también constituyen ψ. La doble manipulabilidad **no discrimina** entre (a) y (b).
2. **Por qué esto importa al EDI:** la intervención `do(coupling = 0)` del aparato EDI es, formalmente, una intervención simultánea sobre todas las aristas de acoplamiento ODE→ABM. Es **estructuralmente fat-handed** en el sentido de Baumgartner-Gebharter: no aísla un componente, ablaciona el régimen de acoplamiento entero.
3. **Respuesta posicional honesta (a discutir con Jacob):**
   - **Opción A (concesiva fuerte):** reconocer que EDI no resuelve el problema de Baumgartner-Gebharter para casos individuales; la inferencia que sostiene es **a nivel de régimen** (el acoplamiento como conjunto es constitutivamente relevante para la dinámica observada), no a nivel de componente individual. Coste: la tesis pierde la pretensión de identificar componentes constitutivos específicos vía EDI.
   - **Opción B (sustitución del criterio):** abandonar manipulabilidad mutua y adoptar el criterio alternativo de **boolean dependence** de Baumgartner-Gebharter (2016, §4-5) o el de **interventionist sufficiency** de Krickel (2018). Coste: requiere reescribir §2.4.2 y §2.4.3, y el aparato EDI en su forma actual no instancia limpiamente esos criterios alternativos.
   - **Opción C (defensa restringida):** la objeción de fat-handedness aplica a la inferencia de constitución a partir de manipulabilidad mutua **en sistemas modulares**; en sistemas con acoplamiento denso (los del corpus EDI), la distinción (a)/(b) **no tiene contenido empírico** porque no hay descomposición modular única del régimen acoplado. Coste: requiere defender filosóficamente que la modularidad es presupuesto, no hallazgo, y que su ausencia disuelve la objeción.

Las tres opciones tienen costos distintos. La elección no se puede automatizar — es una decisión filosófica sobre qué tan ambiciosa quiere ser la tesis respecto a inferencia constitutiva.

## 4. Costo argumentativo declarado

- Si se aplica solo §3.1 (edición mínima): la tesis declara abiertamente que tiene una deuda activa con la objeción Baumgartner-Gebharter. **Coste:** una pieza más en la lista de deuda residual; **beneficio:** elimina la apariencia de cita decorativa.
- Si se aplica §3.2 con Opción A: la tesis se vuelve más modesta sobre lo que EDI infiere (régimen, no componente). **Coste:** debilita el discurso sobre "componentes constitutivos"; **beneficio:** evita que un evaluador con formación en mecanismos use Baumgartner-Gebharter para descartar el aparato.
- Si se aplica §3.2 con Opción C (la más fuerte filosóficamente): convierte una objeción en confirmación posicional (la modularidad presupuesta no es propiedad del dominio EDI). **Coste:** requiere defender la sustantividad de la no-modularidad; **beneficio:** convierte una vulnerabilidad en marca distintiva del programa.

## 5. Acción solicitada

- [ ] **B-T (técnica):** `/fetch-biblio` para Craver 2007, Baumgartner-Gebharter 2016, Romero 2015 → depositar en `07-bibliografia/`.
- [ ] **B-T (técnica):** tras descarga, `/verify-citations` sobre p. 152-153 de Craver y p. 731-756 (núcleo §3-4) de Baumgartner-Gebharter.
- [ ] **H-J (humana, Jacob):** decidir entre Opción A / B / C de §3.2 y redactar §2.4.5 con su voz.
- [x] **AI ahora:** este reporte; queda como `needs_human` para los tres puntos anteriores.

## 6. Estado de acceptance

Acceptance declarado: *"PDF Craver 2007 verificado p.152-153 + párrafo nuevo en §2.4 que responde a Baumgartner-Gebharter 2016 sobre fat-handedness en ablación EDI"*.

- PDF Craver: **no cumplido** (PDF ausente).
- Párrafo nuevo §2.4.5: **no cumplido** — entregada estructura DRAFT-IA con tres opciones y costos, pendiente de firma Jacob.

**Marcar tarea: `needs_human`.**
