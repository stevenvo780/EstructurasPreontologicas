# F05-05 — Sondas ecológicas (LV, von Thünen) sin justificación frente a May 1973 y Levin 1992

**Fecha:** 2026-05-04
**Tipo:** auditoría adversarial cap 05
**Estado:** `needs_human` (requiere firma de Jacob — decisión filosófica/metodológica + biblio externa)

## (a) Verificación de la afirmación adversarial

Hallazgo del adversarial-reviewer: el cap 05 usa **Lotka-Volterra como sonda ODE para el caso 04 (energía eléctrica)** y **von Thünen para el caso 16 (deforestación)** sin discutir las objeciones canónicas a estas familias.

Verificación textual:

- `05-aplicaciones/07-mapa-aplicaciones-corpus.md:69-71` (Tabla 5.7.3 / A.5.3) lista efectivamente:
  - caso 04 "Energía eléctrica" con sonda **Lotka-Volterra**, EDI=0.6503;
  - caso 16 "Deforestación global" con sonda **von Thünen**, EDI=0.5802.
- `05-aplicaciones/02-biologia-y-ecologia.md:139-168` discute "El ecosistema" en clave general (regime shifts, Scheffer §4.4) pero **no aparece §4.7 "Justificación de sondas"** ni mención a May 1973 (estabilidad LV en sistemas grandes) ni a Levin 1992 (problema de escala). Confirmado: la sección no existe.

La objeción adversarial es legítima:

1. **May (1972/1973)** — *Stability and Complexity in Model Ecosystems* — mostró que en redes aleatorias de N especies con conectancia C y fuerza de interacción α, el equilibrio LV se vuelve **inestable** cuando α·√(NC) > 1. Aplicar LV a "energía eléctrica" (donde "depredador-presa" es metáfora oferta-demanda) requiere defender por qué la dinámica de dos variables LV captura la estructura, dado que el resultado de May sugiere que LV es frágil incluso en su dominio nativo.
2. **Levin (1992)** — *The Problem of Pattern and Scale in Ecology*, Ecology 73(6):1943-1967 — argumentó que ningún modelo ecológico es escala-independiente; el patrón observado depende de la ventana espacio-temporal. von Thünen (1826) es modelo de **renta agrícola estática a escala de hacienda**; aplicarlo a deforestación global (escala continental, dinámica multidecenal) sin discutir el cambio de escala es exactamente lo que Levin advierte.

## (b) Propuesta de edición — `needs_human`

**No edito** porque:

- Defender LV en caso 04 frente a May 1973 requiere posición filosófica (¿es LV aquí *modelo demostrativo* o *sonda mínima de acoplamiento*? La distinción cambia la respuesta).
- Sustituir von Thünen en caso 16 por una sonda con justificación de escala (e.g., Geist-Lambin meta-análisis, modelo de transición forestal Mather) es decisión que **toca la fuente de verdad numérica** (`16_caso_deforestacion/case_config.json` y `outputs/metrics.json`), lo que excede mi rol (CLAUDE.md §4).
- Las dos páginas exactas pedidas en acceptance (May 1973 p.74; Levin 1992 *Ecology* 73:1943) **no están disponibles localmente** en `07-bibliografia/` (verificado: ninguna entrada con "May" o "Levin" en el listado). Citarlas sin el PDF violaría §5 (cita decorativa = F6).

**Acción propuesta para Jacob:**

1. **Añadir §4.7 "Justificación de sondas"** en `05-aplicaciones/02-biologia-y-ecologia.md` con dos sub-secciones:
   - §4.7.1 *LV en caso 04*: declarar explícitamente que LV se usa como **sonda mínima de acoplamiento bidireccional**, no como modelo demostrativo de la dinámica eléctrica; conceder May 1973 (estabilidad sólo en regímenes acotados) como **costo declarado**; argumentar que el EDI mide degradación al apagar el acoplamiento, no realismo del modelo, y por tanto la objeción de May es **ortogonal** al uso evidencial de LV aquí.
   - §4.7.2 *von Thünen en caso 16*: conceder Levin 1992 (no escala-independiente) y declarar que von Thünen se usa como **proxy del gradiente renta-distancia** que sigue siendo empíricamente verificable en datos World Bank a escala país; declarar como deuda residual la sustitución por Geist-Lambin si los datos lo permiten.
2. **Acción técnica complementaria** (B-T*): considerar correr una sonda alternativa en caso 04 (e.g., SIR-económico o difusión de adopción) y reportar si EDI sobrevive — multi-probe-null.
3. **Bibliografía a recuperar** (B-Bib): `/fetch-biblio` para May 1973 y Levin 1992 antes de citar paginadamente.

## (c) Costo argumentativo declarado

- Si se acepta esta justificación, la tesis **concede** que LV y von Thünen no son *modelos correctos* de los dominios respectivos, sólo *sondas mínimas evidenciales*. Esto es coherente con la postura "irrealismo operativo" del marco general, pero **debilita** la lectura realista de las tablas 5.7.3 si el lector las interpreta como "el dominio se rige por LV/von Thünen". La prosa actual no aclara la distinción.
- Si Jacob prefiere defender LV/von Thünen como modelos demostrativos, el costo es responder May/Levin frontalmente con argumento empírico — costo más alto.
- Mantener el texto sin §4.7 deja la tesis vulnerable al hallazgo adversarial: **F6 (cita decorativa) no, pero F-sonda-injustificada sí**.

## Tareas derivadas

- `H-J` Jacob: decidir entre justificación-como-sonda vs defensa-como-modelo y firmar §4.7.
- `B-Bib` asistencia: `/fetch-biblio` May 1973 *Stability and Complexity*; Levin 1992 *Ecology* 73:1943-1967.
- `B-T` (opcional, multi-probe-null): correr sonda alternativa en caso 04 para test de robustez de EDI bajo cambio de sonda.

RESULT: complete | F05-05-sondas-eco-sin-may-levin | needs_human; falta §4.7 y biblio May/Levin
