import { Link } from 'react-router-dom';
import {
  GraduationCap,
  Users,
  Sparkles,
  ScrollText,
  Github,
  ExternalLink,
} from 'lucide-react';

export default function About() {
  return (
    <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8 py-10">
      <header className="mb-10">
        <div className="flex items-center gap-2 text-xs uppercase tracking-wider text-ink-500 dark:text-ink-400 mb-2">
          <ScrollText className="w-3.5 h-3.5" />
          Sobre el proyecto
        </div>
        <h1 className="font-serif text-3xl md:text-4xl font-semibold tracking-tight mb-3">
          Estructuras Pre-Ontológicas
        </h1>
        <p className="text-ink-600 dark:text-ink-400 leading-relaxed">
          Tesis doctoral que defiende el <em>irrealismo operativo de estructuras pre-ontológicas</em>
          como propuesta ontológica general multiescalar, validada operativamente sobre 40 casos
          del corpus EDI agregado.
        </p>
      </header>

      <section className="card p-6 mb-6">
        <h2 className="font-semibold flex items-center gap-2 mb-3 text-ink-800 dark:text-ink-100">
          <Users className="w-4 h-4 text-accent-500" />
          Autoría declarada
        </h2>
        <ul className="space-y-3 text-sm text-ink-700 dark:text-ink-300">
          <li>
            <strong>Jacob Agudelo</strong> · autor principal (concepto y dirección teórica) ·
            Universidad de Antioquia.
          </li>
          <li>
            <strong>Steven Vallejo Ortiz</strong> · colaborador (técnica e ingeniería computacional).
          </li>
          <li>
            <strong>Anthropic Claude</strong> · co-autoría con IA declarada como instrumento bajo
            dirección humana, equivalente epistémico a software estadístico avanzado. La IA no
            aparece como autora en sentido legal ni epistémico.
          </li>
        </ul>
      </section>

      <section className="card p-6 mb-6">
        <h2 className="font-semibold flex items-center gap-2 mb-3 text-ink-800 dark:text-ink-100">
          <GraduationCap className="w-4 h-4 text-accent-500" />
          Marco institucional
        </h2>
        <p className="text-sm text-ink-700 dark:text-ink-300 leading-relaxed">
          Doctorado en Filosofía. Línea: filosofía de la ciencia y ciencias de la complejidad.
          Universidad de Antioquia, Medellín, Colombia. Versión integral defendible al cierre
          conceptual del 2026-04-29.
        </p>
      </section>

      <section className="card p-6 mb-6">
        <h2 className="font-semibold flex items-center gap-2 mb-3 text-ink-800 dark:text-ink-100">
          <Sparkles className="w-4 h-4 text-accent-500" />
          Tres marcos generales coordinados
        </h2>
        <div className="grid md:grid-cols-3 gap-4 text-sm">
          <div className="p-4 rounded-lg bg-ink-50 dark:bg-ink-800/40 border border-ink-200 dark:border-ink-800">
            <div className="font-semibold mb-1">Ontología</div>
            <p className="text-xs text-ink-600 dark:text-ink-400 leading-relaxed">
              Sustrato material dinámico + acoplamiento + atractor empírico + cierre operativo κ,
              instanciable a cualquier escala.
            </p>
          </div>
          <div className="p-4 rounded-lg bg-ink-50 dark:bg-ink-800/40 border border-ink-200 dark:border-ink-800">
            <div className="font-semibold mb-1">Epistemología</div>
            <p className="text-xs text-ink-600 dark:text-ink-400 leading-relaxed">
              Conocimiento como compresión disciplinada bajo intervención ablativa, con verdad
              como preservación estructural verificable.
            </p>
          </div>
          <div className="p-4 rounded-lg bg-ink-50 dark:bg-ink-800/40 border border-ink-200 dark:border-ink-800">
            <div className="font-semibold mb-1">Metodología</div>
            <p className="text-xs text-ink-600 dark:text-ink-400 leading-relaxed">
              Aparato ABM+ODE acoplado + protocolo C1-C5 + EDI + dossier de 14 componentes + suite
              ST de validación lógica.
            </p>
          </div>
        </div>
      </section>

      <section className="card p-6 mb-6">
        <h2 className="font-semibold mb-3 text-ink-800 dark:text-ink-100">Recursos</h2>
        <div className="grid sm:grid-cols-2 gap-3">
          <a
            href="https://github.com/stevenvo780/EstructurasPreontologicas"
            target="_blank"
            rel="noreferrer"
            className="flex items-center gap-2 p-3 rounded-lg border border-ink-200 dark:border-ink-800 hover:border-accent-400 hover:bg-accent-50 dark:hover:bg-accent-900/10 transition-colors"
          >
            <Github className="w-4 h-4 text-ink-500" />
            <div>
              <div className="text-sm font-medium">Repositorio en GitHub</div>
              <div className="text-xs text-ink-500">Código fuente completo</div>
            </div>
            <ExternalLink className="w-3 h-3 text-ink-400 ml-auto" />
          </a>
          <Link
            to="/tesis"
            className="flex items-center gap-2 p-3 rounded-lg border border-ink-200 dark:border-ink-800 hover:border-accent-400 hover:bg-accent-50 dark:hover:bg-accent-900/10 transition-colors"
          >
            <ScrollText className="w-4 h-4 text-ink-500" />
            <div>
              <div className="text-sm font-medium">Manuscrito completo</div>
              <div className="text-xs text-ink-500">Tesis ensamblada en línea</div>
            </div>
          </Link>
        </div>
      </section>
    </div>
  );
}
