# AU-7 — Caso 30 Behavioral: ¿sobrevive Holm-Bonferroni con m=30?

Fecha: 2026-05-04
Modo: auditoría (read-only sobre Tesis.md y metrics.json)
Disparador: hallazgo del adversarial-reviewer 2026-05-05 — "p=0.044 al borde; bajo Holm/Bonferroni con 30 casos cae".

## 1. Verificación de la afirmación textual

### Fuente: `09-simulaciones-edi/30_caso_behavioral_dynamics/outputs/metrics.json`
Fase **real** (la que cita la prosa):

| campo | valor |
|---|---|
| `edi.value` | 0.26216558939208157 |
| `edi.ci_lo` / `ci_hi` | 0.2494 / 0.2798 |
| `edi.permutation_pvalue` | **0.044044…** |
| `edi.permutation_significant` | true (single-test) |
| `edi.valid` | **false** |
| `criteria.edi_valid` | false |
| `criteria.emergence_pass` | false |
| `criteria.cr_valid` | false |
| `emergence_taxonomy.nivel` | 3 |
| `emergence_taxonomy.category` | "weak" |
| `emergence_taxonomy.interpretation` | "Cierre operativo débil (Nivel 3): señal macro significativa pero bajo umbral robusto" |

### Prosa auditada — `06-cierre/04-versiones-cortas-defensa.md`
- L25, L53: "8 weak (significativos): incluido caso 30 behavioral dynamics (0.26 v2 …)"
- L27: "El aparato rechazó caso 30 v1 (EDI=0.002) … La sonda mejorada v2 produjo Nivel 3 weak honesto."
- L118: "Resultado: EDI=0.262, **p=0.044 significativo**, CI [0.249, 0.280]. Nivel 3 (weak)."

**Coherencia parcial con JSON.** "Nivel 3 weak", `edi.valid=False` y CI son consistentes. La afirmación frágil es **"p=0.044 significativo"**: lo es bajo lectura single-test, pero la tesis afirma un **corpus de 30 casos** y reporta significancia en agregado, sin declarar corrección por múltiples comparaciones.

## 2. Holm-Bonferroni sobre los 30 casos del corpus inter-dominio

Recolección de `edi.permutation_pvalue` (fase real, fallback synthetic) en los 30 casos `01_..30_*` (excluye corpus inter-escala y casos 41/42):

| Rango i | caso | p | umbral Holm 0.05/(30−i+1) | decisión |
|---|---|---|---|---|
| 1–10 | 04, 05, 09, 14, 15, 16, 18, 20, 22, 24 | 0.0000 | 0.00167 … 0.00238 | **rechaza H₀** |
| 11 | 13 políticas | 0.00150 | 0.00250 | rechaza |
| 12 | 11 movilidad | 0.00200 | 0.00263 | rechaza |
| 13 | 27 riesgo biológico | 0.00220 | 0.00278 | rechaza |
| 14 | 21 salinización | 0.00280 | 0.00294 | rechaza |
| **15** | **30 behavioral** | **0.04404** | **0.05/16 = 0.00313** | **NO rechaza** |
| 16–30 | 12, 03, 10, 19, 02, 28, 01, 06, 07, 08, 17, 23, 25, 26, 29 | 0.477 … 1.0 | — | no rechaza |

**Resultado:** **14 casos sobreviven Holm-Bonferroni** con FWER α=0.05 sobre m=30. **Caso 30 es exactamente el corte donde la cadena Holm se rompe**: 0.044 > 0.05/16 = 0.00313, y por la regla de paro de Holm, todos los rangos ≥ 15 dejan de rechazarse.

Equivalente Bonferroni single-step (α/m = 0.05/30 = 0.00167): los 10 casos con p=0 lo cruzan; los demás (incluido caso 30) no. Holm es uniformemente menos conservador que Bonferroni y aun así caso 30 no sobrevive.

## 3. Estado argumental real

La frase "p=0.044 significativo" (L118) es **technically correct para test único, pero engañosa en el contexto del corpus de 30 casos** que la propia tesis usa como agregado. La salvaguarda interna del JSON (`edi.valid=False`, `cr_valid=False`, `emergence_pass=False`) ya degrada el caso a Nivel 3 / weak / "bajo umbral robusto" — eso **está bien declarado** en la prosa cuando dice "weak". El problema es local: la palabra "significativo" sin matiz de FWER en un capítulo defensivo.

## 4. Propuestas de edición concretas (DRAFT, requieren firma de Jacob)

### Opción A — declaración mínima honesta (recomendada por costo/beneficio)

Reescribir L118 (`06-cierre/04-versiones-cortas-defensa.md`):

> **Antes:** "Resultado: EDI=0.262, p=0.044 significativo, CI [0.249, 0.280]. Nivel 3 (weak)."
> **Después:** "Resultado: EDI=0.262, p=0.044 (significativo en test único; **no sobrevive Holm-Bonferroni con m=30, donde el umbral en su rango es 0.05/16 ≈ 0.0031**), CI [0.249, 0.280]. Por eso `edi.valid=False` en el JSON y la taxonomía lo clasifica Nivel 3 *weak*: 'señal macro significativa pero bajo umbral robusto'. La degradación está hecha; la palabra 'significativo' aquí se entiende solo como 'la permutación rechaza H₀ del caso aislado', no como afirmación de corpus."

