# Anexo A.2. Mapa de operadores formales

## Función

Mapa visual y operativo de los cinco operadores del aparato formal de la tesis con su flujo canónico de uso, criterios de admisión, criterios de fallo y procedimientos empíricos.

---

## Diagrama del aparato

```
                       ┌──────────────────────────────────┐
                       │  Q = (φ, τ, R)                   │
                       │  Pregunta paramétrica fechada    │
                       └─────────────────┬────────────────┘
                                         │
                                         ▼
                       ┌──────────────────────────────────┐
                       │  μ : R → X                       │
                       │  Operador de medición            │
                       │  X = variables observables       │
                       └─────────────────┬────────────────┘
                                         │
                                         ▼
                       ┌──────────────────────────────────┐
                       │  G = (V, E, W, T)                │
                       │  Grafo basal de dependencias     │
                       │  cada arista pasa do-test        │
                       └─────────────────┬────────────────┘
                                         │
                                         ▼
                       ┌──────────────────────────────────┐
                       │  H = (V, 𝓔)                      │
                       │  Hipergrafo (orden superior)     │
                       │  cuando dependencias no son binarias
                       └─────────────────┬────────────────┘
                                         │
                                         ▼
                       ┌──────────────────────────────────┐
                       │  κ : G → G*                      │
                       │  Compresión                      │
                       │  empírica vía EDI                │
                       └─────────────┬───────┬────────────┘
                                     │       │
                                     │       │ (si validación falla)
                                     │       ▼
                                     │   ┌─────────────────────┐
                                     │   │  ε : n → G_n        │
                                     │   │  Expansión inversa  │
                                     │   └─────────────────────┘
                                     │
                                     ▼
                       ┌──────────────────────────────────┐
                       │  Validación (4 pruebas + C1-C5)  │
                       │  + 8 criterios extra             │
                       │  = overall_pass                  │
                       └─────────────────┬────────────────┘
                                         │
                                         ▼
                       ┌──────────────────────────────────┐
                       │  Clasificación en paisaje        │
                       │  Nivel 0 a Nivel 4 (5 futuro)    │
                       └──────────────────────────────────┘
```

---

## Flujo canónico de uso

```python
# 1. Fijar Q
Q = (
    formulacion='¿exhibe el fenómeno X cierre operativo bajo sonda S?',
    tolerancia=0.05,            # error medio aceptable
    regimen='medición mensual'  # frecuencia de muestreo
)

# 2. Aplicar μ: extraer variables del dominio
X = mu(R, regimen=Q.regimen)
# X = lista de variables observables/inferidas con su unidad

# 3. Construir G: grafo basal con criterios de admisión
G = construir_grafo(X, criterios_admision={'do_test': True})
# Cada arista pasa do-test (manipular v_i debe cambiar v_j)

# 4. Detectar H si procede
H = detectar_hipergrafo(G) if hay_dependencias_no_binarias(G) else None

# 5. Ensayar κ: compresión empírica vía EDI
G_star = kappa(G, metodo='EDI', n_perm=999, n_boot=500)
# Calcula EDI = 1 - RMSE_coupled / RMSE_no_ode

# 6. Validar con 13 condiciones (C1-C5 + extras)
validacion = validar(G_star, Q,
                     pruebas=['reproduccion', 'generalizacion', 'topologia', 'intervencion'],
                     protocolo=['C1', 'C2', 'C3', 'C4', 'C5'])

# 7. Si falla: aplicar ε para reabrir y reintentar
if not validacion.overall_pass:
    G_n = epsilon(G_star, region_problematica=validacion.fallo_localizado)
    # Iterar o declarar limitaciones honestas

# 8. Clasificar en paisaje
nivel = clasificar(EDI=validacion.edi,
                   p=validacion.p_value,
                   overall=validacion.overall_pass)
```

---

## Operador μ — detalle

**Tabla A.2.1.**

| Campo | Especificación |
|-------|----------------|
| Firma | `μ : R → X` |
| Entrada | dominio efectivo de realidad |
| Salida | conjunto de variables operacionalizadas |
| Criterio de admisión | régimen R especificado, variables operacionalizables, repetibilidad documentada |
| Criterio de fallo | medidas no repetibles bajo el mismo régimen |
| Implementación EDI | función `data.py::fetch_<dominio>` por caso |

---

## Operador G — detalle

**Tabla A.2.2.**

| Campo | Especificación |
|-------|----------------|
| Firma | `G = (V, E, W, T)` |
| V (nodos) | variables observadas |
| E (aristas) | dependencias detectadas que pasan do-test |
| W (pesos) | covarianza condicional, sensibilidad a intervención |
| T (reglas) | leyes físicas + leyes de control empíricamente identificables |
| Criterio de admisión | aristas robustas a intervenciones específicas |
| Criterio de fallo | manipular v_i no cambia v_j según predicción → eliminar arista |
| Implementación EDI | implícita en `hybrid_validator.py::run_full_validation` |

