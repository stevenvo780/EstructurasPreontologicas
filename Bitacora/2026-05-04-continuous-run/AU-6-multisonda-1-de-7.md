# AU-6 — Multi-sonda 1/7 (14%): convergencia reportada pero no propagada al juicio

**Fecha:** 2026-05-05
**Origen:** Hallazgo adversarial-reviewer 2026-05-05
**Estado:** `needs_human` (requiere B-T1 para 40 casos + firma Jacob para reescritura abstract/conclusión + fetch de Cartwright 1999)

## (a) Verificación de la afirmación

1. **Tasa 1/7 está verificada** contra la fuente operativa.
   - `09-simulaciones-edi/multi_sonda/secondary_on_primary_arrays.md:6-7`:
     - `Convergencia |ΔEDI| ≤ 0.05: 0/7`
     - `Convergencia |ΔEDI| ≤ 0.10: 1/7` (caso 27_caso_riesgo_biologico, ΔEDI=0.059)
   - `06-cierre/04-versiones-cortas-defensa.md:60` reproduce literalmente "1/7 converge bajo |ΔEDI| ≤ 0.10 — limitación honestamente reportada".
   - `06-cierre/01-conclusion-demostrativa.md:147` (fila tabla deuda) declara la misma cifra y vincula a F13 "cierra parcialmente".

2. **El denominador 7 no es 40.** El propio `secondary_on_primary_arrays.md:30-37` advierte que de 32+2 archivos `primary_arrays.json` existentes, **solo 2 son arrays reales** (41 wolfram, 42 histéresis) y 5 son reconstruidos desde RMSE publicado (informativos solo en superficie); los 25 restantes son reconstrucciones no interpretables. La tasa "1/7" mezcla 2 reales + 5 reconstruidos calibrados — es decir, **la base interpretable estricta es 2 casos, no 7**, y la convergencia real fuerte se da en 1 de esos.

3. **La objeción adversarial es válida.** El abstract corto (`06-cierre/04` línea 60) reporta la cifra dentro de un párrafo cuyo encabezado es **"Hostile testing severo"** y la enmarca como elemento más entre "0/1500 falsos positivos", "0/12 circularidad". El lector razonable absorbe el conjunto como prueba de robustez; la cifra 1/7 (=14%) bajo el umbral *relajado* y 0/7 bajo el *fuerte* contradice el tono. La conclusión demostrativa (`06-cierre/01:147`) la ubica como "cierra parcialmente F13", pero **ningún sitio del cuerpo argumental traduce la tasa al juicio sobre la fuerza de la afirmación κ-ontológica/inter-paradigma a nivel de corpus**.

4. **Cita Cartwright 1999 cap.4 p.89: NO verificable localmente.**
   - `07-bibliografia/` solo contiene `Cartwright - How the Laws of Physics Lie (1983).pdf`. **No está** *The Dappled World* (1999).
   - `04-debates/` actualmente **no contiene ninguna mención a Cartwright** (grep negativo).
   - Por tanto, la acceptance "cita Cartwright 1999 cap.4 p.89 paginada en cap 04-debates" **no puede cumplirse sin antes obtener el PDF** o, en su defecto, sin que un humano con acceso institucional verifique la paginación.

## (b) Propuesta de edición concreta

**Edición 1 — `06-cierre/04-versiones-cortas-defensa.md:60` (defensa corta).**
Sacar la cifra 1/7 de la enumeración "Hostile testing severo" y darle frase propia con peso proporcional. Borrador (DRAFT-AI, requiere firma Jacob):

