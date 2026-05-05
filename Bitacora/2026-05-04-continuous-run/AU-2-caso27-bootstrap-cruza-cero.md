# AU-2 — Caso 27 Riesgo Biológico: CI bootstrap cruza cero pero declarado Strong gate completo

**Fecha:** 2026-05-04
**Origen:** hallazgo de `@adversarial-reviewer` 2026-05-05.
**Tarea:** verificar la afirmación contra `metrics.json` y proponer edición o `needs_human`.
**Estado:** `needs_human` (decisión editorial-metodológica que toca conteo "4 casos strong" en 3 capítulos).

---

## 1. Verificación de la afirmación contra fuente de verdad

Fuente: `09-simulaciones-edi/27_caso_riesgo_biologico/outputs/metrics.json`, fase `real`
(líneas 240-289).

| Campo | Valor JSON |
|---|---|
| `overall_pass` | `true` |
| `edi.value` | 0.3325786 |
| `edi.bootstrap_mean` | 0.3096444 |
| `edi.ci_lo` | **-0.19753129** |
| `edi.ci_hi` | **+0.64843992** |
| `edi.permutation_pvalue` | 0.00220022 |
| `edi.permutation_significant` | `true` |
| `edi.valid` | `true` |

**Hecho numérico:** el CI bootstrap al 95% es **[-0.198, +0.648]** y **cruza cero**.
El test de permutación es significativo (p=0.0022) y el gate global devuelve
`overall_pass=true`. Es decir: el caso pasa el gate binario implementado en
`hybrid_validator.py`, pero **el bootstrap del propio EDI no excluye cero**.

La afirmación del adversarial-reviewer es **correcta y reproducible**.

## 2. Lugares donde la prosa repite la categoría "Strong gate completo" para caso 27

- `06-cierre/01-conclusion-demostrativa.md:55` — Tabla 6.1.1, fila
  "Strong (gate completo) | 4 | … Riesgo Biológico (0.333)".
- `06-cierre/04-versiones-cortas-defensa.md:25,51,110` — repite "4 casos strong"
  / "4 strong con gate completo" incluyendo Riesgo Biológico (0.33).
- `05-aplicaciones/07-mapa-aplicaciones-corpus.md:28` — Tabla A.5.1/5.7.1, fila
  "Strong (`overall_pass=True`) | 4 | … Riesgo Biológico"; y `:73` (Tabla
  A.5.3/5.7.3) lo lista en "Bloque I — Strong con gate completo".

## 3. Lectura honesta del gate vs. el CI

El criterio `overall_pass` agregado en el validador combina test de permutación,
viscosidad, sympl·okē, no-localidad, persistencia, etc. **No exige que `ci_lo>0`.**
La prosa en cambio promueve la lectura de "strong" como "robusta" en sentido
fuerte, lo cual el lector razonable interpretará como CI completamente positivo.

Hay tres salidas defendibles, con costos:

(a) **Mantener "4 strong" y declarar el costo en nota al pie.**
   Texto sugerido: "Riesgo Biológico pasa el gate compuesto (`overall_pass=True`,
   p_perm=0.0022) pero su CI bootstrap [-0.198, +0.648] cruza cero. La promoción
   a Nivel 4 strong descansa en la significancia permutacional, no en exclusión
   bootstrap del cero." Costo: el lector adversarial puede atacar la categoría.

(b) **Reclasificar Riesgo Biológico como Strong-sin-gate o Weak.**
   Implica: en `06-01:55` cambiar "Strong (gate completo) | 4" → "3";
   en `06-04:25,51,110` cambiar "4 casos strong" → "3"; en `05-07:28,73`
   reubicar el caso. Costo: pérdida narrativa del "4 casos en 4 dominios"
   (energía/deforestación/Kessler/biológico cubre física-energética,
   socioecológica, tecno-orbital, salud pública); con 3 strong queda
   física-energética + socioecológica + tecno-orbital, sin biomédico.

(c) **Re-ejecutar con bootstrap más agresivo y/o más datos.**
   Si `n_boot` actual produce CI tan ancho, podría no ser suficiente potencia.
   Verificar `case_config.json` y considerar `HYPER_N_BOOT=1500`. Si el CI sigue
   cruzando cero, (a) o (b) son inevitables. Costo: tiempo de cómputo + riesgo
   de confirmar lo mismo.

## 4. Acción operativa propuesta

No edito `Tesis.md` ni `metrics.json` (regla harness). No edito los capítulos
fuente porque la decisión entre (a)/(b)/(c) **es editorial-filosófica** y altera
el conteo central "4 casos strong" que aparece en defensa pública. Requiere
firma de Jacob.

**Marca:** `needs_human` (H-J*).

**Pasos previos al human-review (que la asistencia puede hacer si Jacob aprueba (c)):**

1. Re-ejecutar caso 27 con `HYPER_N_PERM=2999 HYPER_N_BOOT=1500
   python3 09-simulaciones-edi/27_caso_riesgo_biologico/src/validate.py`.
2. Inspeccionar nuevo `ci_lo`. Si `ci_lo>0`, ruta (a) sin nota al pie problemática.
   Si `ci_lo<0`, Jacob decide entre (a) con nota explícita o (b).

## 5. Costo argumentativo declarado

- Si Jacob acepta (b), el conteo "4 strong" cae a 3 en al menos 4 ubicaciones
  de prosa cerrada (06-01:55; 06-04:25, 51, 110; 05-07:28, 73). El argumento
  central "demostración multidominio en 4 dominios independientes" se debilita
  pero **gana defensibilidad** frente a crítica adversarial sobre robustez.
- Si Jacob acepta (a), el manuscrito asume públicamente que "strong" significa
  "pasa el gate compuesto, no necesariamente CI bootstrap > 0". Esto es
  honesto pero abre un flanco: un reviewer puede pedir reclasificación.
- (c) es la única ruta que podría preservar "4 strong" sin costo argumental;
  su éxito depende de que la cobertura del dato real soporte CI más estrecho.

## 6. Bibliografía/aparato

No requiere lectura de fuente primaria adicional para esta auditoría. La
inconsistencia es interna al pipeline EDI y a la prosa derivada.

---

**RESULT line abajo.**
