"""
Sistema de calificación de calidad de evidencia (QES) — métrica ad-hoc del proyecto.

NOTA EXPLÍCITA: QES es métrica de diseño propio, NO estándar reconocido en
literatura de calidad de evidencia (no es GRADE, no es AMSTAR). Sirve como
filtro interno operativo del corpus EDI. Cualquier evaluador externo puede
inspeccionar la implementación y los pesos en este archivo y decidir si los
acepta o no como árbitro.

Componentes (suma de pesos = 1.0):

  Q0  Signo y potencia del EDI (precondición de afirmación robusta).
  Q1a Trazabilidad criptográfica del archivo de datos (SHA-256, presencia).
  Q1b Trazabilidad empírica (datos provenientes de observación física;
      los datos sintéticos derivados de parámetros publicados puntúan más
      bajo que los datos reales fetcheados).
  Q2  Tamaño efectivo (n y potencia estadística).
  Q3  Calidad de la sonda (protocolo con cita disciplinar).
  Q4  Reproducibilidad mecanizada (SETUP_HASH, git_commit, seed).
  Q5  Multi-sonda con penalización por divergencia inter-paradigma alta.
  Q6  Level of Evidence empírico (escala 1-5).
  Q7  Calibración estadística (block bootstrap, FWER, Newey-West).

Categorías y umbrales:

  ROBUSTO       QES ≥ 0.85  Y  Q0 ≥ 0.60  Y  Q1b ≥ 0.50.
                Sin Q0/Q1b adecuados, el caso no califica como ROBUSTO
                aunque su QES agregado sea alto. Esto evita el
                paper-science formal: infraestructura presente sin
                contenido empírico sustantivo.
  DEMOSTRATIVO  0.70 ≤ QES < 0.85, o QES ≥ 0.85 con Q0/Q1b bajos.
  PROGRAMÁTICO  0.55 ≤ QES < 0.70.
  PILOTO        0.40 ≤ QES < 0.55.
  INADMISIBLE   QES < 0.40.

El filtro QES es interno y orientativo. La afirmación "0 paper-science según
QES" debe interpretarse como "ningún caso cae bajo el umbral interno de 0.40";
una clasificación contra criterios externos (revisión por pares, GRADE) es
deuda explícita.
"""
from __future__ import annotations

import json
import math
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any


QES_WEIGHTS = {
    "Q0_signo_potencia_edi":      0.10,
    "Q1a_traza_criptografica":    0.10,
    "Q1b_traza_empirica":         0.15,
    "Q2_tamano_efectivo":         0.10,
    "Q3_calidad_sonda":           0.15,
    "Q4_reproducibilidad":        0.10,
    "Q5_multi_sonda_penalizada":  0.10,
    "Q6_loe_empirico":            0.10,
    "Q7_calibracion_estadistica": 0.10,
}
assert abs(sum(QES_WEIGHTS.values()) - 1.0) < 1e-9, "Pesos QES deben sumar 1.0"


@dataclass
class QualityComponent:
    score: float
    evidence: str
    raw: dict = field(default_factory=dict)


def _extract_phase(metrics: dict) -> dict:
    phases = metrics.get("phases") or {}
    phase = phases.get("real") or phases.get("synthetic")
    if isinstance(phase, dict):
        return phase
    return metrics if "edi" in metrics else {}


