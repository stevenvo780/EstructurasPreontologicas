"""common_coupling.py — 09-simulaciones-edi/_coupling

Logica compartida para el eje N (No-localidad) del IHO: mide cuanto del poder
explicativo de una estructura B vive en su ACOPLAMIENTO con otra estructura A,
en vez de vivir en B aislada.

Esto NO reusa hybrid_validator.py/case_runner.py tal cual, porque esos modulos
estan diseniados para UN solo caso (una serie observada + su propio ODE/ABM
calibrado), no para dos estructuras cruzadas. En vez de forzar el aparato EDI
completo (permutacion + bootstrap + ABM) sobre un par inter-caso para el que
no fue disenado, se usa un PROXY honesto y documentado, explicitamente
etiquetado como tal:

  EDI_acoplamiento := reduccion relativa de RMSE fuera de muestra al predecir
  B(t) desde [B(t-1)] (baseline autorregresivo) vs desde [B(t-1), A(t-1)]
  (agregando el driver cruzado, con lag para evitar fuga de informacion
  contemporanea). Ambos modelos son regresion lineal simple (OLS), ajustados
  SOLO en el tramo de entrenamiento, evaluados en el tramo de prueba (split
  cronologico, sin mirar el futuro).

  edi_coupling = (rmse_baseline - rmse_coupled) / rmse_baseline

  Positivo => A ayuda a predecir B mas alla de la inercia de B misma
  (evidencia de acoplamiento inter-estructura, eje N). Cero o negativo =>
  el driver cruzado no aporta (o empeora) la prediccion fuera de muestra.
"""
import numpy as np
import pandas as pd


def _ols_fit_predict(X_train, y_train, X_test):
    """OLS simple con intercepto. X: (n, k) sin columna de unos (se agrega aca)."""
    Xtr = np.column_stack([np.ones(len(X_train)), X_train])
    Xte = np.column_stack([np.ones(len(X_test)), X_test])
    coef, *_ = np.linalg.lstsq(Xtr, y_train, rcond=None)
    return Xte @ coef


def rmse(a, b):
    return float(np.sqrt(np.mean((np.asarray(a) - np.asarray(b)) ** 2)))


def compute_coupling_edi(merged, target_col, driver_col, test_frac=0.3):
    """merged: DataFrame ordenado por year/date con columnas [target_col, driver_col].

    Retorna dict con rmse_without, rmse_with, edi_coupling, n_train, n_test.
    """
    df = merged.dropna(subset=[target_col, driver_col]).reset_index(drop=True)
    n = len(df)
    if n < 8:
        return {
            "error": f"muy pocos puntos superpuestos (n={n} < 8) para un split honesto",
            "n": n,
        }

    y = df[target_col].to_numpy(dtype=float)
    a = df[driver_col].to_numpy(dtype=float)

    # y(t-1) como predictor autorregresivo; A(t-1) como driver cruzado con lag.
    y_lag = y[:-1]
    a_lag = a[:-1]
    y_target = y[1:]

    n_eff = len(y_target)
    n_test = max(3, int(round(n_eff * test_frac)))
    n_train = n_eff - n_test
    if n_train < 4:
        return {"error": f"muy pocos puntos de entrenamiento (n_train={n_train})", "n": n}

    y_train, y_test = y_target[:n_train], y_target[n_train:]
    ylag_train, ylag_test = y_lag[:n_train], y_lag[n_train:]
    alag_train, alag_test = a_lag[:n_train], a_lag[n_train:]

    pred_baseline = _ols_fit_predict(ylag_train.reshape(-1, 1), y_train, ylag_test.reshape(-1, 1))
    rmse_baseline = rmse(y_test, pred_baseline)

    X_train_coupled = np.column_stack([ylag_train, alag_train])
    X_test_coupled = np.column_stack([ylag_test, alag_test])
    pred_coupled = _ols_fit_predict(X_train_coupled, y_train, X_test_coupled)
    rmse_coupled = rmse(y_test, pred_coupled)

    edi_coupling = (rmse_baseline - rmse_coupled) / rmse_baseline if rmse_baseline > 0 else None

    return {
        "n": n,
        "n_train": int(n_train),
        "n_test": int(n_test),
        "rmse_without_driver": rmse_baseline,
        "rmse_with_driver": rmse_coupled,
        "edi_coupling": edi_coupling,
        "method": "proxy_rmse_reduction_ar1_ols_lagged_driver",
    }


def load_annual_csv(csv_path, value_col="value", date_col="date", rename_to="value",
                     start_year=None, end_year=None):
    df = pd.read_csv(csv_path)
    df["date"] = pd.to_datetime(df[date_col])
    df["year"] = df["date"].dt.year
    df = df[["year", value_col]].rename(columns={value_col: rename_to})
    if start_year is not None:
        df = df[df["year"] >= start_year]
    if end_year is not None:
        df = df[df["year"] <= end_year]
    return df.sort_values("year").reset_index(drop=True)
