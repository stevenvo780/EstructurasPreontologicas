# Bitácora pasada nocturna 2026-04-29

Iteración de la asistencia computacional bajo la directriz: **revisar la tesis y profundizar lo ejecutable, dejar deuda explícita en `TAREAS_PENDIENTES.md` para lo que requiera firma humana o re-ejecución larga**. Sigue las reglas de `CLAUDE.md` y del `REPORTE_AUTOINDULGENCIAS.md`.

---

## Lo cerrado en esta pasada

### B-F5 — ancla disciplinar de self-organization

`02-fundamentos/04-anclaje-conductual-ecologico.md` §4 reformulado: la sección canónica donde la tesis define self-organization ahora abre con dos citas textuales paginadas:

- Maturana y Varela 1980, *Autopoiesis and Cognition*, p. 78-79 (definición de organización viva como *"network of processes of production [...] that continuously regenerate and realize the network"*).
- Haken 1977, *Synergetics: An Introduction*, cap. 1 p. 1-7 y cap. 7 p. 191-204 (slaving principle como reducción de muchos modos a pocos).

Se añade además **convención del manuscrito**: cualquier ocurrencia textual de "self-organization", "auto-organización" o equivalentes remite a esta sección o se sustituye por "estabilización dinámica" / "convergencia a atractor". Se actualizaron 7 ocurrencias en cap 02-01, 04-01, 04-03, 05-02, 05-05, 06-cierre/02 y 06-cierre/04 con referencia cruzada explícita a 02-04 §4 y al par disciplinar (Maturana-Varela 1980, Haken 1977). Las 3 ocurrencias restantes (cap 02-01 §10 tabla, §14 evolución conceptual, 06-cierre/01 tabla) no requieren cita porque ya están en contextos donde el ancla es inmediato.

### B-F6 — sinónimos coloquiales

Convención del glosario operativo §"Sinónimos coloquiales del núcleo conceptual" satisface la métrica: el cuerpo usa "patrón estabilizado", "regularidad operativa", "estructura operativa" y "cuenca de atracción" como registros coloquiales declarados.

### B-T4 — Effective Information como métrica auxiliar

La función `effective_information(obs, full, reduced) = H(residuos_reducido) − H(residuos_completo)` ubicada en `09-simulaciones-edi/common/hybrid_validator.py:249` queda **declarada como métrica auxiliar, no central**. Decisión documentada en cap 03-04 §"Información efectiva como métrica auxiliar (declaración)" con tres aclaraciones:

1. NO es la Effective Information de Hoel-Albantakis-Tononi 2013 (definida sobre matrices de transición con intervención uniforme).
2. NO implica adopción de IIT (no se afirma phi, experiencia integrada, propiedad protoconsciente).
3. NO es árbitro del aparato: no entra en QES, no entra en `overall_pass`, no entra en la clasificación del paisaje de emergencia.

Se añadió entrada al glosario operativo §"Información efectiva (uso auxiliar)" para cerrar B-E4.

### B-E2 — uniformidad Chicago author-date

Auditados 19 patrones "X y Y (año)" frente a 0 "X and Y (año)" en cuerpo en español. Dos `&` decorativos en "Ladyman & Ross" detectados y corregidos a "Ladyman y Ross" (cap 04-04 y glosario). Sin anomalías persistentes.

### B-E1 — re-ensamblado del manuscrito

`python3 TesisFinal/build.py` ejecutado tras los cambios. **Resultado:** 633 056 bytes / 9 052 líneas. Sin errores de ensamblado.

### Auditoría hostil cap 02-01

Detectados y corregidos:

- **Cita Hoyos 1996 *Borradores para una fenomenología* (Cali: U. del Valle, p. 47)** no presente en bibliografía y con texto literal no verificable. Reformulado el §0.3 para mantener el diálogo con Hoyos sin reproducir cita textual paginada que la asistencia no pudo verificar al cierre. La voz autoral final del diálogo con Hoyos queda como tarea H-J5 de Jacob.
- **Cita Simondon 1958 *L'individuation*, p. 24** con texto literal en francés no verificado contra edición disponible. Reformulado el §0.2.2 para retener la formulación del concepto preindividual sin reproducir cita textual paginada hasta verificación contra edición consultada (Millon 2005 / PUF 1964 / Aubier 1989).
- **Bunge 1977 *Ontology I: The Furniture of the World*** citado en cuerpo §1.3 con p. 27 pero ausente en bibliografía. Añadido como entrada `4bis`.
- **Simondon 1958/2005 *L'individuation*** citado en múltiples capítulos sin entrada bibliográfica. Añadido como entrada `18bis`.

### Auditoría hostil cap 04-debates §04

Detectado y corregido en §7 (dimensiones omitidas):

- Cita decorativa "(Hoyos)" sin obra ni página — exactamente lo que F6 prohíbe. Reformulada la sección descolonial: las referencias Quijano 2000, Mignolo 2007, Castro-Gómez 2007 ahora traen obra y sección específica. La declaración de deuda descolonial se hace explícita y honesta como deuda declarada para pasada futura.

### Auditoría hostil cap 05-aplicaciones

Detectado y corregido en cap 05-06:

- Frases auto-elogiosas ("no más auto-indulgente", "tras hostile testing severo", "Esto NO es auto-indulgencia retórica") detectadas como patrón de declaración de honestidad sustituyendo demostración. Reformuladas a prosa técnica sin adjetivación retórica.

### Verificación de cifras EDI

- **Caso 31 (Decoherencia qubit):** manuscrito reportaba EDI=0.84 en tres ubicaciones (cap 02-01 Tabla 2.1.2, cap 05-06 Tabla 5.6.1, cap 10-A.12.1 Tabla A.12.1). El `metrics.json` actual (`09-simulaciones-edi/corpus_multiescala/31_decoherencia_cuantica/outputs/metrics.json`) reporta EDI=0.913. Las tres ubicaciones actualizadas a EDI=0.91 con CI [0.89, 0.93] donde aplica. **Cumple regla CLAUDE.md §4: prosa pierde, JSON gana.**
- **Caso 30 (Behavioral Dynamics):** manuscrito reporta EDI=0.262 con p=0.044, CI [0.249, 0.280]. `metrics.json` real-phase reporta EDI=0.255 con p_perm=0.517 (pero `permutation_significant: True` por bootstrap-CI). Los desfases en p y CI son grandes; no resoluble sin re-ejecución agresiva (n_perm=2999, n_boot=1500) que es lo que el manuscrito declara como perfil de verificación. **Registrado como tarea B-E5** en `TAREAS_PENDIENTES.md`.

### Bibliografía expandida

Añadidas ~30 entradas que el cuerpo cita pero la bibliografía no listaba:

- **Sección M (epistemología naturalizada):** Carnap 1950, Hacking 1983, Quine 1969, Sellars 1956.
- **Sección N (panpsiquismo, identidad):** Chalmers 1996, Goff 2019, Locke 1690, Parfit 1984, Reid 1785, Strawson 2006.
- **Sección O (deudas declaradas cap 04-04 §7):** Castro-Gómez 2007, Dewey 1934, Lefebvre 1974, Lewis 1991, Mignolo 2007, Mouffe 2005, Quijano 2000, Rancière 1995, Simons 1987, Whitehead 1929.
- **Sección P (información ecológica):** Bateson 1972, Dretske 1981, Floridi 2011.
- **Sección Q (análisis topológico):** Grassberger-Procaccia 1983, Haken 1977 (1.ª ed.), Rosenstein-Collins-De Luca 1993, Takens 1981.
- **Sección R (calibración estadística):** Holm 1979, Künsch 1989, Newey-West 1987, Politis-Romano 1994.
- **Sección S (mecánica cuántica realista):** DeWitt 1970, Everett 1957, Ghirardi-Rimini-Weber 1986, Zurek 2003.
- **Sección T (biología procesual y enactivismo):** Hutto-Myin 2013 y 2017, Thompson 2007.
- **Sección U (filosofía colombiana):** Bunge 1980, Hoyos 1986.

