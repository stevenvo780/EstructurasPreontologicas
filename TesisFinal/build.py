"""build.py — Ensamblador del manuscrito doctoral final.

Genera TesisFinal/Tesis.md con:
  - Front matter visible (sin anchors duplicados)
  - TOC colapsable por partes (HTML inline limpio)
  - Anclajes únicos por capítulo (sin duplicación)
  - Enlaces "↑ volver al índice" tras cada capítulo

Uso:
    cd /datos/repos/EstructurasPreontologicas
    python3 TesisFinal/build.py
"""

import os
from pathlib import Path

REPO = Path(__file__).parent.parent

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

**Director de tesis:** [pendiente de declaración formal — bloqueador procedimental conocido; documentación administrativa fuera del manuscrito en `00-proyecto/04-formalizacion-institucional.md`].

**Co-autoría con inteligencia artificial declarada:** Anthropic Claude (Opus 4.7), como instrumento de implementación bajo dirección humana. La IA no aparece como autora en el sentido legal ni epistémico: aparece como herramienta, igual que cualquier software estadístico avanzado. La declaración detallada del rol y los límites de la IA está en el capítulo de ética de investigación y gobernanza de datos (Parte II, cap. 5).

### Marco institucional

**Programa de inscripción:** Doctorado en Filosofía. Línea: filosofía de la ciencia y ciencias de la complejidad.

**Estado del manuscrito:** integral defendible. La formalización institucional completa se conserva como documentación administrativa del repositorio, fuera del cuerpo argumental.

**Versión consolidada:** 2026-04-28.

### Sobre la disponibilidad y la fuente de verdad del documento

> Documento ensamblado automáticamente desde el repositorio doctoral. La fuente de verdad textual son los capítulos individuales en cada carpeta numerada. La fuente de verdad numérica del corpus EDI son los `outputs/metrics.json` versionados en `09-simulaciones-edi/<caso>/`. Si hay discrepancia entre este ensamblado y la fuente, prevalece la fuente.

### Agradecimientos

