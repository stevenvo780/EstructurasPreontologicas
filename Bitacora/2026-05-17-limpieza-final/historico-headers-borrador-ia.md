# Histórico — drenaje de blockquotes BORRADOR-IA en headers de capítulos clave (2026-05-17)

Drenaje de los blockquotes "BORRADOR-IA — pendiente firma H-J8" visibles al abrir cinco capítulos clave. Razón: ruido infraestructural visible para Ricardo en revisión. Sustitución por HTML comments discretos al inicio del archivo (`<!-- requires: H-J8 ... -->`). El marcador de firma autoral se preserva, pero deja de ser texto visible.

NO se eliminó contenido sustantivo. Solo se removió la metadescripción interna sobre fases de consolidación (D.2, D.3, D.4), fechas de síntesis (2026-05-11) y enumeración de decisiones pendientes Jacob ya registradas en `TAREAS_PENDIENTES.md`.

---

## 1. `00-proyecto/01-estructura-y-plan.md` línea 3

Texto eliminado:

```
> **BORRADOR-IA — pendiente firma H-J8.** Este archivo es el resultado de la fusión D.4 (`00-proyecto/01-estructura-general.md` + `00-proyecto/03-plan-de-capitulos.md` → un solo archivo) ejecutada como consolidación editorial bajo Fase 2 de la síntesis 2026-05-11. Reemplaza ambos archivos sin afectar `TesisFinal/Tesis.md` (ninguno entra al ensamblado). Decisión pendiente Jacob: (1) si `01-estructura-y-plan.md` debe promoverse al cuerpo del manuscrito como capítulo introductorio metodológico; (2) si la política «un capítulo = una pregunta = un interlocutor principal» debe sobrevivir como doctrina declarada en este archivo o sólo operativa en el cuerpo.
```

---

## 2. `00-proyecto/03-plan-de-capitulos.md` línea 3

Texto eliminado:

```
> **Stub redirect (fusión D.4, cf. marcador BORRADOR-IA H-J8 vivo en `00-proyecto/01-estructura-y-plan.md` §encabezado).** El contenido de este archivo fue fusionado en `00-proyecto/01-estructura-y-plan.md` como parte de la consolidación editorial D.4 (Fase 2, síntesis 2026-05-11). Este stub existe únicamente para que las referencias cruzadas vivas no apunten a archivo inexistente; el marcador pendiente de firma autoral H-J8 vive en el archivo destino, no aquí.
```

---

## 3. `04-debates/01-debates-con-posiciones-rivales.md` línea 3

Texto eliminado:

```
> **BORRADOR-IA — pendiente firma H-J8.** Este capítulo es el resultado de la consolidación D.2 (reducción 491→~246 líneas + migración de 7 desarrollos extensos a `04-debates/_extendido/rival-<X>.md`) ejecutada como consolidación editorial bajo Fase 2 de la síntesis 2026-05-11. Decisiones pendientes Jacob: (1) confirmar la división rivales tabulares §2 vs rivales discursivos §3; (2) confirmar la lista de siete `_extendido/rival-<X>.md` ya creados; (3) decidir si la frase eslogan «Wolfram fundamenta; la tesis disciplina» se conserva o se reemplaza (auditoría F04-06 la marca como manierismo que oculta asimetría modal).
```

---

## 4. `04-debates/02-limitaciones-y-puntos-de-presion.md` línea 3

Texto eliminado:

```
> **BORRADOR-IA — pendiente firma H-J8.** Este capítulo es el resultado de la reducción D.3 (200→~65 líneas) ejecutada como consolidación editorial bajo Fase 2 de la síntesis 2026-05-11: §1, §4, §6, §8 originales se eliminaron por subsunción en `04-debates/05-limitaciones-declaradas-consolidacion.md` (L1-L20); se preservaron §7 «Riesgos heredados» (aquí §1), §9 «Lo que sí puede prometer» (aquí §2), §10 «Diálogo con interlocutores» (aquí §3), §11 «Filtro de objeciones futuras» (aquí §4) y §12 «Fórmula de honestidad filosófica» (aquí §5). Decisiones pendientes Jacob: (1) ratificar el nuevo título; (2) decidir si `02` permanece en posición canónica (capítulo 28) o se reordena después de `05`.
```

---

## 5. `06-cierre/01-conclusion-demostrativa.md` línea 3

Texto eliminado (informativo: enumeración exhaustiva de decisiones autorales pendientes ya registradas en `TAREAS_PENDIENTES.md`; ruido al abrir el capítulo final):

```
> **Decisiones autorales pendientes:** H-J1..H-J12 (firma filosófica) y H-U1..H-U2 + H-S1/H-S2 (procedimentales) listadas en `TAREAS_PENDIENTES.md`. Las secciones de este capítulo cuya prosa final espera firma de Jacob están registradas allí por identificador; no representan trabajo incompleto del aparato.
```

---

## Sustitución uniforme

Cada archivo recibe en lugar del blockquote un comment HTML al inicio (entre título y primera sección visible):

```html
<!-- requires: H-J8 (firma autoral pendiente; ver TAREAS_PENDIENTES.md) -->
```

Para `06-cierre/01-conclusion-demostrativa.md` el comment es:

```html
<!-- requires: H-J1..H-J12, H-U1..H-U2, H-S1/H-S2 (decisiones autorales pendientes; ver TAREAS_PENDIENTES.md) -->
```

## Verificación

- `python3 TesisFinal/build.py` re-ensambla `TesisFinal/Tesis.md` sin error.
- Inventario antes/después en `inventario-borrador-ia-antes.txt` / `inventario-borrador-ia-despues.txt` (de la misma carpeta).