---

## Lo que sigue abierto y por qué

- **A.1, A.2, A.3 (humanas e institucionales):** sin cambio respecto a la pasada anterior. Designación de director (H-U1), plantilla institucional (H-U2), declaración de originalidad (H-U3), política IA (H-U4), tribunal (H-U5), revisores externos hostiles (H-S1, H-S2), coordinación con director (H-S3), decisión sobre caso 30 humano (H-S4), firma de Jacob para cap 04-debates §04 (H-J1) y cinco decisiones filosóficas H-J2…H-J6.
- **B-T1 (F13):** array_dump real para los 33 casos restantes del corpus inter-dominio. Cierre parcial 7/40 con datos reales + 25/40 reconstruidos honestamente desde RMSE (`RECONSTRUIDO_DESDE_METRICS`, `verified_real_data: false`). La extensión a real_data en los 25 casos requiere re-ejecución por caso.
- **B-T2 (F16):** elevación masiva de los 30 casos macro a datos reales descargables. 2 OOS verificadas (cefeidas OGLE-IV LMC, OWID CO2/GDP). Resto pendiente con cronograma 3-6 semanas.
- **B-E5 (nueva):** reconciliación EDI/p/CI caso 30 declarado en cuerpo vs `metrics.json` actual.
- **B-E6 (nueva):** auditoría completa caso por caso del corpus macro contra `metrics.json` real-phase. Caso 31 cerrado en esta pasada; los 29 restantes pendientes.

---

## Verificación

- Re-ejecución de `python3 TesisFinal/build.py`: 9 052 líneas, sin errores.
- `grep -c "EDI 0\.84.*Lindblad" TesisFinal/Tesis.md` = 0 (corrección caso 31 propagada).
- Cobertura self-organization: 17 ocurrencias auditadas, 14 con cross-ref explícita a 02-04 §4 (Maturana-Varela + Haken), 3 en contextos con anclaje inmediato.
- 19 patrones "X y Y (año)" en cuerpo, 0 "X and Y" — uniformidad Chicago en español OK.
- Bibliografía: ~30 entradas añadidas; cobertura de los autores citados en cuerpo verificada para Carnap, Hacking, Quine, Sellars 1956, Strawson, Goff, Locke, Reid, Parfit, Mouffe, Rancière, Quijano, Mignolo, Castro-Gómez, Bateson, Dretske, Haken 1977, Rosenstein 1993, Grassberger-Procaccia 1983, Takens 1981, Everett 1957, Zurek 2003, etc.

---

## Trazabilidad

- Documento maestro: `TAREAS_PENDIENTES.md` (raíz) — actualizado con B-E5, B-E6.
- Postura para iteraciones futuras: `CLAUDE.md` (raíz).
- Reporte previo de auto-indulgencias (lectura obligatoria antes de nueva pasada): `Bitacora/2026-04-28-iteraciones-IA/REPORTE_AUTOINDULGENCIAS.md`.
- Cierre técnico anterior: `Bitacora/2026-04-28-cierre-tecnico/REPORTE_CIERRE_TECNICO.md`.
- Cierre filosófico/técnico previo: `Bitacora/2026-04-29-cierre-filosofia-y-tecnico/00-bitacora.md`.

---

## Recordatorio metodológico

Esta pasada se hizo bajo directriz nocturna autónoma. Las decisiones tomadas son operativas dentro del régimen del aparato y respetan la regla de `CLAUDE.md`: cuando la prosa contradice el JSON, gana el JSON; cuando una cita textual paginada no se verifica, se elimina o paráfrasis con declaración de deuda; cuando un autor entra como cita decorativa, se sustituye por engagement con obra y sección o se retira; cuando una tarea no se cierra con contenido defendible bajo crítica hostil, **se deja abierta** en `TAREAS_PENDIENTES.md` antes que cerrarse mal.
