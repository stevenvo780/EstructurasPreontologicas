# Mapa de aplicaciones — corpus inter-dominio e inter-escala

## Función

Mapa del alcance empírico del programa: 30 casos inter-dominio y 10 inter-escala. El capítulo distingue resultados técnicos crudos, clasificaciones históricas y estatus inferencial bajo el régimen estricto B-T2.1. Un caso ejecutado prueba que el aparato puede formularse en ese dominio; no prueba por ese solo hecho que los cuatro invariantes propuestos existan allí ni que la ontología sea general.

> **Nota global de versionado.** Las clasificaciones reflejan el estado del corpus tras re-validación consolidada. Histórico de evolución archivado internamente y disponible bajo solicitud.
>
> **Régimen reportado en este capítulo.** La clasificación histórica pre-B-T2.1 se conserva solo como trazabilidad. El estatus defendible exige pre-registro ex ante, datos refrescados, detrend, block-permutation y comparación rival. Ese régimen todavía no cubre los 30 casos; por ello este capítulo no presenta la distribución cruda de `metrics.json` como distribución final de evidencia.

---

## Resumen ejecutivo

**Total de casos:** 40 (30 inter-dominio + 10 inter-escala). La cobertura indica dónde se ejecutó el aparato, no cuántos dominios corroboran la ontología.

### Corpus inter-dominio (30 casos)

**Distribución por modo:**

- **Modo técnico-ejecutado** (dossier EDI completo, `metrics.json` reproducible bajo el protocolo C1-C5): 30 casos. Todos tienen dossier en `09-simulaciones-edi/<caso>/`.
- **Modo demostrativo en sentido estricto** (14/14 componentes): 0 casos cerrados. Warren funciona como ancla paradigmática con 9/14 componentes sustantivos y deudas explícitas.
- **Aplicaciones filosóficas programáticas adicionales:** 4 dominios sin caso EDI directo (capítulos 05-01 a 05-04).

*Nota sobre el modo técnico-ejecutado.* 'Dossier técnico completo' indica que el caso fue corrido con el protocolo C1-C5 y produce `metrics.json` reproducible. No equivale a demostración positiva. Tampoco basta una categoría cruda Strong: el régimen B-T2.1 mostró que detrend, block-permutation y datos refrescados pueden degradar o invertir esa clasificación.

**Estatus inferencial vigente:**

**Tabla A.5.1.**

**Tabla 5.7.1.**

| Estatus | N | Casos o alcance |
|---------|--:|-----------------|
| Strong robusto puro confirmado bajo régimen estricto | 0 | Ninguno |
| Weak validado bajo B-T2.1 ex ante | 1 | Energía (04) |
| Candidato pendiente de cierre estricto | 1 | Starlink (26) |
| Falsificación local del aparato | 4 | Acidificación (19), Kessler (20), Erosión (23), Microplásticos (24) |
| Controles negativos rechazados | 3 | Exogeneidad (06), No-estacionariedad (07), Observabilidad (08) |
| Sin estatus estricto cerrado | 21 | Requieren cierre B-T2.1 caso por caso; no se agregan como positivos ni como nulls definitivos |

La tabla no suma categorías crudas, porque el mismo criterio no fue ejecutado en todos los casos. Reportar 19/30 con señal significativa mezclaría ventanas, pruebas de permutación y versiones del aparato incompatibles. El resultado agregado se mantiene abierto hasta terminar B-T2.1.

### Corpus inter-escala (10 casos)

**Tabla A.5.2.**

**Tabla 5.7.2.**

