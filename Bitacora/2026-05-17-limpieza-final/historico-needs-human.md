# Histórico: menciones `needs_human` eliminadas del cuerpo manuscrito

**Fecha:** 2026-05-24
**Alcance:** capítulos 00-06 (excluye `_extendido/historico-*` y subcarpetas históricas)
**Razón:** `needs_human` es jerga del orquestador interno Claude Code, no terminología académica reconocida. Se elimina del cuerpo del manuscrito conservando la información sustantiva (qué decisión humana falta).

## Hits originales (10)

### 02-fundamentos/05-temporalidad-y-causalidad.md:156
```
- **[F02-12 2026-05-11]** §2.4.4 (línea 116) usa la expresión "modus tollens vacuo" para describir la refutación a Kim 2005 sobre causación mental. Hallazgo: "modus tollens vacuo" no es un término técnico estándar; la teoría ST T13 verifica vacuidad lógica, no fuerza filosófica. Kim 2005 anticipa la maniobra "constitución, no causación" en *Physicalism, or Something Near Enough* pp.39-42; PDF ausente en `07-bibliografia/`. Acción: reescribir §2.4.4 invocando manipulabilidad woodwardiana (presente local) sin declarar "refutación" de Kim, o fetch Kim 2005 antes de paginar. `needs_human` para corte filosófico.
```

### 02-fundamentos/04-anclaje-conductual-ecologico.md:260
```
- **[F02-11 2026-05-11]** §50-67 invoca a Bateson (cibernética) y Dretske (información shannoniana) como combinables bajo la noción ecológica de información. Hallazgo: Bateson cibernético ("the difference that makes a difference") y Dretske semántico-shannoniano son incompatibles en su tratamiento de la intencionalidad; "combina" es engañoso. PDFs Bateson 1972 y Dretske 1981 ausentes en `07-bibliografia/`. Acción: declarar subordinación bajo Gibson (información ecológica como variable estructural del entorno) y fetch Bateson/Dretske antes de cita paginada. `needs_human` para corte filosófico.
```

### 03-formalizacion/02-criterios-de-legitimidad-y-metodo.md:251
```
- **[F03-03 2026-05-11]** §82 y §98-129 describen la matriz dossier con valoraciones 0/1/2 sin definir qué cuenta como "contenido sustantivo" para asignar cada nivel; el caso ancla Warren obtiene 20/20 por construcción del propio capítulo 05-05. Acción: añadir rúbrica explícita por criterio (umbrales operativos para 0, 1, 2) en el cuerpo del capítulo; DRAFT de rúbrica pendiente de migrar al cuerpo del capítulo. `needs_human` para validar umbrales.
```

