"""
Fetchers para datos reales de los casos del corpus multiescala — F16.

Implementa esqueletos de descarga, cacheo y validación para los datasets
abiertos identificados en `Anexos/A12-corpus-multiescala-tablas.md` Tabla A.12.4:

  - PhysioNet (HRV cardíaco, caso 37)
  - OGLE Variable Star Catalog (cefeidas pulsantes, caso 39)
  - BRENDA enzyme kinetics (Michaelis-Menten, caso 34)
  - Gaia DR3 (cúmulos globulares, caso 40)
  - IBM Quantum Experience (decoherencia qubit, caso 31) — requiere API key

Política de honestidad: cada fetcher:
  1. Documenta la URL canónica del dataset.
  2. Documenta el formato esperado y el preprocesamiento.
  3. Si la descarga falla, lanza `DataFetchError` con instrucciones manuales.
  4. **No genera fallback sintético**: la circularidad de F16 vino de mezclar
     fallback sintético con label "real". Aquí o hay datos reales o hay error.

Cache: `09-simulaciones-edi/data_cache/multiescala/<caso>/`.

Para activar el reemplazo de los datos sintéticos del corpus, llamar
`fetch_<caso>(use_cache=True)` desde el `data.py` del caso correspondiente.
"""
from __future__ import annotations

import io
import json
import os
import urllib.request
from pathlib import Path

CACHE_ROOT = Path(__file__).resolve().parent / "data_cache" / "multiescala"
CACHE_ROOT.mkdir(parents=True, exist_ok=True)


class DataFetchError(RuntimeError):
    """Lanzada cuando un fetcher no puede obtener datos reales."""


def _cache_dir(case_id: str) -> Path:
    d = CACHE_ROOT / case_id
    d.mkdir(parents=True, exist_ok=True)
    return d


def _http_get(url: str, timeout: int = 60) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "EDI-multiscale-fetcher/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


# ============================================================================
# Caso 37 — HRV cardíaco (PhysioNet MIT-BIH Normal Sinus Rhythm Database)
# ============================================================================

PHYSIONET_HRV_URL = "https://physionet.org/files/nsrdb/1.0.0/RECORDS"
"""
PhysioNet MIT-BIH Normal Sinus Rhythm Database (nsrdb).
Acceso libre. Las anotaciones RR se descargan con el toolbox `wfdb`.

Para series RR: requiere instalar `wfdb` (pip install wfdb) y luego:

    import wfdb
    rec = wfdb.rdrecord("16265", pn_dir="nsrdb")
    rr = wfdb.rdann("16265", "atr", pn_dir="nsrdb")

Aquí proporcionamos solo la URL de records y un ejemplo precomputado vía
PhysioToolkit si está cacheado.
"""


def fetch_hrv_records_list(use_cache: bool = True) -> list[str]:
    cache = _cache_dir("37_hrv_cardiaco") / "records.txt"
    if use_cache and cache.exists():
        return cache.read_text().splitlines()
    try:
        data = _http_get(PHYSIONET_HRV_URL).decode()
        records = [l.strip() for l in data.splitlines() if l.strip()]
        cache.write_text("\n".join(records))
        return records
    except Exception as e:
        raise DataFetchError(
            f"PhysioNet HRV records fetch failed: {e}\n"
            f"Manual: visit {PHYSIONET_HRV_URL} and save record IDs to {cache}"
        )


def fetch_hrv_series(record_id: str = "16265", use_cache: bool = True) -> dict:
    """Descarga RR series para un registro NSRDB. Requiere `wfdb` instalado."""
    cache = _cache_dir("37_hrv_cardiaco") / f"{record_id}_rr.json"
    if use_cache and cache.exists():
        return json.loads(cache.read_text())
    try:
        import wfdb  # type: ignore
    except ImportError:
        raise DataFetchError(
            "wfdb library not installed. Run: pip install wfdb"
        )
    try:
        ann = wfdb.rdann(record_id, "atr", pn_dir="nsrdb")
        sample = ann.sample.tolist()
        rr_intervals = [(sample[i+1] - sample[i]) / 128.0 for i in range(len(sample)-1)]  # 128 Hz
        result = {
            "record_id": record_id,
            "source": "PhysioNet MIT-BIH NSRDB",
            "sampling_rate_hz": 128,
            "n_intervals": len(rr_intervals),
            "rr_intervals_seconds": rr_intervals,
        }
        cache.write_text(json.dumps(result))
        return result
    except Exception as e:
        raise DataFetchError(f"PhysioNet record {record_id} fetch failed: {e}")