| Nivel | Categoría | N | Casos (escala instanciada) |
|:----:|-----------|:-:|----------------------------|
| 4 | Strong crudo (`overall_pass=True`) | 7 | 31 Decoherencia (cuántica), 32 Espín-órbita (atómica), 34 Michaelis-Menten (bioquímica), 36 NF-κB (celular oscilatoria), 37 HRV (individual), 39 Cefeida (astrofísica), 40 Cúmulo globular (astrofísica masiva) |
| 3 | Weak | 1 | 35 Ciclo celular (celular) |
| 0 | Null honesto | 1 | 33 Villin Headpiece (sonda equilibrio inadecuada) |
| 0 | Failure mode | 1 | 38 Locomoción τ-dot (sonda mal especificada para reinicios discretos) |

**Cobertura nominal de escalas:** 30 órdenes de magnitud espaciales (10⁻¹⁰ m → 10²⁰ m), 30 órdenes temporales (10⁻¹⁵ s → 10¹⁴ s). Los casos usan parámetros publicados pero datos parcial o totalmente sintéticos. Demuestran portabilidad computacional del esquema, no invariancia ontológica ni validez empírica en treinta órdenes de magnitud.

### Lectura integrada y límite inferencial

El corpus agregado prueba que un vocabulario común puede formularse y ejecutarse en dominios heterogéneos. No autoriza a inferir, por conteo de aplicaciones, que todos los casos instancien una estructura ontológica única. Esa generalización permanece como hipótesis filosófica H-J2: necesita, además de traducción nominal, medición independiente, convergencia entre sondas y replicación externa.

---

## Casos del corpus EDI

### Bloque I — Strong con gate completo (Nivel 4) — reconciliación canónica ↔ B-T2.1

**Tabla A.5.3.**

**Tabla 5.7.3.** Casos históricamente clasificados como *Strong con gate completo* bajo el régimen canónico (pre-B-T2.1, sin block-permutation ni detrend honesto, en algunos casos con ventana sintética o histórica), reconciliados con la clasificación post-B-T2.1 genuino (block-permutation con `ℓ ∝ n^{1/3}` Politis & White 2004 + detrend honesto + pre-registro firmado *ex ante* del fetch de datos). La cifra autoritativa para la conclusión del manuscrito es la de la columna post-B-T2.1 (cf. cap 06-01 §1 Tabla 6.1.1).

