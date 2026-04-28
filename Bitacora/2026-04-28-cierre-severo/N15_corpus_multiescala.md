# N15 — Corpus EDI multiescala: 10 casos en escalas distintas a la macro

> Plan de extensión del corpus EDI para demostrar que la tesis ontológica del **irrealismo operativo de estructuras pre-ontológicas** opera **a través de escalas**, no solo en sistemas macroscópicos. Solicitado por la dirección tras la auditoría severa, dada la observación correcta de que el corpus actual (30 casos) se concentra en escala macro (cuerpos sociales, ecosistemas, agregados estadísticos), lo que limita la generalidad ontológica reclamada.

## Marco teórico de la extensión

La tesis afirma que las **estructuras pre-ontológicas** son atractores empíricos de sistemas dinámicos acoplados, **independientemente de la escala**. Si esto es verdad, el aparato EDI debería:

1. detectar cierre operativo en sistemas cuánticos (escala 10⁻¹⁰ m / 10⁻¹⁵ s);
2. detectar cierre operativo en sistemas moleculares y celulares;
3. detectar cierre operativo en sistemas individuales (un agente, no población);
4. detectar cierre operativo en sistemas astrofísicos (escala 10²⁰ m / 10⁹ años);
5. fallar honestamente donde no haya cierre genuino, sin importar la escala.

Si el aparato funciona solo en escala macro-poblacional, la tesis ontológica debe restringirse a esa escala y no presentarse como general.

## Los 10 casos propuestos

### Escala cuántica (10⁻¹⁵–10⁻⁹ m)

#### Caso 31 — Decoherencia cuántica de qubit aislado

**Sistema:** qubit en interacción con baño térmico. Variable observable: tasa de decoherencia (T2). Sonda macro: ecuación de Lindblad con un único modo de baño. Forcing: temperatura del baño.

**Datos candidatos:** datasets públicos de IBM Quantum Experience (T1, T2 de qubits superconductores) o experimentos NIST con átomos atrapados.

**Hipótesis:** EDI ≥ 0.30 si la dinámica de decoherencia tiene cierre operativo (Lindblad reduce la varianza condicional de T2 respecto a un modelo no-acoplado al baño).

**Esfuerzo:** 4-6 semanas.

#### Caso 32 — Acoplamiento espín-órbita en sistemas de pocos átomos

**Sistema:** átomos individuales en redes ópticas con interacción espín-órbita ajustable. Variable: distribución de momento angular total. Sonda: Hamiltoniano efectivo de baja dimensión.

**Datos candidatos:** publicaciones de grupos de Bloch (MPI-Munich) con datos abiertos.

**Hipótesis:** EDI alto en régimen acoplado, EDI bajo en régimen no-acoplado.

**Esfuerzo:** 4-6 semanas.

### Escala molecular (10⁻⁹–10⁻⁷ m)

#### Caso 33 — Plegamiento de proteína pequeña (Villin Headpiece)

**Sistema:** dinámica de plegamiento Villin Headpiece (35 residuos). Variable observable: RMSD respecto al estado plegado. Sonda: modelo dos-estados con barrera (Markov state model de baja dimensión).

**Datos candidatos:** trayectorias de Anton (D.E. Shaw Research, publicadas como datasets abiertos).

**Hipótesis:** EDI alto bajo MSM, baja dimensión efectiva detectable, transición de plegamiento como bifurcación.

**Esfuerzo:** 6-8 semanas (datos masivos requieren preprocesamiento).

#### Caso 34 — Reacción enzima-sustrato (Michaelis-Menten)

**Sistema:** cinética enzimática observada por espectroscopía de molécula única. Variable: tasa de turnover. Sonda: ecuación de Michaelis-Menten + ruido. Forcing: concentración de sustrato.

**Datos candidatos:** datasets de Yang Lab (Berkeley) sobre β-galactosidasa.

**Hipótesis:** EDI alto en régimen Michaelis-Menten validado, baja dimensión efectiva (2-3 estados).

**Esfuerzo:** 4 semanas.

### Escala celular (10⁻⁵–10⁻⁴ m)

#### Caso 35 — Ciclo celular de levadura (S. cerevisiae)

**Sistema:** dinámica del ciclo celular bajo perturbación nutricional. Variable: fase del ciclo (G1, S, G2, M). Sonda: modelo de Tyson-Novak de baja dimensión (4 ODEs).

**Datos candidatos:** publicaciones de Cross Lab (Rockefeller) con datasets de microscopía time-lapse.

**Hipótesis:** EDI alto bajo Tyson-Novak; bifurcación en fase G1/S identificable.

**Esfuerzo:** 4-6 semanas.

#### Caso 36 — Expresión génica oscilatoria (NF-κB)

**Sistema:** oscilaciones de NF-κB en respuesta a TNF. Variable: concentración nuclear NF-κB. Sonda: modelo de Hoffmann (delay differential equation).

**Datos candidatos:** Single-cell traces de Hoffmann Lab (UCSD) o Tay Lab (ETH).

**Hipótesis:** EDI alto, oscilación como atractor límite-ciclo.

**Esfuerzo:** 4 semanas.

### Escala individual (un agente, no población)

