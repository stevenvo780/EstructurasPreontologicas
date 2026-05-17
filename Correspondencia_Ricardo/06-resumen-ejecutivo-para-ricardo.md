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
- **Conteo corpus inter-dominio (30 casos, actualizado 2026-05-16 tras iter 4 B-T2 + adversarial iter 4):** 4 strong con `overall_pass`, 1 strong sin gate, **5 weak (antes 8)**, 2 suggestive, **5 trend (antes 4)**, **10 null subdivididos en 7 genuinos + 1 EDI negativo por sonda inadecuada (Paradigmas) + 1 falsificación local del aparato (caso 19 Acidificación oceánica, EDI=-0.0047 con CI bootstrap=[-0.0054, -0.0041] que excluye cero por la izquierda; ASA Wasserstein-Lazar 2016 principio 5) + 1 rechazado por gate C1-C5 (antes 8 sin subdivisión)**, 3 controles de falsación rechazados.
- **Caso 16 — Deforestación con datos REALES de World Bank API**: EDI = 0.5802 (rango Strong, p < 0.001). Es la primera verificación del marco con datos públicos no sintéticos.
- **Caso 01 — Clima regional reclasificado Trend → Null tras re-ejecución con datos reales IPCC-calibrados (2026-05-16)**: EDI = -0.0007, p_perm = 0.998 bajo sonda Budyko-Sellers. Es ejemplo del aparato declarando honestamente ausencia de cierre cuando datos reales contradicen la expectativa previa (Trend con datos sintéticos). El aparato no es máquina de validar deseos.
- **Caso 03 — Contaminación PM2.5 reclasificado Weak → Null tras re-ejecución iter 3 con datos World Bank PM2.5 reales (2026-05-16)**: EDI = -0.0109, p_perm = 0.616. Tercer ejemplo del aparato declarando honestamente cuando datos reales no soportan la categoría previa: junto a los casos 16 (datos reales confirman Strong) y 01 (datos reales reclasifican a Null), el caso 03 muestra simetría — el motor no infla la métrica cuando los datos contradicen la clasificación heredada.
- **Caso 13 — Políticas estratégicas reclasificado Weak → Trend tras re-ejecución iter 4 B-T2 con datos institucionales reales (2026-05-16)**: EDI = 0.0821, p_perm = 0.162 (era Weak sintético EDI = 0.2972, p = 0.0015). Cuarto ejemplo del aparato declarando honestamente: la magnitud sintética del acoplamiento gasto-militar/conducta-política no se sostiene cuando los datos institucionales reales reemplazan al simulado calibrado.
- **Caso 11 — Movilidad confirmado Trend Nivel 1 tras re-ejecución iter 4 B-T2 con datos TomTom reales (2026-05-16)**: EDI = 0.0599, p_perm = 0.922 (era Weak sintético EDI = 0.1283, p = 0.0020). Quinto ejemplo: bajo sonda Bilinear diffusion sobre datos TomTom reales el ruido domina la señal de cierre; la magnitud sintética no transfiere al régimen real.
- **Hostile testing severo**: 0 / 2 000 falsos positivos del gate completo (C1–C5), Wilson 95 % CI = [0, 0.00191].

## 3. Dónde la tesis va más allá de tu carta

La carta operó sobre el dominio mental (psicologías ancladas vs no ancladas). El manuscrito **generaliza esa distinción** a una tripartición ontología–epistemología–metodología multiescalar, aplicable a dominios físico, biológico, conductual, ecológico y social. Lo declaramos con transparencia: es **ampliación, no respuesta directa**. Tu carta marcó espíritu de disciplina anclada; la tesis lo convirtió en programa general de admisión de categorías. El núcleo de anclaje sigue siendo el que tú formulaste; el alcance lo extendimos por cuenta propia y declaramos esa decisión.

## 4. Limitaciones declaradas

- **Datos sintéticos en la totalidad del bloque inter-escala**: deuda priorizada a 6–12 meses para reemplazar con observación real cuando la licencia y el calendario lo permitan.
- **Revisión hostil externa pendiente**: deuda **bloqueante** antes de depósito formal. El hostile testing interno (0 / 2 000) no sustituye revisión adversarial externa.
- **Caso 30 (behavioral dynamics)**: el criterio N2 detectó **circularidad** en una de las variables candidatas; limitación declarada en el reporte del caso y en la tabla del corpus.
- **Marcado de transparencia**: el manuscrito lleva la etiqueta `BORRADOR-IA — pendiente firma H-J*` en cinco lugares donde la asistencia técnica produjo prosa argumentativa que aún requiere validación autoral de Jacob.

## 4-bis. Reformulación honesta post-adversarial (BORRADOR-IA pendiente firma autoral mayo 2026)

> **BORRADOR-IA pendiente firma autoral H-J5/H-J6/H-J7 — reformulación post-adversarial 2026-05-16, actualizada iter 5 con upgrades 2026-05-17.** La expansión B-T2 con datos reales (mayo 2026) reveló que el corpus sintético inter-dominio (30 casos) debe leerse, en lectura honesta endurecida, como **calibración del aparato**, no como evidencia ontológica positiva. La evidencia ontológica real son al cierre iter 5 los **4 casos strong reales** obtenidos con APIs públicas (Deforestación World Bank EDI=0.5802, Energía OWID EDI=0.4615, Kessler NASA ODPO EDI=0.6936, **Urbanización World Bank SP.URB.TOTL.IN.ZS EDI=0.3366 con `overall_pass=True`, promovida Weak→Strong tras re-ejecución con datos reales iter 5 B-T2 2026-05-17**) **+ 1 weak real** (Finanzas yfinance SPY + FRED EDI=0.1027 con CI=[0.1006, 0.1052] estrictamente positivo, promovida Suggestive→Weak iter 5 B-T2 2026-05-17), más 3 null genuinos (Clima, Acidificación, Riesgo Biológico) y 1 falsificación local del aparato (caso 19, EDI<0 con CI que excluye cero por la izquierda). El aparato cumple su rol de protocolo de admisión honesto **en ambas direcciones**: declara strong cuando los datos lo soportan (incluida promoción de casos previamente weak/suggestive), null o falsificación cuando no. La expansión B-T2 no es máquina monolítica de degradación; produce upgrades reales (09, 18) tanto como downgrades (01, 03, 11, 13), confirmando calibración bidireccional del aparato. La reformulación queda pendiente firma autoral mayor; mientras Jacob no firme, la formulación canónica de los bloques previos permanece vigente. Detalle: `Bitacora/2026-05-16-adversarial-downgrades/`.

## 5. Qué te pedimos

Una **lectura crítica honesta** antes del depósito formal: dónde el aparato se sostiene, dónde el anclaje queda débil, qué afirmación retirarías. No solicitamos rol formal (dirección, codirección, evaluación); solicitamos juicio académico sobre un trabajo que tu carta ayudó a estructurar.

Gracias de antemano por el tiempo,
Jacob Agudelo · Steven Vallejo
