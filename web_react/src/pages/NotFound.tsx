import { Link } from 'react-router-dom';
import { FileQuestion, Home } from 'lucide-react';

export default function NotFound() {
  return (
    <div className="mx-auto max-w-2xl px-4 py-24 text-center">
      <FileQuestion className="w-16 h-16 mx-auto text-ink-300 dark:text-ink-700 mb-4" />
      <h1 className="font-serif text-3xl font-semibold mb-2">Sección no encontrada</h1>
      <p className="text-ink-500 dark:text-ink-400 mb-6">
        La ruta solicitada no existe en la web de la tesis.
      </p>
      <Link to="/" className="btn-primary inline-flex">
        <Home className="w-4 h-4" />
        Volver al inicio
      </Link>
    </div>
  );
}
