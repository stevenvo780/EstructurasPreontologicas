# Apéndice técnico 3. Figuras Mermaid

Diagramas formales del manuscrito en formato Mermaid (renderable directamente por GitHub, GitLab, Pandoc + filtros, y la mayoría de visores Markdown). Reemplaza los diagramas ASCII art que aparecen en el cuerpo de los capítulos.

**Versiones vectoriales pre-depósito (generadas por `@mermaid-js/mermaid-cli`):**

- SVG: `figures/mermaid_svg/figura_<NN>.svg`
- PNG (1600×1200): `figures/mermaid_png/figura_<NN>.png`
- Fuente `.mmd` extraída automáticamente: `figures/mermaid_src/figura_<NN>.mmd`

La numeración `<NN>` (01-09) corresponde al orden de aparición en este apéndice (`Figura T.3.1` → `figura_01.svg`, etc.). La regeneración es reproducible con `scripts/render_mermaid.sh`.

---

## Fig. 2.2. Acoplamiento dinámico organismo-entorno-tarea-historia (capítulo 02-04)

**Figura A.10.1.**

```mermaid
graph LR
    H[Historia] --> A[Agente / Organismo]
    T[Tarea] --> A
    A -->|β: fuerza| E[Entorno]
    E -->|λ: información ecológica| A
    A -->|ȧ = Ψ a,i| A
    E -->|ė = Φ e,F| E
    style A fill:#cdf
    style E fill:#fdc
    style T fill:#dfc
    style H fill:#fcd
```

---

## Fig. 3.1. Mapa de operadores formales (capítulo 03-01)

**Figura A.10.2.**

```mermaid
graph TD
    R[Realidad R] -->|μ: medir| X[Variables X]
    X -->|construir grafo| G[Grafo basal G = V,E,W,T]
    G -->|relaciones n-arias| H[Hipergrafo H]
    G -->|comprimir| K[κ: G → G*]
    H -->|comprimir| K
    K -->|errores de traducción| Eps[ε: G ↔ G*]
    K -->|admitir| S[Semántica revisada S]
    Eps -->|reabrir si| K
    style R fill:#fee
    style X fill:#efe
    style G fill:#eef
    style H fill:#eff
    style K fill:#fef
    style Eps fill:#ffe
    style S fill:#cfc
```

---

## Fig. 3.2. Dossier de anclaje (14 componentes — capítulo 03-02)

**Figura A.10.3.**

```mermaid
graph TD
    Q[1 Pregunta Q fechada] --> V[2 Variables operacionalizadas]
    V --> Sus[3 Sustrato instanciante]
    Sus --> Gr[4 Grafo G construido]
    Gr --> Hi[5 Hipergrafo H si procede]
    Hi --> Kp[6 Compresión κ]
    Kp --> At[7 Atractores identificados]
    At --> Pv[8 Pruebas de validación]
    Pv --> Pred[9 Predicción discriminante]
    Pred --> Iv[10 Intervención discriminante]
    Iv --> Eps[11 Operador ε]
    Eps --> Tr[12 Traducción B↔L3]
    Tr --> Lim[13 Limitaciones]
    Lim --> Rv[14 Comparación rival]
```

---

## Fig. 3.3. Pipeline EDI (capítulo 03-04)

**Figura A.10.4.**

```mermaid
graph LR
    D[Datos] --> ABM[Simulación ABM N=200, 50x50]
    D --> ODE_p[Sonda ODE primaria]
    ABM -->|coupled| RC[RMSE coupled]
    ABM -->|sin ODE| RnO[RMSE no_ode]
    ODE_p --> ABM
    RC --> EDI[EDI = 1 - RC/RnO]
    RnO --> EDI
    EDI --> Pe[Permutación 999]
    EDI --> Bo[Bootstrap 500]
    Pe --> Pv[p-value]
    Bo --> CI[CI 95%]
    EDI --> C[Protocolo C1-C5]
    C --> OP[overall_pass]
```

---

## Fig. 5.1. Asimetría L1↔B↔L3↔S como protocolo (capítulo 02-04)

**Figura A.10.5.**

```mermaid
graph LR
    L1[L1 psicológico ordinario<br>preguntas comunicables] -.indirecto.-> B[B conductual biológico<br>anclaje empírico]
    B -->|directo<br>traduccional| L3[L3 estructural relacional<br>formalización]
    L3 -->|consecuencias<br>observables| L1
    L3 -->|filtro empírico| S[S semántica revisada<br>categorías que sobreviven]
    B -->|atractores reales| S
    style L1 fill:#fcc
    style B fill:#cfc
    style L3 fill:#ccf
    style S fill:#fcf
```

---

## Fig. 6.1. Paisaje de emergencia del corpus (capítulo 06-01)

**Figura A.10.6.**

```mermaid
pie title Distribución del corpus EDI 30 casos
    "Strong gate (4)" : 4
    "Strong sin gate (1)" : 1
    "Weak (8)" : 8
    "Suggestive (2)" : 2
    "Trend (4)" : 4
    "Null (8)" : 8
    "Falsación rechazada (3)" : 3
```

---

## Fig. 9.1. Arquitectura del motor ABM+ODE (capítulo 09-00)

**Figura A.10.7.**

```mermaid
graph TD
    DC[case_config.json] --> CR[case_runner.py]
    Data[fetch_*.py por caso] --> CR
    CR --> ABM_C[abm_core CPU]
    CR --> ABM_G[abm_core_gpu CuPy/PyTorch]
    CR --> OM[ode_models.py 22 sondas]
    OM --> HV[hybrid_validator.py núcleo]
    ABM_C --> HV
    ABM_G --> HV
    HV --> Pp[permutation_test_edi]
    HV --> Bp[bootstrap_ci]
    HV --> Cp[protocolo C1-C5 + 8 cond]
    Pp --> Out[outputs/metrics.json]
    Bp --> Out
    Cp --> Out
```

---

## Fig. 9.31. Multi-sonda (capítulo 09-31)

**Figura A.10.8.**

```mermaid
graph LR
    A[Caso strong] -->|sonda primaria| EP[EDI primario]
    A -->|sonda alternativa<br>motivación distinta| EA[EDI alternativa]
    EP -->|comparar| D[Δ delta]
    EA --> D
    D -->|abs Δ ≤ 0.10| CF[Convergencia fuerte]
    D -->|0.10 menor abs Δ menor 0.20| CM[Convergencia moderada]
    D -->|abs Δ mayor 0.20| Dv[Divergencia]
```

---

## Fig. C.1. Esquema de convergencia EDI-Wolfram (capítulo 04-debates §14)

**Figura A.10.9.**

```mermaid
graph TD
    R[1 Selección regla<br>p.ej. CA Rule 110] --> S[2 Generar 200 simulaciones<br>con perturbaciones iniciales]
    S --> SM[3 Construir sonda macro<br>densidad / curvatura discreta]
    SM --> EE[4 Aplicar EDI<br>con perm 999 + boot 500 + C1-C5]
    EE --> H[5 Hipótesis<br>EDI ≥ 0.30 → cierre operativo macro<br>EDI menor 0.10 → irreducibilidad confirmada]
    H --> L[6 Lectura interpretativa]
```

---

## Trazabilidad

Las figuras están versionadas en este apéndice. Cualquier cambio se ejecuta aquí y se referencia desde el capítulo que las menciona. La conversión a SVG/PNG se ejecuta pre-depósito mediante:

```bash
mmdc -i 10-apendices-tecnicos/03-figuras-mermaid.md -o figures/mermaid_svg/  # mermaid-cli
```

o automáticamente por GitHub/Pandoc con filtros mermaid.
