# Corpus EDI inter-dominio: ejecución, resultados y alcance

## Función

Este capítulo documenta el motor híbrido ABM+ODE, los 30 casos inter-dominio y la infraestructura de ejecución y auditoría. El corpus evalúa si una sonda acoplada mejora la predicción frente a un modelo reducido. No convierte esa ganancia, por sí sola, en prueba de una entidad o invariante ontológico.

> **Nota de versionado.** `metrics.json` es la fuente de verdad de cada ejecución. El estatus inferencial final requiere además el régimen estricto B-T2.1. Los valores crudos, históricos y estrictos no deben mezclarse.

## Tesis del capítulo

El corpus prueba que el aparato es ejecutable, trazable y capaz de producir resultados positivos, nulos y negativos. Como B-T2.1 todavía no cubre los 30 casos, no existe una distribución confirmatoria homogénea del corpus ni un conjunto Strong robusto confirmado.

## 1. Estado estricto vigente

| Estatus B-T2.1 | N | Casos o alcance |
|---|---:|---|
| Strong robusto puro confirmado | 0 | Ninguno |
| Weak validado | 1 | Energía, caso 04: EDI 0.1571, p_block 0.006, CI [0.133, 0.193] |
| Candidato pendiente | 1 | Starlink, caso 26: EDI 0.7575, p_block 0.079, `overall_pass=false` |
| Falsificación local del aparato | 4 | Acidificación, Kessler, Erosión y Microplásticos, casos 19, 20, 23 y 24 |
| Controles negativos rechazados | 3 | Casos 06, 07 y 08 |
| Sin estatus estricto cerrado | 21 | Requieren reejecución B-T2.1 |

Una falsificación local indica que la sonda o el modelo propuestos predicen peor que el reducido en la ventana evaluada. No demuestra ausencia del fenómeno y tampoco salva automáticamente la ontología.

## 2. Reclasificaciones decisivas

| Caso | Resultado histórico | Resultado vigente | Lectura |
|---|---|---|---|
| 04 Energía | Strong, EDI 0.6503 | Weak validado, EDI 0.1571, p_block 0.006 | La corrección reduce la magnitud, conserva señal local |
| 20 Kessler | Strong, EDI 0.3527 | EDI -1.000, p_block 1.0 | Falsificación local |
| 24 Microplásticos | Strong, EDI ~0.8 | EDI -1.000, p_block 1.0 | Falsificación local tras datos refrescados |
| 26 Starlink | Strong sin gate | EDI 0.7575, p_block 0.079, gate fallido | Candidato, no confirmación |
| 30 Behavioral | Strong o Weak en narrativas previas | EDI 0.2622, `overall_pass=false`; block bootstrap p≈0.978 | Piloto con circularidad parcial |
| 16 Deforestación | Strong con gate, EDI 0.5802 | Weak, `overall_pass=false`, `trend_ok=false`, detrended -0.0438 | Fix M4/M5: magnitud raw era tendencia |
| 18 Urbanización | Strong con gate, EDI 0.3366 | Weak, `overall_pass=false`, `trend_ok=false`, detrended 0.0722 | Fix M4/M5: trend_r2=0.997 |
| 21 Salinización | Strong con gate, EDI 0.5152 | Weak, `overall_pass=false`, `trend_ok=false`, detrended 0.0007 | Fix M4/M5: detrended trivial |
| 22 Fósforo | Strong con gate, EDI 0.3221 | Weak, `overall_pass=false`, `trend_ok=false`, detrended -0.0449 | Fix M4/M5: magnitud raw era tendencia |

Las reclasificaciones muestran que el pipeline puede corregir sus resultados. Esta propiedad sustenta la auditabilidad del método; no constituye evidencia independiente de la ontología.

## 3. Controles y calibración

