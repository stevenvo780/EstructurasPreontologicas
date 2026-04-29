import { useQuery } from '@tanstack/react-query';
import { useMemo, useState } from 'react';
import { Search, Filter, SortAsc, X, FlaskConical } from 'lucide-react';
import { api } from '../lib/api';
import { PageLoading, ErrorBox } from '../components/Loading';
import CaseCard from '../components/CaseCard';
import { Case } from '../types';
import { cn } from '../lib/cn';

type SortBy = 'edi-desc' | 'edi-asc' | 'p-asc' | 'case-num';
type FilterCat = 'all' | 'strong' | 'weak' | 'suggestive' | 'trend' | 'null' | 'falsified';

export default function Cases() {
  const { data: cases, isLoading, error } = useQuery({
    queryKey: ['cases'],
    queryFn: api.cases,
  });

  const [query, setQuery] = useState('');
  const [filter, setFilter] = useState<FilterCat>('all');
  const [sortBy, setSortBy] = useState<SortBy>('edi-desc');
  const [onlyPass, setOnlyPass] = useState(false);

  const filtered = useMemo(() => {
    if (!cases) return [];
    let out = [...cases];
    if (filter !== 'all') {
      out = out.filter((c) => c.metrics.category.toLowerCase() === filter);
    }
    if (onlyPass) {
      out = out.filter((c) => c.metrics.overall_pass);
    }
    if (query.trim()) {
      const q = query.toLowerCase();
      out = out.filter(
        (c) =>
          c.title.toLowerCase().includes(q) ||
          c.case_name.toLowerCase().includes(q) ||
          c.case_id.toLowerCase().includes(q)
      );
    }
    out.sort((a, b) => {
      switch (sortBy) {
        case 'edi-desc':
          return (b.metrics.edi ?? -Infinity) - (a.metrics.edi ?? -Infinity);
        case 'edi-asc':
          return (a.metrics.edi ?? Infinity) - (b.metrics.edi ?? Infinity);
        case 'p-asc':
          return (a.metrics.pvalue ?? Infinity) - (b.metrics.pvalue ?? Infinity);
        case 'case-num':
          return (a.case_num ?? 999) - (b.case_num ?? 999);
      }
    });
    return out;
  }, [cases, filter, onlyPass, query, sortBy]);

  const counts = useMemo(() => {
    const c = cases ?? [];
    return {
      total: c.length,
      strong: c.filter((x) => x.metrics.category.toLowerCase() === 'strong').length,
      weak: c.filter((x) => x.metrics.category.toLowerCase() === 'weak').length,
      suggestive: c.filter((x) => x.metrics.category.toLowerCase() === 'suggestive').length,
      trend: c.filter((x) => x.metrics.category.toLowerCase() === 'trend').length,
      null: c.filter((x) => x.metrics.category.toLowerCase() === 'null').length,
      falsified: c.filter((x) => x.metrics.category.toLowerCase() === 'falsified').length,
      pass: c.filter((x) => x.metrics.overall_pass).length,
    };
  }, [cases]);

  if (isLoading) return <PageLoading label="Cargando corpus EDI…" />;
  if (error) return <div className="mx-auto max-w-7xl p-8"><ErrorBox error={error} /></div>;

  return (
    <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-8 lg:py-10">
      <header className="mb-8">
        <div className="flex items-center gap-2 text-xs uppercase tracking-wider text-ink-500 dark:text-ink-400 mb-2">
          <FlaskConical className="w-3.5 h-3.5" />
          Corpus EDI
        </div>
        <h1 className="font-serif text-3xl md:text-4xl font-semibold tracking-tight text-balance">
          Casos del corpus
        </h1>
        <p className="mt-2 text-ink-600 dark:text-ink-400 max-w-3xl">
          Cartografía empírica del paisaje de emergencia. Cada caso instancia los cuatro invariantes
          ontológicos: sustrato material, acoplamiento dinámico, atractor empírico, cierre operativo κ.
        </p>
      </header>

      {/* Filtros */}
      <div className="card p-4 mb-6 sticky top-[4.25rem] z-30 backdrop-blur-md bg-white/85 dark:bg-ink-900/85">
        <div className="flex flex-col lg:flex-row gap-3 items-stretch lg:items-center">
          {/* Search */}
          <div className="relative flex-1 min-w-0">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-3.5 h-3.5 text-ink-400" />
            <input
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Buscar por título, dominio o ID…"
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

          {/* Sort */}
          <div className="flex items-center gap-2">
            <SortAsc className="w-3.5 h-3.5 text-ink-400" />
            <select
              value={sortBy}
              onChange={(e) => setSortBy(e.target.value as SortBy)}
              className="input !w-auto !py-1.5"
            >
              <option value="edi-desc">EDI ↓ (mayor)</option>
              <option value="edi-asc">EDI ↑ (menor)</option>
              <option value="p-asc">p-value ↑ (más significativo)</option>
              <option value="case-num">Número de caso</option>
            </select>
          </div>

          <label className="flex items-center gap-2 text-sm text-ink-700 dark:text-ink-300 cursor-pointer select-none">
            <input
              type="checkbox"
              checked={onlyPass}
              onChange={(e) => setOnlyPass(e.target.checked)}
              className="w-4 h-4 rounded accent-accent-500"
            />
            Solo overall_pass
          </label>
        </div>

        {/* Pills de categoría */}
        <div className="flex items-center gap-1.5 mt-3 flex-wrap">
          <Filter className="w-3.5 h-3.5 text-ink-400" />
          <FilterPill active={filter === 'all'} onClick={() => setFilter('all')}>
            Todos · {counts.total}
          </FilterPill>
          <FilterPill active={filter === 'strong'} onClick={() => setFilter('strong')} accent="success">
            Strong · {counts.strong}
          </FilterPill>
          <FilterPill active={filter === 'weak'} onClick={() => setFilter('weak')} accent="accent">
            Weak · {counts.weak}
          </FilterPill>
          <FilterPill active={filter === 'suggestive'} onClick={() => setFilter('suggestive')} accent="warning">
            Suggestive · {counts.suggestive}
          </FilterPill>
          <FilterPill active={filter === 'trend'} onClick={() => setFilter('trend')} accent="scholar">
            Trend · {counts.trend}
          </FilterPill>
          <FilterPill active={filter === 'null'} onClick={() => setFilter('null')}>
            Null · {counts.null}
          </FilterPill>
          {counts.falsified > 0 && (
            <FilterPill active={filter === 'falsified'} onClick={() => setFilter('falsified')} accent="danger">
              Falsación · {counts.falsified}
            </FilterPill>
          )}
        </div>
      </div>

      {/* Resultados */}
      {filtered.length === 0 ? (
        <div className="card p-12 text-center">
          <FlaskConical className="w-10 h-10 mx-auto text-ink-300 dark:text-ink-700 mb-3" />
          <h3 className="font-semibold mb-1">Sin resultados</h3>
          <p className="text-sm text-ink-500 dark:text-ink-400">
            Ajusta filtros o limpia la búsqueda.
          </p>
        </div>
      ) : (
        <>
          <div className="text-sm text-ink-500 dark:text-ink-400 mb-3">
            Mostrando {filtered.length} de {counts.total} casos
          </div>
          <div className="grid sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
            {filtered.map((c) => (
              <CaseCard key={c.case_id} c={c as Case} />
            ))}
          </div>
        </>
      )}
    </div>
  );
}

