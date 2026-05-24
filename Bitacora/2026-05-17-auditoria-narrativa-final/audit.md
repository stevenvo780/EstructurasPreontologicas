# Auditoría narrativa final de la tesis completa

**Fecha:** 2026-05-24 (sello declarado por usuario: 2026-05-17).
**Alcance:** `TesisFinal/Tesis.md` (9177 líneas, 759 KB) tras limpieza radical post-loop nocturno iter 18.
**Verificador:** process-verifier (proceso, no resultado).

---

## 1. Estructura global (formato académico)

| Componente | Estado | Locus |
|---|---|---|
| Portada + autoría | OK | L1-L56 |
| Resumen ES + Abstract EN bilingüe | OK | L166-192 |
| Información bibliográfica + citation suggestion | OK | L200-213 |
| Listas figuras/tablas/abreviaturas | OK (numeración A.9.x + 0.6.x **dual**) | L222-368 |
| Glosario operativo | OK | L376-674 |
| TOC colapsable (HTML `<details>`) | OK | construido por `build.py` |
| Introducción (pregunta, tesis, H1-H7) | OK | L676-760 |
| Estado del arte (5 subcampos) | OK | L762-900 |
| Parte I (cap 1-6 fundamentos) | OK | L912-2343 |
| Parte II (cap 7-14 aparato y método) | OK | L2345-4372 |
| Parte III (cap 15-24 evidencia) | OK | L4374-6655 |
| Parte IV (cap 25-29 discusión) | OK | L6657-7717 |
| Parte V (cap 30-31 cierre) | OK | L7720-8311 |
| Bibliografía consolidada | OK | L8313-8720 |
| Apéndices técnicos (3) | OK | L8725-9177 |
| Paginación coherente | N/A (Markdown; PDF generado por `build_pdf.py`) | — |

**Diagnóstico:** la tesis **sí cumple el formato académico** esperado (introducción → marco → metodología → resultados → discusión → conclusión + bibliografía + apéndices). Tablas y figuras tienen doble numeración (legacy A.x + canónica X.y), lo que es ruidoso pero no defectuoso.

---

## 2. Continuidad argumental (propiedad A)

### Lo que funciona

- La cadena **pregunta central (L685) → tesis principal (L691) → tres marcos generales (L697-699) → H1-H7 (L715-721)** está bien anudada. El lector sabe qué afirma y cómo lo justifica.
- La definición técnica de **estructura pre-ontológica** (L962-964, cuatro condiciones) se mantiene consistente desde el cap 02-01 hasta el cap 06-01 §5.1.
- Los **cinco operadores (μ, G, H, κ, ε)** se introducen en cap 7 (L2350) con función definida y se reutilizan sin desviación en cap 8, 12 y 30.
- La **asimetría L1↔B↔L3↔S** se define en cap 02-04 §8 (L1969) y se invoca de forma estable como protocolo formal hasta el cierre.
- El **dossier de 14 componentes** se introduce en cap 9 (L2961) y se referencia uniformemente; el caso ancla Warren declara cobertura 9/14 con deudas explícitas (L4834), lo cual es honesto.
- La **distinción κ-pragmática vs κ-ontológica** está presente en cap 02-01 §Nota (L1041-1071) y se sostiene en cap 06-01 §5.1 y §8.2.

### Saltos detectados

