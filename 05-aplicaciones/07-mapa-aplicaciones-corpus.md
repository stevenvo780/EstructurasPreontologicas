# Mapa de aplicaciones — corpus inter-dominio e inter-escala

## Función

Mapa completo del paisaje de aplicaciones del marco como **ontología general multiescalar**. Cada caso aparece con su modo (demostrativo/programático), nivel de cierre operativo, escala instanciada, criterio de elevación si procede, y referencias cruzadas. El paisaje agrega 40 casos: 30 inter-dominio + 10 inter-escala. Cada caso es **instancia particular de los cuatro invariantes ontológicos** (sustrato material, acoplamiento dinámico, atractor empírico, cierre operativo κ); ningún caso es aplicación aislada del aparato a un dominio.

---

## Resumen ejecutivo

**Total de casos:** 40 (30 corpus inter-dominio + 10 corpus inter-escala). Cobertura conjunta: 8 escalas físicas/biológicas/cosmológicas + 7 dominios disciplinares heterogéneos.

### Corpus inter-dominio (30 casos)

**Distribución por modo:**

- **Modo demostrativo (con dossier completo):** 30 casos. Todos tienen dossier en `09-simulaciones-edi/<caso>/`.
- **Aplicaciones filosóficas programáticas adicionales:** 4 dominios sin caso EDI directo (capítulos 05-01 a 05-04).

**Distribución por Nivel:**

**Tabla A.5.1.**

| Nivel | Categoría | N | Casos |
|:----:|-----------|:-:|-------|
| 4 | Strong (`overall_pass=True`) | 4 | Energía, Deforestación, Kessler, Riesgo Biológico |
| 4 | Strong sin gate completo | 1 | Microplásticos |
| 3 | Weak | 8 | Políticas, Postverdad, Urbanización, Fósforo, Wikipedia, Epidemiología, Movilidad, Behavioral Dynamics (caso 30) |
| 2 | Suggestive | 2 | Finanzas, Salinización |
| 1 | Trend | 4 | Justicia, Starlink, Fuga cerebros, Clima |
| 0 | Null | 8 | Conciencia, Contaminación, Paradigmas, Océanos, Acidificación, Erosión, Acuíferos, IoT |
| — | Falsación rechazada (controles) | 3 | Exogeneidad, No-estacionariedad, Observabilidad |

**Total con señal significativa:** 15/30 (50%).
**Falsación correcta:** 3/3 (100%).

### Corpus inter-escala (10 casos)

**Tabla A.5.2.**

| Nivel | Categoría | N | Casos (escala instanciada) |
|:----:|-----------|:-:|----------------------------|
| 4 | Strong (`overall_pass=True`) | 7 | 31 Decoherencia (cuántica), 32 Espín-órbita (atómica), 34 Michaelis-Menten (bioquímica), 36 NF-κB (celular oscilatoria), 37 HRV (individual), 39 Cefeida (astrofísica), 40 Cúmulo globular (astrofísica masiva) |
| 3 | Weak | 1 | 35 Ciclo celular (celular) |
| 0 | Null honesto | 1 | 33 Villin Headpiece (sonda equilibrio inadecuada) |
| 0 | Failure mode | 1 | 38 Locomoción τ-dot (sonda mal especificada para reinicios discretos) |

**Cobertura de escalas:** 30 órdenes de magnitud espaciales (10⁻¹⁰ m → 10²⁰ m), 30 órdenes temporales (10⁻¹⁵ s → 10¹⁴ s).

### Lectura ontológica integrada

Los 40 casos del corpus agregado **no son aplicaciones independientes**: cada uno es **instancia de los cuatro invariantes ontológicos** que la tesis afirma. Lo que cambia entre casos es el dominio sustantivo y la escala física donde los invariantes se materializan; la **estructura ontológica subyacente es una sola**. Esto es lo que la tesis llama *"ontología general multiescalar"*: una arquitectura común que se instancia diferenciadamente.

---

## Casos del corpus EDI

### Bloque I — Strong con gate completo (Nivel 4)

**Tabla A.5.3.**

| # | Caso | EDI | p | Sonda | LoE | Datos |
|---|------|----:|--:|-------|----:|-------|
| 04 | Energía eléctrica | 0.6503 | 0.0000 | Lotka-Volterra | 4 | OPSD |
| 16 | Deforestación global | 0.5802 | 0.0000 | von Thünen | 4 | World Bank |
| 20 | Síndrome de Kessler | 0.3527 | 0.0000 | Densidad orbital | 3 | CelesTrak |
| 27 | Riesgo biológico (mortalidad) | 0.3326 | 0.0022 | Mortalidad | 3 | World Bank |