A la Universidad de Antioquia, por sostener una tradición de filosofía de la ciencia que hace posible este trabajo. A los colegas y revisores que aportaron críticas tempranas. A los autores de los datasets públicos del corpus, sin los cuales la cartografía multidominio no sería viable. A William H. Warren y Brett R. Fajen por la conjetura cuantitativa de la behavioral dynamics que opera como caso ancla.
'''),
        ('Resumen y abstract bilingüe', '00-proyecto/05-resumen-y-abstract.md', None),
        ('Listas de figuras, tablas y abreviaturas', '00-proyecto/06-listas-figuras-tablas-abreviaturas.md', None),
        ('Glosario operativo', '00-proyecto/07-glosario-operativo.md', None),
    ]),
    # ── INTRODUCCIÓN ────────────────────────────────────────────────
    ('Introducción', 'introduccion', [
        ('Introducción', '00-proyecto/00-introduccion.md', None),
        ('Estado del arte', '01-diagnostico/03-estado-del-arte.md', None),
    ]),
    # ── PARTE I: FUNDAMENTOS ────────────────────────────────────────
    ('Parte I — Fundamentos ontológicos y epistemológicos', 'parte-1-fundamentos', [
        ('Capítulo 1: Ontología material-relacional', '02-fundamentos/01-ontologia-material-relacional.md', None),
        ('Capítulo 2: Epistemología de la compresión', '02-fundamentos/02-epistemologia-de-la-compresion.md', None),
        ('Capítulo 3: Categorías, objetos, propiedades, identidad', '02-fundamentos/03-categorias-objetos-propiedades-e-identidad.md', None),
        ('Capítulo 4: Anclaje empírico (nivel B multiescalar)', '02-fundamentos/04-anclaje-conductual-ecologico.md', None),
        ('Capítulo 5: Temporalidad y causalidad', '02-fundamentos/05-temporalidad-y-causalidad.md', None),
        ('Capítulo 6: Dimensión normativa y ética', '02-fundamentos/06-dimension-normativa-y-etica.md', None),
    ]),
    # ── PARTE II: APARATO Y MÉTODO ──────────────────────────────────
    ('Parte II — Aparato formal y método', 'parte-2-metodo', [
        ('Capítulo 7: Aparato formal mínimo', '03-formalizacion/01-aparato-formal.md', None),
        ('Capítulo 8: Mapa de operadores formales', '03-formalizacion/06-mapa-operadores-formales.md', None),
        ('Capítulo 9: Criterios de legitimidad y dossier', '03-formalizacion/02-criterios-de-legitimidad-y-metodo.md', None),
        ('Capítulo 10: Plantilla del dossier de anclaje', '03-formalizacion/07-plantilla-dossier-anclaje.md', None),
        ('Capítulo 11: Auditoría ontológica como protocolo', '03-formalizacion/03-auditoria-ontologica-y-diseno-de-investigacion.md', None),
        ('Capítulo 12: Operacionalización de κ vía EDI', '03-formalizacion/04-operacionalizacion-de-kappa.md', None),
        ('Capítulo 13: Validación lógica formal con ST', '03-formalizacion/08-validacion-logica-st.md', None),
        ('Capítulo 14: Ética de investigación y gobernanza de datos', '03-formalizacion/05-etica-y-gobernanza-de-datos.md', None),
    ]),
    # ── PARTE III: EVIDENCIA EMPÍRICA ───────────────────────────────
    ('Parte III — Evidencia empírica', 'parte-3-evidencia', [
        ('Capítulo 15: Criterios de admisión de aplicaciones', '05-aplicaciones/00-criterios-de-admision.md', None),
        ('Capítulo 16: Mapa de aplicaciones — corpus inter-dominio e inter-escala', '05-aplicaciones/07-mapa-aplicaciones-corpus.md', None),
        ('Capítulo 17: Caso ancla canónico — Behavioral Dynamics (Warren 2006)', '05-aplicaciones/05-dinamica-conductual-reconstruccion-warren.md', None),
        ('Capítulo 18: Corpus inter-dominio (30 casos)', '09-simulaciones-edi/README.md', None),
        ('Capítulo 19: Corpus inter-escala (10 casos)', '05-aplicaciones/06-corpus-multiescala.md', None),
        ('Capítulo 20: Caso 30 — Behavioral Dynamics bajo EDI', '09-simulaciones-edi/30_caso_behavioral_dynamics/README.md', None),
        ('Capítulo 21: Aplicaciones programáticas — Mente, memoria, yo', '05-aplicaciones/01-mente-memoria-yo.md', None),
        ('Capítulo 22: Aplicaciones programáticas — Biología y ecología', '05-aplicaciones/02-biologia-y-ecologia.md', None),
        ('Capítulo 23: Aplicaciones programáticas — Sistemas técnicos distribuidos', '05-aplicaciones/03-sistemas-tecnicos-distribuidos.md', None),
        ('Capítulo 24: Aplicaciones programáticas — Instituciones, mercado, Estado', '05-aplicaciones/04-instituciones-mercado-y-estado.md', None),
    ]),
    # ── PARTE IV: DISCUSIÓN CRÍTICA ─────────────────────────────────
    ('Parte IV — Discusión crítica', 'parte-4-discusion', [
        ('Capítulo 25: Debates con posiciones rivales', '04-debates/01-debates-con-posiciones-rivales.md', None),
        ('Capítulo 26: Tabla comparativa con rivales', '04-debates/03-tabla-comparativa-rivales.md', None),
        ('Capítulo 27: Anticipación de objeciones filosóficas', '04-debates/04-anticipacion-objeciones-filosoficas.md', None),
        ('Capítulo 28: Limitaciones y puntos de presión', '04-debates/02-limitaciones-y-puntos-de-presion.md', None),
        ('Capítulo 29: Limitaciones declaradas consolidadas', '04-debates/05-limitaciones-declaradas-consolidacion.md', None),
    ]),
    # ── PARTE V: CIERRE ─────────────────────────────────────────────
    ('Parte V — Cierre demostrativo', 'parte-5-cierre', [
        ('Capítulo 30: Conclusión demostrativa', '06-cierre/01-conclusion-demostrativa.md', None),
        ('Capítulo 31: Hoja de ruta post-defensa', '06-cierre/03-hoja-de-ruta-para-tesis-final.md', None),
    ]),
    # ── BIBLIOGRAFÍA ────────────────────────────────────────────────
    ('Bibliografía', 'bibliografia', [
        ('Bibliografía consolidada', '07-bibliografia/01-bibliografia-orientativa.md', None),
    ]),
    # ── APÉNDICES TÉCNICOS MÍNIMOS ─────────────────────────────────
    ('Apéndices técnicos mínimos', 'apendices-tecnicos', [
        ('Apéndice técnico 1: Tablas crudas del corpus inter-dominio', '10-apendices-tecnicos/01-tablas-crudas-corpus-interdominio.md', None),
        ('Apéndice técnico 2: Tablas crudas del corpus inter-escala', '10-apendices-tecnicos/02-tablas-crudas-corpus-multiescala.md', None),
        ('Apéndice técnico 3: Figuras Mermaid', '10-apendices-tecnicos/03-figuras-mermaid.md', None),
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
BACK_LINK = (
    f'\n\n<p align="right"><sub><a href="#{TOC_ANCHOR}">↑ volver al índice</a></sub></p>\n\n---\n')


def build_toc():
    """Construye el TOC colapsable como bloque HTML válido."""
    toc = []

    # Anchor único del TOC (oculto pero referenciable)
    toc.append(f'<div id="{TOC_ANCHOR}"></div>\n\n')
    toc.append('# 📑 Tabla de Contenidos\n\n')
    toc.append(
        '> **Navegación:** este manuscrito tiene ~10 mil líneas. '
        'Las partes están agrupadas en secciones colapsables. '
        'Haz clic en ▸ para expandir cada parte. Cada capítulo termina '
        'con un enlace «↑ volver al índice» que regresa aquí.\n\n')

    # Navegación rápida
    toc.append('## Navegación rápida por partes\n\n')
    for part_title, part_anchor, _ in PARTS:
        toc.append(f'- [{part_title}](#{part_anchor})\n')
    toc.append('\n---\n\n')

    # Índice detallado colapsable
    toc.append('## Índice detallado\n\n')

    for part_title, part_anchor, items in PARTS:
        is_open = ' open' if part_anchor in (
            'frontmatter', 'parte-0-proyecto') else ''
        toc.append(f'<details{is_open}>\n')
        toc.append(f'<summary><b>{part_title}</b></summary>\n\n')
        for title, _, _ in items:
            anchor = slugify(title)
            toc.append(f'- [{title}](#{anchor})\n')
        toc.append('\n</details>\n\n')

    toc.append('---\n')
    return ''.join(toc)


def build():
    out_path = REPO / 'TesisFinal/Tesis.md'
    out_path.parent.mkdir(parents=True, exist_ok=True)

    body = []

    for part_title, part_anchor, items in PARTS:
        # Anchor de la parte (único, antes del título)
        body.append(f'\n\n<div id="{part_anchor}"></div>\n\n')

        # Encabezado de parte (front matter ya viene con su propio H1)
        if part_anchor != 'frontmatter':
            body.append(f'# {part_title}\n\n')

        # Capítulos de la parte
        for title, path, raw in items:
            anchor = slugify(title)
            body.append(f'\n<div id="{anchor}"></div>\n\n')
            if raw is not None:
                body.append(raw)
            else:
                full_path = REPO / path
                if not full_path.exists():
                    print(f'  WARNING: missing {path}')
                    body.append(f'> _Capítulo no disponible: {path}_\n')
                else:
                    content = full_path.read_text(encoding='utf-8')
                    body.append(content)
                    body.append(BACK_LINK)

    # Estructura final: Front matter, luego TOC, luego resto del cuerpo
    front_matter_block = body[0] + body[1] + body[2]  # anchor parte + raw front
    rest = ''.join(body[3:])
    toc = build_toc()

    final_md = front_matter_block + '\n\n' + toc + rest
    out_path.write_text(final_md, encoding='utf-8')

    size = os.path.getsize(out_path)
    lines = len(final_md.splitlines())
    print(f'Manuscrito ensamblado en: {out_path}')
    print(f'Tamaño: {size:,} bytes')
    print(f'Líneas: {lines:,}')


if __name__ == '__main__':
    build()
