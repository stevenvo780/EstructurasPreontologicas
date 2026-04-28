# Bitácora de integración: iteración Jacob → manuscrito doctoral consolidado

**Fecha:** 2026-04-27
**Sesión:** integración masiva de la iteración previa "TesisJacobContenidos" al manuscrito doctoral consolidado

## Contexto

El proyecto tiene dos iteraciones del mismo programa de investigación:

- **Iteración 1** (`TesisJacobContenidos`, 2026-02): liderada por Jacob Agudelo (U. Antioquia). Tesis doctoral *"Irrealismo Operativo de Hiperobjetos: Clasificación de Fenómenos por Grado de Cierre Operativo"*. Marco computacional ABM+ODE con métrica EDI (Effective Dependence Index) y protocolo C1-C5. 29 casos validados sobre datos reales (World Bank, OWID, Meteostat, Yahoo Finance, OPSD, CelesTrak, Wikimedia).
- **Iteración 2** (`EstructurasPreontologicas`, 2026-04): consolidación filosófica con caso ancla canónico Warren 2006 (behavioral dynamics), aparato formal con cinco operadores y asimetría L1↔B↔L3↔S, dossier de anclaje de 14 componentes.

Ambas iteraciones comparten posición filosófica (realismo estructural moderado + pluralismo epistemológico + anti-reificación operativa). La integración consolida el aparato empírico de la iteración 1 (29 casos cuantitativos) con la arquitectura argumental de la iteración 2 (manuscrito doctoral defendible).

## Atribución corregida

- **Autor principal (concepto y dirección):** Jacob Agudelo, Universidad de Antioquia.
- **Colaborador (técnica, ingeniería computacional, formalización):** Steven Vallejo Ortiz.
- **Co-autoría IA:** declarada explícitamente en el manuscrito como instrumento de implementación y documentación bajo dirección humana.

## Decisiones arquitectónicas

### A. Posición filosófica unificada

Adoptar el vocabulario afilado de Jacob — **irrealismo operativo** = realismo estructural moderado + pluralismo epistemológico + anti-reificación operativa — como articulación canónica. Esto reemplaza formulaciones equivalentes pero más blandas del manuscrito iteración 2.

### B. EDI como operacionalización empírica de κ

La métrica EDI de Jacob (`EDI = 1 - RMSE_coupled / RMSE_no_ode`) es la operacionalización empírica más precisa del operador de compresión κ del manuscrito iteración 2. Mide degradación predictiva al apagar la constricción macro, con prueba de permutación (999) y bootstrap (500). Sustituye al "procedimiento empírico vía baja dimensionalidad" formulado abstractamente en el capítulo 03-04.

### C. Protocolo C1-C5 como condiciones del dossier de anclaje

Los cinco filtros de Jacob (Convergencia, Robustez, Determinismo aleatorio, Consistencia de dominio, Reporte de incertidumbre) más los 13 criterios adicionales de `overall_pass=True` se incorporan al dossier de anclaje de 14 componentes del manuscrito iteración 2 como check operativo.

### D. Modelo ABM+ODE acoplado como estructura básica del nivel B

La arquitectura híbrida ABM (Agent-Based Modeling) + ODE (Ordinary Differential Equations) de Jacob es la implementación canónica del par dinámico acoplado del nivel B (capítulo 02-04). El ABM realiza la dinámica micro; la ODE realiza la sonda macro. La medida del acoplamiento (mc) y del forcing (fs) son las contribuciones diferenciables del sistema acoplado.

### E. 29 casos como demostración multidominio masiva

El paisaje de emergencia de Jacob (29 casos en física, biología, economía, política, tecnología, cultura) reemplaza la asimetría caso-ancla-único / cuatro-dominios-programáticos de la iteración 2. Los 29 casos incluyen:

