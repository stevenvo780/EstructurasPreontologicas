import { useState } from 'react';
import { ShieldCheck, Play, Loader2, Terminal, CheckCircle2, XCircle } from 'lucide-react';
import { useMutation } from '@tanstack/react-query';
import toast from 'react-hot-toast';
import { api } from '../lib/api';
import HtmlContent from '../components/HtmlContent';

export default function ST() {
  const [output, setOutput] = useState<string>('');
  const [reportHtml, setReportHtml] = useState<string>('');
  const [success, setSuccess] = useState<boolean | null>(null);

  const runMutation = useMutation({
    mutationFn: api.runST,
    onSuccess: (data) => {
      setOutput(data.log);
      setReportHtml(data.html);
      setSuccess(data.success);
      if (data.success) toast.success('Suite ST ejecutada correctamente');
      else toast.error('Suite ST falló');
    },
    onError: (err) => {
      toast.error(`Error: ${err instanceof Error ? err.message : 'desconocido'}`);
    },
  });

  return (
    <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-8 lg:py-10">
      <header className="mb-6">
        <div className="flex items-center gap-2 text-xs uppercase tracking-wider text-ink-500 dark:text-ink-400 mb-2">
          <ShieldCheck className="w-3.5 h-3.5" />
          Validación lógica formal
        </div>
        <h1 className="font-serif text-3xl md:text-4xl font-semibold tracking-tight">
          Suite ST
        </h1>
        <p className="mt-2 text-ink-600 dark:text-ink-400 max-w-3xl">
          Capa de consistencia lógica del manuscrito mediante el lenguaje{' '}
          <code className="text-xs">@stevenvo780/st-lang</code>. La suite cubre 24 teorías:
          asimetría L1↔B↔L3↔S, operadores formales, condiciones de overall_pass, discriminación
          contra rivales, niveles del paisaje, falsabilidad, coherencia modal y paraconsistencia.
        </p>
      </header>

      <div className="card p-5 mb-6">
        <div className="flex items-center justify-between gap-4 flex-wrap">
          <div>
            <h3 className="font-semibold text-ink-800 dark:text-ink-100 mb-1">
              Ejecutar suite completa
            </h3>
            <p className="text-xs text-ink-500 dark:text-ink-400">
              Corre <code>npm run st:check</code> en el directorio <code>08-consistencia-st</code> y
              renderiza el reporte generado.
            </p>
          </div>
          <button
            onClick={() => runMutation.mutate()}
            disabled={runMutation.isPending}
            className="btn-primary"
          >
            {runMutation.isPending ? (
              <>
                <Loader2 className="w-4 h-4 animate-spin" />
                Ejecutando…
              </>
            ) : (
              <>
                <Play className="w-4 h-4" />
                Ejecutar
              </>
            )}
          </button>
        </div>
        {success !== null && (
          <div
            className={`mt-4 flex items-center gap-2 px-3 py-2 rounded-lg text-sm ${
              success
                ? 'bg-success/10 text-success border border-success/30'
                : 'bg-danger/10 text-danger border border-danger/30'
            }`}
          >
            {success ? (
              <CheckCircle2 className="w-4 h-4" />
            ) : (
              <XCircle className="w-4 h-4" />
            )}
            {success ? 'Última ejecución: éxito' : 'Última ejecución: errores detectados'}
          </div>
        )}
      </div>

      <div className="grid lg:grid-cols-2 gap-6">
        {output && (
          <div className="card p-5">
            <h3 className="font-semibold text-ink-800 dark:text-ink-100 mb-3 flex items-center gap-2">
              <Terminal className="w-4 h-4 text-accent-500" />
              Salida del runner
            </h3>
            <pre className="bg-ink-900 dark:bg-ink-950 text-ink-100 rounded-lg p-3 overflow-x-auto text-[11px] leading-relaxed font-mono max-h-[60vh]">
              {output}
            </pre>
          </div>
        )}
        {reportHtml && (
          <div className="card p-5 lg:col-span-2">
            <h3 className="font-semibold text-ink-800 dark:text-ink-100 mb-3">
              Último reporte generado
            </h3>
            <HtmlContent html={reportHtml} />
          </div>
        )}
      </div>
    </div>
  );
}