# ============================================================================
# Caso 39 — Cefeidas pulsantes (OGLE-IV catálogo)
# ============================================================================

OGLE_CEPHEIDS_URL = "https://www.astrouw.edu.pl/ogle/ogle4/OCVS/lmc/cep/ident.dat"
"""
OGLE-IV LMC Cepheids identification table.
Formato: ID, RA, Dec, P [días], V, I, ...
Acceso libre.
"""


def fetch_ogle_cepheids_list(use_cache: bool = True, max_n: int = 100) -> list[dict]:
    cache = _cache_dir("39_cefeidas_ogle") / "ident.json"
    if use_cache and cache.exists():
        return json.loads(cache.read_text())[:max_n]
    try:
        raw = _http_get(OGLE_CEPHEIDS_URL).decode("utf-8", errors="ignore")
    except Exception as e:
        raise DataFetchError(
            f"OGLE Cepheids fetch failed: {e}\n"
            f"Manual: download {OGLE_CEPHEIDS_URL} and save to {cache.with_suffix('.dat')}"
        )
    rows = []
    for line in raw.splitlines():
        parts = line.split()
        if len(parts) < 4:
            continue
        try:
            rows.append({
                "id": parts[0],
                "type": parts[1],  # F = fundamental, 1O = first overtone, etc.
                "ra_sex": parts[2],
                "dec_sex": parts[3],
            })
        except (ValueError, IndexError):
            continue
    cache.write_text(json.dumps(rows))
    # Periods are in a separate file: ident.dat is identification only.
    # For periods + magnitudes, fetch:
    #   https://www.astrouw.edu.pl/ogle/ogle4/OCVS/lmc/cep/phot/I/{id}.dat
    return rows[:max_n]


# ============================================================================
# Caso 34 — Michaelis-Menten (BRENDA enzyme database)
# ============================================================================

BRENDA_API_HINT = "https://www.brenda-enzymes.org/soap_admin.php"
"""
BRENDA requires SOAP client + free academic registration.
Implementación esquemática: el cliente SOAP completo está fuera del alcance
de este script. Usuario debe:
  1. Registrarse en https://www.brenda-enzymes.org/register.php
  2. Usar `brendapyrser` (pip install brendapyrser) o cliente SOAP
  3. Query getKmValue para EC numbers de interés
"""


def fetch_brenda_km_values(ec_number: str = "1.1.1.1",
                           email: str | None = None,
                           password_md5: str | None = None,
                           use_cache: bool = True) -> dict:
    cache = _cache_dir("34_michaelis_menten") / f"km_{ec_number.replace('.', '_')}.json"
    if use_cache and cache.exists():
        return json.loads(cache.read_text())
    if not email or not password_md5:
        raise DataFetchError(
            "BRENDA requires authentication. Set email and md5(password) and retry.\n"
            f"See {BRENDA_API_HINT} for SOAP API documentation."
        )
    try:
        from zeep import Client  # type: ignore
    except ImportError:
        raise DataFetchError("zeep SOAP library not installed. Run: pip install zeep")
    try:
        wsdl = "https://www.brenda-enzymes.org/soap/brenda_zeep.wsdl"
        client = Client(wsdl)
        params = (email, password_md5, f"ecNumber*{ec_number}")
        result_str = client.service.getKmValue(*params)
        cache.write_text(json.dumps({"ec": ec_number, "result_raw": result_str}))
        return {"ec": ec_number, "result_raw": result_str}
    except Exception as e:
        raise DataFetchError(f"BRENDA SOAP failed for EC {ec_number}: {e}")


# ============================================================================
# Caso 40 — Cúmulos globulares (Gaia DR3 vía VizieR)
# ============================================================================

GAIA_DR3_VIZIER_URL = (
    "https://vizier.cds.unistra.fr/viz-bin/asu-tsv?-source=I/355/gaiadr3"
    "&-out=Source,RA_ICRS,DE_ICRS,Plx,pmRA,pmDE,Gmag&-out.max=1000&-c={ra},{dec}&-c.rs=10"
)
"""
Gaia DR3 vía VizieR. Acceso libre.
Centro de cúmulo y radio en arcmin. Devuelve TSV con cinemática.
"""