- **5 strong** (4 con `overall_pass=True`): Energía (EDI=0.650), Deforestación (0.602), Microplásticos (0.782), Kessler (0.353), Riesgo Biológico (0.333). El umbral del 5to (Microplásticos, EDI=0.782) está fuera de gate por aspectos técnicos del bootstrap.
- **7 weak**: Políticas Estratégicas (0.297), Postverdad (0.243), Urbanización (0.236), Wikipedia (0.192), Fósforo (0.192), Epidemiología (0.130), Movilidad (0.128).
- **2 suggestive**: Finanzas (0.081), Salinización (0.018).
- **4 trend**: Justicia (0.227), Starlink (0.689 con val_steps=1), Fuga de Cerebros (0.025), Clima (0.011).
- **8 null**: Conciencia, Contaminación, Paradigmas, Océanos, Acidificación Oceánica, Erosión Dialéctica, Acuíferos, IoT.
- **3 controles de falsación correctamente rechazados**: Exogeneidad (ruido puro), No-estacionariedad (random walk), Observabilidad (estado oculto).

### F. Caso 30: behavioral dynamics extiende el corpus

El caso ancla canónico de la iteración 2 (Warren 2006 behavioral dynamics) se reformula como caso 30 del corpus EDI: dinámica conductual locomotora medida sobre el ciclo percepción-acción agente-entorno. Esto conecta los dos manuscritos en un solo aparato empírico unificado y eleva el caso ancla de demostración cualitativa (varianza explicada r²=0.980) a demostración cuantitativa con métrica EDI bajo el mismo protocolo de los otros 29.

### G. Estructuras pre-ontológicas como nombre del programa

El nombre del repositorio (`EstructurasPreontologicas`) recoge una formulación de Jacob que el manuscrito iteración 2 no había integrado: las estructuras pre-ontológicas son **regularidades operativas anteriores a la objetualidad**. No son ficciones, no son sustancias; son patrones cuya existencia se mide por su irreducibilidad funcional bajo intervención (EDI). El "realismo irrealista" de Jacob es la formulación afilada del realismo estructural moderado.

### H. Wolfram como interlocutor explícito

Jacob piensa la tesis como análoga al programa de Wolfram (Wolfram Physics Project, hypergraph rewriting, Ruliad) pero como **ontología y epistemología generales integradoras**, no como física fundamental. Esto añade un interlocutor de gran peso al capítulo de debates (04-01) que el manuscrito iteración 2 había omitido. La diferencia principal: Wolfram busca una *ontología fundamental* desde reglas computacionales; el irrealismo operativo busca un *protocolo de admisión* de constructos macro bajo intervención empírica. Convergen en el papel central de los hipergrafos como representación; divergen en la ambición ontológica.

## Hardware disponible

- 2 GPUs NVIDIA: RTX 5070 Ti (16 GB) + RTX 2060 (6 GB)
- CPU 32 hilos (sin información de marca exacta en lscpu, pero alto rendimiento)
- RAM 123 GB total, 65 GB disponibles, 191 GB swap
- Disco RAID 0: 1.2 TB en `/datos` con 579 GB libres
- Docker, PyTorch 2.10, CUDA 13.0, TensorRT, cuDNN
- Stack Python: numpy, scipy, pandas, scikit-learn, joblib, meteostat, yfinance, pytrends, requests

Esto permite re-ejecutar las 29 simulaciones con perfiles agresivos (n_perm > 999, n_boot > 500, batch GPU para ABM) y construir caso 30 de behavioral dynamics con cómputo serio.

## Acciones ejecutadas en esta sesión

1. Clonado de `TesisJacobContenidos` en `/tmp` para estudio.
2. Lectura completa de:
   - `README.md` y `CLAUDE.md` (orientación al proyecto y a IA);
   - `TesisDesarrollo/Indice_Maestro.md` (mapa de capítulos);
   - `TesisDesarrollo/00_Marco_Conceptual/00_00_Marco_Conceptual.md` (postura filosófica completa);
   - `TesisDesarrollo/01_Metodologia_Medicion/01_00_Metodologia_Medicion.md` (Emergentómetro y EDI);
   - `TesisFinal/abstract.md` y primeras 300 líneas de `TesisFinal/Tesis.md`.
