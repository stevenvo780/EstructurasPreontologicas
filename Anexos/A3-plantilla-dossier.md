# Anexo A.3. Plantilla del dossier de anclaje

## Función

Plantilla estandarizada del dossier de anclaje obligatorio para cualquier categoría candidata en modo demostrativo. Cualquier caso que entre en el manuscrito debe presentar este dossier completo. Para modo programático, los componentes 1-3 y 7-9 son obligatorios; los demás son conjeturas con criterio de elevación.

---

## Plantilla

```markdown
# Dossier de anclaje: [Nombre del caso]

**Categoría heredada (L1):** [término ordinario o disciplinar]
**Modo:** [demostrativo / programático]
**Fecha de fijación:** [YYYY-MM-DD]

---

## 1. Pregunta Q

- **Formulación φ:** [enunciado preciso del problema]
- **Tolerancia τ:** [criterio de error aceptable, e.g., r² ≤ 0.05]
- **Régimen R:** [instrumento, condiciones, frecuencia de muestreo]
- **Cambios posteriores prohibidos:** sí. Si Q cambia, se reinicia el ciclo de admisión con Q'.

## 2. Variables X

| Variable | Tipo | Régimen R | Operacionalización |
|----------|------|-----------|--------------------|
| ... | observable / inferida | mensual / anual / etc | método de medición |

## 3. Sustrato material instanciante

[Descripción explícita de los procesos, soportes, cuerpos, infraestructuras
que materialmente realizan el fenómeno.]

## 4. Grafo G = (V, E, W, T)

- **V (nodos):** [lista de variables]
- **E (aristas):** [dependencias detectadas que pasan do-test]
- **W (pesos):** [covarianzas, sensibilidades]
- **T (reglas):** [leyes físicas, leyes de control empíricas]

## 5. Hipergrafo H (si procede)

[Si las dependencias son binarias, escribir "no aplica". Si hay relaciones
de orden superior, listar hiperaristas y justificar no-reducibilidad.]

## 6. Compresión κ propuesta

- **Método:** EDI vía intervención ablativa
- **Sonda ODE:** [nombre del modelo, e.g., mean_reversion, behavioral_attractor]
- **Forma funcional:** [ecuación]
- **Parámetros calibrados:**
  - α = [valor]
  - β = [valor]
  - macro_coupling = [valor]
  - forcing_scale = [valor]
- **Dimensionalidad efectiva (d):** [número]

## 7. Atractores, repulsores, bifurcaciones identificados

- **Atractores empíricos:** [lista con valores y cuenca]
- **Repulsores empíricos:** [lista]
- **Bifurcaciones documentadas:** [lista con parámetros de control]

## 8. Pruebas de validación

| Prueba | Resultado | Tolerancia |
|--------|-----------|-----------:|
| Reproducción | varianza explicada = X% | τ específica |
| Generalización | desempeño fuera entrenamiento = X | τ |
| Topología | atractores preservados sí/no | — |
| Intervención | predicciones cumplidas X/N | — |

**Protocolo C1-C5:**

| Filtro | Estado | Detalle |
|--------|:------:|---------|
| C1 Convergencia | ✓/✗ | RMSE_coupled vs RMSE_no_ode |
| C2 Robustez | ✓/✗ | clasificación estable bajo ±20% perturbación |
| C3 Determinismo | ✓ | seed=42 |
| C4 Consistencia dominio | ✓/✗ | trayectorias respetan restricciones físicas |
| C5 Reporte de incertidumbre | ✓ | CI bootstrap, modos de fallo, LoE, val_steps |

**EDI cuantitativo:**

- EDI = [valor]
- Bootstrap CI = [lo, hi]
- p-value (permutación 999) = [valor]
- overall_pass = [True/False]
- Nivel = [0/1/2/3/4]

## 9. Predicción discriminante

[Predicción específica que un rival explícito no produce o produce peor.
Debe ser cuantitativa y verificable.]

**Rival explícito:** [posición y referencia]
**Predicción de la tesis:** [enunciado]
**Predicción del rival:** [enunciado]
**Datos empíricos disponibles:** [referencia]
**Verificación:** [a favor de la tesis / del rival / inconcluso]

## 10. Intervención discriminante

[Experimento o intervención cuyo resultado contrario falsaría la propuesta.
Debe ser ejecutable y registrable.]

## 11. Operador ε con protocolo de reapertura

[Plan de reapertura para regiones donde la compresión no funciona.
Identificar variables que se reabrirían y régimen de reapertura.]

## 12. Traducción B↔L3

| Parámetro de L3 | Variable de B | Unidad | Operacionalización |
|-----------------|---------------|--------|---------------------|
| ode_alpha | tasa de [...] | unidades físicas | medición directa |
| ode_beta | constante de [...] | unidades físicas | calibración empírica |
| ... | ... | ... | ... |

[Cada parámetro de L3 debe traducirse a B. Si alguno no se traduce, la
categoría está flotando y debe reformularse.]

## 13. Limitaciones declaradas

- **Régimen de no aplicabilidad:** [condiciones donde el modelo deja de aplicar]
- **Datos insuficientes:** [si val_steps < 10, marcar exploratorio]
- **Sonda única:** [si no hay multi-sonda, declararlo]
- **Otras limitaciones:** [...]

## 14. Comparación rival

| Criterio | Tesis (irrealismo operativo) | Rival 1 | Rival 2 | Rival 3 |
|---|---|---|---|---|
| A (anclaje) | sí | ... | ... | ... |
| B (multiescala) | sí | ... | ... | ... |
| C (admisión empírica) | EDI + C1-C5 | ... | ... | ... |
| D (traducibilidad B↔L3) | obligatoria | ... | ... | ... |
| E (caso ancla con datos) | sí | ... | ... | ... |
| F (alcance) | multidominio | ... | ... | ... |

[Discriminación pública: ventaja en al menos dos celdas. Si no, reformular.]

---

## Cierre del dossier

- **Conclusión sobre el caso:** [admitido como Nivel X / programático con criterio Y]
- **Trabajo futuro:** [extensiones planificadas]
- **Referencias cruzadas en el manuscrito:** [capítulos donde se discute]
```

