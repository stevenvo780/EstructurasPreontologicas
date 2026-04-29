# Figuras

Versiones vectoriales y rasterizadas de las figuras del manuscrito. Las fuentes están en los anexos correspondientes; este directorio contiene **artefactos generados** y se regenera con scripts del repo.

## Estructura

```
figures/
├── corpus/              # F33 — visualización del corpus EDI
│   ├── corpus_edi_bars.{png,svg}            barras EDI con CI 95% (32 casos macro)
│   ├── corpus_multiescala_scatter.{png,svg} escala espacial vs temporal (10 casos)
│   ├── corpus_qes_distribution.{png,svg}    histograma QES + curva acumulada
│   ├── corpus_domain_heatmap.{png,svg}      dominio × banda EDI
│   └── corpus_summary_table.csv             tabla maestra (42 casos)
│
├── mermaid_src/         # fuente .mmd extraída de Anexos/A10
├── mermaid_svg/         # SVG vectorial pre-depósito
└── mermaid_png/         # PNG 1600×1200 para exportes pesados
```

## Regeneración

```bash
# corpus (requiere venv con matplotlib, pandas, numpy)
09-simulaciones-edi/.venv/bin/python scripts/visualize_corpus.py

# mermaid (requiere node, npx, chrome/puppeteer)
scripts/render_mermaid.sh
```

## Convenciones

- **SVG es la fuente preferente** para depósito; PNG se entrega como respaldo.
- **DPI:** 150 para PNG generados con matplotlib; 1600×1200 px para PNG generados desde Mermaid.
- **Numeración:** `figura_<NN>` corresponde al orden en `Anexos/A10` (no al número de figura del manuscrito, que sigue el esquema `Figura A.10.K`).

## Trazabilidad

| Salida | Generador | Fuente de datos |
|--------|-----------|-----------------|
| `corpus/*.png/svg/csv` | `scripts/visualize_corpus.py` | `09-simulaciones-edi/<caso>/outputs/metrics.json` + `QES_AUDIT_REPORT.json` |
| `mermaid_*/figura_NN.*` | `scripts/render_mermaid.sh` | `Anexos/A10-figuras-mermaid.md` |
