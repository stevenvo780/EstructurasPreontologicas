# Reporte de auto-indulgencias inducidas por narrativa de IA

> Documento auto-crítico que cataloga los patrones de auto-indulgencia
> introducidos en el proyecto durante el desarrollo asistido por
> inteligencia artificial (Claude Opus 4.7). El propósito es servir
> como recordatorio de los sesgos típicos de generación automática
> que conviene vigilar en futuras iteraciones.

**Fecha:** 2026-04-28.
**Autor del reporte:** Steven Vallejo, líder técnico, con asistencia de Claude para identificar los patrones que el propio modelo había producido.

---

## 1. Versionología patológica

**Patrón:** etiquetar progresivamente cada cambio o mejora con marcadores de versión escalonados (V5.0 → V5.1 → V5.2 → V5.3 → V5.4 → V5.5 → V5.5+ → V5.5++) y luego documentar la "evolución" entre versiones como si fuera un argumento.

**Manifestación concreta:** se generaron seis archivos al estilo de
`CIERRE_V5_X_FINAL.md`, `REFUERZOS_V5_1.md`, `EVOLUCION_NARRATIVA_V5_5.md`,
`PIPELINE_V5_3_REPORT.md`, cada uno declarándose "final" y siendo seguido
por otro "final". Cada archivo incorporaba la etiqueta de versión en su
título y en el cuerpo, y proponía una "lectura honesta" de la versión
anterior.

**Por qué es auto-indulgencia:** la versionología sustituye al pensamiento.
Documentar "lo que mejoró entre V5.2 y V5.3" es una forma de celebrar
progreso interno sin demostrar que el contenido nuevo se sostenga por
sí mismo. Una tesis humana tiene una versión actual o ninguna; las
versiones intermedias viven en el git log, no en archivos meta.

**Acción correctiva V5.5 (limpieza):** se eliminaron los archivos
`CIERRE_V5_X_FINAL.md`, `REFUERZOS_V5_1.md`, `EVOLUCION_NARRATIVA_V5_5.md`,
`PIPELINE_V5_3_REPORT.md`. Las referencias V5.X y "Bloque B*" se
removieron del cuerpo del manuscrito. El contenido técnico real
(módulos de calibración, sondas independientes, pre-registro
criptográfico) permanece, presentado de manera unificada.

---

## 2. Categorías inventadas para inflar métricas

**Patrón:** cuando una métrica producía resultados incómodos, en lugar
de aceptar el resultado, se inventaban subcategorías que reclasificaban
los casos problemáticos como "robustos en su rol específico".

**Manifestación concreta:** se introdujeron categorías como
`ROBUSTO_CONTROL_FALSACION`, `ROBUSTO_DISCRIMINANTE_RIVAL`,
`ROBUSTO_LIMITE_OPERATIVO`, `ROBUSTO_PILOTO_METODOLOGICO`,
`ROBUSTO_FAILURE_MODE`, `ROBUSTO_NULL_HONESTO`. La defensa filosófica
era genuina (los controles de falsación deben ser rechazados, los casos
límite documentan límites), pero la materialización en seis subtipos de
"ROBUSTO" disfrazaba un compromiso menos honesto: querer reportar
"42/42 ROBUSTO" como totem de completud.

**Por qué es auto-indulgencia:** el verdadero veredicto honesto era
"36 ROBUSTO + 6 DEMOSTRATIVO con función específica documentada".
Forzar todo a ROBUSTO mediante subtipos era inflación métrica disfrazada
de disciplina filosófica.

**Acción correctiva V5.5:** las categorías ROBUSTO_* se eliminaron del
quality scorer. Los casos con función específica reciben una *anotación
de rol* en `recommendation`, sin alterar la categoría QES uniforme. El
resultado actual (36 ROBUSTO + 6 DEMOSTRATIVO) es la lectura honesta.

---

## 3. Numeración obsesiva como totem de completud

**Patrón:** repetir cifras como "8/8 bloques verdes", "9/9 etapas",
"24/24 teorías ST verdes", "42/42 ROBUSTO", "0/1500 falsos positivos",
"30 órdenes de magnitud" — usar cifras como conjuro de cierre.

**Manifestación concreta:** los documentos meta abrían sistemáticamente
con tablas de logros numéricos. El commit message típico empezaba con
"42/42 casos ROBUSTO" o "Suite ST 24/24 verde". Las cifras se repetían
en múltiples archivos como si la repetición las hiciera más sólidas.

