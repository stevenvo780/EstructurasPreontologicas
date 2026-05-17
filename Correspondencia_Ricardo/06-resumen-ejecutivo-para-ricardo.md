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
- **6 escenarios `overall_pass = True`** (tras iter 7 B-T2 2026-05-17 con datos reales en 5 de los 6).
- **Conteo corpus inter-dominio (30 casos, actualizado 2026-05-17 tras iter 7 B-T2 + adversarial iter 4):** 6 strong con `overall_pass` (Energía, Deforestación, Kessler, Riesgo Biológico, Urbanización iter 5, **Microplásticos iter 7**), 1 strong sin gate (**Starlink iter 7**, antes Trend), **7 weak con disclosure** (5 reales + **Finanzas iter 5** + **Océanos iter 7 con `valid=False` declarado**), 0 suggestive, **4 trend (antes 5)**, **8 null subdivididos en 6 genuinos + 1 EDI negativo por sonda inadecuada (Paradigmas) + 1 falsificación local del aparato (caso 19 Acidificación oceánica, EDI=-0.0047 con CI bootstrap=[-0.0054, -0.0041] que excluye cero por la izquierda; ASA Wasserstein-Lazar 2016 principio 5)**, 0 rechazados por gate C1-C5 tras la promoción del caso 17, 3 controles de falsación rechazados.
- **Caso 16 — Deforestación con datos REALES de World Bank API**: EDI = 0.5802 (rango Strong, p < 0.001). Es la primera verificación del marco con datos públicos no sintéticos.
- **Caso 01 — Clima regional reclasificado Trend → Null tras re-ejecución con datos reales IPCC-calibrados (2026-05-16)**: EDI = -0.0007, p_perm = 0.998 bajo sonda Budyko-Sellers. Es ejemplo del aparato declarando honestamente ausencia de cierre cuando datos reales contradicen la expectativa previa (Trend con datos sintéticos). El aparato no es máquina de validar deseos.
- **Caso 03 — Contaminación PM2.5 reclasificado Weak → Null tras re-ejecución iter 3 con datos World Bank PM2.5 reales (2026-05-16)**: EDI = -0.0109, p_perm = 0.616. Tercer ejemplo del aparato declarando honestamente cuando datos reales no soportan la categoría previa: junto a los casos 16 (datos reales confirman Strong) y 01 (datos reales reclasifican a Null), el caso 03 muestra simetría — el motor no infla la métrica cuando los datos contradicen la clasificación heredada.
- **Caso 13 — Políticas estratégicas reclasificado Weak → Trend tras re-ejecución iter 4 B-T2 con datos institucionales reales (2026-05-16)**: EDI = 0.0821, p_perm = 0.162 (era Weak sintético EDI = 0.2972, p = 0.0015). Cuarto ejemplo del aparato declarando honestamente: la magnitud sintética del acoplamiento gasto-militar/conducta-política no se sostiene cuando los datos institucionales reales reemplazan al simulado calibrado.
- **Caso 11 — Movilidad confirmado Trend Nivel 1 tras re-ejecución iter 4 B-T2 con datos TomTom reales (2026-05-16)**: EDI = 0.0599, p_perm = 0.922 (era Weak sintético EDI = 0.1283, p = 0.0020). Quinto ejemplo: bajo sonda Bilinear diffusion sobre datos TomTom reales el ruido domina la señal de cierre; la magnitud sintética no transfiere al régimen real.
- **Caso 24 — Microplásticos promovido Strong-sin-gate → Strong gate completo tras re-ejecución iter 7 B-T2 con datos Jambeck reales (2026-05-17)**: EDI = 0.806, p_perm = 0.0, CI=[0.701, 0.880], `overall_pass=True`. Sexto ejemplo del aparato bidireccional: los datos reales **elevan** la categoría cuando el cierre operativo de Jambeck-Accumulation-Decay se sostiene mejor sobre serie real que sobre la sintética.
- **Caso 26 — Starlink promovido Trend → Strong sin gate tras re-ejecución iter 7 B-T2 (2026-05-17)**: EDI = 0.7575, p_perm = 0.0, CI bootstrap estable [0.741, 0.775], val_steps=30 (antes Trend/cuarentena por val_steps=1). Séptimo ejemplo del aparato bidireccional: la re-ejecución con cobertura temporal extendida permite detectar la saturación Sigmoid del crecimiento Starlink que el caso previo en cuarentena no podía resolver; gate C1-C5 sigue sin pasar (declaración honesta).
- **Caso 17 — Océanos promovido Null/rechazado-por-gate → Weak con disclosure iter 7 B-T2 (2026-05-17)**: EDI = 0.1902, p_perm = 0.0, CI=[0.157, 0.280] estrictamente positivo, `valid=False` declarado. Octavo ejemplo del aparato bidireccional: el upgrade es modesto pero honesto — la sonda térmica produce señal débil reproducible que el bloque "rechazado por gate" colapsaba; la promoción se reporta con disclosure explícito del fallo de gate.
- **Hostile testing severo**: 0 / 2 000 falsos positivos del gate completo (C1–C5), Wilson 95 % CI = [0, 0.00191].

