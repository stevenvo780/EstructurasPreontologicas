import { useEffect, useRef, useState, useMemo } from 'react';
import { useNavigate } from 'react-router-dom';
import { useQuery } from '@tanstack/react-query';
import {
  Search,
  X,
  FlaskConical,
  Folders,
  BookOpen,
  ShieldCheck,
  LayoutDashboard,
  ArrowRight,
  Hash,
} from 'lucide-react';
import Fuse from 'fuse.js';
import { api } from '../lib/api';
import { cn } from '../lib/cn';

interface CommandPaletteProps {
  open: boolean;
  onClose: () => void;
}

interface SearchItem {
  id: string;
  label: string;
  sublabel?: string;
  category: 'page' | 'case' | 'chapter';
  href: string;
  icon: React.ComponentType<{ className?: string }>;
  edi?: number | null;
}

const STATIC_ITEMS: SearchItem[] = [
  {
    id: 'home',
    label: 'Resumen del corpus',
    sublabel: 'Dashboard principal',
    category: 'page',
    href: '/',
    icon: LayoutDashboard,
  },
  {
    id: 'tesis',
    label: 'Manuscrito completo',
    sublabel: 'Tesis ensamblada',
    category: 'page',
    href: '/tesis',
    icon: BookOpen,
  },
  {
    id: 'casos',
    label: 'Todos los casos EDI',
    sublabel: 'Corpus inter-dominio + inter-escala',
    category: 'page',
    href: '/casos',
    icon: FlaskConical,
  },
  {
    id: 'capitulos',
    label: 'Capítulos por carpeta',
    sublabel: 'Versiones de trabajo',
    category: 'page',
    href: '/capitulos',
    icon: Folders,
  },
  {
    id: 'st',
    label: 'Validación lógica ST',
    sublabel: 'Suite de pruebas formales',
    category: 'page',
    href: '/st',
    icon: ShieldCheck,
  },
];

