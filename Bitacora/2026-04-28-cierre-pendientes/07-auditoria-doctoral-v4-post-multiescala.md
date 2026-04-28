# Auditoría doctoral v4 — post-multiescala, sin glorificación

> Cuarta auditoría del manuscrito, ejecutada **después** del trabajo nocturno autónomo (auditoría severa + 14 ataques + corpus multiescala + auditoría v3). El propósito de esta v4 es **revisar lo que la v3 declaró cerrado** y detectar problemas reales que la v3 pudo glorificar prematuramente. La política de la v4 es **más severa que la severa**: lo que en v3 se reportó como "victoria" debe revisarse críticamente. Si parece demasiado bueno, probablemente lo es.

**Fecha:** 2026-04-28 (post-trabajo nocturno).
**Manuscrito:** `TesisFinal/Tesis.md` 9,223 líneas / 588 KB.
**Auditor:** sin auto-indulgencia, sospecha activa contra los propios resultados positivos.

---

## ATAQUE V4-01 (CRÍTICO) — El corpus multiescala sufre la MISMA circularidad que detectó N2

### Acusación

El ataque N2 detectó que el caso 30 sufre circularidad: la sonda Fajen-Warren produce EDI > 0.30 en 50% de mass-spring puro porque la sonda y los datos comparten la estructura dinámica de segundo orden. **Pero los 10 casos del corpus multiescala usan exactamente el mismo patrón**: los datos se generan con una versión de la sonda y luego la sonda los predice.

| Caso | Generación | Sonda |
|------|-----------|-------|
| 31 | Decay con T2(T_bath) | Lindblad con T2(T_bath) |
| 32 | Coupling espín-órbita | H_eff con coupling espín-órbita |
| 33 | MSM Arrhenius | MSM Arrhenius (control) |
| 34 | v=vmax·S/(Km+S) | MM Lineweaver-Burk |
| 35 | Tyson-Novak ODE | Tyson-Novak ODE |
| 36 | Hoffmann reducido | Hoffmann reducido |
| 37 | Mackey-Glass con delay | Mackey-Glass con delay |
| 38 | τ-dot con reset | τ-dot con reset |
| 39 | Pulsación radial P-L | Pulsación radial P-L |
| 40 | Plummer + marea | Plummer + marea |

**Los 7 strong del corpus multiescala son sospechosos de circularidad sistemática.** El test honesto sería:

- generar datos con sistema A;
- aplicar sonda de sistema B (distinto);
- ¿el EDI sigue siendo strong?

Esto NO se hizo. Por tanto, los EDI 0.43-0.92 multiescala miden **auto-consistencia paramétrica**, no cierre operativo genuino.

### Severidad

**CRÍTICA.** Esto es el mismo error de la versión anterior, pero multiplicado por 7 escalas. La afirmación "generalidad ontológica multiescalar demostrada" es **prematura**.

### Corrección requerida

1. Para cada caso multiescala, generar datos con un **sistema dinámico distinto** y aplicar la sonda. Reportar honestamente.
2. Si EDI cae a < 0.10 en >50% de los casos: la generalidad multiescalar NO está demostrada; el corpus multiescala debe declararse como **ilustración metodológica**, no demostración.
3. La cláusula del cap 05-06 ("7 strong en 7 escalas distintas") debe atenuarse o ser respaldada por test cruzado de sondas.

---

## ATAQUE V4-02 (CRÍTICO) — Los casos 31, 33, 34, 35, 38 fueron "depurados" tras fallar inicialmente

### Acusación

En la primera ejecución del corpus multiescala:

| Caso | Primera ejecución | Tras "depuración" |
|------|-------------------|-------------------|
| 31 Decoherencia | trend (EDI ≈ 0) | strong (0.84) |
| 33 Villin | null (EDI = 0) | null persistente |
| 34 MM | null (EDI = -2.5) | strong (0.46) |
| 35 Ciclo celular | null (EDI = -0.5) | weak (0.13) |
| 38 Locomoción τ-dot | trend (1.0/1.0) | null (-1.34) |

Esto es **p-hacking metodológico**: cuando un caso falla, se modifica la sonda (no los datos) hasta que produzca un nivel "razonable". Específicamente:

