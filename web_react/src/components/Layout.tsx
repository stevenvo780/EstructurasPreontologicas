import { Outlet, NavLink, useLocation } from 'react-router-dom';
import {
  BookOpen,
  LayoutDashboard,
  FlaskConical,
  Folders,
  ShieldCheck,
  BookMarked,
  Sun,
  Moon,
  Search,
  Github,
  Sparkles,
  Menu,
  X,
} from 'lucide-react';
import { useTheme } from '../hooks/useTheme';
import { cn } from '../lib/cn';
import { useState, useEffect } from 'react';
import CommandPalette from './CommandPalette';

interface NavItem {
  to: string;
  label: string;
  icon: React.ComponentType<{ className?: string }>;
  end?: boolean;
}

const NAV: NavItem[] = [
  { to: '/', label: 'Resumen', icon: LayoutDashboard, end: true },
  { to: '/tesis', label: 'Manuscrito', icon: BookOpen },
  { to: '/casos', label: 'Casos EDI', icon: FlaskConical },
  { to: '/capitulos', label: 'Capítulos', icon: Folders },
  { to: '/bibliografia', label: 'Bibliografía', icon: BookMarked },
  { to: '/st', label: 'Validación ST', icon: ShieldCheck },
];

export default function Layout() {
  const { theme, toggleTheme } = useTheme();
  const location = useLocation();
  const [paletteOpen, setPaletteOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 8);
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
    return () => window.removeEventListener('scroll', onScroll);
  }, []);

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault();
        setPaletteOpen((o) => !o);
      }
      if (e.key === 'Escape' && mobileMenuOpen) {
        setMobileMenuOpen(false);
      }
    };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [mobileMenuOpen]);

  // Cerrar menú móvil + scroll a top en cambio de ruta
  useEffect(() => {
    setMobileMenuOpen(false);
    if (!location.hash) {
      window.scrollTo({ top: 0, behavior: 'instant' });
    }
  }, [location.pathname]);

  // Bloquear scroll cuando el drawer móvil está abierto
  useEffect(() => {
    document.body.style.overflow = mobileMenuOpen ? 'hidden' : '';
    return () => {
      document.body.style.overflow = '';
    };
  }, [mobileMenuOpen]);

  return (
    <div className="min-h-screen flex flex-col">
      {/* Header */}
      <header
        className={cn(
          'sticky top-0 z-40 transition-all duration-200',
          scrolled
            ? 'glass shadow-sm'
            : 'bg-white/40 dark:bg-ink-950/40 backdrop-blur-sm border-b border-transparent'
        )}
      >
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16 gap-3">
            <NavLink
              to="/"
              className="flex items-center gap-2.5 group min-w-0"
              aria-label="Inicio"
            >
              <div className="relative flex-none">
                <div className="w-9 h-9 rounded-lg bg-gradient-to-br from-accent-500 to-accent-700 flex items-center justify-center shadow-md group-hover:shadow-lg transition-shadow">
                  <Sparkles className="w-5 h-5 text-white" />
                </div>
                <div className="absolute -inset-1 rounded-lg bg-accent-500/20 blur-sm opacity-0 group-hover:opacity-100 transition-opacity" />
              </div>
              <div className="hidden sm:block min-w-0">
                <div className="font-semibold text-sm tracking-tight truncate">
                  Estructuras Pre-Ontológicas
                </div>
                <div className="text-[10.5px] font-medium text-ink-500 dark:text-ink-400 -mt-0.5 truncate">
                  Irrealismo operativo · EDI multidominio
                </div>
              </div>
            </NavLink>

            {/* Nav desktop (≥xl) */}
            <nav className="hidden xl:flex items-center gap-1">
              {NAV.map((item) => (
                <NavLink
                  key={item.to}
                  to={item.to}
                  end={item.end}
                  className={({ isActive }) =>
                    cn(
                      'flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-sm font-medium transition-colors',
                      isActive
                        ? 'bg-accent-100 dark:bg-accent-900/30 text-accent-700 dark:text-accent-300'
                        : 'text-ink-600 dark:text-ink-300 hover:bg-ink-100 dark:hover:bg-ink-800/50 hover:text-ink-900 dark:hover:text-ink-100'
                    )
                  }
                >
                  <item.icon className="w-4 h-4" />
                  <span>{item.label}</span>
                </NavLink>
              ))}
            </nav>

            <div className="flex items-center gap-1.5">
              <button
                onClick={() => setPaletteOpen(true)}
                className="hidden md:flex items-center gap-2 px-3 py-1.5 rounded-lg border border-ink-300 dark:border-ink-700 text-sm text-ink-500 dark:text-ink-400 hover:border-accent-400 hover:text-accent-600 dark:hover:text-accent-400 transition-colors"
                aria-label="Buscar"
              >
                <Search className="w-3.5 h-3.5" />
                <span className="hidden lg:inline">Buscar</span>
                <kbd className="hidden lg:inline-flex items-center gap-0.5 px-1.5 py-0.5 rounded text-[10px] bg-ink-100 dark:bg-ink-800 text-ink-500 dark:text-ink-400 font-mono">
                  ⌘K
                </kbd>
              </button>
              <button
                onClick={() => setPaletteOpen(true)}
                className="md:hidden btn-ghost !p-2"
                aria-label="Buscar"
              >
                <Search className="w-4 h-4" />
              </button>
              <button
                onClick={toggleTheme}
                className="btn-ghost !p-2"
                aria-label="Cambiar tema"
                title={theme === 'dark' ? 'Modo claro' : 'Modo oscuro'}
              >
                {theme === 'dark' ? (
                  <Sun className="w-4 h-4" />
                ) : (
                  <Moon className="w-4 h-4" />
                )}
              </button>
              <a
                href="https://github.com/stevenvo780/EstructurasPreontologicas"
                target="_blank"
                rel="noreferrer"
                className="btn-ghost !p-2 hidden sm:inline-flex"
                aria-label="Repositorio en GitHub"
                title="GitHub"
              >
                <Github className="w-4 h-4" />
              </a>

              {/* Toggle drawer móvil/tablet (<xl) */}
              <button
                onClick={() => setMobileMenuOpen((o) => !o)}
                className="xl:hidden btn-ghost !p-2"
                aria-label={mobileMenuOpen ? 'Cerrar menú' : 'Abrir menú'}
                aria-expanded={mobileMenuOpen}
              >
                {mobileMenuOpen ? (
                  <X className="w-5 h-5" />
                ) : (
                  <Menu className="w-5 h-5" />
                )}
              </button>
            </div>
          </div>
        </div>

        {/* Drawer móvil/tablet — overlay full screen */}
        <div
          className={cn(
            'xl:hidden fixed inset-0 z-30 transition-all duration-200',
            mobileMenuOpen
              ? 'opacity-100 pointer-events-auto'
              : 'opacity-0 pointer-events-none'
          )}
        >
          <div
            className="absolute inset-0 bg-ink-950/40 backdrop-blur-sm"
            onClick={() => setMobileMenuOpen(false)}
            aria-hidden
          />
          <div
            className={cn(
              'absolute right-0 top-16 bottom-0 w-full max-w-sm bg-white dark:bg-ink-950 shadow-2xl border-l border-ink-200 dark:border-ink-800 overflow-y-auto transition-transform duration-200',
              mobileMenuOpen ? 'translate-x-0' : 'translate-x-full'
            )}
          >
            <nav className="p-3">
              <div className="text-[10px] uppercase tracking-wider font-semibold text-ink-500 dark:text-ink-400 px-3 pt-2 pb-1">
                Navegación
              </div>
              {NAV.map((item) => (
                <NavLink
                  key={item.to}
                  to={item.to}
                  end={item.end}
                  className={({ isActive }) =>
                    cn(
                      'flex items-center gap-3 px-3 py-3 rounded-lg text-sm font-medium transition-colors mb-0.5',
                      isActive
                        ? 'bg-accent-100 dark:bg-accent-900/30 text-accent-700 dark:text-accent-300'
                        : 'text-ink-700 dark:text-ink-200 hover:bg-ink-100 dark:hover:bg-ink-800/50'
                    )
                  }
                >
                  <item.icon className="w-4.5 h-4.5 flex-none" />
                  <span>{item.label}</span>
                </NavLink>
              ))}

              <div className="mt-4 pt-3 border-t border-ink-200 dark:border-ink-800 px-3 space-y-2">
                <a
                  href="https://github.com/stevenvo780/EstructurasPreontologicas"
                  target="_blank"
                  rel="noreferrer"
                  className="flex items-center gap-3 py-2 text-sm text-ink-600 dark:text-ink-400 hover:text-accent-600 dark:hover:text-accent-400"
                >
                  <Github className="w-4 h-4" />
                  <span>Repositorio en GitHub</span>
                </a>
              </div>
            </nav>
          </div>
        </div>
      </header>

      <main className="flex-1">
        <Outlet />
      </main>

      <footer className="mt-16 border-t border-ink-200 dark:border-ink-800 bg-white/50 dark:bg-ink-950/50">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-8">
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-6 text-sm">
            <div>
              <div className="font-semibold mb-2 text-ink-900 dark:text-ink-100">
                Tesis doctoral
              </div>
              <p className="text-ink-600 dark:text-ink-400 leading-relaxed">
                Jacob Agudelo (concepto y dirección) · Steven Vallejo (técnica) ·
                Universidad de Antioquia.
              </p>
            </div>
            <div>
              <div className="font-semibold mb-2 text-ink-900 dark:text-ink-100">
                Fuente de verdad
              </div>
              <ul className="space-y-1 text-ink-600 dark:text-ink-400">
                <li>
                  <code className="text-xs">09-simulaciones-edi/*/outputs/metrics.json</code>
                </li>
                <li>
                  <code className="text-xs">TesisFinal/Tesis.md</code>
                </li>
              </ul>
            </div>
            <div>
              <div className="font-semibold mb-2 text-ink-900 dark:text-ink-100">
                Recursos
              </div>
              <ul className="space-y-1">
                <li>
                  <a
                    href="https://github.com/stevenvo780/EstructurasPreontologicas"
                    className="text-accent-600 dark:text-accent-400 hover:underline"
                  >
                    Repositorio GitHub
                  </a>
                </li>
                <li>
                  <NavLink to="/about" className="text-ink-600 dark:text-ink-400 hover:text-accent-600 dark:hover:text-accent-400">
                    Sobre el proyecto
                  </NavLink>
                </li>
              </ul>
            </div>
          </div>
          <div className="mt-6 pt-4 border-t border-ink-200/60 dark:border-ink-800 text-xs text-ink-500 dark:text-ink-500 text-center">
            Versión integral defendible · Fecha de cierre conceptual: 2026-04-29
          </div>
        </div>
      </footer>

      <CommandPalette open={paletteOpen} onClose={() => setPaletteOpen(false)} />
    </div>
  );
}