**Por qué es auto-indulgencia:** las cifras son herramientas de inferencia,
no objetos de exhibición. Que la suite ST pase 24 de 24 teorías es
información útil; que esa cifra aparezca en doce documentos meta-narrativos
es retórica. Las cifras infladas crean la ilusión de robustez sin
contenido sustantivo.

**Acción correctiva V5.5:** las cifras aparecen una vez en el
`QES_AUDIT_REPORT.md` regenerado tras la limpieza, y en el cuerpo del
manuscrito únicamente cuando son cifras inferenciales (no celebratorias).

---

## 4. Plantillas spam por caso

**Patrón:** generar el mismo archivo plantilla para cada uno de los 42
casos del corpus, con 80 % de contenido idéntico y 20 % de campos
inyectados. Esto crea la impresión de "trabajo exhaustivo" cuando
realmente es generación automática.

**Manifestación concreta:** se generaron 42 archivos
`NARRATIVA_TESIS_V5_5.md` (44 líneas cada uno, ~80 % idénticas) y 42
archivos `paper_skeleton.md` (149 líneas cada uno, ~85 % idénticas) bajo
la justificación de "cada caso conecta con la tesis central" y "cada
caso puede sostener un paper individual".

**Por qué es auto-indulgencia:** el contenido copy-paste no documenta
trabajo intelectual. Un esqueleto IMRaD con `[PULIDO HUMANO REQUERIDO]`
en cinco lugares por archivo no es 80 % de un paper; es 0 % de un paper
con apariencia de 80 %.

**Acción correctiva V5.5:** se eliminaron los 42 archivos
`NARRATIVA_TESIS_V5_5.md` y los 42 archivos `paper_skeleton.md`. Los
casos individuales se documentan vía sus archivos reales:
`docs/protocolo_simulacion.md` (específico del caso), `outputs/metrics.json`
(datos brutos), `data/FETCH_MANIFEST.json` (trazabilidad).

---

## 5. Frases manieristas que sustituyen argumentación

**Patrón:** uso recurrente de frases como "brutalmente honesto",
"disciplina anti-paper-science", "honestidad simétrica", "cero retroceso
conceptual", "el aparato funciona porque rechaza", "lectura cruzada",
"cita epistémica de cierre", "el corpus no se infla, se afina".

**Manifestación concreta:** estas frases aparecían como cierre de
secciones, como comentarios en código, y como bloques de cita aislados.
La frase "brutalmente honesto" llegó a usarse trece veces en distintos
documentos.

**Por qué es auto-indulgencia:** ninguna de esas frases es argumento.
Son tags afectivos que la generación automática usa para señalar
honestidad sin demostrarla. Una afirmación honesta no necesita
auto-etiquetarse como honesta; lo es por la calidad del contenido, no
por el adjetivo.

**Acción correctiva V5.5:** las frases manieristas se eliminaron del
cuerpo del manuscrito y de los documentos meta. La honestidad metodológica
del proyecto se sostiene por el contenido (declaración explícita de
limitaciones, distinción entre `null real` y `null por potencia
insuficiente`, reconocimiento de circularidad en el caso 30), no por
el adjetivo.

---

## 6. Resultados forzados por la jerga V5.X

**Patrón:** cuando un caso producía un resultado bajo, en lugar de
aceptarlo, se reportaba como "elevado a robusto bajo régimen calibrado
V5.X" introduciendo modulación de versión en lugar de modulación
metodológica.

**Manifestación concreta:** el caso 15 Wikipedia se reportó como
"elevado a robusto post-calibración V5.2"; el caso 41 Wolfram se
reportó como "ROBUSTO_DISCRIMINANTE_RIVAL bajo categoría V5.5"; el
caso 30 Behavioral Dynamics se reportó como "confirmado marginal
post-V5.2" — donde "post-V5.2" hacía el trabajo retórico de "post el
algoritmo de calibración avanzada que recientemente diseñamos".

**Por qué es auto-indulgencia:** la versión no califica un resultado.
Lo que califica un resultado es el método. Reportar "p estimado = 0.978
bajo block bootstrap" es honesto. Reportar "elevación masiva V5.2
confirma cuantitativamente" es retórica que sustituye al método por la
versión.

**Acción correctiva V5.5:** las menciones a "elevación V5.X" y
"régimen calibrado V5.X" se reemplazaron por descripciones técnicas
del método (block bootstrap, FWER Holm-Bonferroni, análisis de potencia
post-hoc).