def _q0_signo_potencia(metrics: dict, case_dir: Path) -> QualityComponent:
    """
    Q0: precondición de afirmación robusta.

    Combina:
    - signo del EDI (negativo o cercano a cero descalifica para ROBUSTO);
    - potencia estadística (n suficiente para detectar el efecto declarado).

    Un caso con EDI ≤ 0 y panel grande NO es robusto: es null. Un caso con
    EDI alto pero potencia insuficiente no es robusto: es exploratorio.
    """
    phase = _extract_phase(metrics)
    edi_dict = phase.get("edi", {}) if isinstance(phase, dict) else {}
    edi = float(edi_dict.get("value", 0.0)) if isinstance(edi_dict, dict) else 0.0
    if edi == 0.0:
        edi = float(metrics.get("edi", 0.0))
    p_value = float(edi_dict.get("permutation_pvalue", 1.0)) if isinstance(edi_dict, dict) else 1.0
    if p_value == 1.0 and "p_value" in metrics:
        p_value = float(metrics.get("p_value", 1.0))

    n = 0
    if isinstance(phase, dict):
        data = phase.get("data") or {}
        n = data.get("val_steps") or data.get("steps") or 0
    panel = metrics.get("panel_aggregate_v5_5")
    if isinstance(panel, dict):
        n = int(panel.get("n_effective_total", n))
    n = int(n) if n else 0

    # Score base por signo del EDI
    if edi <= 0:
        signo_score = 0.0
        sign_msg = f"EDI={edi:+.3f} ≤ 0 (null o negativo)"
    elif edi < 0.10:
        signo_score = 0.30
        sign_msg = f"EDI={edi:+.3f} bajo umbral weak"
    elif edi < 0.30:
        signo_score = 0.70
        sign_msg = f"EDI={edi:+.3f} en rango weak"
    else:
        signo_score = 1.00
        sign_msg = f"EDI={edi:+.3f} en rango strong"

    # Penalización por p-value alto
    if p_value > 0.10:
        signo_score *= 0.5

    # Modulación por potencia (Cohen 1988): para detectar EDI=0.10 con α=0.05
    # potencia 0.80 requiere n≈124 con SE≈0.10
    if edi > 0:
        potencia_aprox = 1.0 / (1.0 + math.exp(-(n - 30) / 30.0))
        score = signo_score * (0.4 + 0.6 * potencia_aprox)
    else:
        score = signo_score

    return QualityComponent(
        score=float(min(score, 1.0)),
        evidence=f"{sign_msg}, p={p_value:.3f}, n={n}",
        raw={"edi": edi, "p_value": p_value, "n": n},
    )


def _q1a_traza_criptografica(metrics: dict, case_dir: Path) -> QualityComponent:
    """
    Q1a: presencia de FETCH_MANIFEST con SHA-256 verificable.

    Mide si el archivo de datos tiene cadena de custodia criptográfica.
    No mide veracidad empírica de los datos; eso es Q1b.
    """
    fetch = case_dir / "data" / "FETCH_MANIFEST.json"
    if not fetch.is_file():
        return QualityComponent(0.20, "sin FETCH_MANIFEST")
    try:
        m = json.loads(fetch.read_text())
    except Exception:
        return QualityComponent(0.30, "FETCH_MANIFEST presente pero ilegible")
    files = m.get("data_files") or []
    has_hashes = any(f.get("sha256") for f in files)
    if has_hashes:
        return QualityComponent(1.00, f"{len(files)} archivos con SHA-256")
    if files:
        return QualityComponent(0.70, f"{len(files)} archivos sin SHA-256 verificable")
    return QualityComponent(0.50, "FETCH_MANIFEST presente, sin archivos listados")


