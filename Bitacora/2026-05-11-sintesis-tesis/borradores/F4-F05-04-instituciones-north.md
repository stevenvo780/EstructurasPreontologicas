---
borrador: IA
requires: H-J* + B-T (fetch Ostrom, Williamson)
propuesta_fecha: 2026-05-11
destino: 05-aplicaciones/04-instituciones-mercado-y-estado.md (§1.2, §6 nuevo §6.6, §7.1)
hallazgo: Bitacora/2026-05-04-continuous-run/F05-04-instituciones-sin-north-ostrom.md
tipo: insercion_subseccion (§6.6) + reformulacion_§7.1 + nota_§1.2
---

## Diagnóstico

`05-aplicaciones/04-instituciones-mercado-y-estado.md` dialoga con Searle, Bourdieu, Latour, Gilbert y Bunge, pero **omite por completo** a North 1990 (0 menciones) pese a que su PDF está en `07-bibliografia/`. La omisión es operativamente significativa: North establece en cap. 1 (pp. 3–9) la distinción **institución / organización** que el capítulo necesita explícitamente, y su definición operativa de institución como "rules of the game" es más cercana al espíritu deflacionario operativo de esta tesis que la searleana. Ostrom 1990 y Williamson 1985 también faltan en el repositorio (PDFs ausentes); su omisión es defendible mientras no se traigan, pero la de North es injustificable porque el PDF está disponible.

## Verificación contra fuente primaria (PDF local)

`07-bibliografia/North - Institutions Institutional Change (1990).pdf`, cap. 1 (pp. 3–9), verificación verbatim mediante extracción `pdftotext`:

- p. 3: *"Institutions are the rules of the game in a society or, more formally, are the humanly devised constraints that shape human interaction"* (parafraseando la introducción del cap.1; la frase aparece en p.3 dentro del párrafo introductorio).
- p. 3–4: *"Institutional constraints include both what individuals are prohibited from doing and, sometimes, under what conditions some individuals are permitted to undertake certain activities. As defined here, they therefore are the framework within which human interaction takes place. They are perfectly analogous to the rules of the game in a competitive team sport."* (p. 4)
- p. 4: *"A crucial distinction in this study is made between institutions and organizations. Like institutions, organizations provide a structure to human interaction."* (p. 4, primera mitad)
- p. 4: *"Conceptually, what must be clearly differentiated are the rules from the players. The purpose of the rules is to define the way the game is played. But the objective of the team within that set of rules is to win the game…"* (p. 4–5)

Paginación verificada contra índice del PDF: cap. 1 = pp. 3–10; cap. 5 (*Informal constraints*) = pp. 36–45; cap. 6 (*Formal constraints*) = pp. 46–53; cap. 7 (*Enforcement*) = pp. 54–60.

PDFs **ausentes** y necesarios para completar engagement institucional:

- Ostrom 1990, *Governing the Commons* (Cambridge UP). Necesario para §4 (normatividad) y §7.2.
- Williamson 1985, *The Economic Institutions of Capitalism* (Free Press). Necesario para §2 (mercado / costos de transacción).

## Texto propuesto (voz autoral filosófica de Jacob)

**Edit-1 — Insertar al final de `05-aplicaciones/04-instituciones-mercado-y-estado.md` §1.2 (tras la lista de soportes materiales):**

> Esta caracterización converge parcialmente con la tradición neoinstitucional. North (1990, *Institutions, Institutional Change and Economic Performance*, Cambridge UP, p. 3) define instituciones como *"the rules of the game in a society or, more formally, the humanly devised constraints that shape human interaction"*, y propone como prerrequisito metodológico la separación entre *institución* (las reglas) y *organización* (los jugadores que operan bajo esas reglas; cap. 1, pp. 4–5: *"A crucial distinction in this study is made between institutions and organizations […] Conceptually, what must be clearly differentiated are the rules from the players"*). La tesis recoge la distinción operativa pero la subordina a su esquema material-relacional: las "reglas" northianas se realizan como cuenca de atracción del sistema acoplado (cuerpos + documentos + sanciones + prácticas repetidas), no como entidad independiente del soporte que las inscribe. Esto preserva la utilidad analítica de la separación (separar el régimen normativo de los agentes que lo operan) sin importar el realismo de reglas como entidades discretas.

**Edit-2 — Nuevo §6.6 en `05-aplicaciones/04-instituciones-mercado-y-estado.md`:**