| # | Caso | Canónica pre-B-T2.1 (EDI raw, p, sonda, LoE) | Post-B-T2.1 genuino (cifras reales `metrics.json` real-phase) | Reclasificación |
|---|------|---|---|---|
| 04 | Energía eléctrica | EDI=0.6503, p=0.0000, Lotka-Volterra, LoE=4, datos OPSD | EDI=0.1571, p_block=0.006, CI=[0.133, 0.193], `overall_pass=false`, `detrended_edi=null` (sin tendencia residual material), sonda Lotka-Volterra, datos OPSD | **Weak validado por pre-registro B-T2.1 genuino** (block-perm significativa; magnitud reducida tras corrección del aparato). Cf. cap 06-01 Tabla 6.1.1 fila "Weak validado bajo B-T2.1". |
| 16 | Deforestación global | EDI=0.5802, p=0.0000, von Thünen, LoE=4, World Bank | EDI=0.5802, p_perm=0.0 (método `iid`), CI=[0.423, 0.709], `overall_pass=false`, `trend_ok=false`, `detrended_edi=-0.0438`, `trend_r2=0.785`, `trend_ratio=-0.075`, `warning=true` | **Weak por sesgo de tendencia (Fix M4/M5 2026-09-28)**: magnitud raw dominada por tendencia; sin gate completo. Pendiente B-T2.1 genuino con block-perm para cierre estricto. Cf. cap 06-01 §3 (qué no queda demostrado). |
| 20 | Síndrome de Kessler | EDI=0.3527, p=0.0000, Densidad orbital, LoE=3, CelesTrak | EDI=-1.000, p_perm=1.0 (método `block`), CI=[-12.27, -6.01], `overall_pass=false`, `permutation_significant=false`, sonda densidad orbital, CelesTrak | **Falsificación local del aparato** bajo régimen post-B-T2.1 (sonda densidad orbital no captura la dinámica acoplada en la ventana real evaluada; CI bootstrap excluye cero por la izquierda). Cf. cap 06-01 Tabla 6.1.1 fila "Falsificación local del aparato". |
| 27 | Riesgo biológico (mortalidad) | EDI=0.3326, p=0.0022, Mortalidad, LoE=3, World Bank | EDI=0.2160, p_perm=0.956 (método `iid`), `permutation_significant=false`, CI=[-20.05, 0.32], `overall_pass=false`, sonda mortalidad, World Bank | **Sin significancia permutacional bajo régimen real-phase actual**: el ranking canónico cae cuando se cierra el cómputo de p_perm sobre la ventana real con `iid` sin block-perm calibrada. Pendiente B-T2.1 genuino con block-perm explícita. Cf. cap 06-01 §3; baselines ARIMA/VAR del reporte histórico-sintético superaban al acoplado en val_len=8 (pendiente re-ejecución sobre arrays reales). |
| 18 | Urbanización global | EDI=0.3366, p=0.0000, Logística + atracción, LoE=4, World Bank (SP.URB.TOTL.IN.ZS) | EDI=0.3366, p_perm=0.0 (método `iid`), CI=[0.330, 0.347], `overall_pass=false`, `trend_ok=false`, `detrended_edi=0.0722`, `trend_r2=0.997`, `trend_ratio=0.214`, `warning=true` | **Weak por sesgo de tendencia (Fix M4/M5 2026-09-28)**: `trend_r2=0.997`, detrended EDI 0.0722; sin gate completo. Pendiente B-T2.1 genuino con block-perm y pre-registro firmado *ex ante*. |
| 24 | Microplásticos oceánicos | EDI=0.8057, p=0.0000, Jambeck Accumulation-Decay, LoE=4, Jambeck et al. (fase histórica) | EDI=-1.000, p_perm=1.0 (método `block`), CI=[-3.05, -2.34], `overall_pass=false`, `permutation_significant=false`, `detrended_edi=0.3254`, `trend_r2=0.998`, sonda Jambeck Accumulation-Decay, ventana 2000-2019 refrescada | **Falsificación local del aparato**: el último Strong robusto previamente declarado colapsó al refrescar la ventana de validación bajo pre-registro genuino. Cf. cap 06-01 Tabla 6.1.1 fila "Falsificación local del aparato" y §1.1 sobre auto-corrección bajo B-T2.1 genuino. |
| 30 | Behavioral Dynamics | EDI=0.6143, p=0.0000, Behavioral attractor, LoE=3, Google Mobility real | EDI=0.2622, p_perm=0.044 (método `iid`), CI=[0.249, 0.280], `overall_pass=false`, `detrended_edi=null`, sonda Fajen-Warren behavioral attractor, Google Mobility real | **Sub-Strong bajo régimen real-phase** (p_perm apenas <0.05 sin block-perm; magnitud baja). Cf. cap 06-01 §1.3 (el dominio conductual queda como piloto y agenda prospectiva, no demostración). |
| 21 | Salinización (FAOSTAT enhanced) | EDI=0.5152, p=0.0010, Richards bilineal, LoE=3, FAOSTAT enhanced | EDI=0.5152, p_perm=0.0 (método `iid`), CI=[0.337, 0.668], `overall_pass=false`, `trend_ok=false`, `detrended_edi=0.0007`, `trend_r2=0.893`, `trend_ratio=0.001`, `warning=true` | **Weak por sesgo de tendencia (Fix M4/M5 2026-09-28)**: detrended EDI trivial (`0.0007`); sin gate completo. Pendiente B-T2.1 genuino con block-perm y pre-registro firmado *ex ante*. |

