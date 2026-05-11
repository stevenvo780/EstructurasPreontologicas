# Fase 4 — Índice del rescate restante (BORRADORES-IA)

**Fecha:** 2026-05-11
**Universo:** los RESCATAR del triage `02-triage-bitacora-huerfana.md` que no estaban ya cubiertos por la Fase 3 (top-5: AU-8, AU-3, AU-5, F03-07).
**Objetivo:** producir BORRADOR-IA por cada hallazgo verificable, dejando la firma filosófica final a Jacob (CLAUDE.md §3).
**Modo de trabajo:** read-only sobre el manuscrito y `metrics.json`; verificación contra fuente primaria (PDFs en `07-bibliografia/`, código en `09-simulaciones-edi/common/`, manifestos en `corpus_multiescala/`).

## Cómputo

- **RESCATAR identificados en la pasada de la columna "clasificación" del triage:** 32 ítems después de descontar los 4 ya procesados en Fase 3 (AU-8 ya aplicado al manuscrito; AU-3, AU-5, F03-07 ya en `borradores/F3-*.md`).
- **LISTO:** 32 (todos los identificados como remanentes).
- **DUDOSO_no_pdf:** 0 ítems sin borrador. Algunos LISTO declaran citas literales como "paginación pendiente de verificación tras fetch" — esto es deuda bibliográfica declarada, no falta de borrador.
- **DUDOSO_no_reproduce:** 0.

## Tabla maestra

| ID | clasificación final | borrador | requiere |
|---|---|---|---|
| AU-1 (Starlink val_steps=1) | LISTO | `F4-AU1-caso26-starlink.md` | H-J* |
| AU-2 (caso 27 CI cruza cero) | LISTO | `F4-AU2-caso27-bootstrap-cruza-cero.md` | H-J* |
| AU-4 (significance theater 21/22) | LISTO | `F4-AU4-significance-theater-21-22.md` | H-J* + B-T fetch Wasserstein-Lazar 2016 |
| AU-9 (EDI < 0 no es null) | LISTO | `F4-AU9-edi-negativo-no-es-null.md` | H-J* |
| F02-04 (Maturana-Haken tensión) | LISTO | `F4-F02-04-maturana-haken-tension.md` | H-J* + B-T fetch Thompson 2007 |
| F02-10 (doble rótulo realismo estructural) | LISTO | `F4-F02-10-realismo-estructural-doble-rotulo.md` | H-J* |
| F03-01 (κ bicondicional inverificable) | LISTO | `F4-F03-01-kappa-bicondicional.md` | H-J* (opcional fetch Glymour 1980) |
| F03-04 (traducción B↔L3 sin criterio) | LISTO | `F4-F03-04-traduccion-B-L3-sin-criterio.md` | H-J* |
| F03-08 (do-test vs ablación) | LISTO | `F4-F03-08-do-test-ablacion.md` | H-J* (cita Pearl 2009 p.23 verificable contra PDF local) |
| F03-10 (caso 30 circularidad estructural) | LISTO | `F4-F03-10-caso30-circularidad-parcial.md` | H-J* + B-T sonda alternativa Neural ODE/GP |
| F03-12 (Bunge reorganizan, no extienden) | LISTO | `F4-F03-12-bunge-reorganizar-no-extender.md` | H-J* + B-T fetch Bunge 1967 vol.2 completo |
| F04-02 (6/6 criterios internos) | LISTO | `F4-F04-02-tesis-criterios-internos.md` | H-J* (opcional fetch Bunge 1977 vol.3, Quine 1948) |
| F04-03 (Dennett *Real Patterns* mal leído) | LISTO | `F4-F04-03-dennett-real-patterns.md` | H-J* (cita Dennett 1991 p.40 **verificada contra PDF local**) |
| F04-05 (Trampa 1 corpus sintético) | LISTO | `F4-F04-05-trampa1-corpus-sintetico.md` | H-J* + B-T corregir `is_synthetic` en manifests |
| F04-07 (IIT/Tononi omitida) | LISTO | `F4-F04-07-iit-tononi-rival.md` | H-J* (cita Tononi et al. 2016 p.450 **verificada contra PDF local**) + B-T fetch Tononi 2008, Oizumi-Albantakis-Tononi 2014 |
| F04-09 (caso 30 v1→v2 cinturón protector) | LISTO | `F4-F04-09-caso30-cinturon-protector.md` | H-J* (commit `c6884fb` 2026-04-27 verificable vía `git log`) |
| F04-11 (caso 33 no novel fact) | LISTO | `F4-F04-11-caso33-no-novel-fact.md` | H-J* (cita Lakatos 1978 p.33 — paginación a verificar) |
| F05-04 (North/Ostrom/Williamson) | LISTO | `F4-F05-04-instituciones-north.md` | H-J* (citas North 1990 pp.3-5 **verificadas contra PDF local**) + B-T fetch Ostrom 1990, Williamson 1985 |
| F05-08 (14 criterios post-hoc Lakatos) | LISTO | `F4-F05-08-criterios-admision-post-hoc.md` | H-J* |
| F05-09 (EDI negativo como demostrativo) | LISTO | `F4-F05-09-edi-negativo-no-demostrativo.md` | H-J* (coordinada con F05-08) |
| F05-10 (casos 19, 26 promovidos sin sig.) | LISTO | `F4-F05-10-casos-19-26-trend-ilegitimo.md` | H-J* (coordinada con AU-1, TENG-05) |
| F05-11 (caso 30 doble elevación) | LISTO | `F4-F05-11-caso30-doble-elevacion.md` | H-J* |
| F06-02 (complementarismo neologismo) | LISTO | `F4-F06-02-complementarismo-pluralismo.md` | H-J* + B-T fetch Mitchell 2003 |
| F06-04 (5 escenarios = 3 + 1) | LISTO | `F4-F06-04-cinco-escenarios.md` | H-J* (cita Popper 1959 §6 — paginación a verificar) |
| TENG-01 (permutación iid temporales) | LISTO | `F4-TENG-01-permutacion-iid.md` | H-J* + B-T implementar block_permutation_test_edi |
| TENG-02 (bootstrap percentil sin BCa) | LISTO | `F4-TENG-02-bootstrap-percentil-BCa.md` | H-J* + B-T BCa + fetch DiCiccio-Efron 1996 |
| TENG-04 (C2 CPU/GPU semillas) | LISTO | `F4-TENG-04-c2-cpu-gpu-semillas.md` | H-J* + B-T unificar semilla CPU + re-correr corpus |
| TENG-05 (caso 19 inconsistencia interna) | LISTO | `F4-TENG-05-caso19-inconsistencia.md` | H-J* + B-T re-ejecutar caso 19 + assertion en write_outputs |
| TENG-08 (C1 OR-fallback) | LISTO | `F4-TENG-08-c1-or-fallback.md` | H-J* + B-T reclasificar `c1_absolute` como `c1_fallback` |
| TENG-10 (baselines target distinto) | LISTO | `F4-TENG-10-baselines-target.md` | H-J* + B-T Ruta 1 (baselines sobre primary_arrays.json:obs) |
| TENG-12 (hash MD5 no detecta inconsistencia) | LISTO | `F4-TENG-12-hash-inconsistencia-interna.md` | H-J* (decidir escalar canónico value vs weighted) + B-T `verify_internal_consistency.py` |
| TENG-13 (calibración objetivo no alineado) | LISTO | `F4-TENG-13-calibracion-objetivo.md` | H-J* + B-T sensibilidad en 3 casos |