1. **SALTO CRÍTICO 1 — Contradicción de cifras corpus inter-dominio.** Tres conteos incompatibles aparecen simultáneamente en el manuscrito ensamblado:
   - Resumen ES (L174) y Abstract EN (L188): "**0 strong robusto puro**, 1 candidato (caso 26), 1 weak validado (caso 04), **4 falsificaciones locales (19, 20, 23, 24)**, 9 nulls genuinos, 3 controles rechazados".
   - Estado del arte §7 (L884): "**6 strong gate completo, 1 strong sin gate, 7 weak con disclosure, 4 trend, 8 null subdivididos en 6 genuinos + 1 EDI negativo + 1 falsificación local, 3 controles**".
   - Cap 06-01 §1 Condición 5 Tabla 6.1.1 (L7783-7796): "**0 Strong robusto puro, 1 candidato (26), 1 Weak validado (04), 3 weak más, 1 suggestive, 2 trend, 9 null genuino, 1 EDI negativo, 4 falsificación local (19, 20, 23, 24)**".
   - Cap 05-07 Resumen ejecutivo Tabla 5.7.1 (L4583-4594): "**8 Strong gate completo, 1 Strong sin gate, 4 Weak, 1 Suggestive, 2 Trend, 8 Null genuino, 1 EDI negativo, 2 Falsificación local (19, 23)**".
   - Bloque I Tabla 5.7.3 (L4634-4641) lista **8 casos strong** incluyendo Energía=0.6503, Microplásticos=0.806, Behavioral=0.614, Kessler=0.353.
   - Cap 29 Tabla 4.5.1 L1 (L7540): "**los 6 casos macro `overall_pass=True` tras pre-registros B-T2**".
   - Cap 29 Tabla 4.5.6 (L7644-7650): clasifica casos en categorías nuevas (robusto / marginal / sensible) sin reconciliar con el conteo de cap 05-07.

   **Esto es la inconsistencia más grave del manuscrito.** El cap 05-07 (mapa corpus) reporta cifras de fase histórica/canónica con `Microplásticos EDI=0.806 strong`; el cap 06-01 (conclusión) reporta el régimen B-T2.1 genuino donde Microplásticos colapsa a EDI=-1.0 (falsificación local) y Kessler también cae a Null/Falsificación. **El abstract sigue al cierre del cap 06-01, pero el mapa de aplicaciones del cap 05-07 no fue actualizado.** Un lector externo que lea Parte III (cap 17 ancla → cap 18 corpus → cap 19 multiescala → cap 20 caso 30) verá "8 strong"; al llegar a Parte V (cap 30) leerá "0 strong puro". Esa contradicción rompe el hilo narrativo en el momento más crítico.

2. **SALTO 2 — Caso 30 Behavioral con dos clasificaciones simultáneas.** En cap 05-07 Bloque I (L4640) aparece como "Strong gate completo, EDI=0.6143, Google Mobility real". En cap 06-01 §8.2 (L8012) aparece como "circularidad detectada por N2, p≈0.978 no significativo, piloto metodológico hasta datos humanos reales". En el abstract (L174) la cifra original "Nivel 3 weak" (que coincidía con el estado del arte L875) ya no figura. Tres descripciones inconsistentes del mismo caso.

3. **SALTO 3 — Microplásticos (caso 24).** Cap 05-07 Tabla 5.7.3 lo cuenta como Strong con EDI=0.8057. Cap 06-01 §5.4 (L7936) lo declara **colapsado a EDI=-1.0** bajo B-T2.1. Las dos celdas conviven sin nota de reconciliación; sólo Tabla 6.1.1 lo lista entre las 4 falsificaciones locales.

4. **SALTO 4 — Tres categorías de "modo" sin transición clara.** Cap 15 (criterios admisión, L4441) introduce "modo técnico-ejecutado" como tercera categoría sin que el lector haya visto su necesidad. La distinción demostrativo / programático / técnico-ejecutado es introducida en `[BORRADOR-IA · requires: H-J*]` y no fluye desde el cap 14 (ética) ni anticipa el cap 17 (caso ancla). El lector tiene que aceptar la trifurcación sin transición argumentativa.

5. **SALTO 5 — Cap 29 §5.5 introduce Tabla 4.5.6 con veredictos nuevos (robusto, marginal, sensible, evaluación específica) que no coinciden con ninguna de las clasificaciones de cap 05-07 ni cap 06-01.** El módulo de calibración estadística produce una **cuarta taxonomía** que sólo se reconcilia parcialmente con las anteriores. El lector queda con cuatro mapas del mismo corpus.

### Continuidad de términos centrales