> Hostile testing severo: 0/1500 falsos positivos del gate completo bajo random walk masivo, 0/12 circularidad detectada en test cruzado de sondas inter-escala, suite ST con 6 hallazgos críticos detectados y corregidos.
>
> **Convergencia inter-paradigma honestamente débil.** Aplicadas sondas teóricamente independientes a los arrays primarios reales de 7 casos disponibles, ninguno converge bajo el criterio fuerte (|ΔEDI| ≤ 0.05) y solo uno (caso 27, ΔEDI = 0.059) bajo el relajado (≤ 0.10). De ese conjunto de 7, además, solo 2 corresponden a arrays reales (casos 41, 42); los otros 5 son reconstrucciones calibradas desde RMSE publicado, informativas solo de manera limitada. **Por esta razón ningún caso del corpus alcanza κ-ontológica fuerte**; la tesis sostiene κ-pragmática y deja la elevación a κ-ontológica como programa abierto condicionado a la ejecución completa de B-T1 (re-ejecución de 40 casos con `array_dump=True`).

**Edición 2 — `06-cierre/01-conclusion-demostrativa.md:147` (tabla deuda).** Cambiar "Cierra parcialmente F13" por "Cierra **parcialmente** F13 sobre 7 casos (2 reales + 5 reconstruidos); convergencia 1/7 bajo umbral relajado, 0/7 bajo umbral fuerte; cierre F13 de corpus completo (40 casos) **abierto** y condicionado a B-T1".

**Edición 3 — bloqueada por B-T1.** Reportar convergencia inter-sonda para los 40 casos del corpus exige re-ejecutar los casos con datos reales y `array_dump=True`. Hasta entonces, **no se puede afirmar nada de tasa de convergencia "del corpus"**; solo de los 7 casos con arrays. La acceptance "Convergencia inter-sonda reportada para 40 casos tras B-T1" es por construcción posterior a B-T1.

**Edición 4 — Cartwright 1999.** Tres salidas, decisión de Jacob:
   - (i) `bibliography-fetcher` recupera *The Dappled World* (1999) cap.4 (Cambridge UP); luego `citation-agent` verifica p.89 y se cita en `04-debates/04-anticipacion-objeciones-filosoficas.md` o nuevo §"Patchwork de leyes y multidominio" en `04-debates/`. Coste: dependencia externa.
   - (ii) Sustituir por Cartwright 1983 (sí presente en biblioteca) con paginación verificable, asumiendo el costo argumental de que el argumento de "patchwork" es más explícito en 1999.
   - (iii) Eliminar la exigencia de cita Cartwright si el argumento del cap 04-debates no la requiere realmente.

## (c) Costo argumental declarado

- **Concesión 1 (operativa):** la tesis no puede afirmar a nivel de corpus que las κ son invariantes inter-paradigma. La evidencia disponible cubre 7 casos con interpretación útil sobre 2 (reales). El resto del corpus es elocuente sobre EDI pero **silente sobre convergencia inter-paradigma** hasta B-T1.
- **Concesión 2 (filosófica, vía Cartwright):** un escenario "patchwork de leyes" (Cartwright 1999) es compatible con que cada caso tenga su sonda canónica sin que exista una sonda transversal, y eso erosionaría la generalidad del aparato a la que la tesis aspira. Esta concesión debe declararse en `04-debates/` con cita paginada o eliminarse del programa argumental.
- **Concesión 3 (umbralógica):** el umbral |ΔEDI| ≤ 0.10 es laxo; el lector puede legítimamente exigir el fuerte (≤ 0.05), bajo el cual la tasa es **0/7**. La defensa actual no discute por qué el umbral relajado debe contar como evidencia.

## Marcadores

- `needs_human`: aprobación de Jacob sobre Edición 1, 2 y elección entre (i)/(ii)/(iii) en Edición 4.
- `B-T1`: bloquea Edición 3.
- `bibliography-fetcher`: requerido si se elige Edición 4-(i).

## Acceptance — estado

- [ ] Convergencia inter-sonda reportada para 40 casos tras B-T1 — **pendiente B-T1**
- [ ] Ajuste lenguaje abstract/conclusión proporcional a la tasa — **borrador propuesto, needs_human**
- [ ] Cita Cartwright 1999 cap.4 p.89 paginada en cap 04-debates — **bloqueado: PDF no disponible localmente**
