# Resumen ejecutivo del manuscrito doctoral — Estructuras Pre-Ontológicas

**Jacob Agudelo** (autor principal, concepto y dirección) · **Steven Vallejo** (asistencia técnica, suite formal y corpus empírico). Universidad de Antioquia. Mayo 2026.

> Documento de orientación de una página para acompañar el envío de la versión larga del manuscrito (~744 KB, 9 074 líneas). No sustituye al texto: permite ubicar dónde aterrizó cada movimiento de tu carta.

---

## 1. Cómo aterrizó tu carta en el manuscrito

- **Movimiento 1** (giro epistemológico del trilema hacia criterios de legitimidad) → posición denominada **irrealismo operativo** en cap `06-cierre/01-conclusion-demostrativa.md` §7.
- **Movimiento 2** (anclado / no anclado como distinción central) → operacionalizado como **dossier de anclaje de 14 componentes obligatorios** en cap `03-formalizacion/02-...` (estructura del dossier).
- **Movimiento 3** (L3 formal legítimo sólo bajo anclaje y traducibilidad) → asimetría **L1 ↔ B ↔ L3 ↔ S** en cap `02-marco-teorico/04-...`.
- **Movimiento 4** (añadir conducta al zoom biológico) → renombramiento explícito del nivel intermedio como registro **B (conductual-biológico)**, cap `02-marco-teorico/04-...` §4, marcado como intervención tuya.
- **Movimiento 5** (vínculo L3 ↔ L1 indirecto, no funcional) → **prohibición de sustitución nominal** en cap `02-marco-teorico/01-...` §3 ("nunca *X es Y*; siempre *bajo I, X exhibe cierre G respecto a Q*").
- **Movimiento 6** (cinco criterios operativos finales) → núcleo del **dossier de anclaje** + protocolo **C1–C5** + métrica **EDI**, cap `03-formalizacion/04-...`.

## 2. Lo que el aparato hace operativamente

- **EDI** (Effective Dependence Index) = 1 − RMSE_coupled / RMSE_no_ode, con prueba de permutación (n = 999) + bootstrap (n = 500) e intervención ablativa woodwardiana sobre el acoplamiento dinámico.
- **Corpus de 40 casos** (30 inter-dominio + 10 inter-escala) con `validate.py` reproducible por caso y hashes de baseline.
- **4 escenarios `overall_pass = True`** (3 con datos sintéticos calibrados a parámetros publicados + 1 con datos reales).
- **Conteo corpus inter-dominio (30 casos, actualizado 2026-05-16 tras caso 03):** 4 strong con `overall_pass`, 1 strong sin gate, **7 weak (antes 8)**, 2 suggestive, **3 trend (antes 4)**, **10 null (antes 8)**, 3 controles de falsación rechazados.
- **Caso 16 — Deforestación con datos REALES de World Bank API**: EDI = 0.5802 (rango Strong, p < 0.001). Es la primera verificación del marco con datos públicos no sintéticos.
- **Caso 01 — Clima regional reclasificado Trend → Null tras re-ejecución con datos reales IPCC-calibrados (2026-05-16)**: EDI = -0.0007, p_perm = 0.998 bajo sonda Budyko-Sellers. Es ejemplo del aparato declarando honestamente ausencia de cierre cuando datos reales contradicen la expectativa previa (Trend con datos sintéticos). El aparato no es máquina de validar deseos.
- **Caso 03 — Contaminación PM2.5 reclasificado Weak → Null tras re-ejecución iter 3 con datos World Bank PM2.5 reales (2026-05-16)**: EDI = -0.0109, p_perm = 0.616. Tercer ejemplo del aparato declarando honestamente cuando datos reales no soportan la categoría previa: junto a los casos 16 (datos reales confirman Strong) y 01 (datos reales reclasifican a Null), el caso 03 muestra simetría — el motor no infla la métrica cuando los datos contradicen la clasificación heredada.
- **Hostile testing severo**: 0 / 2 000 falsos positivos del gate completo (C1–C5), Wilson 95 % CI = [0, 0.00191].

## 3. Dónde la tesis va más allá de tu carta

La carta operó sobre el dominio mental (psicologías ancladas vs no ancladas). El manuscrito **generaliza esa distinción** a una tripartición ontología–epistemología–metodología multiescalar, aplicable a dominios físico, biológico, conductual, ecológico y social. Lo declaramos con transparencia: es **ampliación, no respuesta directa**. Tu carta marcó espíritu de disciplina anclada; la tesis lo convirtió en programa general de admisión de categorías. El núcleo de anclaje sigue siendo el que tú formulaste; el alcance lo extendimos por cuenta propia y declaramos esa decisión.

## 4. Limitaciones declaradas

- **Datos sintéticos en la totalidad del bloque inter-escala**: deuda priorizada a 6–12 meses para reemplazar con observación real cuando la licencia y el calendario lo permitan.
- **Revisión hostil externa pendiente**: deuda **bloqueante** antes de depósito formal. El hostile testing interno (0 / 2 000) no sustituye revisión adversarial externa.
- **Caso 30 (behavioral dynamics)**: el criterio N2 detectó **circularidad** en una de las variables candidatas; limitación declarada en el reporte del caso y en la tabla del corpus.
- **Marcado de transparencia**: el manuscrito lleva la etiqueta `BORRADOR-IA — pendiente firma H-J*` en cinco lugares donde la asistencia técnica produjo prosa argumentativa que aún requiere validación autoral de Jacob.

## 5. Qué te pedimos

Una **lectura crítica honesta** antes del depósito formal: dónde el aparato se sostiene, dónde el anclaje queda débil, qué afirmación retirarías. No solicitamos rol formal (dirección, codirección, evaluación); solicitamos juicio académico sobre un trabajo que tu carta ayudó a estructurar.

Gracias de antemano por el tiempo,
Jacob Agudelo · Steven Vallejo
