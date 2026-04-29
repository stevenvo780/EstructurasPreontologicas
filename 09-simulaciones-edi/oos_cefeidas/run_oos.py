"""
Predicción out-of-sample preregistrada — OGLE-IV LMC Cepheids fundamental mode.

Compromiso firme paso 6.ter hoja de ruta cap. 06-03.

Pre-registro: ./preregistro.json (SHA-256 fijo previo a la descarga).

Ejecuta:
  1. Descarga cepF.dat de OGLE-IV LMC.
  2. Filtra fundamentales con P>0 y mag finita.
  3. Ajusta los DOS modelos pre-registrados:
     - acoplado: V = a + b*log10(P) + c*(V-I)
     - no_ode:   V = a' + c'*(V-I)
  4. Calcula EDI = 1 - RMSE_coupled/RMSE_no_ode.
  5. p-value bajo permutación de log10(P) (n_perm=2999).
  6. Clasifica con umbrales pre-registrados.

Salida: outputs/oos_cefeidas_results.json + outputs/oos_cefeidas_report.md.
"""
from __future__ import annotations

import hashlib
import json
import sys
import time
import urllib.request
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
OUT = HERE / "outputs"
OUT.mkdir(parents=True, exist_ok=True)

PREREG = HERE / "preregistro.json"
PREREG_SHA = HERE / "preregistro.sha256"
DATA_RAW = HERE / "cepF.dat"

URL = "https://www.astrouw.edu.pl/ogle/ogle4/OCVS/lmc/cep/cepF.dat"


def verify_preregistro() -> str:
    """Verifica que el pre-registro no ha cambiado tras fijar el hash."""
    expected = PREREG_SHA.read_text().split()[0]
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if expected != actual:
        raise RuntimeError(f"Pre-registro alterado tras fijar hash. expected={expected} actual={actual}")
    print(f"[preregistro] hash verificado: {actual[:16]}...")
    return actual


def download_data() -> str:
    """Descarga cepF.dat si no existe en disco. Devuelve SHA-256 del archivo crudo."""
    if not DATA_RAW.exists():
        print(f"[download] fetching {URL}")
        req = urllib.request.Request(URL, headers={"User-Agent": "EDI-OOS/1.0"})
        with urllib.request.urlopen(req, timeout=120) as r:
            DATA_RAW.write_bytes(r.read())
    sha = hashlib.sha256(DATA_RAW.read_bytes()).hexdigest()
    print(f"[download] cepF.dat sha256={sha[:16]}... size={DATA_RAW.stat().st_size} bytes")
    return sha


def parse_cepF(path: Path) -> tuple[np.ndarray, np.ndarray, np.ndarray, list[str]]:
    """
    Formato OGLE-IV cepF.dat (orden de columnas):
      ID  I_mag  V_mag  Period_d  P_err  T0  I_amp  R21  phi21  R31  phi31

    Ajustes:
      - Algunos campos pueden ser '-' (faltantes). Filtrar.
    """
    ids, I_mags, V_mags, periods = [], [], [], []
    text = path.read_text()
    for line in text.splitlines():
        parts = line.split()
        if len(parts) < 4:
            continue
        try:
            star_id = parts[0]
            I_mag = float(parts[1])
            V_mag = float(parts[2])
            period = float(parts[3])
            if not (np.isfinite(I_mag) and np.isfinite(V_mag) and np.isfinite(period)):
                continue
            if period <= 0:
                continue
            # OGLE marca valores ausentes con '-' (saltado por float() que da error).
            # I y V deben ser razonables (10-22 para LMC Cepheids).
            if not (10 <= I_mag <= 22 and 10 <= V_mag <= 22):
                continue
            ids.append(star_id)
            I_mags.append(I_mag)
            V_mags.append(V_mag)
            periods.append(period)
        except ValueError:
            continue
    return (
        np.array(I_mags, dtype=np.float64),
        np.array(V_mags, dtype=np.float64),
        np.array(periods, dtype=np.float64),
        ids,
    )


def fit_ols(X: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, np.ndarray, float]:
    """OLS con intercepto. Devuelve (coeficientes, predicciones, RMSE)."""
    n = X.shape[0]
    X_aug = np.column_stack([np.ones(n), X])
    beta, *_ = np.linalg.lstsq(X_aug, y, rcond=None)
    y_pred = X_aug @ beta
    rmse = float(np.sqrt(np.mean((y - y_pred) ** 2)))
    return beta, y_pred, rmse


