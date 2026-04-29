import { useParams, Link } from 'react-router-dom';
import { useQuery } from '@tanstack/react-query';
import { ArrowLeft, FileText, Folders, Bookmark } from 'lucide-react';
import { useState } from 'react';
import { api } from '../lib/api';
import { PageLoading, ErrorBox } from '../components/Loading';
import HtmlContent from '../components/HtmlContent';
import { cn } from '../lib/cn';

export default function ChapterDetail() {
  const { slug = '' } = useParams();
  const { data, isLoading, error } = useQuery({
    queryKey: ['chapter', slug],
    queryFn: () => api.chapter(slug),
    enabled: !!slug,
  });

  const [activeDoc, setActiveDoc] = useState(0);

  if (isLoading) return <PageLoading label={`Cargando capítulo ${slug}…`} />;
  if (error || !data)
    return (
      <div className="mx-auto max-w-5xl p-8">
        <ErrorBox error={error ?? new Error('Capítulo no encontrado')} />
        <Link to="/capitulos" className="btn-outline mt-4">
          ← Volver
        </Link>
      </div>
    );

  const current = data.docs[activeDoc];

  return (
    <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-8">
      <Link
        to="/capitulos"
        className="inline-flex items-center gap-1.5 text-sm text-ink-500 dark:text-ink-400 hover:text-accent-600 dark:hover:text-accent-400 mb-4 transition-colors"
      >
        <ArrowLeft className="w-3.5 h-3.5" />
        Volver a capítulos
      </Link>

      <header className="mb-6">
        <div className="flex items-center gap-2 text-xs text-ink-500 dark:text-ink-400 mb-2 flex-wrap">
          <span className="font-mono px-2 py-0.5 rounded bg-accent-100 dark:bg-accent-900/30 text-accent-700 dark:text-accent-300 font-semibold">
            {data.code}
          </span>
          <span className="inline-flex items-center gap-1">
            <Folders className="w-3 h-3" />
            {data.docs.length} documentos
          </span>
        </div>
        <h1 className="font-serif text-3xl md:text-4xl font-semibold tracking-tight">
          {data.title}
        </h1>
        {data.description && (
          <p className="mt-2 text-ink-600 dark:text-ink-400 max-w-3xl">
            {data.description}
          </p>
        )}
      </header>

      <div className="grid lg:grid-cols-[260px_1fr] gap-6">
        {/* Sidebar con docs */}
        <aside>
          <div className="sticky top-[5.5rem] max-h-[calc(100vh-7rem)] overflow-y-auto card p-3">
            <div className="flex items-center gap-1.5 px-2 py-1 mb-2 text-xs font-semibold uppercase tracking-wider text-ink-500 dark:text-ink-400">
              <FileText className="w-3 h-3" />
              Documentos
            </div>
            <ul className="space-y-0.5">
              {data.docs.map((doc, i) => (
                <li key={i}>
                  <button
                    onClick={() => setActiveDoc(i)}
                    className={cn(
                      'w-full text-left px-3 py-2 rounded-lg text-sm transition-colors flex items-center gap-2',
                      i === activeDoc
                        ? 'bg-accent-100 dark:bg-accent-900/30 text-accent-700 dark:text-accent-300 font-medium'
                        : 'text-ink-700 dark:text-ink-300 hover:bg-ink-100 dark:hover:bg-ink-800/50'
                    )}
                  >
                    <FileText className="w-3.5 h-3.5 flex-none" />
                    <span className="truncate">{doc.title}</span>
                  </button>
                </li>
              ))}
            </ul>

            {current?.toc && current.toc.length > 0 && (
              <>
                <div className="flex items-center gap-1.5 px-2 py-1 mt-4 mb-1 text-xs font-semibold uppercase tracking-wider text-ink-500 dark:text-ink-400">
                  <Bookmark className="w-3 h-3" />
                  Secciones
                </div>
                <ul className="space-y-0.5 text-xs">
                  {current.toc.map((t, i) => (
                    <li key={i} style={{ paddingLeft: (t.level - 1) * 8 }}>
                      <a
                        href={`#${t.anchor}`}
                        className="block px-2 py-1 rounded text-ink-600 dark:text-ink-400 hover:bg-ink-100 dark:hover:bg-ink-800/50 hover:text-ink-900 dark:hover:text-ink-100 truncate"
                      >
                        {t.title}
                      </a>
                    </li>
                  ))}
                </ul>
              </>
            )}
          </div>
        </aside>

        <article className="min-w-0">
          <div className="card p-6 sm:p-8 lg:p-10">
            {current ? (
              <HtmlContent html={current.html} />
            ) : (
              <p className="text-sm text-ink-500">Selecciona un documento</p>
            )}
          </div>
        </article>
      </div>
    </div>
  );
}