Misma cláusula en L25, L27, L53 si se conserva la mención a "weak significativos": cambiar "8 weak (significativos)" por "8 weak (single-test); 4 sobreviven Holm-Bonferroni; caso 30 no" — y declarar cuáles son los 4 (13 políticas, 11 movilidad, 27 riesgo biológico, 21 salinización).

### Opción B — degradar caso 30 a "trend / sugerente" en la nomenclatura externa

Si Jacob prefiere coherencia entre clasificación pública y FWER, mover caso 30 a la cubeta "suggestive" o "trend" en las tablas de cierre. Costo: pierde la narrativa "el aparato disciplinó v1→v2" como ejemplo de Nivel 3 weak. Beneficio: cierra la objeción multitesting de raíz.

### Opción C — defender la lectura per-caso con argumento explícito

Sostener "significativo per-caso" agregando en el glosario (`00-proyecto/07-glosario-operativo.md`) y en `06-cierre/04-versiones-cortas-defensa.md` una nota: "Las p-values reportadas son per-caso, sin corrección por familia, porque cada caso constituye un test independiente con sonda específica; el agregado del corpus se valida por hostile testing (0/1500 falsos positivos), no por FWER paramétrico." Costo: defensible pero polémico — un revisor estadístico riguroso responderá que el hostile testing controla calibración del gate, no la inflación de tipo I del corpus reportado.

## 5. Costo argumentativo declarado

- **Opción A** mantiene la narrativa pero introduce friccción didáctica en una versión "30s/2min" que se vende como pulida. Costo bajo pero molesto.
- **Opción B** sacrifica el caso emblemático "v1 rechazado → v2 admitido weak" como ejemplo de disciplina; el ejemplo siguiría existiendo conceptualmente pero no podría llamarse "weak admitido".
- **Opción C** defiende la lectura actual pero abre frente con estadística clásica; viable solo si Jacob acepta que la respuesta a la objeción Holm es "no aplico Holm porque mi diseño no lo requiere", y eso debe estar argumentado, no asumido.

## 6. Bandera `edi.valid=False`

La objeción adversarial sugiere "documentar valid=False en glosario o eliminarla". El campo **ya está documentado de facto** por composición (`emergence_pass`, `cr_valid`, gate completo) en `09-simulaciones-edi/common/hybrid_validator.py`, pero **no aparece en `00-proyecto/07-glosario-operativo.md`**. Recomiendo entrada explícita:

> "**`edi.valid` (bool):** verdadero solo si EDI atraviesa el gate completo C1–C5 + emergence_pass + cr_valid + coupling_check + rmse_fraud_check. Una p-value baja con `edi.valid=False` indica señal estadística per-caso pero no cierre operativo robusto; clasificación correspondiente: Nivel 3 *weak* o inferior."

## 7. Acción

- **`needs_human` (H-J):** Jacob decide entre A/B/C. Sin esa firma, la asistencia no edita `06-cierre/04-versiones-cortas-defensa.md`.
- **`B-T` ejecutable sin firma:** añadir la entrada de `edi.valid` al glosario (Opción del §6). Pendiente de tarea explícita en `TAREAS_PENDIENTES.md`.

## 8. Reproducción

```bash
cd /datos/repos/EstructurasPreontologicas/09-simulaciones-edi
for d in [0-3][0-9]_caso_*/; do
  python3 -c "import json; d=json.load(open('$d/outputs/metrics.json')); ph=d['phases'].get('real') or d['phases']['synthetic']; print('$d', ph['edi']['permutation_pvalue'])"
done | sort -k2 -g
```

Verificación Holm en Python:

```python
import json, glob
ps = []
for f in sorted(glob.glob('[0-3][0-9]_caso_*/outputs/metrics.json')):
    d = json.load(open(f))
    ph = d['phases'].get('real') or d['phases']['synthetic']
    ps.append((f, ph['edi']['permutation_pvalue']))
ps.sort(key=lambda x: x[1])
m = len(ps)  # 30
for i, (name, p) in enumerate(ps, start=1):
    thr = 0.05 / (m - i + 1)
    print(f'{i:2d}  {name:55s}  p={p:.6f}  thr={thr:.6f}  {"REJECT" if p<=thr else "STOP"}')
    if p > thr: break
```

---

**Resultado de la auditoría:** la objeción adversarial es **válida en su núcleo** (p=0.044 no sobrevive Holm con m=30). La prosa de defensa contiene una palabra ("significativo") que no está mal en lo técnico per-caso pero es engañosa en el contexto del corpus. La salvaguarda en el JSON (`valid=False`, "weak", "bajo umbral robusto") ya hace la mitad del trabajo. Falta cerrar la mitad restante con edición explícita en L118 y entrada de glosario para `edi.valid`. Decisión filosófica entre A/B/C: **needs_human (H-J)**.
