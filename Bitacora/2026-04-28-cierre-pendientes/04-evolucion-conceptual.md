# Evolución conceptual: manuscrito-fuente original → capítulos canónicos

> Diff conceptual entre la formulación intuitiva inicial (`Bitacora/2026-04-27-integracion-jacob/00-tesis-fuente-original.md`, 408 líneas, 2026-04-27) y el manuscrito canónico ensamblado al cierre 2026-04-28 (`TesisFinal/Tesis.md`, ~9000 líneas). Cierra el ataque A12 de la auditoría severa.

## Política

Se reportan tres categorías:

1. **Claims preservados sin cambio sustancial.**
2. **Claims refinados** (mismo contenido, formulación más rigurosa).
3. **Claims abandonados, atenuados o reformulados radicalmente.**

## 1. Claims preservados (núcleo conceptual estable)

Los siguientes 7 claims de la versión corta del manuscrito-fuente se mantienen sin cambio sustancial en los capítulos canónicos:

| Claim original | Capítulo canónico equivalente |
|----------------|-------------------------------|
| Existe un solo plano material dinámico | Cap 02-01 |
| Entidades son estructuras pre-ontológicas (atractores) | Cap 02-01 §2 |
| Conocer es compresión disciplinada bajo intervención | Cap 02-02 |
| Asimetría L1 ↔ B ↔ L3 ↔ S | Cap 02-04 §8 |
| Emergencia como self-organization, no sustancia | Cap 02-04 §4 |
| Toda categoría pasa dossier de anclaje | Cap 03-02 |
| Nunca "X es Y", siempre "exhibe cierre operativo bajo I respecto a Q" | Cap 02-01 |

## 2. Claims refinados (rigor añadido sin cambio de contenido)

| Claim original | Refinamiento aplicado |
|----------------|------------------------|
| "EDI = 1 − RMSE_coupled / RMSE_no_ode con 4 pruebas + C1-C5" | Capítulo 03-04 detalla 13 condiciones para overall_pass; el manuscrito-fuente solo menciona C1-C5 |
| "Niveles 0-4 más Nivel 5 como programa futuro" | Capítulo 03-04 + Anexo A.9 declaran las 3 condiciones precisas del Nivel 5 (multi-sonda + LoE = 5 + frontera nítida) |
| "Discriminación contra 14 rivales" | Capítulo 04-01 desarrolla cada rival con citas textuales; el manuscrito-fuente solo enumera |
| "Asimetría L1↔B↔L3↔S" | Cap 02-04 §8.0 (post-ST) declara explícitamente nivel cuantificacional: B↔L3 universal, L1↔S existencial |
| Modal de la materialidad | Cap 02-01 (post-ST) declara sistema modal **al menos T (KT)** |
| Compromiso ontológico de κ | Cap 02-01 (post-severa A8) distingue **κ-pragmática** vs **κ-ontológica** |

## 3. Claims abandonados, atenuados o reformulados radicalmente

### 3.1. "30 casos demuestran multidominio"

**Manuscrito-fuente:** *"corpus EDI de 30 casos que abarcan física, biología, economía, política, tecnología, cultura y conducta humana"*. Tono: demostración multidominio cumplida.

**Cap canónico (post-severa):** se reconoce honestamente que (a) el corpus es post-hoc (`Bitacora/.../05-pre-registro-corpus-honesto.md`); (b) se concentra en **escala macro**, no es ontología multiescalar genuina (auditoría severa N15 con 10 casos en cuántica/molecular/celular/individual/astrofísica como deuda alta priorizada); (c) la composición es FRÁGIL a umbrales (N4: pasar de 0.10/0.30 a 0.15/0.40 reduce strong de 5 a 3).

**Atenuación:** la afirmación "demostración multidominio" se reformula como "discriminación multidominio post-hoc en escala macro, con AUC-ROC = 0.886".

### 3.2. "El caso 30 (behavioral dynamics) es weak con señal genuina"

**Manuscrito-fuente:** EDI = 0.262 con p = 0.044 reportado como Nivel 3 weak con "señal genuina y robusta".

**Cap canónico (post-severa N2):** se reconoce que la sonda Fajen-Warren produce EDI > 0.30 en **50% de mass-spring puro** bajo nulo. **Circularidad confirmada**: el caso 30 detecta auto-consistencia paramétrica de segundo orden, no behavioral dynamics específico. La elevación a LoE = 4 con datos humanos reales sigue como prerequisito para limpiar la circularidad.

**Atenuación:** el caso 30 se mantiene como **caso piloto metodológico**, no como demostración fuerte hasta tener datos humanos.

