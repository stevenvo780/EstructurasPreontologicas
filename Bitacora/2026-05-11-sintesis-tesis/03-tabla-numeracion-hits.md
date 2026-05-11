# Tabla 03 — Hits de numeración triplicada/duplicada

**Fecha auditoría:** 2026-05-11
**Bug:** `scripts/number_tables.py` ejecutado con regex de single-level (pre-commit 052a073) produjo labels duplicados al re-ejecutarse sobre archivos ya etiquetados con multi-level.
**Total ocurrencias:** 96
**Archivos afectados:** 33
**Líneas eliminables (excess label + blank):** ~312

## Resumen por archivo

| Archivo | Línea | Duplicado | Label |
|---------|-------|-----------|-------|
| `00-proyecto/07-glosario-operativo.md` | 190 | x2 | `**Tabla 0.7.1.**` |
| `01-diagnostico/02-objeciones-y-riesgos.md` | 120 | x3 | `**Tabla 1.2.1.**` |
| `01-diagnostico/03-estado-del-arte.md` | 102 | x3 | `**Tabla 1.3.1.**` |
| `02-fundamentos/02-epistemologia-de-la-compresion.md` | 12 | x3 | `**Tabla 2.2.1.**` |
| `02-fundamentos/02-epistemologia-de-la-compresion.md` | 178 | x3 | `**Tabla 2.2.2.**` |
| `02-fundamentos/03-categorias-objetos-propiedades-e-identidad.md` | 48 | x3 | `**Tabla 2.3.1.**` |
| `02-fundamentos/03-categorias-objetos-propiedades-e-identidad.md` | 135 | x3 | `**Tabla 2.3.2.**` |
| `02-fundamentos/04-anclaje-conductual-ecologico.md` | 19 | x3 | `**Tabla 2.4.1.**` |
| `02-fundamentos/04-anclaje-conductual-ecologico.md` | 191 | x3 | `**Tabla 2.4.2.**` |
| `02-fundamentos/05-temporalidad-y-causalidad.md` | 138 | x3 | `**Tabla 2.5.1.**` |
| `02-fundamentos/06-dimension-normativa-y-etica.md` | 60 | x3 | `**Tabla 2.6.1.**` |
| `03-formalizacion/01-aparato-formal.md` | 218 | x3 | `**Tabla 3.1.1.**` |
| `03-formalizacion/01-aparato-formal.md` | 240 | x3 | `**Tabla 3.1.2.**` |
| `03-formalizacion/02-criterios-de-legitimidad-y-metodo.md` | 112 | x3 | `**Tabla 3.2.1.**` |
| `03-formalizacion/03-auditoria-ontologica-y-diseno-de-investigacion.md` | 90 | x3 | `**Tabla 3.3.1.**` |
| `03-formalizacion/03-auditoria-ontologica-y-diseno-de-investigacion.md` | 123 | x3 | `**Tabla 3.3.2.**` |
| `03-formalizacion/03-auditoria-ontologica-y-diseno-de-investigacion.md` | 229 | x3 | `**Tabla 3.3.3.**` |
| `03-formalizacion/04-operacionalizacion-de-kappa.md` | 141 | x3 | `**Tabla 3.4.1.**` |
| `03-formalizacion/04-operacionalizacion-de-kappa.md` | 188 | x3 | `**Tabla 3.4.2.**` |
| `03-formalizacion/05-etica-y-gobernanza-de-datos.md` | 11 | x3 | `**Tabla 3.5.1.**` |
| `03-formalizacion/05-etica-y-gobernanza-de-datos.md` | 34 | x3 | `**Tabla 3.5.2.**` |
| `03-formalizacion/05-etica-y-gobernanza-de-datos.md` | 71 | x3 | `**Tabla 3.5.3.**` |
| `03-formalizacion/05-etica-y-gobernanza-de-datos.md` | 136 | x3 | `**Tabla 3.5.4.**` |
| `03-formalizacion/06-mapa-operadores-formales.md` | 115 | x2 | `**Tabla 3.6.1.**` |
| `03-formalizacion/06-mapa-operadores-formales.md` | 134 | x2 | `**Tabla 3.6.2.**` |
| `03-formalizacion/06-mapa-operadores-formales.md` | 155 | x2 | `**Tabla 3.6.3.**` |
| `03-formalizacion/06-mapa-operadores-formales.md` | 173 | x2 | `**Tabla 3.6.4.**` |
| `03-formalizacion/06-mapa-operadores-formales.md` | 202 | x2 | `**Tabla 3.6.5.**` |
| `03-formalizacion/06-mapa-operadores-formales.md` | 220 | x2 | `**Tabla 3.6.6.**` |
| `03-formalizacion/06-mapa-operadores-formales.md` | 239 | x2 | `**Tabla 3.6.7.**` |
| `03-formalizacion/07-plantilla-dossier-anclaje.md` | 31 | x2 | `**Tabla 3.7.1.**` |
| `03-formalizacion/07-plantilla-dossier-anclaje.md` | 78 | x2 | `**Tabla 3.7.2.**` |
| `03-formalizacion/07-plantilla-dossier-anclaje.md` | 93 | x2 | `**Tabla 3.7.3.**` |
| `03-formalizacion/07-plantilla-dossier-anclaje.md` | 138 | x2 | `**Tabla 3.7.4.**` |
| `03-formalizacion/07-plantilla-dossier-anclaje.md` | 162 | x2 | `**Tabla 3.7.5.**` |
| `03-formalizacion/08-validacion-logica-st.md` | 59 | x2 | `**Tabla 3.8.1.**` |
| `04-debates/01-debates-con-posiciones-rivales.md` | 37 | x3 | `**Tabla 4.1.1.**` |
| `04-debates/01-debates-con-posiciones-rivales.md` | 67 | x3 | `**Tabla 4.1.2.**` |
| `04-debates/01-debates-con-posiciones-rivales.md` | 97 | x3 | `**Tabla 4.1.3.**` |
| `04-debates/01-debates-con-posiciones-rivales.md` | 127 | x3 | `**Tabla 4.1.4.**` |
| `04-debates/01-debates-con-posiciones-rivales.md` | 157 | x3 | `**Tabla 4.1.5.**` |
| `04-debates/01-debates-con-posiciones-rivales.md` | 186 | x3 | `**Tabla 4.1.6.**` |
| `04-debates/01-debates-con-posiciones-rivales.md` | 215 | x3 | `**Tabla 4.1.7.**` |
| `04-debates/01-debates-con-posiciones-rivales.md` | 244 | x3 | `**Tabla 4.1.8.**` |
| `04-debates/01-debates-con-posiciones-rivales.md` | 280 | x3 | `**Tabla 4.1.9.**` |
| `04-debates/01-debates-con-posiciones-rivales.md` | 310 | x3 | `**Tabla 4.1.10.**` |
| `04-debates/01-debates-con-posiciones-rivales.md` | 348 | x3 | `**Tabla 4.1.11.**` |
| `04-debates/01-debates-con-posiciones-rivales.md` | 382 | x3 | `**Tabla 4.1.12.**` |
| `04-debates/01-debates-con-posiciones-rivales.md` | 422 | x3 | `**Tabla 4.1.13.**` |
| `04-debates/01-debates-con-posiciones-rivales.md` | 485 | x3 | `**Tabla 4.1.14.**` |
| `04-debates/01-debates-con-posiciones-rivales.md` | 505 | x3 | `**Tabla 4.1.15.**` |
| `04-debates/02-limitaciones-y-puntos-de-presion.md` | 137 | x3 | `**Tabla 4.2.1.**` |
| `04-debates/02-limitaciones-y-puntos-de-presion.md` | 154 | x3 | `**Tabla 4.2.2.**` |
| `04-debates/03-tabla-comparativa-rivales.md` | 13 | x2 | `**Tabla 4.3.1.**` |
| `04-debates/03-tabla-comparativa-rivales.md` | 32 | x2 | `**Tabla 4.3.2.**` |
| `04-debates/03-tabla-comparativa-rivales.md` | 59 | x2 | `**Tabla 4.3.3.**` |
| `04-debates/04-anticipacion-objeciones-filosoficas.md` | 73 | x2 | `**Tabla 4.4.1.**` |
| `04-debates/04-anticipacion-objeciones-filosoficas.md` | 289 | x2 | `**Tabla 4.4.2.**` |
| `04-debates/05-limitaciones-declaradas-consolidacion.md` | 15 | x2 | `**Tabla 4.5.1.**` |
| `04-debates/05-limitaciones-declaradas-consolidacion.md` | 34 | x2 | `**Tabla 4.5.2.**` |
| `04-debates/05-limitaciones-declaradas-consolidacion.md` | 51 | x2 | `**Tabla 4.5.3.**` |
| `04-debates/05-limitaciones-declaradas-consolidacion.md` | 70 | x2 | `**Tabla 4.5.4.**` |
| `04-debates/05-limitaciones-declaradas-consolidacion.md` | 110 | x2 | `**Tabla 4.5.5.**` |
| `04-debates/05-limitaciones-declaradas-consolidacion.md` | 131 | x2 | `**Tabla 4.5.6.**` |
| `04-debates/05-limitaciones-declaradas-consolidacion.md` | 155 | x2 | `**Tabla 4.5.7.**` |
| `04-debates/05-limitaciones-declaradas-consolidacion.md` | 175 | x2 | `**Tabla 4.5.8.**` |
| `05-aplicaciones/00-criterios-de-admision.md` | 63 | x3 | `**Tabla 5.0.1.**` |
| `05-aplicaciones/00-criterios-de-admision.md` | 77 | x3 | `**Tabla 5.0.2.**` |
| `05-aplicaciones/01-mente-memoria-yo.md` | 178 | x3 | `**Tabla 5.1.1.**` |
| `05-aplicaciones/02-biologia-y-ecologia.md` | 180 | x3 | `**Tabla 5.2.1.**` |
| `05-aplicaciones/03-sistemas-tecnicos-distribuidos.md` | 93 | x3 | `**Tabla 5.3.1.**` |
| `05-aplicaciones/04-instituciones-mercado-y-estado.md` | 134 | x3 | `**Tabla 5.4.1.**` |
| `05-aplicaciones/05-dinamica-conductual-reconstruccion-warren.md` | 210 | x3 | `**Tabla 5.5.1.**` |
| `05-aplicaciones/06-corpus-multiescala.md` | 31 | x3 | `**Tabla 5.6.1.**` |
| `05-aplicaciones/06-corpus-multiescala.md` | 49 | x3 | `**Tabla 5.6.2.**` |
| `05-aplicaciones/06-corpus-multiescala.md` | 61 | x3 | `**Tabla 5.6.3.**` |
| `05-aplicaciones/06-corpus-multiescala.md` | 113 | x3 | `**Tabla 5.6.4.**` |
| `05-aplicaciones/06-corpus-multiescala.md` | 170 | x3 | `**Tabla 5.6.5.**` |
| `05-aplicaciones/07-mapa-aplicaciones-corpus.md` | 24 | x2 | `**Tabla 5.7.1.**` |
| `05-aplicaciones/07-mapa-aplicaciones-corpus.md` | 45 | x2 | `**Tabla 5.7.2.**` |
| `05-aplicaciones/07-mapa-aplicaciones-corpus.md` | 70 | x2 | `**Tabla 5.7.3.**` |
| `05-aplicaciones/07-mapa-aplicaciones-corpus.md` | 87 | x2 | `**Tabla 5.7.4.**` |
| `05-aplicaciones/07-mapa-aplicaciones-corpus.md` | 99 | x2 | `**Tabla 5.7.5.**` |
| `05-aplicaciones/07-mapa-aplicaciones-corpus.md` | 118 | x2 | `**Tabla 5.7.6.**` |
| `05-aplicaciones/07-mapa-aplicaciones-corpus.md` | 131 | x2 | `**Tabla 5.7.7.**` |
| `05-aplicaciones/07-mapa-aplicaciones-corpus.md` | 146 | x2 | `**Tabla 5.7.8.**` |
| `05-aplicaciones/07-mapa-aplicaciones-corpus.md` | 165 | x2 | `**Tabla 5.7.9.**` |
| `06-cierre/01-conclusion-demostrativa.md` | 49 | x3 | `**Tabla 6.1.1.**` |
| `06-cierre/01-conclusion-demostrativa.md` | 135 | x3 | `**Tabla 6.1.2.**` |
| `06-cierre/01-conclusion-demostrativa.md` | 206 | x3 | `**Tabla 6.1.3.**` |
| `06-cierre/01-conclusion-demostrativa.md` | 228 | x3 | `**Tabla 6.1.4.**` |
| `06-cierre/03-hoja-de-ruta-para-tesis-final.md` | 82 | x3 | `**Tabla 6.3.1.**` |
| `06-cierre/03-hoja-de-ruta-para-tesis-final.md` | 196 | x3 | `**Tabla 6.3.2.**` |
| `07-bibliografia/01-bibliografia-orientativa.md` | 8 | x3 | `**Tabla 7.1.**` |
| `07-bibliografia/01-bibliografia-orientativa.md` | 319 | x3 | `**Tabla 7.2.**` |
| `07-bibliografia/README.md` | 17 | x3 | `**Tabla 7.1.**` |

## Muestras literales (primeros 6 hits)

### `00-proyecto/07-glosario-operativo.md:190` (x2)
```
**Tabla 0.7.1.**

**Tabla 0.7.1.**

```

### `01-diagnostico/02-objeciones-y-riesgos.md:120` (x3)
```
**Tabla 1.2.1.**

**Tabla 1.2.1.**

**Tabla 1.2.1.**

```

### `01-diagnostico/03-estado-del-arte.md:102` (x3)
```
**Tabla 1.3.1.**

**Tabla 1.3.1.**

**Tabla 1.3.1.**

```

### `02-fundamentos/02-epistemologia-de-la-compresion.md:12` (x3)
```
**Tabla 2.2.1.**

**Tabla 2.2.1.**

**Tabla 2.2.1.**

```

### `02-fundamentos/02-epistemologia-de-la-compresion.md:178` (x3)
```
**Tabla 2.2.2.**

**Tabla 2.2.2.**

**Tabla 2.2.2.**

```

### `02-fundamentos/03-categorias-objetos-propiedades-e-identidad.md:48` (x3)
```
**Tabla 2.3.1.**

**Tabla 2.3.1.**

**Tabla 2.3.1.**

```