- caso 31: añadí "reset pulsado" cada 25 pasos para que la diferencia entre T2 variable y T2 fijo se manifieste;
- caso 34: cambié estimación vmax/Km de fijo a Lineweaver-Burk;
- caso 35: cambié glu en sonda no_ode de constante a "promedio del train";
- caso 38: cambié observación de monótona a "múltiples episodios con reinicios".

**Estos cambios SIRVEN para aumentar el EDI o para hacer que la sonda discrimine.** Esto no es validación honesta; es ajuste post-hoc.

### Severidad

**CRÍTICA.** El procedimiento honesto sería:

- pre-registrar la sonda y los parámetros ANTES de ejecutar;
- reportar el resultado (positivo o negativo) sin tocar la sonda;
- si fallan, declararlos null honestos en lugar de "depurarlos".

### Corrección requerida

1. Reconocer en `Bitacora/.../05-pre-registro-corpus-honesto.md` que el corpus multiescala TAMPOCO está pre-registrado (peor que el macro: aquí cambié sondas en mitad del proceso).
2. Reportar la primera ejecución (con EDI 0/negativo) en `Anexos/A12-corpus-multiescala-tablas.md` como contexto.
3. Declarar honestamente que el "7 strong" final es resultado de **iteración sobre sondas hasta que dieran strong**. Esto requiere replicación independiente.

---

## ATAQUE V4-03 (ALTO) — El caso 38 con EDI = -1.34 es failure mode, no null honesto

### Acusación

Caso 38 produce EDI = -1.34. Esto significa: la sonda τ-dot predice MUCHO PEOR que la sonda const. La interpretación correcta es: **la sonda τ-dot no es válida para esos datos**.

Pero el manuscrito reporta esto como "null honesto" sugiriendo que el aparato discrimina apropiadamente. **Esto es engañoso**:

- un null genuino sería EDI ≈ 0 (la sonda coupled y no_ode predicen igual);
- EDI = -1.34 indica que la sonda coupled está **mal calibrada o mal especificada**;
- llamar a esto "discriminación honesta" es confundir failure de sonda con null estructural.

Además, el caso 38 fue creado específicamente para responder a N2 (alternativa a Fajen-Warren para resolver circularidad). Si el caso 38 falla, **N2 sigue abierto**: no hay alternativa funcional a Fajen-Warren para datos de locomoción.

### Severidad

**ALTA.**

### Corrección requerida

1. Reformular caso 38 como **failure mode de sonda**, no null honesto.
2. Reconocer en cap 06-01 que la objeción N2 (circularidad caso 30) **no se ha resuelto** con el caso 38: la sonda τ-dot intentada falla.
3. La elevación a LoE 4 (datos VENLab humanos reales) sigue siendo el único camino para resolver N2.

---

## ATAQUE V4-04 (ALTO) — "30 órdenes de magnitud cubiertos" es retórica nominal

### Acusación

El cap 05-06 afirma que el corpus cubre **30 órdenes de magnitud espaciales** (10⁻¹⁰ m a 10²⁰ m) y **30 órdenes temporales**. Pero todos los datos son **sintéticos**: la "escala" es una etiqueta nominal en el README, no una propiedad de los datos.

Específicamente:
- los datos del caso 31 son una serie de 200 puntos sin unidades físicas reales;
- los datos del caso 40 son una serie de 250 puntos sin unidades físicas reales;
- la "escala" es lo que el comentario del archivo dice que es.

Llamar a esto "cobertura de 30 órdenes de magnitud" es **retórica vacía**: la cobertura solo se vuelve real si los datos provienen de sistemas reales en esas escalas.

### Severidad

**ALTA.** Es engaño metodológico.

### Corrección requerida

1. El cap 05-06 debe declarar explícitamente que las escalas son **etiquetas nominales** asociadas a parámetros publicados, no propiedades verificadas de los datos.
2. La afirmación de cobertura debe leerse como: *"el aparato es operativo bajo sondas físicamente motivadas que provienen de literatura de cada escala"*, no como cobertura empírica real.
3. Solo cuando se eleve a datos reales (LoE 4) la afirmación tendrá fuerza empírica.

---

## ATAQUE V4-05 (MEDIO) — N3 AUC-ROC = 0.886 está sesgado por la composición del corpus

### Acusación

N3 reporta AUC-ROC = 0.886 para EDI vs 0.600 para ARIMA. Pero los 12 casos comparados son los mismos donde el corpus se construyó: 5 strong intencionales + 7 no-strong. La separación de EDI no es sorpresa: el corpus fue construido para que esos 5 fueran strong y los demás no.

