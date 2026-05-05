# F02-01 — Woodward 2003 p.59: cita verbatim sin verificación primaria

**Fecha:** 2026-05-04
**Sub-agente:** harness daemon (auditoría read-only)
**Archivos auditados:** `02-fundamentos/05-temporalidad-y-causalidad.md` líneas 48 y 89.
**Acceptance:** verbatim verificado contra PDF Oxford de Woodward 2003 (definición M en pp.98-99 cap.2 §2.4) **o** párrafo reescrito sin pretender cita literal.

## (a) Verificación de la afirmación

El manuscrito cita en dos lugares (líneas 48 y 89) la formulación M de Woodward atribuyéndola a:

> Woodward 2003, *Making Things Happen*, **cap. 2 §2.1 "Interventions and Causation", Oxford UP 2003, p. 59**

con el verbatim:

> *"X causes Y if and only if there are background circumstances B such that if some (single) intervention that changes the value of X (and no other variable) were to occur in B, then Y would change"*

**Resultado de la verificación contra el PDF local:**

- PDF en `07-bibliografia/Woodward - Making Things Happen (2003).pdf` existe (419 pp., 22.8 MB), pero su `Producer = libtiff / tiff2pdf` confirma que es un **escaneo image-only sin capa de texto**. `pdftotext` devuelve cadena vacía sobre el rango cap. 2.
- En el host actual **no hay `tesseract` ni `ocrmypdf` instalados** (`which tesseract` → not found). Por tanto **no se puede verificar verbatim ni paginación desde la asistencia en esta pasada**.
- La nota al pie del propio manuscrito (línea 92) ya declara la cita como "**pendiente de re-verificación con OCR** sobre el PDF local".

**Tensión con la acceptance:** la propia rúbrica dice que la definición canónica (M) de Woodward está en **pp. 98-99 §2.4**, no en p. 59 §2.1. La literatura secundaria estándar (Woodward & Hitchcock 2003, *Noûs* 37; Hitchcock 2007 *PPR*; Strevens 2007 reseña en *PhilRev*) cita la formulación (M) con etiqueta explícita en §2.7 / pp. 98 ss. de Woodward 2003 — §2.1 contiene la motivación informal, no el enunciado etiquetado (M). La paginación p. 59 actualmente impresa en el manuscrito **es probablemente errónea por desplazamiento de sección** y no se ha podido confirmar ni refutar por imposibilidad técnica local (sin OCR).

## (b) Propuesta concreta

`needs_human` — la decisión es B-T (técnica con coste) más H-J (firma autoral). Dos rutas, ambas honestas:

**Ruta 1 (B-T, técnica):** instalar `tesseract-ocr` + `ocrmypdf` en el host, ejecutar
```bash
ocrmypdf "07-bibliografia/Woodward - Making Things Happen (2003).pdf" \
         "07-bibliografia/Woodward 2003 - OCR.pdf"
pdftotext -layout -f 95 -l 102 "07-bibliografia/Woodward 2003 - OCR.pdf" -
```
y localizar la formulación etiquetada **(M)** en §2.7 (pp. 98–99 según acceptance). Con la página confirmada, corregir las dos citas (líneas 48 y 89) cambiando "cap. 2 §2.1 ... p. 59" por la sección y página verificadas. Esta ruta resuelve el F02-01 con cita verbatim primaria.

**Ruta 2 (H-J, autoral, recorte conservador):** mientras la verificación OCR no se ejecute, reescribir las líneas 48 y 89 reemplazando la cita textual entrecomillada por **paráfrasis declarada como tal**, sin pretender literalidad:

> *La tesis adopta la teoría manipulabilista de Woodward (2003, Making Things Happen, cap. 2): X causa Y si una intervención sobre X en circunstancias de fondo apropiadas modifica el valor de Y. La formulación canónica (M) de Woodward — cuya cita verbatim queda pendiente de verificación contra el PDF original (escaneo image-only en `07-bibliografia/`) — es operacionalizable mediante el `do`-calculus de Pearl, lo cual basta para los fines argumentales del aparato EDI.*

Esta ruta cumple CLAUDE.md §5 ("cita textual con paginación o no cita") sin riesgo de cita-decorativa: declara explícitamente que es paráfrasis y que la verificación está pendiente.

**Recomendación de la asistencia:** Ruta 2 ya, Ruta 1 cuando Jacob/Steven puedan instalar OCR. La Ruta 2 no debilita el argumento (las "razones operativas" 1–3 de la línea 50 ss. no dependen de la formulación verbatim sino de la operacionalización vía intervención ablativa).

## (c) Costo argumentativo declarado

- **Si Ruta 2:** la tesis pierde el respaldo retórico de la cita verbatim de Woodward, pero **gana defensibilidad** frente a la objeción de "cita decorativa con paginación dudosa". El argumento sustantivo (sec. 2.1 §"Razones operativas") sobrevive intacto: la defensa de la causalidad woodwardiana es operacional (intervención ablativa = `do`), no exegética.
- **Si Ruta 1:** se conserva la cita verbatim pero se asume el coste técnico de instalar OCR y re-paginar dos referencias (líneas 48 y 89). Riesgo residual: si la formulación de p.59 difiere de la formulación canónica (M) de p.98-99, la cita podría estar mezclando dos versiones distintas que Woodward presenta secuencialmente en cap. 2 (versión informal pre-(M) en §2.1, versión (M) etiquetada en §2.7).
- **No hacer nada** mantendría la deuda actual ya declarada en línea 92, pero F02-01 quedaría abierta indefinidamente y el adversarial-reviewer ha señalado que esa deuda **es atacable por un evaluador externo** que abra el PDF y vea que p. 59 no contiene el verbatim afirmado.

## Estado

`needs_human` — requiere decisión de Jacob entre Ruta 1 (técnica, OCR) y Ruta 2 (autoral, paráfrasis). La asistencia no edita `Tesis.md` ni los capítulos sin firma humana en este punto.

## Anexo: hechos verificables sin OCR

- El PDF local existe y es image-only (verificado por `pdfinfo` y `pdftotext` vacío).
- El manuscrito ya declara la deuda en línea 92.
- La acceptance del harness señala explícitamente que la (M) canónica está en pp. 98-99 §2.4, divergente de la paginación actual del manuscrito (p. 59 §2.1).
- Sin tesseract/ocrmypdf en el host, la verificación primaria es imposible desde la asistencia headless.
