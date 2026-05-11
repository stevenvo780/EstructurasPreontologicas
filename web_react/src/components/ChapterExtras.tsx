import { useState } from 'react';
import { useQuery } from '@tanstack/react-query';
import { BookOpen, ChevronDown, ChevronRight, Clock } from 'lucide-react';
import { api } from '../lib/api';
import { ChapterExtraSummary } from '../types';
import HtmlContent from './HtmlContent';
import { Skeleton, ErrorBox } from './Loading';
import { cn } from '../lib/cn';

/**
 * Lecturas extendidas de un capítulo.
 *
 * Consume los endpoints backend introducidos en la Fase 1:
 *   GET /api/chapters/{slug}/extras        → lista de extras disponibles
 *   GET /api/chapters/{slug}/extras/{name} → contenido renderizado on-demand
 *
 * Los extras viven en disco como `<cap>/_extendido/<tema>.md` (p. ej.
 * `04-debates/_extendido/rival-cognitivismo-computacional.md`). Son material
 * suplementario que no entra al ensamblado canónico de `TesisFinal/Tesis.md`,
 * pero que el lector puede expandir inline desde la página del capítulo.
 *
 * UX: acordeón inline. Cada item se expande al click y dispara el fetch del
 * contenido sólo en el primer expand (React Query cachea el resultado).
 */

interface ChapterExtrasProps {
  slug: string;
}

export default function ChapterExtras({ slug }: ChapterExtrasProps) {
  const {
    data,
    isLoading,
    error,
  } = useQuery({
    queryKey: ['chapter-extras', slug],
    queryFn: () => api.chapterExtras(slug),
    enabled: !!slug,
    // Lista barata y estable; no refetchear al volver a foco
    staleTime: 5 * 60_000,
  });

  if (isLoading) {
    return (
      <section className="mt-10">
        <Skeleton className="h-6 w-48 mb-3" />
        <Skeleton className="h-16 w-full" />
      </section>
    );
  }

  if (error) {
    return (
      <section className="mt-10">
        <ErrorBox error={error} />
      </section>
    );
  }

  const extras = data?.extras ?? [];
  if (extras.length === 0) return null;

  return (
    <section className="mt-10 border-t border-ink-200 dark:border-ink-800 pt-8">
      <header className="mb-4 flex items-center gap-2">
        <BookOpen className="w-4 h-4 text-accent-500" />
        <h2 className="font-serif text-xl font-semibold tracking-tight">
          Lecturas extendidas
        </h2>
        <span className="text-xs text-ink-500 dark:text-ink-400 ml-1">
          ({extras.length})
        </span>
      </header>
      <p className="text-sm text-ink-600 dark:text-ink-400 mb-4 max-w-3xl">
        Material suplementario no incluido en el ensamblado canónico. Se carga
        bajo demanda al expandir cada entrada.
      </p>
      <ul className="space-y-2">
        {extras.map((extra) => (
          <ExtraItem key={extra.name} slug={slug} extra={extra} />
        ))}
      </ul>
    </section>
  );
}

interface ExtraItemProps {
  slug: string;
  extra: ChapterExtraSummary;
}

function ExtraItem({ slug, extra }: ExtraItemProps) {
  const [open, setOpen] = useState(false);

  const {
    data: content,
    isLoading,
    error,
    refetch,
  } = useQuery({
    queryKey: ['chapter-extra', slug, extra.name],
    queryFn: () => api.chapterExtra(slug, extra.name),
    enabled: open,
    staleTime: 5 * 60_000,
  });

  return (
    <li className="card overflow-hidden">
      <button
        type="button"
        onClick={() => setOpen((v) => !v)}
        aria-expanded={open}
        className={cn(
          'w-full flex items-center gap-2 px-4 py-3 text-left transition-colors',
          'hover:bg-ink-50 dark:hover:bg-ink-800/40',
          open && 'bg-ink-50 dark:bg-ink-800/30'
        )}
      >
        {open ? (
          <ChevronDown className="w-4 h-4 flex-none text-accent-500" />
        ) : (
          <ChevronRight className="w-4 h-4 flex-none text-ink-400" />
        )}
        <span className="font-medium text-sm text-ink-900 dark:text-ink-100 flex-1 truncate">
          {extra.title}
        </span>
        {extra.extends && (
          <span className="hidden sm:inline-flex items-center text-[11px] font-mono px-1.5 py-0.5 rounded bg-accent-100 dark:bg-accent-900/30 text-accent-700 dark:text-accent-300">
            extiende §{extra.extends}
          </span>
        )}
        {extra.mtime && (
          <span className="hidden md:inline-flex items-center gap-1 text-[11px] text-ink-500 dark:text-ink-400">
            <Clock className="w-3 h-3" />
            {new Date(extra.mtime * 1000).toLocaleDateString('es-CO', {
              year: 'numeric',
              month: 'short',
              day: 'numeric',
            })}
          </span>
        )}
      </button>

      {open && (
        <div className="border-t border-ink-200 dark:border-ink-800 px-4 sm:px-6 py-5">
          {isLoading && (
            <div className="space-y-2">
              <Skeleton className="h-4 w-3/4" />
              <Skeleton className="h-4 w-full" />
              <Skeleton className="h-4 w-5/6" />
              <Skeleton className="h-4 w-2/3" />
            </div>
          )}
          {error && (
            <ErrorBox error={error} retry={() => refetch()} />
          )}
          {content && !isLoading && !error && (
            <div className="grid lg:grid-cols-[1fr_220px] gap-6">
              <article className="min-w-0">
                <HtmlContent html={content.html} />
              </article>
              {content.toc && content.toc.length > 0 && (
                <aside className="hidden lg:block">
                  <div className="sticky top-[5.5rem] max-h-[calc(100vh-7rem)] overflow-y-auto">
                    <div className="text-[11px] font-semibold uppercase tracking-wider text-ink-500 dark:text-ink-400 mb-2">
                      Secciones
                    </div>
                    <ul className="space-y-0.5 text-xs">
                      {content.toc.map((t, i) => (
                        <li
                          key={i}
                          style={{ paddingLeft: (t.level - 1) * 8 }}
                        >
                          <a
                            href={`#${t.anchor}`}
                            className="block px-2 py-1 rounded text-ink-600 dark:text-ink-400 hover:bg-ink-100 dark:hover:bg-ink-800/50 hover:text-ink-900 dark:hover:text-ink-100 truncate"
                          >
                            {t.title}
                          </a>
                        </li>
                      ))}
                    </ul>
                  </div>
                </aside>
              )}
            </div>
          )}
        </div>
      )}
    </li>
  );
}
