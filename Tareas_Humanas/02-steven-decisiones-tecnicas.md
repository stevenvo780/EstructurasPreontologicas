# 2. Steven — decisiones técnicas con criterio humano

Tareas que requieren criterio técnico, asignación de tiempo focal y decisión de prioridad. La asistencia computacional ya dejó los esqueletos; falta ejecución.

---

## 2.1 — F13. Re-ejecución del corpus con `array_dump=True`

**Estado:** F13 cerrado **parcialmente**. Las sondas inter-paradigma se aplicaron a los 7 casos con `primary_arrays.json` disponible, con resultado honesto (1/7 converge bajo |ΔEDI| ≤ 0.10). Cerrar F13 completamente requiere extender `primary_arrays.json` a los 33 casos restantes.

**Acción:** modificar `09-simulaciones-edi/edi_engine.py` (o el `data.py` de cada caso) para emitir arrays primarios durante la corrida del modelo. Re-ejecutar el corpus completo. Aplicar `scripts/run_secondary_probes_on_primary_arrays.py` sobre los 40 casos. Documentar el nuevo resultado de convergencia.

**Tiempo estimado:** 3 semanas.

**Decisión a tomar:** ejecutar antes de defensa, o aceptar honestamente como deuda explícita post-defensa.

---

## 2.2 — F16. Fetch real para corpus inter-dominio

**Estado:** esqueletos de fetchers ya provistos en `09-simulaciones-edi/multiscale_fetchers.py` (multiescala: PhysioNet, OGLE, BRENDA, Gaia DR3, IBM Quantum) y `enhanced_data_fetchers.py` (Google Trends, OpenAlex, CelesTrak para casos macro).

**Acción:** completar fetchers reales para los casos macro donde es viable:

- **World Bank** (deforestación, urbanización, fuga de cerebros, salinización, etc.).
- **OWID** (epidemiología, energía, postverdad).
- **AQICN** (contaminación, salud).
- **NOAA** (clima regional, océanos).
- **OPSD** (energía eléctrica europea).
- **Yahoo Finance** (finanzas globales).

Re-ejecutar esos casos con datos reales. Declarar honestamente cuáles permanecen sintéticos.

**Tiempo estimado:** 3-6 semanas.

---

## 2.3 — F17. Calibración externa de QES

**Estado:** propuesta operativa completa en `09-simulaciones-edi/common/qes_external_calibration.md`. Corpus candidato curado: 10 estudios Q1 con datos abiertos (LIGO GW150914, Higgs ATLAS+CMS, EHT M87*, Hodgkin-Huxley, Pfizer NEJM 2020, Card-Krueger 1994, Reinhart-Rogoff 2010, Henrich WEIRD, Bem 2011 como falsabilidad invertida).

**Acción:** ejecutar el procedimiento descrito. Métrica de aceptación: concordancia categorial ≥ 70% (tolerancia ±1 categoría) y caso Bem 2011 categorizado como INADMISIBLE.

**Tiempo estimado:** 3-5 sesiones de trabajo focal.

---

## 2.4 — Effective Information (EI): verificar que no importa IIT

**Acción:** revisar `09-simulaciones-edi/common/` para localizar el cómputo de `effective_information`. Verificar que su uso es **métrica auxiliar**, no central, y declarar explícitamente que no implica compromiso con IIT (Tononi) ni con la causal emergence de Hoel en su forma fuerte.

Si es central: declarar el compromiso filosófico explícitamente en cap 03-04 (consultar con Jacob).

**Tiempo:** 1 sesión.

---

## 2.5 — Disciplinar uso de "self-organization"

**Acción:** auditar las 21 menciones de "self-organization" en el manuscrito. Para cada una:

- Si está anclada en Maturana-Varela (autopoiesis) o Haken (synergetics) con cita: dejar.
- Si es invocación retórica vaga: sustituir por "estabilización dinámica" o "convergencia a atractor".

**Tiempo:** 1-2 sesiones.

---

## 2.6 — Suprimir sinónimos redundantes

**Acción:** A.1 ya define con precisión **estructura pre-ontológica** (definición filosófica) y **atractor empírico** (operacionalización). Decidir destino de los siguientes sinónimos coloquiales que reaparecen en el manuscrito:

- "patrón estabilizado"
- "regularidad operativa"
- "estructura operativa"
- "cuenca de atracción" (cuando se usa como sinónimo de atractor, no como concepto técnico distinto)

Opciones:

1. Declarar en A.1 que los cuatro son **usos coloquiales** de los dos canónicos.
2. Suprimirlos sistemáticamente.

**Tiempo:** 1 sesión.

---

## 2.7 — Coordinación con director y secretaría

**Acción:**

- Coordinar con director de tesis (una vez designado, F23) sobre cronograma de defensa.
- Coordinar con secretaría del Doctorado en Filosofía sobre plantilla institucional, formato de declaración de originalidad, política sobre IA.

**Tiempo:** 2-4 semanas (depende del calendario institucional).

---

## 2.8 — Contacto con revisores externos hostiles

**Acción:**

- Contactar 1-2 filósofos hostiles externos (humanista clásico, filósofo de la ciencia con formación analítica) para revisión crítica de los fundamentos (F1, F2, F3, F5, F6, F9, F10).
- Contactar 1-2 estadísticos / físicos de complejidad para revisión crítica del aparato cuantitativo.

**Tiempo:** 3-6 meses (depende del calendario del revisor).

---

## Lectura cruzada

- Estado técnico actualizado: `Bitacora/2026-04-28-cierre-tecnico/REPORTE_CIERRE_TECNICO.md`.
- Esqueletos de fetchers: `09-simulaciones-edi/multiscale_fetchers.py`, `09-simulaciones-edi/enhanced_data_fetchers.py`.
- Calibración externa QES: `09-simulaciones-edi/common/qes_external_calibration.md`.
- Reportes técnicos generados: `09-simulaciones-edi/baselines/`, `09-simulaciones-edi/topology/`, `09-simulaciones-edi/multi_sonda/secondary_on_primary_arrays.md`.
