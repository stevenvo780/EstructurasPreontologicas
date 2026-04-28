"""build.py — Ensamblador del manuscrito doctoral final.

Lee los capítulos en su orden canónico y ensambla TesisFinal/Tesis.md.

Uso:
    cd /datos/repos/EstructurasPreontologicas
    python3 TesisFinal/build.py
"""

import os
from pathlib import Path

REPO = Path(__file__).parent.parent

CHAPTERS = [
    # (Título, ruta relativa al repo, contenido inline si no hay archivo)
    ('Front matter', None, '''# Estructuras Pre-Ontológicas

## Realismo Irrealista Operativo y Compresión Multiescala con Validación EDI Multidominio

**Tesis doctoral en Filosofía de la Ciencia y Ciencias de la Complejidad**

**Universidad de Antioquia · Medellín · Colombia**

---

### Autoría declarada

**Autor principal (concepto y dirección teórica):** Jacob Agudelo. Universidad de Antioquia.

**Colaborador (técnica e ingeniería computacional):** Steven Vallejo Ortiz.

**Co-autoría con inteligencia artificial declarada:** Anthropic Claude (Opus 4.7), como instrumento de implementación bajo dirección humana. La IA no aparece como autora en el sentido legal ni epistémico: aparece como herramienta, igual que cualquier software estadístico avanzado. La declaración detallada del rol y los límites de la IA está en el capítulo `03-formalizacion/05-etica-y-gobernanza-de-datos.md`, sección 5.

### Marco institucional

**Programa de inscripción:** Doctorado en Filosofía. Línea: filosofía de la ciencia y ciencias de la complejidad.

**Estado del manuscrito:** integral defendible. La formalización institucional completa se documenta en el capítulo `00-proyecto/04-formalizacion-institucional.md`.

**Versión consolidada:** 2026-04-28.

### Sobre la disponibilidad y la fuente de verdad del documento

> Documento ensamblado automáticamente desde el repositorio doctoral. La fuente de verdad textual son los capítulos individuales en cada carpeta numerada. La fuente de verdad numérica del corpus EDI son los `outputs/metrics.json` versionados en `09-simulaciones-edi/<caso>/`. Si hay discrepancia entre este ensamblado y la fuente, prevalece la fuente.

### Agradecimientos

A la Universidad de Antioquia, por sostener una tradición de filosofía de la ciencia que hace posible este trabajo. A los colegas y revisores que aportaron críticas tempranas. A los autores de los datasets públicos del corpus, sin los cuales la cartografía multidominio no sería viable. A William H. Warren y Brett R. Fajen por la conjetura cuantitativa de la behavioral dynamics que opera como caso ancla.

---
'''),
    ('Abstract', 'Anexos/A7-abstract-bilingue.md', None),
    ('Capítulo 0: Plan general', '00-proyecto/01-estructura-general.md', None),
    ('Capítulo 0.1: Preguntas, objetivos e hipótesis', '00-proyecto/02-preguntas-objetivos-hipotesis.md', None),
    ('Capítulo 0.2: Plan de capítulos', '00-proyecto/03-plan-de-capitulos.md', None),
    ('Capítulo 0.3: Formalización institucional', '00-proyecto/04-formalizacion-institucional.md', None),
    ('Capítulo 1: Diagnóstico estructural', '01-diagnostico/01-falencias-de-la-tesis.md', None),
    ('Capítulo 1.1: Objeciones discriminantes', '01-diagnostico/02-objeciones-y-riesgos.md', None),
    ('Capítulo 1.2: Estado del arte', '01-diagnostico/03-estado-del-arte.md', None),
    ('Capítulo 2: Ontología material-relacional', '02-fundamentos/01-ontologia-material-relacional.md', None),
    ('Capítulo 2.1: Epistemología de la compresión', '02-fundamentos/02-epistemologia-de-la-compresion.md', None),
    ('Capítulo 2.2: Categorías, objetos, propiedades, identidad', '02-fundamentos/03-categorias-objetos-propiedades-e-identidad.md', None),
    ('Capítulo 2.3: Anclaje conductual-ecológico (nivel B)', '02-fundamentos/04-anclaje-conductual-ecologico.md', None),
    ('Capítulo 3: Aparato formal mínimo', '03-formalizacion/01-aparato-formal.md', None),
    ('Capítulo 3.1: Criterios de legitimidad y dossier', '03-formalizacion/02-criterios-de-legitimidad-y-metodo.md', None),
    ('Capítulo 3.2: Auditoría ontológica como protocolo', '03-formalizacion/03-auditoria-ontologica-y-diseno-de-investigacion.md', None),
    ('Capítulo 3.3: Operacionalización de κ vía EDI', '03-formalizacion/04-operacionalizacion-de-kappa.md', None),
    ('Capítulo 3.4: Ética de investigación y gobernanza de datos', '03-formalizacion/05-etica-y-gobernanza-de-datos.md', None),
    ('Capítulo 4: Debates con posiciones rivales', '04-debates/01-debates-con-posiciones-rivales.md', None),
    ('Capítulo 4.1: Limitaciones y puntos de presión', '04-debates/02-limitaciones-y-puntos-de-presion.md', None),
    ('Capítulo 5: Criterios de admisión de aplicaciones', '05-aplicaciones/00-criterios-de-admision.md', None),
    ('Capítulo 5.1: Mente, memoria, yo', '05-aplicaciones/01-mente-memoria-yo.md', None),
    ('Capítulo 5.2: Biología y ecología', '05-aplicaciones/02-biologia-y-ecologia.md', None),
    ('Capítulo 5.3: Sistemas técnicos distribuidos', '05-aplicaciones/03-sistemas-tecnicos-distribuidos.md', None),
    ('Capítulo 5.4: Instituciones, mercado, Estado', '05-aplicaciones/04-instituciones-mercado-y-estado.md', None),
    ('Capítulo 5.5: Caso ancla canónico - Behavioral Dynamics (Warren 2006)', '05-aplicaciones/05-dinamica-conductual-reconstruccion-warren.md', None),
    ('Capítulo 6: Conclusión demostrativa', '06-cierre/01-conclusion-demostrativa.md', None),
    ('Capítulo 6.1: Guía de defensa oral', '06-cierre/02-guia-de-defensa.md', None),
    ('Capítulo 6.2: Hoja de ruta para tesis final', '06-cierre/03-hoja-de-ruta-para-tesis-final.md', None),
    ('Capítulo 9: Corpus EDI - validación empírica multidominio', '09-simulaciones-edi/README.md', None),
    ('Capítulo 9.30: Caso 30 - Behavioral Dynamics bajo EDI', '09-simulaciones-edi/30_caso_behavioral_dynamics/README.md', None),
    ('Capítulo 9.31: Multi-sonda - validación cruzada de 3 strong', '09-simulaciones-edi/multi_sonda/README.md', None),
    ('Capítulo 9.32: Baselines estadísticos - comparación ejecutada', '09-simulaciones-edi/baselines/README.md', None),
    ('Anexo A.1: Glosario operativo', 'Anexos/A1-glosario-operativo.md', None),
    ('Anexo A.2: Mapa de operadores formales', 'Anexos/A2-mapa-operadores.md', None),
    ('Anexo A.3: Plantilla del dossier de anclaje', 'Anexos/A3-plantilla-dossier.md', None),
    ('Anexo A.4: Tabla comparativa con rivales', 'Anexos/A4-tabla-comparativa-rivales.md', None),
    ('Anexo A.5: Mapa de aplicaciones', 'Anexos/A5-mapa-aplicaciones.md', None),
    ('Anexo A.6: Versiones cortas de defensa', 'Anexos/A6-version-corta-defensa.md', None),
    ('Anexo A.8: Tablas crudas del corpus EDI', 'Anexos/A8-tablas-crudas-corpus.md', None),
    ('Anexo A.9: Listas de figuras, tablas y abreviaturas', 'Anexos/A9-listas-figuras-tablas-abreviaturas.md', None),
    ('Bibliografía', '07-bibliografia/01-bibliografia-orientativa.md', None),
]