- Los casos 06, 07 y 08 fueron rechazados correctamente.
- El hostile testing con random walks reporta 0/2000 falsos positivos del gate, Wilson 95 % [0, 0.00191].
- La tasa empírica de tipo I del p-value nominal es aproximadamente 24 %, no 5 %.
- El AUC-ROC histórico 0.8857, CI bootstrap [0.6571, 1.0000], usa EDI como score y una etiqueta derivada del umbral de EDI. Mide consistencia interna, no validez externa.

Los controles reducen la objeción de validación indiscriminada frente a la familia ensayada. Faltan nulos más diversos y rivales estructurados con el mismo presupuesto de ajuste.

## 4. Estructura del corpus

```text
09-simulaciones-edi/
├── README.md
├── common/                              validador, ABM, ODE y backend
├── 01_caso_clima/ ... 30_caso_.../     corpus inter-dominio
│   ├── case_config.json
│   ├── src/
│   └── outputs/metrics.json
├── corpus_multiescala/                  casos 31 a 40
├── auc_roc/                             diagnóstico histórico del umbral
├── baselines/                           comparaciones rivales
└── scripts_orquestacion/                auditoría y reportes
```

## 5. Cómo ejecutar

### Verificación general

```bash
python3 harness/cli.py verify --all
```

### Entorno (una vez, desde la raíz del repo)

```bash
cd 09-simulaciones-edi
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt   # versiones pinnadas
```

### Ejecución desde la CLI

```bash
./tesis demo               # caso clima
./tesis audit              # auditoría rápida (sin re-ejecutar)
./tesis metrics            # regenera reportes
./tesis build              # re-ensambla TesisFinal/Tesis.md
```

### Caso específico

```bash
python3 09-simulaciones-edi/16_caso_deforestacion/src/validate.py
# Caso 04 (régimen estricto B-T2.1):
CASE_CONFIG_JSON=case_config_b_t2_1.json python3 09-simulaciones-edi/04_caso_energia/src/validate.py
```

Semillas fijas en código (sin flags). Guía completa de validación independiente: `VALIDACION.md`.

Cada caso debe declarar sus requisitos adicionales. Una reejecución confirmatoria debe fijar datos, sonda, baseline, ventana, umbrales y criterio de pérdida antes de observar el resultado.

## 6. Sondas de referencia

| Caso | Sonda | Referencia disciplinar |
|---|---|---|
| Clima | Budyko-Sellers | Budyko 1969; Sellers 1969 |
| Energía | Lotka-Volterra | Lotka 1925; Volterra 1926 |
| Deforestación | von Thünen | von Thünen 1826 |
| Epidemiología | SIR/SEIR | Kermack-McKendrick 1927 |
| Kessler | Densidad orbital | Kessler-Cour-Palais 1978 |
| Microplásticos | Acumulación-decaimiento | Jambeck et al. 2015 |
| Behavioral Dynamics | Atractor de heading | Fajen y Warren 2003; Warren 2006 |

La referencia disciplinar motiva una sonda; no prueba que su parametrización concreta sea adecuada para la ventana evaluada.

## 7. Límites

1. B-T2.1 no está cerrado para los 30 casos.
2. Las ventanas, pruebas y fuentes no son todavía homogéneas.
3. Algunos parámetros se estiman con los mismos datos que validan el modelo.
4. Las comparaciones contra rivales no tienen cobertura equivalente en todo el corpus.
5. La dependencia de una sonda por caso limita la inferencia ontológica.
6. No existe replicación externa ciega al EDI.

## 8. Relación con el manuscrito

- fundamento filosófico: capítulos 02;
- definición de κ y EDI: capítulo 03-04;
- mapa reconciliado del corpus: capítulo 05-07;
- corpus inter-escala: capítulo 05-06;
- conclusión y condiciones de elevación: capítulo 06-01.

## 9. Cierre

El corpus es evidencia del funcionamiento y de los límites del método. Su aporte más sólido consiste en hacer públicas las condiciones bajo las cuales una afirmación de cierre se admite, se degrada o se rechaza. La generalización ontológica queda abierta hasta completar el régimen estricto y obtener convergencia y replicación independientes.
