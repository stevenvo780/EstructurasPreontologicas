# Anexo A.5. Mapa de aplicaciones

## Función

Mapa completo del paisaje de aplicaciones del marco. Cada caso aparece con su modo (demostrativo/programático), nivel de cierre operativo, criterio de elevación si procede, y referencias cruzadas.

---

## Resumen ejecutivo

**Total de casos:** 30 (29 corpus EDI original + 1 caso 30 behavioral dynamics).

**Distribución por modo:**

- **Modo demostrativo (con dossier completo):** 30 casos. Todos tienen dossier en `09-simulaciones-edi/<caso>/`.
- **Aplicaciones filosóficas programáticas adicionales:** 4 dominios sin caso EDI directo (capítulos 05-01 a 05-04).

**Distribución por Nivel:**

| Nivel | Categoría | N | Casos |
|:----:|-----------|:-:|-------|
| 4 | Strong (`overall_pass=True`) | 4 | Energía, Deforestación, Kessler, Riesgo Biológico |
| 4 | Strong sin gate completo | 1 | Microplásticos |
| 3 | Weak | 8 | Políticas, Postverdad, Urbanización, Fósforo, Wikipedia, Epidemiología, Movilidad, **Behavioral Dynamics (caso 30 v2)** |
| 2 | Suggestive | 2 | Finanzas, Salinización |
| 1 | Trend | 4 | Justicia, Starlink, Fuga cerebros, Clima |
| 0 | Null | 8 | Conciencia, Contaminación, Paradigmas, Océanos, Acidificación, Erosión, Acuíferos, IoT |
| — | Falsación rechazada (controles) | 3 | Exogeneidad, No-estacionariedad, Observabilidad |

**Total con señal significativa:** 15/30 (50%).
**Falsación correcta:** 3/3 (100%).

---

## Casos del corpus EDI

### Bloque I — Strong con gate completo (Nivel 4)

| # | Caso | EDI | p | Sonda | LoE | Datos |
|---|------|----:|--:|-------|----:|-------|
| 04 | Energía eléctrica | 0.6503 | 0.0000 | Lotka-Volterra | 4 | OPSD |
| 16 | Deforestación global ✓verificado | 0.5802 | 0.0000 | von Thünen | 4 | World Bank |
| 20 | Síndrome de Kessler | 0.3527 | 0.0000 | Densidad orbital | 3 | CelesTrak |
| 27 | Riesgo biológico (mortalidad) | 0.3326 | 0.0022 | Mortalidad | 3 | World Bank |

✓verificado = re-ejecutado en vivo en sesión 2026-04-27 con datos descargados, EDI=0.5802 vs ref 0.6020 (variabilidad <4%, mismo Nivel 4).

### Bloque II — Strong sin gate completo (Nivel 4*)

| # | Caso | EDI | p | Sonda | Por qué no gate |
|---|------|----:|--:|-------|-----------------|
| 24 | Microplásticos | 0.7819 | 0.0000 | Jambeck Accumulation | Bootstrap CI inestable |

### Bloque III — Weak (Nivel 3)

| # | Caso | EDI | p | Sonda |
|---|------|----:|--:|-------|
| 13 | Políticas estratégicas (gasto militar) | 0.2972 | 0.0015 | Saturation growth |
| **30** | **Behavioral Dynamics ✓v2** | **0.2622** | **0.0440** | **behavioral_attractor (segundo orden)** |
| 14 | Postverdad (desinformación) | 0.2428 | 0.0000 | SIS contagion |
| 18 | Urbanización | 0.2358 | 0.0000 | Logística + atracción |
| 22 | Fósforo (fertilizantes) | 0.1924 | 0.0000 | Carpenter P Cycle |
| 15 | Wikipedia (ediciones) | 0.1916 | 0.0000 | Saturation growth |
| 05 | Epidemiología (COVID-19) | 0.1294 | 0.0000 | SEIR |
| 11 | Movilidad (tráfico aéreo) | 0.1283 | 0.0020 | Bilinear diffusion |

✓v2 = construido en sesión 2026-04-27 con sonda mejorada de segundo orden. Avance desde Nivel 0 (v1) a Nivel 3 (v2).

### Bloque IV — Suggestive (Nivel 2)

| # | Caso | EDI | p |
|---|------|----:|--:|
| 09 | Finanzas globales | 0.0813 | 0.0000 |
| 21 | Salinización (irrigación) | 0.0184 | 0.0028 |

