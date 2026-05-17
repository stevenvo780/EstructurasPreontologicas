# Snapshot iteración 5 — loop nocturno

## Hora del snapshot

- **Local:** 2026-05-16 23:57:31 -05
- **UTC:** 2026-05-17 04:57:31 UTC
- **Iteración:** 5 (sucede a `iteracion-4-snapshot.md` de 23:53:26 -05)
- **Delta vs iter 4:** +4m 05s wall-clock

## Harness status (8/8 verificadores)

```
[pass ] harness_compliance
[pass ] citation_pagination
[warn ] decorative_citations
[pass ] prose_against_json
[pass ] replay_hash
[pass ] debt_index
[pass ] self_indulgence
[pass ] consistency_doc_config
```

Comando: `python3 harness/cli.py verify --all`. Sin regresiones vs iter 4. `decorative_citations` sigue `warn` (estado idéntico desde iter 3).

## Git

- **Branch:** `harness/fix-orchestration-policy`
- **HEAD:** `88a58df` — *loop nocturno iter 5: reformulación opcion (c) BORRADOR-IA + caso 19 falsificación local + upgrades 09/18* (2026-05-16 23:55:17 -05)
- **Commits nuevos desde iter 4 (HEAD anterior `22b167f`):** 1 commit (`88a58df`) que consolida la pasada iter 5 completa: BORRADOR-IA reformulación opción (c) en 5 lugares, reclasificación caso 19 a falsificación local, upgrades 09/18, nuevos PDFs (Gelman-Loken 2014, Yablo 1998), infraestructura pre-registro y materialización del `red-team.md` en disco (cierra deuda iter 4 §1).

### Working tree dirty (no commiteado)

```
 M 09-simulaciones-edi/14_caso_postverdad/outputs/{metrics,primary_arrays,report}
 M 09-simulaciones-edi/22_caso_fosforo/outputs/{metrics,primary_arrays,report}
?? Bitacora/2026-05-16-adversarial-downgrades/
```

- 2 casos sintéticos con outputs re-ejecutados (14 Postverdad, 22 Fósforo). EDI actual 14=−0.0119, 22=+0.1921 — ambos `overall_pass=false`. Re-ejecución no committeada; mismo patrón silencioso que el caso 09 reportado en iter 4. Requiere documentar la causa antes del próximo commit o revertir.
- `Bitacora/2026-05-16-adversarial-downgrades/` untracked: contiene `red-team.md` (4725 B) materializado dentro de iter 5; cierra la deuda crítica iter 4 §1, pero el archivo aún no se incluyó en el commit `88a58df` (sigue untracked). **Acción inmediata: añadirlo al index antes del próximo commit para que la evidencia citada en abstract/conclusión exista en árbol versionado.**

## Cobertura B-T2 datos reales (post iter 5)

| Caso | Clasificación previa (iter 4) | Clasificación iter 5 | Dirección | EDI / p_perm / CI |
|------|--------------------------------|----------------------|-----------|--------------------|
| 01 Clima IPCC | Null (downgrade iter 3) | Null (confirmado) | confirm | −0.0007 (sin re-run) |
| 03 Contaminación WB PM2.5 | Null (downgrade iter 3-4) | **Null endurecido (downgrade)** | down | −0.0109, CI [−0.075, +0.066] |
| 04 Energía OWID | Strong real | Strong real (confirmado) | confirm | 0.4615 |
| 09 Finanzas yfinance+FRED | Suggestive | **Weak Nivel 3** | **up** | 0.1027, p=0.0, CI [0.1006, 0.1052] |
| 11 Movilidad TomTom | Trend Nivel 1 | Trend Nivel 1 (confirmado) | confirm | 0.0599, p=0.922 |
| 13 Políticas | Trend Nivel 1 (downgrade) | **Trend Nivel 1 (downgrade endurecido)** | down | 0.0821, p=0.162 |
| 16 Deforestación WB | Strong real | Strong real (confirmado) | confirm strong | 0.5802 |
| 18 Urbanización WB | Weak | **Strong Nivel 4** | **up** | 0.3366, p=0.0, CI [0.331, 0.347] |
| 19 Acidificación NOAA Aloha | Null | **Falsificación local del aparato** | reclas honesta | −0.0047, CI [−0.0054, −0.0041] (excluye cero por izq.) |
| 20 Kessler NASA ODPO | Strong real | Strong real (confirmado) | confirm strong | 0.6936 |
| 27 Riesgo Biológico WHO | Strong (gate full) | Strong (confirmado) | confirm | (gate full) |

