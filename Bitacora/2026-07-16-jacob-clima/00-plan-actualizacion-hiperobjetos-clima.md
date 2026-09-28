# Plan: actualizar la tesis precursora de Hiperobjetos e integrarla al problema del cambio climatico

**Fecha:** 2026-07-16 · **Sesion:** Jacob (Stev durmiendo, Jarvis asistiendo)
**Estatus:** nota de trabajo. NO modifica archivos canonicos. Para revision de Jacob + Stev.

## 0. Que es la precursora (linaje verificado en el repo)

- **Iteracion 1 (precursora), feb-2026, repo `TesisJacobContenidos`:**
  *"Irrealismo Operativo de Hiperobjetos: Clasificacion de Fenomenos por Grado de Cierre Operativo".*
  Hipotesis V0: los fenomenos multidominio se operacionalizan como **hiperobjetos** mortonianos
  (Morton 2013): entidades distribuidas en espacio-tiempo que exceden la captura intuitiva.
  De aqui nacen: metrica **EDI**, protocolo **C1-C5**, hibrido **ABM+ODE**, 29 casos con datos reales.
- **Iteracion 2, abr-2026, repo `EstructurasPreontologicas`:** la absorbio. El texto de la precursora
  sobrevive en `Bitacora/2026-04-27-integracion-jacob/00-tesis-fuente-original.md` + los 29 casos.
- La transicion V0->V5 esta narrada en `Bitacora/2026-04-28-iteraciones-IA/V5_documentos/EVOLUCION_NARRATIVA_V5_5.md`.

## 1. La evolucion ya hecha (no rehacerla: apoyarse en ella)

V0 hiperobjeto mortoniano (sustancia extendida postulada) -> V1-V3 patron estabilizado (atractor
empirico) -> V4 estructura pre-ontologica preliminar -> **V5 estructura pre-ontologica (def. tecnica)**.
Motivo del abandono de "hiperobjeto": carga peso metafisico de ente sustancial = **inflacion
ontologica encubierta**, choca con la anti-reificacion operativa. Morton NO se elimina: queda como
**heuristica de candidatura** (glosario, entrada "Hiperobjeto operativo": constructo que designa un
fenomeno con cierre operativo alto, sin existencia metafisica adicional).

## 2. El nudo: el clima es EL hiperobjeto de Morton, pero el aparato lo marca DEBIL

- Caso 01 clima (Budyko-Sellers linealizado, temperatura CONUS, forcings reales CO2/TSI/OHC/AOD, LoE 5):
  **EDI = 0.011, p = 0.999 -> Nivel 1 (trend)**. El acoplamiento macro no agrega poder predictivo sobre
  el forcing exogeno: a esa sonda/escala el clima regional es **senal forzada casi lineal**, no atractor
  acoplado emergente. El aparato NO falla: **discrimina honestamente**.
- En cambio, sub-estructuras del mismo problema climatico SI cierran, y de forma heterogenea:
  - Deforestacion (16): **EDI 0.602, overall_pass=True (Nivel 4, strong)**.
  - Microplasticos (24): **~0.78 (strong sin gate por bootstrap)**.
  - Urbanizacion (18): 0.236 (weak) · Fosforo (22): 0.192 (weak) · Salinizacion (21): 0.018 (suggestive).
  - Acuiferos (25), Oceanos, Contaminacion, Acidificacion oceanica: **null** (acidificacion en revision
    como falsificacion local, tarea H-J12).
- (Cifras exactas viven en `09-simulaciones-edi/<caso>/outputs/metrics.json`; reproducibles con `./tesis run`.)

**Tesis de la integracion (el titular):** "cambio climatico" NO es un hiperobjeto unico y viscoso;
es una **malla multiescala de estructuras pre-ontologicas acopladas con cierre operativo medible y
heterogeneo**. El One viscoso-nolocal de Morton se **disuelve en una pluralidad medida**. Eso es la
anti-reificacion vuelta empirica, y es exactamente lo que la precursora prometia y el aparato ahora entrega.

## 3. Como actualizar la precursora (acciones concretas)

