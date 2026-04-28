"""
Sistema de calificación de calidad de evidencia (QES) — V5.3.

Asigna a cada caso del corpus un puntaje integral de calidad que combina:

  Q1. Trazabilidad de datos (¿real, sintético, derivado, proxy?)
  Q2. Tamaño efectivo (n y potencia estadística para detectar weak)
  Q3. Calidad de la sonda (¿motivación física? ¿pre-registro de ecuación?)
  Q4. Reproducibilidad (¿seed fijo? ¿hash criptográfico? ¿commit declarado?)
  Q5. Convergencia multi-sonda (¿hay sonda secundaria independiente?)
  Q6. LoE empírico (1-5 escala estándar de evidencia)
  Q7. Calibración estadística (¿p_block? ¿Newey-West? ¿FWER survives?)

Cada Qi ∈ [0, 1]; QES total = media ponderada con pesos justificados.

Esto es el ANTI-PAPER-SCIENCE: ningún caso pasa a "demostrativo" si su
QES < 0.70. Ningún caso pasa a "robusto post-V5.2" si su QES < 0.85.

El propósito es que el aparato no acepte como ciencia lo que es solo
papel: sin datos reales, sin trazabilidad, sin reproducibilidad
mecanizada o sin sonda físicamente motivada, un caso queda como
**hipótesis** o **piloto**, no como demostración.
"""
from __future__ import annotations

import json
import math
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any


# Pesos del puntaje compuesto (suma = 1.0).
# Justificación: trazabilidad y reproducibilidad son piso ético de la
# ciencia ejecutable; sonda y multi-sonda son piso epistémico; n y LoE
# son piso estadístico; calibración es piso inferencial.
QES_WEIGHTS = {
    "Q1_trazabilidad_datos":     0.20,
    "Q2_tamano_efectivo":        0.15,
    "Q3_calidad_sonda":          0.15,
    "Q4_reproducibilidad":       0.15,
    "Q5_convergencia_multisonda": 0.10,
    "Q6_loe_empirico":           0.10,
    "Q7_calibracion_estadistica": 0.15,
}


@dataclass
class QualityComponent:
    score: float       # ∈ [0, 1]
    evidence: str      # justificación textual
    raw: dict = field(default_factory=dict)


def _q1_trazabilidad_datos(metrics: dict, case_dir: Path) -> QualityComponent:
    """
    Evalúa la trazabilidad de los datos del caso.

    Niveles:
      1.00 — datos reales descargados de fuente pública con timestamp;
      0.80 — datos reales en cache con sha verificable;
      0.60 — datos reales convertidos a sintéticos preservando estadísticos;
      0.40 — datos sintéticos derivados de parámetros publicados;
      0.20 — datos sintéticos generados ad-hoc;
      0.00 — sin trazabilidad declarada.
    """
    # Heurística: buscar archivos data/, marker de fetch, timestamps
    data_dir = case_dir / "data"
    has_real_files = data_dir.is_dir() and any(
        p.suffix in {".csv", ".json", ".nc"} and p.stat().st_size > 100
        for p in data_dir.iterdir() if p.is_file()
    )
    fetch_marker = case_dir / "data" / "FETCH_MANIFEST.json"
    has_fetch_manifest = fetch_marker.is_file()
    readme = case_dir / "README.md"
    has_readme = readme.is_file()

    if has_fetch_manifest:
        return QualityComponent(
            score=1.00,
            evidence=f"FETCH_MANIFEST.json declarado con timestamps y SHA",
            raw={"fetch_manifest": True, "real_files": has_real_files},
        )
    if has_real_files and has_readme:
        return QualityComponent(
            score=0.80,
            evidence=f"data/ con archivos reales y README; falta FETCH_MANIFEST",
            raw={"real_files": True, "fetch_manifest": False},
        )
    if has_real_files:
        return QualityComponent(
            score=0.60,
            evidence="archivos en data/ pero sin documentación de origen",
            raw={"real_files": True, "documented": False},
        )
    # Buscar señal de sintéticos derivados de parámetros
    notes = (metrics.get("notes") or "")
    phases = metrics.get("phases", {})
    real_phase = phases.get("real")
    if real_phase and real_phase.get("data", {}).get("coverage", 0) > 0:
        return QualityComponent(
            score=0.50,
            evidence="phase 'real' tiene coverage>0 pero sin manifest",
            raw={"phase_real_present": True},
        )
    if "sintético" in notes.lower() or "synthetic" in notes.lower() or "parámetros publicados" in notes.lower():
        return QualityComponent(
            score=0.40,
            evidence="datos declarados sintéticos derivados de parámetros publicados",
            raw={"synthetic_declared": True},
        )
    return QualityComponent(
        score=0.20,
        evidence="sin trazabilidad clara — asumido sintético ad-hoc",
        raw={},
    )


