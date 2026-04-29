import { useState, useEffect, useRef } from 'react';
import {
  ShieldCheck,
  Play,
  Loader2,
  Terminal,
  CheckCircle2,
  XCircle,
  AlertTriangle,
  Sparkles,
  Activity,
  Bug,
  Cpu,
  GitBranch,
  Zap,
  FileWarning,
  ChevronRight,
  Copy,
  Check,
  Network,
  Atom,
  BookCheck,
} from 'lucide-react';
import { useMutation } from '@tanstack/react-query';
import toast from 'react-hot-toast';
import { motion, AnimatePresence } from 'framer-motion';
import { api } from '../lib/api';
import HtmlContent from '../components/HtmlContent';
import { cn } from '../lib/cn';

interface Theory {
  id: string;
  number: number;
  title: string;
  profile: string;
  focus: string;
  status: 'ok' | 'fixed' | 'critical';
  icon: React.ComponentType<{ className?: string }>;
}

const THEORIES: Theory[] = [
  { id: 'T00', number: 0, title: 'Núcleo ontológico', profile: 'classical.propositional', focus: '4 invariantes + naturalismo + rechazo de 3 rivales', status: 'ok', icon: Atom },
  { id: 'T01', number: 1, title: 'Criterios de legitimidad', profile: 'classical.propositional', focus: '9 condiciones derivan G y H', status: 'ok', icon: BookCheck },
  { id: 'T02', number: 2, title: 'Debates y límites', profile: 'classical.propositional', focus: 'Anti-dualismo, anti-reduccionismo, anti-emergencia', status: 'ok', icon: GitBranch },
  { id: 'T03', number: 3, title: 'Text layer tesis', profile: 'classical.propositional', focus: '3 claims con confianza > 0.94', status: 'ok', icon: BookCheck },
  { id: 'T04', number: 4, title: 'Text layer bibliografía', profile: 'classical.propositional', focus: '3 claims con confianza > 0.90', status: 'ok', icon: BookCheck },
  { id: 'T05', number: 5, title: 'Asimetría L1↔B↔L3↔S', profile: 'classical.first_order', focus: 'Refinamiento a existenciales', status: 'fixed', icon: Network },
  { id: 'T06', number: 6, title: 'Operadores y circularidad', profile: 'classical.propositional', focus: 'μ→G→H→K→E sin atajos viciosos', status: 'ok', icon: Activity },
  { id: 'T07', number: 7, title: 'overall_pass 13 condiciones', profile: 'classical.propositional', focus: 'Colectivamente necesarias', status: 'ok', icon: CheckCircle2 },
  { id: 'T08', number: 8, title: 'Discriminación rivales', profile: 'classical.propositional', focus: '14 rivales discriminados', status: 'ok', icon: GitBranch },
  { id: 'T09', number: 9, title: 'Niveles 0-5 paisaje', profile: 'classical.propositional', focus: 'Excluyentes con axiomas explícitos', status: 'ok', icon: Activity },
  { id: 'T10', number: 10, title: 'Falsabilidad', profile: 'classical.propositional', focus: '5 condiciones por modus tollens', status: 'ok', icon: AlertTriangle },
  { id: 'T11', number: 11, title: 'Modal coherencia', profile: 'modal.k', focus: 'Necesidad requiere axioma T', status: 'fixed', icon: Cpu },
  { id: 'T12', number: 12, title: 'Paraconsistencia Wolfram', profile: 'paraconsistent.belnap', focus: 'Coexistencia sin trivialización', status: 'ok', icon: Zap },
  { id: 'T13', number: 13, title: 'Temporalidad y causalidad', profile: 'classical.propositional', focus: 'B-series + Woodward + constitución vs Kim', status: 'fixed', icon: Activity },
  { id: 'T14', number: 14, title: 'Pre-ontológico genético', profile: 'classical.first_order', focus: '"Pre" simondoniano definido', status: 'ok', icon: BookCheck },
  { id: 'T15', number: 15, title: 'Tres marcos generales', profile: 'classical.propositional', focus: 'Independencia + no inductivismo', status: 'fixed', icon: GitBranch },
  { id: 'T16', number: 16, title: 'Naturalismo + rivales', profile: 'classical.propositional', focus: 'Naturalismo excluye 5 rivales metafísicos', status: 'ok', icon: ShieldCheck },
  { id: 'T17', number: 17, title: 'κ-pragmática vs κ-ontológica', profile: 'classical.propositional', focus: '3 criterios; ningún caso actual los cumple', status: 'ok', icon: Network },
  { id: 'T18', number: 18, title: 'Deóntica normativa', profile: 'deontic.standard', focus: 'Validez/efectividad/legitimidad coherentes', status: 'ok', icon: ShieldCheck },
  { id: 'T19', number: 19, title: 'Asimetría tres marcos', profile: 'classical.first_order', focus: 'Asimetría invariante a la escala', status: 'ok', icon: Network },
  { id: 'T20', number: 20, title: 'Stress test falsabilidad', profile: 'classical.propositional', focus: '8 condiciones de fracaso falsables', status: 'ok', icon: AlertTriangle },
  { id: 'T21', number: 21, title: 'Belnap corpus multiescala', profile: 'paraconsistent.belnap', focus: 'Honestidad metodológica sin colapso', status: 'ok', icon: Zap },
  { id: 'T22', number: 22, title: 'Modal marco tripartito', profile: 'modal.k', focus: 'Invariantes necesarios + sondas contingentes', status: 'ok', icon: Cpu },
  { id: 'T23', number: 23, title: 'Modal T (KT)', profile: 'modal.k + axioma T', focus: 'Cierre formal de "AT LEAST T" del cap 02-01', status: 'ok', icon: Cpu },
];