3. Inspección del código:
   - `repos/Simulaciones/common/hybrid_validator.py` (2252 líneas, validador canónico);
   - estructura de los 29 casos.
4. Migración del código completo de simulaciones a `09-simulaciones-edi/` (6.0 MB).
5. Creación de venv aislado con todas las dependencias del repo previo.
6. Ejecución exitosa de la fase sintética del caso 01 (clima): el pipeline corre con la versión actual de Python 3.13.
7. Migración de los 29 outputs computados (`outputs/metrics.json` por caso) que constituyen la fuente de verdad para la tabla del manuscrito.
8. Generación de tabla maestra reproducible con EDI, p-value, overall_pass, val_steps por caso. Coincidencia exacta con los reportados en el README de la iteración 1.

## Resumen de tabla maestra (29 casos, fase real)

```
caso                                     EDI       p  pass val_steps
04_caso_energia                       0.6503  0.0000  True   13
05_caso_epidemiologia                 0.1294  0.0000 False  104
09_caso_finanzas                      0.0813  0.0000 False  168
11_caso_movilidad                     0.1283  0.0020 False   19
13_caso_politicas_estrategicas        0.2972  0.0015 False   13
14_caso_postverdad                    0.2428  0.0000 False    8
15_caso_wikipedia                     0.1916  0.0000 False   48
16_caso_deforestacion                 0.6020  0.0000  True   13
18_caso_urbanizacion                  0.2358  0.0000 False   23
20_caso_kessler                       0.3527  0.0000  True   15
21_caso_salinizacion                  0.0184  0.0028 False   18
22_caso_fosforo                       0.1924  0.0000 False   18
24_caso_microplasticos                0.7819  0.0000 False   15
27_caso_riesgo_biologico              0.3326  0.0022  True    9
01_caso_clima                         0.0111  0.9990 False  168  (trend)
26_caso_starlink                      0.6892  1.0000 False    1  (trend, ventana muy corta)
06_caso_falsacion_exogeneidad         0.0551  1.0000 False  731  (control rechazado)
07_caso_falsacion_no_estacionariedad -0.8819  1.0000 False  731  (control rechazado)
08_caso_falsacion_observabilidad     -1.0000  1.0000 False   97  (control rechazado)
[8 casos null y demás trend omitidos por brevedad]
```

## Tareas pendientes en el siguiente bloque

1. Refactor completo del manuscrito iteración 2 integrando autoría, EDI, C1-C5, 29 casos, Wolfram, estructuras pre-ontológicas.
2. Construcción del caso 30 (behavioral dynamics) bajo metodología EDI.
3. Re-ejecución de los 29 casos con perfiles de alto rendimiento para verificación de reproducibilidad.
4. Cierre del manuscrito final defendible con tabla de 30 casos y discriminación pública contra rivales (incluido Wolfram).

## Riesgos identificados

- **Sesgo de confirmación por cómputo:** disponer de hardware potente y resultados favorables puede inducir a glorificarse y producir conocimiento profundamente malo. Mitigación: vigilancia crítica permanente, cada resultado nuevo debe pasar el filtro `C1-C5 + dossier`, controles de falsación obligatorios antes de admisión.
- **Pérdida de la asimetría L1↔B↔L3↔S:** la iteración 1 no usa explícitamente esta asimetría. Hay que asegurar que la integración no la sacrifique.
- **Wolfram como rival mal articulado:** discriminar contra Wolfram exige cuidado: la posición es ambiciosa y técnicamente sofisticada. La discriminación en tabla pública debe ser justa y no caricaturizada.
- **El caso 30 (behavioral dynamics) puede no encajar fácilmente** en la metodología EDI porque Warren 2006 es más cualitativo que cuantitativo en el sentido EDI. Hay que reformularlo como un sistema acoplado ABM+ODE legítimo, no forzarlo.

## Régimen de validez de esta integración

La integración no es trivial. Hay decisiones interpretativas sobre cómo se mapean conceptos entre las dos iteraciones. Cada decisión queda documentada aquí para que un tercero pueda auditarlas y, si las considera incorrectas, reformularlas con trazabilidad.