| Término | Definición estable | Uso consistente |
|---|---|---|
| Irrealismo operativo | L703-705 + L1048-1052 | sí |
| EDI = 1 - RMSE_coupled/RMSE_no_ode | L172 + L7755 + L2849 | sí |
| Dossier 14 componentes | L2961 + plantilla cap 10 (L3224) | sí |
| C1-C5 (+8 extras = 13 condiciones) | L172 + L7755 + tabla glosario L313 | sí |
| Asimetría L1↔B↔L3↔S | L1969 + tabla glosario L343-348 | sí |
| κ, ε, μ, G, H | cap 7 (L2350) + glosario L290-294 | sí |
| 40 casos = 30 + 10 | L174 + L4556 + L7942 | sí |

**Diagnóstico continuidad:** los términos están bien definidos y usados consistentemente. **El hilo narrativo se rompe en las cifras del corpus**, no en los conceptos. La tesis filosófica (tres marcos) sobrevive; el respaldo empírico exhibe contradicción interna.

---

## 3. Honestidad metodológica (propiedad B)

**Lo que la tesis hace bien:**
- Cap 06-01 §2 reduce 5 escenarios de fracaso a 3+1 con criterio Popper-ad-hoc (L7821). Esto es auto-corrección filosófica honesta.
- Cap 06-01 §3.6 (L7869-7877) admite que ARIMA/VAR superan al acoplado en Deforestación y Riesgo Biológico, y reduce el alcance sin disolver la tesis.
- Cap 06-01 §5.4 (L7934-7938) declara que el último Strong robusto (caso 24) colapsó bajo B-T2.1 genuino; lo presenta como virtud del aparato.
- Cap 06-01 §8.2 lista 8 "no afirma" explícitos (L8009-8018) incluyendo AUC-ROC=0.886 como coherencia interna, no validación externa.
- Cap 29 consolida 20 limitaciones con plazo y entregable (L7536-7592).

**Lo que rompe la honestidad:**
- La afirmación "**los 40 casos son justificación operativa, no son la tesis**" (L174, L701, L7914, L7942) es consistentemente declarada, pero **el cap 05-07 sigue describiendo el corpus como cartografía positiva con 8 strong**. Si los 40 casos no son la tesis, **el cap 05-07 debería estar reescrito para reflejar el conteo B-T2.1**. No lo está.
- "**Defensa por proceso, no por acumulación**" (L7737) coexiste con frases que sí acumulan: "**discrimina y detecta cierre operativo en cartografía agregada de 40 casos**" (L7942). Las dos posiciones son compatibles si se declaran como simultáneas con costos, pero el manuscrito no lo declara.
- AUC-ROC = 0.886 se reporta como "coherencia interna" en cap 06-01 §5.5 (L7955) pero en el abstract (L174) aparece sin esa cualificación. El abstract heredó el régimen viejo.

---

## 4. Voz autoral y BORRADOR-IA (propiedad C)

- **28 marcadores H-J/H-U/H-S** y **18 BORRADOR-IA** vivos. La mayoría son honestos (declaran qué espera firma), pero algunos sí rompen el flujo:
  - L196 (abstract): "`[BORRADOR-IA — pendiente firma autoral H-J5/H-J6/H-J7]`" inmediatamente después del abstract. Visualmente impacta al lector externo.
  - L7773, L7801, L7877, L7962: marcadores BORRADOR-IA en mitad de la conclusión demostrativa. Esto se reconoce en L7729 ("no representan trabajo incompleto del aparato"), pero un lector externo no familiarizado con el repo verá "pendiente firma" cuatro veces en el cap 30.
  - L6664: el cap 25 (Debates) abre con un párrafo entero de meta-trazabilidad ("consolidación D.2 [...] decisiones pendientes Jacob (1)(2)(3)"). Esto es deuda visible pero rompe la voz autoral filosófica.
- **H-U1 (director no declarado formalmente) está sin resolver** y es bloqueador procedimental único (L7896). Esto NO rompe el flujo narrativo pero sí impide la sustentación.

---

## 5. Preguntas hostiles (propiedad D)

