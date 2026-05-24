# Histórico — Drenaje de menciones H-J*/H-S*/H-U* decorativas (2026-05-24)

Auditoría: 40 ocurrencias de tokens `H-J\d+`, `H-S\d+`, `H-U\d+` distribuidas en 18 líneas del cuerpo del manuscrito (excluyendo `historico-*`, `TAREAS_PENDIENTES.md`).

Política aplicada:
- **CONSERVAR**: menciones en secciones "Deuda residual" como código tipo `H-S1 director` (legítimas crossrefs a TAREAS_PENDIENTES.md).
- **ELIMINAR**: blockquotes BORRADOR-IA infraestructurales con marcador H-J\* (otro agente paralelo está atendiendo blockquotes; aquí drenamos el token decorativo).
- **ELIMINAR**: frontmatter `parte_de: H-J8` en `_extendido/rival-*.md`.
- **ELIMINAR**: `(BORRADOR-IA, requires: H-Jx)` / `(BORRADOR-IA pendiente firma H-Jx)` / `(H-Jx)` parentéticos decorativos en cuerpo argumental.
- **ELIMINAR**: referencias `[PENDIENTE: plantilla institucional H-U2]` en slides y storyboard (la legítima vive en `06-01 §Deuda residual`).

Backup de cada hit (línea original previa al edit) abajo.

## Hits eliminados (decorativos)

### Blockquotes BORRADOR-IA infraestructurales con marcador H-J8 (4 hits)

1. `00-proyecto/03-plan-de-capitulos.md:3` — stub redirect mencionando "marcador BORRADOR-IA H-J8 vivo en 00-proyecto/01-estructura-y-plan.md".
2. `00-proyecto/01-estructura-y-plan.md:3` — blockquote "BORRADOR-IA — pendiente firma H-J8" (fusión D.4).
3. `04-debates/01-debates-con-posiciones-rivales.md:3` — blockquote "BORRADOR-IA — pendiente firma H-J8" (consolidación D.2).
4. `04-debates/02-limitaciones-y-puntos-de-presion.md:3` — blockquote "BORRADOR-IA — pendiente firma H-J8" (reducción D.3).

### Frontmatter `parte_de: H-J8` (7 hits)

5. `04-debates/_extendido/rival-mecanicismo-multinivel.md:5`
6. `04-debates/_extendido/rival-modelos-internos.md:5`
7. `04-debates/_extendido/rival-conductismo-radical.md:5`
8. `04-debates/_extendido/rival-enactivismo-radical.md:5`
9. `04-debates/_extendido/rival-realismo-estructural-informativo.md:5`
10. `04-debates/_extendido/rival-wolfram-physics-project.md:5`
11. `04-debates/_extendido/rival-cognitivismo-computacional.md:5`

### Paréntesis decorativos en cuerpo argumental (5 hits)

12. `03-formalizacion/01-aparato-formal.md:220` — `(BORRADOR-IA, requires: H-J3 — verificación final de equivalencia operador↔variable Fajen-Warren a cargo de Jacob)`.
13. `03-formalizacion/01-aparato-formal.md:266` — `(Marcador BORRADOR-IA / H-J10 vivo en 03-formalizacion/03-auditoria-ontologica-y-diseno-de-investigacion.md §10.5: misma decisión autoral sobre reclasificación de L&R como rival eliminativista y nuance p.131/p.191; aquí se aplica la misma opción conservadora — se mantiene la concesión de Rainforest Realism para evitar acusación de strawman.)`.
14. `03-formalizacion/03-auditoria-ontologica-y-diseno-de-investigacion.md:250` — `(BORRADOR-IA, requires: H-J10 — firma autoral pendiente sobre reclasificación de L&R como rival eliminativista; decisión pendiente sobre nuance p.131/p.191: opción conservadora aplicada — se mantiene la concesión de Rainforest Realism para evitar acusación de strawman.)`.
15. `04-debates/04-anticipacion-objeciones-filosoficas.md:57` — `*(BORRADOR-IA pendiente firma H-J6.)*` y al final `(H-J4)` en línea 319.
16. `04-debates/04-anticipacion-objeciones-filosoficas.md:319` — `*(BORRADOR-IA pendiente firma H-J4.)*` y `(H-J4)` parentético al cierre.

### Slides/storyboard decorativos H-U2 (5 hits)

17. `06-cierre/_extendido/slides/defensa-5min.md:18` — `[PENDIENTE: plantilla institucional H-U2]`.
18. `06-cierre/_extendido/slides/defensa-15min.md:19` — `[PENDIENTE: plantilla institucional H-U2]`.
19. `06-cierre/_extendido/slides/defensa-30min.md:18` — `[PENDIENTE: plantilla institucional H-U2 — logo, tipografía oficial]`.
20. `06-cierre/_extendido/storyboard-defensa.md:8` — frase "voz visual final es de Jacob + plantilla institucional H-U2 (pendiente)".
21. `06-cierre/_extendido/storyboard-defensa.md:42` — `[PENDIENTE: plantilla institucional H-U2 — logo, tipografía oficial.]`.
22. `06-cierre/_extendido/storyboard-defensa.md:261` — "Voz visual y redacción narrativa pendientes de Jacob + plantilla institucional H-U2".

## Hits conservados (legítimos — secciones "Deuda residual")

- `06-cierre/01-conclusion-demostrativa.md:170-172` — códigos H-U1, H-U2, H-S1/H-S2 declarados en sección "Deuda residual / bloqueadores procedimentales" como código tipo `H-S1 director`.
- `04-debates/03-tabla-comparativa-rivales.md:261` — F04-10 en sección Deuda mencionando "árbitro H-S1/H-S2".
- `04-debates/01-debates-con-posiciones-rivales.md:146` — F04-10 paralela en sección Deuda mencionando "árbitro humano externo (H-S1 director, H-S2 jurado)".

Total esperado tras drenaje: 5 tokens distribuidos en 4 líneas (H-U1, H-U2, H-S1, H-S2 — todos crossrefs legítimos a TAREAS_PENDIENTES.md).
