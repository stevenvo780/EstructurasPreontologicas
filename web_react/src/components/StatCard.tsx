import { LucideIcon, TrendingUp, TrendingDown, Minus } from 'lucide-react';
import { cn } from '../lib/cn';

interface StatCardProps {
  label: string;
  value: string | number;
  hint?: string;
  icon?: LucideIcon;
  trend?: 'up' | 'down' | 'flat';
  accent?: 'default' | 'success' | 'warning' | 'danger';
}

export default function StatCard({
  label,
  value,
  hint,
  icon: Icon,
  trend,
  accent = 'default',
}: StatCardProps) {
  const accentStyles = {
    default: 'border-ink-200 dark:border-ink-800',
    success: 'border-success/30 bg-success/5',
    warning: 'border-warning/30 bg-warning/5',
    danger: 'border-danger/30 bg-danger/5',
  }[accent];

  const TrendIcon =
    trend === 'up' ? TrendingUp : trend === 'down' ? TrendingDown : Minus;

  return (
    <div
      className={cn(
        'card card-hover p-5 relative overflow-hidden group',
        accentStyles
      )}
    >
      {Icon && (
        <div className="absolute -top-2 -right-2 opacity-[0.04] group-hover:opacity-[0.07] transition-opacity">
          <Icon className="w-24 h-24" />
        </div>
      )}
      <div className="relative">
        <div className="flex items-center gap-2 text-xs uppercase tracking-wider text-ink-500 dark:text-ink-400 font-medium mb-1.5">
          {Icon && <Icon className="w-3.5 h-3.5" />}
          <span>{label}</span>
        </div>
        <div className="flex items-baseline gap-2">
          <span className="text-3xl font-semibold text-ink-900 dark:text-ink-100 tabular-nums">
            {value}
          </span>
          {trend && (
            <TrendIcon
              className={cn(
                'w-3.5 h-3.5',
                trend === 'up'
                  ? 'text-success'
                  : trend === 'down'
                  ? 'text-danger'
                  : 'text-ink-400'
              )}
            />
          )}
        </div>
        {hint && (
          <div className="mt-1.5 text-xs text-ink-500 dark:text-ink-400 leading-relaxed">
            {hint}
          </div>
        )}
      </div>
    </div>
  );
}
