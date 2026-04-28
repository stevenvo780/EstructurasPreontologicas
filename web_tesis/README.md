# web_tesis — UI de visualización de la tesis

Capa web FastAPI + Jinja2 para navegar la tesis *Estructuras Pre-Ontológicas*
(realismo irrealista operativo + validación EDI multidominio).

Replica la UI de `TesisJacobContenidos` adaptada a este repositorio.

## Qué muestra

- **Inicio (`/`)**: render completo de `TesisFinal/Tesis.md` con índice navegable,
  tablero de KPIs (overall_pass, EDI promedio, etc.), gráficas del corpus EDI
  (niveles de cierre, histograma EDI, dispersión EDI vs CR, mapa de calor de criterios)
  y tarjetas de los 30 casos.
- **Capítulo (`/capitulos/<slug>`)**: docs renderizados de cada carpeta `00-…` a `08-…`.
- **Caso (`/casos/<id>`)**: panel analítico por fase real/sintético, compuertas
  C1-C5+, errores RMSE, calibración, taxonomía y reporte narrativo.
- **API JSON**: `/api/summary`, `/api/casos/<id>`, `/healthz`.

## Cómo ejecutar

```bash
# Desde la raíz del repo
python -m venv .venv-web
source .venv-web/bin/activate
pip install -r web_tesis/requirements.txt

# Servidor de desarrollo (puerto 8080)
python -m web_tesis.app --reload
# o:
uvicorn web_tesis.app:app --reload --port 8080
```

Navegar a <http://127.0.0.1:8080/>.

Para forzar relectura del disco sin reiniciar: `?refresh=1` en la URL.

## Fuentes de datos

| Ruta                                      | Uso                                             |
|-------------------------------------------|-------------------------------------------------|
| `TesisFinal/Tesis.md`                     | Documento principal renderizado en `/`          |
| `09-simulaciones-edi/*_caso_*/outputs/metrics.json` | Métricas EDI/C1-C5/symploke por caso  |
| `09-simulaciones-edi/*_caso_*/outputs/report.md`    | Reporte narrativo por caso            |
| `09-simulaciones-edi/*_caso_*/README.md`            | README del caso                       |
| `09-simulaciones-edi/*_caso_*/docs/*.md`            | Docs adversariales/metodológicos      |
| `00-…` … `08-…`                                     | Capítulos (markdown por carpeta)      |

`visualizations/` se monta automáticamente si existe (PNGs de heatmap/métricas).