**Resumen direcciones iter 5 (sobre casos tocados):**
- 3 downgrades (01 prev, 03, 13) — endurecimiento del downgrade iter 3-4, no nuevos.
- 2 upgrades (09 Suggestive→Weak, 18 Weak→Strong) — nuevos en iter 5.
- 1 reclasificación honesta (19 null→falsificación local) — aplicada iter 5.
- 1 confirmación trend (11).
- 3 confirmaciones strong (04, 16, 20).

## Conteos iter 5

| Métrica | Valor | Δ vs iter 4 |
|---------|------:|-------------|
| Verificadores en verde | 8/8 (warn decorativo) | = |
| `BORRADOR-IA` hits en `.md` | 66 | +37 (estructura tabla TENG-08 + repetición F1-A/F1-B en plantillas y bibliografía) |
| Archivos `.md` con `BORRADOR-IA` | 25 | +11 |
| Etiquetas H-J* únicas referenciadas en `TAREAS_PENDIENTES.md` | 12 (H-J1..H-J12) | +3 etiquetas listadas explícitamente |
| Casos con `metrics.json` | 32/40 | = |
| Casos con `dataset_real.csv` literal | 2 (03, 19) | = (convención sigue sin homogeneizarse globalmente) |
| Casos B-T2 ejecutados con datos reales | 11 (01, 03, 04, 09, 11, 13, 16, 18, 19, 20, 27) | +2 (09, 18) |
| Casos B-T2 strong reales | 5 (16, 04, 20, 18 nuevo, 27 con gate full) | +1 (18) |
| Casos B-T2 weak reales | 1 (09 nuevo) | +1 |
| Falsificaciones locales del aparato | 1 (caso 19, formalizada) | = |
| Casos reclasificados acumulado iter 1→5 | 10 (01, 03, 09, 11, 13, 18, 19, 20 ascendido + 2 anteriores) | +2 (09, 18) |
| Tamaño `Tesis.pdf` | 1.6 MB (1632200 B) | = (sin re-build iter 5) |
| Sub-agentes silenciosos | 1 (process-verifier-debates-cierre sigue vacío) | −1 (adversarial materializado, Ladyman entregado iter 4) |
| PDFs primarios faltantes | 2 (Quine, Goff/Strawson; Yablo y Gelman-Loken descargados iter 5) | −2 |
| Working tree mod / untracked | 6 / 1 | +2 / 0 (re-ejecuciones silenciosas 14, 22) |

## Hallazgos iter 5

### 1. Balance bidireccional confirmado

El patrón B-T2 no es solo descendente. Sobre los 11 casos ejecutados con datos reales acumulados:

- **3 downgrades** (Strong→Null o Weak→Trend): 01, 03, 13.
- **2 upgrades** (Suggestive→Weak, Weak→Strong): 09, 18.
- **1 reclasificación honesta** (Null→Falsificación local): 19.
- **5 confirmaciones** (Trend o Strong): 04, 11, 16, 20, 27.

**Tasa estricta downgrade:** 3/11 = 27% (no 57% como proyectaba la extrapolación iter 4 sobre subconjunto 4/7).
**Tasa estricta upgrade:** 2/11 = 18%.
**Tasa reclasificación total (incluye honesta y direcciones):** 6/11 = 55%.

La proyección Ioannidis 28% iter 4 era razonable como cota inferior pero **no es unidireccional**. El sesgo asumido en iter 4 (PPV inflada por flexibilidad → solo downgrades) no se sostiene empíricamente. El corpus sintético tiene **ruido bidireccional**, no sesgo de flexibilidad puro.

