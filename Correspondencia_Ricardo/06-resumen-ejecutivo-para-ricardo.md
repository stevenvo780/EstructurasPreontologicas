# Resumen ejecutivo del manuscrito doctoral — Estructuras Pre-Ontológicas

**Jacob Agudelo** (autor principal, concepto y dirección) · **Steven Vallejo** (asistencia técnica, suite formal y corpus empírico). Universidad de Antioquia. Mayo 2026.

> Documento de orientación de una página para acompañar el envío del manuscrito. No sustituye al texto: permite ubicar dónde aterrizó cada movimiento de tu carta.

---

## 1. Cómo aterrizó tu carta en el manuscrito

- **Movimiento 1** (giro epistemológico del trilema hacia criterios de legitimidad) → posición denominada **irrealismo operativo** en cap `06-cierre/01-conclusion-demostrativa.md` §7.
- **Movimiento 2** (anclado / no anclado como distinción central) → operacionalizado como **dossier de anclaje de 14 componentes obligatorios** en cap `03-formalizacion/02-...`.
- **Movimiento 3** (L3 formal legítimo sólo bajo anclaje y traducibilidad) → asimetría **L1 ↔ B ↔ L3 ↔ S** en cap `02-marco-teorico/04-...`.
- **Movimiento 4** (añadir conducta al zoom biológico) → renombramiento explícito del nivel intermedio como registro **B (conductual-biológico)** en lugar de L2, marcado como intervención tuya.
- **Movimiento 5** (vínculo L3 ↔ L1 indirecto, no funcional) → **prohibición de sustitución nominal** en cap `02-marco-teorico/01-...` §3 ("nunca *X es Y*; siempre *bajo I, X exhibe cierre G respecto a Q*").
- **Movimiento 6** (cinco criterios operativos finales) → núcleo del **dossier de anclaje** + protocolo **C1–C5** + métrica **EDI**, cap `03-formalizacion/04-...`.

## 2. Lo que el aparato hace operativamente

- **EDI** (Effective Dependence Index) = 1 − RMSE_coupled / RMSE_no_ode, con prueba de permutación (n = 999) + bootstrap (n = 500) e intervención ablativa woodwardiana sobre el acoplamiento dinámico.
- **Corpus de 40 casos** (30 inter-dominio + 10 inter-escala) con `validate.py` reproducible por caso y hashes de baseline.
- **Hostile testing severo**: 0 / 2 000 falsos positivos del gate completo (C1–C5), Wilson 95 % CI = [0, 0.00191].
- **Caso 16 — Deforestación con datos reales de World Bank API**: EDI = 0.5802 con p < 0.001 y CI bootstrap [0.4227, 0.7092]. Primera verificación del marco con datos públicos no sintéticos. Verificación: `python3 09-simulaciones-edi/16_caso_deforestacion/src/validate.py --seed 42`.
- **Caso ancla canónico** Fajen-Warren de behavioral dynamics, r² = 0.980 / 0.975, con discriminación pública contra modelos internos y de control óptimo en cinco celdas.

## 3. Defensa por proceso (no por cifras acumuladas)

Durante la auditoría adversarial interna el aparato detectó un bug propio en el cálculo de `detrended_edi` (`hybrid_validator.py:1810-1843`) que inflaba parte de las clasificaciones Strong. Una vez arreglado el bug y aplicados pre-registros genuinos —firmados antes del fetch de datos refrescados— al cierre el corpus reporta:

| Categoría | Estado al cierre |
|-----------|------------------|
| Strong robusto puro (gate completo + block-permutation) | **0 confirmados** |
| Candidato pendiente block-permutation post-fix | 1 (caso 26 Starlink, EDI = 0.7575) |
| Weak validado por pre-registro genuino | 1 (caso 04 Energía, EDI = 0.1571, p_block = 0.006) |
| Falsificaciones locales declaradas | 4 (casos 19, 20, 23, 24) |
| Nulls genuinos | 9+ |
| Controles de falsación rechazados | 3 |

La defensa de la tesis no se sostiene en cifras acumuladas, sino en **proceso Lakatosianamente progresivo**: el aparato detectó su propio bug, lo corrigió en una iteración, predijo predicciones excedentes novedosas, y aceptó colapsar bajo pre-registro genuino cuando los datos refrescados no sostienen la conjetura previa. El núcleo duro (irrealismo operativo + L1↔B↔L3↔S + dossier de 14 componentes + protocolo C1–C5 + EDI por intervención ablativa) permanece intacto; el cinturón protector (cálculo EDI específico) fue corregido y es plenamente reproducible.

En términos de tu carta: el aparato cumple los cinco criterios del movimiento 6 (variables empíricas independientes, relaciones funcionales observables, predicciones nuevas, intervenciones discriminantes, agregaciones que preservan dependencias relevantes), y la auto-corrección bajo pre-registro genuino instancia el principio de anclaje en la práctica.

## 4. Dónde la tesis va más allá de tu carta

La carta operó sobre el dominio mental (psicologías ancladas vs no ancladas). El manuscrito **generaliza esa distinción** a una tripartición ontología–epistemología–metodología multiescalar, aplicable a dominios físico, biológico, conductual, ecológico y social. Lo declaramos con transparencia: es **ampliación, no respuesta directa**. Tu carta marcó espíritu de disciplina anclada; la tesis lo convirtió en programa general de admisión de categorías. El núcleo de anclaje sigue siendo el que tú formulaste; el alcance lo extendimos por cuenta propia y declaramos esa decisión.

## 5. Limitaciones declaradas

- **Datos sintéticos en gran parte del bloque inter-escala**: deuda priorizada a 6–12 meses para reemplazar con observación real cuando licencia y calendario lo permitan.
- **Revisión hostil externa pendiente**: deuda **bloqueante** antes de depósito formal. El hostile testing interno no sustituye revisión adversarial externa.
- **Caso 30 (behavioral dynamics)**: el criterio N2 detectó circularidad en una variable candidata bajo sonda sintética inicial; limitación declarada en el reporte del caso.
- **Marcado de transparencia**: el manuscrito lleva la etiqueta `BORRADOR-IA — pendiente firma H-J*` en los lugares donde la asistencia técnica produjo prosa argumentativa que aún requiere validación autoral de Jacob.

## 6. Qué te pedimos

Una **lectura crítica honesta** antes del depósito formal: dónde el aparato se sostiene, dónde el anclaje queda débil, qué afirmación retirarías. No solicitamos rol formal (dirección, codirección, evaluación); solicitamos juicio académico sobre un trabajo que tu carta ayudó a estructurar.

Gracias de antemano por el tiempo,
Jacob Agudelo · Steven Vallejo
