import { useQuery } from '@tanstack/react-query';
import { Link } from 'react-router-dom';
import {
  Activity,
  CheckCircle2,
  XCircle,
  TrendingUp,
  BookOpen,
  ArrowRight,
  FlaskConical,
  Layers,
  Microscope,
  Telescope,
  ShieldCheck,
  Database,
  Scale,
  FileText,
} from 'lucide-react';
import {
  BarChart,
  Bar,
  ResponsiveContainer,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  Cell,
  ScatterChart,
  Scatter,
  ZAxis,
} from 'recharts';
import { api } from '../lib/api';
import { PageLoading, ErrorBox } from '../components/Loading';
import StatCard from '../components/StatCard';
import HtmlContent from '../components/HtmlContent';
import { cn } from '../lib/cn';

const CATEGORY_COLORS: Record<string, string> = {
  strong: '#16a34a',
  weak: '#e4760a',
  suggestive: '#eab308',
  trend: '#5388bd',
  null: '#8d97a8',
  falsified: '#dc2626',
  falsification: '#dc2626',
  unknown: '#64748b',
  inadmissible: '#dc2626',
  demonstrative: '#16a34a',
  programmatic: '#5388bd',
  pilot: '#eab308',
};

const CATEGORY_LABELS: Record<string, string> = {
  strong: 'Strong',
  weak: 'Weak',
  suggestive: 'Suggestive',
  trend: 'Trend',
  null: 'Null',
  falsified: 'Falsación',
  falsification: 'Falsación',
  unknown: 'Sin clasificar',
};

function colorFor(cat: string): string {
  const k = cat.toLowerCase();
  return CATEGORY_COLORS[k] ?? '#5d6779';
}

function labelFor(cat: string): string {
  const k = cat.toLowerCase();
  return CATEGORY_LABELS[k] ?? cat;
}

function fmt(value: number | undefined | null, digits = 3): string {
  return typeof value === 'number' && Number.isFinite(value) ? value.toFixed(digits) : '—';
}

function scopeLabel(scope?: string): string {
  if (scope === 'inter-scale') return 'Inter-escala';
  if (scope === 'inter-domain') return 'Inter-dominio';
  return 'Corpus';
}