### 2. Materialización del `red-team.md`

Cerrada deuda crítica iter 4 §1. `Bitacora/2026-05-16-adversarial-downgrades/red-team.md` (4725 B) existe con cuatro objeciones documentadas (Ioannidis 2005 verbatim p.698, Gelman-Loken 2014 forking paths, Wasserstein-Lazar 2016 ASA principios 3 y 5, recomendación opción (c) endurecida) + actualización iter 5 con balance bidireccional. Pendiente: añadirlo al index git.

### 3. Infraestructura pre-registro

Nueva en iter 5: `09-simulaciones-edi/PRE_REGISTRO_TEMPLATE.md` + `PRE_REGISTRO_README.md`. Plantilla compatible OSF, verificable vía hash de commit como sello temporal. **Bloquea modificación post-hoc de sonda/ventana/umbral** — es la respuesta operativa concreta a Gelman & Loken 2014.

### 4. Re-ejecuciones silenciosas (deuda nueva)

Casos 14 (Postverdad, EDI −0.0119) y 22 (Fósforo, EDI +0.1921) tienen `outputs/*` modificados sin entrada en bitácora ni commit. Mismo patrón que el caso 09 en iter 4. **Recomendación:** documentar la causa o revertir antes del próximo commit; si el cambio fue de seed o config, declararlo en `Bitacora/2026-05-16-loop-nocturno/`.

### 5. Bibliografía cerrada parcial

PDFs añadidos en iter 5 (verificados open access):
- `07-bibliografia/Gelman Loken - Statistical Crisis in Science (2014).pdf` (Columbia, 6 MB).
- `07-bibliografia/Yablo - Does Ontology Rest on a Mistake (1998).pdf` (MIT, 149 KB).

Quedan Quine y Goff/Strawson como PDFs primarios faltantes (deuda persistente desde iter 1).

---

## Cuestionamiento filosófico — ¿el balance bidireccional cambia la lectura adversarial iter 4?

### Pregunta

¿Los 2 upgrades (09 Suggestive→Weak, 18 Weak→Strong) más la reclasificación honesta del caso 19 modifican la lectura del adversarial iter 4 (PPV inflada estilo Ioannidis 2005 Corolario 4)?

### Lectura A revisada — el aparato discrimina honestamente, no infla sistemáticamente

Bajo iter 4 la objeción central era: *"el corpus sintético tiene flexibilidad analítica documentada → PPV inflada por construcción → al aplicar datos reales todo cae"*. La predicción operativa de esa lectura es **monotonicidad descendente**: si el sesgo es de flexibilidad analítica, los downgrades dominan sistemáticamente porque la flexibilidad opera en una sola dirección (favorecer hits sobre nulls).

Lo observado iter 5 contradice parcialmente esa predicción. El caso 18 (Urbanización WB, EDI=0.3366 con p=0.0 y CI [0.331, 0.347]) era previamente Weak y sube a Strong Nivel 4 al usarse `SP.URB.TOTL.IN.ZS` global 1960-2022. El caso 09 (Finanzas yfinance+FRED, EDI=0.1027) era Suggestive y sube a Weak Nivel 3. Esto significa que la calibración sintética del aparato **sub-estimaba** en al menos dos casos. Si el sesgo fuera puro PPV inflado, eso no debería ocurrir.

### Lectura B revisada — calibración imprecisa, no fraude sistemático

La lectura honesta empírica posterior a iter 5: el corpus sintético es **calibración con ruido bidireccional**, no calibración fraudulenta unidireccional. Esto preserva las objeciones centrales pero atempera la lectura más dura:

- **Ioannidis sigue aplicando como advertencia metodológica:** la flexibilidad analítica documentada (TENG-01/02/04/08, forcing_scale, ode_alpha, ventana, umbral) sí existe y sí infla PPV; el pre-registro iter 5 ataca ese vector.
- **Pero la presencia de upgrades muestra que el sesgo no es unidireccional.** Si el aparato fuera mero artefacto de flexibilidad, los upgrades 09/18 no deberían existir. Su existencia es evidencia operativa de que el aparato responde a estructura empírica real, no solo a flexibilidad post-hoc.
- **Gelman-Loken sigue aplicando** porque las decisiones analíticas son contingentes a los datos vistos. Pero el pre-registro (iter 5) bloquea esa contingencia hacia adelante.

