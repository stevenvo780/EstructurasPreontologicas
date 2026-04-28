# Manuscrito doctoral final ensamblado

Este directorio contiene el manuscrito doctoral consolidado en un archivo único listo para presentación a la Universidad de Antioquia.

## Archivos

- **Tesis.md** — manuscrito ensamblado completo (~7,200 líneas, ~432 KB).
- **README.md** — este archivo.

## Cómo se construye

El archivo `Tesis.md` se ensambla automáticamente desde los capítulos del repositorio en el orden canónico definido por el plan doctoral:

1. Front matter (portada, autoría, versión)
2. Abstract bilingüe (español + inglés)
3. Capítulos 0 — Plan general
4. Capítulos 1 — Diagnóstico y objeciones
5. Capítulos 2 — Fundamentos (ontología, epistemología, categorías, nivel B)
6. Capítulos 3 — Aparato formal y operacionalización EDI
7. Capítulos 4 — Debates con rivales y limitaciones
8. Capítulos 5 — Aplicaciones (criterios, programáticos, caso ancla)
9. Capítulos 6 — Cierre demostrativo, defensa, hoja de ruta
10. Capítulo 9 — Corpus EDI (validación multidominio)
11. Anexos A.1 a A.6 (glosario, operadores, dossier, rivales, aplicaciones, defensa)
12. Bibliografía formal (90 referencias)

## Re-ensamblaje

Para regenerar el manuscrito tras cambios en capítulos individuales:

```bash
cd /datos/repos/EstructurasPreontologicas
python3 TesisFinal/build.py
```

## Política

Este es el documento que se presenta a la Universidad. Cualquier corrección final se hace primero en los capítulos individuales (fuente de verdad) y luego se re-ensambla.