interface Finding {
  id: string;
  title: string;
  detection: string;
  resolution: string;
  status: 'fixed';
}

const FINDINGS: Finding[] = [
  {
    id: 'ST-1',
    title: 'Asimetría L1↔B↔L3↔S no es expresable como axiomas universales proposicionales',
    detection: 'Test 5 de T19 detectó que mezclar partes universales y existenciales en un solo nivel produce contradicción.',
    resolution: 'Refinada a existenciales en lógica de primer orden (cap 02-04 §8.0). Existen modelos donde B(qubit), B(cumulo), F(qubit), F(cumulo) y S(qubit), S(cumulo) coexisten satisfactoriamente.',
    status: 'fixed',
  },
  {
    id: 'ST-2',
    title: 'Necesidad modal requiere axioma T',
    detection: 'En modal.k puro no se valida □P → P (axioma T no asumido). T22 confirmó la limitación.',
    resolution: 'Sistema modal al menos T (KT) declarado explícitamente en cap 02-01. T23 cierra formalmente la coincidencia entre lo declarado y lo verificado.',
    status: 'fixed',
  },
  {
    id: 'ST-3',
    title: 'Respuesta a Kim sobre downward causation requiere construcción argumental',
    detection: 'T13 Test 4 mostró que la implicación ((C ∧ ¬V) ∧ (K → (V → S))) → ¬S NO es válida sin pasos intermedios.',
    resolution: 'Argumento por modus tollens vacuo: si C → ¬V, entonces de ¬V y (V → S) no se infiere S. Cap 02-05 §2.4 formaliza correctamente.',
    status: 'fixed',
  },
  {
    id: 'ST-4',
    title: 'La generalidad del marco NO se infiere desde los casos del corpus',
    detection: 'T15 Test 2: analyze {J} → G es inferencia NO VÁLIDA. Falacia inductivista detectada.',
    resolution: 'El marco general se sostiene por estructura interna coherente (T15 Test 4: (G → S) ∧ G → S válida), no por inducción sobre casos. Cap 06-01 §5 confirma operativamente.',
    status: 'fixed',
  },
  {
    id: 'ST-5',
    title: 'Los 3 marcos NO colapsan unos sobre otros',
    detection: 'T15 Test 5: contramodelos de O→E, E→M, M→O encontrados.',
    resolution: 'Los 3 marcos (ontológico, epistemológico, metodológico) son lógicamente independientes entre sí. La afirmación de aporte triple sustantivo está formalmente verificada.',
    status: 'fixed',
  },
  {
    id: 'ST-6',
    title: 'El naturalismo metafísico moderado NO se demuestra desde dentro',
    detection: 'T16 Test 6: countermodel para N (naturalismo) encontrado. El naturalismo NO se infiere desde el marco mismo.',
    resolution: 'Confirma honestidad metodológica del cap 02-01 §0.1: el naturalismo es compromiso de partida, no conclusión deductiva.',
    status: 'fixed',
  },
];

