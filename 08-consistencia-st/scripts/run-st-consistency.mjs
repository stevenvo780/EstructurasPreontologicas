import { spawnSync } from 'node:child_process';
import { existsSync, mkdirSync, writeFileSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const projectRoot = path.resolve(__dirname, '..');
const reportsDir = path.join(projectRoot, 'reports');
const stBin = path.join(projectRoot, 'node_modules', '.bin', 'st');
const verbose = process.argv.includes('--verbose');

const suite = [
  { file: 'theories/00-nucleo-ontologico.st', mode: 'check' },
  { file: 'theories/01-criterios-legitimidad.st', mode: 'check' },
  { file: 'theories/02-debates-y-limites.st', mode: 'check' },
  { file: 'theories/03-text-layer-tesis.st', mode: 'run' },
  { file: 'theories/04-text-layer-bibliografia.st', mode: 'run' },
  { file: 'theories/05-asimetria-l1-b-l3-s.st', mode: 'run' },
  { file: 'theories/06-operadores-y-circularidad.st', mode: 'run' },
  { file: 'theories/07-overall-pass-13-condiciones.st', mode: 'run' },
  { file: 'theories/08-discriminacion-rivales.st', mode: 'run' },
  { file: 'theories/09-niveles-paisaje.st', mode: 'run' },
  { file: 'theories/10-falsabilidad.st', mode: 'run' },
  { file: 'theories/11-modal-coherencia-epistemica.st', mode: 'run' },
  { file: 'theories/12-paraconsistencia-wolfram.st', mode: 'run' }
];

mkdirSync(reportsDir, { recursive: true });

if (!existsSync(stBin)) {
  const message = [
    '# Reporte de consistencia ST',
    '',
    '❌ No se encontró el binario local de ST.',
    '',
    'Instala dependencias dentro de `08-consistencia-st/` antes de ejecutar la suite:',
    '',
    '```text',
    'npm install',
    'npm run st:check',
    '```',
    ''
  ].join('\n');

  const reportPath = path.join(reportsDir, 'ultimo-reporte.md');
  writeFileSync(reportPath, message, 'utf8');
  console.error(`No se encontró ST en ${stBin}. Instala dependencias primero.`);
  process.exit(1);
}

const sections = ['# Reporte de consistencia ST', ''];
let hasFailures = false;

for (const entry of suite) {
  const args = [entry.mode, `./${entry.file}`];
  const result = spawnSync(stBin, args, {
    cwd: projectRoot,
    encoding: 'utf8',
    shell: false
  });

  const status = result.status ?? 1;
  const stdout = (result.stdout || '').trim();
  const stderr = (result.stderr || '').trim();
  const ok = status === 0;
  if (!ok) hasFailures = true;

  if (verbose) {
    console.log(`\n==> ${entry.mode.toUpperCase()} ${entry.file}`);
    if (stdout) console.log(stdout);
    if (stderr) console.error(stderr);
  }

  sections.push(`## ${entry.file}`);
  sections.push('');
  sections.push(`- modo: \`${entry.mode}\``);
  sections.push(`- estado: ${ok ? '✅ ok' : '❌ fallo'}`);
  sections.push(`- código de salida: \`${status}\``);
  sections.push('');
  sections.push('### stdout');
  sections.push('');
  sections.push('```text');
  sections.push(stdout || '(sin salida)');
  sections.push('```');
  sections.push('');

  if (stderr) {
    sections.push('### stderr');
    sections.push('');
    sections.push('```text');
    sections.push(stderr);
    sections.push('```');
    sections.push('');
  }
}

sections.push('## Estado global');
sections.push('');
sections.push(hasFailures ? '❌ La suite encontró fallos.' : '✅ La suite pasó completa.');
sections.push('');

const reportPath = path.join(reportsDir, 'ultimo-reporte.md');
writeFileSync(reportPath, sections.join('\n'), 'utf8');

console.log(hasFailures ? `Suite ST con fallos. Revisa ${reportPath}` : `Suite ST completada. Reporte en ${reportPath}`);
process.exit(hasFailures ? 1 : 0);
