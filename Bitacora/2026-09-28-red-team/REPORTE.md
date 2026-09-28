# Rondas adversariales 2026-09-28 — veredictos, verificación y cierres

Dos workflows red-team (10 + 16 agentes) + verificación directa propia de cada
fatal antes de actuar. Nada se marcó cerrado por testimonio ajeno.

## Ronda 1 — red-team-filosofia (complete=false, 4 fatales F1-F4)

Veredicto del juez contra prosa pre-rebase (mayo). Re-verificación propia
contra prosa post-rebase (julio, Jacob) + código:

- **F1 (generador≡sonda inter-escala): MECANISMO CONFIRMADO, CLAIM ABSORBIDO.**
  Código: `32_espin_orbita/run.py:24,28` vs `:37,40` (omega 0.3, coupling
  0.4·B idénticos) — verificado línea por línea. Pero 05-06 reescrito concede:
  "No demuestra... portabilidad computacional" (:7), "No elimina la
  posibilidad de que los generadores sintéticos favorezcan la estructura de
  sus propias sondas" (:51). Downgrade a limitación declarada. Resta pregunta
  (Jacob): etiqueta formal "peso ontológico cero".
- **F2 (EDI≠κ por definiens): EN PIE → H-J-NEW-F2-KAPPA (needs_human).**
  03-01 intacto (diff 2 líneas ajenas). EDI = ganancia predictiva; κ exige
  atractores/bifurcaciones. El manuscrito lo declara no-demostrado (06-01 §3:
  "que κ-pragmática implique κ-ontológica"). Vías: redefinir κ-pragmática ≡
  ganancia ablativa, o test topológico real (§4.3/§4.4).
- **F3 (equívoco demostrativa→procesal): ABSORBIDO.** 06-01 reescrito:
  "Conclusión y estado de la demostración", §3 "Qué no queda demostrado",
  "nombra el horizonte del programa y no el resultado demostrado" (:96),
  "No es defendible todavía como demostración cerrada" (:127). Lenguaje
  C4/C5 "sostenida" eliminado.
- **F4 (ancla viola regla admisión): RESUELTO UPSTREAM.** 05-05:7 "no demuestra
  la tesis general ni valida el EDI del caso 30", :9 "9 de 14... no
  demostración cerrada". El claim "dossier completo... se demuestra aquí" ya
  no existe.

## Ronda 2 — red-team-motor-datos (complete=false, 5 fatales M1-M5)

Todos re-verificados en fuente propia; 4 re-ejecutados número a número.

- **M1 (generator≡sonda load-bearing): CONFIRMADO, ya disclosed (05-06:51).**
  Caso 31: ctes gen≡sonda; EDI colapsa +0.69 con sonda de otra familia
  (juez, re-ejecutado). Sin cambio de código (régimen `edi_engine` distinto);
  registrado aquí como evidencia cuantitativa.
- **M2 (sondas secundarias decoran + seed muerto + reportes V5.4 stale):
  PARCIAL-FIX.** `rng` muerto eliminado (`independent_probes.py:90`, cero
  usos en archivo — verificado); sonda documentada determinista. Δ primario/
  secundario ≫0.05 y forcing-irrelevancia quedan como hallazgo documentado
  (las secundarias no confirman; tampoco se afirma que confirmen en prosa
  vigente). Reportes V5.4 divergentes → cubiertos por banners P1.
- **M3 (baselines/topology stale n=100 + seed abs(hash)): FIX.** Seed estable
  sha256 (`generate_array_dumps.py`); campo `provenance`
  HISTÓRICO-SINTÉTICO en ambos JSON + banners .md; prosa 02-01/05-07/06-03
  calificada. Re-ejecución sobre arrays reales bloqueada (n real 6-13).
