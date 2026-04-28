"""build.py — Ensamblador del manuscrito doctoral final.

Lee los capítulos en su orden canónico y ensambla TesisFinal/Tesis.md
con TOC colapsable agrupado y enlaces de regreso al índice.

Uso:
    cd /datos/repos/EstructurasPreontologicas
    python3 TesisFinal/build.py
"""

import os
from pathlib import Path

REPO = Path(__file__).parent.parent

# Estructura agrupada por partes con TOC colapsable
PARTS = [
    ('Front matter', 'frontmatter', [
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
        ('Abstract bilingüe', 'Anexos/A7-abstract-bilingue.md', None),
    ]),
    ('Parte 0 — Plan general del proyecto', 'parte-0-proyecto', [
        ('Capítulo 0.1: Estructura general', '00-proyecto/01-estructura-general.md', None),
        ('Capítulo 0.2: Preguntas, objetivos e hipótesis', '00-proyecto/02-preguntas-objetivos-hipotesis.md', None),
        ('Capítulo 0.3: Plan de capítulos', '00-proyecto/03-plan-de-capitulos.md', None),
        ('Capítulo 0.4: Formalización institucional', '00-proyecto/04-formalizacion-institucional.md', None),
    ]),
    ('Parte 1 — Diagnóstico estructural', 'parte-1-diagnostico', [
        ('Capítulo 1.1: Falencias de la tesis', '01-diagnostico/01-falencias-de-la-tesis.md', None),
        ('Capítulo 1.2: Objeciones discriminantes', '01-diagnostico/02-objeciones-y-riesgos.md', None),
        ('Capítulo 1.3: Estado del arte', '01-diagnostico/03-estado-del-arte.md', None),
    ]),
    ('Parte 2 — Fundamentos ontológicos y epistemológicos', 'parte-2-fundamentos', [
        ('Capítulo 2.1: Ontología material-relacional', '02-fundamentos/01-ontologia-material-relacional.md', None),
        ('Capítulo 2.2: Epistemología de la compresión', '02-fundamentos/02-epistemologia-de-la-compresion.md', None),
        ('Capítulo 2.3: Categorías, objetos, propiedades, identidad', '02-fundamentos/03-categorias-objetos-propiedades-e-identidad.md', None),
        ('Capítulo 2.4: Anclaje empírico (nivel B multiescalar)', '02-fundamentos/04-anclaje-conductual-ecologico.md', None),
        ('Capítulo 2.5: Temporalidad y causalidad', '02-fundamentos/05-temporalidad-y-causalidad.md', None),
        ('Capítulo 2.6: Dimensión normativa y ética', '02-fundamentos/06-dimension-normativa-y-etica.md', None),
    ]),
    ('Parte 3 — Formalización metodológica', 'parte-3-formalizacion', [
        ('Capítulo 3.1: Aparato formal mínimo', '03-formalizacion/01-aparato-formal.md', None),
        ('Capítulo 3.2: Criterios de legitimidad y dossier', '03-formalizacion/02-criterios-de-legitimidad-y-metodo.md', None),
        ('Capítulo 3.3: Auditoría ontológica como protocolo', '03-formalizacion/03-auditoria-ontologica-y-diseno-de-investigacion.md', None),
        ('Capítulo 3.4: Operacionalización de κ vía EDI', '03-formalizacion/04-operacionalizacion-de-kappa.md', None),
        ('Capítulo 3.5: Ética de investigación y gobernanza de datos', '03-formalizacion/05-etica-y-gobernanza-de-datos.md', None),
    ]),
    ('Parte 4 — Debates y limitaciones', 'parte-4-debates', [
        ('Capítulo 4.1: Debates con posiciones rivales', '04-debates/01-debates-con-posiciones-rivales.md', None),
        ('Capítulo 4.2: Limitaciones y puntos de presión', '04-debates/02-limitaciones-y-puntos-de-presion.md', None),
    ]),
    ('Parte 5 — Aplicaciones del marco', 'parte-5-aplicaciones', [
        ('Capítulo 5.0: Criterios de admisión de aplicaciones', '05-aplicaciones/00-criterios-de-admision.md', None),
        ('Capítulo 5.1: Mente, memoria, yo', '05-aplicaciones/01-mente-memoria-yo.md', None),
        ('Capítulo 5.2: Biología y ecología', '05-aplicaciones/02-biologia-y-ecologia.md', None),
        ('Capítulo 5.3: Sistemas técnicos distribuidos', '05-aplicaciones/03-sistemas-tecnicos-distribuidos.md', None),
        ('Capítulo 5.4: Instituciones, mercado, Estado', '05-aplicaciones/04-instituciones-mercado-y-estado.md', None),
        ('Capítulo 5.5: Caso ancla canónico — Behavioral Dynamics (Warren 2006)', '05-aplicaciones/05-dinamica-conductual-reconstruccion-warren.md', None),
        ('Capítulo 5.6: Corpus inter-escala (10 casos, escalas atómica a astrofísica)', '05-aplicaciones/06-corpus-multiescala.md', None),
    ]),
    ('Parte 6 — Cierre demostrativo', 'parte-6-cierre', [
        ('Capítulo 6.1: Conclusión demostrativa', '06-cierre/01-conclusion-demostrativa.md', None),
        ('Capítulo 6.2: Guía de defensa oral', '06-cierre/02-guia-de-defensa.md', None),
        ('Capítulo 6.3: Hoja de ruta para tesis final', '06-cierre/03-hoja-de-ruta-para-tesis-final.md', None),
    ]),
    ('Parte 9 — Corpus EDI: justificación operativa', 'parte-9-corpus', [
        ('Capítulo 9.0: Corpus inter-dominio (30 casos)', '09-simulaciones-edi/README.md', None),
        ('Capítulo 9.1: Caso 30 — Behavioral Dynamics bajo EDI', '09-simulaciones-edi/30_caso_behavioral_dynamics/README.md', None),
        ('Capítulo 9.2: Multi-sonda — validación cruzada', '09-simulaciones-edi/multi_sonda/README.md', None),
        ('Capítulo 9.3: Baselines estadísticos — comparación ejecutada', '09-simulaciones-edi/baselines/README.md', None),
        ('Capítulo 9.4: Caso piloto COVID — dimensión normativa', '09-simulaciones-edi/covid_pilot/README.md', None),
        ('Capítulo 9.5: Perfil agresivo — análisis de drift', '09-simulaciones-edi/perfil_agresivo/README.md', None),
    ]),
    ('Bibliografía', 'bibliografia', [
        ('Bibliografía consolidada', '07-bibliografia/01-bibliografia-orientativa.md', None),
    ]),
    ('Anexos operativos', 'anexos', [
        ('Anexo A.1: Glosario operativo', 'Anexos/A1-glosario-operativo.md', None),
        ('Anexo A.2: Mapa de operadores formales', 'Anexos/A2-mapa-operadores.md', None),
        ('Anexo A.3: Plantilla del dossier de anclaje', 'Anexos/A3-plantilla-dossier.md', None),
        ('Anexo A.4: Tabla comparativa con rivales', 'Anexos/A4-tabla-comparativa-rivales.md', None),
        ('Anexo A.5: Mapa de aplicaciones', 'Anexos/A5-mapa-aplicaciones.md', None),
        ('Anexo A.6: Versiones cortas de defensa', 'Anexos/A6-version-corta-defensa.md', None),
        ('Anexo A.8: Tablas crudas del corpus inter-dominio', 'Anexos/A8-tablas-crudas-corpus.md', None),
        ('Anexo A.9: Listas de figuras, tablas y abreviaturas', 'Anexos/A9-listas-figuras-tablas-abreviaturas.md', None),
        ('Anexo A.10: Figuras Mermaid', 'Anexos/A10-figuras-mermaid.md', None),
        ('Anexo A.11: Validación lógica formal con ST', 'Anexos/A11-validacion-st.md', None),
        ('Anexo A.12: Corpus inter-escala — tablas crudas', 'Anexos/A12-corpus-multiescala-tablas.md', None),
    ]),
    ('Auditorías metodológicas', 'auditorias', [
        ('Auditoría doctoral integral (v2 final)', 'Bitacora/2026-04-28-cierre-pendientes/02-auditoria-doctoral-v2-final.md', None),
        ('Auditoría V5: vacíos estructurales de contenido filosófico', 'Auditoria_V5_Vacios_Estructurales.md', None),
    ]),
]


