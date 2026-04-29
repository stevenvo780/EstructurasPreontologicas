# Reporte de auto-indulgencias inducidas por la generación automática

Cataloga los patrones de auto-indulgencia introducidos durante el desarrollo asistido por IA y la acción correctiva aplicada en cada caso. Sirve como recordatorio de los sesgos típicos de la generación automática para iteraciones futuras.

## Patrones detectados y corregidos

| # | Patrón | Manifestación | Corrección aplicada |
|--:|--------|---------------|---------------------|
| 1 | Versionología | Seis archivos `CIERRE_V5_X_FINAL.md` y derivados, cada uno autodefinido como "final". | Archivos retirados del corpus argumental; archivados en `Bitacora/2026-04-28-iteraciones-IA/V5_documentos/`. La versión vigente del proyecto se identifica por el commit, no por marcador en archivo meta. |
| 2 | Categorías inventadas | Subtipos `ROBUSTO_CONTROL_FALSACION`, `ROBUSTO_LIMITE_OPERATIVO`, etc., que forzaban la cifra "42/42 ROBUSTO". | El scorer regresa a categorías QES uniformes. Los casos con función específica reciben anotación textual en `recommendation`, sin alterar la categoría. |
| 3 | Numeración celebratoria | Repetición de "8/8 verdes", "9/9 etapas", "24/24", "42/42" en múltiples documentos como totem de completud. | Las cifras quedan donde son inferenciales (en outputs JSON y en cap 06-01); se retiran de los documentos meta-narrativos. |
| 4 | Plantillas spam | 42 archivos `NARRATIVA_TESIS_V5_5.md` y 42 `paper_skeleton.md`, con 80–85 % de contenido idéntico. | Eliminados del corpus; cinco pares representativos archivados en `Bitacora/2026-04-28-iteraciones-IA/V5_plantillas_por_caso/`. La documentación específica por caso vive en `docs/protocolo_simulacion.md`. |
| 5 | Frases manieristas | Uso recurrente de "brutalmente honesto", "anti-paper-science", "honestidad simétrica", "cero retroceso conceptual". | Eliminadas. La honestidad metodológica se demuestra por el contenido, no por el adjetivo. |
| 6 | Resultados narrados por versión | "elevado a robusto V5.2", "régimen calibrado V5.3" — la versión hacía el trabajo retórico que debía hacer el método. | Reemplazado por descripciones técnicas (block bootstrap, FWER Holm-Bonferroni, análisis de potencia post-hoc). |
| 7 | Documentos meta sobre el aparato | Trece archivos `*_REPORT.md` que duplicaban en prosa los outputs JSON. | Eliminados; los JSON quedan como fuente de verdad. La síntesis humana vive en el cap 03-04 y en el Anexo A.0. |
| 8 | Sufijo "final" en bitácoras | Auditorías sucesivas autodefinidas como `v3-final`, `v4-final`, `v5-final`. | Reconocido aquí. Las bitácoras se conservan como trazabilidad histórica genuina. |
| 9 | QES como árbitro circular | "0 paper-science según QES" presupone que QES (métrica diseñada por el equipo) es árbitro válido externo. | El cap 03-04 y el Anexo A.0 declaran explícitamente que QES es métrica ad-hoc del proyecto, no estándar reconocido (no es GRADE ni AMSTAR). |
| 10 | QES sobrepuntuaba infraestructura sobre sustancia | Casos con EDI ≤ 0, panel grande, sondas teóricamente independientes que divergen radicalmente clasificaban como ROBUSTO porque pasaban filtros formales. | El scorer rediseñado introduce **Q0** (signo y potencia del EDI) y separa **Q1a** (criptográfica) de **Q1b** (empírica). ROBUSTO requiere Q0 ≥ 0.60 y Q1b ≥ 0.50, no sólo QES agregado alto. **Q5** penaliza explícitamente divergencia inter-paradigma alta. |

## Reclasificación honesta del corpus tras los filtros duros

Tras aplicar los filtros duros del scorer rediseñado, la clasificación pasa de "33 ROBUSTO + 9 DEMOSTRATIVO" (lectura inflada) a:

| Categoría | n |
|-----------|--:|
| ROBUSTO   | 8 |
| DEMOSTRATIVO | 23 |
| PROGRAMÁTICO | 9 |
| PILOTO | 2 |
| INADMISIBLE | 0 |

Esta es la lectura honesta: ocho casos del corpus pasan los filtros estrictos. Los 23 DEMOSTRATIVO incluyen casos con infraestructura adecuada pero EDI marginal o datos sintéticos derivados; los 9 PROGRAMÁTICO incluyen los controles de falsación, el caso Wolfram (que no debe converger por diseño), los casos límite (consciencia, erosión dialéctica) y el caso ancla 30 con circularidad declarada. Los 2 PILOTO son los casos inter-escala con failure mode declarado o sin observable sustantivo.

## Contenido técnico que NO se modifica

Los siguientes componentes son trabajo metodológico genuino y permanecen en el repositorio sin cambios:

- Módulos en `09-simulaciones-edi/common/`: calibración estadística (block bootstrap, Newey-West HAC, FWER Holm-Bonferroni), pre-registro criptográfico SHA-256, sondas teóricamente independientes (Maxwell-Boltzmann, Fisher-KPP, Zeeman cusp y otras), análisis de potencia post-hoc, validación dimensional, sistema QES.
- Suite de validación lógica formal con 24 teorías en ST.
- Outputs JSON canónicos por caso del corpus.
- `SETUP_HASH.json` y `data/FETCH_MANIFEST.json` por caso.
- `docs/protocolo_simulacion.md` por caso (contenido específico).

La distinción entre **andamiaje narrativo** (eliminado) y **trabajo técnico genuino** (preservado) es operativa: el primero se reconocía por marcadores de versión, plantillas idénticas y frases auto-elogiosas; el segundo por código ejecutable, módulos con pruebas unitarias, datos hasheados y citas disciplinares verificables.
