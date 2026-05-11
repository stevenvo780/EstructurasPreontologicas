---
borrador: IA
requires: H-J*
propuesta_fecha: 2026-05-11
destino: 04-debates/01-debates-con-posiciones-rivales.md:6 ; 04-debates/03-tabla-comparativa-rivales.md:32
hallazgo: Bitacora/2026-05-04-continuous-run/F04-07-iit-tononi-omitida-de-rivales.md
tipo: nueva_subseccion + nueva_fila_tabla
---

## Diagnóstico

El cap 04-01:6 declara discriminación contra "catorce rivales filosófica y empíricamente identificables" y la Tabla 4.3.2 lista exactamente 14 filas. **Ninguna corresponde a la Integrated Information Theory (IIT) de Tononi y colaboradores.** IIT es la métrica formal de organización causal/integración más citada en filosofía de la mente y teoría de la consciencia desde 2008 y es el competidor más natural de EDI en el dominio del caso 02 (consciencia) — caso que la tesis ejecuta y reporta. La tesis menciona IIT sólo lateralmente en cap 02-05:132 para distanciarse, pero la lista de "14 rivales" deja a IIT fuera. Cualquier filósofo de la mente post-2010 leerá la omisión como evasión.

## Verificación

- `04-debates/01-debates-con-posiciones-rivales.md:6` — declaración pública "14 rivales".
- `04-debates/03-tabla-comparativa-rivales.md:32-47` — 14 filas listadas; IIT ausente.
- `02-fundamentos/05-temporalidad-y-causalidad.md:132` — única mención de IIT/Tononi como afinidad lateral con causal emergence, sin discriminación.
- PDF disponible: `07-bibliografia/Tononi - Integrated Information Theory (2016).pdf` (Tononi, Boly, Massimini & Koch 2016, *Nature Reviews Neuroscience* 17:450–461). Verificación literal del abstract:
  > "Integrated information theory […] argues that the physical substrate of consciousness must be a maximum of intrinsic cause–effect power and provides a means to determine, in principle, the quality and quantity of experience." (Tononi et al. 2016, p. 450, primera columna del abstract; cita verbatim contra PDF local mediante `pdftotext`.)
- PDFs de Tononi 2008 *Biological Bulletin* 215(3):216-242 y Oizumi-Albantakis-Tononi 2014 *PLoS Comput Biol* 10(5):e1003588 **no presentes** en `07-bibliografia/`. El argumento de discriminación se sostiene con Tononi et al. 2016 (presente) y se enriquece si se incorporan los anteriores tras `/fetch-biblio tononi 2008 biological bulletin` y `/fetch-biblio oizumi albantakis tononi 2014`.

## Texto propuesto (voz autoral filosófica de Jacob) — Opción 1 recomendada (añadir IIT como rival #15)

**En `04-debates/01-debates-con-posiciones-rivales.md:6`, cambiar "catorce rivales" → "quince rivales" y añadir, como nuevo §15 al final del capítulo:**

> ### §15. IIT (Integrated Information Theory) — Tononi y colaboradores
>
> La IIT formaliza la consciencia como un máximo local de **integrated information** (Φ) intrínseco al sustrato físico. En palabras de Tononi, Boly, Massimini & Koch (2016, *Nature Reviews Neuroscience* 17(7):450–461, p. 450 — verificable contra PDF local):
>
> > "Integrated information theory starts from the essential properties of phenomenal experience, from which it derives the requirements for the physical substrate of consciousness. It argues that the physical substrate of consciousness must be a maximum of intrinsic cause–effect power and provides a means to determine, in principle, the quality and quantity of experience."
>
> IIT comparte con esta tesis: (i) la apuesta por una métrica computable definida sobre estructura de dependencias; (ii) el rechazo del reduccionismo plano; (iii) la pretensión de operar sobre el sustrato material sin colapsarse en él. IIT se separa de esta tesis en cuatro puntos auditables:
>
> 1. **Dominio.** IIT está específicamente diseñada para consciencia. EDI es multidominio (40 casos en física, biología, economía, política, tecnología, conducta humana). Donde IIT opera, EDI también opera (caso 02); donde EDI opera, IIT no.
> 2. **Escala.** IIT define Φ sobre una escala maximizante única (la escala que maximiza el corte mínimo de información integrada). EDI opera con asimetría L1↔B↔L3↔S explícita y multiescalaridad operativa.
> 3. **Tratabilidad.** Φ es computacionalmente intratable a partir de ~10–12 nodos (Tononi 2008, *Biological Bulletin*; complejidad exponencial en el número de subconjuntos). EDI es escalable a cientos o miles de unidades vía ABM+ODE acoplado.
> 4. **Anclaje empírico.** EDI exige dossier de catorce componentes + filtro EDI con permutación 999 + bootstrap 500. IIT exige Φ > 0; los proxies prácticos (PCI de Massimini et al. 2013) operan en un régimen experimental distinto y no satisfacen el dossier completo.
>
> Cláusula de absorción: si Φ se vuelve tratable a escala arbitraria y se publican mediciones de Φ que discriminen entre el corpus EDI con `p_perm < 0.05` y los controles de falsación, esta tesis admite que IIT subsume el caso 02 con métrica superior. Hasta entonces, IIT y EDI coexisten como métricas complementarias en dominios distintos (IIT en consciencia, EDI en consciencia y catorce dominios más).
>
> Posicionamiento sobre el caso 02 (consciencia): la tesis no afirma haber resuelto el problema duro de Chalmers. El EDI reportado para el caso 02 es coherencia operativa de la sonda macro y no compite con Φ en su pretensión axiomática; queda como deuda residual hasta defensa la confrontación detallada EDI vs Φ sobre el mismo dataset.

**Añadir fila 15 en Tabla 4.3.2 (`04-debates/03-tabla-comparativa-rivales.md:32`):**

| # | Posición rival | A · sustrato | B · multiescala | C · dossier 14 | D · asimetría L1↔B↔L3↔S | E · escalabilidad | F · multidominio | Discriminada en |
|---|---|:--:|:--:|:--:|:--:|:--:|:--:|---|
| 15 | IIT (Tononi 2008, Tononi-Boly-Massimini-Koch 2016) | ✓ | parcial | ✗ | ✗ | parcial (intratable >12 nodos) | ✗ (sólo consciencia) | C, D, F + tratabilidad |

## Acciones técnicas derivadas

- **B-IIT-02:** fetch Tononi 2008 *Biological Bulletin* 215(3):216-242 y Oizumi-Albantakis-Tononi 2014 *PLoS Comput Biol* 10(5):e1003588; integrar cita verbatim de la definición de Φ tras `/fetch-biblio` y la operacionalización IIT 3.0.
- Actualizar bitácoras que repiten "14 rivales" para coherencia.

## Costo argumentativo declarado

- La cifra redonda "14 rivales" cae; cambio en cascada en defensas cortas y bitácoras.
- La tesis se compromete a defender que EDI y Φ son **comparables pero no equivalentes** (riesgo: lectura como "IIT-light"; mitigado por la cláusula explícita de dominio y la discriminación en C/D/F + tratabilidad).
- El caso 02 (consciencia) queda con deuda residual fechada (confrontación monográfica EDI vs Φ sobre mismo dataset post-defensa).
- Sin la edición: F04-07 queda como vector de objeción de un evaluador con formación en consciencia. Esa es la peor de las salidas posibles dado que el PDF para sostener la edición ya está en `07-bibliografia/`.
