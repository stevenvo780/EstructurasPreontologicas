# Estructuras Pre-Ontológicas
## Realismo Irrealista Operativo y Compresión Multiescala con Validación EDI Multidominio

**Tesis doctoral en filosofía de la ciencia y ciencias de la complejidad**

**Autor principal (concepto y dirección):** Jacob Agudelo, Universidad de Antioquia.
**Colaborador (técnica e ingeniería computacional):** Steven Vallejo Ortiz.
**Co-autoría IA:** declarada como instrumento de implementación bajo dirección humana.
**Versión:** 2026-04-27.

---

## Idea-fuerza

> Todo fenómeno empíricamente explicable, **a cualquier escala física, biológica o cosmológica**, está anclado en un sustrato material dinámico. Las entidades, niveles y categorías con que lo pensamos son **estructuras pre-ontológicas**: regularidades operativas anteriores a la objetualidad, identificables como atractores empíricamente robustos de sistemas dinámicos acoplados, admisibles solo bajo dossier de anclaje completo, protocolo C1-C5 satisfecho y EDI medido por intervención ablativa.

**La tesis ofrece tres marcos generales simultáneos:**

1. **Ontología general:** una sola estructura ontológica (sustrato material dinámico + acoplamiento + atractor empírico + cierre operativo κ) que se instancia a cualquier escala.
2. **Epistemología general:** una sola teoría del conocimiento como compresión disciplinada bajo intervención ablativa, operativa al mismo modo desde lo cuántico hasta lo cosmológico.
3. **Metodología general:** un solo aparato (motor ABM+ODE acoplado + protocolo C1-C5 + EDI + dossier de 14 componentes + suite ST) que ejecuta esa epistemología sobre esa ontología sin reentrenar arquitectura entre dominios o escalas.

**Los 40 casos del corpus son justificación operativa de los tres marcos, NO son la tesis.** La tesis son los marcos generales; el corpus muestra que las afirmaciones generales de los marcos son ejecutables, discriminantes y transferibles. Sin los casos los marcos serían conjetura plausible; con los casos son propuesta operativamente articulada con respaldo empírico parcial. Pero **la generalidad de los marcos no depende del tamaño del corpus**.

## Posición filosófica: Irrealismo Operativo

**Realismo estructural moderado + pluralismo epistemológico + anti-reificación operativa.** Nunca afirmamos `X es Y`; afirmamos `bajo el instrumento I, X exhibe cierre operativo de grado G respecto a la pregunta Q`. La dependencia instrumento-fenómeno no es defecto: es condición epistémica honesta. Esta posición se afirma **como ontología general**, no como ontología regional para una escala específica.

## Régimen de validez declarado

La tesis se sostiene como **propuesta ontológica multiescalar** validada operativamente sobre **40 casos** del corpus EDI agregado:

### Cobertura empírica

- **Corpus inter-dominio (30 casos):** discriminación entre dominios heterogéneos —física, biología, economía, política, tecnología, cultura, conducta humana— con EDI por intervención ablativa, permutación 999, bootstrap 500, protocolo C1-C5, AUC-ROC = 0.886 vs ARIMA = 0.600. **5 strong** (4 con gate completo): Energía (0.650), Deforestación (0.602), Microplásticos (0.782), Kessler (0.353), Riesgo Biológico (0.333). **3 controles de falsación** correctamente rechazados.
- **Corpus inter-escala (10 casos):** discriminación a través de **30 órdenes de magnitud espaciales** (10⁻¹⁰ m a 10²⁰ m) y **30 órdenes temporales** (10⁻¹⁵ s a 10¹⁴ s), desde dinámica subatómica hasta dinámica de cúmulos globulares. **7 strong en 7 escalas distintas** (atómica, cuántica, bioquímica, celular oscilatoria, individual, astrofísica, astrofísica masiva) + 1 weak + 2 nulls honestos. Sondas físicamente motivadas (Lindblad, Bloch, Tyson-Novak, Hoffmann, Mackey-Glass, Leavitt, Plummer); test cruzado V4-01 confirma especificidad (0/12 circularidad sobre datos no-suyos).

### Aparato verificado bajo hostile testing severo

