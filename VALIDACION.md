# VALIDACIÓN INDEPENDIENTE — guía para científicos y filósofos externos

Cómo verificar esta tesis por su cuenta desde un clon fresco, sin acceso a
nada fuera de este repositorio (+ internet para instalaciones y, en algunos
casos, descargas de datos públicos).

## 1. Lectura del manuscrito (filósofos, sin código)

1. `TesisFinal/Tesis.md` — manuscrito completo ensamblado.
   `TesisFinal/Tesis.pdf` — misma versión en PDF (si existe en su clon).
2. Orden de lectura recomendado: `README.md` § "Orden recomendado de lectura".
3. Mapa de interlocutores y referencias completas:
   `07-bibliografia/01-bibliografia-orientativa.md`.
4. Cada capítulo declara su **Deuda residual** fechada al final: léala antes de
   asumir que un punto está cerrado.

**Límite honesto:** los 103 PDFs de `07-bibliografia/` NO están en git
(685 MB, derechos de terceros). Las citas con paginación se verifican contra
ejemplares propios conseguidos por el lector. Los verificadores de citas del
harness requieren esos PDFs en local.

Versión web (lectura + exploración de casos, sin instalar nada):
`https://estructuras-preontologicas.vercel.app` (verifique frescura contra
git según §5: tras un push reciente la web puede servir código viejo).

## 2. Verificación computacional rápida (~15-30 min, 1 caso + harness)

```bash
git clone https://github.com/stevenvo780/EstructurasPreontologicas.git
cd EstructurasPreontologicas/09-simulaciones-edi
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt   # versiones pinnadas, verificadas 2026-09-28
```

Re-ejecutar un control de falsación (rápido, determinista, semilla 42):

```bash
cd 06_caso_falsacion_exogeneidad/src
python3 validate.py               # perfil canónico n_perm=999, n_boot=500
```

Resultado esperado (`outputs/metrics.json`, fase `real`): EDI ≈ 0.055,
p = 1.0, taxonomía `falsification` — el aparato DEBE fallar aquí.
Los inputs (`data/*.csv`) están versionados como fixtures exactos; no se
requiere red para este caso.

Integridad de outputs versionados (sin re-ejecutar nada):

```bash
cd ../..                 # de vuelta a 09-simulaciones-edi (venía de .../src)
./tesis hash              # 32 casos: hashes vs baseline, debe decir "Sin cambios: 32"
./tesis audit             # tabla corpus + overall_pass: 1/32 → ['42'] (42 legacy extra-corpus, ver §4); 2.º bloque: 29 CHECK + 3 NO-CHECK (30/41/42)
```

Harness formal (solo Python 3 stdlib, desde la raíz del repo):

```bash
python3 harness/cli.py verify --all   # 9/9 pass esperado
```

Qué cubre: paginación de citas, citas decorativas, prosa-contra-JSON,
replay-hash, índice de deuda, auto-indulgencia, consistencia doc↔config,
pre-registro, cumplimiento del harness.

## 3. Re-ejecución profunda (horas; CPU o GPU)

```bash
cd 09-simulaciones-edi
./tesis audit --deep --cases 01,16     # re-ejecuta validate.py (casos indicados)
./tesis metrics && ./tesis sync        # regenera reportes y sincroniza bloques AUTO
./tesis build                          # re-ensambla TesisFinal/Tesis.md
```

`audit --deep` sin `--cases` re-ejecuta los 30 casos canónicos (horas).
`./tesis run --gpu --case <nombre>` usa GPU si hay `nvidia-smi`.

## 4. Bloqueantes y límites conocidos (no los oculte al validar)

- **Caso 01 clima, bit-exacto bloqueado** (`B-T-NEW-CLIMA-DATA` en
  `TAREAS_PENDIENTES.md`): el `metrics.json` versionado (EDI = 0.2581) proviene
  de una variante sintética de julio cuya receta exacta se perdió; re-ejecutar
  con datos reales da EDI ≈ 0.003. **Mismo veredicto** (`overall_pass=False`,
  `trend`), distinta magnitud. La re-ejecución honesta conserva la conclusión.
- **Caso 04 energía exige régimen B-T2.1**: el `metrics.json` canónico
  (EDI = 0.1571, p_block = 0.006) se produce SOLO con
  `CASE_CONFIG_JSON=case_config_b_t2_1.json`; el config por defecto da otro
  experimento (EDI ≈ 0.46). El campo `config_file` en cada `metrics.json`
  declara el régimen usado. Misma trampa potencial en casos 20/24 si se
  re-ejecutan sin su config B-T2.1.
- **Umbral p doc↔código** (`B-T-NEW-P-THRESH`): glosario/tablas dicen p<0.01,
  el código usa p<0.05. No altera veredictos vigentes; pendiente decisión.