def fetch_gaia_cluster_members(ra_deg: float, dec_deg: float,
                                radius_arcmin: float = 10.0,
                                use_cache: bool = True) -> list[dict]:
    cache_key = f"gaia_{ra_deg:.4f}_{dec_deg:.4f}_{radius_arcmin:.1f}.json"
    cache = _cache_dir("40_cumulos_globulares") / cache_key
    if use_cache and cache.exists():
        return json.loads(cache.read_text())
    url = GAIA_DR3_VIZIER_URL.format(ra=ra_deg, dec=dec_deg)
    url = url.replace("&-c.rs=10", f"&-c.rs={radius_arcmin}")
    try:
        raw = _http_get(url, timeout=120).decode("utf-8", errors="ignore")
    except Exception as e:
        raise DataFetchError(
            f"Gaia DR3 VizieR fetch failed: {e}\n"
            f"Manual: open {url} in browser and save TSV to {cache.with_suffix('.tsv')}"
        )
    rows = []
    in_data = False
    for line in raw.splitlines():
        if line.startswith("---"):
            in_data = True
            continue
        if not in_data or not line.strip() or line.startswith("#"):
            continue
        parts = [p.strip() for p in line.split("\t") if p.strip()]
        if len(parts) >= 7:
            try:
                rows.append({
                    "source_id": parts[0],
                    "ra": float(parts[1]),
                    "dec": float(parts[2]),
                    "parallax_mas": float(parts[3]) if parts[3] != "" else None,
                    "pmra_mas_yr": float(parts[4]) if parts[4] != "" else None,
                    "pmdec_mas_yr": float(parts[5]) if parts[5] != "" else None,
                    "G_mag": float(parts[6]) if parts[6] != "" else None,
                })
            except (ValueError, IndexError):
                continue
    cache.write_text(json.dumps(rows))
    return rows


# ============================================================================
# Caso 31 — Decoherencia (IBM Quantum Experience, T1/T2)
# ============================================================================

IBMQ_HINT = (
    "IBM Quantum requires API token from https://quantum-computing.ibm.com/account.\n"
    "Install: pip install qiskit-ibm-runtime\n"
    "Calibration data: backend.properties().t1(qubit), .t2(qubit)"
)


def fetch_ibmq_calibration(backend_name: str = "ibm_brisbane",
                           api_token: str | None = None,
                           use_cache: bool = True) -> dict:
    cache = _cache_dir("31_decoherencia_cuantica") / f"{backend_name}_t1t2.json"
    if use_cache and cache.exists():
        return json.loads(cache.read_text())
    if not api_token:
        raise DataFetchError(IBMQ_HINT)
    try:
        from qiskit_ibm_runtime import QiskitRuntimeService  # type: ignore
    except ImportError:
        raise DataFetchError("qiskit-ibm-runtime not installed.\n" + IBMQ_HINT)
    try:
        service = QiskitRuntimeService(channel="ibm_quantum", token=api_token)
        backend = service.backend(backend_name)
        props = backend.properties()
        n_qubits = backend.configuration().num_qubits
        t1 = [props.t1(q) for q in range(n_qubits)]
        t2 = [props.t2(q) for q in range(n_qubits)]
        result = {
            "backend": backend_name,
            "n_qubits": n_qubits,
            "t1_seconds": t1,
            "t2_seconds": t2,
            "fetched_at": props.last_update_date.isoformat() if props.last_update_date else None,
        }
        cache.write_text(json.dumps(result))
        return result
    except Exception as e:
        raise DataFetchError(f"IBM Quantum fetch failed: {e}")


# ============================================================================
# Registry
# ============================================================================

FETCHERS = {
    "31_decoherencia_cuantica": fetch_ibmq_calibration,
    "34_michaelis_menten": fetch_brenda_km_values,
    "37_hrv_cardiaco": fetch_hrv_series,
    "39_cefeidas_ogle": fetch_ogle_cepheids_list,
    "40_cumulos_globulares": fetch_gaia_cluster_members,
}

__all__ = [
    "DataFetchError",
    "fetch_hrv_records_list",
    "fetch_hrv_series",
    "fetch_ogle_cepheids_list",
    "fetch_brenda_km_values",
    "fetch_gaia_cluster_members",
    "fetch_ibmq_calibration",
    "FETCHERS",
]
