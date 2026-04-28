# Protocolo de simulación — 31_decoherencia_cuantica

## Sonda Lindblad para decoherencia transmón

**Régimen físico:** Qubit superconductor + baño térmico.

## Ecuación de la sonda

```
dρ/dt = -i[H,ρ] + Σ L_k ρ L_k† - 1/2{L_k†L_k, ρ}
```

## Motivación física

Master equation de Lindblad para sistemas cuánticos abiertos.

## Origen de parámetros

Parámetros transmón NIST/IBM (Krantz et al. 2019).

## Citas disciplinares

- Lindblad, G. (1976). *Commun. Math. Phys.* 48(2).

## Lectura cruzada

- `31_decoherencia_cuantica/data/FETCH_MANIFEST.json` — trazabilidad de datos
- `31_decoherencia_cuantica/SETUP_HASH.json` — pre-registro criptográfico
- `31_decoherencia_cuantica/outputs/metrics.json` — outputs canónicos
- `31_decoherencia_cuantica/outputs/metrics_enriched_v5_2.json` — calibración avanzada V5.2/5.3
