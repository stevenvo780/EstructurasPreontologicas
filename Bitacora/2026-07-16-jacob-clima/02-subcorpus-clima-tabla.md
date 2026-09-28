# Sub-corpus CLIMA - tabla de cierre operativo (metrics.json vivo, 2026-07-16)

Fuente de verdad: 09-simulaciones-edi/<caso>/outputs/metrics.json, fase 'real', campo edi.value.
Reproducible: `./tesis run --case <caso>`. (git dirty al momento de leer; re-correr antes de publicar.)

| Caso | Rol | EDI | signif. | pasa gate | Estatus |
|------|-----|-----|---------|-----------|---------|
| 01_clima | AGREGADO (hiperobjeto) | +0.269 | No (p=1.0) | No | Se retira: no admitido |
| 16_deforestacion | subestructura | +0.580 | Si | **Si** | Strong |
| 21_salinizacion | subestructura | +0.515 | Si | **Si** | Strong |
| 18_urbanizacion | subestructura | +0.337 | Si | **Si** | Strong |
| 22_fosforo | subestructura | +0.322 | Si | **Si** | Strong |
| 17_oceanos | subestructura | +0.190 | Si | No | Significativo, sin gate |
| 04_energia | subestructura (adyacente) | +0.157 | Si | No | Significativo, sin gate |
| 25_acuiferos | subestructura | +0.004 | No | No | Null |
| 19_acidificacion_oceanica | subestructura | -0.005 | No | No | Null (revisar como falsif. local, H-J12) |
| 03_contaminacion | subestructura | -0.011 | No | No | Null |

**Lectura:** dentro de un mismo "cambio climatico", el cierre operativo va de strong (deforestacion,
salinizacion, urbanizacion, fosforo) a significativo-sin-gate (oceanos, energia) a null (acuiferos,
acidificacion, contaminacion), y el AGREGADO no se admite. "Cambio climatico" no es un hiperobjeto
unico y viscoso: es una malla multiescala de estructuras pre-ontologicas con cierre heterogeneo y medible.
El Uno de Morton se disuelve en una pluralidad medida -> anti-reificacion vuelta empirica.

**Nota de rigor:** estos valores DIFIEREN de la bitacora 2026-04-27 (corrida vieja: clima 0.011,
microplasticos 0.78). El JSON gana sobre la prosa (regla del repo). Microplasticos (24) colapso a -1.0
en la corrida vigente -> excluido del nucleo strong; su inestabilidad es deuda de reproducibilidad
(condicion de fracaso #16.2 de la tesis-fuente).