const STATUS_LABELS: Record<Theory['status'], { label: string; cls: string; icon: React.ComponentType<{ className?: string }> }> = {
  ok: { label: 'OK', cls: 'bg-success/10 text-success border-success/30', icon: CheckCircle2 },
  fixed: { label: 'Detectado y resuelto', cls: 'bg-warning/10 text-warning border-warning/30', icon: AlertTriangle },
  critical: { label: 'Crítico', cls: 'bg-danger/10 text-danger border-danger/30', icon: XCircle },
};

const PROFILE_COLOR: Record<string, string> = {
  'classical.propositional': 'bg-scholar-100 dark:bg-scholar-900/30 text-scholar-700 dark:text-scholar-300',
  'classical.first_order': 'bg-accent-100 dark:bg-accent-900/30 text-accent-700 dark:text-accent-300',
  'modal.k': 'bg-success/10 text-success',
  'modal.k + axioma T': 'bg-success/15 text-success',
  'paraconsistent.belnap': 'bg-warning/15 text-warning',
  'deontic.standard': 'bg-ink-200 dark:bg-ink-700 text-ink-700 dark:text-ink-200',
};

export default function ST() {
  const [output, setOutput] = useState<string>('');
  const [reportHtml, setReportHtml] = useState<string>('');
  const [success, setSuccess] = useState<boolean | null>(null);
  const [filter, setFilter] = useState<'all' | 'fixed' | 'ok'>('all');
  const [search, setSearch] = useState('');
  const [activeTheory, setActiveTheory] = useState<Theory | null>(null);
  const [copiedLog, setCopiedLog] = useState(false);
  const [progressTick, setProgressTick] = useState(0);
  const logRef = useRef<HTMLPreElement>(null);

  const okCount = THEORIES.filter((t) => t.status === 'ok').length;
  const fixedCount = THEORIES.filter((t) => t.status === 'fixed').length;
  const totalCount = THEORIES.length;

  const filtered = THEORIES.filter((t) => {
    if (filter !== 'all' && t.status !== filter) return false;
    if (search.trim()) {
      const q = search.toLowerCase();
      return (
        t.title.toLowerCase().includes(q) ||
        t.focus.toLowerCase().includes(q) ||
        t.id.toLowerCase().includes(q) ||
        t.profile.toLowerCase().includes(q)
      );
    }
    return true;
  });

  const runMutation = useMutation({
    mutationFn: api.runST,
    onSuccess: (data) => {
      setOutput(data.log);
      setReportHtml(data.html);
      setSuccess(data.success);
      if (data.success) toast.success('Suite ST: 24/24 teorías verificadas');
      else toast.error('Suite ST: errores detectados — revisa la salida');
      setTimeout(() => {
        logRef.current?.scrollTo({ top: logRef.current.scrollHeight });
      }, 200);
    },
    onError: (err) => {
      toast.error(`Error: ${err instanceof Error ? err.message : 'desconocido'}`);
    },
  });

  // Animación de "tick" mientras corre
  useEffect(() => {
    if (!runMutation.isPending) return;
    const id = setInterval(() => setProgressTick((t) => (t + 1) % totalCount), 90);
    return () => clearInterval(id);
  }, [runMutation.isPending, totalCount]);

  const copyLog = async () => {
    if (!output) return;
    await navigator.clipboard.writeText(output);
    setCopiedLog(true);
    toast.success('Log copiado al portapapeles');
    setTimeout(() => setCopiedLog(false), 2000);
  };

  return (
    <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-8 lg:py-10">
      {/* Hero */}
      <header className="mb-8 lg:mb-10 relative">
        <div className="absolute inset-0 -z-10 overflow-hidden pointer-events-none">
          <div className="absolute -top-20 -right-20 w-96 h-96 rounded-full bg-success/5 blur-3xl" />
          <div className="absolute -bottom-32 -left-20 w-96 h-96 rounded-full bg-accent-500/5 blur-3xl" />
        </div>
        <div className="flex items-center gap-2 text-xs uppercase tracking-wider text-success font-medium mb-3">
          <ShieldCheck className="w-3.5 h-3.5" />
          Validación lógica formal
        </div>
        <h1 className="font-serif text-3xl md:text-4xl lg:text-5xl font-semibold tracking-tight text-balance mb-3">
          Suite ST · Verificador de consistencia
        </h1>
        <p className="text-ink-600 dark:text-ink-400 max-w-3xl leading-relaxed">
          La capa formal del manuscrito en{' '}
          <code className="text-xs bg-ink-100 dark:bg-ink-800 px-1.5 py-0.5 rounded">@stevenvo780/st-lang</code>.
          24 teorías cubren ontología, epistemología, operadores, niveles del paisaje, falsabilidad,
          coherencia modal, paraconsistencia y deóntica. La suite{' '}
          <strong>detectó 6 hallazgos críticos</strong> que llevaron a refinar el manuscrito.
        </p>
      </header>

      {/* KPI strip + run */}
      <section className="grid lg:grid-cols-[1fr_auto] gap-4 mb-8">
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
          <KpiTile icon={Network} label="Teorías totales" value={totalCount} accent="ink" />
          <KpiTile icon={CheckCircle2} label="OK directo" value={okCount} accent="success" />
          <KpiTile icon={AlertTriangle} label="Refinados" value={fixedCount} accent="warning" />
          <KpiTile icon={Bug} label="Hallazgos" value={FINDINGS.length} accent="accent" />
        </div>

        <div className="card p-4 flex flex-col justify-between gap-3 min-w-0 lg:min-w-[260px] relative overflow-hidden">
          <div className="absolute -top-3 -right-3 opacity-[0.04]">
            <ShieldCheck className="w-28 h-28" />
          </div>
          <div className="relative">
            <div className="text-xs uppercase tracking-wider text-ink-500 dark:text-ink-400 mb-1">
              Ejecución de la suite
            </div>
            <p className="text-xs text-ink-600 dark:text-ink-400 leading-relaxed">
              Corre <code className="text-[10px]">npm run st:check</code> en{' '}
              <code className="text-[10px]">08-consistencia-st</code> y renderiza el reporte.
            </p>
          </div>
          <button
            onClick={() => runMutation.mutate()}
            disabled={runMutation.isPending}
            className={cn(
              'btn-primary relative overflow-hidden group',
              runMutation.isPending && 'cursor-progress'
            )}
          >
            {runMutation.isPending ? (
              <>
                <Loader2 className="w-4 h-4 animate-spin" />
                Verificando T{String(progressTick).padStart(2, '0')}…
              </>
            ) : (
              <>
                <Play className="w-4 h-4" />
                Ejecutar suite completa
              </>
            )}
          </button>
          {success !== null && (
            <div
              className={cn(
                'flex items-center gap-1.5 text-xs px-2 py-1.5 rounded-md',
                success ? 'bg-success/10 text-success' : 'bg-danger/10 text-danger'
              )}
            >
              {success ? (
                <CheckCircle2 className="w-3.5 h-3.5 flex-none" />
              ) : (
                <XCircle className="w-3.5 h-3.5 flex-none" />
              )}
              <span className="truncate">
                {success ? 'Última corrida: éxito' : 'Última corrida: errores'}
              </span>
            </div>
          )}
        </div>
      </section>

      {/* Hallazgos críticos */}
      <section className="mb-8">
        <h2 className="text-lg font-semibold mb-4 flex items-center gap-2 text-ink-800 dark:text-ink-200">
          <FileWarning className="w-4 h-4 text-warning" />
          Hallazgos críticos detectados durante la verificación
        </h2>
        <div className="grid md:grid-cols-2 gap-3">
          {FINDINGS.map((f) => (
            <motion.article
              key={f.id}
              whileHover={{ y: -2 }}
              className="card p-5 relative overflow-hidden group"
            >
              <div className="absolute top-3 right-3 text-[10px] font-mono px-2 py-0.5 rounded-full bg-warning/15 text-warning border border-warning/30">
                {f.id}
              </div>
              <h3 className="font-semibold text-base leading-tight pr-16 mb-3">
                {f.title}
              </h3>
              <div className="space-y-2.5 text-xs leading-relaxed">
                <div>
                  <div className="text-[10px] uppercase tracking-wider font-semibold text-danger mb-0.5 flex items-center gap-1">
                    <Bug className="w-3 h-3" />
                    Detección
                  </div>
                  <p className="text-ink-600 dark:text-ink-400">{f.detection}</p>
                </div>
                <div>
                  <div className="text-[10px] uppercase tracking-wider font-semibold text-success mb-0.5 flex items-center gap-1">
                    <CheckCircle2 className="w-3 h-3" />
                    Resolución
                  </div>
                  <p className="text-ink-700 dark:text-ink-300">{f.resolution}</p>
                </div>
              </div>
            </motion.article>
          ))}
        </div>
      </section>

      {/* Catálogo de teorías */}
      <section className="mb-8">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-4">
          <h2 className="text-lg font-semibold flex items-center gap-2 text-ink-800 dark:text-ink-200">
            <Sparkles className="w-4 h-4 text-accent-500" />
            Catálogo de las 24 teorías
          </h2>
          <div className="flex items-center gap-2">
            <input
              type="text"
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              placeholder="Filtrar por nombre, perfil o foco…"
              className="input !text-xs !py-1.5 max-w-xs"
            />
            <div className="flex items-center gap-1 bg-ink-100 dark:bg-ink-800 rounded-lg p-0.5">
              {(['all', 'ok', 'fixed'] as const).map((f) => (
                <button
                  key={f}
                  onClick={() => setFilter(f)}
                  className={cn(
                    'px-2.5 py-1 rounded-md text-xs font-medium transition-colors',
                    filter === f
                      ? 'bg-white dark:bg-ink-900 text-ink-900 dark:text-ink-100 shadow-sm'
                      : 'text-ink-500 dark:text-ink-400 hover:text-ink-700 dark:hover:text-ink-200'
                  )}
                >
                  {f === 'all' ? 'Todas' : f === 'ok' ? 'OK' : 'Refinadas'}
                </button>
              ))}
            </div>
          </div>
        </div>

        <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-3">
          {filtered.map((t, idx) => {
            const status = STATUS_LABELS[t.status];
            const animating = runMutation.isPending && progressTick === t.number;
            return (
              <motion.button
                key={t.id}
                onClick={() => setActiveTheory(t)}
                whileHover={{ y: -2, scale: 1.005 }}
                className={cn(
                  'card card-hover p-4 text-left relative overflow-hidden group',
                  animating &&
                    'ring-2 ring-accent-400 dark:ring-accent-500 border-accent-400'
                )}
              >
                <div className="flex items-start justify-between gap-2 mb-2">
                  <div className="flex items-center gap-2">
                    <span
                      className={cn(
                        'flex-none w-8 h-8 rounded-lg flex items-center justify-center',
                        animating
                          ? 'bg-accent-500 text-white animate-pulse'
                          : 'bg-ink-100 dark:bg-ink-800 text-ink-600 dark:text-ink-300'
                      )}
                    >
                      <t.icon className="w-4 h-4" />
                    </span>
                    <span className="font-mono text-[10px] font-semibold px-1.5 py-0.5 rounded bg-ink-100 dark:bg-ink-800 text-ink-600 dark:text-ink-300">
                      {t.id}
                    </span>
                  </div>
                  <span
                    className={cn(
                      'badge text-[10px] border',
                      status.cls
                    )}
                    title={status.label}
                  >
                    <status.icon className="w-3 h-3" />
                    {status.label}
                  </span>
                </div>
                <h3 className="font-semibold text-sm leading-tight mb-1.5 text-ink-900 dark:text-ink-100">
                  {t.title}
                </h3>
                <p className="text-xs text-ink-500 dark:text-ink-400 line-clamp-2 leading-relaxed mb-2">
                  {t.focus}
                </p>
                <div className="flex items-center justify-between">
                  <span
                    className={cn(
                      'text-[10px] font-mono px-1.5 py-0.5 rounded',
                      PROFILE_COLOR[t.profile] ?? 'bg-ink-100 dark:bg-ink-800 text-ink-600'
                    )}
                  >
                    {t.profile}
                  </span>
                  <ChevronRight className="w-3 h-3 text-ink-300 dark:text-ink-700 group-hover:text-accent-500 group-hover:translate-x-0.5 transition-all" />
                </div>
              </motion.button>
            );
          })}
        </div>

        {filtered.length === 0 && (
          <div className="card p-10 text-center text-sm text-ink-500">
            Sin teorías que coincidan con el filtro.
          </div>
        )}
      </section>

      {/* Output: terminal + reporte */}
      <AnimatePresence mode="wait">
        {(output || reportHtml) && (
          <motion.section
            key="output"
            initial={{ opacity: 0, y: 16 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: 16 }}
            className="grid lg:grid-cols-[1fr_1fr] gap-5 mb-6"
          >
            {output && (
              <div className="card overflow-hidden">
                <div className="flex items-center justify-between px-4 py-2.5 border-b border-ink-200 dark:border-ink-800 bg-ink-50 dark:bg-ink-900/60">
                  <div className="flex items-center gap-2 text-sm font-semibold">
                    <Terminal className="w-4 h-4 text-accent-500" />
                    Salida del runner
                  </div>
                  <button
                    onClick={copyLog}
                    className="btn-ghost !text-xs !py-1 !px-2"
                    title="Copiar log"
                  >
                    {copiedLog ? (
                      <>
                        <Check className="w-3.5 h-3.5 text-success" />
                        Copiado
                      </>
                    ) : (
                      <>
                        <Copy className="w-3.5 h-3.5" />
                        Copiar
                      </>
                    )}
                  </button>
                </div>
                <pre
                  ref={logRef}
                  className="bg-ink-950 text-ink-100 px-4 py-3 overflow-auto text-[11px] leading-relaxed font-mono max-h-[60vh] whitespace-pre-wrap break-all"
                >
                  {colorizeLog(output)}
                </pre>
              </div>
            )}
            {reportHtml && (
              <div className="card p-5 max-h-[60vh] overflow-y-auto">
                <h3 className="font-semibold mb-3 flex items-center gap-2">
                  <FileWarning className="w-4 h-4 text-accent-500" />
                  Último reporte generado
                </h3>
                <HtmlContent html={reportHtml} />
              </div>
            )}
          </motion.section>
        )}
      </AnimatePresence>

      {/* Modal de detalle de teoría */}
      <AnimatePresence>
        {activeTheory && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="fixed inset-0 z-50 flex items-center justify-center p-4"
            onClick={() => setActiveTheory(null)}
          >
            <div className="absolute inset-0 bg-ink-950/50 backdrop-blur-sm" />
            <motion.div
              initial={{ opacity: 0, scale: 0.95, y: 12 }}
              animate={{ opacity: 1, scale: 1, y: 0 }}
              exit={{ opacity: 0, scale: 0.95, y: 12 }}
              transition={{ type: 'spring', damping: 22, stiffness: 280 }}
              className="relative w-full max-w-lg card p-6"
              onClick={(e) => e.stopPropagation()}
            >
              <button
                onClick={() => setActiveTheory(null)}
                className="absolute top-3 right-3 btn-ghost !p-1.5"
                aria-label="Cerrar"
              >
                <XCircle className="w-4 h-4" />
              </button>
              <div className="flex items-center gap-3 mb-3">
                <div className="w-12 h-12 rounded-xl bg-accent-100 dark:bg-accent-900/30 flex items-center justify-center text-accent-700 dark:text-accent-300">
                  <activeTheory.icon className="w-6 h-6" />
                </div>
                <div>
                  <div className="font-mono text-xs text-ink-500">{activeTheory.id}</div>
                  <h3 className="font-serif text-xl font-semibold leading-tight">
                    {activeTheory.title}
                  </h3>
                </div>
              </div>
              <div className="space-y-3 text-sm">
                <div>
                  <div className="text-[10px] uppercase tracking-wider font-semibold text-ink-500 dark:text-ink-400 mb-1">
                    Perfil ST
                  </div>
                  <code
                    className={cn(
                      'inline-block text-xs px-2 py-1 rounded',
                      PROFILE_COLOR[activeTheory.profile] ?? 'bg-ink-100 dark:bg-ink-800'
                    )}
                  >
                    {activeTheory.profile}
                  </code>
                </div>
                <div>
                  <div className="text-[10px] uppercase tracking-wider font-semibold text-ink-500 dark:text-ink-400 mb-1">
                    Foco
                  </div>
                  <p className="text-ink-700 dark:text-ink-300 leading-relaxed">
                    {activeTheory.focus}
                  </p>
                </div>
                <div>
                  <div className="text-[10px] uppercase tracking-wider font-semibold text-ink-500 dark:text-ink-400 mb-1">
                    Estado
                  </div>
                  <span
                    className={cn(
                      'inline-flex items-center gap-1.5 px-2 py-1 rounded-md text-xs border',
                      STATUS_LABELS[activeTheory.status].cls
                    )}
                  >
                    {(() => {
                      const Icon = STATUS_LABELS[activeTheory.status].icon;
                      return <Icon className="w-3.5 h-3.5" />;
                    })()}
                    {STATUS_LABELS[activeTheory.status].label}
                  </span>
                </div>
              </div>
              <div className="mt-5 pt-4 border-t border-ink-200 dark:border-ink-800 text-xs text-ink-500 dark:text-ink-400">
                Archivo fuente:{' '}
                <code>08-consistencia-st/theories/{String(activeTheory.number).padStart(2, '0')}-*.st</code>
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* Footer informativo */}
      <section className="card p-5 bg-gradient-to-br from-scholar-50 to-accent-50 dark:from-scholar-900/20 dark:to-accent-900/10 border-scholar-200 dark:border-scholar-800/50">
        <div className="flex items-start gap-3">
          <ShieldCheck className="w-5 h-5 text-scholar-600 dark:text-scholar-400 flex-none mt-0.5" />
          <div className="text-sm text-ink-700 dark:text-ink-300 leading-relaxed">
            <strong className="text-ink-900 dark:text-ink-100">¿Qué prueba la suite?</strong>{' '}
            ST verifica consistencia interna del aparato lógico-formal del manuscrito: que las
            tesis principales no se contradicen entre sí, que los argumentos modales declaran
            su sistema, que las afirmaciones existenciales no se confunden con universales.{' '}
            <strong>No demuestra verdad ontológica</strong>. Es{' '}
            <em>analizador de consistencia</em>, no oráculo. Cuando ST detecta un fallo, el
            manuscrito se refina; cuando ST aprueba, la coherencia interna está atestada bajo
            su modelo formal.
          </div>
        </div>
      </section>
    </div>
  );
}