export default function CommandPalette({ open, onClose }: CommandPaletteProps) {
  const navigate = useNavigate();
  const [query, setQuery] = useState('');
  const [activeIdx, setActiveIdx] = useState(0);
  const inputRef = useRef<HTMLInputElement>(null);

  const { data: cases = [] } = useQuery({
    queryKey: ['cases'],
    queryFn: api.cases,
    enabled: open,
  });
  const { data: chapters = [] } = useQuery({
    queryKey: ['chapters'],
    queryFn: api.chapters,
    enabled: open,
  });

  const items = useMemo<SearchItem[]>(() => {
    const caseItems: SearchItem[] = cases.map((c) => ({
      id: `case-${c.case_id}`,
      label: c.title,
      sublabel: `Caso ${c.case_num ?? '—'} · ${c.metrics.category}`,
      category: 'case',
      href: `/casos/${c.case_id}`,
      icon: FlaskConical,
      edi: c.metrics.edi,
    }));
    const chapterItems: SearchItem[] = chapters.map((ch) => ({
      id: `chapter-${ch.slug}`,
      label: ch.title,
      sublabel: `${ch.code} · ${ch.docs.length} docs`,
      category: 'chapter',
      href: `/capitulos/${ch.slug}`,
      icon: Folders,
    }));
    return [...STATIC_ITEMS, ...caseItems, ...chapterItems];
  }, [cases, chapters]);

  const fuse = useMemo(
    () =>
      new Fuse(items, {
        keys: ['label', 'sublabel'],
        threshold: 0.4,
        includeMatches: false,
      }),
    [items]
  );

  const filtered = useMemo(() => {
    if (!query.trim()) return items.slice(0, 12);
    return fuse
      .search(query)
      .slice(0, 16)
      .map((r) => r.item);
  }, [query, items, fuse]);

  useEffect(() => {
    if (open) {
      setQuery('');
      setActiveIdx(0);
      requestAnimationFrame(() => inputRef.current?.focus());
    }
  }, [open]);

  useEffect(() => {
    setActiveIdx(0);
  }, [query]);

  useEffect(() => {
    if (!open) return;
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        e.preventDefault();
        onClose();
      } else if (e.key === 'ArrowDown') {
        e.preventDefault();
        setActiveIdx((i) => Math.min(i + 1, filtered.length - 1));
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        setActiveIdx((i) => Math.max(i - 1, 0));
      } else if (e.key === 'Enter' && filtered[activeIdx]) {
        e.preventDefault();
        navigate(filtered[activeIdx].href);
        onClose();
      }
    };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [open, filtered, activeIdx, navigate, onClose]);

  if (!open) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-start justify-center pt-[15vh] px-4 animate-fade-in">
      <div
        className="absolute inset-0 bg-ink-950/40 backdrop-blur-sm"
        onClick={onClose}
        aria-hidden
      />
      <div className="relative w-full max-w-2xl rounded-2xl bg-white dark:bg-ink-900 shadow-2xl border border-ink-200 dark:border-ink-800 overflow-hidden animate-slide-in">
        <div className="flex items-center gap-3 px-4 py-3 border-b border-ink-200 dark:border-ink-800">
          <Search className="w-4 h-4 text-ink-400 flex-none" />
          <input
            ref={inputRef}
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Buscar casos, capítulos, secciones…"
            className="flex-1 bg-transparent text-sm focus:outline-none placeholder:text-ink-400"
          />
          <button onClick={onClose} className="text-ink-400 hover:text-ink-700 dark:hover:text-ink-200" aria-label="Cerrar">
            <X className="w-4 h-4" />
          </button>
        </div>
        <div className="max-h-[55vh] overflow-y-auto py-2">
          {filtered.length === 0 ? (
            <div className="px-4 py-6 text-sm text-ink-500 text-center">
              Sin resultados para «{query}»
            </div>
          ) : (
            filtered.map((item, idx) => (
              <button
                key={item.id}
                onClick={() => {
                  navigate(item.href);
                  onClose();
                }}
                onMouseEnter={() => setActiveIdx(idx)}
                className={cn(
                  'w-full flex items-center gap-3 px-4 py-2.5 text-left transition-colors',
                  idx === activeIdx
                    ? 'bg-accent-100 dark:bg-accent-900/20'
                    : 'hover:bg-ink-100/60 dark:hover:bg-ink-800/40'
                )}
              >
                <div
                  className={cn(
                    'flex-none w-8 h-8 rounded-lg flex items-center justify-center',
                    item.category === 'case'
                      ? 'bg-scholar-100 dark:bg-scholar-900/30 text-scholar-700 dark:text-scholar-300'
                      : item.category === 'chapter'
                      ? 'bg-accent-100 dark:bg-accent-900/30 text-accent-700 dark:text-accent-400'
                      : 'bg-ink-100 dark:bg-ink-800 text-ink-600 dark:text-ink-300'
                  )}
                >
                  <item.icon className="w-4 h-4" />
                </div>
                <div className="flex-1 min-w-0">
                  <div className="text-sm font-medium text-ink-900 dark:text-ink-100 truncate">
                    {item.label}
                  </div>
                  {item.sublabel && (
                    <div className="text-xs text-ink-500 dark:text-ink-400 truncate flex items-center gap-1.5">
                      <Hash className="w-3 h-3" />
                      {item.sublabel}
                      {item.edi !== undefined && item.edi !== null && (
                        <span className="ml-auto px-1.5 py-0.5 rounded bg-ink-100 dark:bg-ink-800 font-mono text-[10px]">
                          EDI {item.edi.toFixed(2)}
                        </span>
                      )}
                    </div>
                  )}
                </div>
                <ArrowRight
                  className={cn(
                    'w-3.5 h-3.5 flex-none transition-transform',
                    idx === activeIdx
                      ? 'text-accent-600 dark:text-accent-400 translate-x-0.5'
                      : 'text-ink-300 dark:text-ink-700'
                  )}
                />
              </button>
            ))
          )}
        </div>
        <div className="border-t border-ink-200 dark:border-ink-800 px-4 py-2 flex items-center justify-between text-xs text-ink-500">
          <div className="flex items-center gap-3">
            <span>
              <kbd className="font-mono bg-ink-100 dark:bg-ink-800 px-1.5 py-0.5 rounded">↑↓</kbd>{' '}
              navegar
            </span>
            <span>
              <kbd className="font-mono bg-ink-100 dark:bg-ink-800 px-1.5 py-0.5 rounded">↵</kbd>{' '}
              abrir
            </span>
            <span>
              <kbd className="font-mono bg-ink-100 dark:bg-ink-800 px-1.5 py-0.5 rounded">esc</kbd>{' '}
              cerrar
            </span>
          </div>
          <span>{filtered.length} resultados</span>
        </div>
      </div>
    </div>
  );
}
