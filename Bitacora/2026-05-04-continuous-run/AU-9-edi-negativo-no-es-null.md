# AU-9 — "EDI<<0 listado como null genuino" (auditoría taxonómica)

Fecha: 2026-05-04
Estado: `needs_human` (B-T*) — la corrección requiere reetiquetar la categoría "Null" en 3 loci del manuscrito y firmar la nueva taxonomía.

## (a) Verificación de la afirmación adversarial

El reporte adversarial 2026-05-05 afirmaba: "Casos 23/07/08/29 con EDI<<0 (≤-0.876) listados como 'null genuino'". Verificación contra `outputs/metrics.json` (clave `phases.{synthetic|real}.edi.value`):

| Caso | Nombre | EDI | p_perm | valid | Categoría declarada |
|---|---|---:|---:|:-:|---|
| 02 | Conciencia | **-0.007** | 0.867 | False | Null |
| 03 | Contaminación | **+0.227** | **0.000** | False | Null |
| 07 | Falsación no-estac. | **-0.882** | 1.000 | False | Falsación rechazada (control) |
| 08 | Falsación observ. | **-1.000** | 1.000 | False | Falsación rechazada (control) |
| 12 | Paradigmas | **-0.144** | 0.787 | False | Null |
| 17 | Océanos | **+0.149** | **0.000** | False | Null |
| 19 | Acidificación | **+4.3e-5** | 0.001 | False | Null |
| 23 | Erosión | **-0.019** | 0.975 | False | Null |
| 25 | Acuíferos | **-0.022** | 0.270 | False | Null |
| 29 | IoT | **-0.010** | 0.992 | False | Null |

La afirmación literal del adversarial es **parcialmente incorrecta**:

- **Casos 07 y 08 NO están listados como "Null"** sino como "Falsación rechazada" — los EDI<<0 son por diseño (controles que deben fallar). El adversarial los confunde con la categoría null.
- **Casos 23 y 29 tienen EDI ≈ -0.02 y -0.01**, no ≤-0.876. La cifra "-0.876" del adversarial corresponde a 07, no a 23/29. Reportarlos como "EDI<<0" es exagerado.

## (b) El problema real, sin embargo, existe

Aunque la cita numérica del adversarial es errónea, **la crítica taxonómica subyacente sí aplica**, en otra forma:

1. **Heterogeneidad oculta dentro de "Null"**. Los 8 casos null mezclan:
   - **Null genuino |EDI|<0.05**: 02 (-0.007), 19 (+4e-5), 23 (-0.019), 25 (-0.022), 29 (-0.010). Cinco casos.
   - **Negativo moderado**: 12 Paradigmas (-0.144). Un caso. Esto NO es "ruido alrededor de cero"; es el modelo prediciendo peor con ODE acoplada que sin ella.
   - **EDI positivo y permutación significativa, pero `valid=False`**: 03 Contaminación (+0.227, p=0.000) y 17 Océanos (+0.149, p=0.000). Dos casos. Estos no son nulls; son **señales rechazadas por la batería C1-C5**, no por ausencia de señal.

2. **Implicación**. La frase del manuscrito "8 null" en `06-cierre/04-…:110`, `06-cierre/01-…:60` y `05-aplicaciones/07-…:33` colapsa tres regímenes empíricamente distintos en una sola etiqueta. Eso es exactamente el patrón de "categoría que hace que el conteo encaje" advertido en CLAUDE.md §1.

## (c) Propuesta de edición concreta (needs_human)

Reemplazar la fila "Null" por **tres filas operativamente distinguidas**:

| Subcategoría | N | Casos | Criterio |
|---|--:|---|---|
| Null genuino | 5 | 02, 19, 23, 25, 29 | \|EDI\|<0.05 y permutación no significativa |
| EDI negativo (modelo acoplado peor que sin acoplar) | 1 | 12 Paradigmas | EDI≤-0.10 |
| Señal rechazada por gate de validez | 2 | 03, 17 | EDI>0 y p<0.05 pero `valid=False` (C1-C5 incumplido) |

Loci a editar (3):
- `06-cierre/04-versiones-cortas-defensa.md:110`
- `06-cierre/01-conclusion-demostrativa.md:60`
- `05-aplicaciones/07-mapa-aplicaciones-corpus.md:33`

Adicionalmente, el caso 12 (Paradigmas, EDI=-0.144) requiere **análisis honesto del por qué la sonda predice peor con acoplamiento**. Hipótesis a documentar: la sonda ODE introduce sesgo sistemático (no ruido) por mala especificación; el ABM solo lo hace mejor. Esto NO es "no hay señal"; es "la sonda macro elegida es activamente inadecuada".

## Costo argumentativo declarado

- **Lo que se gana**: honestidad taxonómica; el lector ve que de 30 casos hay **5 nulls genuinos, 1 fallo de sonda macro, 2 señales rechazadas por C1-C5**, no "8 nulls". El relato de "el aparato disciplina honestamente" se refuerza, no se debilita: el aparato distingue tres modos de no-éxito.
- **Lo que se concede**: el conteo agregado "señal/no-señal" pasa de 15/30 ≡ 50% a un cuadro más matizado donde 2 casos (03, 17) cruzan el umbral de permutación pero fallan validez. La cifra "50%" del manuscrito se vuelve frágil sin nota al pie.
- **Lo que NO se concede al adversarial**: la afirmación literal "23/07/08/29 con EDI≤-0.876 listados como null genuino" es factualmente errónea; 07/08 son controles de falsación correctamente clasificados, 23/29 tienen EDI ≈ -0.02. El adversarial confundió números.

## Acción

- B-T (asistencia, mecánica): preparar parche con la subdivisión taxonómica en los 3 loci listados, sin tocar `Tesis.md` ni `metrics.json`. Pendiente.
- H-J (Jacob): firmar la nueva taxonomía (5/1/2 vs 8 null) y decidir si el caso 12 merece sección propia "fallo de sonda macro" o se subsume en deuda residual.

RESULT: complete | AU-9-edi-negativo-no-es-null | needs_human: subdivisión 5/1/2 vs 8 null