#### Caso 37 — Latido cardíaco de individuo bajo estrés

**Sistema:** intervalos R-R cardíacos durante prueba de esfuerzo. Variable: serie temporal de intervalos. Sonda: oscilador no-lineal con acoplamiento autonómico (Glass-Mackey).

**Datos candidatos:** PhysioNet (cardiología, ECG abiertos).

**Hipótesis:** EDI alto en régimen de control autonómico funcional; EDI bajo en arritmias.

**Esfuerzo:** 4 semanas.

#### Caso 38 — Locomoción individual humana en VENLab (próximo)

**Sistema:** trayectoria de heading de un individuo en steering task (NO behavioral_attractor sintético). Variable: φ(t). Sonda: comparar Fajen-Warren contra τ-dot (Lee 1976) y minimum-jerk (Hogan 1984).

**Datos candidatos:** VENLab Brown (cuando se obtenga acceso académico).

**Hipótesis:** convergencia entre las tres sondas en datos reales humanos = no circularidad.

**Esfuerzo:** dependiente de acceso a datos (parte del programa caso 30 LoE=4).

### Escala astrofísica (10⁸–10²² m)

#### Caso 39 — Curvas de luz de estrellas variables Cefeidas

**Sistema:** modulación de brillo de Cefeidas como pulsación radial. Variable: magnitud aparente. Sonda: oscilador armónico con relación período-luminosidad.

**Datos candidatos:** OGLE survey (Optical Gravitational Lensing Experiment), datos abiertos.

**Hipótesis:** EDI alto bajo modelo de pulsación estándar; relación P-L como atractor.

**Esfuerzo:** 3-4 semanas.

#### Caso 40 — Dinámica de cúmulos globulares

**Sistema:** distribución de velocidades estelares en cúmulo globular. Variable: dispersión de velocidades. Sonda: modelo de Plummer + dinámica gravitatoria de baja dimensión.

**Datos candidatos:** Gaia DR3 (datos abiertos sobre cúmulos cercanos).

**Hipótesis:** EDI alto en cúmulos relajados, EDI bajo en cúmulos en transición de mareas.

**Esfuerzo:** 4-6 semanas.

## Cronograma agregado

| Mes | Casos a ejecutar |
|-----|------------------|
| 1 | 31 (decoherencia), 33 (Villin) — diseño de sondas y carga de datos |
| 2 | 31, 33, 34 (Michaelis-Menten) — ejecución |
| 3 | 35 (ciclo celular), 36 (NF-κB) |
| 4 | 37 (latido cardíaco), 39 (Cefeidas) |
| 5 | 32 (espín-órbita), 40 (cúmulos globulares) |
| 6 | 38 (VENLab) si hay acceso; análisis cross-escala consolidado |

Total: **6 meses** de dedicación parcial post-defensa para extender el corpus a 40 casos cubriendo escalas cuántica, molecular, celular, individual y astrofísica.

## Implicaciones documentales

La extensión exige:

1. **Capítulo nuevo `05-aplicaciones/06-corpus-multiescala.md`** que articule la tesis a través de escalas.
2. **Anexo nuevo A.12 — Tablas crudas multiescala** análogo a A.8.
3. **Actualización del cap 02-01** para declarar explícitamente que la tesis ontológica es **multiescalar** (la materialidad y los atractores existen a todas las escalas, no solo macro).
4. **Reformulación del cap 06-01** con cuadro multidominio × multiescala.
5. **Adaptación del aparato** ABM+ODE a series de alta frecuencia (cuántica, molecular requieren resolución temporal mucho mayor que la mensual del corpus actual).

## Implicación crítica para la tesis

Si los 10 casos pasan al menos como Nivel 3 weak en agregado:
- la tesis es **ontológicamente general** y se sostiene como contribución filosófica multiescalar;
- el aporte multidominio se vuelve aporte multidominio + multiescala.

Si los 10 casos fallan masivamente:
- la tesis debe restringirse a escala macro-poblacional;
- el cap 02-01 debe acotar la generalidad ontológica;
- el aporte sigue siendo metodológico pero limitado en alcance.

**El programa es honestamente falsable a nivel agregado.**

## Política de ejecución

1. ningún caso se admite al corpus sin pre-registro de hipótesis;
2. cada caso reporta resultado positivo o negativo con la misma severidad;
3. no se ajustan umbrales para que los casos pasen;
4. al menos 3 casos deben venir con datos LoE = 4 o 5 (no sintéticos).

## Compromiso

Este programa se asume como **deuda alta priorizada post-defensa** del autor técnico (Steven Vallejo) en coordinación con Jacob Agudelo. Su no-ejecución implica reconocer en el manuscrito final que la generalidad multiescalar de la tesis es **conjetural**, no demostrada.

## Lectura cruzada

- Auditoría severa: `Bitacora/2026-04-28-cierre-pendientes/03-auditoria-severa.md`.
- Corpus actual (30 casos macro): `09-simulaciones-edi/README.md`.
- Programas técnicos previos: `Bitacora/2026-04-28-cierre-doctoral/`.
- Hoja de ruta general: `06-cierre/03-hoja-de-ruta-para-tesis-final.md` (debe actualizarse para incluir este programa).
