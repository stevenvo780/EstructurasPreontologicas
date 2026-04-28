# Consistencia lógica con ST

Este subproyecto usa `@stevenvo780/st-lang` como **motor de consistencia** para el repositorio de tesis. La idea no es convertir la tesis en un sistema cerrado ni fingir que una formalización lógica reemplaza el trabajo filosófico. La idea es más sobria y útil:

> usar ST para verificar que el núcleo declarativo del proyecto no incurra en contradicciones simples, que ciertas consecuencias centrales sean derivables y que algunos claims queden trazados hacia pasajes del repositorio.

## Qué valida esta capa

### 1. Núcleo ontológico

Verifica que el corazón de la tesis sea satisfacible y que se deriven consecuencias básicas como:

- de compresión categorial a no reificación;
- de materialidad a rechazo del dualismo;
- de niveles no separados a rechazo del emergentismo sustancialista;
- de preservación estructural a rechazo del reduccionismo plano.

### 2. Criterios de legitimidad

Verifica que la noción de categoría legítima pueda reconstruirse como conjunción de criterios mínimos y que de ahí se sigan formas más fuertes de legitimidad.

### 3. Debates y límites

Verifica que el marco no obligue a aceptar dualismo, reduccionismo plano, emergentismo fuerte o constructivismo arbitrario.

### 4. Text Layer

Usa `passage`, `formalize`, `claim`, `support`, `confidence` y `context` para anclar formalizaciones a archivos reales del repositorio, sobre todo el manuscrito-fuente histórico (`Bitacora/2026-04-27-integracion-jacob/00-tesis-fuente-original.md`), los capítulos numerados, `TesisFinal/Tesis.md` y `07-bibliografia/01-bibliografia-orientativa.md`.

## Estructura

```text
08-consistencia-st/
├── package.json
├── README.md
├── scripts/
│   └── run-st-consistency.mjs
├── theories/
│   ├── 00-nucleo-ontologico.st
│   ├── 01-criterios-legitimidad.st
│   ├── 02-debates-y-limites.st
│   ├── 03-text-layer-tesis.st
│   └── 04-text-layer-bibliografia.st
└── reports/
    └── ultimo-reporte.md
```

## Tabla mínima de símbolos

La formalización usa átomos breves para mantener legibles los scripts.

### Núcleo

- `M`: materialidad del fenómeno explicable.
- `C`: las categorías funcionan como compresiones.
- `R`: no reificación categorial.
- `L`: los niveles no son mundos separados.
- `E`: la explicación preserva estructura relevante.
- `D`: rechazo del dualismo.
- `S`: rechazo del emergentismo sustancialista.
- `P`: rechazo del reduccionismo plano.

### Legitimidad

- `A`: anclaje material.
- `B`: dependencia empírica.
- `F`: fidelidad relacional.
- `I`: poder inferencial.
- `V`: poder predictivo.
- `T`: poder interventivo.
- `U`: reversibilidad parcial.
- `O`: economía explicativa.
- `N`: no reificación.
- `G`: categoría legítima.
- `H`: categoría fuertemente legítima.

## Cómo usarlo

### Instalar dependencias

Desde `08-consistencia-st/`, instala el paquete de ST.

### Ejecutar la suite

- `npm run st:check`
- `npm run st:check:verbose`

### Renderizar claims trazados

- `npm run st:render:claims`
- `npm run st:render:biblio`

## Qué produce la suite

El runner genera `reports/ultimo-reporte.md` con:

- archivo ejecutado;
- modo usado (`check` o `run`);
- código de salida;
- salida capturada;
- estado global de la suite.

## Criterio filosófico de uso

ST aquí no sirve como detector de verdad total. Sirve como:

1. **verificador de consistencia local**;
2. **comprobador de derivaciones explícitas**;
3. **capa de trazabilidad** entre pasajes del proyecto y formalizaciones mínimas.

Dicho en corto: no reemplaza la tesis, pero sí le pone un cinturón lógico bastante útil.