**Reproducibilidad.** Cada cifra de la columna post-B-T2.1 se regenera con `python3 09-simulaciones-edi/<NN>_caso_<nombre>/src/validate.py` (semillas fijas en código; sin flags) y queda registrada en `outputs/metrics.json` bajo la rama `phases.real`, con `config_file` indicando el régimen. Caso 04 exige `CASE_CONFIG_JSON=case_config_b_t2_1.json` (régimen estricto; el config canónico da otro experimento). La columna canónica corresponde a la clasificación histórica (régimen sintético + `iid` sin block-permutation, anterior al fix del bug `detrended_edi` y a la activación de block-permutation en `common/hybrid_validator.py:1810-1843`); el archivo histórico de reclasificaciones se conserva en el repositorio interno del proyecto.

**Conteo agregado post-B-T2.1 del Bloque I histórico (actualizado Fix M4/M5 2026-09-28).** De los 8 casos originalmente listados como *Strong con gate completo*: 0 sobreviven como Strong robusto puro; 1 baja a Weak validado por pre-registro genuino (04 Energía); 3 caen a Weak por sesgo de tendencia (16, 18, 21; `trend_ok=false`); 1 queda como piloto sub-Strong (30); 1 cae sin significancia permutacional (27); y 2 se reclasifican como falsificación local del aparato (20, 24). (El caso 22, fuera de este bloque histórico, también cayó a Weak por `trend_ok=false`.) La auto-corrección prueba auditabilidad del procedimiento. No confirma por sí misma la tesis ontológica.

### Bloque II — Candidato sin gate completo

**Tabla A.5.4.**

**Tabla 5.7.4.**

| # | Caso | EDI | p_block | Sonda | Por qué no gate |
|---|------|----:|--:|-------|-----------------|
| 26 | Constelaciones satelitales Starlink | 0.7575 | 0.0790 | Saturation Growth | `overall_pass=False`; C4 y significancia por block-permutation no superados. CI bootstrap [0.741, 0.775], val_steps=30. Es candidato, no Strong. |

### Bloque III — Weak (Nivel 3)

**Tabla A.5.5.**

**Tabla 5.7.5.**

| # | Caso | EDI | p | Sonda |
|---|------|----:|--:|-------|
| 04 | Energía eléctrica | 0.1571 | 0.0060 (block) | Lotka-Volterra |
| 14 | Postverdad (desinformación) | 0.2428 | 0.0000 | SIS contagion |
| 17 | Océanos (OHC proxy) | 0.1902 | 0.0000 | Sonda térmica (disclosure: `valid=False`, gate C1-C5 no superado pero CI=[0.157, 0.280] estrictamente positivo) |
| 22 | Fósforo (fertilizantes) | 0.1924 | 0.0000 | Carpenter P Cycle |
| 05 | Epidemiología (COVID-19) | 0.1294 | 0.0000 | SEIR |

### Bloque IV — Suggestive (Nivel 2)

**Tabla A.5.6.**

**Tabla 5.7.6.**

| # | Caso | EDI | p_perm | CI 95 % bootstrap | Comentario |
|---|------|----:|--:|---|---|
| 10 | Justicia (Estado de Derecho) | 0.0579 | 0.0170 | [-0.151, +0.345] | Suggestive porque p<0.05 con magnitud baja y CI cruza cero (datos World Bank Rule-of-Law `RL.EST` 10 economías top 1996–2023, val_steps=11). |

**Costo de admisión declarado.** La regla `CI 95 % no cruza cero` opera como criterio adicional al ranking permutacional. La coexistencia de `p<0.01` con magnitud trivial y CI cruzando cero no debe contar como evidencia positiva, conforme a Wasserstein y Lazar (2016, *The American Statistician* 70(2):129-133, ASA Statement on p-values, Principle 3 — verbatim en `07-bibliografia/Wasserstein-Lazar - ASA Statement on p-values (Am Stat 2016).pdf` p. 2): *"Scientific conclusions and business or policy decisions should not be based only on whether a p-value passes a specific threshold."* La auditoría retrospectiva de casos contabilizados bajo este criterio queda como deuda residual fechada (cf. cap 03 §criterios de admisión).

