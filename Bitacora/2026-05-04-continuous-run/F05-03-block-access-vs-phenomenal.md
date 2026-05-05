# F05-03 — Block 1995 (access vs phenomenal) omitido en §7.1 qualia

**Fecha:** 2026-05-04
**Hallazgo origen:** adversarial-reviewer cap05 (2026-05-05)
**Archivo objetivo:** `05-aplicaciones/01-mente-memoria-yo.md` §7.1 (líneas 220-225)
**Estado:** `needs_human` — requiere acceso a fuente primaria + firma de Jacob.

---

## 1. Verificación de la afirmación del adversarial

El adversarial sostiene que §7.1 ("Postura sobre los qualia") **omite la distinción técnica más importante de los últimos 30 años en filosofía de la conciencia**: Ned Block (1995), "On a confusion about a function of consciousness", *Behavioral and Brain Sciences* 18:227-247, donde se separa:

- **A-consciousness (access consciousness):** estado mental cuyo contenido está disponible para razonamiento, control verbal y control de la acción. Funcional, en tercera persona.
- **P-consciousness (phenomenal consciousness):** la cualidad experiencial bruta, el "what-it-is-like-ness". No reducible a A-consciousness por argumento.

**Lectura de §7.1 (líneas 220-225):** la sección habla de "qualia (cualidades fenoménicas: el rojo del rojo, el dolor del dolor)" y los declara *no reducibles a atractores conductuales* pero *no requirentes de sustancia mental separada*. **No menciona a Block, ni la distinción A/P, ni el argumento que la sostiene.** El hallazgo del adversarial es **correcto**: la omisión es real y materialmente relevante porque la distinción A/P organiza la disputa contemporánea sobre qualia (Chalmers 1996, Tye 1995, Dennett 1995-2005, Carruthers, Rosenthal) y la tesis no puede sostener una postura naturalista no-reduccionista sobre qualia sin posicionarse respecto a ella.

**Costo de la omisión:** la prosa actual queda en un nivel pre-1995. Un lector entrenado en filosofía analítica de la conciencia detectará inmediatamente que la sección no engancha con la disputa real.

---

## 2. Imposibilidad de cumplir el acceptance criterion desde la asistencia

Acceptance pedía: *cita textual Block 1995 BBS 18 p.230-231 + posicionamiento explícito A-consciousness vs P-consciousness*.

**Búsqueda en `07-bibliografia/`:** Ned Block (1995) BBS 18 NO está disponible localmente (búsqueda `*block*` y `*consciousness*` vacía). El paper es accesible públicamente en la página de Block en NYU, pero CLAUDE.md §5 prohíbe citar con paginación sin verificación contra fuente, y la asistencia computacional no puede garantizar paginación BBS sin abrir el PDF.

**Por tanto:** la cita textual paginada **no se produce desde aquí**. Cualquier intento de la asistencia de poner *"p.230-231"* con texto entre comillas sería violación directa de CLAUDE.md §5 ("cita decorativa" = F6).

---

## 3. Propuesta de edición concreta (DRAFT-AI, requiere firma de Jacob)

Insertar tras línea 225 una sub-sección **§7.1.1** con esta estructura — el texto entre comillas del fragmento de Block queda como **placeholder `[CITA-BLOCK-1995]`** que Jacob (o `@citation-agent` con el PDF descargado a `07-bibliografia/`) debe completar con paginación BBS 18 verificada:

