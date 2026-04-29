# Apéndice técnico 2. Tablas crudas del corpus EDI multiescala

## Función

Apéndice tabular de **resultados crudos verificables** del corpus EDI multiescala (10 casos en escalas distintas a la macro). La fuente de verdad numérica son los `outputs/metrics.json` versionados en `09-simulaciones-edi/corpus_multiescala/<caso>/`.

**Política:** todas las cifras son las publicadas en los `metrics.json`. Si hay discrepancia entre este apéndice y el `metrics.json` correspondiente, **prevalece el `metrics.json`**.

---

## Tabla A.12.1. Resultados del corpus multiescala (10 casos)

**Tabla A.12.1.**

| # | Caso | Escala (longitud) | Escala (tiempo) | EDI | p | CI 95% | Nivel | Overall pass |
|---|------|-------------------|-----------------|----:|--:|--------|------:|:------------:|
| 31 | Decoherencia qubit | 10⁻⁹ m | 10⁻⁶ s | 0.84 | 0.000 | estrecho | 4 | True |
| 32 | Espín-órbita | 10⁻¹⁰ m | 10⁻¹⁵ s | 0.83 | 0.000 | [0.80, 0.85] | 4 | True |
| 33 | Villin Headpiece | 10⁻⁹ m | 10⁻⁶ s | 0.00 | 0.826 | ~0 | 0 | False |
| 34 | Michaelis-Menten | 10⁻⁸ m | 10⁻³ s | 0.46 | 0.000 | [0.33, 0.57] | 4 | True |
| 35 | Ciclo celular | 10⁻⁵ m | 10³ s | 0.13 | 0.000 | [0.11, 0.15] | 3 | False |
| 36 | NF-κB | 10⁻⁵ m | 10² s | 0.59 | 0.000 | [0.58, 0.59] | 4 | True |
| 37 | HRV cardíaco | 1 m | 1 s | 0.58 | 0.000 | [0.51, 0.64] | 4 | True |
| 38 | Locomoción τ-dot | 1 m | 1 s | -1.34 | 1.000 | [-1.51, -1.21] | 0 | False |
| 39 | Cefeida pulsante | 10¹¹ m | 10⁵ s | 0.92 | 0.000 | [0.90, 0.93] | 4 | True |
| 40 | Cúmulo globular | 10¹⁷-10²⁰ m | 10¹⁴ s | 0.43 | 0.000 | [0.35, 0.51] | 4 | True |

## Tabla A.12.2. Distribución por nivel y por escala

**Tabla A.12.2.**

| Nivel | Cuenta | Escalas representadas |
|-------|-------:|----------------------|
| 4 strong (`overall_pass=True`) | 7 | atómica, cuántica, bioquímica, celular oscilatoria, individual, astrofísica chica, astrofísica grande |
| 3 weak | 1 | celular (ciclo) |
| 0 null | 2 | molecular (Villin), individual (Lee τ-dot) |

**Selectividad multiescala:** 8/10 con señal positiva (EDI > 0); 7/10 con `overall_pass=True`.

## Tabla A.12.3. Sondas físicas usadas por caso

**Tabla A.12.3.**

| # | Caso | Sonda macro | Referencia teórica |
|---|------|-------------|---------------------|
| 31 | Decoherencia qubit | Lindblad con T2(T_bath) | Lindblad 1976; Bloch 1946 |
| 32 | Espín-órbita | H_eff con (L·S) acoplado | Bloch theorem |
| 33 | Villin | MSM 2-estados Arrhenius | Lindorff-Larsen 2011 |
| 34 | MM | Lineweaver-Burk | Michaelis-Menten 1913 |
| 35 | Ciclo celular | Tyson-Novak 4 ODE | Tyson-Novak 2001 |
| 36 | NF-κB | Hoffmann reducido | Hoffmann 2002 |
| 37 | HRV | Mackey-Glass con delay | Mackey-Glass 1977 |
| 38 | Locomoción τ-dot | Lee 1976 control óptico | Lee 1976 |
| 39 | Cefeida | P-L Leavitt | Leavitt 1912 |
| 40 | Cúmulo globular | Plummer + marea | Plummer 1911 |

## Tabla A.12.4. Datos candidatos para elevación a LoE 4

**Tabla A.12.4.**

| # | Caso | Dataset abierto | Acceso | Cronograma |
|---|------|-----------------|--------|------------|
| 31 | Decoherencia | IBM Quantum Experience (T1, T2) | abierto | 2-3 meses |
| 32 | Espín-órbita | Bloch Lab MPI Munich | académico | 4-6 meses |
| 33 | Villin | DE Shaw Anton trayectorias | académico | 4-6 meses |
| 34 | MM | BRENDA enzyme database | abierto | 2-3 meses |
| 35 | Ciclo celular | Cross Lab Rockefeller | académico | 6-8 meses |
| 36 | NF-κB | Tay Lab ETH single-cell | académico | 4-6 meses |
| 37 | HRV | PhysioNet ECG | abierto | 1-2 meses |
| 38 | Locomoción | VENLab / WALK-MS | académico | 9-12 meses |
| 39 | Cefeida | OGLE survey | abierto | 1-2 meses |
| 40 | Cúmulo globular | Gaia DR3 | abierto | 2-3 meses |

## Trazabilidad

- fuente de verdad: `09-simulaciones-edi/corpus_multiescala/<caso>/outputs/metrics.json`
- código: `09-simulaciones-edi/corpus_multiescala/<caso>/run.py`
- motor común: `09-simulaciones-edi/corpus_multiescala/edi_engine.py`
- discusión: `05-aplicaciones/06-corpus-multiescala.md`
- corpus macro original: `10-apendices-tecnicos/01-tablas-crudas-corpus-interdominio.md`