---

## Casos completos disponibles en el repositorio

- **04 Energía:** dossier en `09-simulaciones-edi/04_caso_energia/` (overall_pass=True)
- **16 Deforestación:** dossier en `09-simulaciones-edi/16_caso_deforestacion/` (overall_pass=True, reproducido en sesión 2026-04-27)
- **20 Kessler:** dossier en `09-simulaciones-edi/20_caso_kessler/` (overall_pass=True)
- **27 Riesgo Biológico:** dossier en `09-simulaciones-edi/27_caso_riesgo_biologico/` (overall_pass=True)
- **30 Behavioral Dynamics:** dossier en `09-simulaciones-edi/30_caso_behavioral_dynamics/` (Nivel 3 weak, sesión 2026-04-27)

Cada uno tiene:
- `case_config.json` con parámetros y dates
- `src/{abm,ode,data,validate}.py` con implementación
- `outputs/metrics.json` con resultados
- `README.md` con análisis cualitativo

---

## Política de uso

1. **Modo demostrativo:** los catorce componentes son obligatorios.
2. **Modo programático:** componentes 1-3 (Q, X, sustrato) y 7-9 (atractores conjeturados, ¿pruebas?, predicción discriminante a buscar) son obligatorios. El resto son objetivos del programa de elevación.
3. **Auditoría:** un tercer investigador competente debe poder reproducir el dossier desde el case_config y los datos.

## Cierre

> El dossier no es burocracia: es la articulación operativa del filtro de admisión que distingue una tesis de un manifiesto. Cualquier categoría que entre al manuscrito sin dossier completo (en demostrativo) o sin criterio de elevación (en programático) está fuera del marco.