```markdown
### 7.1.1. Distinción access vs phenomenal (Block 1995)

La disputa contemporánea sobre qualia está organizada por la distinción de
Block (1995, *Behavioral and Brain Sciences* 18:227-247) entre:

- **A-consciousness (acceso):** un estado es A-consciente si su contenido está
  disponible para razonamiento, reporte verbal y control racional de la acción.
  Es una propiedad **funcional**, capturable en tercera persona.
- **P-consciousness (fenoménica):** la cualidad experiencial misma — el
  "what-it-is-like-ness" en sentido de Nagel (1974). Block argumenta que es
  conceptualmente independiente de A-consciousness:
  [CITA-BLOCK-1995, BBS 18 p.230-231 — needs_human verificación PDF].

**Posicionamiento de la tesis frente a la distinción:**

- el aparato EDI describe **A-consciousness operacionalizada como atractor
  conductual con disponibilidad para control de la acción**: la integración
  que el operador μ captura es access-consciousness materializada en la
  dinámica acoplada organismo-entorno (cap 02-04 §2);
- el aparato EDI **NO describe P-consciousness**: esa es exactamente la
  brecha que el "problema duro" de Chalmers (§7.2) marca y que la tesis
  declara no abordar en su régimen de tercera persona;
- la tesis acepta el realismo de P-consciousness (no es eliminativista al
  modo de Dennett 1991/2005, cuya estrategia de disolver P-consciousness
  en A-consciousness la tesis rechaza por sobre-extensión del aparato
  funcional);
- **costo declarado:** al aceptar el realismo de P-consciousness sin
  reducirla a A-consciousness, la tesis se compromete a una posición
  **naturalista no-reduccionista de doble aspecto operativo**, no a
  fisicalismo tipo-tipo ni a funcionalismo clásico. Esto es coherente con
  §7.2 (complementariedad con fenomenología) pero debe sostenerse contra
  Dennett (eliminación de P) y contra Chalmers (dualismo de propiedades).
```

**Cambios derivados que esta inserción exige:**

1. Renumerar §7.1.1 → §7.1.2 si ya existe sub-numeración (no la hay actualmente).
2. Añadir entrada Block 1995 a `07-bibliografia/01-bibliografia-orientativa.md` cuando el PDF se incorpore.
3. Crear ítem en `TAREAS_PENDIENTES.md` Sección B-T como **B-T-BLOCK1995**: descargar Block (1995) BBS 18 a `07-bibliografia/`, verificar paginación, sustituir placeholder.
4. La frase de §7.1 actual *"los qualia son propiedades constitutivas del sistema acoplado organismo-mundo bajo el aspecto en primera persona"* sobrevive intacta — la nueva §7.1.1 la enriquece, no la contradice.

---

## 4. Costo argumentativo declarado

- **Costo de aceptar realismo de P-consciousness (lo que esta edición hace explícito):** la tesis se distancia de Dennett en este punto específico (Dennett trata P como ilusión cognitiva o como nada-sobre-y-encima-de A). Esto **fricciona** con §6.1 donde Dennett aparece como aliado en "patrones reales" / "centro de gravedad narrativo". La fricción no es contradicción — uno puede recoger a Dennett en yo-narrativo y rechazarlo en qualia — pero **debe declararse**, porque ahora mismo §6.1 lee como adhesión global a Dennett.
- **Costo de no abordar P-consciousness con el aparato EDI:** la tesis acepta una **brecha explicativa permanente** en su lado de tercera persona. §7.2 ya lo declaraba para Chalmers; la nueva §7.1.1 lo formaliza con el vocabulario de Block.
- **Costo de no reducir P a A:** cierra puertas funcionalistas duras (Lewis, Armstrong, Dennett) pero abre la puerta a acusaciones de "qualia freak" en sentido de Dennett (1988). La tesis lo asume.

---

## 5. Estado y siguiente paso

- **Hallazgo del adversarial:** confirmado.
- **Edición propuesta:** redactada como DRAFT-AI arriba; **NO aplicada al manuscrito** porque (a) requiere cita textual con paginación que la asistencia no puede verificar y (b) toca una decisión filosófica (alineamiento parcial con Dennett en yo-narrativo + ruptura con Dennett en qualia) que es de Jacob.
- **Marca:** `needs_human` — requiere:
  1. `@bibliography-fetcher` o Jacob: descarga de Block 1995 BBS 18 a `07-bibliografia/`.
  2. `@citation-agent`: verificación textual paginada de la cita Block que sustituya `[CITA-BLOCK-1995]`.
  3. Jacob: firma sobre la posición declarada en §7.1.1 (alineamiento con Block, ruptura parcial con Dennett, costo asumido).
- **No se editó** `Tesis.md` ni `metrics.json`.
