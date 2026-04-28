# Scripts de la Tesis

Herramientas para ejecutar, auditar y documentar las **29 simulaciones ABM+ODE** del proyecto de tesis doctoral *"Irrealismo Operativo de Hiperobjetos"*.

---

## ✅ Atajo recomendado (CLI tesis)

```bash
./tesis web --reload  # dashboard visual (home tesis + graficos)
./tesis demo      # caso Clima
./tesis audit     # auditoría rápida (sin re-ejecutar)
./tesis metrics   # regenera tablas
./tesis build     # ensambla TesisFinal/Tesis.md
./tesis run --case clima
```

La CLI `./tesis` decide CPU/GPU automáticamente (si hay nvidia-smi + contenedor).  
Para forzar: `./tesis run --cpu` o `./tesis run --gpu`.

---

## 🗂️ Estructura

```text
repos/scripts/
├── run/          # ejecucion CPU/GPU
├── audit/        # auditorias y reproducibilidad
├── build/        # tablas, reportes y generacion documental
├── templates/    # plantillas para scaffold de casos
├── tesis.py      # CLI Python principal
└── tesis_manifest.json
```

---

## 🚀 Ejecución de simulaciones

Existen **dos scripts ejecutores** mutuamente excluyentes. Ambos producen `metrics.json` y `report.md` en `{caso}/outputs/`.

| | `run/cpu_run.sh` | `run/gpu_run.sh` |
|---|---|---|
| **Dónde corre** | Localmente (Python nativo) | Dentro del contenedor Docker `tesis-gpu` |
| **Aceleración** | Solo CPU (NumPy) | GPU via CuPy (sub-batching automático) |
| **Requisitos** | Python 3.10+, dependencias instaladas | Docker + NVIDIA Container Toolkit |
| **Multi-GPU** | N/A | Sí — distribución proporcional por VRAM |
| **Velocidad (grid=50)** | ~15s/caso | ~6s/caso |
| **Velocidad (grid=2000)** | ~horas/caso | ~minutos/caso |

---

### `run/cpu_run.sh` — Ejecución local en CPU

No requiere Docker ni GPU. Workers paralelos auto-ajustados a los cores disponibles.

```bash
# ─── Básico ───────────────────────────────────────────────────
./run/cpu_run.sh                           # 29 casos, grid por caso, auto workers

# ─── Caso específico (match parcial, case-insensitive) ────────
./run/cpu_run.sh --case clima              # 01_caso_clima
./run/cpu_run.sh --case deforest           # 16_caso_deforestacion
./run/cpu_run.sh --case falsacion          # 06, 07, 08 (matchea los 3)

# ─── Tandas (dividir 29 casos en bloques) ────────────────────
./run/cpu_run.sh --parts 3                 # 3 tandas secuenciales
./run/cpu_run.sh --parts 5 --part 2        # solo la tanda 2 de 5

# ─── Control de paralelismo ──────────────────────────────────
./run/cpu_run.sh --workers 4               # máximo 4 procesos simultáneos

# ─── Escalado de grid (ponderado por tamaño base) ────────────
./run/cpu_run.sh --grid-mult 2

# ─── Secuencial (1 caso a la vez) ───────────────────────────
./run/cpu_run.sh --step-by-step

# ─── Previsualizar sin ejecutar ──────────────────────────────
./run/cpu_run.sh --dry-run
./run/cpu_run.sh --case falsacion --dry-run
```

**Flags completas:**

| Flag | Default | Descripción |
|------|---------|-------------|
| `--parts N` | 1 | Dividir casos en N tandas |
| `--part K` | todas | Ejecutar solo la tanda K de N |
| `--case NOMBRE` | — | Filtrar por nombre (match parcial, case-insensitive) |
| `--workers N` | auto | Workers paralelos (auto = `min(nproc, 16)`) |
| `--grid-mult X` | 1.0 | Multiplicador de grid (ponderado; no reduce) |
| `--step-by-step` | off | Secuencial: 1 caso a la vez, output live en terminal |
| `--perm N` | 9999 | Permutaciones para test EDI |
| `--boot N` | 5000 | Bootstrap samples para intervalos de confianza |
| `--refine N` | 50000 | Iteraciones de refinamiento en calibración |
| `--runs N` | 50 | Simulaciones por configuración (C5) |
| `--dry-run` | off | Solo muestra el plan, no ejecuta nada |

**Logs:** `/tmp/cpu_run_logs/{caso}.log`

**Nota grid-mult (ponderado):** grids <=10 no escalan; de 10→25 escalan linealmente hasta el factor completo. Si `use_topology=True`, el grid se limita a 50 para mantener topología.

---

### `run/gpu_run.sh` — Ejecución en GPU (Docker)