- **Reportes baselines/topology son histórico-sintéticos** (n=100, era
  pre-B-T2.1): llevan banner `provenance` explícito; no re-ejecutados sobre
  arrays reales (n real 6-13, insuficiente para ARIMA/VAR).
- **Casos 41/42** no tienen `validate.py` ni `case_config.json` (usan `run.py`
  por diseño); la auditoría los reporta como notas, no como OK/fallo.
- **Caso 42 `overall_pass=True` es legacy extra-corpus** (E4, ronda cierre
  2026-09-28): `metrics.json` del 2026-04-28 con schema antiguo (categoría
  `?`, sin `trend_bias`/`criteria_breakdown` ni `config_file`); el gate
  fresco post-Fix M4/M5 da **0 passes** en todo el corpus. No lo cite como
  positivo vigente.
- **`outputs/metrics_enriched_v5_2.json` es rancio pre-B-T2.1** (E9, ronda
  cierre 2026-09-28): ej. caso 04 dice EDI=0.6503 "ELEVADO A ROBUSTO" vs
  canónico 0.1571. Alimenta solo Q7 (calibración interna QES, no veredicto).
  Las Tablas 5.7.5/5.7.8 que lo citaban (filas 14/22) se corrigieron a
  `metrics.json` canónico el 2026-09-28. Valide contra `metrics.json`, nunca
  contra el enriquecido.
- **Runner `scripts/run_full_secondary_probes.py` es legacy provisional**
  (E5, ronda cierre 2026-09-28): semilla `abs(hash(case_id))`
  no-determinista entre procesos + reconstrucción circular desde EDI
  publicado sobre proxys sintéticos (F13). Sucesor:
  `scripts/run_secondary_probes_on_primary_arrays.py`. Ningún veredicto
  vigente depende de él.
- **Re-ejecuciones verificadas bit-idénticas 2026-09-28:** casos 06, 07, 08,
  12, 13, 25 (12/13 con ruido float 1e-15/1e-16, misma conclusión).
  Otros casos: fixtures presentes, re-ejecución completa pendiente de
  `audit --deep` a escala corpus.
- **p-value mal calibrado (declarado):** tasa empírica de tipo I ≈ 24%, no 5%.
  Los umbrales EDI sí son robustos. Ver `README.md` § "Limitaciones honestas".
- **Datos inter-escala sintéticos** derivados de parámetros publicados;
  elevación a datos reales es deuda post-defensa (6-12 meses).
- **Revisión por pares humanos hostiles:** deuda externa bloqueante para
  sustentación. Usted puede ser ese par: la ronda adversarial en curso se
  documenta en `Bitacora/`.

## 5. Estado git/Vercel (a la fecha de esta guía)

- Rama `main` en `origin` es la fuente de verdad; el deploy de producción de
  Vercel se reconstruye automáticamente con cada push a `main`.
- Si la fecha del último deploy (ver pie de la web o `vercel ls`) es anterior
  al último commit de `main`, la web sirve código viejo: valide contra git,
  no contra la web.
- La API web expone SOLO capítulos `.md` y ficheros de casos `.md/.json`
  (rutas constreñidas); `TAREAS_*`, `harness/`, `Bitacora/`, PDFs y `.git`
  no se sirven (ver `web_tesis/app.py::_serve_constrained`).

## 6. Qué significa "validada"

La tesis NO afirma certeza ni demostración cerrada (06-01 §3 lista qué no
queda demostrado): afirma un programa articulado con 40 instancias operativas
(0 strong / 0 `overall_pass` real tras Fix M4/M5; taxonomía cruda: 9 weak —1 validado B-T2.1—, 8 trend, 9 null, 3 falsificación, 1 suggestive),
controles de falsación rechazados, hostile testing 0/2000 falsos positivos
del gate, y deudas declaradas. Rondas adversariales 2026-09-28 ya ejecutaron
este protocolo: el criterio (a) SE DISPARÓ (gate C1 vacuo + tendencia ciega
→ Fix M4/M5, 7 flips strong→weak) y quedó cerrado con evidencia; (b)-(d)
resultaron absorbidos por la reescritura jul-2026 o convertidos en deuda
declarada (F2 κ: H-J-NEW-F2-KAPPA). Un validador externo refuta
suficientemente si demuestra, con evidencia `ruta:línea` o re-ejecución,
cualquiera de: (a') NUEVO error estadístico en el motor que invierta
veredictos vigentes; (b) circularidad dato-sonda no declarada; (c) ruptura
lógica en 06-01 §§2-5; (d) atribución falsa a un rival en 04.
Si encuentra una, abra issue con la evidencia: es el resultado más valioso
que puede producir esta guía.