1. **Reencuadre del titulo/marco:** de "Irrealismo Operativo de Hiperobjetos" a la aplicacion climatica
   como *cartografia de estructuras pre-ontologicas del sistema climatico*. Morton entra como epigrafe
   heuristico, no como ontologia.
2. **Sub-corpus clima (bajo costo, los casos ya existen):** agrupar clima 01 + deforestacion 16 +
   urbanizacion 18 + salinizacion 21 + fosforo 22 + microplasticos 24 + acuiferos 25 + oceanos +
   acidificacion + contaminacion en UNA cartografia climatica con narrativa unica y tabla de cierre.
3. **Programa multi-sonda con el clima como buque insignia** (roadmap #3 + limitacion #2). El EDI bajo del
   clima es *dependiente de sonda*. Añadir sondas alternativas: escala global vs regional; observables
   distintos (OHC, nivel del mar, hielo) en vez de solo temperatura; ventanas largas. Pregunta honesta:
   el clima es atractor acoplado emergente o senal forzada? La respuesta se **mide**, no se postula.
4. **Casos de acoplamiento inter-estructura (operacionalizar la 'no-localidad' de Morton):** construir
   casos donde una sub-estructura fuerza a otra (deforestacion->temp regional; acidificacion->fosforo/biol)
   y medir el EDI del **acoplamiento**. Eso convierte la no-localidad poetica en dependencia inter-escala medible.
5. **Retirar la deuda de datos sinteticos JUSTO aqui:** el clima tiene datos reales LoE 5 (IPCC AR6, CMIP6,
   instrumentales). El sub-corpus clima es el mejor lugar para elevar de sinteticos a reales (deuda declarada
   en tesis-fuente §15.2 y roadmap #3). Ganancia de credibilidad maxima con el minimo riesgo.
6. **Tabla puente Morton -> metrica operativa** (para la presentacion; ver §4).

## 4. Puente Morton -> operativo (rasgos del hiperobjeto traducidos a metrica)

- **No-localidad** -> EDI de acoplamiento inter-escala entre sub-estructuras (accion 3.4).
- **Viscosidad** (no podes salir del objeto) -> dependencia instrumento-fenomeno; todo resultado es el trio
  {fenomeno, instrumento, pregunta}, nunca el fenomeno aislado.
- **Ondulacion temporal** (fases de tiempo masivas) -> atractor multiescala de constantes de tiempo largas;
  ventanas de validacion largas en el programa multi-sonda.
- **Fasing / retiro** (nunca se da entero) -> EDI agregado bajo (0.011) con EDI de componentes alto:
  el objeto "clima" se retira como agregado pero se manifiesta por sus estructuras.
- **Interobjetividad** -> la malla acoplada ODE<->ABM: el objeto existe en la red de acoplamientos, no en si.

## 5. Guardrails (la honestidad ES el activo de credibilidad)

- La urgencia politica del clima tienta a reificar y a inflar EDIs debiles. **No.** El clima=trend se
  presenta como fortaleza discriminativa, no se esconde.
- Arrastrar sin lavar las deudas de la precursora: **p-value mal calibrado (error tipo I empirico ~24%,
  no 5%)**, composicion de corpus post-hoc, auditorias endogenas (falta lectura externa hostil). El umbral
  EDI si es robusto; el p-value no.
- Regla del repo: un cierre debe sobrevivir preguntas hostiles; si no, queda abierto.

## 6. Deuda residual de esta nota

- No verifique cada metrics.json caso por caso en esta sesion; las cifras provienen de la bitacora de
  integracion (2026-04-27) y tesis-fuente. Antes de citar en la presentacion, correr `./tesis run --case <c>`.
- El repo precursor `TesisJacobContenidos` no esta en /workspace (se fundio en iteracion 2); si Jacob quiere
  el texto original literal, esta condensado en `00-tesis-fuente-original.md`.
- La lista de sub-estructuras clima es propuesta de Jarvis; la seleccion final de que cuenta como
  "sistema climatico" es decision autoral de Jacob.
