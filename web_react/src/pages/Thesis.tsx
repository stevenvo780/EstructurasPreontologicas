import { useQuery } from '@tanstack/react-query';
import { useEffect, useMemo, useState, useRef } from 'react';
import {
  BookOpen,
  PanelLeftClose,
  PanelLeft,
  ArrowUp,
  Maximize2,
  Minimize2,
  Search,
  Bookmark,
  ChevronRight,
  ChevronDown,
  X,
} from 'lucide-react';
import { api } from '../lib/api';
import { PageLoading, ErrorBox } from '../components/Loading';
import HtmlContent from '../components/HtmlContent';
import { TocItem } from '../types';
import { cn } from '../lib/cn';

const TOC_STORAGE = 'epo-thesis-toc-open';
const READING_STORAGE = 'epo-thesis-reading';

export default function Thesis() {
  const { data, isLoading, error } = useQuery({
    queryKey: ['thesis'],
    queryFn: api.thesis,
  });

  // Persistencia de preferencias
  const [tocOpen, setTocOpen] = useState<boolean>(() => {
    if (typeof window === 'undefined') return true;
    const stored = localStorage.getItem(TOC_STORAGE);
    return stored === null ? true : stored === '1';
  });
  const [readingMode, setReadingMode] = useState<boolean>(() => {
    if (typeof window === 'undefined') return false;
    return localStorage.getItem(READING_STORAGE) === '1';
  });
  const [tocQuery, setTocQuery] = useState('');
  const [activeAnchor, setActiveAnchor] = useState<string | null>(null);
  const contentRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    localStorage.setItem(TOC_STORAGE, tocOpen ? '1' : '0');
  }, [tocOpen]);
  useEffect(() => {
    localStorage.setItem(READING_STORAGE, readingMode ? '1' : '0');
  }, [readingMode]);

  // En modo lectura, ocultamos el TOC automáticamente
  const effectiveTocOpen = tocOpen && !readingMode;

  const filteredToc = useMemo(() => {
    if (!data?.toc) return [];
    if (!tocQuery.trim()) return data.toc;
    const q = tocQuery.toLowerCase();
    return data.toc.filter((t) => t.title.toLowerCase().includes(q));
  }, [data?.toc, tocQuery]);

  // Resaltar sección activa al scrollear
  useEffect(() => {
    if (!data?.toc || !contentRef.current) return;
    const headings = data.toc
      .map((t) => document.getElementById(t.anchor))
      .filter(Boolean) as HTMLElement[];
    const observer = new IntersectionObserver(
      (entries) => {
        const visible = entries
          .filter((e) => e.isIntersecting)
          .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
        if (visible[0]) setActiveAnchor(visible[0].target.id);
      },
      { rootMargin: '-15% 0% -75% 0%' }
    );
    headings.forEach((h) => observer.observe(h));
    return () => observer.disconnect();
  }, [data?.toc, data?.html]);

  // Atajos de teclado
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      const target = e.target as HTMLElement | null;
      if (target?.tagName === 'INPUT' || target?.tagName === 'TEXTAREA') return;
      if (e.key === '\\' || (e.key === 'b' && (e.ctrlKey || e.metaKey))) {
        e.preventDefault();
        setTocOpen((v) => !v);
      } else if (e.key === 'r' && !e.ctrlKey && !e.metaKey && !e.altKey) {
        setReadingMode((v) => !v);
      }
    };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, []);

  if (isLoading) return <PageLoading label="Cargando manuscrito completo…" />;
  if (error || !data)
    return (
      <div className="mx-auto max-w-5xl p-8">
        <ErrorBox error={error ?? new Error('Sin datos')} />
      </div>
    );

  const linesText = data.line_count ? `${data.line_count.toLocaleString('es')} líneas` : '';
  const wordsText = data.word_count ? `${data.word_count.toLocaleString('es')} palabras` : '';

  return (
    <div className={cn('relative', readingMode && 'reading-mode')}>
      {/* Topbar de la tesis */}
      <div className="sticky top-16 z-30 border-b border-ink-200 dark:border-ink-800 bg-white/85 dark:bg-ink-950/85 backdrop-blur-md">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-2.5 flex items-center justify-between gap-3">
          <div className="flex items-center gap-2 min-w-0">
            <button
              onClick={() => setTocOpen((v) => !v)}
              className="btn-ghost !p-1.5"
              aria-label={effectiveTocOpen ? 'Ocultar índice' : 'Mostrar índice'}
              title={`${effectiveTocOpen ? 'Ocultar' : 'Mostrar'} índice (\\)`}
            >
              {effectiveTocOpen ? (
                <PanelLeftClose className="w-4 h-4" />
              ) : (
                <PanelLeft className="w-4 h-4" />
              )}
            </button>
            <BookOpen className="w-4 h-4 text-accent-500 flex-none" />
            <div className="min-w-0">
              <div className="text-sm font-semibold truncate">Manuscrito doctoral</div>
              <div className="text-[10.5px] text-ink-500 dark:text-ink-400 truncate">
                {linesText}
                {wordsText && linesText ? ' · ' : ''}
                {wordsText}
              </div>
            </div>
          </div>
          <div className="flex items-center gap-1.5">
            <button
              onClick={() => setReadingMode((v) => !v)}
              className={cn(
                'btn-ghost !text-xs !py-1.5',
                readingMode &&
                  '!bg-accent-100 dark:!bg-accent-900/30 !text-accent-700 dark:!text-accent-300'
              )}
              title={readingMode ? 'Salir de modo lectura (R)' : 'Modo lectura (R)'}
            >
              {readingMode ? (
                <>
                  <Minimize2 className="w-3.5 h-3.5" />
                  <span className="hidden sm:inline">Salir lectura</span>
                </>
              ) : (
                <>
                  <Maximize2 className="w-3.5 h-3.5" />
                  <span className="hidden sm:inline">Lectura</span>
                </>
              )}
            </button>
            <button
              onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
              className="btn-ghost !p-1.5"
              title="Subir"
              aria-label="Volver arriba"
            >
              <ArrowUp className="w-4 h-4" />
            </button>
          </div>
        </div>
      </div>

      <div
        className={cn(
          'mx-auto px-4 sm:px-6 lg:px-8 py-6 transition-[grid-template-columns] duration-200',
          // Cuando cambia el grid, también cambia el max-width para mejor balance
          effectiveTocOpen
            ? 'max-w-7xl grid lg:grid-cols-[280px_minmax(0,1fr)] gap-6'
            : 'max-w-4xl grid grid-cols-1'
        )}
      >
        {/* TOC sidebar — escritorio */}
        {effectiveTocOpen && (
          <aside className="hidden lg:block">
            <div className="sticky top-[7.5rem] max-h-[calc(100vh-9rem)] overflow-y-auto">
              <div className="card p-4">
                <div className="flex items-center justify-between mb-3">
                  <h3 className="font-semibold text-sm flex items-center gap-1.5">
                    <Bookmark className="w-3.5 h-3.5 text-accent-500" />
                    Índice
                  </h3>
                  <button
                    onClick={() => setTocOpen(false)}
                    className="text-ink-400 hover:text-ink-700 dark:hover:text-ink-200"
                    title="Ocultar índice"
                    aria-label="Ocultar índice"
                  >
                    <PanelLeftClose className="w-3.5 h-3.5" />
                  </button>
                </div>
                <div className="relative mb-3">
                  <Search className="absolute left-2.5 top-1/2 -translate-y-1/2 w-3 h-3 text-ink-400" />
                  <input
                    type="text"
                    value={tocQuery}
                    onChange={(e) => setTocQuery(e.target.value)}
                    placeholder="Filtrar secciones…"
                    className="input !text-xs !py-1.5 pl-7"
                  />
                </div>
                <TocTree items={filteredToc} activeAnchor={activeAnchor} />
              </div>
            </div>
          </aside>
        )}

        {/* TOC drawer móvil/tablet */}
        {tocOpen && !readingMode && (
          <div
            className="lg:hidden fixed inset-0 z-40 animate-fade-in"
            onClick={() => setTocOpen(false)}
          >
            <div className="absolute inset-0 bg-ink-950/40 backdrop-blur-sm" />
            <div
              className="absolute left-0 top-0 bottom-0 w-[84vw] max-w-sm bg-white dark:bg-ink-950 shadow-2xl border-r border-ink-200 dark:border-ink-800 overflow-y-auto"
              onClick={(e) => e.stopPropagation()}
            >
              <div className="sticky top-0 bg-white dark:bg-ink-950 border-b border-ink-200 dark:border-ink-800 p-3 flex items-center justify-between">
                <h3 className="font-semibold text-sm flex items-center gap-1.5">
                  <Bookmark className="w-3.5 h-3.5 text-accent-500" />
                  Índice de la tesis
                </h3>
                <button
                  onClick={() => setTocOpen(false)}
                  className="btn-ghost !p-1"
                  aria-label="Cerrar"
                >
                  <X className="w-4 h-4" />
                </button>
              </div>
              <div className="p-3">
                <div className="relative mb-3">
                  <Search className="absolute left-2.5 top-1/2 -translate-y-1/2 w-3 h-3 text-ink-400" />
                  <input
                    type="text"
                    value={tocQuery}
                    onChange={(e) => setTocQuery(e.target.value)}
                    placeholder="Filtrar secciones…"
                    className="input !text-xs !py-1.5 pl-7"
                  />
                </div>
                <TocTree
                  items={filteredToc}
                  activeAnchor={activeAnchor}
                  onSelect={() => setTocOpen(false)}
                />
              </div>
            </div>
          </div>
        )}

        {/* Contenido */}
        <article ref={contentRef} className="min-w-0">
          <div
            className={cn(
              'card p-6 sm:p-8 lg:p-10 transition-all',
              readingMode && 'shadow-none border-transparent !bg-transparent !p-0'
            )}
          >
            <HtmlContent html={data.html} />
          </div>

          {/* Hint de atajos en pie */}
          <div className="mt-6 text-center text-[11px] text-ink-400 dark:text-ink-600">
            <kbd className="font-mono bg-ink-100 dark:bg-ink-800 px-1.5 py-0.5 rounded mr-1">\</kbd>
            ocultar/mostrar índice ·
            <kbd className="font-mono bg-ink-100 dark:bg-ink-800 px-1.5 py-0.5 rounded mx-1">R</kbd>
            modo lectura
          </div>
        </article>
      </div>
    </div>
  );
}

