import { Link } from 'react-router-dom';
import { ArrowRight, CheckCircle2, AlertCircle, Circle, XCircle } from 'lucide-react';
import { Case } from '../types';
import { cn } from '../lib/cn';

interface CaseCardProps {
  c: Case;
  highlightQuery?: string;
}

const NIVEL_LABELS: Record<number, { name: string; cls: string }> = {
  0: { name: 'Null', cls: 'bg-ink-200 dark:bg-ink-800 text-ink-600 dark:text-ink-400' },
  1: { name: 'Trend', cls: 'bg-scholar-100 dark:bg-scholar-900/30 text-scholar-700 dark:text-scholar-300' },
  2: { name: 'Suggestive', cls: 'bg-warning/15 text-warning' },
  3: { name: 'Weak', cls: 'bg-accent-100 dark:bg-accent-900/30 text-accent-700 dark:text-accent-300' },
  4: { name: 'Strong', cls: 'bg-success/15 text-success' },
};

function statusIcon(c: Case) {
  if (c.metrics.overall_pass) return CheckCircle2;
  if (c.metrics.nivel === 4) return AlertCircle; // strong sin gate
  if (c.metrics.nivel === 0) return XCircle;
  return Circle;
}

function statusColor(c: Case): string {
  if (c.metrics.overall_pass) return 'text-success';
  if (c.metrics.nivel === 4) return 'text-warning';
  if ((c.metrics.nivel ?? 0) >= 2) return 'text-accent-500';
  if ((c.metrics.nivel ?? 0) === 0) return 'text-ink-400';
  return 'text-scholar-500';
}

export default function CaseCard({ c }: CaseCardProps) {
  const nivelInfo = c.metrics.nivel != null ? NIVEL_LABELS[c.metrics.nivel] : null;
  const Status = statusIcon(c);
  const isFalsacion = c.case_id.startsWith('06_') || c.case_id.startsWith('07_') || c.case_id.startsWith('08_');

  return (
    <Link
      to={`/casos/${c.case_id}`}
      className="card card-hover p-5 group block relative"
    >
      <div className="flex items-start justify-between gap-3 mb-2">
        <div className="flex items-center gap-2.5 min-w-0">
          <span className="font-mono text-[10px] font-semibold px-2 py-1 rounded-md bg-ink-100 dark:bg-ink-800 text-ink-600 dark:text-ink-300 flex-none">
            #{c.case_num != null ? String(c.case_num).padStart(2, '0') : '—'}
          </span>
          <Status className={cn('w-4 h-4 flex-none', statusColor(c))} />
        </div>
        <ArrowRight className="w-4 h-4 text-ink-300 dark:text-ink-700 group-hover:text-accent-500 group-hover:translate-x-0.5 transition-all flex-none" />
      </div>

      <h3 className="font-semibold text-base leading-tight mb-1 text-ink-900 dark:text-ink-100 line-clamp-2">
        {c.title}
      </h3>
      <p className="text-xs text-ink-500 dark:text-ink-400 font-mono truncate mb-3">
        {c.case_name}
      </p>

      <div className="grid grid-cols-3 gap-2 pt-3 border-t border-ink-100 dark:border-ink-800/60">
        <Stat
          label="EDI"
          value={
            c.metrics.edi != null ? c.metrics.edi.toFixed(3) : '—'
          }
          accent={
            c.metrics.edi != null
              ? c.metrics.edi >= 0.3
                ? 'success'
                : c.metrics.edi >= 0.1
                ? 'accent'
                : c.metrics.edi >= 0
                ? 'scholar'
                : 'muted'
              : 'muted'
          }
        />
        <Stat
          label="p"
          value={c.metrics.pvalue != null ? c.metrics.pvalue.toFixed(3) : '—'}
          accent={
            c.metrics.pvalue != null && c.metrics.pvalue < 0.05 ? 'success' : 'muted'
          }
        />
        <Stat
          label="CR"
          value={c.metrics.cr != null ? c.metrics.cr.toFixed(2) : '—'}
          accent="muted"
        />
      </div>

      <div className="flex items-center gap-1.5 mt-3 flex-wrap">
        {nivelInfo && (
          <span className={cn('badge', nivelInfo.cls)}>
            Nivel {c.metrics.nivel} · {nivelInfo.name}
          </span>
        )}
        {c.metrics.overall_pass && (
          <span className="badge-success">overall_pass</span>
        )}
        {isFalsacion && (
          <span className="badge-neutral">Falsación</span>
        )}
      </div>
    </Link>
  );
}

function Stat({
  label,
  value,
  accent,
}: {
  label: string;
  value: string;
  accent: 'success' | 'accent' | 'scholar' | 'muted';
}) {
  const colors = {
    success: 'text-success',
    accent: 'text-accent-600 dark:text-accent-400',
    scholar: 'text-scholar-600 dark:text-scholar-400',
    muted: 'text-ink-500 dark:text-ink-400',
  }[accent];
  return (
    <div className="text-center">
      <div className="text-[10px] uppercase tracking-wider text-ink-500 dark:text-ink-500 font-medium">
        {label}
      </div>
      <div className={cn('font-mono text-sm font-semibold tabular-nums mt-0.5', colors)}>
        {value}
      </div>
    </div>
  );
}