- **0/1500 falsos positivos** del gate completo bajo random walk masivo (N1+N5+V4-06).
- **Suite ST de 13 teorías** formales con 2 hallazgos críticos detectados y corregidos.
- **Tests unitarios** del motor `edi_engine.py` pasados (V4-09).
- **Discriminación pública** contra catorce posiciones rivales (incluido Wolfram Physics Project, con piloto Rule 110 ejecutado mostrando convivencia de irreducibilidad micro y cierre macro detectable).

### Limitaciones honestas reconocidas

- p-value declarado mal calibrado (tasa empírica de tipo I = 24%, no 5%); **los umbrales EDI sí son robustos**;
- caso 30 (behavioral dynamics) sufre circularidad detectada por sonda alternativa; se mantiene como caso piloto metodológico hasta elevación con datos humanos reales;
- composición de los corpus es post-hoc, no pre-registrada;
- datos del corpus inter-escala son **sintéticos derivados de parámetros publicados**; la elevación a datos reales abiertos (IBM Quantum, BRENDA, PhysioNet, OGLE, Gaia DR3) es deuda priorizada de 6-12 meses post-defensa;
- todas las auditorías son endógenas; revisión por pares humanos hostiles es deuda externa bloqueante para sustentación.

## Estructura del repositorio

```
.
├── README.md                         ← este archivo
├── TesisFinal/                       ← manuscrito doctoral ensamblado (Tesis.md + Tesis.pdf)
├── 00-proyecto/                      ← arquitectura, preguntas, plan de capítulos
├── 01-diagnostico/                   ← falencias, objeciones, sesiones (subcarpeta)
├── 02-fundamentos/                   ← ontología, epistemología, categorías, nivel B
├── 03-formalizacion/                 ← aparato, criterios, auditoría, κ empírico (EDI)
├── 04-debates/                       ← rivales (incluido Wolfram), limitaciones
├── 05-aplicaciones/                  ← criterios, programáticas, caso ancla behavioral
├── 06-cierre/                        ← conclusión demostrativa, defensa, hoja de ruta
├── 07-bibliografia/                  ← corpus PDF y mapa de interlocutores
├── 08-consistencia-st/               ← capa ST de validación lógica
├── 09-simulaciones-edi/              ← código y outputs de los 30 casos del corpus EDI
└── Bitacora/                         ← bitácoras, trazabilidad histórica y mega-tareas archivadas
```

## Orden recomendado de lectura

### Para evaluador externo

1. `00-proyecto/01-estructura-general.md` (mapa);
2. `00-proyecto/02-preguntas-objetivos-hipotesis.md` (qué se pregunta y se responde);
3. `02-fundamentos/01-ontologia-material-relacional.md` (qué existe);
4. `02-fundamentos/04-anclaje-conductual-ecologico.md` (nivel B, asimetría L1↔B↔L3↔S);
5. `03-formalizacion/01-aparato-formal.md` (operadores μ, G, H, κ, ε);
6. `03-formalizacion/02-criterios-de-legitimidad-y-metodo.md` (dossier de anclaje);
7. `03-formalizacion/04-operacionalizacion-de-kappa.md` (κ vía baja dimensionalidad);
8. `09-simulaciones-edi/README.md` (corpus EDI: 30 casos);
9. `04-debates/01-debates-con-posiciones-rivales.md` (discriminación contra rivales, incluido Wolfram);
10. `05-aplicaciones/05-dinamica-conductual-reconstruccion-warren.md` (caso ancla);
11. `06-cierre/01-conclusion-demostrativa.md` (la tesis demostrada y sus condiciones de fracaso);
12. `06-cierre/02-guia-de-defensa.md` (la tesis defendible oralmente).

### Para autor o continuador del proyecto

Igual que arriba, más todos los capítulos restantes y `Bitacora/2026-04-27-integracion-jacob/00-bitacora.md` para entender cómo se consolidaron las dos iteraciones.

## Hardware disponible para validación empírica

- 2 GPUs NVIDIA: RTX 5070 Ti (16GB) + RTX 2060 (6GB)
- CPU 32 hilos
- 123 GB RAM, 191 GB swap
- Disco RAID 0: 1.2 TB (579 GB libres)
- Docker, PyTorch 2.10, CUDA 13.0, TensorRT, cuDNN
- Stack Python: numpy, scipy, pandas, joblib, meteostat, yfinance, pytrends