### Bloque V — Trend (Nivel 1)

**Tabla A.5.7.**

**Tabla 5.7.7.**

| # | Caso | EDI | p | Comentario |
|---|------|----:|--:|------------|
| 13 | Políticas estratégicas (gasto militar) | 0.0821 | 0.1622 | Trend Nivel 1 bajo datos institucionales reales; CI=[0.065, 0.100]. Ruido domina señal. |
| 11 | Movilidad (tráfico aéreo / TomTom) | 0.0599 | 0.9219 | Trend Nivel 1 bajo datos TomTom reales; CI=[-0.392, 0.205]. Ruido domina señal de cierre bajo sonda Bilinear diffusion. |

### Bloque VI — Null (Nivel 0)

**Tabla A.5.8.**

**Tabla 5.7.8.**

| # | Caso | EDI | Comentario |
|---|------|----:|-----------|
| 01 | Clima regional | -0.0007 | Null genuino bajo datos reales IPCC-calibrados (p_perm=0.998, sonda Budyko-Sellers). |
| 02 | Conciencia global | -0.0121 | Null genuino bajo datos reales (p_perm=0.315, CI=[-0.016, -0.010]; sonda dinámica colectiva). Consistente con LoE=1 especulativa. |
| 03 | Contaminación PM2.5 | -0.0109 | Null genuino bajo datos World Bank PM2.5 reales (p_perm=0.616, sonda dispersión-decaimiento). |
| 09 | Finanzas globales | -0.0020 | Null/artefacto bajo régimen detrended honesto (raw=+0.1027 con `trend_r2=0.979`, warning activo). |
| 12 | Paradigmas (ciencia) | -0.1536 | Reflexividad; null bajo régimen real-phase actual. |
| 25 | Acuíferos | -0.1462 | Datos heterogéneos. |
| 29 | IoT | -0.8760 | Reflexividad técnica. |
| 15 | Wikipedia (atención colectiva — "Climate change" EN) | -0.0038 | Null genuino bajo datos Wikimedia pageviews mensuales 2015–2024 (p_perm=0.769, CI=[-0.023, -0.002]). Magnitud trivial domina (`\|EDI\|<0.05`). |
| 28 | Fuga de cerebros (multi-driver WB) | 0.0298 | Null genuino bajo datos WB multi-driver (researchers, enrollment, remittances, GDP pc, net migration; p_perm=0.969, CI=[-0.095, +0.159], val_steps=18). Candidato a panel bilateral origen-destino para próxima ejecución. |

Convención para Bloque VI: `\|EDI\|<0.05` y `p_perm>0.05` cubren los nulls clásicos; el caso 15 con `p_perm>0.05` y CI bootstrap [-0.023, -0.002] que excluye cero por la izquierda con magnitud trivial se declara Null genuino porque la magnitud trivial domina sobre la exclusión bootstrap marginal.

### Bloque VI.5 — Falsificación local del aparato (sonda inadecuada con CI que excluye cero por la izquierda)

**Tabla 5.7.8b.**

