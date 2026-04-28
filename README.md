# Tesis doctoral: Monismo material-relacional con compresión multiescala

## Qué es este repositorio

Este repositorio contiene un proyecto de tesis doctoral cuya idea central puede expresarse en una línea:

> Todo fenómeno empíricamente explicable está anclado en un sustrato material dinámico; las entidades, niveles y categorías con que lo pensamos son patrones relacionales estabilizados — atractores empíricamente identificables de sistemas dinámicos acoplados — que se admiten en el marco solo bajo dossier de anclaje completo y traducibilidad verificable entre registros de descripción.

El manuscrito-fuente original (`tesis.md`) presenta esta idea en forma extensa. El resto del repositorio convierte la idea en arquitectura doctoral defendible: diagnóstico estructural, fundamentos, formalización, debates con rivales, aplicaciones (caso ancla canónico + cuatro dominios programáticos), cierre demostrativo, guía de defensa, hoja de ruta.

## Régimen de validez declarado

La tesis está **demostrada** en su caso ancla canónico — la dinámica conductual de la percepción y la acción (Warren 2006) — con dossier de anclaje completo, predicciones cumplidas con varianza explicada superior al 97%, y discriminación pública contra modelos internos y otras posiciones rivales. La tesis está **articulada como programa** en cuatro dominios adicionales (mente, biología, sistemas técnicos, instituciones) con criterios explícitos de elevación a modo demostrativo. La asimetría se nombra como hoja de ruta, no se disimula.

## Estructura del repositorio

```
.
├── tesis.md                          ← manuscrito-fuente
├── README.md                         ← este archivo
├── 00-proyecto/                      ← arquitectura, preguntas, plan de capítulos
├── 01-diagnostico/                   ← falencias, objeciones, sesiones (subcarpeta)
├── 02-fundamentos/                   ← ontología, epistemología, categorías, nivel B
├── 03-formalizacion/                 ← aparato, criterios, auditoría, κ empírica
├── 04-debates/                       ← rivales, limitaciones
├── 05-aplicaciones/                  ← criterios, programáticas, caso ancla canónico
├── 06-cierre/                        ← conclusión demostrativa, defensa, hoja de ruta
├── 07-bibliografia/                  ← corpus PDF y mapa de interlocutores
├── 08-consistencia-st/               ← capa ST de validación lógica
└── Tareas/                           ← backlog duro y mega-tareas
```

## Orden recomendado de lectura

### Para evaluador o lector externo

1. `00-proyecto/01-estructura-general.md` (mapa del proyecto);
2. `00-proyecto/02-preguntas-objetivos-hipotesis.md` (qué se pregunta y qué se responde);
3. `01-diagnostico/01-falencias-de-la-tesis.md` (problema a resolver);
4. `02-fundamentos/01-ontologia-material-relacional.md` (qué existe);
5. `02-fundamentos/04-anclaje-conductual-ecologico.md` (nivel B y asimetría L1↔B↔L3↔S);
6. `03-formalizacion/01-aparato-formal.md` (con qué herramientas se opera);
7. `03-formalizacion/02-criterios-de-legitimidad-y-metodo.md` (filtro de admisión: dossier de anclaje);
8. `04-debates/01-debates-con-posiciones-rivales.md` (discriminación pública contra rivales);
9. `05-aplicaciones/00-criterios-de-admision.md` (modo demostrativo vs programático);
10. `05-aplicaciones/05-dinamica-conductual-reconstruccion-warren.md` (caso ancla canónico, demostrativo);
11. `06-cierre/01-conclusion-demostrativa.md` (la tesis demostrada y sus condiciones de fracaso);
12. `06-cierre/02-guia-de-defensa.md` (la tesis defendible oralmente).

### Para autor o continuador del proyecto

Igual que arriba, más:

13. `01-diagnostico/02-objeciones-y-riesgos.md`;
14. `02-fundamentos/02-epistemologia-de-la-compresion.md`;
15. `02-fundamentos/03-categorias-objetos-propiedades-e-identidad.md`;
16. `03-formalizacion/03-auditoria-ontologica-y-diseno-de-investigacion.md`;
17. `03-formalizacion/04-operacionalizacion-de-kappa.md`;
18. `04-debates/02-limitaciones-y-puntos-de-presion.md`;
19. `05-aplicaciones/01-mente-memoria-yo.md` (programático);
20. `05-aplicaciones/02-biologia-y-ecologia.md` (programático);
21. `05-aplicaciones/03-sistemas-tecnicos-distribuidos.md` (programático);
22. `05-aplicaciones/04-instituciones-mercado-y-estado.md` (programático);
23. `06-cierre/03-hoja-de-ruta-para-tesis-final.md`;
24. `07-bibliografia/01-bibliografia-orientativa.md`;
25. `08-consistencia-st/README.md`;
26. `Tareas/README.md`.

## Qué resuelve cada carpeta

### `00-proyecto`