## Hallazgos LISTOS de mayor impacto (top-5 dentro de F4)

Ordenados por defendibilidad bajo crítica hostil (CLAUDE.md §2) e impacto sobre múltiples capítulos:

1. **F04-07 — IIT/Tononi omitida.** La cifra "14 rivales" deja fuera al competidor más natural del aparato EDI en el dominio consciencia (caso 02). PDF de Tononi et al. 2016 disponible local; cita verbatim p.450 verificada. Impacto: lista pública en `04-debates/01:6` y Tabla 4.3.2 (`04-debates/03:32`). Un revisor de filosofía de la mente detecta la omisión en minutos.

2. **F04-03 — Dennett *Real Patterns* mal leído.** Cita verbatim p.40 verificada contra PDF local: la intervención que Dennett autoriza es interna al bit-map del Game of Life, no woodwardiana sobre sustrato físico externo. La equivalencia "ablación EDI = intervención woodwardiana" excede tanto a Dennett como a Woodward. Impacto: `04-debates/04 §5` (líneas 216-221) y por extensión a la narrativa de cada caso EDI en cap 09.

3. **TENG-05 — Caso 19 `metrics.json` mezclado.** Invariante violado: `weighted/loe = -0.000191 ≠ value = 0.7278`. La regla "gana el JSON" deja de tener sentido cuando el JSON es internamente contradictorio. Cruza con AU-1 (Starlink en cuarentena), F05-10 (reclasificar 19, 26 fuera de Trend), TENG-12 (hash MD5 no detecta el bug).

