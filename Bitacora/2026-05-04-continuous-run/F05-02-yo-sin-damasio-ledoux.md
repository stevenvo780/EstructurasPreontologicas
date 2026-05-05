# F05-02 — Caso `yo` (§3 de 05-aplicaciones/01) sin engagement con Damasio / LeDoux / Botvinick-Tsakiris

Fecha: 2026-05-04
Estado: **needs_human** (decisión de Jacob: fetch biblio + reescritura, o restringir alcance de §3)

## (a) Verificación de la afirmación

`05-aplicaciones/01-mente-memoria-yo.md:114-156` desarrolla la categoría `yo` como
"atractor dinámico de integración multivariable con cuenca persistente" con dimensiones
de integración corporal, narrativa, social, afectiva y temporal (líneas 122-131), y
menciona explícitamente la *rubber hand illusion* (línea 152) como prueba clínica del
criterio de elevación. Sin embargo:

1. **Ninguna fuente neurocientífica primaria sobre el yo es citada en §3** (3.1-3.7,
   líneas 114-156). No aparece Damasio (proto-self / core-self / autobiographical
   self, *The Feeling of What Happens*, 1999), ni LeDoux (*Synaptic Self*, 2002), ni
   Botvinick & Cohen (1998, *Nature* 391:756, paradigma RHI original), ni Tsakiris
   (multisensoriedad y propiedad corporal).
2. La taxonomía de dimensiones del §3.2 (corporal / narrativa / social / afectiva /
   temporal) **es estructuralmente paralela** a la tripartición de Damasio
   (proto/core/autobiographical) y a la distinción de LeDoux entre yo implícito
   (sináptico) y explícito, pero el manuscrito **no declara la deuda**, no compara, y
   no discrimina la "cuenca de atractor" frente a esas taxonomías neurales ya
   establecidas. Esto es precisamente F6 según CLAUDE.md §5: invocar el dominio
   (yo, RHI, esquema corporal) sin engagement con quienes lo formularon.
3. **Verificación bibliográfica local** (`ls 07-bibliografia/ | grep -iE
   "damasio|ledoux|botvinick|tsakiris|gallagher|metzinger"`): cero resultados. Las
   fuentes primarias no están en el repo. Por CLAUDE.md §5 ("si no puedes acceder a
   la fuente, no cites el autor"), no puedo redactar §3.5 con paginación verificada
   desde la asistencia.

## (b) Propuesta de edición — needs_human

Dos rutas posibles, ambas requieren firma de Jacob:

**Ruta A — fetch + reescritura (preferida si el yo se quiere defender como caso
fuerte).** Encolar tarea `B-T-FETCH-DAMASIO-LEDOUX-RHI` para `@bibliography-fetcher`:

- Damasio, A. (1999) *The Feeling of What Happens*, Harcourt — proto-self (cap. 5,
  pp. 153-167 aprox.), core-self (cap. 6), autobiographical self (cap. 7, pp.
  195-233 aprox.). Paginación a verificar contra edición.
- LeDoux, J. (2002) *Synaptic Self*, Viking — distinción yo implícito/explícito,
  cap. 1 y cap. 2 aprox.
- Botvinick, M. & Cohen, J. (1998) "Rubber hands feel touch that eyes see",
  *Nature* 391:756 (1 página, paradigma original).
- Tsakiris, M. (2010) "My body in the brain: A neurocognitive model of body-
  ownership", *Neuropsychologia* 48:703-712.

Tras fetch, reescribir §3.5 ("Rival principal") y §3.6 ("Criterio de elevación")
mostrando: (i) cómo la cuenca de atractor propuesta **converge** con la
tripartición de Damasio en sus dimensiones corporal-afectiva-narrativa, (ii) cómo
**diverge** al sustituir la jerarquía proto→core→autobiographical por una
estructura de coordinación multi-atractor sin jerarquía estricta, y (iii) qué
predice el modelo dinámico sobre RHI que el modelo de integración multisensorial
de Botvinick-Tsakiris no predique (criterio de discriminación operativo, no
solo terminológico — exigencia de CLAUDE.md §6).

**Ruta B — restricción honesta de alcance.** Si no se va a hacer engagement con
neurociencia del yo en este pase, **declarar deuda explícita** en §3.7 o en
"Deuda residual" del capítulo: "§3 propone el yo como atractor dinámico sin
discriminar contra las taxonomías neurocientíficas establecidas (Damasio 1999,
LeDoux 2002) ni contra los modelos de propiedad corporal (Botvinick-Cohen 1998,
Tsakiris 2010). El §3 queda al nivel de hipótesis programática hasta que ese
engagement se realice." Esto cumple §7 de CLAUDE.md (deuda declarada > deuda
oculta) sin sobrevender el caso `yo`.

## (c) Costo argumentativo declarado

- **Ruta A** eleva el caso `yo` a defendible pero exige ~2-4 h de lectura primaria
  + reescritura por Jacob; el riesgo es que el dossier muestre que la "cuenca de
  atractor" **no añade poder predictivo** sobre Damasio+Tsakiris, en cuyo caso el
  caso `yo` debe rebajarse o retirarse.
- **Ruta B** es honesta y barata pero **debilita §3 a hipótesis programática**;
  el §3.7 ya admite condicionalidad ("se mantiene como compresión legítima si el
  dossier se construye"), así que el costo retórico es menor de lo que parece.
- **Costo común**: la mención de RHI en §3.6 (línea 152) sin cita de Botvinick-
  Cohen 1998 es, hoy, una cita decorativa F6. Debe corregirse por A o por B.

## Acceptance check

§3.5 actualmente **no incluye** discusión paginada de Damasio/LeDoux ni de
Botvinick/Tsakiris. Acceptance **NO satisfecha**. La asistencia no puede
satisfacerla unilateralmente: requiere (i) fetch externo de fuentes ausentes en
`07-bibliografia/`, (ii) decisión de Jacob entre Ruta A y Ruta B.

Marcar como `needs_human` y encolar dependencia `B-T-FETCH-DAMASIO-LEDOUX-RHI`
si Jacob elige Ruta A.
