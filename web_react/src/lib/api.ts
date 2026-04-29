// Cliente API tipado para el backend FastAPI

const API_BASE = import.meta.env.DEV ? '' : '';

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const res = await fetch(`${API_BASE}${path}`, {
    headers: { 'Content-Type': 'application/json', ...(init?.headers || {}) },
    ...init,
  });
  if (!res.ok) {
    const text = await res.text().catch(() => '');
    throw new Error(`HTTP ${res.status} en ${path}: ${text || res.statusText}`);
  }
  return res.json() as Promise<T>;
}

export const api = {
  summary: () => request<import('../types').Summary>('/api/summary'),
  cases: () => request<import('../types').Case[]>('/api/cases'),
  case: (id: string) => request<import('../types').CaseDetail>(`/api/casos/${id}`),
  chapters: () => request<import('../types').Chapter[]>('/api/chapters'),
  chapter: (slug: string) =>
    request<import('../types').ChapterDetail>(`/api/chapters/${slug}`),
  thesis: () => request<import('../types').ThesisData>('/api/thesis'),
  runST: () =>
    request<{ success: boolean; log: string; html: string }>('/api/run-st', {
      method: 'POST',
    }),
};