def slugify(s: str) -> str:
    s = s.lower().replace(' ', '-').replace(':', '')
    for a, b in [('á', 'a'), ('é', 'e'), ('í', 'i'), ('ó', 'o'), ('ú', 'u'), ('ñ', 'n')]:
        s = s.replace(a, b)
    return s


def build():
    out_path = REPO / 'TesisFinal/Tesis.md'
    out_path.parent.mkdir(parents=True, exist_ok=True)

    out_lines = []

    for title, path, raw in CHAPTERS:
        anchor = slugify(title)
        out_lines.append(f'\n\n<a id="{anchor}"></a>\n\n')
        if raw is not None:
            out_lines.append(raw)
        else:
            full_path = REPO / path
            if not full_path.exists():
                print(f'  WARNING: missing {path}')
                out_lines.append(f'> _Capítulo no disponible: {path}_\n')
            else:
                content = full_path.read_text(encoding='utf-8')
                out_lines.append(content)
                out_lines.append('\n\n---\n')

    toc_lines = ['# Tabla de Contenidos\n\n']
    for title, path, raw in CHAPTERS:
        anchor = slugify(title)
        toc_lines.append(f'- [{title}](#{anchor})\n')
    toc_lines.append('\n---\n')

    final_md = out_lines[0] + out_lines[1] + ''.join(toc_lines) + ''.join(out_lines[2:])
    out_path.write_text(final_md, encoding='utf-8')

    size = os.path.getsize(out_path)
    lines = len(final_md.splitlines())
    print(f'Manuscrito ensamblado en: {out_path}')
    print(f'Tamaño: {size:,} bytes')
    print(f'Líneas: {lines:,}')


if __name__ == '__main__':
    build()
