# Sistemas técnicos distribuidos

## MODO PROGRAMÁTICO

Aplicación en **modo programático** según el capítulo 05-00. La presentación del fenómeno es robusta y el aparato se opera con claridad pedagógica, pero falta el modelo dinámico cuantitativo con datos públicos que eleve el caso a demostrativo.


## Conjetura del capítulo

> Los sistemas técnicos distribuidos son patrones materialmente sostenidos cuya disponibilidad, latencia y modos de fallo se modelan dinámicamente con acoplamientos múltiples. La conjetura es que el aparato del marco mejora el diagnóstico y la predicción de fallo respecto a vistas estáticas (arquitectura como diagrama) o reduccionistas (todo es hardware). La elevación a demostrativo requiere caso específico con datos de telemetría públicos y modelo dinámico cuantitativo.

## 1. La categoría `servicio`

### 1.1. Recorte heredado

En la práctica cotidiana se dice `el servicio está arriba`, `el servicio cayó`, `el servicio responde lento`.

### 1.2. Hipótesis de auditoría

`Servicio` es compresión operativa legítima cuando la pregunta es disponibilidad global, arquitectura, frontera funcional, responsabilidad organizativa. Es compresión que oculta cuando la pregunta es diagnóstico fino. La regla del capítulo 03-02 (compresión cuando el detalle no cambia inferencia, expansión cuando sí) opera con claridad.

### 1.3. Reconstrucción material

Un servicio depende de:

- procesos en máquinas;
- red entre máquinas;
- rutas y DNS;
- certificados TLS;
- balanceadores de carga;
- almacenamiento (bases de datos, colas);
- autenticación y autorización;
- configuración y despliegues;
- monitoreo y observabilidad;
- usuarios y patrones de tráfico;
- dependencias externas.

### 1.4. Variables candidatas (X)

- latencia (p50, p99) por endpoint;
- throughput;
- error rate por tipo;
- saturación de recursos (CPU, memoria, IO, red);
- profundidad de cola;
- validez de certificados;
- tiempo de resolución DNS;
- estado de despliegues recientes.

### 1.5. Atractores conjeturados

- estado estable de operación nominal con latencia y error rate dentro de SLO;
- estados degradados (latencia elevada pero servicio funcional);
- estado de fallo total (servicio caído).

### 1.6. Bifurcaciones

- transiciones entre estados (saturación cascada, fallo de dependencia, expiración de certificado);
- regímenes biestables donde pequeñas perturbaciones empujan al sistema entre operación y degradación.

### 1.7. Compresión y expansión en la práctica

- compresión legítima al describir arquitectura general: `el servicio sirve requests`;
- expansión necesaria al diagnosticar fallo: `¿falló DNS, TLS, persistencia, autenticación, dependencia externa, despliegue, configuración, capacidad?`;
- la práctica de incident response implementa esta dialéctica.

## 2. Hipergrafo de dependencias

Los sistemas distribuidos requieren H, no solo G binario. Razones:

- fallos cascada involucran múltiples servicios simultáneamente;
- restricciones de capacidad afectan conjuntos de operaciones;
- timeouts y retry policies acoplan dinámicas no binarias.

La modelización con hipergrafo permite representar grupos de servicios que comparten infraestructura, cuyas fallas se correlacionan no por dependencia directa sino por restricción global compartida.

## 3. Rival principal

Vistas estáticas de arquitectura (diagramas de servicios sin dinámica) y aproximaciones físicalistas absurdas (todo es electrones, transistores). Ninguna captura la dinámica acoplada que produce los fallos reales.

## 4. Criterio de elevación a demostrativo

Adoptar caso publicado o construible con datos:

- telemetría completa (logs, métricas, traces) de servicio distribuido durante un incidente;
- ajuste de modelo dinámico de bajo orden sobre indicadores clave;
- predicción de cascada con respecto a tiempo de respuesta;
- intervención discriminante: estrategia de circuit breaker con parámetros derivados del modelo dinámico contra estrategia ad hoc.

Candidatos: SRE journals con post-mortems publicados, datasets de Google Borg, traces de Microsoft Azure publicados con permisos.

## 5. Qué evita el marco en este dominio

**Tabla 5.3.1.**

| Tentación | Razón |
|---|---|
| Reificado técnico | No tratar `la plataforma`, `la app` o `el backend` como cosas simples |
| Reduccionismo físico absurdo | Nadie diagnostica caída de producción describiendo electrones |
| Diagramas estáticos sin dinámica | Las arquitecturas no operan en estado estático; viven dinámica |
| Modelado solo de happy path | Los fallos en sistemas distribuidos son cualitativos, no cuantitativos lineales |

## 6. Diálogo con interlocutores

### 6.1. Simondon — modo de existencia de los objetos técnicos

Simondon ofrece la categoría de individuación técnica y de objetos técnicos como concretizaciones de tendencias. La tesis lo opera: un servicio es individuación técnica cuya identidad depende de su funcionamiento sostenido en red.

### 6.2. Latour — actantes y redes

Latour insiste en redes con humanos y no-humanos. La tesis aplica: los componentes técnicos son actantes que entran en `V` si pasan filtro de admisión.

### 6.3. SRE / práctica de operaciones (Beyer y colegas)

Los principios de Site Reliability Engineering (definir SLO, error budgets, circuit breakers, blast radius limitation) son implementación informal de la auditoría ontológica del marco. La tesis los recoge como inspiración técnica.

## 7. Lo que este capítulo devuelve a la tesis general

Este caso es valioso pedagógicamente: muestra con claridad mínima de filosofía cómo opera la dialéctica compresión / expansión y por qué el modelo dinámico es preferible al diagrama estático. El servicio es real como patrón operativo, no como bloque autosuficiente; es nodo comprimido reabrible en hipergrafo de dependencias. La traducción al aparato es directa.

## 8. Limitación honesta

Este capítulo articula la conjetura con claridad, pero falta el modelo dinámico cuantitativo con datos públicos que eleve a demostrativo. La elevación es plausible y se prioriza en hoja de ruta.