def _q1b_traza_empirica(metrics: dict, case_dir: Path) -> QualityComponent:
    """
    Q1b: trazabilidad empírica.

    Distingue:
    - datos reales descargados de fuente pública: 1.00
    - datos sintéticos derivados de parámetros publicados (literatura): 0.50
    - datos sintéticos ad-hoc generados por el equipo: 0.30
    - control de falsación (sintético por diseño): 0.20
    - sin información: 0.20
    """
    fetch = case_dir / "data" / "FETCH_MANIFEST.json"
    if not fetch.is_file():
        return QualityComponent(0.20, "sin información de origen")
    try:
        m = json.loads(fetch.read_text())
    except Exception:
        return QualityComponent(0.20, "FETCH_MANIFEST ilegible")
    is_synthetic = bool(m.get("is_synthetic", False))
    has_url = bool(m.get("source_url"))
    limitation = m.get("limitation") or ""

    if "control" in limitation.lower() or "falsación" in limitation.lower():
        return QualityComponent(0.20, "control de falsación (sintético por diseño)")
    if not is_synthetic and has_url:
        return QualityComponent(1.00, f"datos reales con URL: {m.get('source')}")
    if not is_synthetic:
        return QualityComponent(0.80, f"datos reales sin URL: {m.get('source')}")
    if is_synthetic and "publicados" in (m.get("source") or "").lower():
        return QualityComponent(0.50, "sintético derivado de parámetros publicados")
    if is_synthetic and "literatura" in (m.get("source") or "").lower():
        return QualityComponent(0.50, "sintético derivado de literatura")
    return QualityComponent(0.30, f"sintético ad-hoc: {m.get('source')}")


def _q2_tamano_efectivo(metrics: dict) -> QualityComponent:
    phase = _extract_phase(metrics)
    n = 0
    if isinstance(phase, dict):
        data = phase.get("data") or {}
        n = data.get("val_steps") or data.get("steps") or 0
    if not n:
        n = metrics.get("val_steps") or metrics.get("train_steps") or 0
    n = int(n) if n else 0
    panel = metrics.get("panel_aggregate_v5_5")
    if isinstance(panel, dict):
        n_eff = int(panel.get("n_effective_total", n))
        if n_eff > n:
            n = n_eff
    score = 1.0 / (1.0 + math.exp(-(n - 30) / 30.0))
    if n >= 100:
        ev = f"n={n}: potencia ≥ 0.80 para detectar EDI weak"
    elif n >= 30:
        ev = f"n={n}: tamaño aceptable; potencia ≈ 0.50"
    elif n >= 10:
        ev = f"n={n}: tamaño limitado"
    else:
        ev = f"n={n}: tamaño exploratorio"
    return QualityComponent(score=float(score), evidence=ev, raw={"n": n})


def _q3_calidad_sonda(metrics: dict, case_dir: Path) -> QualityComponent:
    proto = case_dir / "docs" / "protocolo_simulacion.md"
    arch = case_dir / "docs" / "arquitectura.md"
    has_proto = proto.is_file()
    has_arch = arch.is_file()
    notes = (metrics.get("notes") or "").lower()
    keywords = [
        "lindblad", "bloch", "tyson-novak", "hoffmann", "mackey-glass",
        "leavitt", "plummer", "lotka-volterra", "kermack", "budyko",
        "sellers", "von thünen", "jambeck", "fajen-warren", "carpenter",
        "maxwell", "fisher-kpp", "zeeman", "wolfram", "cook", "oxcgrt",
        "hale", "searle", "bunge", "stommel", "henry", "darcy",
        "fitzhugh", "king", "reimers", "heston", "soros", "taleb", "bass",
        "gompertz", "harris-todaro", "north", "kessler", "volterra",
        "daley", "kuhn", "markov", "hill", "goldbeter", "kramers",
        "kolmogorov", "petrovsky",
    ]
    cite_in_notes = any(k in notes for k in keywords)
    cite_in_proto = False
    if has_proto:
        try:
            cite_in_proto = any(k in proto.read_text(encoding="utf-8").lower() for k in keywords)
        except Exception:
            pass
    if has_proto and has_arch and (cite_in_proto or cite_in_notes):
        return QualityComponent(1.00, "protocolo + arquitectura + cita disciplinar")
    if has_proto and (cite_in_proto or cite_in_notes):
        return QualityComponent(0.85, "protocolo con cita disciplinar")
    if has_proto:
        return QualityComponent(0.65, "protocolo sin cita disciplinar verificada")
    if cite_in_notes:
        return QualityComponent(0.65, "cita en notes pero sin protocolo")
    return QualityComponent(0.40, "sin protocolo ni cita")