- **M4+M5 (C1 vacuo + trend ciega gate): FIX COMPLETO.**
  `evaluate_c1`: epsilon relativo 1e-9 (antes `> 0` aceptaba 1e-14);
  `corr_threshold` vivo (default 0.3 = docstring; configs 0.5+ ahora rigen);
  rama-B fuera del gate, solo diagnóstica (prescripción M6 jul-2026);
  `trend_ok` en `overall_pass` + taxonomía strong (`warning` = ratio<0.5 y
  r2>0.7). `common/test_gate_fixes.py` 12/12.
  Re-runs 04(B-T2.1)/05/16/18/21/22: EDI bit-idénticos, 7 flips
  strong/True→weak/False (04syn, 05syn, 16/18syn+real, 21/22real).
  Corpus real: **0 strong / 0 overall_pass** (9 weak, 8 trend, 9 null,
  1 suggestive, 3 falsación). Prosa sincronizada (glosario, 03-07, 05-07,
  09-README Tabla reclasificaciones, banners `_extendido/` + P7/P8).

## Hallazgo de linaje B-T2.1 (propio, durante re-runs)

`case_runner` hardcodeaba `case_config.json`; el régimen estricto del caso 04
(EDI=0.1571, p_block) exige `case_config_b_t2_1.json` y se corría con swap
manual indocumentado (mi primer re-run dio EDI=0.4615, otro experimento).
Fix: `CASE_CONFIG_JSON`/arg + campo `config_file` en metrics.json (04
re-ejecutado canónico: EDI=0.1571 exacto). Documentado en VALIDACION.md §4,
05-07 §Reproducibilidad, 09-README §5. Trampa análoga pendiente en 20/24.

## Ronda de cierre + red-team sobre correcciones (2026-09-28T04:12Z, HEAD 3d8cc1f)

- Sentencia juez cierre: `complete=true`, `fatal=[]` (M4/M5 aguantan en
  lineal; bypass no-lineal probado con impacto corpus 0; E1–E10 verificados).
- Reconciliación e7e0adf (verificación directa propia, JSON gana): mapa
  filas 14/22/12/25/29/01 a canónico; hedges E6/E7/E8; comentarios E1/E2/E3;
  banner legacy E5; VALIDACION exacta; TAREAS TREND-NONLIN/EPS-DERIV/
  PROBE-DET abiertas, MAPA-REG cerrada.
- Red-team sobre e7e0adf: AF3/AF4 SOSTENIDOS; AF1/AF2 DEBILITADOS →
  3d8cc1f adopta regla máquina trend/null (`hybrid_validator.py:2008-2016`),
  01/28→trend, convención reescrita. `fatal[]` vacío. Rerun independiente
  caso 01 por red-team: EDI=0.0030, pass=False.
- Vercel prod Ready sirviendo 3d8cc1f (allow/deny + marcadores verificados).
- Síntesis completa: `harness/reports/2026-09-28-tesis-pass.md` (local,
  gitignore) — este REPORTE.md es su espejo versionado.

## Deudas abiertas por estas rondas

- H-J-NEW-F2-KAPPA, H-J-NEW-FALSIF-1 (condición (1) "los 4 overall_pass se
  desmoronan" SE DISPARÓ → decisión autoral), B-T-NEW-P-THRESH (p 0.01 vs
  0.05), B-E-NEW-EXTENDIDO (reescritura voz autoral), B-T-NEW-CLIMA-DATA,
  B-T-NEW-TREND-NONLIN, B-T-NEW-EPS-DERIV, B-T-NEW-PROBE-DET.
- Unresolved rondas (no re-ejecutados por mí): hostile 0/2000 y cruzado 0/12
  independientes; 13 condiciones C1-C5 línea por línea (solo C1 auditada a
  fondo); calibration.py/full_secondary_probes.py/preregistration.py.

## Comandos de re-verificación

- `09-simulaciones-edi/.venv/bin/python 09-simulaciones-edi/common/test_gate_fixes.py` → 12/12
- `python3 harness/cli.py verify --all` → 9/9 (2026-09-28 post-ripple)
- `CASE_CONFIG_JSON=case_config_b_t2_1.json python3 09-simulaciones-edi/04_caso_energia/src/validate.py` → EDI=0.1571
- Tabla flips pre/post: snapshots en `/tmp/preM4/*.json` (sesión; no versionados)