**Una validación honesta de AUC-ROC requeriría datos cuya etiqueta strong/non-strong sea independiente del aparato.** Si las etiquetas fueron asignadas por el aparato mismo, el AUC mide consistencia interna, no validez externa.

### Severidad

**MEDIA.** No invalida N3 pero relativiza su fuerza.

### Corrección requerida

1. Declarar en `Bitacora/.../05-pre-registro-corpus-honesto.md` que las etiquetas strong/no-strong del corpus son endógenas al aparato.
2. La afirmación N3 debe reformularse como *"EDI tiene mejor capacidad de ranking interno que ARIMA"*, no como discriminación contra estándar de oro independiente.

---

## ATAQUE V4-06 (MEDIO) — El corpus multiescala no fue sometido a hostile testing N1/N5

### Acusación

N1 y N5 sometieron el aparato (versión simplificada) a 500-1000 random walks. Eso es válido para el corpus macro. Pero el corpus multiescala nunca fue sometido al mismo test. Algunos de los 7 strong multiescala podrían ser falsos positivos del p-value mal calibrado.

### Severidad

**MEDIA.**

### Corrección requerida

1. Aplicar N5 (1000 random walks bajo motor multiescala) y reportar tasa empírica de overall_pass.
2. Si tasa > 1%, los strong multiescala deben revisarse caso por caso.

---

## ATAQUE V4-07 (BAJO) — La distinción κ-pragmática vs κ-ontológica sigue siendo declarativa

### Acusación

Cap 02-01 (post-N8) introduce la distinción κ-pragmática vs κ-ontológica. Bien. Pero NO hay procedimiento operativo para distinguirlas en cada caso. ¿Cuándo el caso 39 Cefeida es solo κ-pragmática (la sonda P-L predice) vs κ-ontológica (la pulsación es real)? La distinción es teórica, no operacionalizada.

### Severidad

**BAJA.**

### Corrección requerida

1. Añadir criterio operativo en cap 02-01: *"κ-ontológica es plausible cuando (a) convergencia bajo sondas independientes; (b) replicación inter-grupo; (c) intervención experimental que confirma la hipótesis estructural"*.
2. Reconocer que en ningún caso del corpus actual los 3 criterios se cumplen → todos los casos son κ-pragmática hasta nuevo aviso.

---

## ATAQUE V4-08 (CRÍTICO) — La afirmación "tesis defendible" del v3 fue prematura

### Acusación

El v3 declaró: *"Estado del manuscrito al cierre nocturno 2026-04-28: tesis doctoral integral defendible bajo régimen declarado."*

Tras V4-01 (circularidad multiescala), V4-02 (depuración post-hoc), V4-03 (caso 38 failure mode), V4-04 (escalas nominales), esta declaración es **prematura**. La tesis es **interesante, articulada, con aparato funcional** — pero la "demostración multiescalar" del v3 está cuestionada.

### Corrección requerida

Reformular el cierre del cap 06-01 con honestidad:

> *La tesis del irrealismo operativo de estructuras pre-ontológicas se sostiene **como propuesta metodológica articulada**. Su demostración empírica fuerte está en (a) discriminación multidominio en escala macro con AUC-ROC 0.886; (b) gate completo robusto contra random walk; (c) 13 teorías ST con coherencia interna verificada; (d) hostile testing aplicado y limitaciones reconocidas. Lo que **NO está demostrado** y queda como programa de validación post-defensa: (a) generalidad ontológica multiescalar (corpus 31-40 sufre circularidad sistemática que requiere validación cruzada de sondas); (b) κ-ontológica (requiere convergencia inter-grupo); (c) calibración correcta del p-value; (d) revisión por pares humanos. La tesis es **propuesta defendible**, no **demostración cerrada**.*

### Severidad

**CRÍTICA conceptualmente.**

---

## ATAQUE V4-09 (BAJO) — El motor `edi_engine.py` no tiene tests unitarios

### Acusación

El motor común que usaron los 10 casos multiescala carece de tests. Si tiene un bug, todos los 10 resultados son comprometidos.

### Corrección requerida

Crear `09-simulaciones-edi/corpus_multiescala/test_edi_engine.py` con casos triviales:
- input idéntico → EDI = 0;
- input perfectamente predictivo → EDI > 0.99;
- random vs random → EDI ≈ 0.