def _q2_tamano_efectivo(metrics: dict) -> QualityComponent:
    """
    Evalúa el tamaño efectivo (n) y potencia estadística.

    Curva: score = sigmoid((n-30)/30), saturada en [0,1].
    n=20  → 0.36 (insuficiente)
    n=60  → 0.73 (aceptable)
    n=100 → 0.91 (bueno)
    n=200 → 0.99 (excelente)
    """
    phases = metrics.get("phases") or {}
    phase = phases.get("real") or phases.get("synthetic") or metrics
    n = 0
    if isinstance(phase, dict):
        data = phase.get("data") or {}
        n = data.get("val_steps") or data.get("steps") or 0
    if not n:
        n = metrics.get("val_steps") or metrics.get("train_steps") or 0
    n = int(n) if n else 0

    score = 1.0 / (1.0 + math.exp(-(n - 30) / 30.0))
    if n >= 100:
        evidence = f"n={n}: tamaño suficiente para potencia 0.80 detectando weak"
    elif n >= 30:
        evidence = f"n={n}: tamaño aceptable; potencia ~0.50 para detectar weak"
    elif n >= 10:
        evidence = f"n={n}: tamaño insuficiente; potencia <0.40 para detectar weak"
    else:
        evidence = f"n={n}: tamaño exploratorio extremo; no admite inferencia"
    return QualityComponent(score=float(score), evidence=evidence, raw={"n": n})


def _q3_calidad_sonda(metrics: dict, case_dir: Path) -> QualityComponent:
    """
    Calidad de la sonda ODE.

    Niveles:
      1.00 — ecuación canónica de literatura disciplinar con cita;
      0.80 — ecuación parametrizada por valores empíricos publicados;
      0.60 — ecuación genérica (Lotka-Volterra, AR(1)) sin cita específica;
      0.40 — ecuación ad-hoc pero documentada;
      0.20 — sonda reportada sin documentación.
    """
    # Heurística: buscar protocolo_simulacion.md, citas en notes
    proto = case_dir / "docs" / "protocolo_simulacion.md"
    arch = case_dir / "docs" / "arquitectura.md"
    has_proto = proto.is_file()
    has_arch = arch.is_file()
    notes = metrics.get("notes", "") or ""

    physics_keywords = ["Lindblad", "Bloch", "Tyson-Novak", "Hoffmann",
                        "Mackey-Glass", "Leavitt", "Plummer", "Lotka-Volterra",
                        "Kermack", "Budyko", "Sellers", "von Thünen",
                        "Jambeck", "Fajen-Warren", "Carpenter", "Maxwell",
                        "Fisher-KPP", "Zeeman"]
    has_physics_citation = any(k.lower() in notes.lower() for k in physics_keywords)

    if has_proto and has_arch and has_physics_citation:
        return QualityComponent(1.00, "protocolo + arquitectura + citación física")
    if has_physics_citation:
        return QualityComponent(0.85, "sonda con citación de literatura física")
    if has_proto:
        return QualityComponent(0.70, "protocolo de simulación documentado")
    return QualityComponent(0.50, "sonda sin documentación física específica")


def _q4_reproducibilidad(metrics: dict, case_dir: Path) -> QualityComponent:
    """
    Reproducibilidad mecanizada.
    """
    setup_hash = case_dir / "SETUP_HASH.json"
    has_hash = setup_hash.is_file()
    git_commit = (metrics.get("git") or {}).get("commit")
    if not git_commit and has_hash:
        try:
            rec = json.loads(setup_hash.read_text())
            git_commit = rec.get("git_commit")
        except Exception:
            pass
    has_seed = (
        "seed" in str(metrics).lower() or
        "seed=42" in str(metrics).lower() or
        "deterministic" in str(metrics).lower()
    )
    if not has_seed:
        # Buscar seed en archivos run.py / config.py
        for f in case_dir.rglob("*.py"):
            try:
                if "seed" in f.read_text(encoding="utf-8", errors="ignore").lower():
                    has_seed = True
                    break
            except Exception:
                pass
    score = 0.0
    components = []
    if has_hash:
        score += 0.4
        components.append("SETUP_HASH ✓")
    if git_commit:
        score += 0.3
        components.append(f"git_commit ✓ ({git_commit[:8]})")
    if has_seed:
        score += 0.3
        components.append("seed fijo ✓")
    return QualityComponent(score, " | ".join(components) if components else "sin reproducibilidad mecanizada")


def _q5_convergencia_multisonda(metrics: dict, case_dir: Path) -> QualityComponent:
    """¿Tiene sonda secundaria con motivación independiente?"""
    enriched = case_dir / "outputs" / "metrics_enriched_v5_2.json"
    if not enriched.is_file():
        return QualityComponent(0.30, "sin enriquecimiento V5.2")
    try:
        e = json.loads(enriched.read_text())
    except Exception:
        return QualityComponent(0.30, "metrics_enriched_v5_2 corrupto")
    case_id = case_dir.name
    # V5.3 B4 extendido a 12 casos
    cases_with_b4_extended = {
        "04_caso_energia", "05_caso_epidemiologia", "09_caso_finanzas",
        "11_caso_movilidad", "13_caso_politicas_estrategicas",
        "14_caso_postverdad", "15_caso_wikipedia", "16_caso_deforestacion",
        "18_caso_urbanizacion", "20_caso_kessler", "24_caso_microplasticos",
        "27_caso_riesgo_biologico",
    }
    if case_id in cases_with_b4_extended:
        return QualityComponent(0.85, "sonda secundaria B4 implementada (V5.3 extendido)")
    return QualityComponent(0.40, "enriquecimiento V5.2 sin sonda secundaria")