def _q4_reproducibilidad(metrics: dict, case_dir: Path) -> QualityComponent:
    setup_hash = case_dir / "SETUP_HASH.json"
    has_hash = setup_hash.is_file()
    git_commit = (metrics.get("git") or {}).get("commit")
    if not git_commit and has_hash:
        try:
            git_commit = json.loads(setup_hash.read_text()).get("git_commit")
        except Exception:
            pass
    has_seed = "seed" in str(metrics).lower()
    if not has_seed:
        for f in case_dir.rglob("*.py"):
            try:
                if "seed" in f.read_text(encoding="utf-8", errors="ignore").lower():
                    has_seed = True
                    break
            except Exception:
                pass
    score = 0.0
    parts = []
    if has_hash:
        score += 0.4
        parts.append("SETUP_HASH")
    if git_commit:
        score += 0.3
        parts.append(f"git {git_commit[:8]}")
    if has_seed:
        score += 0.3
        parts.append("seed fijo")
    return QualityComponent(score, " | ".join(parts) if parts else "sin reproducibilidad")


def _q5_multi_sonda_penalizada(metrics: dict, case_dir: Path) -> QualityComponent:
    """
    Q5: presencia de sonda secundaria, con criterio jerárquico.

    Distinción clave (Fallo F21): cuando dos sondas divergen, la asimetría
    de motivación teórica indica cuál es la sonda fiable. Una sonda
    primaria con cita disciplinar canónica + protocolo documentado tiene
    prior más alto que una sonda secundaria de prueba. La divergencia
    indica entonces que la SECUNDARIA es inadecuada, no que ambas lo sean.

    Reglas:
    - convergencia |Δ| ≤ 0.05: confirmación inter-paradigma robusta.
    - divergencia 0.05 < |Δ| ≤ 0.30: ambigua; reduce la confianza pero
      no descalifica la sonda primaria si tiene alto Q3.
    - divergencia |Δ| > 0.30: indica que la secundaria es inadecuada
      (o, menos probable, que ambas lo son). Q5 baja, pero no a 0.25
      si Q3 primaria es alta.
    """
    sec_path = case_dir / "outputs" / "secondary_probe_report.json"
    if not sec_path.is_file():
        return QualityComponent(0.40, "sin sonda secundaria")
    try:
        sec = json.loads(sec_path.read_text())
    except Exception:
        return QualityComponent(0.40, "secondary_probe_report ilegible")

    convergence = sec.get("convergence") or sec
    delta = convergence.get("delta_edi")
    if delta is None:
        delta_p = convergence.get("delta_inter_paradigma")
        if delta_p is not None:
            delta = float(delta_p)
    converge = bool(convergence.get("convergen", False))
    primary_arrays = (case_dir / "outputs" / "primary_arrays.json").is_file()

    if delta is None:
        return QualityComponent(0.55, "sonda secundaria presente sin Δ reportado")

    delta = float(delta)
    # Prior sobre la sonda primaria: si tiene protocolo + cita disciplinar
    # documentada en docs/, asumimos que la motivación teórica es robusta.
    proto_exists = (case_dir / "docs" / "protocolo_simulacion.md").is_file()
    primary_strong = proto_exists  # Q3 alto = sonda primaria fiable

    if delta <= 0.05 and primary_arrays:
        return QualityComponent(0.95, f"convergencia inter-paradigma sobre arrays reales (Δ={delta:.3f})")
    if delta <= 0.05:
        return QualityComponent(0.85, f"convergencia inter-paradigma sobre proxys (Δ={delta:.3f})")
    if delta <= 0.15:
        return QualityComponent(0.65, f"sonda secundaria con Δ moderado ({delta:.3f})")
    if delta <= 0.30:
        # Divergencia ambigua: si la primaria tiene protocolo robusto,
        # la secundaria probablemente es inadecuada (no ambas).
        score = 0.55 if primary_strong else 0.45
        return QualityComponent(score, f"sonda secundaria con divergencia (Δ={delta:.3f}); primaria tiene protocolo: {primary_strong}")
    # Divergencia alta. Si la primaria tiene protocolo, la inadecuación
    # cae sobre la secundaria; el caso primario sigue válido pero sin
    # confirmación inter-paradigma.
    if primary_strong:
        return QualityComponent(0.40, f"divergencia alta (Δ={delta:.3f}); sonda secundaria probablemente inadecuada (primaria con protocolo robusto)")
    return QualityComponent(0.25, f"divergencia alta inter-paradigma (Δ={delta:.3f}); al menos una sonda es inadecuada")