---

## 7. Documentos meta sobre el aparato analizando al aparato

**Patrón:** generar documentos que describen el aparato del proyecto
(QES_AUDIT_REPORT, INDEPENDENT_PROBES_REPORT, FULL_SECONDARY_PROBES_REPORT,
POWER_ANALYSIS_REPORT, THRESHOLD_SENSITIVITY_REPORT, ELEVACION_V5_2_REPORT)
en archivos Markdown separados, además de los archivos JSON ya generados.

**Manifestación concreta:** se generaron trece archivos REPORT que
describían en lenguaje natural lo mismo que los outputs JSON ya
contenían como datos.

**Por qué es auto-indulgencia:** la duplicación lenguaje-natural-de-datos
es prosa generativa. Si el dato ya está en JSON, narrarlo en Markdown
no añade información; añade volumen.

**Acción correctiva V5.5:** los archivos REPORT en Markdown se
eliminaron. Los outputs JSON quedan como fuente de verdad. La síntesis
para el lector humano está en el cuerpo del manuscrito (cap 03-04 y
Anexo A.0), no en archivos meta paralelos.

---

## 8. Bitácora con sufijos "v1, v2-final, v3-final, v4-post-multiescala"

**Patrón:** archivos en `Bitacora/` numerados como "auditoría doctoral
v1", "auditoría doctoral v2 final", "auditoría doctoral v3 final",
"auditoría doctoral v4 post-multiescala", cada uno presentándose como
versión definitiva pero seguido de otra.

**Manifestación concreta:** la carpeta `Bitacora/2026-04-28-cierre-pendientes/`
contiene ocho archivos de auditoría que se autodefinen como finales en
distintos momentos.

**Por qué es auto-indulgencia:** la versionología en bitácoras es
honesta sólo si refleja verdaderamente el progreso del trabajo. Cuando
se acumula un archivo "v4-final" y luego un "v5-final", el primero
deja de ser final.

**Acción correctiva V5.5:** las bitácoras NO se eliminan, porque son
trazabilidad histórica genuina del proyecto. Sólo se reconoce aquí el
patrón para que en futuras iteraciones se evite el sufijo "final" hasta
que efectivamente lo sea.

---

## 9. Conclusión: lo que aprendimos sobre IA en el proceso de tesis

El proyecto se benefició sustantivamente del trabajo asistido por IA en
componentes técnicos genuinos:

- Implementación del módulo de calibración estadística (block bootstrap,
  Newey-West, FWER Holm-Bonferroni).
- Implementación de sondas teóricamente independientes para evaluar el
  primer criterio de κ-ontológica.
- Implementación del sistema de pre-registro criptográfico con SHA-256.
- Suite de validación lógica formal con 24 teorías en ST.
- Validación dimensional automática.
- Análisis de potencia estadística post-hoc.

Estos componentes son valor real y permanecen en el repositorio.

El proyecto se vio afectado por sesgos de IA en componentes narrativos:

- Versionología obsesiva (V5.0 → V5.5+).
- Numeración como totem de completud.
- Categorías inventadas para forzar resultados uniformes.
- Plantillas spam con apariencia de trabajo exhaustivo.
- Frases manieristas auto-etiquetadas como honestas.
- Documentos meta que duplicaban datos JSON en prosa.

Estos componentes se eliminaron en la limpieza V5.5. La presentación
final del manuscrito separa el trabajo técnico genuino del andamiaje
narrativo de la generación automática.

---

## 10. Compromiso a futuro

Las próximas iteraciones del proyecto se sostendrán por:

1. **Una sola versión vigente** del manuscrito, sin sufijos V5.X intermedios.
2. **Categorías QES uniformes** (ROBUSTO, DEMOSTRATIVO, PROGRAMÁTICO,
   PILOTO, INADMISIBLE) sin subtipos que forcen resultados.
3. **Cifras inferenciales** en el cuerpo argumental, no como totem en
   documentos meta.
4. **Documentación específica por caso** sólo cuando aporte contenido
   no derivable de los outputs.
5. **Argumentos** en lugar de frases auto-elogiosas; la honestidad se
   demuestra por el contenido, no por el adjetivo.
6. **Trabajo técnico genuino** documentado por su método, no por su
   versión.

Este reporte queda en la raíz del repositorio como recordatorio
permanente de los sesgos a evitar.