interface TocNode {
  item: TocItem;
  children: TocNode[];
}

function buildTree(items: TocItem[]): TocNode[] {
  const root: TocNode[] = [];
  const stack: TocNode[] = [];
  for (const item of items) {
    const node: TocNode = { item, children: [] };
    while (stack.length > 0 && stack[stack.length - 1].item.level >= item.level) {
      stack.pop();
    }
    if (stack.length === 0) {
      root.push(node);
    } else {
      stack[stack.length - 1].children.push(node);
    }
    stack.push(node);
  }
  return root;
}

function TocTree({
  items,
  activeAnchor,
  onSelect,
}: {
  items: TocItem[];
  activeAnchor: string | null;
  onSelect?: () => void;
}) {
  const tree = useMemo(() => buildTree(items), [items]);
  return (
    <ul className="space-y-0.5 text-sm">
      {tree.map((n, i) => (
        <TocNodeItem key={i} node={n} activeAnchor={activeAnchor} onSelect={onSelect} />
      ))}
    </ul>
  );
}

function TocNodeItem({
  node,
  activeAnchor,
  onSelect,
}: {
  node: TocNode;
  activeAnchor: string | null;
  onSelect?: () => void;
}) {
  const [open, setOpen] = useState(node.item.level <= 2);
  const isActive = activeAnchor === node.item.anchor;
  const hasChildren = node.children.length > 0;
  const indent = (node.item.level - 1) * 10;

  return (
    <li>
      <div
        className={cn(
          'flex items-center gap-1 group rounded-md transition-colors',
          isActive
            ? 'bg-accent-100 dark:bg-accent-900/30 text-accent-700 dark:text-accent-300'
            : 'hover:bg-ink-100 dark:hover:bg-ink-800/50 text-ink-700 dark:text-ink-300'
        )}
        style={{ paddingLeft: indent }}
      >
        {hasChildren ? (
          <button
            onClick={() => setOpen((o) => !o)}
            className="flex-none p-1 text-ink-400 hover:text-ink-700 dark:hover:text-ink-200"
            aria-label="Toggle"
          >
            {open ? <ChevronDown className="w-3 h-3" /> : <ChevronRight className="w-3 h-3" />}
          </button>
        ) : (
          <span className="w-5 flex-none" />
        )}
        <a
          href={`#${node.item.anchor}`}
          onClick={onSelect}
          className={cn(
            'flex-1 py-1 pr-2 text-xs leading-snug truncate',
            node.item.level === 1 && 'font-semibold',
            node.item.level === 2 && 'font-medium'
          )}
          title={node.item.title}
        >
          {node.item.title}
        </a>
      </div>
      {hasChildren && open && (
        <ul className="space-y-0.5">
          {node.children.map((c, i) => (
            <TocNodeItem key={i} node={c} activeAnchor={activeAnchor} onSelect={onSelect} />
          ))}
        </ul>
      )}
    </li>
  );
}
