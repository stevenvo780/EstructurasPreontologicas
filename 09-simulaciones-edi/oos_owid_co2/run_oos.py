"""Segundo OOS preregistrado — OWID CO2/GDP/energy per capita (Kaya identity reducida)."""
from __future__ import annotations
import csv, hashlib, json, time
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
OUT = HERE / "outputs"; OUT.mkdir(parents=True, exist_ok=True)
PREREG = HERE / "preregistro.json"; PREREG_SHA = HERE / "preregistro.sha256"
DATA = HERE / "owid_co2.csv"


def verify_preregistro() -> str:
    expected = PREREG_SHA.read_text().split()[0]
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if expected != actual:
        raise RuntimeError(f"Pre-registro alterado: {expected} != {actual}")
    print(f"[preregistro] hash verificado: {actual[:16]}...")
    return actual


def fit_ols(X, y):
    n = X.shape[0]
    X_aug = np.column_stack([np.ones(n), X])
    beta, *_ = np.linalg.lstsq(X_aug, y, rcond=None)
    y_pred = X_aug @ beta
    rmse = float(np.sqrt(np.mean((y - y_pred) ** 2)))
    return beta, y_pred, rmse


def main():
    print(f"[oos-owid-co2] start {time.strftime('%Y-%m-%d %H:%M:%S')}")
    prereg_hash = verify_preregistro()
    data_hash = hashlib.sha256(DATA.read_bytes()).hexdigest()
    print(f"[data] sha256={data_hash[:16]}... size={DATA.stat().st_size}")

    # Parse CSV; columns of interest:
    co2_pc = []; gdp_pc = []; ene_pc = []; rows_kept = 0
    with DATA.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                year = int(row["year"])
                if year < 1990: continue
                # exclude regional aggregates: filter by iso_code present and country != 'World' etc.
                iso = (row.get("iso_code") or "").strip()
                if not iso or len(iso) != 3 or iso == "OWID": continue
                co2pc = float(row["co2_per_capita"]) if row["co2_per_capita"] else None
                gdp = float(row["gdp"]) if row["gdp"] else None
                pop = float(row["population"]) if row["population"] else None
                ene_pc_v = float(row["energy_per_capita"]) if row.get("energy_per_capita") else None
                if co2pc is None or gdp is None or pop is None or ene_pc_v is None: continue
                if co2pc <= 0 or gdp <= 0 or pop <= 0 or ene_pc_v <= 0: continue
                gdp_pc_v = gdp / pop
                co2_pc.append(co2pc)
                gdp_pc.append(gdp_pc_v)
                ene_pc.append(ene_pc_v)
                rows_kept += 1
            except (KeyError, ValueError):
                continue

    co2 = np.log(np.array(co2_pc))
    gdp = np.log(np.array(gdp_pc))
    ene = np.log(np.array(ene_pc))
    n = len(co2)
    print(f"[parse] N filas país-año válidas: {n}")
    if n < 200:
        raise RuntimeError(f"Muy pocas filas: {n}")

    # Modelo acoplado: log(co2pc) = a + b*log(gdppc) + c*log(enepc)
    X_full = np.column_stack([gdp, ene])
    beta_full, _, rmse_full = fit_ols(X_full, co2)

    # Modelo no_ode: log(co2pc) = a' + c'*log(enepc)
    X_red = ene.reshape(-1, 1)
    beta_red, _, rmse_red = fit_ols(X_red, co2)

    edi = 1.0 - rmse_full / rmse_red
    print(f"[edi] rmse_acoplado={rmse_full:.4f}  rmse_no_ode={rmse_red:.4f}  EDI={edi:+.4f}")
    print(f"[fit] coefs full: a={beta_full[0]:.3f} b_logGDP={beta_full[1]:.3f} c_logE={beta_full[2]:.3f}")

    # Permutación de log(gdp_pc)
    rng = np.random.RandomState(42)
    n_perm = 2999; null_edis = np.empty(n_perm)
    t0 = time.time()
    for i in range(n_perm):
        gdp_perm = rng.permutation(gdp)
        X_p = np.column_stack([gdp_perm, ene])
        _, _, rmse_p = fit_ols(X_p, co2)
        null_edis[i] = 1.0 - rmse_p / rmse_red
    p_value = float((np.sum(null_edis >= edi) + 1) / (n_perm + 1))
    print(f"[perm] n_perm={n_perm} elapsed={time.time()-t0:.1f}s  p={p_value:.6f}  null_max={null_edis.max():+.4f}  null_p95={np.percentile(null_edis, 95):+.4f}")

    if edi >= 0.40 and p_value <= 0.01: cls = "strong"
    elif 0.20 <= edi < 0.40 and p_value <= 0.05: cls = "weak"
    elif 0.10 <= edi < 0.20 and p_value <= 0.05: cls = "suggestive"
    elif edi > 0 and p_value <= 0.10: cls = "trend"
    else: cls = "null"
    print(f"[clasif] {cls.upper()}")

    result = {
        "compromiso": "paso 6.ter (segundo test) hoja de ruta cap. 06-03",
        "preregistro_sha256": prereg_hash,
        "dataset": {"fuente": "OWID co2-data master", "sha256": data_hash, "n_filas_validas": n},
        "modelo_acoplado": {"rmse": rmse_full, "coefs": {"a": float(beta_full[0]), "b_log_gdp_pc": float(beta_full[1]), "c_log_energy_pc": float(beta_full[2])}},
        "modelo_no_ode": {"rmse": rmse_red, "coefs": {"a": float(beta_red[0]), "c_log_energy_pc": float(beta_red[1])}},
        "edi": edi,
        "permutacion": {"n_perm": n_perm, "seed": 42, "p_value": p_value, "null_max": float(null_edis.max()), "null_p95": float(np.percentile(null_edis, 95))},
        "clasificacion_calibrada_preregistrada": cls,
        "ejecutado_en_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    out_json = OUT / "oos_owid_co2_results.json"
    out_json.write_text(json.dumps(result, indent=2))
    print(f"[saved] {out_json}")
    return result


if __name__ == "__main__":
    main()