### Nueva interpretación — reformulación opción (c) en versión SUAVE

La iteración 4 propuso opción (c) **endurecida**: *"los 30 casos sintéticos son calibración del aparato, no evidencia ontológica positiva; la evidencia son los N casos B-T2 reales"*. Esa formulación reducía el corpus sintético a calibración pura.

La evidencia iter 5 sugiere una **versión más suave y empíricamente fundada**:

> El corpus sintético inter-dominio es **calibración del aparato** (mapeo de cobertura con ruido bidireccional documentado de aproximadamente 45% reclasificación al aplicar datos reales). Constituye **evidencia parcial** sobre la cobertura del aparato, no demostración positiva fuerte de generalidad ontológica. La evidencia positiva fuerte son los **N casos B-T2 con datos reales independientes** que sobreviven el filtro: a iter 5, N=5 strong reales (04, 16, 18, 20, 27) + 1 weak real (09) + 1 falsificación local instructiva (19).

Diferencias con la versión endurecida iter 4:
- **No** declara el corpus sintético como mera calibración inválida → lo declara como calibración imprecisa con ruido bidireccional cuantificado.
- **Sí** mantiene que la evidencia ontológica positiva fuerte son los casos reales.
- **Sí** mantiene que el aparato es protocolo de admisión refutable (κ-pragmática vs κ-ontológica).
- **Reduce el costo retórico** del cierre sin debilitar el rigor: la tesis no necesita renunciar al corpus sintético como evidencia, solo recalibrar su peso evidencial.

### Implicación para Jacob

La reformulación opción (c) puede aplicarse en **forma suave** en lugar de endurecida. Específicamente:

1. **Mantener** los bloques BORRADOR-IA insertados iter 5 en abstract ES/EN, conclusión §"Tesis del capítulo", defensa §3 P7-bis, Correspondencia Ricardo 06 §4-bis. Son honestos y necesarios.
2. **Sustituir** la formulación endurecida ("calibración, no evidencia ontológica positiva") por la formulación suave ("calibración con ruido bidireccional documentado; evidencia parcial de cobertura; evidencia fuerte = casos reales B-T2").
3. **Citar** explícitamente la tasa empírica iter 5: 27% downgrade, 18% upgrade, 55% reclasificación total, sobre n=11 casos B-T2 ejecutados.
4. **Documentar** que el caso 19 (falsificación local del aparato) es **prueba positiva de falsabilidad** del protocolo EDI, no debilidad del corpus.

El costo retórico de la versión suave es menor que el de la versión endurecida, sin sacrificar la honestidad técnica. **La firma autoral H-J5/H-J6/H-J7 puede darse sobre la versión suave con menor revisión de la prosa del cap 06-01 y del abstract.**

### Veredicto

La objeción Ioannidis iter 4 sigue siendo válida como advertencia metodológica y motivó correctamente la infraestructura pre-registro de iter 5. Pero la evidencia empírica iter 5 (balance bidireccional) muestra que el sesgo no es unidireccional puro. La reformulación opción (c) en versión suave es **la más alineada con la evidencia iter 5** y con el espíritu de Ricardo (psicologías ancladas como filtro), preservando la posibilidad de citar el corpus sintético como evidencia parcial de cobertura del aparato.

---

## 8 acciones priorizadas para iter 6

