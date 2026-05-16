---
paths:
  - "09-simulaciones-edi/**"
---

# Motor EDI

Estás trabajando en el motor empírico. Las cifras producidas aquí son la fuente de verdad numérica de la tesis.

## Definición

`EDI = 1 - RMSE_coupled / RMSE_no_ode`. Mide degradación predictiva al apagar el acoplamiento ODE→ABM. Significancia: permutación 999, CI bootstrap 500.

Glosario completo: `00-proyecto/07-glosario-operativo.md`.

## Reglas duras

1. **`outputs/metrics.json` es fuente de verdad — hook bloquea edición directa.** Se regenera ejecutando `validate.py`.
2. **Cada cifra reproducible:** "se ejecutó `python3 09-simulaciones-edi/16_caso_deforestacion/src/validate.py --seed 42` y produjo `edi=0.602`". Sin comando exacto = sin cifra reportable.
3. **Datos reales > sintéticos.** Hay GPU y datos públicos. Si optas por sintético, declara por qué (licencia, acceso, calendario) como deuda fechada.
4. **No maquillar resultados negativos.** Casos null son null. No inflar potencia con pseudo-replicación, no usar baselines de paja.

## Núcleo en `common/`

- `hybrid_validator.py` — validador canónico (Emergentómetro/protocolo C1-C5+).
- `case_runner.py` — orquestador por caso.
- `abm_core.py` / `abm_core_gpu.py` / `abm_numpy.py` — ABM en CPU/GPU/NumPy.
- `ode_models.py` — sondas macro (Lotka-Volterra, von Thünen, Budyko-Sellers, SIR/SEIR, etc.).
- `gpu_backend.py` — detección CUDA/CuPy/PyTorch, fallback CPU.
- `topology.py` / `topology_generator.py` — exponente Lyapunov, Grassberger-Procaccia, embedding Takens.
- `array_dump.py` — emite `primary_arrays.json` para sondas secundarias.
- `baselines.py` — ARIMA/VAR/RW/GP.

## Layout por caso

```
NN_caso_<nombre>/
  case_config.json         ← sonda, datos, splits, umbrales, topología
  src/{abm,ode,data,validate}.py
  data/
  outputs/metrics.json     ← fuente de verdad numérica
  outputs/report.md        ← derivado narrativo
```

## Comandos

```bash
cd 09-simulaciones-edi && source .venv/bin/activate   # entorno aislado propio

./tesis run --case clima                              # auto CPU/GPU
./tesis run --gpu --case deforest                     # forzar GPU
./tesis run --cpu --case 16                           # forzar CPU
./tesis audit --deep --cases 01,16                    # re-ejecuta validate.py
./tesis metrics                                       # regenera tablas y reportes
./tesis hash                                          # verifica hashes vs baseline

# Caso aislado
python3 09-simulaciones-edi/<NN>_caso_<nombre>/src/validate.py
HYPER_N_PERM=2999 HYPER_N_BOOT=1500 python3 .../validate.py    # perfil agresivo

# Re-ejecución masiva
python3 09-simulaciones-edi/run_all_validations_parallel.py
```

## Para re-ejecución delegar a sub-agente

Para B-T1 (array_dump), B-T5 (caso 19), B-E7 (caso 16) y similares: delega a `@execution-queue` (modelo haiku, ejecuta `Bash` directo con fallback CUDA→CPU y verificación de hashes).

Para resolver casos null con sondas alternativas: delega a `@multi-probe-runner` (modelo sonnet, motiva físicamente 3-5 sondas y reporta cuál rompe el null).