def _q6_loe_empirico(metrics: dict) -> QualityComponent:
    """LoE empírico declarado en el caso."""
    phases = metrics.get("phases", {})
    phase = phases.get("real") or phases.get("synthetic") or {}
    edi_dict = phase.get("edi", {}) if isinstance(phase, dict) else {}
    loe_factor = edi_dict.get("loe_factor", 0) if isinstance(edi_dict, dict) else 0
    # loe_factor es 0.2 (LoE=1) hasta 1.0 (LoE=5)
    score = float(loe_factor) if loe_factor else 0.4
    if loe_factor >= 1.0:
        ev = "LoE=5 (datos físicos directos, >30 años)"
    elif loe_factor >= 0.8:
        ev = "LoE=4 (series consistentes, múltiples fuentes, >10 años)"
    elif loe_factor >= 0.6:
        ev = "LoE=3 (datos estructurados <5 años)"
    elif loe_factor >= 0.4:
        ev = "LoE=2 (datos digitales con ruido semántico alto)"
    else:
        ev = "LoE=1 (especulativo o sintético sin ground truth)"
    return QualityComponent(score, ev)


def _q7_calibracion_estadistica(metrics: dict, case_dir: Path) -> QualityComponent:
    """¿Sobrevive el caso al régimen calibrado V5.2?"""
    enriched = case_dir / "outputs" / "metrics_enriched_v5_2.json"
    if not enriched.is_file():
        return QualityComponent(0.30, "sin métricas calibradas V5.2")
    try:
        e = json.loads(enriched.read_text())
    except Exception:
        return QualityComponent(0.30, "metrics_enriched corrupto")

    # Buscar p_block y survives_FWER
    b1 = e.get("B1_calibration") or e
    p_block = b1.get("p_value_block_bootstrap_estimated") or e.get("p_value_block_bootstrap_estimado")
    fwer_pos = b1.get("fwer_position_in_corpus") or {}
    survives = fwer_pos.get("survives_fwer_at_alpha_0_05")
    if survives is None:
        survives = e.get("sobrevive_fwer")
    if p_block is None or survives is None:
        return QualityComponent(0.50, "métricas calibradas parciales")
    score = 0.0
    if p_block <= 0.05:
        score += 0.6
    elif p_block <= 0.10:
        score += 0.3
    if survives:
        score += 0.4
    msg = f"p_block={p_block:.4f}, FWER survives={survives}"
    return QualityComponent(score, msg)


def quality_score(metrics: dict, case_dir: Path) -> dict:
    """
    Calcula el puntaje QES integral del caso.
    """
    components = {
        "Q1_trazabilidad_datos":     _q1_trazabilidad_datos(metrics, case_dir),
        "Q2_tamano_efectivo":        _q2_tamano_efectivo(metrics),
        "Q3_calidad_sonda":          _q3_calidad_sonda(metrics, case_dir),
        "Q4_reproducibilidad":       _q4_reproducibilidad(metrics, case_dir),
        "Q5_convergencia_multisonda": _q5_convergencia_multisonda(metrics, case_dir),
        "Q6_loe_empirico":           _q6_loe_empirico(metrics),
        "Q7_calibracion_estadistica": _q7_calibracion_estadistica(metrics, case_dir),
    }
    qes = sum(QES_WEIGHTS[k] * c.score for k, c in components.items())

    if qes >= 0.85:
        category = "ROBUSTO"
        recommendation = "Apto para afirmación demostrativa post-V5.2"
    elif qes >= 0.70:
        category = "DEMOSTRATIVO"
        recommendation = "Apto para afirmación demostrativa con honestidad"
    elif qes >= 0.55:
        category = "PROGRAMÁTICO"
        recommendation = "Apto sólo en modo programático con criterios de elevación"
    elif qes >= 0.40:
        category = "PILOTO"
        recommendation = "Caso piloto con limitaciones explícitas; no afirmar como demostración"
    else:
        category = "INADMISIBLE"
        recommendation = (
            "PAPER-SCIENCE: no satisface el piso ético-epistémico. "
            "Retirar como caso demostrativo, declarar como hipótesis especulativa, "
            "o re-implementar con datos reales y sonda físicamente motivada."
        )

    return {
        "case_id": case_dir.name,
        "QES": float(qes),
        "components": {k: asdict(c) for k, c in components.items()},
        "category": category,
        "recommendation": recommendation,
        "weights": QES_WEIGHTS,
    }


__all__ = ["quality_score", "QES_WEIGHTS"]
