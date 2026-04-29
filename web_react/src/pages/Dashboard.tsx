import { useQuery } from '@tanstack/react-query';
import { Link } from 'react-router-dom';
import {
  Activity,
  CheckCircle2,
  AlertTriangle,
  XCircle,
  TrendingUp,
  BookOpen,
  ArrowRight,
  Sparkles,
  FlaskConical,
  Layers,
  Microscope,
  Telescope,
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
  Legend,
} from 'recharts';
import { api } from '../lib/api';
import { PageLoading, ErrorBox } from '../components/Loading';
import StatCard from '../components/StatCard';
import { cn } from '../lib/cn';

const CATEGORY_COLORS: Record<string, string> = {
  strong: '#16a34a',
  weak: '#e4760a',
  suggestive: '#eab308',
  trend: '#5388bd',
  null: '#8d97a8',
  falsified: '#dc2626',
  inadmissible: '#dc2626',
  demonstrative: '#16a34a',
  programmatic: '#5388bd',
  pilot: '#eab308',
};

function colorFor(cat: string): string {
  const k = cat.toLowerCase();
  return CATEGORY_COLORS[k] ?? '#5d6779';
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

  if (isLoading) return <PageLoading label="Cargando resumen del corpus…" />;
  if (error) return <div className="mx-auto max-w-7xl p-8"><ErrorBox error={error} /></div>;
  if (!summary) return null;

  const { stats, distribution } = summary;

  const scatterData = (cases ?? [])
    .filter((c) => c.metrics.edi != null && c.metrics.pvalue != null)
    .map((c) => ({
      id: c.case_id,
      caso: c.title,
      edi: c.metrics.edi!,
      p: c.metrics.pvalue!,
      category: c.metrics.category,
      nivel: c.metrics.nivel,
    }));

  const strongCases = (cases ?? []).filter((c) => c.metrics.overall_pass);

  return (
    <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-8 lg:py-12">
      {/* Hero */}
      <section className="mb-12 lg:mb-16 relative">
        <div className="absolute inset-0 -z-10 overflow-hidden pointer-events-none">
          <div className="absolute -top-32 -right-32 w-[600px] h-[600px] rounded-full bg-accent-500/5 blur-3xl" />
          <div className="absolute top-32 -left-40 w-[500px] h-[500px] rounded-full bg-scholar-500/5 blur-3xl" />
        </div>

        <div className="grid lg:grid-cols-12 gap-8 items-end">
          <div className="lg:col-span-8">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-accent-100 dark:bg-accent-900/30 text-accent-700 dark:text-accent-300 text-xs font-medium mb-4">
              <Sparkles className="w-3.5 h-3.5" />
              Tesis doctoral · Universidad de Antioquia
            </div>
            <h1 className="font-serif text-4xl md:text-5xl lg:text-6xl font-semibold tracking-tight leading-[1.05] text-balance text-ink-900 dark:text-ink-50 mb-5">
              Estructuras Pre-Ontológicas
            </h1>
            <p className="text-base md:text-lg text-ink-600 dark:text-ink-400 leading-relaxed max-w-2xl text-balance">
              Realismo irrealista operativo y compresión multiescala con validación EDI multidominio.
              Una propuesta ontológica general validada operativamente sobre 40 casos en 8 escalas físicas y 30 dominios disciplinares.
            </p>
            <div className="mt-7 flex flex-wrap gap-3">
              <Link to="/tesis" className="btn-primary">
                <BookOpen className="w-4 h-4" />
                Leer manuscrito completo
              </Link>
              <Link to="/casos" className="btn-outline">
                <FlaskConical className="w-4 h-4" />
                Explorar corpus EDI
              </Link>
            </div>
          </div>

          <div className="lg:col-span-4 grid grid-cols-2 gap-3">
            <PillarCard icon={Layers} label="3 marcos generales" value="ontológico · epistemológico · metodológico" />
            <PillarCard icon={FlaskConical} label="40 casos del corpus" value="30 inter-dominio + 10 inter-escala" />
            <PillarCard icon={Microscope} label="8 escalas físicas" value="cuántica → cosmológica" />
            <PillarCard icon={Telescope} label="0/1500 falsos positivos" value="hostile testing severo" />
          </div>
        </div>
      </section>

      {/* KPIs */}
      <section className="mb-12">
        <h2 className="text-lg font-semibold mb-4 flex items-center gap-2 text-ink-800 dark:text-ink-200">
          <Activity className="w-4 h-4 text-accent-500" />
          Estado del corpus
        </h2>
        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-3">
          <StatCard
            label="Total casos"
            value={stats.total_cases}
            icon={FlaskConical}
            hint="inter-dominio + inter-escala"
          />
          <StatCard
            label="overall_pass"
            value={stats.overall_pass}
            icon={CheckCircle2}
            accent="success"
            hint="Gate completo de 13 condiciones"
          />
          <StatCard
            label="Weak o mejor"
            value={stats.weak_or_better}
            icon={TrendingUp}
            accent="warning"
            hint="EDI ≥ 0.10 con p < 0.05"
          />
          <StatCard
            label="Null honesto"
            value={stats.null_count}
            icon={XCircle}
            hint="Sin estructura macro detectable"
          />
          <StatCard
            label="Falsación rechazada"
            value={stats.falsified}
            icon={AlertTriangle}
            accent="danger"
            hint="Controles inversos correctamente rechazados"
          />
          <StatCard
            label="EDI mediana"
            value={stats.median_edi != null ? stats.median_edi.toFixed(3) : '—'}
            icon={Activity}
            hint={`Media: ${stats.mean_edi != null ? stats.mean_edi.toFixed(3) : '—'}`}
          />
        </div>
      </section>

      {/* Charts */}
      <section className="mb-12 grid lg:grid-cols-2 gap-5">
        {/* Distribución */}
        <div className="card p-5">
          <div className="flex items-center justify-between mb-4">
            <h3 className="font-semibold text-ink-800 dark:text-ink-100">Distribución por categoría</h3>
            <Link to="/casos" className="text-xs text-accent-600 dark:text-accent-400 hover:underline flex items-center gap-1">
              Ver todos <ArrowRight className="w-3 h-3" />
            </Link>
          </div>
          <ResponsiveContainer width="100%" height={260}>
            <BarChart data={distribution} margin={{ top: 8, right: 8, left: 0, bottom: 8 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="rgb(125 138 159 / 0.18)" vertical={false} />
              <XAxis
                dataKey="category"
                tick={{ fontSize: 11, fill: 'currentColor' }}
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
              />
              <Bar dataKey="count" radius={[6, 6, 0, 0]}>
                {distribution.map((d, i) => (
                  <Cell key={i} fill={colorFor(d.category)} />
                ))}
              </Bar>
            </BarChart>
          </ResponsiveContainer>
        </div>

        {/* Scatter EDI vs p */}
        <div className="card p-5">
          <div className="flex items-center justify-between mb-4">
            <h3 className="font-semibold text-ink-800 dark:text-ink-100">EDI vs p-value</h3>
            <span className="text-xs text-ink-500">{scatterData.length} casos</span>
          </div>
          <ResponsiveContainer width="100%" height={260}>
            <ScatterChart margin={{ top: 8, right: 16, left: 0, bottom: 8 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="rgb(125 138 159 / 0.18)" />
              <XAxis
                type="number"
                dataKey="edi"
                name="EDI"
                domain={[-0.2, 1]}
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
              <ZAxis range={[40, 40]} />
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
                  const pl = p.payload as any;
                  return [
                    `${pl.caso} · EDI ${pl.edi.toFixed(3)} · p ${pl.p.toFixed(3)} · ${pl.category}`,
                    '',
                  ];
                }}
              />
              <Legend
                wrapperStyle={{ fontSize: '0.75rem' }}
                iconType="circle"
              />
              <Scatter name="Strong" data={scatterData.filter((d) => d.category === 'strong')} fill="#16a34a" />
              <Scatter name="Weak" data={scatterData.filter((d) => d.category === 'weak')} fill="#e4760a" />
              <Scatter name="Suggestive" data={scatterData.filter((d) => d.category === 'suggestive')} fill="#eab308" />
              <Scatter name="Trend" data={scatterData.filter((d) => d.category === 'trend')} fill="#5388bd" />
              <Scatter name="Null" data={scatterData.filter((d) => d.category === 'null')} fill="#8d97a8" />
            </ScatterChart>
          </ResponsiveContainer>
        </div>
      </section>

      {/* Casos strong */}
      {strongCases.length > 0 && (
        <section className="mb-12">
          <div className="flex items-center justify-between mb-4">
            <h2 className="text-lg font-semibold flex items-center gap-2 text-ink-800 dark:text-ink-200">
              <CheckCircle2 className="w-4 h-4 text-success" />
              Casos overall_pass · gate completo
            </h2>
            <Link to="/casos" className="text-sm text-accent-600 dark:text-accent-400 hover:underline">
              Ver corpus completo →
            </Link>
          </div>
          <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-3">
            {strongCases.map((c) => (
              <Link
                key={c.case_id}
                to={`/casos/${c.case_id}`}
                className="card card-hover p-4 group"
              >
                <div className="text-[10px] uppercase tracking-wider text-success font-medium mb-1">
                  Strong
                </div>
                <h3 className="font-semibold text-sm leading-tight mb-2 text-ink-900 dark:text-ink-100 line-clamp-2">
                  {c.title}
                </h3>
                <div className="flex items-center justify-between text-xs">
                  <span className="font-mono text-ink-500 dark:text-ink-400">EDI</span>
                  <span className="font-mono font-semibold text-success tabular-nums">
                    {c.metrics.edi?.toFixed(3)}
                  </span>
                </div>
              </Link>
            ))}
          </div>
        </section>
      )}
    </div>
  );
}

function PillarCard({
  icon: Icon,
  label,
  value,
}: {
  icon: React.ComponentType<{ className?: string }>;
  label: string;
  value: string;
}) {
  return (
    <div className="card p-3.5">
      <Icon className="w-4 h-4 text-accent-500 mb-1.5" />
      <div className="text-[10.5px] font-medium text-ink-500 dark:text-ink-400 uppercase tracking-wider">
        {label}
      </div>
      <div className="text-xs text-ink-700 dark:text-ink-200 mt-0.5 leading-snug">
        {value}
      </div>
    </div>
  );
}