def main():
    print(f"[oos-cefeidas] start {time.strftime('%Y-%m-%d %H:%M:%S')}")
    prereg_hash = verify_preregistro()

    # 1. Descarga
    data_hash = download_data()

    # 2. Parse
    I_mag, V_mag, P_days, ids = parse_cepF(DATA_RAW)
    n = len(ids)
    print(f"[parse] N cefeidas fundamentales válidas: {n}")
    if n < 100:
        raise RuntimeError(f"Muy pocas cefeidas válidas: {n}")

    log_P = np.log10(P_days)
    V_minus_I = V_mag - I_mag

    # 3. Modelo acoplado: V = a + b*logP + c*(V-I)
    X_full = np.column_stack([log_P, V_minus_I])
    beta_full, V_pred_full, rmse_full = fit_ols(X_full, V_mag)

    # 4. Modelo no_ode: V = a' + c'*(V-I)
    X_color = V_minus_I.reshape(-1, 1)
    beta_color, V_pred_color, rmse_color = fit_ols(X_color, V_mag)

    # 5. EDI puntual
    edi = 1.0 - rmse_full / rmse_color
    print(f"[edi] rmse_acoplado={rmse_full:.4f}  rmse_no_ode={rmse_color:.4f}  EDI={edi:+.4f}")

    # 6. Permutación: barajar log_P y recalcular EDI bajo la nula H0:logP no informativo
    rng = np.random.RandomState(42)
    n_perm = 2999
    null_edis = np.empty(n_perm)
    t0 = time.time()
    for i in range(n_perm):
        log_P_perm = rng.permutation(log_P)
        X_perm = np.column_stack([log_P_perm, V_minus_I])
        _, _, rmse_perm = fit_ols(X_perm, V_mag)
        null_edis[i] = 1.0 - rmse_perm / rmse_color
    p_value = float((np.sum(null_edis >= edi) + 1) / (n_perm + 1))
    print(f"[perm] n_perm={n_perm} elapsed={time.time()-t0:.1f}s  p={p_value:.6f}  null_max={null_edis.max():+.4f}  null_95pct={np.percentile(null_edis, 95):+.4f}")

    # 7. Clasificación según umbrales pre-registrados
    if edi >= 0.40 and p_value <= 0.01:
        clasif = "strong"
    elif 0.20 <= edi < 0.40 and p_value <= 0.05:
        clasif = "weak"
    elif 0.10 <= edi < 0.20 and p_value <= 0.05:
        clasif = "suggestive"
    elif edi > 0 and 0.05 < p_value <= 0.10:
        clasif = "trend"
    else:
        clasif = "null"
    print(f"[clasif] {clasif.upper()} (umbrales pre-registrados)")

    # 8. Salida estructurada
    result = {
        "compromiso": "paso 6.ter hoja de ruta cap. 06-03 — predicción out-of-sample preregistrada",
        "preregistro_path": str(PREREG.relative_to(HERE.parent.parent)),
        "preregistro_sha256": prereg_hash,
        "dataset": {
            "fuente_url": URL,
            "archivo_local": str(DATA_RAW.relative_to(HERE.parent.parent)),
            "sha256_dato_crudo": data_hash,
            "n_filas_validas": n,
        },
        "modelo_acoplado": {
            "forma": "V = a + b*log10(P) + c*(V-I)",
            "coeficientes": {"a": float(beta_full[0]), "b_logP": float(beta_full[1]), "c_color": float(beta_full[2])},
            "rmse": rmse_full,
        },
        "modelo_no_ode": {
            "forma": "V = a' + c'*(V-I)",
            "coeficientes": {"a_prime": float(beta_color[0]), "c_prime": float(beta_color[1])},
            "rmse": rmse_color,
        },
        "edi": edi,
        "permutacion": {
            "n_perm": n_perm,
            "seed": 42,
            "metodo": "permutacion_logP",
            "p_value": p_value,
            "null_max": float(null_edis.max()),
            "null_p95": float(np.percentile(null_edis, 95)),
            "null_mean": float(null_edis.mean()),
        },
        "clasificacion_calibrada_preregistrada": clasif,
        "veredicto": (
            "Hipótesis pre-registrada CONFIRMADA: el período es ablativamente necesario "
            "para predecir luminosidad media de cefeidas fundamentales bajo el aparato."
        ) if clasif == "strong" else (
            f"Hipótesis pre-registrada NO confirmada en grado strong: clasificación = {clasif}. "
            f"Se reporta sin atenuación según compromiso."
        ),
        "ejecutado_en_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }

    out_json = OUT / "oos_cefeidas_results.json"
    out_json.write_text(json.dumps(result, indent=2))
    print(f"[saved] {out_json}")

    return result


if __name__ == "__main__":
    main()
