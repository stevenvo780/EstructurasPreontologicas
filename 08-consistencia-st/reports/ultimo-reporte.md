# Reporte de consistencia ST

## theories/00-nucleo-ontologico.st

- modo: `check`
- estado: ✅ ok
- código de salida: `0`

### stdout

```text
✓ /datos/repos/EstructurasPreontologicas/08-consistencia-st/theories/00-nucleo-ontologico.st: sin errores
```

## theories/01-criterios-legitimidad.st

- modo: `check`
- estado: ✅ ok
- código de salida: `0`

### stdout

```text
✓ /datos/repos/EstructurasPreontologicas/08-consistencia-st/theories/01-criterios-legitimidad.st: sin errores
```

## theories/02-debates-y-limites.st

- modo: `check`
- estado: ✅ ok
- código de salida: `0`

### stdout

```text
✓ /datos/repos/EstructurasPreontologicas/08-consistencia-st/theories/02-debates-y-limites.st: sin errores
```

## theories/03-text-layer-tesis.st

- modo: `run`
- estado: ✅ ok
- código de salida: `0`

### stdout

```text
Perfil logico: classical.propositional
Passage p_formulacion = [[../Bitacora/2026-04-27-integracion-jacob/00-tesis-fuente-original.md#1-formulacion-central]]
Formalizacion f_formulacion: p_formulacion -> (M & C & R & L)
Claim c_formulacion registrado
Support: c_formulacion <- p_formulacion
Confidence: c_formulacion = 0.98
Context: c_formulacion = "Núcleo de la formulación central: materialidad, compresión, no reificación y niveles no separados"
Passage p_criterios = [[../03-formalizacion/02-criterios-de-legitimidad-y-metodo.md#los-diez-criterios-de-legitimidad]]
Formalizacion f_criterios: p_criterios -> (A & B & F & I & V & T & U & O & N)
Claim c_criterios registrado
Support: c_criterios <- p_criterios
Confidence: c_criterios = 0.95
Context: c_criterios = "Matriz mínima de legitimidad epistemológica"
Passage p_principio = [[../Bitacora/2026-04-27-integracion-jacob/00-tesis-fuente-original.md#44-la-tesis-como-principio-general]]
Formalizacion f_principio: p_principio -> (M & C & R)
Claim c_principio registrado
Support: c_principio <- p_principio
Confidence: c_principio = 0.94
Context: c_principio = "Principio de realidad relacional comprimible"
── Render: claims (markdown) ──
  Claim "c_formulacion": (M ∧ C ∧ R ∧ L)
    Soporte: p_formulacion
    Confianza: 0.98
    Contexto: Núcleo de la formulación central: materialidad, compresión, no reificación y niveles no separados
  Claim "c_criterios": (A ∧ B ∧ F ∧ I ∧ V ∧ T ∧ U ∧ O ∧ N)
    Soporte: p_criterios
    Confianza: 0.95
    Contexto: Matriz mínima de legitimidad epistemológica
  Claim "c_principio": (M ∧ C ∧ R)
    Soporte: p_principio
    Confianza: 0.94
    Contexto: Principio de realidad relacional comprimible
── Render: theory (markdown) ──
  Perfil: classical.propositional
  Axiomas: 0
  Teoremas: 0
  Claims: 3
```

## theories/04-text-layer-bibliografia.st

- modo: `run`
- estado: ✅ ok
- código de salida: `0`

### stdout

```text
Perfil logico: classical.propositional
Passage p_patrones = [[../07-bibliografia/01-bibliografia-orientativa.md#2-realismo-estructural-y-patrones]]
Formalizacion f_patrones: p_patrones -> (D & L)
Claim c_patrones registrado
Support: c_patrones <- p_patrones
Confidence: c_patrones = 0.9
Context: c_patrones = "Dennett y Ladyman/Ross apoyan el eje patrones-estructura"
Passage p_mecanismos = [[../07-bibliografia/01-bibliografia-orientativa.md#3-explicacion-mecanicista-y-multinivel]]
Formalizacion f_mecanismos: p_mecanismos -> (C & B)
Claim c_mecanismos registrado
Support: c_mecanismos <- p_mecanismos
Confidence: c_mecanismos = 0.91
Context: c_mecanismos = "Craver y Bechtel apoyan el plano de niveles, mecanismos y organización"
Passage p_st = [[../07-bibliografia/01-bibliografia-orientativa.md#11-herramientas-formales-y-de-validacion]]
Formalizacion f_st: p_st -> S
Claim c_st registrado
Support: c_st <- p_st
Confidence: c_st = 0.97
Context: c_st = "ST se incorpora como herramienta metodológica de validación local"
── Render: claims (markdown) ──
  Claim "c_patrones": (D ∧ L)
    Soporte: p_patrones
    Confianza: 0.9
    Contexto: Dennett y Ladyman/Ross apoyan el eje patrones-estructura
  Claim "c_mecanismos": (C ∧ B)
    Soporte: p_mecanismos
    Confianza: 0.91
    Contexto: Craver y Bechtel apoyan el plano de niveles, mecanismos y organización
  Claim "c_st": S
    Soporte: p_st
    Confianza: 0.97
    Contexto: ST se incorpora como herramienta metodológica de validación local
── Render: theory (markdown) ──
  Perfil: classical.propositional
  Axiomas: 0
  Teoremas: 0
  Claims: 3
```

## Estado global

✅ La suite pasó completa.