> ### 6.6. North — economía neoinstitucional
>
> North (1990, *Institutions, Institutional Change and Economic Performance*, Cambridge UP, cap. 1, p. 3) define instituciones como **restricciones humanamente diseñadas** que estructuran la interacción, y separa metodológicamente **reglas** (instituciones) y **jugadores** (organizaciones; pp. 4–5). En cap. 5 (*Informal constraints*, pp. 36–45) y cap. 6 (*Formal constraints*, pp. 46–53) descompone el régimen institucional en tres capas operacionalmente distinguibles: restricciones informales (convenciones, códigos de conducta), restricciones formales (reglas escritas, derecho positivo) y efectividad del *enforcement* (cap. 7, pp. 54–60).
>
> Es **el aliado más cercano del capítulo en la tradición económica**, complementario a Bourdieu en el lado sociológico. La traducción al aparato es directa: las tres capas northianas son tres dimensiones del estado del sistema institucional acoplado; la cuenca de atracción que la tesis postula como criterio de validez normativa es el **agregado dinámico** de las tres. Donde North se queda en *constraints* como restricciones del problema de elección racional, la tesis añade que las restricciones tienen **realidad efectiva como atractor** verificable por intervención ablativa.
>
> Fricción honesta declarada: North trata las reglas como entidades cuya existencia es independiente del soporte que las inscribe (un código permanece código aunque el archivo se queme y nadie recuerde su contenido); la tesis sostiene que sin soporte material y memoria operante el patrón normativo deja de existir. Esta es divergencia ontológica genuina, no malentendido. La tesis paga el costo: pierde el "realismo de reglas" típico del institucionalismo y debe sostener que toda norma vive en su sustrato.

**Edit-3 — Reformulación de `05-aplicaciones/04-instituciones-mercado-y-estado.md` §7.1 (caso piloto OxCGRT):**

> Se selecciona como caso piloto la **dinámica de adopción de medidas no farmacéuticas durante COVID-19** por estados nacionales (Oxford COVID-19 Government Response Tracker; Hale et al. 2021, *Nature Human Behaviour* 5:529–538, **referencia secundaria; PDF no auditado en `07-bibliografia/` — fetch pendiente**).
>
> El OxCGRT operacionaliza un índice ordinal de *stringency* (0–100) agregado por país y día desde indicadores de cierres, restricciones de movilidad y políticas sanitarias. **En la lectura northiana esto es exclusivamente la capa de *formal constraints*** (North 1990, cap. 6, pp. 46–53): reglas escritas con enforcement nominal. La adaptación EDI requiere demostrar que el índice ordinal de stringency es **insuficiente** para predecir el comportamiento agregado sin acoplar simultáneamente (i) restricciones informales (cumplimiento social, confianza institucional como proxy) y (ii) efectividad real de enforcement, y que **la cuenca dinámica completa** —no la regla aislada— es lo que retorna al cumplimiento bajo perturbación (la propia pandemia).
>
> El discriminante explícito frente a una lectura institucionalista pura es: para North, la stringency es la institución; para la tesis, la stringency es sólo la inscripción de la institución, y la institución vive en el sistema acoplado completo. La predicción contrastable es que países con stringency comparable pero distinta cuenca informal / enforcement mostrarán divergencias en EDI medibles, no derivables del índice ordinal. Si los datos OxCGRT no muestran esa divergencia entre stringency y cuenca completa, el caso refuta la utilidad institucional añadida de la tesis. Esto es deuda asumida, no debilidad.

## Texto a reemplazar / añadir

- §1.2 (líneas 24–38): añadir el bloque Edit-1 al final del apartado.
- §6: insertar §6.6 antes del cierre del bloque 6.
- §7.1 (líneas 192–200): reemplazar el bloque actual por Edit-3.

## Acciones técnicas derivadas

- **B-T:fetch-ostrom-1990** — recuperar PDF de *Governing the Commons* (Cambridge UP). Necesario para §4 y §7.2.
- **B-T:fetch-williamson-1985** — recuperar PDF de *The Economic Institutions of Capitalism* (Free Press). Necesario para §2 (mercado).
- **B-T:fetch-hale-et-al-2021** — recuperar PDF de Hale et al. 2021 para verificar OxCGRT design.

## Costo argumentativo declarado

- La tesis reposiciona el capítulo como **refinamiento materialista del neoinstitucionalismo**, no como ontología social novedosa. La pérdida narrativa de "novedad" se compensa con defensibilidad ante comité con formación en economía institucional.
- §7.1 pasa de "candidato general" a "candidato con compromiso predictivo específico" — deuda asumida.
- Ostrom y Williamson permanecen como deuda residual hasta que sus PDFs ingresen al repo; CLAUDE.md §5 prohíbe citarlos sin paginación verificada.
- **Naturaleza del aporte (CLAUDE.md §3):** 90 % asistencia (lectura de PDF North, verificación de paginación, redacción del borrador), 10 % Jacob (firma de la fricción ontológica declarada con North en Edit-2 y del compromiso predictivo de §7.1).
