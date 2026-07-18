# Limitaciones declaradas

> **BORRADOR-IA · requires: H-J2, H-J8.** Consolidación editorial basada en el estado reproducible del corpus. Sustituye inventarios históricos y reclasificaciones incompatibles por una sola matriz vigente.

## Función

Este capítulo reúne los límites que condicionan la interpretación de la tesis. No repite la defensa de cada decisión ni el historial de auditorías. Distingue cuatro clases de restricción: metodológica, empírica, filosófica y procedimental.

## 1. Estado empírico que debe gobernar la lectura

La clasificación estricta vigente es:

| Estado | Casos | Alcance |
|---|---:|---|
| Strong confirmado | 0 | Ningún caso autoriza cierre robusto fuerte |
| Weak validado | 1 | Caso 04 Energía: EDI 0.1571, p_block 0.006, IC [0.133, 0.193] |
| Candidato | 1 | Caso 26 Starlink: EDI 0.7575, p_block 0.079; no supera el gate completo |
| Falsificación local | 4 | Casos 19, 20, 23 y 24 |
| Control rechazado | 3 | Casos 06, 07 y 08 |
| Sin cierre estricto | 21 | Evidencia insuficiente bajo el régimen vigente |

Esta tabla reemplaza las distribuciones históricas basadas en etiquetas crudas, p-values i.i.d. o umbrales anteriores. Los resultados crudos se conservan para reproducibilidad, pero no son el veredicto filosófico.

## 2. Limitaciones metodológicas

| Código | Limitación | Consecuencia | Cierre requerido |
|---|---|---|---|
| M1 | El régimen B-T2.1 no está cerrado homogéneamente en todos los casos | No puede estimarse prevalencia final de cierre | Reejecución caso por caso con perfil estricto único |
| M2 | Parte del corpus histórico usa permutación i.i.d. sobre series autocorrelacionadas | Los p-values históricos pueden ser optimistas | Block permutation o block bootstrap como regla canónica |
| M3 | Los umbrales fueron elegidos dentro del desarrollo del aparato | Sensibilidad y sobreajuste siguen siendo posibles | Análisis de sensibilidad y validación ciega externa |
| M4 | AUC 0.886 compara etiquetas derivadas del propio EDI | Mide consistencia interna, no validez externa | Etiquetas independientes y evaluación intergrupo |
| M5 | Varios casos tienen potencia insuficiente | Un null puede indicar falta de resolución | Análisis de potencia previo y muestras mayores |
| M6 | El criterio C1 admite una rama absoluta sin exigir aporte ODE | Puede producir C1 positivo con EDI negativo | Separar el fallback diagnóstico del gate confirmatorio |
| M7 | La corrección de sesgo se calibra en train y puede degradarse en validación no estacionaria | Riesgo de generalización aparente | Prueba de estacionariedad del residuo en validación |
| M8 | El criterio de viscosidad del atractor es débil y no entra al gate | No sostiene inferencia confirmatoria | Redefinirlo respecto de la escala temporal o retirarlo |

Los módulos existentes de calibración, prerregistro, sondas independientes, sensibilidad y potencia son infraestructura. Su existencia no equivale a aplicación uniforme ni a validación externa.

## 3. Limitaciones empíricas

### 3.1. Corpus inter-dominio

El corpus demuestra que el procedimiento puede ejecutarse, registrar fallos y revisar clasificaciones. No demuestra que el cierre operativo sea frecuente ni que los dominios compartan una ontología. Con 0 casos Strong confirmados, cualquier generalización positiva debe permanecer condicionada.

### 3.2. Corpus inter-escala

Los diez casos inter-escala usan principalmente datos sintéticos derivados de parámetros publicados. Prueban portabilidad computacional, no invariancia ontológica. La elevación exige datos primarios reales, sondas específicas y replicación independiente.

### 3.3. Caso 30

El caso de behavioral dynamics bajo EDI es un piloto metodológico. Su posterior block bootstrap produce p aproximado de 0.978 y la sonda alternativa detecta circularidad. No valida el caso Warren ni demuestra cierre conductual. Su continuación requiere datos humanos reales y un protocolo experimental independiente.

### 3.4. Independencia

La mayor parte de las auditorías y ejecuciones se realizó dentro del mismo proyecto. No existe todavía replicación externa formal, estudio ciego ni publicación revisada por pares que confirme las inferencias centrales.

## 4. Limitaciones filosóficas

| Código | Límite | Posición defendible |
|---|---|---|
| F1 | κ-ontológica fuerte no demostrada | El corpus evalúa κ-pragmática local |
| F2 | El naturalismo no se deduce del aparato | Es un compromiso metodológico de partida |
| F3 | La portabilidad no implica ontología común | La generalidad multiescalar es una conjetura programática |
| F4 | La identidad como cuenca no resuelve identidad personal o haecceidad | Solo ofrece continuidad operativa bajo transformaciones |
| F5 | EDI no agota experiencia en primera persona | Consciencia permanece como aplicación parcial |
| F6 | Estabilidad institucional no equivale a legitimidad | La dimensión normativa requiere tratamiento propio |
| F7 | Una ablación simulada no equivale a intervención física | La fuerza ontológica depende del tipo de intervención |

Estas restricciones no son promesas aplazadas en todos los casos. Algunas delimitan el objeto de la tesis: no se ofrece una teoría completa de la consciencia, una solución al libre albedrío, un algoritmo moral ni una ontología total.

## 5. Limitaciones procedimentales

| Código | Pendiente | Efecto |
|---|---|---|
| P1 | Director de tesis sin declaración formal en el manuscrito | Bloquea cierre institucional |
| P2 | Plantilla y estilo bibliográfico institucional pendientes | Bloquea depósito final |
| P3 | Revisión externa humana pendiente | Bloquea la pretensión de validación independiente |
| P4 | Política institucional sobre asistencia con IA por confirmar | Requiere adecuar la declaración de herramientas |
| P5 | Decisiones autorales H-J2 y H-J8 abiertas | Impiden cerrar el estatuto ontológico y la voz final |

## 6. Prioridades de cierre

Las tareas que cambian el estatuto de la tesis son, en orden:

1. cerrar B-T2.1 con un perfil estadístico único y publicar la matriz completa;
2. obtener replicación independiente de al menos un caso Weak o candidato;
3. sustituir los casos inter-escala sintéticos por datos reales;
4. prerregistrar predicciones sobre dominios no usados para construir el aparato;
5. resolver las decisiones filosóficas e institucionales humanas.

Las mejoras de presentación, nuevas visualizaciones o módulos adicionales no sustituyen estos cierres.

## 7. Regla de interpretación

La tesis debe leerse con una regla única: una limitación del instrumento no se convierte en ausencia del fenómeno, y una señal producida por el instrumento no se convierte automáticamente en entidad. Entre ambos extremos, el resultado válido es el que conserva su régimen de medición, incertidumbre y alcance local.
