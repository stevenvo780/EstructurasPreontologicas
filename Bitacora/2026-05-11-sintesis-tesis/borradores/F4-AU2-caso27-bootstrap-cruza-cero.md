---
borrador: IA
requires: H-J*
propuesta_fecha: 2026-05-11
destino: 06-cierre/01-conclusion-demostrativa.md:55 ; 05-aplicaciones/07-mapa-aplicaciones-corpus.md:28
hallazgo: Bitacora/2026-05-04-continuous-run/AU-2-caso27-bootstrap-cruza-cero.md
tipo: insercion_nota + reformulacion_tabla
---

## Diagnóstico

Caso 27 (Riesgo Biológico) figura en Tabla 6.1.1 ("Strong gate completo | 4 casos") y en 5.7.1/5.7.3 con la misma etiqueta, pese a que su CI bootstrap es `[-0.198, +0.648]` y por tanto **cruza el cero**. El gate `overall_pass=True` integra C1-C5 + permutación, pero **no exige `ci_lo > 0`**. La prosa actual induce al lector razonable a leer "strong" como CI completamente positivo, lo que el `metrics.json` no autoriza.

## Verificación contra fuente primaria

`09-simulaciones-edi/27_caso_riesgo_biologico/outputs/metrics.json` (phases.real, líneas 240–289):

```
overall_pass                = true
edi.value                   = 0.3325786
edi.bootstrap_mean          = 0.3096444
edi.ci_lo                   = -0.19753129
edi.ci_hi                   = +0.64843992
edi.permutation_pvalue      = 0.00220022
edi.permutation_significant = true
edi.valid                   = true
```

Comando regenerador: `python3 09-simulaciones-edi/27_caso_riesgo_biologico/src/validate.py` (perfil canónico).

## Texto propuesto (voz autoral filosófica de Jacob)

**Insertar como nota inmediatamente bajo la Tabla 6.1.1 en `06-cierre/01-conclusion-demostrativa.md:55`** y replicar bajo la Tabla 5.7.1 (`05-aplicaciones/07-mapa-aplicaciones-corpus.md:28`):

> **Costo declarado del agregador `overall_pass`.** El gate compuesto `overall_pass=True` integra el conjunto C1-C5 + viscosidad + significancia permutacional + persistencia, pero **no exige que `ci_lo` del bootstrap del EDI sea positivo**. Riesgo Biológico (caso 27) ilustra el costo: pasa el gate con `p_perm=0.0022` y `edi.value=0.333`, pero su CI bootstrap 95 % `[-0.198, +0.648]` cruza el cero. La promoción a "strong gate completo" descansa, por tanto, sobre la significancia permutacional del ranking del estadístico observado, no sobre la exclusión bootstrap del cero. La tesis sostiene esta categorización pero declara su límite: un revisor que lea "strong" como "CI bootstrap excluye el cero" estará leyendo más de lo que el agregador certifica. Si en una pasada posterior se exige `ci_lo > 0` como requisito de admisión, caso 27 se reclasifica a "strong sin gate bootstrap" y el conteo "4 strong" del corpus inter-dominio cae a 3 con pérdida del dominio biomédico-epidemiológico.

## Texto a reemplazar / modificar

- Añadir columna **CI 95 %** explícita en Tabla 6.1.1 y en Tablas 5.7.1/5.7.3 para cada caso strong; sin esa columna la nota anterior queda en el aire.
- `06-cierre/04-versiones-cortas-defensa.md:25,51,110`: la frase "4 casos strong" queda como está pero gana una llamada al pie con la nota anterior.

## Costo argumentativo declarado

Si Jacob acepta el límite del gate, la tesis preserva los cuatro casos strong al precio de declarar honestamente qué significa "strong" en el aparato; si Jacob prefiere endurecer el criterio (Salida (b) del informe AU-2), el conteo cae a 3 con pérdida narrativa del dominio biomédico. Mantener la formulación actual sin nota es la opción menos defendible: un revisor con `metrics.json` abierto detecta la asimetría entre gate y CI en menos de un minuto.
