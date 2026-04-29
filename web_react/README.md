# Web React — Estructuras Pre-Ontológicas

SPA en React+Vite+TypeScript que reemplaza la vista Jinja2 anterior.

## Stack

- **React 18** + **TypeScript** + **Vite 5**
- **React Router 6** para navegación
- **TanStack Query** para fetching/caching de la API
- **Tailwind CSS 3** con paleta editorial sobria
- **Lucide React** para iconografía
- **Recharts** para visualización de datos
- **react-markdown** + **rehype-katex** + **remark-math** para Markdown académico
- **mermaid** para diagramas
- **react-syntax-highlighter** para code blocks
- **Fuse.js** para búsqueda fuzzy (command palette)
- **framer-motion** para transiciones

## Páginas

| Ruta | Descripción |
|------|-------------|
| `/` | Dashboard: hero, KPIs, distribución, scatter EDI vs p, casos strong |
| `/tesis` | Manuscrito completo con TOC sticky, modo lectura, búsqueda |
| `/casos` | Grid de 30+ casos del corpus con filtros y ordenación |
| `/casos/:id` | Detalle de caso con métricas, charts de trayectorias, README, docs |
| `/capitulos` | Lista de capítulos por carpeta |
| `/capitulos/:slug` | Detalle de capítulo con sidebar de docs y TOC |
| `/bibliografia` | Bibliografía consolidada con búsqueda |
| `/st` | Validación lógica ST con run button |
| `/about` | Autoría, marco institucional, recursos |

## Features

- **Dark/light mode** con `prefers-color-scheme` + persistencia
- **Command palette** (`⌘K` / `Ctrl+K`) con búsqueda fuzzy global
- **Modo lectura** para tesis y capítulos
- **TOC interactivo** con highlight de sección visible (IntersectionObserver)
- **Filtros y ordenación** en /casos (categoría, EDI, p-value)
- **Charts interactivos** con Recharts (responsive, tooltips, leyendas)
- **Markdown académico** con KaTeX, mermaid, syntax highlighting
- **Responsive design** mobile-first

## Build

```bash
cd web_react
npm install
npm run build      # genera dist/
npm run dev        # servidor de desarrollo (puerto 5173) con proxy a FastAPI :8080
```

## Servir

El backend FastAPI (`web_tesis/app.py`) detecta automáticamente `web_react/dist/`
y lo sirve cuando existe. Si no existe, muestra una página informativa con la
instrucción de build. Las rutas SPA (cualquier ruta no `/api/*`) se redirigen a
`index.html` para que React Router maneje la navegación.

```bash
# desde la raíz del repo
python3 -m web_tesis.app --port 8080
```

## API consumida

Todas bajo `/api/*` y devuelven JSON:

- `GET /api/summary` — KPIs y distribución
- `GET /api/cases` — listado compacto
- `GET /api/casos/:id` — detalle con report+arrays
- `GET /api/chapters` — listado
- `GET /api/chapters/:slug` — detalle con docs renderizados
- `GET /api/thesis` — manuscrito ensamblado
- `POST /api/run-st` — ejecuta suite ST

## Despliegue Vercel

`vercel.json` rutea todo a `api/index.py` (FastAPI ASGI). Como el build de
Vite es estático, basta con commitear `dist/` para que el FastAPI serverless
lo sirva. Alternativa más limpia: configurar build hook de Vite en Vercel
(no implementado).