4. **F03-08 — `do`-test confundido con ablación de modelo.** Cita Pearl 2009 p.23 verificable contra PDF local. EDI no es `do`-test pearliano excepto en caso 30 VENLab; en 29/30 casos es ablación de modelo bajo supuestos identificadores no declarados. Impacto: §4.3-4.4 y §12.1 de `03-formalizacion/01-aparato-formal.md` + Tabla 3.6.2.

5. **F05-04 — Instituciones sin North/Ostrom/Williamson.** PDF de North 1990 ya en `07-bibliografia/`; citas pp.3-5 verificadas contra extracción `pdftotext` directa. La omisión es injustificable porque el PDF está disponible; el capítulo se reposiciona como refinamiento materialista del neoinstitucionalismo, no como ontología social novedosa. Impacto: cap 05-04 §1.2, §6 nuevo §6.6, §7.1.

## DUDOSO_no_pdf (autores y obras pendientes de `/fetch-biblio`)

Ningún ítem RESCATAR remanente quedó sin borrador por ausencia total de PDF; cada borrador LISTO declara sus dependencias bibliográficas como deuda fechada. La lista agregada de PDFs que un próximo `/fetch-biblio` aceleraría:

- **Block-permutation / bootstrap dependiente:** Davison & Hinkley 1997 *Bootstrap Methods*; DiCiccio & Efron 1996 *Statistical Science*.
- **Filosofía de la ciencia:** Glymour 1980 *Theory and Evidence*; Forster & Sober 1994 *BJPS*; Bunge 1967 *La Investigación Científica* vol. 2 edición Ariel completa (los PDFs locales son scans parciales); Bunge 1977 *Treatise on Basic Philosophy* vol. 3; Quine 1948 "On What There Is" *Review of Metaphysics*; Mitchell 2003 *Biological Complexity and Integrative Pluralism*; Chalmers 1996 *The Conscious Mind* (los Chalmers locales son obras distintas); Wasserstein & Lazar 2016 *American Statistician*; Ioannidis 2005 *PLoS Medicine*.
- **Filosofía de la mente / consciencia:** Tononi 2008 *Biological Bulletin* 215(3); Oizumi-Albantakis-Tononi 2014 *PLoS Comput Biol* 10(5); Block 1995 access/phenomenal; Varela 1996 neurofenomenología.
- **Cognición / memoria / fenomenología:** Thompson 2007 *Mind in Life*; Damasio 1999; LeDoux 2002; Tulving 1972; Botvinick-Cohen 1998; Tsakiris 2010.
- **Economía institucional:** Ostrom 1990 *Governing the Commons*; Williamson 1985 *The Economic Institutions of Capitalism*; Hale et al. 2021 OxCGRT.
- **Otros:** Lakatos 1978 p.33 (paginación contra edición local); Lakatos 1978 pp.116-122 sobre ad hoc rescue tipo 3; Popper 1959 *LSD* §6 sobre inmunización (paginaciones a verificar contra ediciones locales presentes).

## DUDOSO_no_reproduce

Ninguno. Cada hallazgo técnico (AU-1, AU-2, AU-4, AU-9, TENG-01 a TENG-13) se reprodujo contra `metrics.json` o contra `hybrid_validator.py` línea a línea durante la verificación de la Fase 4.

## Capítulos más afectados (por número de borradores que les apuntan)

| Capítulo destino | Nº de borradores que lo modifican |
|---|--:|
| `05-aplicaciones/07-mapa-aplicaciones-corpus.md` | 7 (AU-1, AU-2, AU-4, AU-9, F05-08, F05-09, F05-10, F05-11) |
| `06-cierre/01-conclusion-demostrativa.md` | 5 (AU-2, AU-9, F06-04, además de los ya aplicados AU-3, AU-5) |
| `06-cierre/04-versiones-cortas-defensa.md` | 4 (AU-1, AU-2, AU-9, F04-05) |
| `06-cierre/05-respuestas-tipo-defensa.md` | 4 (F04-05, F04-09, F06-02 P5, además del ya aplicado en parte) |
| `03-formalizacion/01-aparato-formal.md` | 2 (F03-01, F03-08, además del ya aplicado F03-07) |
| `04-debates/03-tabla-comparativa-rivales.md` | 2 (F04-02, F04-07) |
| `04-debates/04-anticipacion-objeciones-filosoficas.md` | 2 (F04-03, F04-11) |
| `03-formalizacion/04-operacionalizacion-de-kappa.md` | 2 (F03-01, F03-04) |
| `03-formalizacion/05-etica-y-gobernanza-de-datos.md` | 2 (F03-04, F03-10) |
| `04-debates/05-limitaciones-declaradas-consolidacion.md` | 3 (TENG-04, TENG-05, TENG-08) |
| `02-fundamentos/01-ontologia-material-relacional.md` | 1 (F02-04) |
| `02-fundamentos/02-epistemologia-de-la-compresion.md` | 1 (F02-10) |
| `02-fundamentos/04-anclaje-conductual-ecologico.md` | 1 (F02-04) |
| `02-fundamentos/06-protocolo-empirico.md` | 2 (TENG-01, TENG-02) |
| `00-proyecto/07-glosario-operativo.md` | 6 (F02-04, F03-01, F03-10, TENG-01, TENG-04, TENG-08, TENG-13) |
| `05-aplicaciones/04-instituciones-mercado-y-estado.md` | 1 (F05-04) |
| `05-aplicaciones/00-criterios-de-admision.md` | 1 (F05-08) |

