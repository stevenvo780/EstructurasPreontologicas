import { Loader2 } from 'lucide-react';

export function PageLoading({ label = 'Cargando datos…' }: { label?: string }) {
  return (
    <div className="flex flex-col items-center justify-center py-24 gap-3 text-ink-500 dark:text-ink-400">
      <Loader2 className="w-8 h-8 animate-spin text-accent-500" />
      <p className="text-sm">{label}</p>
    </div>
  );
}

export function Skeleton({ className = '' }: { className?: string }) {
  return (
    <div
      className={`animate-pulse-slow bg-ink-100 dark:bg-ink-800 rounded-lg ${className}`}
    />
  );
}

export function ErrorBox({ error, retry }: { error: unknown; retry?: () => void }) {
  const msg = error instanceof Error ? error.message : 'Error desconocido';
  return (
    <div className="rounded-xl border border-danger/30 bg-danger/5 p-6 text-sm">
      <div className="font-semibold text-danger mb-1">No se pudieron cargar los datos</div>
      <div className="text-ink-600 dark:text-ink-400 font-mono text-xs">{msg}</div>
      {retry && (
        <button onClick={retry} className="btn-outline mt-3">
          Reintentar
        </button>
      )}
    </div>
  );
}