export default function Dashboard() {
  const { data: summary, isLoading, error } = useQuery({
    queryKey: ['summary'],
    queryFn: api.summary,
  });
  const { data: cases } = useQuery({
    queryKey: ['cases'],
    queryFn: api.cases,
  });

  if (isLoading) return <PageLoading label="Cargando resumen de tesis…" />;
  if (error)
    return (
      <div className="mx-auto max-w-7xl p-8">
        <ErrorBox error={error} />
      </div>
    );
  if (!summary) return null;

  const { stats, distribution } = summary;
  const presentation = summary.presentation;
  const corpusScope = summary.corpus_scope;

  const scatterData = (cases ?? [])
    .filter((c) => c.metrics.edi != null && c.metrics.pvalue != null)
    .map((c) => ({
      id: c.case_id,
      caso: c.title,
      edi: c.metrics.edi!,
      p: c.metrics.pvalue!,
      category: c.metrics.category,
      nivel: c.metrics.nivel,
      scope: c.scope,
    }));

  const passRatio = stats.total_cases
    ? Math.round((stats.overall_pass / stats.total_cases) * 100)
    : 0;

  return (
    <div className="pb-12">
      <section className="border-b border-ink-200 dark:border-ink-800 bg-white dark:bg-ink-950">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-8 lg:py-12">
          <div className="grid lg:grid-cols-[minmax(0,1.08fr)_minmax(360px,0.92fr)] gap-8 lg:gap-10 items-start">
            <div className="min-w-0">
              <h1 className="font-serif text-4xl md:text-5xl lg:text-6xl font-semibold tracking-tight leading-[1.04] text-balance text-ink-950 dark:text-ink-50">
                {presentation?.title ?? 'Estructuras Pre-Ontológicas'}
              </h1>
              <p className="mt-4 text-lg md:text-xl text-ink-700 dark:text-ink-300 leading-relaxed max-w-3xl text-balance">
                {presentation?.subtitle ??
                  'Realismo irrealista operativo y compresión multiescala con validación EDI multidominio.'}
              </p>

              <div className="mt-7 flex flex-wrap gap-3">
                <Link to="/tesis" className="btn-primary">
                  <BookOpen className="w-4 h-4" />
                  Leer manuscrito
                </Link>
                <Link to="/casos" className="btn-outline">
                  <FlaskConical className="w-4 h-4" />
                  Explorar corpus
                </Link>
              </div>

              {presentation?.resumen_excerpt_html && (
                <div className="mt-8 border-l-4 border-accent-500 pl-5 max-w-4xl">
                  <div className="text-xs uppercase tracking-wider font-semibold text-ink-500 dark:text-ink-400 mb-2">
                    Resumen del manuscrito
                  </div>
                  <HtmlContent
                    html={presentation.resumen_excerpt_html}
                    className="dashboard-summary-prose"
                  />
                  {presentation.source_path && (
                    <a
                      href={`/repo_files/${presentation.source_path}`}
                      target="_blank"
                      rel="noreferrer"
                      className="mt-2 inline-flex items-center gap-1.5 text-xs font-medium text-accent-700 dark:text-accent-300 hover:underline"
                    >
                      <FileText className="w-3.5 h-3.5" />
                      {presentation.source_path}
                    </a>
                  )}
                </div>
              )}
            </div>

            <aside className="rounded-lg border border-ink-200 dark:border-ink-800 bg-ink-50 dark:bg-ink-900/45 p-5 lg:p-6">
              <div className="flex items-center justify-between gap-3 mb-5">
                <div>
                  <div className="text-xs uppercase tracking-wider font-semibold text-ink-500 dark:text-ink-400">
                    Estado verificable
                  </div>
                  <div className="mt-1 font-semibold text-ink-950 dark:text-ink-50">
                    Corpus EDI publicado en la web
                  </div>
                </div>
                <ShieldCheck className="w-5 h-5 text-success flex-none" />
              </div>

              <div className="grid grid-cols-2 gap-3">
                <HeroMetric label="Métricas visibles" value={stats.total_cases} />
                <HeroMetric label="Core declarado" value={corpusScope?.declared_core_cases ?? 40} />
                <HeroMetric label="overall_pass" value={stats.overall_pass} tone="success" />
                <HeroMetric label="Pass ratio" value={`${passRatio}%`} />
              </div>

              {corpusScope && (
                <div className="mt-5 space-y-2 text-sm">
                  <ScopeRow
                    icon={Layers}
                    label="Inter-dominio base"
                    value={`${corpusScope.core_inter_domain} casos`}
                  />
                  <ScopeRow
                    icon={Microscope}
                    label="Inter-escala"
                    value={`${corpusScope.multiscale} casos`}
                  />
                  <ScopeRow
                    icon={Telescope}
                    label="Extensiones versionadas"
                    value={`${corpusScope.extensions} casos`}
                  />
                </div>
              )}

              <p className="mt-5 text-xs leading-relaxed text-ink-500 dark:text-ink-400">
                {corpusScope?.note ??
                  'Los datos se cargan desde metrics.json versionados; el resumen textual se carga desde el front matter del manuscrito.'}
              </p>
            </aside>
          </div>
        </div>
      </section>

      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-8 lg:py-10">
        <section className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-3 mb-8">
          <StatCard
            label="Total casos"
            value={stats.total_cases}
            icon={Database}
            hint="metrics.json detectados"
          />
          <StatCard
            label="overall_pass"
            value={stats.overall_pass}
            icon={CheckCircle2}
            accent="success"
            hint="Gate completo"
          />
          <StatCard
            label="Weak o mejor"
            value={stats.weak_or_better}
            icon={TrendingUp}
            accent="warning"
            hint="Strong + weak + suggestive"
          />
          <StatCard
            label="Null honesto"
            value={stats.null_count}
            icon={XCircle}
            hint="Sin señal robusta"
          />
          <StatCard
            label="EDI mediana"
            value={fmt(stats.median_edi)}
            icon={Activity}
            hint={`Media: ${fmt(stats.mean_edi)}`}
          />
          <StatCard
            label="Escalas"
            value={corpusScope?.multiscale ?? 10}
            icon={Scale}
            hint="corpus multiescala"
          />
        </section>

        <section className="grid lg:grid-cols-[minmax(0,1fr)_360px] gap-5 mb-8">
          <div className="card p-5">
            <div className="flex items-center justify-between gap-3 mb-4">
              <div>
                <h2 className="font-semibold text-ink-900 dark:text-ink-100">
                  Distribución del corpus
                </h2>
                <p className="text-xs text-ink-500 dark:text-ink-400 mt-1">
                  Categorías de cierre operativo calculadas desde la API.
                </p>
              </div>
              <Link
                to="/casos"
                className="text-xs text-accent-700 dark:text-accent-300 hover:underline inline-flex items-center gap-1"
              >
                Ver todos <ArrowRight className="w-3 h-3" />
              </Link>
            </div>
            <ResponsiveContainer width="100%" height={280}>
              <BarChart data={distribution} margin={{ top: 8, right: 8, left: 0, bottom: 8 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="rgb(125 138 159 / 0.18)" vertical={false} />
                <XAxis
                  dataKey="category"
                  tick={{ fontSize: 11, fill: 'currentColor' }}
                  tickFormatter={labelFor}
                  tickLine={false}
                  axisLine={{ stroke: 'rgb(125 138 159 / 0.3)' }}
                  className="text-ink-600 dark:text-ink-400"
                />
                <YAxis
                  tick={{ fontSize: 11, fill: 'currentColor' }}
                  tickLine={false}
                  axisLine={false}
                  className="text-ink-600 dark:text-ink-400"
                />
                <Tooltip
                  contentStyle={{
                    background: 'rgb(var(--color-card))',
                    border: '1px solid rgb(var(--color-line))',
                    borderRadius: '0.5rem',
                    fontSize: '0.85em',
                    padding: '0.5rem 0.75rem',
                  }}
                  cursor={{ fill: 'rgb(228 118 10 / 0.08)' }}
                  labelFormatter={labelFor}
                />
                <Bar dataKey="count" radius={[5, 5, 0, 0]}>
                  {distribution.map((d, i) => (
                    <Cell key={i} fill={colorFor(d.category)} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>

          <div className="card p-5">
            <h2 className="font-semibold text-ink-900 dark:text-ink-100 mb-1">
              Casos de mayor EDI
            </h2>
            <p className="text-xs text-ink-500 dark:text-ink-400 mb-4">
              Accesos rápidos para defensa y discusión.
            </p>
            <div className="space-y-2.5">
              {(summary.top_cases ?? []).slice(0, 6).map((c) => (
                <Link
                  key={c.case_id}
                  to={`/casos/${c.case_id}`}
                  className="flex items-center gap-3 rounded-lg border border-ink-200 dark:border-ink-800 px-3 py-2.5 hover:border-accent-400 hover:bg-accent-50 dark:hover:bg-accent-900/10 transition-colors"
                >
                  <span className="font-mono text-[10px] w-8 text-center rounded bg-ink-100 dark:bg-ink-800 py-1">
                    {c.case_num != null ? String(c.case_num).padStart(2, '0') : '—'}
                  </span>
                  <span className="min-w-0 flex-1">
                    <span className="block text-sm font-medium truncate">{c.title}</span>
                    <span className="block text-[11px] text-ink-500 dark:text-ink-400">
                      {scopeLabel(c.scope)} · {labelFor(c.category ?? '')}
                    </span>
                  </span>
                  <span className="font-mono text-sm font-semibold text-success tabular-nums">
                    {fmt(c.edi)}
                  </span>
                </Link>
              ))}
            </div>
          </div>
        </section>

        <section className="grid lg:grid-cols-2 gap-5 mb-8">
          <div className="card p-5">
            <div className="flex items-center justify-between gap-3 mb-4">
              <div>
                <h2 className="font-semibold text-ink-900 dark:text-ink-100">
                  EDI vs p-value
                </h2>
                <p className="text-xs text-ink-500 dark:text-ink-400 mt-1">
                  Selectividad empírica: señal, significancia y categoría.
                </p>
              </div>
              <span className="text-xs text-ink-500">{scatterData.length} casos</span>
            </div>
            <ResponsiveContainer width="100%" height={300}>
              <ScatterChart margin={{ top: 8, right: 16, left: 0, bottom: 8 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="rgb(125 138 159 / 0.18)" />
                <XAxis
                  type="number"
                  dataKey="edi"
                  name="EDI"
                  domain={[-1.5, 1]}
                  tick={{ fontSize: 11, fill: 'currentColor' }}
                  tickLine={false}
                  axisLine={{ stroke: 'rgb(125 138 159 / 0.3)' }}
                  label={{ value: 'EDI', position: 'insideBottomRight', offset: -2, fill: 'currentColor', fontSize: 11 }}
                  className="text-ink-600 dark:text-ink-400"
                />
                <YAxis
                  type="number"
                  dataKey="p"
                  name="p-value"
                  domain={[0, 1]}
                  tick={{ fontSize: 11, fill: 'currentColor' }}
                  tickLine={false}
                  axisLine={false}
                  label={{ value: 'p', angle: -90, position: 'insideLeft', fill: 'currentColor', fontSize: 11 }}
                  className="text-ink-600 dark:text-ink-400"
                />
                <ZAxis range={[42, 42]} />
                <Tooltip
                  cursor={{ strokeDasharray: '3 3', stroke: 'rgb(228 118 10 / 0.4)' }}
                  contentStyle={{
                    background: 'rgb(var(--color-card))',
                    border: '1px solid rgb(var(--color-line))',
                    borderRadius: '0.5rem',
                    fontSize: '0.8em',
                    padding: '0.4rem 0.6rem',
                  }}
                  formatter={(_v, _n, p) => {
                    const payload = p.payload as any;
                    return [
                      `${payload.caso} · EDI ${payload.edi.toFixed(3)} · p ${payload.p.toFixed(3)} · ${labelFor(payload.category)}`,
                      '',
                    ];
                  }}
                />
                {Object.keys(CATEGORY_COLORS).map((category) => (
                  <Scatter
                    key={category}
                    name={labelFor(category)}
                    data={scatterData.filter((d) => d.category === category)}
                    fill={colorFor(category)}
                  />
                ))}
              </ScatterChart>
            </ResponsiveContainer>
          </div>

          <EvidencePanel presentation={presentation} />
        </section>

        {presentation?.resumen_html && (
          <section className="card p-5 lg:p-7">
            <details open className="summary-details">
              <summary className="cursor-pointer select-none font-semibold text-ink-900 dark:text-ink-100">
                Resumen completo en español
              </summary>
              <div className="mt-5">
                <HtmlContent html={presentation.resumen_html} className="dashboard-full-summary" />
              </div>
            </details>
          </section>
        )}
      </div>
    </div>
  );
}

function HeroMetric({
  label,
  value,
  tone = 'default',
}: {
  label: string;
  value: string | number;
  tone?: 'default' | 'success';
}) {
  return (
    <div className="rounded-lg border border-ink-200 dark:border-ink-800 bg-white dark:bg-ink-950/55 px-3 py-3">
      <div className="text-[10px] uppercase tracking-wider font-semibold text-ink-500 dark:text-ink-400">
        {label}
      </div>
      <div
        className={cn(
          'mt-1 text-2xl font-semibold tabular-nums',
          tone === 'success' ? 'text-success' : 'text-ink-950 dark:text-ink-50'
        )}
      >
        {value}
      </div>
    </div>
  );
}

function ScopeRow({
  icon: Icon,
  label,
  value,
}: {
  icon: React.ComponentType<{ className?: string }>;
  label: string;
  value: string;
}) {
  return (
    <div className="flex items-center gap-3 rounded-lg border border-ink-200 dark:border-ink-800 bg-white/70 dark:bg-ink-950/35 px-3 py-2.5">
      <Icon className="w-4 h-4 text-accent-600 dark:text-accent-300 flex-none" />
      <span className="text-ink-600 dark:text-ink-300 flex-1">{label}</span>
      <span className="font-semibold text-ink-900 dark:text-ink-100">{value}</span>
    </div>
  );
}

function EvidencePanel({
  presentation,
}: {
  presentation: import('../types').Summary['presentation'];
}) {
  return (
    <div className="card p-5">
      <h2 className="font-semibold text-ink-900 dark:text-ink-100 mb-1">
        Puntos para defensa
      </h2>
      <p className="text-xs text-ink-500 dark:text-ink-400 mb-4">
        Lo que debe verse sin abrir el manuscrito completo.
      </p>

      <div className="space-y-4">
        <div className="rounded-lg border border-success/25 bg-success/5 p-4">
          <div className="flex items-center gap-2 text-sm font-semibold text-success mb-2">
            <CheckCircle2 className="w-4 h-4" />
            Lección epistémica
          </div>
          {presentation?.key_lesson_html ? (
            <HtmlContent html={presentation.key_lesson_html} className="dashboard-note-prose" />
          ) : (
            <p className="text-sm text-ink-600 dark:text-ink-400">
              El aparato debe poder rechazar casos esperados para que la tesis sea defendible.
            </p>
          )}
        </div>

        <div className="rounded-lg border border-warning/30 bg-warning/5 p-4">
          <div className="flex items-center gap-2 text-sm font-semibold text-warning mb-2">
            <ShieldCheck className="w-4 h-4" />
            Limitaciones declaradas
          </div>
          {presentation?.limitations_html ? (
            <HtmlContent html={presentation.limitations_html} className="dashboard-note-prose" />
          ) : (
            <p className="text-sm text-ink-600 dark:text-ink-400">
              La fuerza inferencial se interpreta junto con LoE, ventana de validación y dependencia instrumento-fenómeno.
            </p>
          )}
        </div>

        {presentation?.keywords && presentation.keywords.length > 0 && (
          <div>
            <div className="text-xs uppercase tracking-wider font-semibold text-ink-500 dark:text-ink-400 mb-2">
              Vocabulario central
            </div>
            <div className="flex flex-wrap gap-1.5">
              {presentation.keywords.slice(0, 12).map((keyword) => (
                <span key={keyword} className="badge-neutral">
                  {keyword}
                </span>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