### Bloque V — Trend (Nivel 1)

| # | Caso | EDI | p | Comentario |
|---|------|----:|--:|------------|
| 10 | Justicia (Estado de Derecho) | 0.2274 | 0.4775 | Ventana corta |
| 26 | Starlink | 0.6892 | 1.0000 | val_steps=1 — exploratorio |
| 28 | Fuga de cerebros | 0.0249 | 0.9975 | Ruido domina |
| 01 | Clima regional | 0.0111 | 0.9990 | Sonda Budyko-Sellers insuficiente |

### Bloque VI — Null (Nivel 0)

| # | Caso | EDI | Comentario |
|---|------|----:|-----------|
| 02 | Conciencia global | -0.1165 | Datos especulativos LoE=1 |
| 03 | Contaminación PM2.5 | -0.0038 | Sin estructura macro |
| 12 | Paradigmas (ciencia) | -0.0060 | Reflexividad |
| 17 | Océanos (temperatura) | -0.0154 | Sin sonda específica |
| 19 | Acidificación oceánica | -0.0002 | Proxy débil |
| 23 | Erosión dialéctica | -1.0000 | Categoría mal definida |
| 25 | Acuíferos | -0.1462 | Datos heterogéneos |
| 29 | IoT | -0.8760 | Reflexividad técnica |

### Bloque VII — Controles de falsación (correctamente rechazados)

| # | Caso | EDI | p | Diseño |
|---|------|----:|--:|--------|
| 06 | Falsación de exogeneidad | 0.0551 | 1.0000 | Ruido puro |
| 07 | Falsación de no-estacionariedad | -0.8819 | 1.0000 | Random walk |
| 08 | Falsación de observabilidad | -1.0000 | 1.0000 | Estado oculto |

**3/3 controles correctamente rechazados** — aparato discrimina genuinamente, no es máquina de validar arbitrariamente.

---

## Aplicaciones filosóficas programáticas (sin caso EDI directo)

### Capítulo 05-01 — Mente, memoria, yo

**Estado:** modo programático.

**Conjetura central:** las categorías mentales son atractores de integración multivariable en sistemas acoplados organismo-entorno-tarea-historia.

**Criterio de elevación:** construir tareas cognitivas con datos cuantitativos donde atractores conductuales discriminen contra cognitivismo simbólico.

**Caso 30 (behavioral dynamics, Nivel 3 weak)** es el primer paso de elevación parcial: muestra que el aparato detecta cierre operativo significativo en behavioral dynamics, aun sin alcanzar Nivel 4.

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

### 1. La termodinámica manda

Los 4 casos `overall_pass=True` están conectados con dinámicas físicas o termodinámicas robustas. Cuanto más anclado físicamente, más robusto el cierre operativo.

### 2. La paradoja del LoE

LoE alto no garantiza EDI alto (Clima: LoE=5, EDI=0.011). Sondas inadecuadas producen EDI bajos incluso con datos excelentes. **Sondas, no datos, son cuello de botella en algunos casos.**

### 3. La importancia del val_steps

Ventanas largas → estadística robusta pero EDI moderados. Ventanas cortas → EDI altos posibles pero requieren cautela. Ventana de 1 (Starlink) = exploratorio, no confirmatorio.

### 4. El éxito de la falsación

3/3 controles rechazados. Refuta la objeción de tautología. Si la ablación fuera trivialmente destructiva, los controles también producirían EDI alto, pero no lo hacen.

### 5. Behavioral dynamics como caso bisagra

El caso 30 v2 (Nivel 3 weak) conecta el corpus EDI macro-temporal con el caso ancla cualitativo de Warren. **El aparato funciona en escala behavioral**, produciendo señal genuina con discriminación pública contra nulos.

---

## Lectura cruzada

- Caso ancla canónico cualitativo: capítulo 05-05
- Aplicaciones programáticas filosóficas: capítulos 05-01 a 05-04
- Caso 30 detallado: `09-simulaciones-edi/30_caso_behavioral_dynamics/README.md`
- Cada caso del corpus: `09-simulaciones-edi/<caso>/README.md`
- Resultados consolidados: `09-simulaciones-edi/README.md`
- Verificación de reproducibilidad: `Procesos/2026-04-27-integracion-jacob/02-verificacion-reproducibilidad.md`
