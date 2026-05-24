# Histórico: drenaje de referencias densas a `Bitacora/` del cuerpo argumental

**Fecha:** 2026-05-24
**Objetivo:** reducir 79 menciones de `Bitacora/` en cuerpo manuscrito a ≤10 (solo metodológicamente esenciales).
**Motivo:** infraestructura interna no debe filtrarse a lector externo (Ricardo, tribunal).

## Inventario inicial

79 referencias detectadas vía:
```
grep -rn "Bitacora/" 00-* 01-* 02-* 03-* 04-* 05-* 06-* --include="*.md" | grep -v "/historico-"
```

## Política aplicada

1. **CONSERVAR (referencia esencial):**
   - Pre-registros de adversarial serios atendidos (`2026-05-16-adversarial-irrealismo-operativo/`).
   - `auditoria-cobertura-B-T2.md` como evidencia de cobertura.
   - Programa multi-sonda extendido (`2026-04-28-cierre-doctoral/`) cuando ancla deuda futura específica.
   - Re-ejecución de caso 19 con re-clasificación documentada.
   - Procedencia metodológica del loop-nocturno (nota global única).

2. **REFORMULAR (drenar sufijo "Origen: `Bitacora/...`"):**
   - Entradas de deuda residual `[F##-## YYYY-MM-DD] ... Origen: Bitacora/...` mantienen el código F## (es trazable internamente) pero eliminan la ruta concreta al archivo de origen — el código F## ya es identificador único.

3. **ELIMINAR:**
   - Referencias decorativas a carpetas (`la carpeta Bitacora/` documenta...).
   - Referencias trazabilidad genérica ("trazabilidad histórica del proyecto").
   - "Origen: Bitacora/..." en entradas que ya viven en el cuerpo del manuscrito (la entrada queda; sólo se omite la ruta).
   - "Paralela en ... Origen: Bitacora/..." cuando la trazabilidad cruzada interna ya es suficiente.

## Detalle por archivo

Ver inventario completo abajo y `historico-drenaje-bitacora-refs-inventario.txt` adjunto.

## Resultado esperado

- Antes: 79 menciones.
- Después objetivo: ≤10 metodológicamente esenciales.
- Trazabilidad interna del proyecto (códigos F##, TENG-##, AU-##) preservada: las bitácoras siguen siendo el archivo histórico, sólo dejan de aparecer rutas en el cuerpo manuscrito.