Ejecuta dentro del contenedor Docker `tesis-gpu`. Distribución multi-GPU dinámica con cola de trabajo `flock`. Sub-batching automático en VRAM.

```bash
# ─── Básico ───────────────────────────────────────────────────
./run/gpu_run.sh                           # 29 casos, grid por caso, ambas GPUs

# ─── Caso específico ─────────────────────────────────────────
./run/gpu_run.sh --case deforest           # 16_caso_deforestacion
./run/gpu_run.sh --case deforest

# ─── Escalado de grid (ponderado por tamaño base) ────────────
./run/gpu_run.sh --grid-mult 2

# ─── Forzar una GPU específica ───────────────────────────────
./run/gpu_run.sh --gpu 0                   # solo RTX 5070 Ti (16 GB)
./run/gpu_run.sh --gpu 1 --case clima      # solo RTX 2060 (6 GB)

# ─── Secuencial (1 caso/GPU a la vez) ─────────────────────────
./run/gpu_run.sh --step-by-step                        # 2 GPUs: 2 casos simultáneos (1/GPU)
./run/gpu_run.sh --step-by-step --gpu 0                # 1 GPU: puramente secuencial

# ─── Previsualizar sin ejecutar ──────────────────────────────
./run/gpu_run.sh --dry-run
./run/gpu_run.sh --parts 5 --dry-run
```

**Flags completas:**

| Flag | Default | Descripción |
|------|---------|-------------|
| `--parts N` | 1 | Dividir en N tandas (1–10) |
| `--part K` | todas | Ejecutar solo la tanda K de N |
| `--case NOMBRE` | — | Filtrar por nombre (match parcial, case-insensitive) |
| `--gpu N` | auto | Forzar GPU N (0 o 1). Auto = ambas GPUs |
| `--step-by-step` | off | Secuencial: 1 caso/GPU. Con 2 GPUs → 2 simultáneos |
| `--grid-mult X` | 1.0 | Multiplicador de grid (ponderado; no reduce) |
| `--perm N` | 9999 | Permutaciones para test EDI |
| `--boot N` | 5000 | Bootstrap samples para intervalos de confianza |
| `--refine N` | 50000 | Iteraciones de refinamiento en calibración |
| `--runs N` | 50 | Simulaciones por configuración (C5) |
| `--container C` | tesis-gpu | Nombre del contenedor Docker |
| `--dry-run` | off | Solo muestra el plan, no ejecuta nada |

**Logs:** `docker exec tesis-gpu ls /tmp/gpu_run_logs/`

**Nota grid-mult (ponderado):** grids <=10 no escalan; de 10→25 escalan linealmente hasta el factor completo. Si `use_topology=True`, el grid se limita a 50 para mantener topología.

---

### 🧠 ¿Cuándo usar cada modo?

| Situación | Comando recomendado |
|-----------|---------------------|
| Desarrollo rápido / debug de un caso | `run/cpu_run.sh --case NOMBRE` |
| Validación completa de los 29 casos | `run/gpu_run.sh` |
| Sensibilidad de grid en un caso | Editar `grid_size` en `validate.py` del caso |
| Escalar grids globalmente (ponderado) | `run/cpu_run.sh --grid-mult 2` o `run/gpu_run.sh --grid-mult 2` |
| Secuencial (1 caso por GPU) | `run/gpu_run.sh --step-by-step --case NOMBRE` |
| Sin GPU disponible | `run/cpu_run.sh` |
| Prueba rápida (params mínimos) | `--runs 5 --perm 99 --boot 100 --refine 100` |
| Verificar plan sin ejecutar | `--dry-run` (disponible en ambos) |

### ⚙️ Arquitectura interna

```
run/cpu_run.sh                      run/gpu_run.sh
    │                                   │
    ├── flock cola dinámica             ├── flock cola dinámica
    ├── N workers (1 por core)          ├── N workers (proporcional a VRAM/GPU)
    │                                   ├── CUDA_VISIBLE_DEVICES por worker
    ▼                                   ▼
  python3 validate.py               docker exec tesis-gpu python3 validate.py
    │                                   │
    ├── abm_core.py (NumPy)             ├── abm_core_gpu.py (CuPy)
    │                                   │   └── sub-batching: 25% VRAM libre
    ├── ode.py                          ├── ode.py
    ├── metrics.py → EDI, C1-C5         ├── metrics.py → EDI, C1-C5
    └── outputs/metrics.json            └── outputs/metrics.json
```

**Sub-batching GPU:** Cada proceso reserva el 25% de la VRAM libre para ejecutar B simulaciones simultáneas. B se ajusta automáticamente según grid y VRAM disponible. Si OOM con B=1, cae a CPU transparentemente.

**VRAM por proceso (estimada):**

