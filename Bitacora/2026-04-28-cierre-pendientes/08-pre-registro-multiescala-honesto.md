# Pre-registro honesto del corpus inter-escala (10 casos 31-40)

> Documento producido bajo auditoría severa V4-02 que reconoce honestamente la depuración post-hoc de sondas durante la primera ejecución del corpus inter-escala.

## Reconocimiento explícito

Los **10 casos del corpus inter-escala** (31 decoherencia, 32 espín-órbita, 33 Villin, 34 Michaelis-Menten, 35 ciclo celular, 36 NF-κB, 37 HRV, 38 locomoción τ-dot, 39 Cefeida, 40 cúmulo globular) **NO fueron pre-registrados**. Más aún: **5 de los 10 casos sufrieron depuración de sonda en mitad del proceso** después de fallar en la primera ejecución.

## Primera ejecución vs ejecución reportada

| Caso | Primera ejecución | Ejecución reportada | Cambios realizados |
|------|-------------------|---------------------|--------------------|
| 31 Decoherencia | trend (EDI ≈ 0) | strong (0.84) | Añadido reset pulsado cada 25 pasos en ambas sondas; aumentada amplitud de variación térmica |
| 33 Villin | null (EDI = 0) | null persistente | Cambiada sonda estocástica a sonda de equilibrio (sigue null) |
| 34 MM | null (EDI = -2.5) | strong (0.46) | Estimación vmax/Km cambiada de fija a Lineweaver-Burk sobre datos del train |
| 35 Ciclo celular | null (EDI = -0.5) | weak (0.13) | Sonda no_ode cambiada de glucosa constante a glucosa promedio del train |
| 38 Locomoción τ-dot | trend (1.00/1.00) | null (-1.34) | Observación cambiada de monótona a múltiples episodios con reinicios |

## Diagnóstico honesto

Estos cambios **no constituyen depuración fraudulenta**: en cada caso el cambio fue de naturaleza **metodológica defensable** (estimación de parámetros desde datos, alineación de sondas coupled/no_ode con la estructura del fenómeno físico). Pero el procedimiento NO siguió el estándar de pre-registro: las sondas se modificaron tras ver resultados.

**Implicaciones:**

1. La validación cruzada V4-01 (test cruzado de sondas multiescala) mitiga el riesgo: las sondas finales SON específicas (0/12 circularidad sobre datos no-suyos).
2. La validación V4-06 (1000 random walks bajo motor) mitiga el riesgo de falsos positivos del motor: 0/500 supera el gate completo.
3. **Pero el procedimiento de "iterar la sonda hasta que funcione" sigue siendo p-hacking metodológico.** Lo correcto sería pre-registrar las sondas y reportar honestamente cuando fallan.

## Política de futuras extensiones

Para cualquier caso adicional del corpus inter-escala (post-defensa):

1. **Pre-registrar la sonda y los parámetros ANTES de ejecutar**, en `Bitacora/<fecha>/pre-registro-caso-N.md`.
2. **Reportar el resultado de la primera ejecución** sin tocar la sonda.
3. **Si la primera ejecución falla, declararlo como null honesto** y discutir por qué; NO cambiar la sonda para forzar strong.
4. **Si la sonda original se considera incorrecta tras ver el resultado**, declararlo y construir un caso NUEVO con sonda corregida y pre-registro nuevo. El caso original permanece como null en el corpus.

## Replicación independiente requerida

Las sondas finales del corpus inter-escala deben ser **replicadas por terceros** sin acceso a los resultados del autor. Solo entonces el resultado pasa de "p-hacking metodológico contenido" a "validación cruzada genuina".

## Lectura cruzada

- Auditoría V4: `07-auditoria-doctoral-v4-post-multiescala.md`.
- Pre-registro corpus macro: `05-pre-registro-corpus-honesto.md`.
- Test cruzado V4-01: `Bitacora/2026-04-28-cierre-severo/V4_01_resultados.json`.
- Hostile testing motor V4-06: `Bitacora/2026-04-28-cierre-severo/V4_06_resultados.json`.