| # | Caso | EDI | CI bootstrap | Comentario |
|---|------|----:|--------------|-----------|
| 19 | Acidificación oceánica | -0.0047 | [-0.0054, -0.0041] | Falsificación local del aparato: el bootstrap del EDI **excluye cero por la izquierda**, indicando que el modelo acoplado predice estrictamente peor que el reducido en held-out. La inadecuación es de la **sonda Revelle/calcificadores para la serie Aloha pH**, no del dato; conforme a ASA Wasserstein-Lazar 2016 principio 5, el resultado se reporta como información sobre el aparato y no como ausencia de fenómeno. **Caveat de datos:** `data/dataset.csv` PMEL/NOAA no estaba versionado; proxy calibrado a estadísticas del run original. Reproducción bit-a-bit requiere fetch del CSV NOAA real. Comando regenerador: `python3 09-simulaciones-edi/19_caso_acidificacion_oceanica/src/validate.py`. |
| 23 | Erosión dialéctica | -1.0000 | [-3.336, -1.008] | Falsificación local del aparato con pre-registro firmado VALIDADO EXACTO (`09-simulaciones-edi/23_caso_erosion_dialectica/docs/PRE_REGISTRO.md`): predicción EDI=-1.0 ±0.30 → observado EDI=-1.000 EXACTO, p_perm=1.0, CI bootstrap [-3.336, -1.008] que excluye cero por la izquierda. La sonda Abrams-Strogatz `prestige_competition` no es físicamente apropiada para la serie real propuesta (modela competencia entre dos lenguas en sustrato fijo; aplicar a "erosión dialéctica" sin variable observable con dos competidores claros produce mismatch sistemático). El aparato declara honestamente la inadecuación local ex ante en el pre-registro y la confirma bit-a-bit en la ejecución; ASA Wasserstein-Lazar 2016 principio 5. La falsificación local confirmada es fortaleza: el pre-registro firmado bloquea operativamente el forking path de defenderla post-hoc como "categoría mal definida". Comando regenerador: `python3 09-simulaciones-edi/23_caso_erosion_dialectica/src/validate.py --seed 42`. |

### Bloque VII — Controles de falsación (correctamente rechazados)

**Tabla A.5.9.**

**Tabla 5.7.9.**

| # | Caso | EDI | p | Diseño |
|---|------|----:|--:|--------|
| 06 | Falsación de exogeneidad | 0.0551 | 1.0000 | Ruido puro |
| 07 | Falsación de no-estacionariedad | -0.8819 | 1.0000 | Random walk |
| 08 | Falsación de observabilidad | -1.0000 | 1.0000 | Estado oculto |

**3/3 controles correctamente rechazados.** Este resultado debilita la objeción más simple de que el aparato valida cualquier entrada, pero no basta para demostrar discriminación general: los controles cubren una familia limitada de nulos y deben ampliarse con rivales estructurados.

---

## Aplicaciones filosóficas programáticas (sin caso EDI directo)

### Capítulo 05-01 — Mente, memoria, yo

**Estado:** modo programático **sin caso EDI ejecutado ni candidato del corpus**.

**Conjetura central:** las categorías mentales (memoria, atención, decisión, conciencia perceptiva) son **atractores de integración multivariable** en sistemas acoplados organismo–entorno–tarea–historia. Esta es conjetura programática, no resultado empírico de este manuscrito.

**Criterio de elevación:** construir tareas cognitivas con datos cuantitativos públicos donde atractores conductuales discriminen contra cognitivismo simbólico. El corpus actual **no incluye tal caso**. El caso 30 (behavioral dynamics, EDI = 0.2622, `overall_pass=false`) opera en coordinación motora, no en cognición simbólica. Además, el control con block bootstrap estima p ≈ 0.978 y muestra circularidad parcial de la sonda; por ello se conserva como piloto metodológico, no como demostración ni elevación parcial de este capítulo.

**Deuda residual fechada:** identificar caso público con datos de tarea cognitiva (decisión bajo incertidumbre, memoria de trabajo, atención sostenida) susceptible de modelado dinámico acoplado, ejecutarlo con `validate.py` y reportar EDI con significancia bootstrap. Hasta entonces, el capítulo 05-01 permanece como conjetura programática declarada.

### Capítulo 05-02 — Biología y ecología

**Estado:** modo programático.

**Conjetura central:** los fenómenos vivos son patrones operativos materialmente sostenidos con cierre dinámico verificable.

**Criterio de elevación:** adoptar caso publicado de regime shift ecológico (Scheffer y colegas) con bifurcación documentada y construir dossier completo.

**Casos del corpus que ya cubren parcialmente:** 16 Deforestación, 22 Fósforo, 21 Salinización, 19 Acidificación oceánica.

### Capítulo 05-03 — Sistemas técnicos distribuidos

