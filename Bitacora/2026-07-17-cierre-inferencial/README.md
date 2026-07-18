# Cierre inferencial del manuscrito y la web

**Fecha:** 2026-07-17

**Tipo de pasada:** auditoría filosófica, reconciliación prosa-datos, cierre editorial y build

**Estado:** cambios técnicos cerrados; decisiones autorales H-J2/H-J8 abiertas

## 1. Diagnóstico

La versión pública mezclaba tres niveles distintos:

1. salidas crudas o históricas de `metrics.json`;
2. resultados estrictos del régimen B-T2.1;
3. afirmaciones de generalidad ontológica.

Esa mezcla producía contradicciones visibles: el resumen declaraba 0 Strong robustos mientras el dashboard mostraba 1; capítulos centrales usaban entre 4 y 6 Strong históricos; el corpus inter-escala convertía datos sintéticos en evidencia de invariancia ontológica; y el caso 30 se presentaba como demostración pese a `overall_pass=false` y block bootstrap p≈0.978.

## 2. Decisión de alcance

La tesis se reordenó en tres estratos:

- **programa ontológico:** hipótesis material-relacional y multiescalar, abierta;
- **tesis epistemológica:** el cierre se indexa a fenómeno, sonda, modelo, baseline, ventana y pregunta;
- **resultado metodológico:** protocolo C1-C5, EDI, controles, pre-registros y trazabilidad.

El EDI autoriza una afirmación epistemológica local sobre ganancia predictiva. No autoriza por sí solo el paso a κ-ontológica ni a una ontología general.

## 3. Estado numérico autoritativo

| Estatus inter-dominio B-T2.1 | N |
|---|---:|
| Strong robusto puro confirmado | 0 |
| Weak validado | 1, Energía |
| Candidato | 1, Starlink |
| Falsificaciones locales | 4, casos 19, 20, 23 y 24 |
| Controles negativos rechazados | 3, casos 06, 07 y 08 |
| Sin cierre estricto | 21 |

El corpus inter-escala se declara como prueba de portabilidad computacional sobre datos sintéticos. El caso 30 se declara piloto metodológico.

## 4. Cambios principales

- reescritura de introducción, preguntas, hipótesis, resumen y abstract;
- reconstrucción completa de la conclusión;
- reconciliación del mapa de aplicaciones y los corpus inter-dominio e inter-escala;
- reclasificación del caso Warren como ancla paradigmática con 9/14 componentes;
- retiro del caso 30 como demostración conductual;
- retiro del AUC histórico como evidencia de validación externa;
- actualización de la guía de defensa y del estado institucional;
- corrección del dashboard, explorador de casos y fichas para distinguir salida técnica de estatus estricto;
- actualización de apéndices para marcar tablas históricas y mostrar el estado B-T2.1.
- segunda pasada editorial de concisión: salida del cuerpo principal de README técnicos, hoja de ruta y cuadros duplicados; traslado del glosario al final; condensación de anclaje B, criterios de admisión, objeciones y limitaciones.

Toda prosa filosófica nueva que afecta el alcance quedó marcada `BORRADOR-IA · requires: H-J2/H-J8` conforme a las reglas del repositorio.

## 5. Build y QA

- `python3 TesisFinal/build.py`: 7.159 líneas, 75.792 palabras, 549.160 bytes.
- `python3 TesisFinal/build_pdf.py`: 204 páginas, A4, 743.422 bytes.
- Verificación geométrica PyMuPDF: 0 páginas con texto fuera del área.
- Inspección visual: portada, resumen, fundamentos, objeciones, limitaciones, conclusión y apéndices.
- `npm run build`: 4.460 módulos transformados, build Vite exitoso.
- `python3 harness/cli.py verify --all`: sin fallos; advertencias conocidas en deuda y pre-registros.
- `git diff --check`: sin errores.

## 6. Deuda que no puede cerrarse automáticamente

1. H-J2: decidir si la generalidad ontológica es regulativa, constitutiva con argumento independiente o programática.
2. H-J8: firmar la arquitectura final y la reclasificación del caso ancla.
3. B-T2.1: completar el régimen estricto sobre el corpus.
4. B-T2.4: sustituir o revalidar casos inter-escala con datos reales.
5. Revisión externa ciega y requisitos institucionales H-U1 a H-U5.
6. Despliegue del sitio y publicación en GitHub ejecutados tras autorización explícita del autor.

## 7. Artefactos

- `TesisFinal/Tesis.md`
- `TesisFinal/Tesis.pdf`
- `output/pdf/Estructuras_Pre_Ontologicas_2026-07-17.pdf`
- `TesisFinal/build_pdf.py`
- `TesisFinal/pdf_sanitize.lua`
- `TesisFinal/pdf_header.tex`