Las 29 simulaciones del corpus EDI están en `09-simulaciones-edi/` y se ejecutan con:

```bash
cd 09-simulaciones-edi
source .venv/bin/activate    # entorno aislado
./tesis demo                  # ejecuta caso clima
./tesis run --case clima      # CPU/GPU auto
./tesis audit                 # auditoría de outputs
```

## Aporte original sustantivo

La novedad no es de inventario sino de **articulación ontológica multiescalar**:

1. **Monismo ontológico multiescalar** sin reduccionismo plano: el mismo sustrato material dinámico subyace desde la dinámica subatómica hasta la cosmológica.
2. **Realismo estructural moderado** con anclaje empírico (estructuras pre-ontológicas como atractores con cinco condiciones, **independientemente de la escala**).
3. **Pluralismo explicativo controlado** con asimetría L1↔B↔L3↔S como protocolo formal y sistema modal T declarado.
4. **Formalización metodológica** con procedimiento empírico de κ vía EDI + C1-C5, distinción explícita κ-pragmática vs κ-ontológica.
5. **Cartografía multidominio + multiescala** con 40 casos agregados (30 inter-dominio + 10 inter-escala), discriminación pública contra rivales identificables (incluido Wolfram con piloto ejecutado), validación lógica formal con suite ST de 13 teorías, hostile testing aplicado y verificado.

## Estado del manuscrito

**Lo consolidado:**

- ontología material-relacional con definición técnica de patrón;
- epistemología de la compresión con verdad como preservación estructural;
- nivel B y asimetría L1↔B↔L3↔S;
- aparato formal de cinco operadores con procedimiento empírico de κ vía EDI;
- diez criterios y dossier de catorce componentes;
- protocolo C1-C5 con 13 condiciones para `overall_pass`;
- discriminación pública contra catorce rivales (incluido Wolfram);
- corpus EDI con 30 casos validados sobre datos públicos y sintéticos;
- 4 casos `overall_pass=True`;
- 3 controles de falsación correctamente rechazados;
- conclusión demostrativa con cinco condiciones de fracaso falsables;
- guía de defensa oral en tres tiempos.

**Lo ejecutado en el cierre 2026-04-28:**

- corpus inter-escala con 10 casos (atómica → astrofísica masiva): **7 strong**;
- multi-sonda + baselines ARIMA/VAR/RW/GP ejecutados;
- piloto EDI sobre Wolfram Rule 110 ejecutado (EDI 0.55, cierre macro detectable);
- caso piloto COVID dimensión normativa ejecutado con resultado null honesto;
- hostile testing N1-N5 + V4-01-V4-09 ejecutado;
- suite ST extendida a 13 teorías con 2 hallazgos críticos corregidos;
- 4 anexos nuevos (A.8-A.11), capítulo 05-06 nuevo, cap 02-01 con declaración multiescalar;
- distinción κ-pragmática/κ-ontológica formalizada;
- pre-registro honesto reconociendo limitaciones post-hoc;
- 18 citas textuales con paginación inyectadas en cap 02-01, 02-02, 02-03, 03-01, 03-02, 03-03.

**Lo que queda como deuda externa post-defensa:**

- elevación del caso 30 (behavioral dynamics) con datos humanos VENLab/WALK-MS (9-12 meses, requiere aval CEI);
- elevación del corpus inter-escala con datos reales abiertos en 5 escalas (6-12 meses);
- revisión por pares humanos hostiles (3-6 meses, deuda externa bloqueante);
- calibración correcta del p-value (refinamiento metodológico);
- conversión a plantilla institucional para depósito (3 semanas pre-depósito).

Cronograma post-defensa para programa de validación completo: 24-36 meses (capítulo 06-03).

## Cómo citar (versión preliminar)

> Agudelo, J., y Vallejo Ortiz, S. (2026). *Estructuras Pre-Ontológicas: Realismo Irrealista Operativo y Compresión Multiescala con Validación EDI Multidominio*. Manuscrito doctoral en preparación, Universidad de Antioquia.

## Licencia

[Por especificar según política institucional]
