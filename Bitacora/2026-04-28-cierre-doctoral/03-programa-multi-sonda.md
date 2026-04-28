# Programa multi-sonda para casos strong del corpus

## Función

Documento que especifica el plan de validación cruzada del corpus EDI bajo **sondas ODE alternativas** para neutralizar la objeción de **dependencia instrumental** señalada en el bloque 5 de la auditoría doctoral interna. Cada caso del corpus usa actualmente una sola sonda ODE; este programa diseña al menos una sonda alternativa para los tres casos strong principales y especifica criterios de convergencia.

## 1. Motivación

La objeción anticipable del comité es: *"si el aparato detecta cierre operativo bajo la sonda X, ¿lo detectaría bajo una sonda Y con motivación teórica distinta? Si convergen, fortalece la conclusión; si divergen, identifica qué aspecto del fenómeno captura cada sonda".*

La tesis ha defendido la dependencia instrumental como condición epistémica honesta del marco. Pero la defensa exige **prueba operativa**: al menos un caso (idealmente tres) re-ejecutado bajo sonda alternativa con reporte explícito de convergencia.

## 2. Casos seleccionados

Tres casos strong con `overall_pass = True`:

| # | Caso | Sonda primaria | Datos | EDI primario |
|---|------|----------------|-------|--------------|
| 04 | Energía eléctrica | Lotka-Volterra | OPSD | 0.6503 |
| 16 | Deforestación global | von Thünen frontier | World Bank | 0.6020 |
| 27 | Riesgo biológico | Mortalidad | World Bank | 0.3326 |

Estos tres casos cubren tres tipos de dinámica: producción-consumo (Energía), expansión espacial (Deforestación), riesgo-mortalidad (Riesgo Biológico). Su robustez bajo sondas alternativas es prueba diferenciada.

## 3. Sondas alternativas propuestas

### 3.1. Caso 04 (Energía eléctrica)

**Sonda primaria:** Lotka-Volterra (depredador-presa, oferta vs. demanda).

**Sonda alternativa:** **balance termodinámico de bajo orden** con tres compartimentos (generación, almacenamiento, consumo) y conservación de energía. Motivación teórica distinta: la dinámica de Energía es termodinámica antes que ecológica; un balance directo prueba si el cierre operativo persiste sin la metáfora ecológica.

**Hipótesis de convergencia:** EDI ≥ 0.50 con p < 0.001, `overall_pass = True`. Banda de tolerancia: ±0.10 respecto al primario.

**Esfuerzo:** 1 semana de implementación, 1 día de ejecución.

### 3.2. Caso 16 (Deforestación global)

**Sonda primaria:** von Thünen frontier (renta agrícola vs. distancia al mercado).

**Sonda alternativa:** **logística espacial saturada** (modelo de difusión espacial con límite de saturación territorial determinado por la frontera agrícola disponible). Motivación teórica distinta: la dinámica es de saturación de un recurso espacial, no de renta económica.

**Hipótesis de convergencia:** EDI ≥ 0.45 con p < 0.001. Banda de tolerancia: ±0.10.

**Esfuerzo:** 1 semana de implementación, 1 día de ejecución.

### 3.3. Caso 27 (Riesgo biológico)

**Sonda primaria:** mortalidad (modelo simple de tasa de mortalidad acoplada a presión biológica).

**Sonda alternativa:** **SIR demográfico extendido** con compartimento exposición-susceptible-recuperado y mortalidad acoplada al estado infeccioso. Motivación teórica distinta: dinámica epidemiológica clásica vs. mortalidad agregada directa.

**Hipótesis de convergencia:** EDI ≥ 0.25 con p < 0.05. Banda de tolerancia: ±0.10.

**Esfuerzo:** 2 semanas de implementación (más complejo), 1 día de ejecución.

## 4. Criterios de convergencia

Tabla de convergencia que se reportará en el manuscrito final:

