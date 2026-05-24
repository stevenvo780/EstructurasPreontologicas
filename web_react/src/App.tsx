import { Routes, Route, Navigate, useLocation } from 'react-router-dom';
import Layout from './components/Layout';
import Dashboard from './pages/Dashboard';
import Cases from './pages/Cases';
import CaseDetail from './pages/CaseDetail';
import Chapters from './pages/Chapters';
import ChapterDetail from './pages/ChapterDetail';
import Thesis from './pages/Thesis';
import ST from './pages/ST';
import Bibliography from './pages/Bibliography';
import About from './pages/About';
import NotFound from './pages/NotFound';

function TrailingSlashFallback() {
  const { pathname, search, hash } = useLocation();
  if (pathname.length > 1 && pathname.endsWith('/')) {
    const stripped = pathname.replace(/\/+$/, '') || '/';
    return <Navigate to={`${stripped}${search}${hash}`} replace />;
  }
  return <NotFound />;
}

export default function App() {
  return (
    <Routes>
      <Route element={<Layout />}>
        <Route path="/" element={<Dashboard />} />
        <Route path="/index.html" element={<Navigate to="/" replace />} />
        <Route path="/tesis" element={<Thesis />} />
        <Route path="/casos" element={<Cases />} />
        <Route path="/casos/:caseId" element={<CaseDetail />} />
        <Route path="/capitulos" element={<Chapters />} />
        <Route path="/capitulos/:slug" element={<ChapterDetail />} />
        <Route path="/bibliografia" element={<Bibliography />} />
        <Route path="/st" element={<ST />} />
        <Route path="/about" element={<About />} />
        <Route path="*" element={<TrailingSlashFallback />} />
      </Route>
    </Routes>
  );
}