- **¿Un lector externo entiende qué es "irrealismo operativo" tras leer cap 02-01?** Sí. La definición técnica está en L1048-1052 y los criterios κ-pragmática/κ-ontológica están en L1055-1073.
- **¿La transición cap 02→03 explica por qué necesitamos el aparato formal?** Parcialmente. Cap 02-04 §11 (L2040) anuncia el aparato como consecuencia del nivel B; cap 03-01 §1 (L2357) abre con la tesis del aparato mínimo. La transición está, pero es seca; el "puente" entre fundamentos y aparato podría ser más explícito.
- **¿Cap 04 anticipa las objeciones de un tribunal hostil?** Sí. Cap 27 (anticipación objeciones, L7085-7434) trata F1, F2, F3, F5, F6, F9, F10 con esquema "objeción / concesión / distinción / argumento / costo". Es la mejor sección de defensa de la tesis.
- **¿Cap 06 cierra honestamente?** Sí, **dentro del cap 06-01**. El problema es que **el cap 06-01 no reconcilia su cuenta canónica con el cap 05-07**. La conclusión es honesta pero parcialmente desconectada del cap 17-20.
- **¿Hay capítulos sobrantes / redundantes?** Cap 26 (Tabla comparativa rivales) y cap 25 (Debates con rivales) se solapan; cap 25 ya declara "matriz síntesis 15×6 está en cap 26". Cap 29 (Limitaciones consolidadas) duplica parcialmente cap 28 (Riesgos heredados). Cap 8 (Mapa operadores formales) duplica con cap 7 (Aparato formal). El manuscrito reconoce estas consolidaciones D.1/D.2/D.3, pero no las ejecuta del todo.
- **¿BORRADOR-IA H-J* rompen el flujo?** En frontmatter sí (L196). En cuerpo argumental son aceptables si el lector entiende la convención. En conclusión (cap 30) son frecuentes y visualmente molestos.

---

## 6. Tres fortalezas narrativas

1. **Cap 27 (anticipación objeciones).** Esquema objeción/concesión/distinción/argumento/costo aplicado a 7 fallos. Es prosa filosófica con engagement primario citado (Ladyman-Ross PNC verbatim p.37-38, Whitehead PR pp.27-32, Dewey *Art as Experience* pp.15-17, Friston 2010 p.2-3, Clark 2013 p.1+p.19, Wasserstein-Lazar 2016).
2. **Cap 02-01 §0.1-§0.2 (definición pre-ontológico Simondon).** Aclara qué sentido del prefijo "pre" se adopta y cuáles se rechazan. Declara Simondon como referencia primaria sin citar paginación verbatim (deuda H-J5 declarada). Eso es honestidad estructural.
3. **Cap 06-01 §3.6 (baselines lineales superan).** El manuscrito admite que ARIMA/VAR superan al acoplado en 2/8 strong y reduce alcance sin disolver la tesis. Reformulación lakatosiana real, no retórica.

---

## 7. Diagnóstico final

**La tesis tiene sentido narrativo de principio a fin con caveats serios pero acotados.**

Los **conceptos filosóficos** fluyen bien: ontología → epistemología → aparato → operadores → dossier → caso ancla → aplicaciones → debates → cierre. Los **términos centrales** se usan consistentemente.

Los **números del corpus** no fluyen. La auto-corrección B-T2.1 está incorporada en el cap 06-01 y en el abstract, pero el cap 05-07 (mapa corpus) y la Tabla 5.7.3 del Bloque I siguen reportando el conteo viejo (8 strong, Microplásticos=0.806, Behavioral=0.614). Cap 29 introduce una cuarta clasificación (robusto/marginal/sensible) que no se reconcilia con ninguna anterior.

**WARN_BROKEN_STEP — needs_human:** Reconciliar cap 05-07 con cap 06-01 §1. Sin esa reconciliación, un lector externo encontrará tres mapas del mismo corpus en el mismo manuscrito y la afirmación "0 strong puro" del abstract será contradicha por "8 strong" del Bloque I del cap 17-18.