def _q6_loe_empirico(metrics: dict) -> QualityComponent:
    phase = _extract_phase(metrics)
    edi_dict = phase.get("edi", {}) if isinstance(phase, dict) else {}
    loe = float(edi_dict.get("loe_factor", 0)) if isinstance(edi_dict, dict) else 0
    score = float(loe) if loe else 0.4
    if loe >= 1.0:
        ev = "LoE 5 (datos físicos directos > 30 años)"
    elif loe >= 0.8:
        ev = "LoE 4 (series consistentes > 10 años)"
    elif loe >= 0.6:
        ev = "LoE 3 (datos estructurados)"
    elif loe >= 0.4:
        ev = "LoE 2 (datos digitales con ruido alto)"
    else:
        ev = "LoE 1 (especulativo o sintético)"
    return QualityComponent(score, ev)


def _q7_calibracion_estadistica(metrics: dict, case_dir: Path) -> QualityComponent:
    enriched = case_dir / "outputs" / "metrics_enriched_v5_2.json"
    if not enriched.is_file():
        return QualityComponent(0.30, "sin métricas calibradas")
    try:
        e = json.loads(enriched.read_text())
    except Exception:
        return QualityComponent(0.30, "métricas calibradas ilegibles")
    b1 = e.get("B1_calibration") or e
    p_block = b1.get("p_value_block_bootstrap_estimated") or e.get("p_value_block_bootstrap_estimado")
    fwer = b1.get("fwer_position_in_corpus") or {}
    survives = fwer.get("survives_fwer_at_alpha_0_05")
    if survives is None:
        survives = e.get("sobrevive_fwer", False)
    score = 0.5
    if p_block is not None:
        if p_block <= 0.05:
            score = max(score, 0.85)
        elif p_block <= 0.10:
            score = max(score, 0.70)
        elif p_block <= 0.30:
            score = max(score, 0.60)
    if survives:
        score = min(score + 0.15, 1.0)
    se = b1.get("newey_west_se_estimated")
    if se is not None:
        score = min(score + 0.05, 1.0)
    return QualityComponent(score, f"p_block={p_block}, FWER={survives}, SE_HAC={se}")