### 3.3. "El aparato discrimina con 50% de selectividad"

**Manuscrito-fuente:** *"15/30 casos con señal significativa. 3/3 controles correctamente rechazados. El aparato discrimina genuinamente, no es máquina de validar arbitrariamente."*

**Cap canónico (post-severa N1+N5):**
- bajo random walk masivo (1000 trials), el **gate completo** overall_pass tiene tasa empírica = 0% (✅ robusto);
- pero el **p-value declarado** tiene tasa empírica de tipo I = 24%, no 5%; calibración del p-value rota;
- los **umbrales EDI** (0.10 weak, 0.30 strong) sí son robustos: 0.6% / 0% bajo random walk;
- la "selectividad de 50%" depende de la composición específica del corpus, no es propiedad poblacional.

**Atenuación:** el aparato **discrimina** (AUC-ROC 0.886 > ARIMA 0.600); el **gate completo** es robusto; pero la **calibración del p-value** y la **composición del corpus** requieren refinamiento metodológico futuro.

### 3.4. "Validación lógica formal con ST"

**Manuscrito-fuente:** ST mencionada brevemente como capa de validación interna.

**Cap canónico (post-cierre):** suite ST extendida a **13 teorías** con **2 hallazgos críticos** detectados y corregidos (asimetría como existenciales en FOL; modal T para necesidad). Anexo A.11 con limitaciones explícitas (ST no valida axiomas vacíos, no valida calibración, no detecta circularidad empírica).

**Refinamiento radical:** ST pasa de mención a **componente sustantivo** del marco con limitaciones declaradas.

### 3.5. "Aporte ontológico nuevo"

**Manuscrito-fuente:** sugería que la tesis introduce ontología nueva (estructuras pre-ontológicas como categorías originales).

**Cap canónico (post-severa A14):** se reformula como **aporte primario metodológico**, no ontológico nuevo. Las "estructuras pre-ontológicas" no son entidades nuevas: son **criterio operativo** para admitir entidades reconocidas. La tesis no descubre cosas nuevas en cada uno de los 30 dominios; ofrece protocolo replicable.

**Atenuación filosófica:** la tesis se posiciona como **contribución metodológica** a filosofía de la complejidad, no como ontología sustantiva nueva.

## 4. Lo que el manuscrito-fuente sugería pero el cierre canónico NO sostiene

| Promesa del fuente | Cierre canónico |
|---------------------|-----------------|
| "30 casos demuestran ontología general multidominio" | Discrimina en escala macro post-hoc; multiescalaridad genuina queda como N15 (10 casos pendientes) |
| "Caso 30 con señal genuina" | Caso piloto metodológico; circularidad detectada por N2 |
| "Aparato verificablemente discrimina" | Gate completo sí; p-value mal calibrado |
| "Validación filosófica completa" | Validación lógica interna (ST) + validación empírica multidominio en escala macro; revisión humana experta como deuda externa A13 |
| "Demostración cuantitativa de la dimensión normativa via caso piloto COVID" | Caso piloto COVID ejecutado con resultado **null honesto**; dimensión normativa permanece programática |

## 5. Coherencia general

**Verificación:** el núcleo conceptual del manuscrito-fuente (7 claims preservados de §1) sobrevive al cierre canónico **sin contradicción interna**. Las atenuaciones son **honestidad metodológica** añadida tras hostile testing, no abandono del núcleo.

La tesis sigue siendo:

> *Mínima en sustancias, rica en relaciones, controlada en sus recortes, reversible en sus niveles, anclada en cartografía empírica multidominio (escala macro), abierta en su programa de extensión (multiescalar como N15), verificable contra rivales por discriminación pública, y disciplinada por anti-reificación operativa.*

**Lo que cambia desde el fuente al cierre canónico no es la tesis, es su grado de honestidad metodológica.** Las correcciones aplicadas tras N1-N15 hacen el marco más defensible, no más débil: una tesis que admite limitaciones empíricas y conceptuales es más robusta que una que las oculta.

## 6. Lectura cruzada

- Manuscrito-fuente original: `Bitacora/2026-04-27-integracion-jacob/00-tesis-fuente-original.md`.
- Capítulos canónicos: `00-proyecto/` a `06-cierre/`.
- Auditoría severa: `Bitacora/2026-04-28-cierre-pendientes/03-auditoria-severa.md`.
- Resultados N1-N5: `Bitacora/2026-04-28-cierre-severo/N{1,2,3,4,5}_resultados.json`.
- Plan multiescala: `Bitacora/2026-04-28-cierre-severo/N15_corpus_multiescala.md`.