function KpiTile({
  icon: Icon,
  label,
  value,
  accent,
}: {
  icon: React.ComponentType<{ className?: string }>;
  label: string;
  value: number | string;
  accent: 'ink' | 'success' | 'warning' | 'accent';
}) {
  const colors = {
    ink: 'text-ink-700 dark:text-ink-200',
    success: 'text-success',
    warning: 'text-warning',
    accent: 'text-accent-600 dark:text-accent-400',
  }[accent];
  return (
    <div className="card p-4 relative overflow-hidden group">
      <Icon className={cn('w-4 h-4 mb-2', colors)} />
      <div className="text-[10px] uppercase tracking-wider font-medium text-ink-500 dark:text-ink-400">
        {label}
      </div>
      <div className={cn('text-2xl font-semibold tabular-nums mt-0.5', colors)}>{value}</div>
    </div>
  );
}

/** Aplica colores naive al log según prefijos típicos de st-cli. */
function colorizeLog(raw: string): React.ReactNode {
  return raw.split('\n').map((line, i) => {
    let cls = 'text-ink-300';
    if (/✓|PASS|OK|SUCCESS/i.test(line)) cls = 'text-success';
    else if (/✗|FAIL|ERROR/i.test(line)) cls = 'text-danger';
    else if (/⚠|WARN/i.test(line)) cls = 'text-warning';
    else if (/^\s*\[T\d+\]|theor/i.test(line)) cls = 'text-accent-300';
    else if (/^\s*\$|^>/.test(line)) cls = 'text-scholar-300';
    return (
      <span key={i} className={cls + ' block'}>
        {line || ' '}
      </span>
    );
  });
}