| Grid | RTX 5070 Ti (16 GB) | RTX 2060 (6 GB) |
|------|---------------------|------------------|
| 50 | ~550 MB | ~550 MB |
| 200 | ~650 MB | ~650 MB |
| 500 | ~1450 MB | ~950 MB |
| 2000 | ~2330 MB | ~805 MB |

---

## 🔧 Scripts de utilidad

### Auditoría y validación

| Script | Qué hace | Uso |
|--------|----------|-----|
| `auditar_simulaciones.py` | Auditoría documental: estructura, métricas, coherencia (solo lectura) | `python3 audit/auditar_simulaciones.py` |
| `auditoria_cientifica_profunda.py` | Auditoría caso-por-caso: imports, ejecución, resultados | `python3 audit/auditoria_cientifica_profunda.py --no-exec` |
| `_audit_fresh.py` | Auditoría rápida de todos los `metrics.json` existentes | `python3 audit/_audit_fresh.py` |
| `verificar_consistencia.py` | Verifica sincronización entre `repos/Simulaciones/` y `TesisDesarrollo/` | `python3 audit/verificar_consistencia.py` |
| `replay_hash.py` | Genera o verifica hashes MD5 **normalizados** (ignora `generated_at`) de outputs para reproducibilidad | `python3 audit/replay_hash.py --verify` |
| `repos/Simulaciones/run_all_validations_parallel.py` | Ejecuta validate.py en paralelo con logs y timeout | `python3 repos/Simulaciones/run_all_validations_parallel.py --max-workers 8` |

Flags útiles de auditoría profunda:
```bash
python3 audit/auditoria_cientifica_profunda.py --no-exec
python3 audit/auditoria_cientifica_profunda.py --cases 01,16 --timeout 600
python3 audit/auditoria_cientifica_profunda.py --pattern "0[1-5]"
```

Replay hash (normalizado vs crudo):
```bash
python3 audit/replay_hash.py --verify         # normalizado (recomendado)
python3 audit/replay_hash.py --verify --raw   # crudo (incluye timestamps)
```

Auditoría ligera por subconjunto:
```bash
python3 audit/auditar_simulaciones.py --cases 01,16 --output /tmp/auditoria.md
```

### Generación de documentos

| Script | Qué hace | Uso |
|--------|----------|-----|
| `tesis.py` | CLI principal: scaffold, build, sync, audit, validate | `python3 tesis.py build` |
| `evaluar_simulaciones.py` | Resumen de métricas en tablas Markdown | `python3 build/evaluar_simulaciones.py --write` |
| `actualizar_tablas_002.py` | Actualiza tablas en `02_Modelado_Simulacion.md` desde `metrics.json` | `python3 build/actualizar_tablas_002.py --stdout` |
| `sync_outputs_to_tesis.py` | Sincroniza `outputs/` de `repos/Simulaciones/` hacia `TesisDesarrollo/` | `python3 build/sync_outputs_to_tesis.py --case clima` |
| `generar_docs_casos.py` | Genera los 5 docs/ estándar para casos 19-29 | `python3 build/generar_docs_casos.py --cases 19,24` |
| `regenerar_readmes.py` | Regenera `README.md` de cada caso desde `metrics.json` | `python3 build/regenerar_readmes.py --case falsacion` |

Flags útiles de generación:
```bash
# actualizar_tablas_002.py
python3 build/actualizar_tablas_002.py --dry-run
python3 build/actualizar_tablas_002.py --only-report
python3 build/actualizar_tablas_002.py --stdout

# generar_docs_casos.py
python3 build/generar_docs_casos.py --dry-run
python3 build/generar_docs_casos.py --cases 19,20,21

# regenerar_readmes.py
python3 build/regenerar_readmes.py --dry-run --case 06
```

Auditoría Python (`tesis.py`) con severidad configurable:
```bash
python3 tesis.py audit                  # warnings informativos, exit 0
python3 tesis.py audit --strict         # warnings/fallos -> exit 1
```

### Datos

| Archivo | Descripción |
|---------|-------------|
| `tesis_manifest.json` | Manifiesto de secciones de la tesis |
| `audit/replay_baseline.json` | Baseline de hashes MD5 para reproducibilidad |
| `templates/` | Plantillas para scaffolding de nuevos casos |

---

## ⚙️ Variables de entorno (recursos y cache)

| Variable | Efecto |
|---|---|
| `SIM_SHARED_CACHE` | Ruta base de cache compartida |
| `SIM_CACHE_DIR` | Alternativa a `SIM_SHARED_CACHE` |
| `SIM_OFFLINE=1` | Desactiva red (usa cache/fallback) |
| `SIM_REFRESH=1` | Ignora cache y refresca |
| `SIM_TIMEOUT=60` | Timeout default para fetchers |
| `SIM_AUTO_CACHE=1` | Auto-cachea cuando no se pasa `cache_path` |