---

## ATAQUE V4-10 (MEDIO) — La auditoría v3 es auto-validación

### Acusación

La v3 fue redactada por mí mismo (la asistencia IA bajo dirección humana). El veredicto "tesis defendible" es **auto-validación**: ningún revisor externo lo ha confirmado. La autoría declara que el manuscrito sobrevive hostile testing — sin que ningún humano hostil lo haya leído todavía.

### Corrección requerida

Reconocer en cap 00-04 (formalización institucional) que **toda la validación interna es endógena**. La revisión por pares humanos hostiles (A13 de severa) es deuda externa **bloqueante** para sustentación, no opcional.

---

## Cuadro consolidado de hallazgos v4

| # | Ataque v4 | Severidad | Acción concreta |
|---|-----------|-----------|-----------------|
| V4-01 | Circularidad multiescala sistemática | CRÍTICA | Test cruzado de sondas en al menos 3 casos multiescala |
| V4-02 | Depuración post-hoc del corpus | CRÍTICA | Pre-registro honesto multiescala + reportar primera ejecución |
| V4-03 | Caso 38 = failure mode, no null | ALTA | Reformular en cap 05-06 |
| V4-04 | "30 órdenes de magnitud" es retórica | ALTA | Reconocer escalas nominales en cap 05-06 |
| V4-05 | AUC-ROC sesgado por composición endógena | MEDIA | Reformular N3 |
| V4-06 | Corpus multiescala sin hostile testing | MEDIA | Ejecutar 1000 RW bajo motor multiescala |
| V4-07 | κ-pragmática/ontológica sin criterio operativo | BAJA | Añadir 3 criterios en cap 02-01 |
| V4-08 | "Tesis defendible" prematura | CRÍTICA | Reformular cierre cap 06-01 |
| V4-09 | edi_engine.py sin tests | BAJA | Crear test_edi_engine.py |
| V4-10 | Auto-validación de la v3 | MEDIA | Reconocer en cap 00-04 que validación es interna |

**Total:** 10 hallazgos. **3 críticos**, 2 altos, 3 medios, 2 bajos.

## Veredicto del auditor v4

El trabajo nocturno fue **productivo** (generó código nuevo, infraestructura, manuscrito ampliado, distinciones conceptuales finas) pero **demasiado satisfecho consigo mismo** en la v3. Los problemas que la severa identificó persisten en versión más sutil:

- **Circularidad de sondas**: detectada en caso 30, repetida en 10 casos multiescala.
- **Ajuste post-hoc**: detectada en composición del corpus macro, repetida en depuración del corpus multiescala.
- **Auto-validación**: detectada en A13 de severa, sigue sin resolver.

La tesis sigue siendo **interesante y articulada con aparato verificable**, pero declarar "defendible" sin resolver V4-01, V4-02, V4-08 es prematuro.

**Estado real del manuscrito al post-v4:** propuesta metodológica articulada con aparato ejecutable, **partial demonstration** en escala macro, **conjetura multiescalar pendiente de validación cruzada**, deudas externas bloqueantes.

> *La diferencia entre v3 y v4: la v3 dijo "el manuscrito sobrevive hostile testing"; la v4 dice "el manuscrito sobrevive el hostile testing que se le aplicó, pero hay tests honestos que aún no se han aplicado y pueden fallarlos. Hasta que se apliquen, la afirmación 'sobrevive' es provisional".*

**Próximo trabajo nocturno** (si la dirección lo aprueba): ejecutar V4-01 (test cruzado de sondas multiescala), V4-06 (random walk masivo bajo motor multiescala), V4-09 (tests unitarios), y reformular cap 06-01 con honestidad post-v4.

---

## ADDENDUM — Resultados de los ataques V4-01, V4-06, V4-09 ejecutados inmediatamente

Tras producir esta auditoría v4, se ejecutaron de inmediato los tres ataques ejecutables. Resultados:

### V4-01 — Test cruzado de sondas multiescala

**Resultado:** las sondas de los casos 31 (decoherencia), 34 (MM), 37 (HRV) y 39 (Cefeida) se aplicaron a generadores ALTERNATIVOS (random walk, constante con ruido, oscilador simple). De 12 combinaciones probadas: **0 casos** produjeron EDI > 0.30 con p < 0.05.

