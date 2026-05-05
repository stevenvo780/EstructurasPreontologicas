# F04-05 — Trampa 1: corpus inter-escala sintético, riesgo de circularidad

**Fecha:** 2026-05-04
**Origen:** adversarial-reviewer cap04+06 2026-05-05
**Archivos auditados:**
- `06-cierre/04-versiones-cortas-defensa.md:188-190` (Trampa 1)
- `06-cierre/05-respuestas-tipo-defensa.md:67-71` (P8)

## (a) Verificación de la afirmación

**Afirmación literal en el manuscrito (04-versiones-cortas-defensa.md:190):**
> "el corpus agregado de 40 casos cubre dominios y escalas que están **muy lejos** de behavioral dynamics: dinámica de espín-órbita atómica, decoherencia cuántica, plegamiento de proteína, ciclo celular, dinámica gravitacional de cúmulos globulares. La generalidad multiescalar (10⁻¹⁰ m a 10²⁰ m) elimina la objeción 'es behavioral dynamics renombrado'."

**Lo que confirma la inspección del repo:**

Los casos del corpus inter-escala citados como prueba de generalidad **son sintéticos**. Evidencia directa en los manifest:

- `corpus_multiescala/31_decoherencia_cuantica/data/FETCH_MANIFEST.json` →
  `"source": "Sintético Lindblad — parámetros transmón NIST/IBM"`
- `corpus_multiescala/40_cumulos_globulares/data/FETCH_MANIFEST.json` →
  `"source": "Sintético Plummer — parámetros Gaia DR3"`

El campo `is_synthetic: false` **contradice** literalmente al campo `source` ("Sintético …") en los mismos manifests — bug de marcado, pero el origen sintético es explícito.

**Circularidad operativa real:**

La sonda macro que el aparato EDI prueba en cada uno de estos casos **es la misma ODE que generó la serie temporal**. Lindblad genera la traza y Lindblad es probada. Plummer genera la dinámica gravitacional y Plummer es probada. Tyson-Novak genera el ciclo celular y Tyson-Novak es probada. La afirmación "10⁻¹⁰ a 10²⁰ m elimina la objeción behavioral-dynamics-renombrado" no se sostiene como **discriminación empírica**: lo único que muestra es que un solver numérico de ODE recupera los datos que un solver numérico de ODE produjo, lo cual es trivialmente cierto y **no atestigua generalidad ontológica**.

Esto es exactamente la **trampa que la propia tesis denuncia** en cap 03 cuando exige distinguir entre "ajustar paramétricamente la fenomenología" y "tener una sonda mecanísticamente correcta". El corpus inter-escala, tal como está, comete la primera y la presenta como segunda.

## (b) Propuesta de edición concreta

Reformular Trampa 1 (04-versiones-cortas-defensa.md:188-190) y P8 (05-respuestas-tipo-defensa.md:67-71) para distinguir **dos niveles** de evidencia inter-escala:

**Reformulación propuesta (Trampa 1):**

> **Respuesta:** la defensa empírica de la generalidad descansa en los casos macro con datos reales que pasaron umbrales strong: 16 deforestación (Hansen/MapBiomas), 04 energía, 05 epidemiología, 18 urbanización, 20 Kessler, 27 riesgo biológico, 42 histeresis institucional. El corpus inter-escala (10⁻¹⁰ m a 10²⁰ m) **no es evidencia adicional empírica**: son simulaciones sintéticas de Lindblad, Plummer, Tyson-Novak, etc., donde la sonda probada coincide con la ODE generadora — su función es **conjetura de aplicabilidad** y prueba mínima de no-degeneración numérica del aparato fuera de su dominio macro original, no demostración de generalidad. La generalidad multiescalar es **conjetura abierta fechada**, no resultado. La objeción "behavioral dynamics renombrado" se refuta por los casos macro reales listados, no por los 30 órdenes de magnitud sintéticos.

**Reformulación propuesta (P8):**

> **Respuesta:** behavioral dynamics es un caso entre 40, y la generalidad de la tesis no descansa en él ni en su réplica multiescalar sintética. Descansa en los casos macro con datos públicos reales (16 deforestación, 04, 05, 18, 20, 27, 42) que superan umbrales strong bajo permutación 999. El corpus inter-escala 10⁻¹⁰–10²⁰ m es sintético (Lindblad, Plummer, Tyson-Novak…) y se reporta como **conjetura de aplicabilidad**, no como prueba empírica de generalidad. Confundir ambos niveles sería precisamente la trampa que la tesis denuncia.

**Costo argumentativo declarado:**

- Se renuncia a la frase de impacto "30 órdenes de magnitud cubiertos" como evidencia y se la rebaja a conjetura.
- La pretensión "ontológica general multiescalar operativamente articulada con demostración parcial" (04-versiones-cortas-defensa.md:198) **debe revisarse**: la palabra *demostración* sólo aplica al subconjunto macro-real; el resto es *conjetura demostrada formalmente consistente con el aparato*.
- La afirmación cap 06-02 §4 P12 sobre el corpus inter-escala como evidencia inter-escala fuerte queda debilitada y debe declarar lo sintético explícitamente.
- Ganancia: la tesis deja de ser vulnerable al ataque de circularidad sonda↔generador; gana defensibilidad a costa de una pretensión inflada.

## (c) Estado

**needs_human (Jacob).** La reformulación toca el alcance público de la pretensión inter-escala — decisión filosófica que no puede cerrarse desde la asistencia. Se propone como borrador para que Jacob decida entre:

1. Aceptar la rebaja a conjetura (recomendado por defendibilidad).
2. Reemplazar al menos un caso del corpus inter-escala por datos reales independientes de la sonda (p.ej. Gaia DR3 directo, no parámetros de Plummer; transmón IBM Quantum Experience real, no Lindblad simulado), antes de defender 30 órdenes de magnitud como evidencia.
3. Mantener la formulación actual asumiendo el costo de ser refutable por este vector — desaconsejado.

Tarea derivada técnica abierta: corregir el campo `is_synthetic: false` en los `FETCH_MANIFEST.json` del corpus inter-escala que reportan `source: "Sintético …"` — es inconsistencia interna grave (B-T*).

**No se editó Tesis.md ni metrics.json.**

RESULT: complete | F04-05-trampa1-corpus-sintetico | reformulación propuesta, needs_human Jacob
