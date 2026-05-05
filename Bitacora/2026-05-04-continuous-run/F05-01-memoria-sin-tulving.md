# F05-01 — Capítulo memoria sin Tulving / Schacter / Nader-LeDoux

**Fecha:** 2026-05-05
**Origen:** hallazgo `adversarial-reviewer` cap 05, 2026-05-05.
**Archivo señalado:** `05-aplicaciones/01-mente-memoria-yo.md` §2 (líneas 63–112), específicamente §2.6 "Rival principal" (línea 96–98).

## (a) Verificación de la afirmación

§2.6 hace dos afirmaciones sustantivas sobre literatura empírica de memoria:

1. "Modelo de memoria como almacén con buffers (modelo modal Atkinson-Shiffrin y descendientes)."
2. "Los datos publicados en la literatura sobre interferencia, forgetting y reconsolidación favorecen modelo dinámico, pero la discriminación cuantitativa fina queda como trabajo posterior."

**Problema (CLAUDE.md §5):** ambas afirmaciones invocan la literatura empírica sin **una sola cita textual paginada**. La sección entera (§2.1–§2.8) no cita a Tulving, Schacter, Squire, Nader-LeDoux, Atkinson-Shiffrin, ni a ningún investigador empírico de memoria post-1970. La distinción episódica/semántica/procedimental aparece en §2.5 ("la diferencia entre memoria episódica, memoria de trabajo y memoria procedimental se reformularía como diferencia entre tipos de atractor") **sin atribución a Tulving 1972**, que es la fuente canónica de esa distinción. La mención a "reconsolidación" en §2.3 y §2.6 no cita a **Nader, Schafe & LeDoux 2000** (*Nature* 406:722–726), que es la fuente canónica del fenómeno.

Esto cae bajo el F6 declarado por CLAUDE.md §5: "citas decorativas (autor invocado como autoridad sin engagement) son F6 — fallo declarado de la tesis". Aquí el problema es peor: ni siquiera hay cita decorativa; hay **invocación implícita de un consenso empírico sin nombrar fuentes**.

## (b) Verificación bibliográfica disponible

Búsqueda en `07-bibliografia/`:

```
ls 07-bibliografia/ | grep -iE "tulving|schacter|nader|ledoux|memory|memoria"
→ (sin resultados)
```

**No hay PDFs** de Tulving 1972/1983, Schacter 1996 *Searching for Memory*, Nader-Schafe-LeDoux 2000, ni Atkinson-Shiffrin 1968 en la biblioteca local. Sí hay PDFs adyacentes (Bechtel *Filosofía de la mente*, Maturana-Varela *De cuerpo presente* / *Árbol del conocimiento*, Dennett *La conciencia explicada*) pero ninguno cubre la literatura empírica específica que §2.6 invoca.

**Consecuencia:** no puedo producir citas verbatim paginadas verificadas. Producirlas desde memoria del modelo violaría CLAUDE.md §5 ("Cita textual con paginación o no cita") y §4 (reproducibilidad). El acceptance del task ("≥3 citas verbatim paginadas post-1970 incorporadas a §2.6") **no es ejecutable desde la asistencia sin las fuentes primarias**.

## (c) Propuesta operativa

**Acción correcta es bifurcada:**

1. **`needs_biblio` (B-T*):** disparar `/fetch-biblio` con queries:
   - Tulving E. (1972). *Episodic and semantic memory*. En Tulving & Donaldson (eds.), *Organization of Memory*, Academic Press, pp. 381–403.
   - Schacter D.L. (1996). *Searching for Memory: The Brain, the Mind, and the Past*, Basic Books.
   - Nader K., Schafe G.E., LeDoux J.E. (2000). "Fear memories require protein synthesis in the amygdala for reconsolidation after retrieval." *Nature* 406(6797):722–726.
   - (complementario) Squire L.R. (2004). "Memory systems of the brain: A brief history and current perspective." *Neurobiology of Learning and Memory* 82(3):171–177.

2. **`needs_human` (H-J*):** una vez los PDFs estén en `07-bibliografia/`, la incorporación a §2.6 implica una decisión filosófica que **no cierra desde la asistencia**: cuán fuerte es el compromiso del marco con la taxonomía de Tulving (sistemas múltiples) frente a la lectura dinamicista (Roediger, McClelland). Tres opciones con costos:
   - **Opción A (compromiso fuerte con sistemas múltiples):** adoptar Tulving-Schacter-Squire como anclaje; costo: el marco material-relacional queda parasitario de una taxonomía cognitivista clásica que precisamente §2.5 quería reformular.
   - **Opción B (apropiación crítica):** citar a Tulving 1972 como observación empírica robusta (la disociación episódica/semántica existe) pero leerla como diferencia de atractor, no de almacén; costo: requiere argumento sobre por qué la disociación neuropsicológica (e.g. K.C., H.M.) no implica almacenes separados.
   - **Opción C (anclaje en reconsolidación):** usar Nader et al. 2000 como caso paradigmático del marco dinámico (la traza no es objeto fijo recuperable, sino estado labilizable) y dejar Tulving/Schacter como literatura adyacente; costo: el peso del capítulo cae sobre un único hallazgo empírico.

**La recomendación de la asistencia:** Opción B con cita explícita a Nader et al. 2000 como evidencia más fuerte del lado dinámico. Pero la firma es de Jacob.

## Costo argumentativo declarado

- §2 del capítulo 05-01 actualmente **no es defendible bajo CLAUDE.md §5**: invoca "datos publicados" sin un solo paper citado.
- La reescritura no se puede ejecutar desde la asistencia sin las fuentes primarias en local.
- La decisión filosófica (qué relación tiene el marco con la taxonomía de sistemas múltiples) requiere firma de Jacob.

## Estado

**`needs_biblio` + `needs_human`.** No editar §2.6 hasta que (1) los PDFs estén en `07-bibliografia/` con citas verificables y (2) Jacob firme la opción A/B/C.

**Touches:** ninguno (read-only audit).
