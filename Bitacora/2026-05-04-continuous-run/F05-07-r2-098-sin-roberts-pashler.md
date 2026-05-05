# F05-07 — r²=0.98 Fajen-Warren / Yilmaz-Warren reportado sin crítica Roberts-Pashler 2000

Fecha: 2026-05-05
Capítulo: `05-aplicaciones/05-dinamica-conductual-reconstruccion-warren.md`
Status: **needs_human** (requiere firma de Jacob para reescritura sustantiva + verificación de paginación)

## (a) Verificación de la afirmación

### Lo que dice el manuscrito hoy

- L163: «Yilmaz y Warren (1995) midieron cuatro mil ochocientos ensayos en doce participantes y encontraron exactamente esa relación: la regresión del cambio de fuerza de frenado contra `τ̇` cruza el cero en `τ̇ = −0.52`, con pendiente `−1.04` y `r² = 0.98` (fig. 6 del paper).»
- L188: «con `b = 3.25`, `k_g = 7.50`, `c1 = 0.40`, `c2 = 0.40`, `k_o = 198.0`, `c3 = 6.5`, `c4 = 0.8`. Las simulaciones reproducen 0.980 de la varianza de los caminos humanos para meta sola y 0.975 para meta con obstáculo.»

### El problema (hallazgo del adversarial-reviewer)

Ambos r² ≥ 0.975 se reportan como evidencia fuerte del marco, pero:

1. **Fajen & Warren 2003** ajusta **7 parámetros libres** (`b, k_g, c1, c2, k_o, c3, c4`) a las trayectorias humanas. La razón k/N (parámetros / trayectorias-test independientes) no se reporta en el manuscrito.
2. **No se declara cross-validation**: no consta si el r²=0.98 es in-sample (los mismos datos a los que se ajustó) o sobre un hold-out independiente. La lectura natural es in-sample.
3. **Roberts & Pashler 2000** ("How persuasive is a good fit? A comment on theory testing", *Psychological Review* 107(2): 358-367) demostraron que un buen ajuste es débil como evidencia salvo que se controle (i) la flexibilidad del modelo, (ii) la variabilidad de los datos, y (iii) qué alternativas quedan descartadas. Un r² alto con muchos parámetros y sin restricción a priori del rango de comportamientos posibles es compatible con prácticamente cualquier resultado y por tanto no discrimina teorías.

Citar r²=0.98 sin esta cualificación **infla la fuerza inferencial** del caso Warren, contradiciendo CLAUDE.md §1 (no celebrar antes de tiempo) y §6 (no maquillar potencia, no usar baselines de paja).

### Verificación de paginación de Roberts-Pashler 2000

**No verificada localmente**. El PDF de Roberts & Pashler 2000 no está en `07-bibliografia/` (búsqueda `grep -i roberts|pashler` vacía). La referencia bibliográfica estándar es:

> Roberts, S. & Pashler, H. (2000). How persuasive is a good fit? A comment on theory testing. *Psychological Review*, 107(2), 358–367. doi:10.1037/0033-295X.107.2.358

El argumento central — que el ajuste por sí solo no es evidencia, hay que conocer qué *no* podría haber predicho el modelo — está en la primera página del artículo (p. 358) y se desarrolla en pp. 359-361. La cita pedida en el acceptance ("p. 360") es plausible para la formulación canónica del argumento sobre flexibilidad excesiva, pero **no la puedo confirmar textualmente sin el PDF**. Se requiere que `@bibliography-fetcher` traiga el PDF o que Jacob/Steven verifiquen la paginación exacta antes de fijar la cita.

## (b) Propuesta de edición concreta

Insertar una subsección entre L188 y L190 (antes de "### Atractores, repulsores, bifurcaciones") y un comentario paralelo entre L163 y L165:

### Borrador L188+ (caso Fajen-Warren 2003)

```markdown
### Crítica Roberts-Pashler 2000 (costo argumental declarado)

El modelo de Fajen y Warren (2003) ajusta **siete parámetros libres** (`b, k_g, c1,
c2, k_o, c3, c4`) a las trayectorias humanas. El r² ≈ 0.98 reportado es **in-sample**
sobre el conjunto de ajuste; no se reporta cross-validation con un hold-out independiente.
Roberts y Pashler (2000) mostraron que un buen ajuste, por sí solo, es evidencia débil
de un modelo: hay que saber además (i) qué resultados habría podido predecir el modelo
con otros valores plausibles de sus parámetros, (ii) cuán variables son los datos y
(iii) qué alternativas teóricas quedaron descartadas. Aplicado aquí: con siete parámetros
libres ajustados a posteriori, el r² alto demuestra que la familia de leyes de control
acopladas *contiene* la conducta observada, no que la *prediga*. La fuerza inferencial
correcta es por tanto: el caso Warren es **consistente** con el marco, no lo *confirma*
discriminantemente. La discriminación viene de las predicciones cualitativas (bifurcación
tangente al variar geometría obstáculo-meta) y de los contrastes contra hipótesis rivales
(excentricidad fija, deriva), no del r² numérico.
```

### Borrador L163+ (caso Yilmaz-Warren 1995)

```markdown
> El r² = 0.98 corresponde a la regresión lineal sobre datos agregados de doce
> participantes y es in-sample. La fuerza inferencial del dato no es la magnitud
> de r² sino la convergencia del cruce por cero en τ̇ ≈ −0.5 a través de participantes,
> que es predicción cualitativa específica del marco τ-acoplado y no de hipótesis
> rivales (frenado por velocidad o por distancia). Cf. Roberts y Pashler (2000)
> sobre los límites del ajuste como evidencia.
```

### Tabla 5.5.1 (L218): añadir fila

```markdown
| Costo argumental: r² in-sample con 7 parámetros libres | — | Declarado como consistencia, no como confirmación | Cita Roberts-Pashler 2000 |
```

## (c) Costo argumental declarado

Esta corrección **debilita** la lectura aparente del caso Warren (no demuestra el marco, solo es consistente con él) pero **fortalece** la defensibilidad: cierra una objeción metodológica estándar que cualquier lector con formación en philosophy of modeling levantaría. La discriminación real del caso queda en las predicciones cualitativas (bifurcaciones, atractores/repulsores asimétricos), que son lo que el marco dice que debe pasar y lo que las alternativas no predicen — no en el número r².

## Acción humana requerida (needs_human)

1. **Jacob:** firmar la reescritura sustantiva (cambia el peso epistémico del caso Warren — decisión filosófica, no técnica).
2. **Bibliografía:** descargar Roberts & Pashler 2000 a `07-bibliografia/` y verificar paginación exacta del argumento sobre flexibilidad de modelo (p. 360 ± 1) antes de cerrar la cita. Invocar `/fetch-biblio` o `@bibliography-fetcher`.
3. **Opcional (Steven):** revisar Fajen & Warren 2003 (Journal of Experimental Psychology: Human Perception and Performance 29(2): 343-362) y reportar si los autores declararon cross-validation o si todo el r² es in-sample. Si hay hold-out, suavizar la crítica; si no, mantenerla como aquí.

## Marca de tarea

`needs_human` — H-J* (firma filosófica de Jacob) + B-T* (verificación de paginación bibliográfica).

RESULT: complete | F05-07-r2-098-sin-roberts-pashler | reporte con borrador de edición; needs_human Jacob+biblio
