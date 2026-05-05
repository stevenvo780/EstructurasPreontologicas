# F03-09 — Dimensionalidad sin protocolo de elección

**Fecha:** 2026-05-04
**Origen:** adversarial-reviewer cap03 (2026-05-05)
**Archivo señalado:** `03-formalizacion/04-operacionalizacion-de-kappa.md:36-48` (Paso 3)

## (a) Verificación de la afirmación

Lectura literal del Paso 3 (`04-operacionalizacion-de-kappa.md:36-48`):

> "Sobre las series multivariadas se aplica un análisis de dimensionalidad efectiva. Métodos válidos según el caso:
> - análisis de componentes principales (PCA) sobre las trayectorias;
> - estimación de dimensión de correlación (Grassberger–Procaccia);
> - estimación de dimensión intrínseca por vecinos más cercanos;
> - truncamiento por varianza explicada acumulada;
> - exponentes de Lyapunov para detectar caos versus régimen de baja dimensión.
>
> El resultado es un número `d` (con su intervalo de confianza)…"

**El hallazgo del adversarial es correcto.** El texto enumera cinco métodos como "válidos según el caso" sin definir:

1. **Cuál se elige y bajo qué criterio.** "Según el caso" es subdeterminación abierta: cualquier autor puede elegir post-hoc el método que produce el `d` más conveniente.
2. **Cómo se reporta el CI.** Se menciona "(con su intervalo de confianza)" pero no el procedimiento (bootstrap sobre observaciones, sobre embeddings, sobre escalas de Grassberger–Procaccia, etc.).
3. **Qué hacer cuando los métodos discrepan.** PCA suele sobreestimar `d` (lineal) y Grassberger–Procaccia subestimarla en datos cortos/ruidosos (Camastra & Vinciarelli 2002; Camastra & Staiano 2016, *Information Sciences* 328:26-41). NN (Levina–Bickel 2004) tiene su propio sesgo. La omisión de un protocolo de reconciliación reproduce el problema "garden of forking paths" que la propia tesis denuncia.

La crítica de Simmons, Nelson & Simonsohn (2011, *Psychological Science* 22:1359-1366) sobre flexibilidad analítica encubierta aplica exactamente: cinco métodos × elección post-hoc = espacio de grados de libertad del investigador no declarado.

## (b) Propuesta de edición

**Estatuto:** `needs_human` para firma de Jacob (afecta protocolo central de κ; tiene costo argumentativo).

Borrador propuesto (Paso 3 reescrito) — DRAFT-AI, no aplicar sin revisión:

> ### Paso 3. Estimar la dimensionalidad efectiva
>
> Sobre las series multivariadas se aplica un **protocolo triple obligatorio** de estimación de dimensionalidad efectiva. La admisión a Paso 4 requiere acuerdo cualitativo entre al menos dos de los tres estimadores; la divergencia obliga a declarar régimen "alta dimensión / no comprimible" o a ampliar la ventana de medición.
>
> 1. **d_PCA** — análisis de componentes principales sobre trayectorias estandarizadas. Se reporta el menor `k` tal que la varianza acumulada explica ≥ 90 %. CI por bootstrap no paramétrico sobre las observaciones (B=500).
> 2. **d_GP** — dimensión de correlación de Grassberger–Procaccia (1983) sobre embedding de Takens con τ por primer mínimo de información mutua y `m` por falsos vecinos cercanos. Pendiente estimada en la región lineal de `log C(r)` vs `log r`. CI por bootstrap sobre escalas.
> 3. **d_NN** — dimensión intrínseca por vecinos más cercanos (Levina & Bickel 2004, *NeurIPS* 17). CI por bootstrap sobre puntos.
>
> **Criterio de admisión:** se considera "baja dimensión candidata" sii ⌈d_X⌉ = ⌈d_Y⌉ para al menos dos pares (X,Y) de métodos, o sus CIs se solapan. Si los tres divergen (Δ > 1 entre extremos sin solape de CI), el caso queda en estatus "alta dimensionalidad / κ no admisible bajo este protocolo".
>
> **Tabla de reporte obligatoria por caso:**
>
> | Caso | d_PCA (CI) | d_GP (CI) | d_NN (CI) | Acuerdo ≥2 | Admite Paso 4 |
> |------|------------|-----------|-----------|------------|---------------|
> | …    | …          | …         | …         | sí/no      | sí/no         |
>
> Truncamiento por varianza explicada y exponentes de Lyapunov **se reportan como diagnósticos auxiliares** (caos vs baja dimensión), no como sustitutos de los tres estimadores.

## (c) Costo argumentativo declarado

1. **Costo computacional retroactivo.** El corpus actual (40 casos) no tiene la triple estimación con CI. Aplicar el protocolo retroactivo produce dos resultados posibles: (i) confirma baja dimensión en los casos strong (ROBUSTO) y refuerza la tesis; (ii) revela que algunos casos hoy admitidos no satisfacen el acuerdo ≥2 — estos pasarían a estatus "no admisible bajo el nuevo protocolo" y deben moverse a deuda. La opción (ii) es real y debe asumirse.
2. **Costo de cobertura.** Casos con `n` pequeña (<50) probablemente no producen `d_GP` estable (Camastra & Staiano 2016 §4). Si el protocolo se aplica estrictamente, varios casos inter-escala podrían quedar inadmisibles por insuficiencia de datos para Grassberger–Procaccia, no por carencia de baja dimensión real.
3. **Concesión filosófica.** La tesis pierde la cláusula "métodos válidos según el caso" — que era flexibilidad legítima en investigación exploratoria pero abre la puerta al cherry-picking en defensa doctoral. La pérdida es deseable: cierra un grado de libertad del investigador.
4. **Beneficio.** Cierra el flanco F03 que el adversarial-reviewer identificó. Hace `κ` auditable bajo el mismo estándar Simmons-Nelson-Simonsohn que la tesis aplica a sus rivales.

## Verificación bibliográfica pendiente

- Camastra & Staiano (2016) y Simmons, Nelson & Simonsohn (2011): el adversarial los cita pero no se verificó paginación contra PDF en `07-bibliografia/`. Dejar como `needs_human` para `@citation-agent` antes de incorporar al manuscrito.
- Levina & Bickel (2004): citado en el borrador; verificar acceso al PDF antes de fijarlo.

## Marca

`needs_human` — la reescritura del Paso 3 cambia el criterio de admisión central de κ y debe ser firmada por Jacob (decisión H-J*). El borrador queda como propuesta sustantiva, no como edición aplicada.

RESULT: complete | F03-09-dimensionalidad-sin-protocolo | needs_human; borrador triple-estimador
