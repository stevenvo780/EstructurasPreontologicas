# Sondas teóricamente independientes — reporte V5.1

Bloque científico B4. Verificación operativa del criterio C1 de κ-ontológica fuerte (cap 02-01 §criterios) sobre 3 casos strong del corpus inter-dominio.

## Síntesis

- **Casos evaluados:** 3
- **Casos que cumplen C1 (convergencia |Δ EDI| ≤ 0.05 con ambos EDI > 0.10):** 0

## Tabla por caso

| Caso | Primaria | Secundaria | EDI primaria | EDI secundaria | \|Δ\| | Convergen | C1 |
|------|----------|------------|--------------|----------------|--------|-----------|----|
| 04_caso_energia | Lotka-Volterra ecológico | maxwell_boltzmann_energy_probe | +0.650 | -0.736 | 1.386 | ✗ | ✗ |
| 16_caso_deforestacion | von Thünen económico-espacial | fisher_kpp_deforestation_probe | +0.600 | +0.861 | 0.261 | ✗ | ✗ |
| 27_caso_riesgo_biologico | SIR epidemiológico | zeeman_catastrophe_biorisk_probe | +0.330 | +0.706 | 0.376 | ✗ | ✗ |

## Notas operativas

Las predicciones primarias se reconstruyen desde EDI publicado, no desde arrays primarios versionados. La validación definitiva requiere que cada caso emita en outputs/ los arrays obs, abm, reduced y forcing individualmente. Esto está en deuda L17.

## Lectura cruzada

- Cap 02-01 §Nota sobre κ — distinción κ-pragmática vs κ-ontológica con tres criterios.
- Anexo A.0 limitación L11 — κ-ontológica fuerte como deuda; este reporte cierra parcialmente.
- `09-simulaciones-edi/common/independent_probes.py` — sondas implementadas.
