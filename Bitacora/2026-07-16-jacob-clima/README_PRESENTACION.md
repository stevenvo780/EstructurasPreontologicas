# De la idea a la acción — trazabilidad, inteligibilidad y IHO del corpus

_Paquete de presentabilidad para las dos tesis (precursora **hiperobjetos** → **estructuras
pre-ontológicas** aplicadas al cambio climático). Generado 2026-07-16._

**Propósito invisible del proyecto:** que este conocimiento filosófico sea usable para la
**toma de decisiones y la organización política**. Por eso cada caso no se queda en su
estadística: se vuelve (1) **trazable** (de dónde salió el dato), (2) **inteligible**
(qué afirma la tesis, visto), y (3) **accionable** (dónde intervenir).

## 1. Trazabilidad de datos — `TRAZABILIDAD_LEDGER.{md,json}`
Auditoría determinista de los **42 casos** del corpus EDI (8 sub-sondas/plantillas excluidas).
Clasificación honesta de integridad del dato:

| Clase | N | Qué significa |
|---|---|---|
| 🟢 REAL verificado | 26 | fuente real declarada, sin fallback sintético |
| 🟡 REAL con fallback | 3 | se declara real pero la fuente admite proxy/timeout/offline → **resolver** |
| 🟠 SINTÉTICO declarado | 12 | dato sintético-realista (incluye los 5 controles de falsación y los 10 inter-escala) |
| ⚪ Indeterminado | 1 | provenance incompleta |

**Huecos priorizados (remediación = "de la idea a la acción" aplicada al propio corpus):**
1. **REAL con fallback (3):** `04_energia`, `20_kessler`, `25_acuiferos` — la `source` admite
   proxy/fallback. Reclasificar o reemplazar por fetch real.
2. **SHA256 = "tbd" (8):** `01_clima, 04_energia, 12_paradigmas, 19_acidificacion, 20_kessler,
   23_erosion, 41_wolfram, 42_histeresis` — integridad no verificable hasta llenar el hash.
3. **Clima sintético pese a LoE 5 (1):** `01_clima` cayó a sintético por timeout SSL de OWID.
   Es el **mejor lugar para pasar a dato real** (IPCC AR6 / CMIP6): máxima credibilidad.
4. **Sin comando de reproducción en el manifest (41):** el pipeline `./tesis` reproduce, pero
   el manifest no registra el comando por caso → estandarizar el campo `reproducibility`.
5. **Sin fase real (12):** los 10 inter-escala + `41,42` corren solo en sintético (deuda ya declarada).

## 2. Inteligibilidad gráfica por caso — `figs/` (`INDEX.md` + `CONTACT_SHEET.png`)
Una **figura-firma** por caso que hace VISIBLE lo que la tesis afirma, no solo la estadística:
- **Panel izquierdo — Intervención EDI:** observado vs modelo **acoplado** vs modelo **ablado**
  `do(coupling=0)`. El **gap** sombreado = la degradación predictiva al apagar el acoplamiento
  = el **cierre operativo, visto**. (Deforestación: gap ancho, EDI 0.580, gate ✓.)
- **Panel derecho — Firma dinámica:** mapa de retorno `estado(t)→estado(t+1)` coloreado por
  tiempo = el **atractor**. (Clima: **recta perfecta** = señal forzada, sin atractor emergente.
  Deforestación: trayectoria curvada = estructura real.)
- **Badge de integridad** (real/real?fb/sintético, con marca de agua "SINTÉTICO" donde aplica),
  EDI±CI, gate, **fuente**, y una **Lectura para decisión** derivada del EDI medido (no inventada).

**Regla de lectura para decisión (idea→acción), derivada del cierre medido:**
- **Cierre fuerte + gate ✓** → hay retroalimentación interna real → una palanca sobre el
  **acoplamiento** (gobernanza, no solo compensación) puede torcer la trayectoria.
- **Nulo / tendencia** → señal forzada casi lineal a esa escala → intervenir sobre el
  **forzante exógeno**; la palanca "sistémica-emergente" no está justificada ahí.
- **Falsación** → control negativo: calibra la confianza de todo el corpus.

## 3. El hiperobjeto, mantenido como instrumento — IHO (`iho.py`, `01-IHO-instrumento.md`)
Morton no se descarta ni se reifica: el hiperobjeto se **mantiene** como **perfil medible de 5 ejes**
(V viscosidad, N no-localidad, T ondulación temporal, P retiro, I interobjetividad). Se reporta
como **vector, nunca un solo número**. El próximo paso (experimentos **V** multi-sonda y **N**
acoplamiento inter-estructura) cierra los dos ejes que faltaban → ver `STATUS_V_N.md`.

## Guardrail (rigor de la tesis, no lavar la deuda)
El p-value sigue **mal calibrado** (error tipo I empírico ≈24%, no 5%); los **umbrales EDI sí
robustos**. Composición de corpus post-hoc. Auditorías endógenas (falta peer-review externo).
La urgencia política **no** justifica inflar EDIs débiles: el `clima=tendencia` se presenta como
**fortaleza discriminativa** del aparato, no como fracaso.
