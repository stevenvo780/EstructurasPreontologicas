# F02-11 — Síntesis Bateson + Dretske declarada como "combinación" pese a incompatibilidad

**Fecha:** 2026-05-04
**Origen:** adversarial-reviewer cap 02 (2026-05-05), ref. Adams 2003, *The Informational Turn in Philosophy* (Minds and Machines 13:471–501).
**Archivos auditados:** `02-fundamentos/04-anclaje-conductual-ecologico.md` líneas 50–67.
**Estado:** `needs_human` (decisión filosófica de re-anclaje primario H-J*) + edición técnica propuesta.

---

## (a) Verificación de la afirmación

Texto actual (líneas 54, 59, 67):

> "La tesis adopta una **definición material-relacional de información** que **combina dos tradiciones**: Bateson (1972) [...] Dretske (1981) [...]"
>
> "**Síntesis de la tesis:** la información es diferencia materialmente realizada [...] que modula la dinámica del sistema acoplado cuando es detectada por sistemas perceptivos calibrados."
>
> "información ecológica (Gibson, Bateson + tesis): diferencia materialmente realizada que modula dinámica acoplada **sin requerir representación interna**."

La objeción del adversarial-reviewer es válida y no es de matiz:

1. **Bateson (1972)** — el "*difference which makes a difference*" es un dispositivo **cibernético-relacional** explícitamente formulado contra el reduccionismo informacional shannoniano. La "diferencia" es **observador/sistema-dependiente**: solo cuenta como información cuando hay un *circuito mental* que la registra (Bateson, *Steps*, "Form, Substance and Difference"). No es propiedad intrínseca del entorno.
2. **Dretske (1981)** — la información semántica es **correlación nómica objetiva** entre estados de la fuente y del receptor, fundada en probabilidades condicionales shannonianas (cap. 3). Es un realismo informacional **externalista** que presupone exactamente el aparato probabilístico que Bateson resiste.
3. **Adams 2003** documenta que el "informational turn" anglo (Dretske, Fodor, Floridi) se constituye **sin Bateson** y, donde se cruzan, lo hacen como tradiciones rivales: Bateson aporta retórica, Dretske aporta ontología semántica. Combinarlas como si compartieran sustrato es elisión.

**Veredicto:** el verbo "combina" es engañoso. La tesis no combina las dos tradiciones; **selecciona** elementos (la metáfora de la diferencia, el externalismo de la correlación) y los **reinterpreta** dentro de un marco gibsoniano. Eso no es combinación, es **subordinación bajo Gibson**.

Verificación bibliográfica local: no hay PDF de Dretske 1981 ni Bateson 1972 en `07-bibliografia/`; sí está Gibson 1979. Las paginaciones citadas (Bateson p. 459, Dretske p. 63) no se pudieron auditar contra fuente primaria en este pase — queda como deuda menor (B-T).

## (b) Propuesta de edición concreta (§2.3.0)

Reescritura mínima que (i) elimina "combina", (ii) declara primaria Gibson-Dretske operativa, (iii) reconoce la tensión con Bateson y la resuelve por subordinación, no por síntesis:

```markdown
#### 2.3.0. Definición filosófica de información

La tesis adopta una definición **gibsoniana operativa** de información,
con anclaje semántico dretskiano y un uso heurístico (no constitutivo)
de Bateson.

- **Primaria (Gibson 1979, p. 127–143):** la información ecológica es
  estructura **especificacional** del arreglo óptico/acústico/háptico
  ambiental: invariantes que están materialmente inscritos en la
  geometría del entorno y que sistemas perceptivos calibrados
  detectan sin representarlos internamente.
- **Anclaje semántico (Dretske 1981, cap. 3):** cuando se requiere
  decir *de qué* informa una variable ecológica, la tesis usa la
  correlación nómica dretskiana entre estado de la fuente y estado
  del receptor que sostiene inferencia confiable. Este es el
  componente externalista que justifica hablar de información
  *materialmente realizada*, no en la mente del observador.
- **Heurístico (Bateson 1972):** el lema *"a difference which makes
  a difference"* se conserva como recurso expositivo, no como
  fundamento. Reconocemos que Bateson es **incompatible** con
  Dretske en su forma fuerte: el primero hace la diferencia
  observador-dependiente y resiste el aparato probabilístico
  shannoniano que el segundo presupone (Adams 2003). La tesis no
  intenta sintetizar ambas tradiciones; **subordina** la metáfora
  batesoniana al realismo informacional gibsoniano-dretskiano.

**Costo declarado:** al elegir Gibson-Dretske como espina operativa,
la tesis pierde la sensibilidad cibernética de Bateson al
observador-en-el-circuito. Eso es coherente con la postura
material-relacional defendida en el cap. 02-01: lo que ancla B no es
el observador sino el acoplamiento dinámico. Quien quiera retener
Bateson como fundamento (no como heurístico) tiene que rechazar
también el externalismo dretskiano, y con él la cláusula
"materialmente realizada" que el aparato EDI necesita.

**Distinción operativa:**

- **información sintáctica** (Shannon): reducción de incertidumbre
  estadística;
- **información semántica** (Dretske, Floridi): correlación nómica
  con contenido inferencial;
- **información ecológica** (Gibson, con anclaje dretskiano):
  invariantes especificacionales del entorno que modulan la
  dinámica del sistema acoplado **sin requerir representación
  interna**.

La tesis usa principalmente **información ecológica** así definida.
```

Cambios respecto al texto actual:

- "combina dos tradiciones" → "Primaria Gibson, anclaje Dretske, heurístico Bateson".
- Bateson deja de ser co-fundamento y pasa a recurso expositivo.
- Tensión Bateson/Dretske declarada explícitamente con cita Adams 2003.
- Costo argumentativo añadido al final del bloque (no oculto).
- Línea 67 ("Gibson, Bateson + tesis") debe sustituirse por "Gibson, con anclaje Dretske".

## (c) Costo argumentativo declarado

1. **Pérdida cibernética:** el observador-en-el-circuito de Bateson queda fuera. Para una tesis material-relacional esto es coherente, pero hay que asumirlo en el cap. 04-debates (§ rivales constructivistas).
2. **Compromiso externalista:** apoyarse en Dretske obliga a sostener correlaciones nómicas objetivas. Si en algún caso EDI la "información" reportada falla la prueba de correlación nómica (p. ej., variables internas del modelo que no especifican estado del entorno), la tesis debe aceptar que ahí ya no aplica el rótulo "información ecológica".
3. **Deuda bibliográfica menor:** la paginación Bateson p. 459 y Dretske p. 63 no se auditó contra fuente primaria en este pase. Marcar como B-T (verificación con PDFs cuando estén accesibles).

## Estado de cierre

- **needs_human:** la decisión de degradar Bateson de co-fundamento a heurístico es filosóficamente sustantiva y requiere firma de Jacob (H-J*). La asistencia no la cierra.
- **Acción técnica reversible:** la propuesta de edición de §2.3.0 está lista; aplicar solo tras visto bueno de Jacob.
- **No se editan** `Tesis.md` ni `metrics.json` en este pase.