**Estado:** modo programático.

**Conjetura central:** los sistemas distribuidos son patrones técnicos modelables como pares acoplados con dinámica de fallo.

**Criterio de elevación:** trace público de incidente con modelo dinámico cuantitativo y predicción de cascada.

**Casos del corpus relevantes:** 20 Kessler, 26 Starlink (overhead técnico).

### Capítulo 05-04 — Instituciones, mercado, Estado

**Estado:** modo programático.

**Conjetura central:** las instituciones son patrones materialmente sostenidos por prácticas, normas, soportes; los mercados son redes dinámicas; el Estado es organización material-normativa.

**Criterio de elevación:** transición de régimen político o crisis institucional con datos cuantitativos publicados.

**Casos del corpus relevantes:** 13 Políticas, 09 Finanzas, 14 Postverdad.

---

## Patrones transversales

### 1. El anclaje físico no basta

Varios casos con motivación física obtuvieron categorías altas bajo el régimen histórico y colapsaron al refrescar datos, retirar tendencia o introducir block-permutation. Kessler y Microplásticos son los ejemplos decisivos. El anclaje físico orienta la construcción de la sonda, pero la robustez depende de datos, ventana, baseline y validación fuera de muestra.

### 2. La paradoja del LoE

LoE alto no garantiza EDI alto (Clima: LoE=5, EDI≈0). Sondas inadecuadas producen EDI bajos incluso con datos excelentes. **Sondas, no datos, son cuello de botella en algunos casos.**

### 3. La importancia del val_steps

Ventanas largas → estadística robusta pero EDI moderados. Ventanas cortas → EDI altos posibles pero requieren cautela. Ventana de 1 = exploratorio, no confirmatorio.

### 4. El éxito de la falsación

3/3 controles rechazados. El resultado debilita la objeción de tautología trivial, pero no la refuta de manera general. Harían falta controles negativos más diversos y rivales estructurados evaluados con el mismo presupuesto de ajuste.

### 5. Behavioral dynamics como límite metodológico

El caso 30 no demuestra cierre operativo específico en escala conductual. Su EDI real es 0.2622, no supera el gate completo y la prueba de circularidad con block bootstrap no es significativa. El ajuste de Warren (r² = 0.980) describe un resultado experimental publicado distinto; no puede usarse como validación del EDI del caso 30. Juntos delimitan una agenda de prueba, no una demostración acumulativa.

---

## Deuda residual

(Deuda declarada el 2026-05-11 — fecha del commit que introdujo esta sección.)


- **Limitación 1.** El Bloque VI (Null, Nivel 0) agrega casos heterogéneos que requieren distinguir tres regímenes operativamente distintos: (i) nulls genuinos (EDI ≈ 0, p > 0.05), (ii) caso con EDI fuertemente negativo (degradación bajo acoplamiento), (iii) casos rechazados por gate C1-C5 antes del cómputo de EDI. La subdivisión vigente en bloques 0a / 0b / 0c / 0d (más Bloque VI.5 de falsificación local) atiende esa distinción; el conteo agregado preserva el total pero hace visible la diferencia operativa entre "el aparato no detecta señal" vs "el aparato detecta degradación" vs "el aparato rechaza antes de calcular". Paralela en `06-cierre/01-conclusion-demostrativa.md` §4.1 y `06-cierre/_extendido/versiones-cortas-defensa.md`.

## Lectura cruzada

- Caso ancla canónico cualitativo: capítulo 05-05
- Aplicaciones programáticas filosóficas: capítulos 05-01 a 05-04
- Caso 30 detallado: `09-simulaciones-edi/30_caso_behavioral_dynamics/README.md`
- Cada caso del corpus: `09-simulaciones-edi/<caso>/README.md`
- Resultados consolidados: `09-simulaciones-edi/README.md`
- Verificación de reproducibilidad y histórico de reclasificaciones del corpus: archivados internamente y disponibles bajo solicitud.