### 03-formalizacion/03-auditoria-ontologica-y-diseno-de-investigacion.md:266
```
- **[F03-11 2026-05-11]** §6 (línea 6) afirma "criterio de cierre es replicabilidad por tercero", pero **ninguna replicación externa ha sido ejecutada** sobre el corpus EDI: el manuscrito no tiene evidencia de tercero independiente reproduciendo los resultados desde `case_config.json` + datos. Esto choca con la objeción de Collins ("experimenter's regress"). Acción: degradar "replicabilidad" de hecho consumado a reclamo operativo (CLAUDE.md §10 — promesa pública defendible, no afirmación retórica); abrir entrada `H-J##` en `TAREAS_PENDIENTES.md` para invitar replicación independiente con plazo declarado. `needs_human` para apertura formal de la invitación.
```

### 04-debates/03-tabla-comparativa-rivales.md:259
```
- **[F04-01 2026-05-11]** Fila 1 de la tabla (Dualismo de propiedades, línea 34) marca "✗" en la columna A (sustrato físico). El dualismo de propiedades **naturalista** (Chalmers 1996, *The Conscious Mind*, cap. 4 «Naturalistic Dualism»; PDF no disponible localmente, referencia secundaria pendiente de verificación) acepta sustrato físico; el "✗" es hombre de paja contra esa versión. Acción: dividir fila 1 en 1a (naturalista, A=✓) y 1b (anti-naturalista, A=✗); fetch Chalmers 1996 *The Conscious Mind*. `needs_human` para validar división filosófica. Paralela en `04-debates/01-debates-con-posiciones-rivales.md` §2.
```

### 04-debates/01-debates-con-posiciones-rivales.md:144
```
- **[F04-01 2026-05-11]** El tratamiento del dualismo como posición monolítica en la matriz canónica de `04-debates/03 §1` no distingue el dualismo de propiedades **naturalista** de Chalmers 1996 (*The Conscious Mind*), que acepta sustrato físico, del dualismo de propiedades **anti-naturalista**. Hallazgo: la valoración "✗" en la columna A (sustrato físico) es hombre de paja contra la versión naturalista; sólo aplica a la versión anti-naturalista. PDF *The Conscious Mind* ausente en `07-bibliografia/`. Acción: dividir la fila 1 de la tabla en 1a (naturalista) y 1b (anti-naturalista) con valoraciones distintas en A; fetch Chalmers 1996. `needs_human` para validar la división filosófica.
```

### 04-debates/01-debates-con-posiciones-rivales.md:146
```
- **[F04-10 2026-05-11]** El "Compromiso público" alojado en `04-debates/03-tabla-comparativa-rivales.md` declara compromisos epistémicos sin árbitro externo: el manuscrito mismo evalúa si los compromisos se cumplen. Esto es auto-arbitraje. Acción: añadir cláusula de árbitro humano externo (H-S1 director, H-S2 jurado) para la evaluación post-defensa de los compromisos, o declarar explícitamente la limitación (auto-arbitraje preserva trazabilidad pero no objetividad inter-subjetiva). `needs_human` para designar árbitros. Paralela en `04-debates/03-tabla-comparativa-rivales.md` §222-224.
```

### 02-fundamentos/01-ontologia-material-relacional.md:403
```
- **[F02-09 2026-05-11]** §1.3 importa el ontology CESM bungeano sin disociar el M-mecanismo (materialismo) del esqueleto C+E. Los volúmenes 3 y 4 del *Treatise on Basic Philosophy* de Bunge NO están en `07-bibliografia/`; la adopción del CESM debe declararse como restringida a Composición y Entorno, con costo: la tesis no compra el materialismo bungeano íntegro. Acción: añadir declaración explícita de adopción restringida + fetch Bunge vol.3/4 antes de citar paginación. `needs_human` para validación filosófica.
```

### 02-fundamentos/01-ontologia-material-relacional.md:404
```
- **[F02-13 2026-05-11]** §13 (caso 31 decoherencia cuántica) opera con decoherencia + einselection y declara neutralidad entre interpretaciones realistas. Hallazgo del triage: decoherencia + einselection compromete *en uso* con la familia Everett-Wallace (no es neutra entre Bohm-DeBroglie, GRW, Everett). Wallace 2012 *The Emergent Multiverse* NO está en `07-bibliografia/`. Acción: reescribir §13 declarando compromiso interpretativo efectivo o fetch de Wallace 2012 antes de paginar la cita. `needs_human` para corte filosófico.
```

### 06-cierre/_extendido/respuestas-tipo-defensa.md:39 y :94
```
> **Deuda residual [F04-04 2026-05-11]:** la formulación "modus tollens vacuo" es manierismo no técnico; Kim 2005 en *Physicalism, or Something Near Enough* anticipa explícitamente la maniobra "constitución, no causación". PDF Kim 2005 ausente en `07-bibliografia/`. Acción pendiente: reescribir invocando manipulabilidad woodwardiana (Woodward 2003 presente local) sin pretender "refutación" de Kim, o fetch Kim 2005 antes de paginar el engagement. `needs_human` para corte filosófico.
```
```
- **[F04-08 2026-05-11]** La respuesta sobre eliminativismo (Trampa 4 en `06-cierre/02-guia-de-defensa.md §4`) responde a "eliminar de más" sin responder a la objeción complementaria "eliminar **de menos**": los casos null del corpus podrían exigir eliminación regional de la categoría asociada (si la sonda no detecta cierre operativo, ¿por qué se preserva el término?). Acción: añadir sub-respuesta articulando la doble exigencia (no eliminar de más, no preservar de más). `needs_human` para corte filosófico sobre umbral de eliminación regional.
```

## Estrategia de sustitución

Todas las menciones aparecen al final de una entrada de "Deuda residual" como flag interno indicando qué decisión humana falta. Se eliminan eliminando la frase final ``` `needs_human` para … ``` y conservando el resto del análisis. La información sustantiva ("corte filosófico", "validación de umbrales", "designación de árbitros", etc.) ya está implícita en el texto previo: las entradas describen acciones pendientes que, por naturaleza, requieren juicio humano del autor (Jacob).

Cuando la frase eliminada contiene información no redundante (e.g. "para corte filosófico sobre umbral de eliminación regional"), esa información se integra al cuerpo de la entrada o se reformula como decisión pendiente sin la etiqueta `needs_human`.