---

## Operador H — detalle

**Tabla A.2.3.**

| Campo | Especificación |
|-------|----------------|
| Firma | `H = (V, 𝓔)` |
| 𝓔 | hiperaristas que conectan ≥3 nodos simultáneamente |
| Cuándo crear H | dependencias conjuntas no reducibles sin pérdida a pares |
| Criterio de admisión | separar la hiperarista en pares cambia las predicciones |
| Implementación EDI | `topology_generator.py` para topologías heterogéneas (scale-free, small-world) |

---

## Operador κ — detalle (operacionalizado vía EDI)

**Tabla A.2.4.**

| Campo | Especificación |
|-------|----------------|
| Firma | `κ : G → G*` |
| Definición empírica | `EDI = 1 - RMSE_coupled / RMSE_no_ode` |
| Significancia | prueba de permutación (n_perm=999) |
| CI | bootstrap (n_boot=500) |
| Refinamiento | n_refine=5000 sobre top_k=10 candidatos |
| Criterio de admisión | EDI > 0 + p < 0.05 + protocolo C1-C5 |
| Gate completo (overall_pass) | 13 condiciones simultáneas |
| Criterio de fallo | falla en cualquiera de las 4 pruebas (reproducción, generalización, topología, intervención) |
| Implementación | `common/hybrid_validator.py` (2252 líneas) |

### Las cuatro pruebas de validación

1. **Reproducción**: el sistema reducido reproduce trayectorias medias dentro de tolerancia τ. Métrica: varianza explicada en condiciones similares al entrenamiento.
2. **Generalización**: predice trayectorias en condiciones no usadas para ajuste.
3. **Topología**: el campo vectorial reducido tiene los mismos atractores, repulsores y bifurcaciones que los datos.
4. **Intervención**: predice correctamente qué pasa al intervenir una variable.

---

## Operador ε — detalle

**Tabla A.2.5.**

| Campo | Especificación |
|-------|----------------|
| Firma | `ε : n → G_n` |
| Cuándo aplicar | tres signos: compresión impide distinguir casos relevantes; estructura interna modifica predicciones; sistema cerca de bifurcación |
| Criterio de admisión | ganancia inferencial mayor que el costo introducido |
| Garantía | la existencia operativa de ε es condición de admisión de κ |
| Implementación EDI | reapertura de subestructuras vía `resource_manager.py` o re-calibración local |

---

## Pregunta Q — detalle

**Tabla A.2.6.**

| Campo | Especificación |
|-------|----------------|
| Estructura | `Q = (φ, τ, R)` |
| φ | formulación del problema explicativo o interventivo |
| τ | tolerancia: qué diferencia es aceptable |
| R | régimen de medición: instrumento, condiciones, frecuencia |
| Fechado | obligatorio. Cambiar Q después del fallo invalida el ciclo |
| Implementación EDI | `case_config.json` con dates, thresholds, execution params |

---

## Validación canónica vs perfiles agresivos

**Tabla A.2.7.**

| Parámetro | Canónico | Agresivo (HYPER_*) |
|-----------|---------:|-------------------:|
| n_perm (permutación) | 999 | 2999 |
| n_boot (bootstrap) | 500 | 1500 |
| n_refine (refinamiento) | 5000 | 10000 |
| n_runs (réplicas) | 15 | 30 |
| grid_size (ABM) | 40 | 60+ |

---

## Niveles del paisaje y umbrales

```
EDI = -1 ─┬───────────────────┬───────────────────┬────────── EDI = 1
          │                   │                   │
       Nivel 0           Nivel 1-2-3          Nivel 4
       (null)         (trend/sug/weak)        (strong)
                            │
       EDI ≤ 0      0 < EDI ≤ 0.30           0.30 < EDI ≤ 0.90
       
                                            (con overall_pass=True
                                             requiere 13 condiciones)
```

**Flag de tautología:** EDI > 0.90 es flag para revisión manual (puede indicar sobreajuste).

**Flag de epifenomenalismo:** macro_coupling < 0.10 es flag (la sonda no está realmente acoplada).

---

## Referencias cruzadas al manuscrito

- Definición conceptual de los operadores: capítulo 03-01
- Criterios de admisión y dossier: capítulo 03-02
- Auditoría como protocolo: capítulo 03-03
- Operacionalización de κ vía EDI: capítulo 03-04
- Implementación: `09-simulaciones-edi/common/`
- Aplicación a 30 casos: capítulo 09 + `09-simulaciones-edi/<caso>/`
