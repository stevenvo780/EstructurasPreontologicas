# Protocolo de simulación — 30_caso_behavioral_dynamics

## Sonda Fajen-Warren (caso ancla canónico)

**Régimen físico:** Caso ancla. Sistema acoplado organismo-tarea con datos sintéticos derivados del modelo.

## Ecuación de la sonda

```
φ̈ = -b*φ̇ - k_g*(φ-ψ_g)*(e^{-c1·d_g}+c2) + k_o*(φ-ψ_o)*e^{-c3|φ-ψ_o|}*e^{-c4·d_o}
```

## Motivación física

Behavioral dynamics segundo orden (Warren 2006, Fajen-Warren 2003).

## Origen de parámetros

Sintético del sistema completo Fajen-Warren.

## Citas disciplinares

- Warren, W. H. (2006). *Psychol. Rev.* 113(2).
- Fajen, B. R. y Warren, W. H. (2003). *J. Exp. Psychol. HPP* 29(2).

## Limitaciones declaradas

N2 detectó circularidad. Confirmado marginal por V5.2 (p_block=0.978). Piloto metodológico.

## Lectura cruzada

- `30_caso_behavioral_dynamics/data/FETCH_MANIFEST.json` — trazabilidad de datos
- `30_caso_behavioral_dynamics/SETUP_HASH.json` — pre-registro criptográfico
- `30_caso_behavioral_dynamics/outputs/metrics.json` — outputs canónicos
- `30_caso_behavioral_dynamics/outputs/metrics_enriched_v5_2.json` — calibración avanzada V5.2/5.3