def slugify(s: str) -> str:
    s = s.lower().replace(' ', '-').replace(':', '')
    pairs = [('á', 'a'), ('é', 'e'), ('í', 'i'), ('ó', 'o'), ('ú', 'u'),
             ('ñ', 'n'), ('κ', 'kappa'), ('μ', 'mu'), ('ε', 'epsilon'),
             ('φ', 'phi'), ('ψ', 'psi'), ('τ', 'tau'), ('β', 'beta'),
             ('α', 'alpha'), ('γ', 'gamma'), ('δ', 'delta'),
             ('ç', 'c'), ('ü', 'u'), ('—', '-'), ('–', '-')]
    for a, b in pairs:
        s = s.replace(a, b)
    keep = []
    for ch in s:
        if ch.isalnum() or ch in '-_.':
            keep.append(ch)
        elif ch == ' ':
            keep.append('-')
    return ''.join(keep)


TOC_ANCHOR = 'tabla-de-contenidos'
TOP_LINK = (f'\n\n<sub>[↑ volver al índice](#{TOC_ANCHOR})</sub>\n\n---\n')


def build():
    out_path = REPO / 'TesisFinal/Tesis.md'
    out_path.parent.mkdir(parents=True, exist_ok=True)

    body_lines = []
    toc_lines = [f'\n\n<a id="{TOC_ANCHOR}"></a>\n\n# 📑 Tabla de Contenidos\n\n']
    toc_lines.append(
        '> **Navegación:** este manuscrito tiene ~10 mil líneas. '
        'Las partes están agrupadas en secciones colapsables. '
        'Haz clic en ▸ para expandir cada parte. Cada capítulo tiene un enlace '
        '«↑ volver al índice» al final para regresar aquí.\n\n')

    # TOC: navegación rápida por partes
    toc_lines.append('## Navegación rápida por partes\n\n')
    for part_title, part_anchor, _ in PARTS:
        toc_lines.append(f'- [{part_title}](#{part_anchor})\n')
    toc_lines.append('\n---\n\n')

    # TOC detallado colapsable
    toc_lines.append('## Índice detallado (colapsable)\n\n')

    for part_title, part_anchor, items in PARTS:
        # Front matter no se colapsa: es la entrada
        is_open = ('open' if part_anchor in ('frontmatter', 'parte-0-proyecto')
                   else '')
        toc_lines.append(f'<details {is_open}>\n')
        toc_lines.append(
            f'<summary><strong>{part_title}</strong></summary>\n\n')
        for title, path, raw in items:
            anchor = slugify(title)
            toc_lines.append(f'- [{title}](#{anchor})\n')
        toc_lines.append('\n</details>\n\n')

    toc_lines.append('---\n')

    # Body: cada parte con su anchor y cada capítulo con anchor + back-to-top
    for part_title, part_anchor, items in PARTS:
        body_lines.append(f'\n\n<a id="{part_anchor}"></a>\n\n')
        # Encabezado de parte (excepto front matter que ya tiene su título)
        if part_anchor != 'frontmatter':
            body_lines.append(f'# {part_title}\n\n')
            body_lines.append(
                f'<sub>[↑ volver al índice](#{TOC_ANCHOR})</sub>\n\n')

        for title, path, raw in items:
            anchor = slugify(title)
            body_lines.append(f'\n\n<a id="{anchor}"></a>\n\n')
            if raw is not None:
                body_lines.append(raw)
            else:
                full_path = REPO / path
                if not full_path.exists():
                    print(f'  WARNING: missing {path}')
                    body_lines.append(f'> _Capítulo no disponible: {path}_\n')
                else:
                    content = full_path.read_text(encoding='utf-8')
                    body_lines.append(content)
                    body_lines.append(TOP_LINK)

    # Front matter primero, luego TOC, luego body restante
    front_idx = 0
    # body_lines[0] = anchor frontmatter; body_lines[1] = front matter raw
    front = body_lines[0] + body_lines[1]
    rest = ''.join(body_lines[2:])
    final_md = front + ''.join(toc_lines) + rest

    out_path.write_text(final_md, encoding='utf-8')

    size = os.path.getsize(out_path)
    lines = len(final_md.splitlines())
    print(f'Manuscrito ensamblado en: {out_path}')
    print(f'Tamaño: {size:,} bytes')
    print(f'Líneas: {lines:,}')


if __name__ == '__main__':
    build()
