# Manuscrito doctoral final ensamblado

Este directorio contiene el manuscrito doctoral consolidado en un archivo único listo para presentación a la Universidad de Antioquia.

## Archivos

- **Tesis.md** — manuscrito ensamblado completo.
- **README.md** — este archivo.
- **MAPA_INTEGRACION_ANEXOS.md** — trazabilidad de la absorción de anexos al cuerpo y de los apéndices técnicos mínimos.

## Cómo se construye

El archivo `Tesis.md` se ensambla automáticamente desde los capítulos del repositorio en el orden canónico definido por el plan doctoral:

1. Preliminares: portada, resumen/abstract, listas editoriales y glosario.
2. Introducción y estado del arte.
3. Parte I: fundamentos ontológicos y epistemológicos.
4. Parte II: aparato formal, dossier, operacionalización EDI, validación ST y gobernanza.
5. Parte III: evidencia empírica, corpus EDI, corpus multiescala y aplicaciones.
6. Parte IV: rivales, objeciones y limitaciones consolidadas.
7. Parte V: cierre demostrativo y hoja de ruta post-defensa.
8. Bibliografía.
9. Apéndices técnicos mínimos: tablas crudas inter-dominio, tablas crudas multiescala y figuras Mermaid.

## Re-ensamblaje

Para regenerar el manuscrito tras cambios en capítulos individuales:

```bash
cd /datos/repos/EstructurasPreontologicas
python3 TesisFinal/build.py
```

## Política

Este es el documento que se presenta a la Universidad. Cualquier corrección final se hace primero en los capítulos individuales (fuente de verdad) y luego se re-ensambla. Los materiales administrativos, bitácoras y defensa oral quedan en el repositorio, pero fuera del cuerpo del manuscrito salvo cuando aportan argumento o evidencia verificable.
