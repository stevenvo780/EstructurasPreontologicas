# Estructuras Pre-Ontológicas

## Irrealismo operativo y compresión multiescala con evaluación EDI

**Manuscrito doctoral en filosofía de la ciencia y ciencias de la complejidad**

**Autor principal, concepto y dirección filosófica:** Jacob Agudelo, Universidad de Antioquia

**Colaboración técnica e ingeniería computacional:** Steven Vallejo Ortiz

**Asistencia de IA:** declarada como instrumento de implementación bajo dirección humana
**Estado:** revisión predefensa, 2026-07-17

> **[BORRADOR-IA · requires: H-J2/H-J8]** La formulación filosófica de este resumen requiere firma autoral.

## Tesis en una frase

Algunas categorías pueden estudiarse como estabilizaciones relacionales antes que como sustancias dadas. El EDI evalúa, para un fenómeno, una sonda, un modelo, un baseline y una pregunta declarados, cuánto aporta el acoplamiento a la predicción. Los resultados actuales establecen la ejecutabilidad y auditabilidad del programa, pero no demuestran todavía una ontología general multiescalar.

## Qué propone el proyecto

El manuscrito distingue tres estratos que no deben confundirse:

1. **Programa ontológico:** el irrealismo operativo interpreta ciertos objetos como estabilizaciones de relaciones materiales dinámicas.
2. **Tesis epistemológica:** toda atribución de cierre está indexada al recorte fenómeno-sonda-modelo-pregunta.
3. **Resultado metodológico:** el protocolo C1-C5, el EDI, los controles y los pre-registros vuelven ejecutable y refutable esa atribución.

El resultado metodológico es reproducible. La tesis epistemológica recibe apoyo local. La generalidad ontológica permanece como hipótesis filosófica abierta.

## Estado empírico vigente

El corpus central contiene 40 casos: 30 inter-dominio y 10 inter-escala. La cobertura muestra dónde se ejecutó el aparato; no equivale al número de corroboraciones ontológicas.

### Corpus inter-dominio

| Estatus estricto B-T2.1 | N | Alcance |
|---|---:|---|
| Strong robusto puro confirmado | 0 | Ninguno |
| Weak validado | 1 | Energía, caso 04: EDI 0.1571, p_block 0.006 |
| Candidato pendiente | 1 | Starlink, caso 26: EDI 0.7575, p_block 0.079, `overall_pass=false` |
| Falsificación local del aparato | 4 | Casos 19, 20, 23 y 24 |
| Controles negativos rechazados | 3 | Casos 06, 07 y 08 |
| Sin estatus estricto cerrado | 21 | Requieren B-T2.1 caso por caso |

Las categorías históricas y el campo crudo `overall_pass` no se agregan como evidencia final porque el mismo régimen estadístico no se aplicó a los 30 casos.

### Corpus inter-escala

Los 10 casos trasladan la arquitectura de cómputo a escalas nominales desde 10⁻¹⁰ m hasta 10²⁰ m. Siete obtienen `overall_pass=true` bajo el régimen crudo, uno queda Weak y dos son null o failure mode. Como parte de los datos son sintéticos o parametrizados desde la literatura, este bloque prueba portabilidad computacional, no invariancia ontológica ni validación empírica a través de treinta órdenes de magnitud.

### Caso conductual

El caso 30 es piloto, no demostración. En la fase real obtiene EDI 0.2622 y `overall_pass=false`; el control posterior con block bootstrap estima p ≈ 0.978 y detecta circularidad parcial de la sonda.

## Qué sí queda establecido

- vocabulario material-relacional articulado mediante μ, G, H, κ y ε;
- protocolo C1-C5 y EDI por intervención ablativa;
- dossiers versionados, métricas legibles por máquina y comandos regeneradores;
- 0/2000 falsos positivos del gate bajo random walks, con Wilson 95 % [0, 0.00191];
- 3/3 controles negativos rechazados;
- capacidad documentada de degradar o rechazar clasificaciones previas;
- suite ST de control de coherencia formal.

