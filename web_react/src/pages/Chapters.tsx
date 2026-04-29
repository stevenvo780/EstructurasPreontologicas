import { useQuery } from '@tanstack/react-query';
import { Link } from 'react-router-dom';
import { Folders, FileText, ArrowRight } from 'lucide-react';
import { api } from '../lib/api';
import { PageLoading, ErrorBox } from '../components/Loading';

export default function Chapters() {
  const { data: chapters, isLoading, error } = useQuery({
    queryKey: ['chapters'],
    queryFn: api.chapters,
  });

  if (isLoading) return <PageLoading label="Cargando estructura de capítulos…" />;
  if (error) return <div className="mx-auto max-w-7xl p-8"><ErrorBox error={error} /></div>;
  if (!chapters) return null;

  return (
    <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-8 lg:py-10">
      <header className="mb-8">
        <div className="flex items-center gap-2 text-xs uppercase tracking-wider text-ink-500 dark:text-ink-400 mb-2">
          <Folders className="w-3.5 h-3.5" />
          Capítulos del repositorio
        </div>
        <h1 className="font-serif text-3xl md:text-4xl font-semibold tracking-tight">
          Estructura editorial
        </h1>
        <p className="mt-2 text-ink-600 dark:text-ink-400 max-w-3xl">
          Versiones de trabajo por carpeta — las mismas que el ensamblador <code className="text-xs">TesisFinal/build.py</code> integra
          en el manuscrito final.
        </p>
      </header>

      <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4">
        {chapters.map((ch) => (
          <Link
            key={ch.slug}
            to={`/capitulos/${ch.slug}`}
            className="card card-hover p-5 group block"
          >
            <div className="flex items-start justify-between mb-2">
              <span className="font-mono text-[10px] font-semibold px-2 py-1 rounded-md bg-accent-100 dark:bg-accent-900/30 text-accent-700 dark:text-accent-300">
                {ch.code}
              </span>
              <ArrowRight className="w-4 h-4 text-ink-300 dark:text-ink-700 group-hover:text-accent-500 group-hover:translate-x-0.5 transition-all" />
            </div>
            <h3 className="font-semibold text-base leading-tight mb-1.5 text-ink-900 dark:text-ink-100">
              {ch.title}
            </h3>
            {ch.description && (
              <p className="text-xs text-ink-500 dark:text-ink-400 line-clamp-2 mb-3">
                {ch.description}
              </p>
            )}
            <div className="flex items-center gap-1.5 text-[11px] text-ink-500 dark:text-ink-400">
              <FileText className="w-3 h-3" />
              {ch.docs.length} {ch.docs.length === 1 ? 'documento' : 'documentos'}
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}