| Caso | EDI primario | EDI alterno | Δ (alterno − primario) | Banda ±0.10 | `overall_pass` primario | `overall_pass` alterno | Veredicto |
|------|-------------:|------------:|-----------------------:|:-----------:|:------------------------:|:----------------------:|-----------|
| 04 Energía | 0.6503 | [pendiente] | [pendiente] | [pendiente] | True | [pendiente] | [pendiente] |
| 16 Deforestación | 0.6020 | [pendiente] | [pendiente] | [pendiente] | True | [pendiente] | [pendiente] |
| 27 Riesgo Bio | 0.3326 | [pendiente] | [pendiente] | [pendiente] | True | [pendiente] | [pendiente] |

**Veredicto cualitativo:**

- **Convergencia fuerte:** EDI alterno dentro de banda ±0.10 y `overall_pass` preservado. Conclusión: la dependencia instrumental no anula la conclusión.
- **Convergencia moderada:** EDI alterno dentro de banda ±0.20 pero `overall_pass` puede variar. Conclusión: el cierre operativo es robusto pero el grado depende de la sonda. Discutir.
- **Divergencia:** EDI alterno fuera de banda o cambia de signo. Conclusión: identificar qué aspecto del fenómeno captura cada sonda; documentar como hallazgo no anticipado.

## 5. Procedimiento de implementación

| Paso | Acción | Responsable |
|------|--------|-------------|
| 1 | Implementar sondas alternativas en `09-simulaciones-edi/common/ode_models.py` | autor técnico |
| 2 | Crear case_config alternativo por caso (sufijo `_alt`) | autor técnico |
| 3 | Re-ejecutar bajo perfil canónico (n_perm = 999, n_boot = 500) | autor técnico |
| 4 | Verificar con perfil agresivo (n_perm = 2999, n_boot = 1500) | autor técnico |
| 5 | Documentar resultado en `09-simulaciones-edi/<caso>/outputs/metrics_alt.json` | autor técnico |
| 6 | Actualizar README del caso con tabla comparativa primario vs. alterno | autor técnico |
| 7 | Producir resumen consolidado en este documento o en anexo | ambos autores |
| 8 | Reportar veredicto cualitativo en capítulo 09 y conclusión demostrativa | ambos autores |

## 6. Cronograma estimado

- **Semana 1:** sonda alterna Energía (balance termodinámico).
- **Semana 2:** sonda alterna Deforestación (logística espacial).
- **Semana 3–4:** sonda alterna Riesgo Bio (SIR demográfico).
- **Semana 5:** ejecución masiva, perfil agresivo, verificación.
- **Semana 6:** análisis, reporte, actualización del manuscrito.

Total: 6 semanas de dedicación parcial.

## 7. Extensión a casos weak (deuda futura)

Si el resultado en strong es convergente, conviene extender a los casos weak con `p < 0.001` (Postverdad, Urbanización, Fósforo, Wikipedia, Epidemiología). El esfuerzo es proporcional. Queda como deuda secundaria post-cierre del programa principal.

## 8. Limitación reconocida

- la elección de **una** sonda alternativa por caso, no múltiples, es compromiso entre rigor y factibilidad;
- las sondas alternativas se eligen con motivación teórica distinta pero ambas siguen siendo modelos de bajo orden; el aparato EDI no se compara contra modelos de alto orden ni redes neuronales (eso entraría en el programa de baselines estadísticos, documentado por separado en `04-programa-baselines-estadisticos.md`);
- la convergencia bajo dos sondas no garantiza convergencia bajo todas las sondas concebibles; pero es prueba positiva contra la objeción de dependencia instrumental fuerte.

## 9. Compromiso

Este programa se ejecuta como **deuda alta priorizada** durante el cierre doctoral. Su no-ejecución hasta el momento del depósito implica que la sección correspondiente del manuscrito final declara la limitación explícitamente con prioridad alta de trabajo posterior. Su ejecución parcial (uno o dos casos) se reporta con honestidad: parcial es parcial.

## 10. Lectura cruzada

- Auditoría que motivó este programa: `Bitacora/2026-04-27-integracion-jacob/04-auditoria-doctoral-v1.md` §5.
- Programa complementario de baselines estadísticos: `04-programa-baselines-estadisticos.md`.
- Hoja de ruta general: `06-cierre/03-hoja-de-ruta-para-tesis-final.md`.
- Casos del corpus: `09-simulaciones-edi/<caso>/README.md`.