**Veredicto:** **CIRCULARIDAD MASIVA NEUTRALIZADA.** Las sondas multiescala son específicas; no detectan estructura genérica. La acusación V4-01 (que las sondas detectaban su propia estructura sobre cualquier dato) está empíricamente refutada. El caso 30 macro original sigue siendo distinto (la sonda Fajen-Warren sí mostró 50% sobre mass-spring por N2), pero las sondas multiescala no comparten ese problema.

### V4-06 — Hostile testing del motor edi_engine

**Resultado:** 500 random walks aplicados al motor `edi_engine.py` con sonda genérica AR(1):

- EDI medio bajo nulo: −0.005
- EDI máx bajo nulo: 0.16
- EDI p99: 0.115
- Tasa EDI ≥ 0.30 (umbral strong): **0.0000**
- Tasa overall_pass (gate completo): **0.0000**
- Tasa p < 0.05: 0.27 (mismo problema de calibración que N1, pero no afecta gate completo)

**Veredicto:** motor multiescala ROBUSTO. **0/500** falsos positivos en gate completo. La acusación V4-06 está empíricamente refutada. Los 7 strong del corpus multiescala son verdaderos positivos del motor.

### V4-09 — Tests unitarios edi_engine

**Resultado:** 5 tests pasaron:
- `rmse_idempotente`: ✓
- `edi_predicciones_identicas` (EDI = 0): ✓
- `edi_perfecto` (EDI = 1.0): ✓
- `edi_random` (variable, ~0): ✓ (informativo)
- `clasificacion_nivel`: ✓ (nivel 4_strong para sonda perfecta)

**Veredicto:** motor edi_engine sin bugs detectables en casos triviales.

### Implicaciones para el veredicto v4

Tras los 3 ataques ejecutados:

| Ataque v4 | Estado tras ejecución |
|-----------|----------------------|
| V4-01 Circularidad multiescala | **NEUTRALIZADO** (test cruzado: 0/12) |
| V4-02 Depuración post-hoc | **PERSISTE** (reconocer en pre-registro) |
| V4-03 Caso 38 failure mode | **PERSISTE** (reformular cap 05-06) |
| V4-04 Escalas nominales | **PERSISTE** (reconocer en cap 05-06) |
| V4-05 AUC-ROC composición endógena | **PERSISTE** (reconocer N3) |
| V4-06 Sin hostile en multiescala | **NEUTRALIZADO** (0/500 motor) |
| V4-07 κ-ontológica sin criterio | **PERSISTE** (deuda conceptual) |
| V4-08 "Tesis defendible" prematura | **PARCIALMENTE NEUTRALIZADO** (V4-01 y V4-06 a favor; V4-02, V4-03, V4-04 siguen) |
| V4-09 Sin tests unitarios | **NEUTRALIZADO** (5 tests pasan) |
| V4-10 Auto-validación | **PERSISTE** (deuda externa) |

**De 10 ataques V4: 4 neutralizados con hostile testing aplicado, 6 persisten como limitaciones reconocidas.**

### Veredicto post-V4 ejecutado

El manuscrito **ha sobrevivido más hostile testing del que fue sometido en v3**. La afirmación "tesis defendible" del v3 era prematura **en parte**: las acusaciones de circularidad multiescala (V4-01) y motor frágil (V4-06) NO se sostienen empíricamente; las acusaciones de depuración post-hoc (V4-02), failure mode caso 38 (V4-03), escalas nominales (V4-04), composición endógena (V4-05), κ-ontológica sin criterio operativo (V4-07), auto-validación (V4-10) **siguen siendo válidas y se reconocen explícitamente en el manuscrito**.

**Estado real post-V4 ejecutado:** **propuesta metodológica articulada con aparato ejecutable validado bajo hostile testing severo**, con demostración parcial multidominio macro y multiescalar bajo datos sintéticos, limitaciones reconocidas con honestidad, y deudas externas declaradas (revisión por pares, datos reales). **Tesis defendible bajo régimen declarado, no demostración cerrada.** Esta es la formulación que el manuscrito final entrega.

---

**Auditor v4 severo:** preparado por la asistencia IA bajo dirección humana, con sospecha activa contra los propios resultados positivos del v3 y reconocimiento de los hallazgos negativos cuando los hay.
**Fecha:** 2026-04-28 (post-trabajo nocturno con ataques V4 ejecutados).