def quality_score(metrics: dict, case_dir: Path) -> dict:
    components = {
        "Q0_signo_potencia_edi":      _q0_signo_potencia(metrics, case_dir),
        "Q1a_traza_criptografica":    _q1a_traza_criptografica(metrics, case_dir),
        "Q1b_traza_empirica":         _q1b_traza_empirica(metrics, case_dir),
        "Q2_tamano_efectivo":        _q2_tamano_efectivo(metrics),
        "Q3_calidad_sonda":           _q3_calidad_sonda(metrics, case_dir),
        "Q4_reproducibilidad":        _q4_reproducibilidad(metrics, case_dir),
        "Q5_multi_sonda_penalizada":  _q5_multi_sonda_penalizada(metrics, case_dir),
        "Q6_loe_empirico":            _q6_loe_empirico(metrics),
        "Q7_calibracion_estadistica": _q7_calibracion_estadistica(metrics, case_dir),
    }
    qes = sum(QES_WEIGHTS[k] * c.score for k, c in components.items())

    q0 = components["Q0_signo_potencia_edi"].score
    q1b = components["Q1b_traza_empirica"].score

    # Filtros duros para ROBUSTO: necesita Q0 ≥ 0.60 (EDI positivo con
    # potencia razonable) y Q1b ≥ 0.50 (datos reales o sintéticos derivados
    # de parámetros publicados, no ad-hoc). Sin estos filtros, un caso con
    # infraestructura impecable pero EDI nulo o sintético ad-hoc clasificaría
    # como ROBUSTO, lo cual sería paper-science formal.
    if qes >= 0.85 and q0 >= 0.60 and q1b >= 0.50:
        category = "ROBUSTO"
        recommendation = "Apto para afirmación demostrativa."
    elif qes >= 0.85:
        category = "DEMOSTRATIVO"
        if q0 < 0.60:
            recommendation = (
                f"QES alto pero Q0={q0:.2f} insuficiente (EDI no positivo o "
                "potencia limitada). Caso con infraestructura adecuada y "
                "contenido empírico no robusto."
            )
        else:
            recommendation = (
                f"QES alto pero Q1b={q1b:.2f} insuficiente (datos sintéticos "
                "ad-hoc o sin trazabilidad empírica). Caso requiere elevación "
                "a datos reales para afirmación robusta."
            )
    elif qes >= 0.70:
        category = "DEMOSTRATIVO"
        recommendation = "Apto para afirmación demostrativa con limitaciones explícitas."
    elif qes >= 0.55:
        category = "PROGRAMÁTICO"
        recommendation = "Modo programático con criterios de elevación declarados."
    elif qes >= 0.40:
        category = "PILOTO"
        recommendation = "Caso piloto con limitaciones explícitas."
    else:
        category = "INADMISIBLE"
        recommendation = (
            "No satisface el piso interno. Reformular con datos reales y sonda "
            "físicamente motivada, declarar como hipótesis especulativa, "
            "o retirar como caso demostrativo."
        )

    role_note = _role_note_for_case(case_dir.name)
    if role_note:
        recommendation = f"{recommendation} {role_note}"

    return {
        "case_id": case_dir.name,
        "QES": float(qes),
        "components": {k: asdict(c) for k, c in components.items()},
        "category": category,
        "recommendation": recommendation,
        "weights": QES_WEIGHTS,
    }


def _role_note_for_case(case_id: str) -> str | None:
    if case_id in {
        "06_caso_falsacion_exogeneidad",
        "07_caso_falsacion_no_estacionariedad",
        "08_caso_falsacion_observabilidad",
    }:
        return ("Función específica: control de falsación. El caso debe rechazarse "
                "bajo FWER por diseño.")
    if case_id == "41_caso_wolfram_extendido":
        return ("Función específica: discriminación contra Wolfram. EDI agregado "
                "no debe converger inter-paradigma por diseño.")
    if case_id in {"02_caso_conciencia", "23_caso_erosion_dialectica"}:
        return ("Función específica: caso límite del aparato. Documenta "
                "operativamente los límites declarados en cap 04-02.")
    if case_id == "30_caso_behavioral_dynamics":
        return ("Función específica: caso ancla canónico, declarado con "
                "circularidad detectada en N2 (Fajen-Warren) y confirmada "
                "cuantitativamente por block bootstrap. Piloto metodológico "
                "hasta datos humanos reales (VENLab/WALK-MS).")
    if case_id == "38_locomocion_alternativa":
        return ("Función específica: failure mode declarado de la hipótesis "
                "tau-dot, documentando que no es el modelo correcto.")
    if case_id == "33_villin_headpiece":
        return ("Función específica: null honesto inter-escala. La sonda de "
                "equilibrio MSM dos estados no captura la dinámica completa "
                "de plegamiento.")
    return None


__all__ = ["quality_score", "QES_WEIGHTS"]
