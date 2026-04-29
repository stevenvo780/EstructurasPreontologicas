# Caso 21 — Salinización de Suelos (Richards-Solute)

## Propósito

Evaluar si la salinización de suelos a escala global exhibe propiedades de
estructura pre-ontológica: no-localidad (irrigación global redistribuye sales),
viscosidad temporal (acumulación irreversible a escalas humanas), y
causalidad descendente del «proceso de salinización» sobre parcelas locales.

---

## Modelos

### ODE — Transporte de Solutos Richards-Convección

$$\frac{dS}{dt} = \alpha(F - \beta S) + \gamma \cdot F \cdot S + \varepsilon$$

Modelo de balance salino: acumulación proporcional al forcing (irrigación),
lavado natural, y término bilineal (feedback evaporación×salinidad).

| Parámetro | Valor | Justificación |
|-----------|-------|---------------|
| $\alpha$ | 0.05 | Tasa de acumulación salina ~5%/año (Qadir et al. 2014, Nature Reviews) |
| $\beta$ | 0.015 | Tasa de lavado natural ~1.5%/año (Hillel 2000, Academic Press) |
| $\gamma$ | 0.02 | Feedback bilineal evaporación×salinidad (Rhoades et al. 1992: no-linealidad observada) |
| `ode_noise` | 0.015 | Variabilidad interanual |
| Clip S | [−10, 10] | Rango normalizado (espacio Z) |

### ABM — Grid con Gradiente Lineal (abm_core.py)

Celdas representan parcelas agrícolas. Gradiente de irrigación
río→secano (más sal cerca del drenaje pobre).

| Parámetro | Valor | Justificación |
|-----------|-------|---------------|
| `grid_size` | 25 | Grilla 25×25 = 625 parcelas |
| `forcing_gradient_type` | `"linear"` | Gradiente de irrigación río→desierto |
| `forcing_gradient_strength` | 0.55 | Moderado-alto (Tanji & Kielen 2002: distribución espacial) |
| `heterogeneity_strength` | 0.30 | Alta variabilidad edáfica, CV ~25-40% (Rhoades 1992) |
| `forcing_scale` | 0.10 | Sensibilidad ABM a driver externo |
| `macro_coupling` | 0.35 | Acoplamiento macro→micro moderado-alto |
| `base_noise` | 0.002 | Ruido bajo (proceso lento) |

**Forcing sintético:**
$$F(t) = 0.008\,t + 0.0003\,t^{1.2}$$
- Lineal: ~0.8%/año de expansión de irrigación global (FAO 2021)
- Super-lineal: retroalimentación irrigación→salinización→abandono→presión

### Datos reales

World Bank API: indicador `AG.LND.IRIG.AG.ZS` (% tierra irrigada), 1961–2022.
Cache local: `data/wb_arable_land.csv`.

---

## Resultado

| Fase | EDI | Interpretación |
|------|-----|----------------|
| Sintética | 0.505 | **Acoplamiento macro significativo** |
| Real | −1.378 | Sin estructura macro en datos reales |

## Correcciones

- `random.seed()` y `random.gauss()` reemplazados por `np.random.default_rng(seed)` y `rng.normal()` en `ode.py`
- `metrics.py` eliminado (código muerto)
- Todos los números mágicos documentados con referencias

## Referencias

- Hillel, D. (2000). *Salinity Management for Sustainable Irrigation*. The World Bank.
- Qadir, M. et al. (2014). Economics of salt-induced land degradation. *Natural Resources Forum*, 38(4), 282–295.
- Rhoades, J. D. et al. (1992). *The Use of Saline Waters for Crop Production*. FAO Irrigation & Drainage Paper 48.
- Tanji, K. K. & Kielen, N. C. (2002). *Agricultural Drainage Water Management*. FAO Irrigation & Drainage Paper 61.
- Richards, L. A. (1931). Capillary conduction through porous mediums. *Physics*, 1(5), 318–333.