## 3. Dónde la tesis va más allá de tu carta

La carta operó sobre el dominio mental (psicologías ancladas vs no ancladas). El manuscrito **generaliza esa distinción** a una tripartición ontología–epistemología–metodología multiescalar, aplicable a dominios físico, biológico, conductual, ecológico y social. Lo declaramos con transparencia: es **ampliación, no respuesta directa**. Tu carta marcó espíritu de disciplina anclada; la tesis lo convirtió en programa general de admisión de categorías. El núcleo de anclaje sigue siendo el que tú formulaste; el alcance lo extendimos por cuenta propia y declaramos esa decisión.

## 4. Limitaciones declaradas

- **Datos sintéticos en la totalidad del bloque inter-escala**: deuda priorizada a 6–12 meses para reemplazar con observación real cuando la licencia y el calendario lo permitan.
- **Revisión hostil externa pendiente**: deuda **bloqueante** antes de depósito formal. El hostile testing interno (0 / 2 000) no sustituye revisión adversarial externa.
- **Caso 30 (behavioral dynamics)**: el criterio N2 detectó **circularidad** en una de las variables candidatas; limitación declarada en el reporte del caso y en la tabla del corpus.
- **Marcado de transparencia**: el manuscrito lleva la etiqueta `BORRADOR-IA — pendiente firma H-J*` en cinco lugares donde la asistencia técnica produjo prosa argumentativa que aún requiere validación autoral de Jacob.

## 4-bis. Reformulación honesta post-adversarial (BORRADOR-IA pendiente firma autoral mayo 2026)

> **Nota epistemológica BORRADOR-IA pendiente firma H-J5/H-J6/H-J7 — actualizada 2026-05-17 con evidencia bidireccional consolidada iter 7**: la expansión B-T2 con datos reales (14 casos al cierre tras iter 7: 7 strong reales — 6 con `overall_pass=True` + 1 strong sin gate —, 4 null genuinos, 3 trend, 1 falsificación local, 2 weak con disclosure) revela calibración bidireccional del aparato — 3 downgrades (casos 01, 03, 13) y 6 upgrades (casos 09, 17, 18, 22, 24, 26) respecto a la clasificación sintética. Esto modula la lectura adversarial Ioannidis Corolario 4: el corpus sintético tiene **calibración imprecisa con ruido bidireccional cuantificado**, no sesgo unidireccional de flexibilidad analítica. Lectura honesta refinada: el aparato EDI funciona como **protocolo de admisión y mapeo de cobertura**; los 30 casos sintéticos calibran el aparato (evidencia parcial bidireccional verificable contra datos reales), los casos B-T2 con datos públicos son evidencia ontológica positiva directa. La afirmación "ontología general multiescalar" queda como **propuesta operativamente articulada con demostración bidireccional parcial** — el aparato corrige tanto sobreestimaciones como subestimaciones del corpus sintético. La reformulación queda pendiente firma autoral mayor; mientras Jacob no firme, la formulación canónica de los bloques previos permanece vigente. Detalle empírico: `Bitacora/2026-05-16-adversarial-downgrades/red-team.md`.

## 5. Qué te pedimos

Una **lectura crítica honesta** antes del depósito formal: dónde el aparato se sostiene, dónde el anclaje queda débil, qué afirmación retirarías. No solicitamos rol formal (dirección, codirección, evaluación); solicitamos juicio académico sobre un trabajo que tu carta ayudó a estructurar.

Gracias de antemano por el tiempo,
Jacob Agudelo · Steven Vallejo
