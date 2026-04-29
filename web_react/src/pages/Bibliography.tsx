import { useQuery } from '@tanstack/react-query';
import { useState, useMemo } from 'react';
import { BookMarked, Search, X } from 'lucide-react';
import { api } from '../lib/api';
import { PageLoading, ErrorBox } from '../components/Loading';
import HtmlContent from '../components/HtmlContent';

export default function Bibliography() {
  const { data, isLoading, error } = useQuery({
    queryKey: ['chapter', 'bibliografia'],
    queryFn: () => api.chapter('07-bibliografia'),
  });

  const [query, setQuery] = useState('');

  const html = useMemo(() => {
    if (!data?.docs[0]) return '';
    if (!query.trim()) return data.docs[0].html;
    const q = query.toLowerCase();
    // Naive line-level filtering: parse HTML, keep only sections matching
    const parser = new DOMParser();
    const doc = parser.parseFromString(data.docs[0].html, 'text/html');
    const allLi = Array.from(doc.querySelectorAll('li, tr'));
    let matches = 0;
    allLi.forEach((el) => {
      const text = (el.textContent || '').toLowerCase();
      if (!text.includes(q)) {
        (el as HTMLElement).style.display = 'none';
      } else {
        matches++;
      }
    });
    return doc.body.innerHTML;
  }, [data, query]);

  if (isLoading) return <PageLoading label="Cargando bibliografía consolidada…" />;
  if (error) return <div className="mx-auto max-w-7xl p-8"><ErrorBox error={error} /></div>;

  return (
    <div className="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8 py-8 lg:py-10">
      <header className="mb-6">
        <div className="flex items-center gap-2 text-xs uppercase tracking-wider text-ink-500 dark:text-ink-400 mb-2">
          <BookMarked className="w-3.5 h-3.5" />
          Bibliografía consolidada
        </div>
        <h1 className="font-serif text-3xl md:text-4xl font-semibold tracking-tight">
          Aparato citacional
        </h1>
        <p className="mt-2 text-ink-600 dark:text-ink-400">
          Chicago author-date adaptado al manuscrito doctoral en español. ~157 entradas
          distribuidas en secciones temáticas (filosofía de la ciencia, causalidad, mecanicismo,
          fenomenología, ontología social, calibración estadística, dinámica no lineal y más).
        </p>
      </header>

      <div className="card p-3 mb-6 sticky top-[5rem] z-30 backdrop-blur-md bg-white/90 dark:bg-ink-900/90">
        <div className="relative">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-3.5 h-3.5 text-ink-400" />
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Buscar autor, año o título…"
            className="input pl-9 pr-9"
          />
          {query && (
            <button
              onClick={() => setQuery('')}
              className="absolute right-3 top-1/2 -translate-y-1/2 text-ink-400 hover:text-ink-700 dark:hover:text-ink-200"
            >
              <X className="w-3.5 h-3.5" />
            </button>
          )}
        </div>
      </div>

      <div className="card p-6 lg:p-8">
        <HtmlContent html={html} />
      </div>
    </div>
  );
}
