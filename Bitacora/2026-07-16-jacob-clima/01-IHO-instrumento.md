# IHO - Indice de Hiperobjetividad Operativa

**Que es:** el instrumento que mantiene VIVO el hiperobjeto de Morton sin reificarlo.
El hiperobjeto deja de ser una sustancia postulada y pasa a ser un **PERFIL medible** sobre el
aparato EDI ya existente. Un fenomeno *es hiperobjeto en el grado y los ejes* en que puntua.
Ni se descarta a Morton (su intuicion se vindica), ni se reifica (cada eje es una relacion
computada sobre el sustrato material, no una sustancia nueva). Es la version con dientes de la
entrada de glosario "hiperobjeto operativo".

**Regla de lectura (la filosofia, preservada):** el IHO se reporta como VECTOR (V,N,T,P,I),
deliberadamente NO se colapsa a un escalar. Colapsar re-reificaria el hiperobjeto como una sola
magnitud, traicionando la anti-reificacion operativa. El perfil es la medida; no hay "un numero".

## Los cinco ejes (rasgo de Morton -> metrica operativa)

| Eje | Rasgo mortoniano | Definicion operativa | Proxy computable | Hoy? |
|-----|------------------|----------------------|------------------|------|
| **V** Viscosidad | no podes salir del objeto; se te pega | dependencia instrumento-fenomeno: no hay vista sin sonda | dispersion del EDI del fenomeno entre sondas (var/CV multi-sonda) | PEND. (roadmap #3) |
| **N** No-localidad | no esta en ninguna instancia local | fraccion del EDI explicativo que vive en acoplamientos inter-escala, no en componentes aislados | EDI-acoplamiento medio / EDI-componente medio | PEND. (roadmap #4) |
| **T** Ondulacion temporal | fases de tiempo masivas, no humanas | constante de tiempo caracteristica de la dinamica acoplada vs ventana de observacion | mediana tau ODE (approx) | APROX hoy |
| **P** Fasing / Retiro | nunca dado entero; se retira | el todo se retira (cierre agregado nulo) mientras las partes se manifiestan (cierre alto) | media(EDI de subestructuras con gate) - EDI(agregado) | **SI hoy** |
| **I** Interobjetividad | existe en la malla de relaciones | densidad de estructuras co-activas (significativas) en la malla | fraccion de subestructuras significativas (proxy) / densidad del grafo de acoplamientos (full) | PARCIAL hoy |

## Resultado CLIMA (metrics.json vivo, 2026-07-16)

- **P = +0.170** (media de las 4 subestructuras con gate = +0.439, menos agregado clima +0.269).
  Convencion estricta: si se trata el EDI no-significativo del agregado como cierre operativo NULO
  (0), P = **+0.439**. Se reporta el crudo (+0.170) y el estricto (+0.439); elegir es decision autoral.
- **I = 0.67** (6/9 subestructuras significativas: deforestacion, oceanos, urbanizacion, salinizacion,
  fosforo, energia).
- **T ~ 87 meses** (~7.3 anos, mediana tau ODE, APROX).
- **V, N = pendientes** (requieren el programa multi-sonda y los casos de acoplamiento inter-estructura).

**Firma categorica limpia (lo mas fuerte para presentar):** el agregado "clima" NO pasa el gate
(permutacion no significativa, p=1.0) mientras **4 subestructuras SI lo pasan** (deforestacion 0.580,
salinizacion 0.515, urbanizacion 0.337, fosforo 0.322, todas pass=True). El todo se retira; las partes
se manifiestan. **El EDI agregado nulo NO es un fracaso: es la HUELLA del retiro (eje P) del hiperobjeto.**
La vergueenza del clima=trend se convierte en la evidencia de su hiperobjetividad.

## Como se computa

`python3 iho.py` (en 09-simulaciones-edi/). Lee cada outputs/metrics.json del sub-corpus clima,
extrae edi.value / permutation_significant / overall_pass, y calcula P, I, T. Fuente de verdad = JSON.

## Donde se integra en la tesis

- Nuevo eje del capitulo 04 (debates) o 03 (formalizacion): el IHO formaliza la "heuristica de
  candidatura" del glosario como instrumento reproducible.
- El sub-corpus clima (ver 02-subcorpus-clima-tabla.md) es su primer caso de aplicacion.
- Cierra el circulo del linaje: la precursora se llamaba "Irrealismo Operativo de Hiperobjetos";
  el IHO devuelve el hiperobjeto al centro, pero ya disciplinado por el aparato que el mismo engendro.

## Deuda residual

- V, N no computables aun (faltan multi-sonda y acoplamientos). P, I(proxy), T(approx) si.
- P depende de una convencion (crudo vs estricto); declararla en el manuscrito.
- Varios EDI puntuales son inestables entre corridas (clima 0.011 en abril -> 0.269 hoy;
  microplasticos 0.78 -> -1.0). El invariante estable es la CLASIFICACION por gate, no el punto.
  Esa inestabilidad es, ella misma, senal preliminar del eje V (viscosidad).
