import { useParams, Link } from 'react-router-dom';
import { useQuery } from '@tanstack/react-query';
import {
  ArrowLeft,
  CheckCircle2,
  XCircle,
  Activity,
  GitCommit,
  Calendar,
  Hash,
  FileText,
  FlaskConical,
  ExternalLink,
  Layers,
} from 'lucide-react';
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from 'recharts';
import { api } from '../lib/api';
import { PageLoading, ErrorBox } from '../components/Loading';
import HtmlContent from '../components/HtmlContent';
import StatCard from '../components/StatCard';
import { cn } from '../lib/cn';
import { useState } from 'react';

export default function CaseDetail() {
  const { caseId = '' } = useParams();
  const { data: c, isLoading, error } = useQuery({
    queryKey: ['case', caseId],
    queryFn: () => api.case(caseId),
    enabled: !!caseId,
  });

  const [activeTab, setActiveTab] = useState<'overview' | 'readme' | 'docs' | 'math'>('overview');

  if (isLoading) return <PageLoading label={`Cargando caso ${caseId}…`} />;
  if (error || !c)
    return (
      <div className="mx-auto max-w-5xl p-8">
        <ErrorBox error={error ?? new Error('Caso no encontrado')} />
        <Link to="/casos" className="btn-outline mt-4">
          ← Volver a corpus
        </Link>
      </div>
    );

  const arr = c.primary_arrays;
  const hasArrays = !!(arr && arr.obs && arr.obs.length > 0);

  let chartData: Array<Record<string, number>> = [];
  if (hasArrays) {
    const len = Math.min(
      arr!.obs.length,
      arr!.abm_coupled?.length ?? Infinity,
      arr!.abm_no_ode?.length ?? Infinity
    );
    chartData = Array.from({ length: len }, (_, i) => {
      const row: Record<string, number> = { t: i, obs: arr!.obs[i] };
      if (arr!.abm_coupled) row.acoplado = arr!.abm_coupled[i];
      if (arr!.abm_no_ode) row.no_ode = arr!.abm_no_ode[i];
      if (arr!.ode_pred) row.ode = arr!.ode_pred[i];
      if (arr!.forcing) row.forcing = arr!.forcing[i];
      return row;
    });
  }

  return (
    <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-8">
      <Link
        to="/casos"
        className="inline-flex items-center gap-1.5 text-sm text-ink-500 dark:text-ink-400 hover:text-accent-600 dark:hover:text-accent-400 mb-4 transition-colors"
      >
        <ArrowLeft className="w-3.5 h-3.5" />
        Volver al corpus
      </Link>

      {/* Hero */}
      <header className="card p-6 lg:p-8 mb-6 relative overflow-hidden">
        <div className="absolute -top-8 -right-8 opacity-[0.04]">
          <FlaskConical className="w-48 h-48" />
        </div>
        <div className="relative">
          <div className="flex items-center gap-2 text-xs text-ink-500 dark:text-ink-400 mb-3 flex-wrap">
            <span className="font-mono px-2 py-0.5 rounded bg-ink-100 dark:bg-ink-800">
              Caso {c.case_num != null ? String(c.case_num).padStart(2, '0') : '—'}
            </span>
            <span className="font-mono">{c.case_name}</span>
            {c.meta?.generated_at && (
              <span className="inline-flex items-center gap-1">
                <Calendar className="w-3 h-3" />
                {new Date(c.meta.generated_at).toLocaleString('es-CO', {
                  dateStyle: 'medium',
                  timeStyle: 'short',
                })}
              </span>
            )}
            {c.meta?.git?.commit && (
              <span className="inline-flex items-center gap-1 font-mono">
                <GitCommit className="w-3 h-3" />
                {c.meta.git.commit.slice(0, 10)}
              </span>
            )}
          </div>
          <h1 className="font-serif text-3xl md:text-4xl font-semibold tracking-tight text-balance mb-3">
            {c.title}
          </h1>
          <div className="flex items-center gap-2 flex-wrap">
            <CategoryBadge category={c.metrics.category} pass={c.metrics.overall_pass} nivel={c.metrics.nivel} />
            {c.metrics.overall_pass && (
              <span className="badge-success">
                <CheckCircle2 className="w-3 h-3" />
                overall_pass
              </span>
            )}
            {c.metrics.nivel != null && (
              <span className="badge-neutral">
                <Hash className="w-3 h-3" />
                Nivel {c.metrics.nivel}
              </span>
            )}
            {c.phase_order && c.phase_order.length > 0 && (
              <span className="badge-neutral">
                Fases: {c.phase_order.join(', ')}
              </span>
            )}
          </div>
        </div>
      </header>

      {/* KPIs */}
      <section className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-3 mb-6">
        <StatCard
          label="EDI"
          value={c.metrics.edi != null ? c.metrics.edi.toFixed(4) : '—'}
          icon={Activity}
          accent={
            c.metrics.edi != null
              ? c.metrics.edi >= 0.3
                ? 'success'
                : c.metrics.edi >= 0.1
                ? 'warning'
                : 'default'
              : 'default'
          }
        />
        <StatCard
          label="p-perm"
          value={c.metrics.pvalue != null ? c.metrics.pvalue.toFixed(4) : '—'}
          accent={c.metrics.pvalue != null && c.metrics.pvalue < 0.05 ? 'success' : 'default'}
        />
        <StatCard label="CR" value={c.metrics.cr != null ? c.metrics.cr.toFixed(3) : '—'} />
        <StatCard label="Categoría" value={c.metrics.category} />
        <StatCard label="Nivel" value={c.metrics.nivel != null ? String(c.metrics.nivel) : '—'} />
        <StatCard
          label="overall_pass"
          value={c.metrics.overall_pass ? 'PASS' : 'FAIL'}
          icon={c.metrics.overall_pass ? CheckCircle2 : XCircle}
          accent={c.metrics.overall_pass ? 'success' : 'danger'}
        />
      </section>

      {/* Charts */}
      {hasArrays && (
        <section className="card p-5 mb-6">
          <h3 className="font-semibold text-ink-800 dark:text-ink-100 mb-4 flex items-center gap-2">
            <Layers className="w-4 h-4 text-accent-500" />
            Trayectorias del caso (primary_arrays)
          </h3>
          <ResponsiveContainer width="100%" height={340}>
            <LineChart data={chartData} margin={{ top: 8, right: 16, left: 0, bottom: 8 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="rgb(125 138 159 / 0.18)" />
              <XAxis
                dataKey="t"
                tick={{ fontSize: 11, fill: 'currentColor' }}
                tickLine={false}
                axisLine={{ stroke: 'rgb(125 138 159 / 0.3)' }}
                label={{ value: 'paso temporal', position: 'insideBottomRight', offset: -2, fontSize: 11 }}
              />
              <YAxis
                tick={{ fontSize: 11, fill: 'currentColor' }}
                tickLine={false}
                axisLine={false}
              />
              <Tooltip
                contentStyle={{
                  background: 'rgb(var(--color-card))',
                  border: '1px solid rgb(var(--color-line))',
                  borderRadius: '0.5rem',
                  fontSize: '0.8em',
                  padding: '0.4rem 0.6rem',
                }}
              />
              <Legend
                wrapperStyle={{ fontSize: '0.75rem', paddingTop: '0.5rem' }}
                iconType="line"
              />
              <Line type="monotone" dataKey="obs" stroke="#0e1219" strokeWidth={2} dot={false} name="Observado" />
              <Line type="monotone" dataKey="acoplado" stroke="#16a34a" strokeWidth={1.6} dot={false} name="ABM acoplado" />
              <Line type="monotone" dataKey="no_ode" stroke="#dc2626" strokeWidth={1.6} dot={false} name="ABM no_ode (ablativo)" strokeDasharray="4 3" />
              <Line type="monotone" dataKey="ode" stroke="#5388bd" strokeWidth={1.4} dot={false} name="ODE solo" strokeDasharray="2 2" />
              {arr?.forcing && (
                <Line type="monotone" dataKey="forcing" stroke="#e4760a" strokeWidth={1.2} dot={false} name="Forcing" strokeDasharray="6 3" />
              )}
            </LineChart>
          </ResponsiveContainer>
          <p className="text-xs text-ink-500 dark:text-ink-400 mt-3 leading-relaxed">
            La diferencia entre <span className="text-success font-mono">acoplado</span> y{' '}
            <span className="text-danger font-mono">no_ode</span> mide el cierre operativo κ vía intervención ablativa:
            EDI = 1 − RMSE_acoplado / RMSE_no_ode.
          </p>
        </section>
      )}

      {/* Tabs */}
      <section className="mb-6">
        <div className="flex items-center gap-1 border-b border-ink-200 dark:border-ink-800 mb-4 overflow-x-auto">
          <TabButton active={activeTab === 'overview'} onClick={() => setActiveTab('overview')}>
            <FileText className="w-3.5 h-3.5" /> Reporte
          </TabButton>
          {c.thesis_readme_html && (
            <TabButton active={activeTab === 'readme'} onClick={() => setActiveTab('readme')}>
              <FileText className="w-3.5 h-3.5" /> README de tesis
            </TabButton>
          )}
          {c.thesis_docs_html && c.thesis_docs_html.length > 0 && (
            <TabButton active={activeTab === 'docs'} onClick={() => setActiveTab('docs')}>
              <FileText className="w-3.5 h-3.5" /> Documentación ({c.thesis_docs_html.length})
            </TabButton>
          )}
          {c.math_explainer_html && (
            <TabButton active={activeTab === 'math'} onClick={() => setActiveTab('math')}>
              <FileText className="w-3.5 h-3.5" /> Explicador matemático
            </TabButton>
          )}
        </div>

        <div className="card p-6 lg:p-8">
          {activeTab === 'overview' && c.report_html && (
            <HtmlContent html={c.report_html} />
          )}
          {activeTab === 'overview' && !c.report_html && (
            <div className="text-sm text-ink-500 dark:text-ink-400">
              Sin reporte adicional disponible. Métricas verificables en{' '}
              <code className="text-xs">09-simulaciones-edi/{c.case_name}/outputs/metrics.json</code>.
            </div>
          )}
          {activeTab === 'readme' && c.thesis_readme_html && (
            <HtmlContent html={c.thesis_readme_html} />
          )}
          {activeTab === 'docs' && c.thesis_docs_html && (
            <div className="space-y-8">
              {c.thesis_docs_html.map((doc, i) => (
                <div key={i}>
                  <h3 className="font-semibold text-lg mb-3 flex items-center gap-2">
                    <FileText className="w-4 h-4 text-accent-500" />
                    {doc.title}
                  </h3>
                  <HtmlContent html={doc.html} />
                </div>
              ))}
            </div>
          )}
          {activeTab === 'math' && c.math_explainer_html && (
            <HtmlContent html={c.math_explainer_html} />
          )}
        </div>
      </section>

      {/* Enlaces */}
      <section className="card p-5">
        <h3 className="font-semibold text-ink-800 dark:text-ink-100 mb-3 text-sm">Recursos del caso</h3>
        <div className="grid sm:grid-cols-2 gap-2 text-sm">
          <a
            href={`/sim_files/${c.case_name}/outputs/metrics.json`}
            target="_blank"
            rel="noreferrer"
            className="flex items-center gap-2 px-3 py-2 rounded-lg border border-ink-200 dark:border-ink-800 hover:border-accent-400 hover:bg-accent-50 dark:hover:bg-accent-900/10 transition-colors"
          >
            <ExternalLink className="w-3.5 h-3.5 text-ink-400" />
            <code className="text-xs">metrics.json</code>
          </a>
          <a
            href={`/sim_files/${c.case_name}/case_config.json`}
            target="_blank"
            rel="noreferrer"
            className="flex items-center gap-2 px-3 py-2 rounded-lg border border-ink-200 dark:border-ink-800 hover:border-accent-400 hover:bg-accent-50 dark:hover:bg-accent-900/10 transition-colors"
          >
            <ExternalLink className="w-3.5 h-3.5 text-ink-400" />
            <code className="text-xs">case_config.json</code>
          </a>
          {hasArrays && (
            <a
              href={`/sim_files/${c.case_name}/outputs/primary_arrays.json`}
              target="_blank"
              rel="noreferrer"
              className="flex items-center gap-2 px-3 py-2 rounded-lg border border-ink-200 dark:border-ink-800 hover:border-accent-400 hover:bg-accent-50 dark:hover:bg-accent-900/10 transition-colors"
            >
              <ExternalLink className="w-3.5 h-3.5 text-ink-400" />
              <code className="text-xs">primary_arrays.json</code>
            </a>
          )}
        </div>
      </section>
    </div>
  );
}

function CategoryBadge({
  category,
  pass,
  nivel,
}: {
  category: string;
  pass: boolean;
  nivel: number | null;
}) {
  const k = category.toLowerCase();
  const map: Record<string, string> = {
    strong: 'badge-success',
    weak: 'badge-accent',
    suggestive: 'badge-warning',
    trend: 'badge-neutral',
    null: 'badge-neutral',
    falsified: 'badge-danger',
  };
  return <span className={cn(map[k] ?? 'badge-neutral', 'capitalize')}>{category}</span>;
}

function TabButton({
  active,
  children,
  onClick,
}: {
  active: boolean;
  children: React.ReactNode;
  onClick: () => void;
}) {
  return (
    <button
      onClick={onClick}
      className={cn(
        'flex items-center gap-1.5 px-4 py-2.5 text-sm font-medium border-b-2 transition-colors whitespace-nowrap',
        active
          ? 'border-accent-500 text-accent-700 dark:text-accent-300'
          : 'border-transparent text-ink-500 dark:text-ink-400 hover:text-ink-800 dark:hover:text-ink-200'
      )}
    >
      {children}
    </button>
  );
}