Define la lógica global del trabajo: arquitectura del manuscrito doctoral, preguntas centrales y secundarias, hipótesis (H1 a H7), objetivos, plan de capítulos.

### `01-diagnostico`

Identifica las falencias estructurales del manuscrito-fuente y las objeciones discriminantes que cualquier evaluación seria planteará. La subcarpeta `sesiones/` conserva la trazabilidad histórica de las correcciones.

### `02-fundamentos`

Desarrolla el núcleo duro: ontología material-relacional con definición técnica de patrón estabilizado, epistemología de la compresión multiescala, reformulación operativa de categorías-objetos-propiedades-identidad, y nivel B (conductual-biológico) con asimetría L1↔B↔L3↔S.

### `03-formalizacion`

Traduce la tesis a aparato operativo: cinco operadores (μ, G, H, κ, ε), pregunta paramétrica Q, diez criterios de legitimidad, dossier de anclaje de catorce componentes, protocolo de auditoría ontológica de nueve fases, procedimiento empírico de κ vía baja dimensionalidad efectiva.

### `04-debates`

Sitúa la propuesta frente a catorce posiciones rivales identificables (filosóficas y empíricas) con tabla de discriminación pública, y reconoce las seis limitaciones genuinas que sobreviven a las correcciones.

### `05-aplicaciones`

Distingue modo demostrativo de modo programático. Contiene el caso ancla canónico (behavioral dynamics, modo demostrativo) y cuatro aplicaciones programáticas (mente, biología, sistemas técnicos, instituciones) con criterios de elevación.

### `06-cierre`

Reúne la conclusión demostrativa con condiciones de fracaso falsables, la guía de defensa oral en tres tiempos (2, 5, 15 minutos), y la hoja de ruta para tesis final con cronograma agregado.

### `07-bibliografia`

Mapa de interlocutores funcionales por capítulo y corpus PDF. Su conversión en bibliografía formal con citas rigurosas es uno de los pasos de la hoja de ruta.

### `08-consistencia-st`

Capa local de validación lógica con `@stevenvo780/st-lang`: formalizaciones mínimas del núcleo argumental con comprobación automática de no-contradicción y trazabilidad textual hacia archivos del repositorio.

### `Tareas`

Backlog duro: crítica radical pre-corrección, pasos no negociables, mega-tareas estratégicas (programa científico general, traducción de obras, operacionalización-validación, benchmark rivales, corpus ST), tareas documentales delegables.

## Estado del manuscrito

**Lo consolidado** (verificable en cada capítulo):

- diagnóstico estructural cerrado;
- ontología material-relacional con definición técnica de patrón;
- epistemología de la compresión con verdad como preservación estructural;
- nivel B y asimetría L1↔B↔L3↔S;
- aparato formal de cinco operadores con procedimiento empírico de κ;
- diez criterios y dossier de catorce componentes;
- auditoría ontológica como protocolo de nueve fases;
- discriminación pública contra catorce rivales;
- caso ancla canónico (behavioral dynamics) con dossier completo;
- aplicaciones programáticas con criterios de elevación;
- conclusión demostrativa con condiciones de fracaso falsables;
- guía de defensa oral.

**Lo pendiente** (especificado como deuda en capítulo 06-01):

- elevación de al menos un caso programático a demostrativo (prioridad: biología por la accesibilidad de datos sobre regime shifts);
- integración bibliográfica formal con citas rigurosas en cada capítulo;
- desarrollo del aparato para variables normativas;
- redacción unificada en estilo doctoral con anexos operativos;
- lectura externa por evaluadores hostiles.

Cronograma plausible para tesis final: 24-36 meses (capítulo 06-03).

## Idea-fuerza que unifica el repositorio

> La realidad es material, pero su inteligibilidad depende de patrones relacionales — atractores empíricamente identificables de sistemas dinámicos acoplados — que se admiten en el marco solo bajo dossier de anclaje completo y traducibilidad verificable entre registros de descripción.

## Diferencia respecto al borrador original

El manuscrito-fuente tiene una intuición filosófica fuerte. El proyecto la disciplina mediante seis correcciones estructurales identificadas tras la respuesta del profesor que motivó la pregunta original (capítulo 01-01):

1. caso ancla canónico (Warren 2006) en lugar de generalidad sin demostración;
2. patrón estabilizado definido técnicamente como atractor empírico con cinco condiciones;
3. aparato formal con protocolo empírico de κ vía baja dimensionalidad;
4. nivel B (conductual-biológico) en lugar de L2 neurobiológico estrecho;
5. condiciones de fracaso global falsables;
6. bibliografía integrada por capítulo con interlocutor principal y secundarios.

Estas correcciones convierten el manifiesto sofisticado en programa de investigación auditable.

## Cómo citar

Borrador en proceso. Hasta cierre de tesis final, citar como:

> [Autor]. *Monismo material-relacional con compresión multiescala*. Manuscrito doctoral en preparación, [año].

## Licencia

[Por especificar según política institucional]