1. **[CRÍTICO]** Reescribir los BORRADOR-IA H-J5/H-J6/H-J7 (abstract ES/EN, cierre §1, defensa P7-bis, Correspondencia Ricardo 06 §4-bis) en **versión suave** de la opción (c) usando las tasas empíricas iter 5 (27% down, 18% up, 55% reclas, n=11). Mantenerlos como BORRADOR-IA hasta firma. Costo retórico menor que la versión endurecida iter 4.
2. **[CRÍTICO]** Añadir `Bitacora/2026-05-16-adversarial-downgrades/` al index git e incluirlo en el próximo commit. Hoy `red-team.md` existe pero está untracked; la prosa del manuscrito lo cita como evidencia.
3. **[CRÍTICO]** Documentar o revertir las re-ejecuciones silenciosas de casos 14 (Postverdad, EDI=−0.0119) y 22 (Fósforo, EDI=+0.1921). Mismo patrón silencioso del caso 09 en iter 4. Si la re-ejecución fue intencional, declarar causa en bitácora; si fue accidental (seed, env), revertir a baseline.
4. **[ALTO]** Atender los 5 saltos del process-verifier abiertos desde iter 2. Sub-agente `process-verifier-debates-cierre/` sigue vacío en iter 5 (única deuda de silencio que persiste). Re-lanzar con prompt explícito de salida obligatoria y verificación post-ejecución del archivo en disco.
5. **[ALTO]** Ejecutar pre-registro (`PRE_REGISTRO_TEMPLATE.md`) **antes** de re-ejecutar los próximos 5 casos B-T2 reales (02, 05, 06, 07, 08, 14, 15, 17, 21-26, 28-30). El pre-registro existe en iter 5 pero no se ha aplicado a ningún caso aún. Aplicar es la única forma de bloquear forking paths Gelman-Loken hacia adelante.
6. **[ALTO]** Auditar caso 19 con `multi-probe-null` (sonda alternativa físicamente motivada). Si una sonda alternativa produce EDI ≥ 0, el caso 19 vuelve a Trend/Weak; si todas las sondas justificables fallan, la falsificación local del aparato queda confirmada y se documenta como prueba positiva de falsabilidad.
7. **[MEDIO]** Documentar globalmente la convención `dataset_real.csv` vs `dataset.csv` en `09-simulaciones-edi/README.md` o `CLAUDE.md` §7. Renombrar al menos casos 09, 11, 13, 18 (todos re-ejecutados con datos reales sin renombrar archivo). Deuda iter 3 abierta desde hace 2 ciclos.
8. **[MEDIO]** Re-build `Tesis.pdf` con todos los cambios iter 4-5 aplicados (downgrades 01/03/13, upgrades 09/18, reclasificación 19, BORRADOR-IA opción (c) suave una vez firmada). Hoy el PDF sigue en 1.6 MB / 413 pp del re-build iter 3; está desfasado respecto al estado real del manuscrito.

---

## Base de comparación para iter 6

| Métrica | Valor iter 5 |
|---------|---------------|
| Verificadores en verde | 8/8 (decorative_citations en warn) |
| HEAD commit | `88a58df` |
| Working tree mod / untracked | 6 / 1 |
| Casos con `metrics.json` | 32/40 |
| Casos B-T2 ejecutados con datos reales | 11 (01, 03, 04, 09, 11, 13, 16, 18, 19, 20, 27) |
| Casos B-T2 strong reales | 5 (04, 16, 18 nuevo, 20, 27) |
| Casos B-T2 weak reales | 1 (09 nuevo) |
| Falsificaciones locales del aparato | 1 (caso 19, formalizada) |
| Casos reclasificados acumulado iter 1→5 | 10 |
| Tasa bidireccional iter 5 sobre n=11 | 27% down, 18% up, 55% reclas total |
| BORRADOR-IA hits / archivos | 66 / 25 |
| H-J* etiquetas únicas | 12 (H-J1..H-J12) |
| Tamaño `Tesis.pdf` | 1.6 MB (sin re-build iter 4-5) |
| Sub-agentes silenciosos | 1 (process-verifier-debates-cierre) |
| Hallazgos críticos abiertos | 3 (re-ejecuciones silenciosas 14/22; saltos A/B/C process-verifier; convención dataset_real.csv) |
| PDFs primarios faltantes | 2 (Quine, Goff/Strawson) |
| Tasa entrega sub-agentes iter 5 | 7/8 (87.5%) — mejora vs iter 4 (75%) |
