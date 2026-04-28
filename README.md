# Estructuras Pre-Ontológicas
## Realismo Irrealista Operativo y Compresión Multiescala con Validación EDI Multidominio

**Tesis doctoral en filosofía de la ciencia y ciencias de la complejidad**

**Autor principal (concepto y dirección):** Jacob Agudelo, Universidad de Antioquia.
**Colaborador (técnica e ingeniería computacional):** Steven Vallejo Ortiz.
**Co-autoría IA:** declarada como instrumento de implementación bajo dirección humana.
**Versión:** 2026-04-27.

---

## Idea-fuerza

> Todo fenómeno empíricamente explicable está anclado en un sustrato material dinámico. Las entidades, niveles y categorías con que lo pensamos son **estructuras pre-ontológicas**: regularidades operativas anteriores a la objetualidad, identificables como atractores empíricamente robustos de sistemas dinámicos acoplados, admisibles solo bajo dossier de anclaje completo, protocolo C1-C5 satisfecho y EDI medido por intervención ablativa.

## Posición filosófica: Irrealismo Operativo

**Realismo estructural moderado + pluralismo epistemológico + anti-reificación operativa.** Nunca afirmamos `X es Y`; afirmamos `bajo el instrumento I, X exhibe cierre operativo de grado G respecto a la pregunta Q`. La dependencia instrumento-fenómeno no es defecto: es condición epistémica honesta.

## Régimen de validez declarado

La tesis está **demostrada** en cartografía multidominio de **30 casos** del corpus EDI con:

- **EDI** (Effective Dependence Index) calculado por intervención ablativa con prueba de permutación (999) y bootstrap (500);
- **Protocolo C1-C5** (Convergencia, Robustez, Determinismo, Consistencia, Incertidumbre) más 8 criterios adicionales para `overall_pass=True`;
- **5 casos strong** (4 con gate completo): Energía (EDI=0.650), Deforestación (0.602), Microplásticos (0.782), Kessler (0.353), Riesgo Biológico (0.333);
- **3 controles de falsación** correctamente rechazados;
- **Discriminación pública** contra catorce posiciones rivales (incluido Wolfram Physics Project).

## Estructura del repositorio

```
.
├── tesis.md                          ← manuscrito-fuente consolidado
├── README.md                         ← este archivo
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
├── Procesos/                         ← bitácoras y trazabilidad histórica
└── Tareas/                           ← backlog duro y mega-tareas
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

Igual que arriba, más todos los capítulos restantes y `Procesos/2026-04-27-integracion-jacob/00-bitacora.md` para entender cómo se consolidaron las dos iteraciones.

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

La novedad no es de inventario sino de **articulación**:

1. **Monismo ontológico** sin reduccionismo plano.
2. **Realismo estructural moderado** con anclaje empírico (estructuras pre-ontológicas como atractores con cinco condiciones).
3. **Pluralismo explicativo controlado** con asimetría L1↔B↔L3↔S como protocolo formal.
4. **Formalización metodológica** con procedimiento empírico de κ vía EDI + C1-C5.
5. **Cartografía multidominio masiva** con 30 casos y discriminación pública contra rivales identificables, incluido Wolfram.

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

**Lo pendiente:**

- elevación del caso 30 (behavioral dynamics) bajo metodología EDI completa;
- programa multi-sonda para 3-5 casos clave;
- integración bibliográfica formal con citas rigurosas;
- desarrollo del aparato para variables normativas;
- lectura externa hostil;
- redacción unificada en estilo doctoral final.

Cronograma plausible: 24-36 meses (capítulo 06-03).

## Cómo citar (versión preliminar)

> Agudelo, J., y Vallejo Ortiz, S. (2026). *Estructuras Pre-Ontológicas: Realismo Irrealista Operativo y Compresión Multiescala con Validación EDI Multidominio*. Manuscrito doctoral en preparación, Universidad de Antioquia.

## Licencia

[Por especificar según política institucional]