function FilterPill({
  active,
  children,
  onClick,
  accent,
}: {
  active: boolean;
  children: React.ReactNode;
  onClick: () => void;
  accent?: 'success' | 'warning' | 'danger' | 'accent' | 'scholar';
}) {
  const accentMap: Record<string, string> = {
    success: 'data-[active=true]:bg-success data-[active=true]:text-white data-[active=true]:border-success',
    warning: 'data-[active=true]:bg-warning data-[active=true]:text-white data-[active=true]:border-warning',
    danger: 'data-[active=true]:bg-danger data-[active=true]:text-white data-[active=true]:border-danger',
    accent: 'data-[active=true]:bg-accent-500 data-[active=true]:text-white data-[active=true]:border-accent-500',
    scholar: 'data-[active=true]:bg-scholar-600 data-[active=true]:text-white data-[active=true]:border-scholar-600',
  };
  return (
    <button
      onClick={onClick}
      data-active={active}
      className={cn(
        'px-3 py-1 rounded-full text-xs font-medium border transition-colors',
        'border-ink-200 dark:border-ink-700 text-ink-700 dark:text-ink-300',
        'data-[active=true]:bg-ink-900 data-[active=true]:text-white data-[active=true]:border-ink-900',
        'dark:data-[active=true]:bg-ink-100 dark:data-[active=true]:text-ink-900',
        'hover:border-ink-400 dark:hover:border-ink-600',
        accent && accentMap[accent]
      )}
    >
      {children}
    </button>
  );
}
