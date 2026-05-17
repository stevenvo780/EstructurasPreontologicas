# Red-team adversarial — Patrón sistemático de downgrades con datos reales

**Fecha:** 2026-05-16
**Tarea:** cuestionamiento filosófico profundo de las implicaciones del patrón sistemático de downgrades detectado en iter 2-3 del loop nocturno.

## Contexto

El loop ha re-ejecutado 7 casos con datos reales:
- Strong real: 3 casos (16 Deforestación WB, 04 Energía OWID fallback, 20 Kessler NASA ODPO)
- Null real: 4 casos (01 Clima IPCC downgrade, 03 Contaminación WB PM2.5 downgrade, 19 Acidificación NOAA PMEL confirmado, 27 Riesgo Biológico WHO)
- Tasa downgrade: 2/7 (28%)

## Claim atacada

`06-cierre/01-conclusion-demostrativa.md` §1 línea 5: "La tesis del **irrealismo operativo de estructuras pre-ontológicas** se sostiene como **propuesta ontológica general multiescalar** validada operativamente sobre **40 casos del corpus EDI agregado**."

## Objeción A — Ioannidis 2005 Corolario 4 (verificado)

Cita textual verificada (Ioannidis, *PLoS Med* 2(8):e124, 2005, p. 698 col. 1):
> "The greater the flexibility in designs, definitions, outcomes, and analytical modes in a scientific field, the less likely the research findings are to be true. Flexibility increases the potential for transforming what would be 'negative' results into 'positive' results, i.e., bias."

**Aplicación al corpus EDI:** la tesis declara un protocolo C1-C5 más gate de permutación, pero la historia operativa del corpus es justamente lo que Ioannidis denuncia: 30 casos sintéticos calibrados post-hoc sobre el aparato, con flexibilidad analítica documentada en TENG-01, TENG-02, TENG-04, TENG-08. Cuando se aplican datos reales (no calibrables al aparato), 4/7 colapsan a NULL.

Esto **es exactamente el patrón predicho por Ioannidis**: la PPV del corpus sintético estaba inflada por bias por flexibilidad analítica.

## Objeción B — Gelman & Loken 2014 (PDF descargado iter 5)

Garden of forking paths: un investigador no necesita p-hackear conscientemente; basta con que las decisiones analíticas (qué sonda, qué ventana, qué umbral) sean contingentes a los datos vistos.

**Evidencias operativas en bitácora:**
- Caso 30 (Behavioral): EDI inicial 0.002 → "refinamiento de sonda al modelo Fajen-Warren" → weak. Forking path explícito.
- AU-9: subdivisión post-hoc de la categoría null en tres regímenes tras ver cifra adversarial.
- TENG-08: c1 = c1_relative OR c1_absolute (disyuntivo) — Bonferroni implícito no aplicado.

**Prueba decisiva pendiente:** pre-registro pre-ejecución (plantilla creada iter 5: `09-simulaciones-edi/PRE_REGISTRO_TEMPLATE.md`).

## Objeción C — Wasserstein-Lazar 2016 ASA (verificado)

ASA principio 3: "Scientific conclusions and business or policy decisions should not be based only on whether a p-value passes a specific threshold."
ASA principio 5: "p-value, or statistical significance, does not measure the size of an effect."

**Aplicación al caso 19:** EDI=-0.0047, CI=[-0.0054, -0.0041]. El CI excluye cero por la izquierda. **No es null — es falsificación local del aparato** (modelo acoplado predice peor que reducido). Llamarlo "null confirmado" era eufemismo.

## Recomendación: opción (c) endurecida

> "El aparato EDI es **protocolo de admisión y filtro de discriminación**; los 30 casos sintéticos del corpus inter-dominio constituyen **calibración y mapeo de cobertura del aparato**, no demostración positiva de generalidad ontológica. La evidencia positiva real son los **N casos que sobreviven B-T2 con datos reales independientes y pre-registro**."

Al cierre iter 5: N=5 strong reales (16, 04, 20, 18, parcial 09 weak), 3 null genuinos (01, 03, 27), 1 falsificación local (19).

**ACTUALIZACIÓN iter 5 — balance bidireccional:**
- Hay UPGRADES también: caso 09 Suggestive→Weak, caso 18 Weak→Strong.
- Patrón NO es solo downgrade — es calibración bidireccional.
- Esto modula la lectura adversarial: el aparato corrige tanto sobreestimaciones como subestimaciones del corpus sintético.

## Pendiente firma autoral H-J5/H-J6/H-J7

La reformulación opción (c) está aplicada como BORRADOR-IA en 5 lugares (06-01 §1, abstract ES/EN, defensa, resumen Ricardo, borrador respuesta). Jacob debe firmar o reformular.

## Bibliografía verificada

- Ioannidis 2005: `07-bibliografia/Ioannidis - Why Most Published Research Findings Are False (PLoS Med 2005).pdf` pp. 696-698.
- Wasserstein-Lazar 2016: `07-bibliografia/Wasserstein-Lazar - ASA Statement on p-values (Am Stat 2016).pdf` pp. 1-2.
- Gelman & Loken 2014: `07-bibliografia/Gelman Loken - Statistical Crisis in Science (2014).pdf` (descargado iter 5).
- Yablo 1998: `07-bibliografia/Yablo - Does Ontology Rest on a Mistake (1998).pdf` (descargado iter 5).