Estos resultados prueban trazabilidad y selectividad frente a la familia de nulos ensayada. No sustituyen comparación contra rivales estructurados ni replicación independiente.

## Qué no se afirma

- que κ-pragmática implique κ-ontológica;
- que los cuatro invariantes existan en todos los casos;
- que una sola estructura ontológica se conserve en todas las escalas;
- que el EDI supere globalmente a ARIMA, VAR, GP o Neural ODE;
- que el AUC-ROC histórico de 0.886 mida validez externa;
- que el p-value nominal esté calibrado a 5 %;
- que exista validación externa por especialistas o pares humanos.

El AUC histórico usa el EDI como score y una etiqueta derivada del mismo umbral de EDI. Se conserva como diagnóstico de consistencia interna, no como evidencia discriminativa.

## Estructura del repositorio

```text
.
├── 00-proyecto/          arquitectura, preguntas, objetivos y resúmenes
├── 01-diagnostico/       falencias, objeciones y sesiones
├── 02-fundamentos/       ontología, epistemología, categorías y nivel B
├── 03-formalizacion/     aparato, criterios, auditoría y κ empírico
├── 04-debates/           posiciones rivales y limitaciones
├── 05-aplicaciones/      casos filosóficos y mapa del corpus
├── 06-cierre/            conclusión, defensa y hoja de ruta
├── 07-bibliografia/      corpus bibliográfico
├── 08-consistencia-st/   validación lógica interna
├── 09-simulaciones-edi/  código, datos y outputs EDI
├── Bitacora/             trazabilidad de revisiones
└── TesisFinal/           manuscrito ensamblado
```

## Lectura recomendada

1. `00-proyecto/02-preguntas-objetivos-hipotesis.md`
2. `00-proyecto/05-resumen-y-abstract.md`
3. `02-fundamentos/01-ontologia-material-relacional.md`
4. `02-fundamentos/04-anclaje-conductual-ecologico.md`
5. `03-formalizacion/01-aparato-formal.md`
6. `03-formalizacion/02-criterios-de-legitimidad-y-metodo.md`
7. `03-formalizacion/04-operacionalizacion-de-kappa.md`
8. `05-aplicaciones/07-mapa-aplicaciones-corpus.md`
9. `04-debates/01-debates-con-posiciones-rivales.md`
10. `06-cierre/01-conclusion-demostrativa.md`
11. `TAREAS_PENDIENTES.md`

## Reproducción

Verificación general:

```bash
python3 harness/cli.py verify --all
```

Reconstrucción del manuscrito:

```bash
python3 TesisFinal/build.py
```

Ejecución de un caso:

```bash
./tesis run --case <NN>
```

Cada caso declara su comando y conserva `outputs/metrics.json`. La cifra visible en el JSON debe distinguirse de su estatus inferencial bajo B-T2.1.

## Condiciones de elevación

Antes de defender la propuesta como ontología general deben cerrarse, como mínimo:

- B-T2.1 sobre los 30 casos con un único régimen estadístico;
- parámetros medidos fuera del ajuste;
- convergencia entre sondas estructuralmente distintas;
- comparación contra rivales con igual presupuesto de ajuste;
- datos reales abiertos para el corpus inter-escala;
- replicación independiente y evaluación externa ciega al EDI;
- decisión y firma autoral de H-J2/H-J8;
- requisitos institucionales de dirección, plantilla, originalidad y política de IA.

## Estado del manuscrito

El manuscrito es defendible como propuesta filosófica formalizada con contribución metodológica reproducible y evidencia parcial. No está cerrado como demostración de una ontología general multiescalar. El registro autoritativo de bloqueos y cierres está en `TAREAS_PENDIENTES.md`.

## Cómo citar, versión preliminar

> Agudelo, J., y Vallejo Ortiz, S. (2026). *Estructuras Pre-Ontológicas: Irrealismo operativo y compresión multiescala con evaluación EDI*. Manuscrito doctoral en preparación, Universidad de Antioquia.

## Licencia

Pendiente de definición según política institucional.