Reproducibilidad: el caso 16 ha sido re-ejecutado con datos World Bank descargados en vivo (variabilidad estocástica <4%, mismo Nivel 4 strong). La trazabilidad detallada está en `Bitacora/`.

### Bloque II — Strong sin gate completo (Nivel 4*)

**Tabla A.5.4.**

| # | Caso | EDI | p | Sonda | Por qué no gate |
|---|------|----:|--:|-------|-----------------|
| 24 | Microplásticos | 0.7819 | 0.0000 | Jambeck Accumulation | Bootstrap CI inestable |

### Bloque III — Weak (Nivel 3)

**Tabla A.5.5.**

| # | Caso | EDI | p | Sonda |
|---|------|----:|--:|-------|
| 13 | Políticas estratégicas (gasto militar) | 0.2972 | 0.0015 | Saturation growth |
| 30 | Behavioral Dynamics | 0.2622 | 0.0440 | behavioral_attractor (segundo orden) |
| 14 | Postverdad (desinformación) | 0.2428 | 0.0000 | SIS contagion |
| 18 | Urbanización | 0.2358 | 0.0000 | Logística + atracción |
| 22 | Fósforo (fertilizantes) | 0.1924 | 0.0000 | Carpenter P Cycle |
| 15 | Wikipedia (ediciones) | 0.1916 | 0.0000 | Saturation growth |
| 05 | Epidemiología (COVID-19) | 0.1294 | 0.0000 | SEIR |
| 11 | Movilidad (tráfico aéreo) | 0.1283 | 0.0020 | Bilinear diffusion |

### Bloque IV — Suggestive (Nivel 2)

**Tabla A.5.6.**

| # | Caso | EDI | p |
|---|------|----:|--:|
| 09 | Finanzas globales | 0.0813 | 0.0000 |
| 21 | Salinización (irrigación) | 0.0184 | 0.0028 |

### Bloque V — Trend (Nivel 1)

**Tabla A.5.7.**

| # | Caso | EDI | p | Comentario |
|---|------|----:|--:|------------|
| 10 | Justicia (Estado de Derecho) | 0.2274 | 0.4775 | Ventana corta |
| 26 | Starlink | 0.6892 | 1.0000 | val_steps=1 — exploratorio |
| 28 | Fuga de cerebros | 0.0249 | 0.9975 | Ruido domina |
| 01 | Clima regional | 0.0111 | 0.9990 | Sonda Budyko-Sellers insuficiente |

### Bloque VI — Null (Nivel 0)

**Tabla A.5.8.**

| # | Caso | EDI | Comentario |
|---|------|----:|-----------|
| 02 | Conciencia global | -0.1165 | Datos especulativos LoE=1 |
| 03 | Contaminación PM2.5 | -0.0901 | Sin estructura macro detectable bajo régimen real-phase actual |
| 12 | Paradigmas (ciencia) | -0.1536 | Reflexividad; null bajo régimen real-phase actual |
| 17 | Océanos (temperatura) | -0.0154 | Sin sonda específica |
| 19 | Acidificación oceánica | 0.7278 | EDI elevado pero p=0.49 (no significativo); promovido a Nivel 1\* trend con cautela inferencial — candidato a re-evaluación con sondas físicas alternativas |
| 23 | Erosión dialéctica | -1.0000 | Categoría mal definida |
| 25 | Acuíferos | -0.1462 | Datos heterogéneos |
| 29 | IoT | -0.8760 | Reflexividad técnica |

### Bloque VII — Controles de falsación (correctamente rechazados)

**Tabla A.5.9.**

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

El caso 30 (Nivel 3 weak) demuestra que **el aparato EDI funciona en escala behavioral**, produciendo señal genuina con discriminación pública contra nulos. La complementariedad con la demostración cualitativa de Warren (r²=0.980) cubre dos escalas temporales del fenómeno.

---

## Lectura cruzada

- Caso ancla canónico cualitativo: capítulo 05-05
- Aplicaciones programáticas filosóficas: capítulos 05-01 a 05-04
- Caso 30 detallado: `09-simulaciones-edi/30_caso_behavioral_dynamics/README.md`
- Cada caso del corpus: `09-simulaciones-edi/<caso>/README.md`
- Resultados consolidados: `09-simulaciones-edi/README.md`
- Verificación de reproducibilidad: `Bitacora/2026-04-27-integracion-jacob/02-verificacion-reproducibilidad.md`