## Acciones derivadas priorizadas

**B-T inmediatas ejecutables por asistencia (sin firma humana, sin tocar manuscrito ni `metrics.json` por hook):**
1. Calcular `ACF(lag=1)` sobre `obs_val` de los 40 casos del corpus inter-dominio para diagnóstico de F4-TENG-01.
2. Auditar `is_synthetic` vs `source` en los 10 manifests del corpus inter-escala (F4-F04-05) y producir parche pendiente de aplicación.
3. Implementar borrador de `verify_internal_consistency.py` (read-only, no modifica `metrics.json`) y ejecutarlo sobre el corpus completo para identificar todos los casos con inconsistencia tipo TENG-05.
4. Ejecutar `git log` sobre cada caso del corpus para detectar otros patrones tipo F04-09 (commit que introduce sonda + ejecuta + reporta en una sola atomic unit).

**B-T mayores que requieren firma Jacob/Steven:**
1. Re-ejecutar `validate.py` caso 19 (F4-TENG-05) — bloqueado por hook que protege `metrics.json`.
2. Implementar `block_permutation_test_edi` / `block_bootstrap_edi` y re-correr corpus (F4-TENG-01).
3. Implementar BCa en `bootstrap_edi` y re-correr los 21 casos con `val_steps < 30` (F4-TENG-02).
4. Unificar semilla CPU/GPU en `evaluate_c2` y re-correr corpus (F4-TENG-04).
5. Implementar sonda alternativa en caso 30 (Neural ODE o GP) y reportar `delta_vs_fajen_warren` (F4-F03-10).
6. Reclasificar `c1_absolute` como `c1_fallback` diagnóstico (F4-TENG-08) y re-correr 8 fases afectadas.
7. Implementar Ruta 1 de F4-TENG-10 (baselines sobre `primary_arrays.json:obs`).

**`/fetch-biblio` próximas (priorizadas por cobertura sobre borradores):**
- Tier 1 (afecta varios borradores): Lakatos 1978 paginación precisa, Bunge vol.2 y vol.3 completos, Mitchell 2003, Chalmers 1996.
- Tier 2 (afecta deuda residual técnica): Davison-Hinkley 1997, DiCiccio-Efron 1996, Forster-Sober 1994, Glymour 1980.
- Tier 3 (filosofía de la mente y memoria): Tononi 2008, Oizumi-Albantakis-Tononi 2014, Thompson 2007, Block 1995, Damasio 1999, LeDoux 2002, Tulving 1972, Varela 1996, Botvinick-Cohen 1998, Tsakiris 2010.
- Tier 4 (instituciones): Ostrom 1990, Williamson 1985, Hale et al. 2021.

## Costo declarado de la pasada

- Naturaleza del aporte (CLAUDE.md §3): 90 % asistencia técnica (lectura de bitácoras origen, verificación contra fuentes primarias disponibles localmente, redacción de borradores, índice y enlace cruzado), 10 % Jacob (firmas pendientes en cada borrador).
- Ninguno de los 32 borradores modifica `Tesis.md`, `metrics.json` ni los capítulos del manuscrito. Todos quedan en `Bitacora/2026-05-11-sintesis-tesis/borradores/F4-*.md` esperando firma humana antes de aplicarse al manuscrito mediante una pasada coordinada.
- La voz autoral filosófica final es de Jacob (CLAUDE.md §3); los borradores ofrecen redacciones defendibles con costos declarados, no decisiones cerradas.
