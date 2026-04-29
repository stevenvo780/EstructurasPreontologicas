// Tipos compartidos de la API

export interface Summary {
  stats: {
    total_cases: number;
    overall_pass: number;
    weak_or_better: number;
    null_count: number;
    falsified: number;
    median_edi?: number;
    mean_edi?: number;
  };
  distribution: { category: string; count: number }[];
  level_breakdown?: { level: number; count: number; label?: string }[];
  by_domain?: { domain: string; count: number }[];
  scatter?: { id: string; case_name: string; edi: number; p?: number; category: string }[];
}

export interface Case {
  case_id: string;
  case_num: number | null;
  case_name: string;
  title: string;
  category: string;
  metrics: {
    edi: number | null;
    pvalue: number | null;
    cr: number | null;
    overall_pass: boolean;
    nivel: number | null;
    category: string;
  };
  meta?: {
    generated_at?: string;
    git?: { commit?: string; dirty?: boolean };
  };
  domain?: string;
  scale?: string;
  loe?: number | null;
}

export interface CaseDetail extends Case {
  phase_order?: string[];
  report_html?: string;
  thesis_readme_html?: string;
  thesis_docs_html?: { title: string; html: string }[];
  math_explainer_html?: string;
  raw_metrics?: Record<string, unknown>;
  primary_arrays?: {
    obs: number[];
    abm_coupled?: number[];
    abm_no_ode?: number[];
    ode_pred?: number[];
    forcing?: number[];
  };
}

export interface Chapter {
  slug: string;
  code: string;
  title: string;
  description?: string;
  docs: { title: string; path: string; size?: number }[];
}

export interface ChapterDetail {
  slug: string;
  code: string;
  title: string;
  description?: string;
  docs: ChapterDoc[];
}

export interface ChapterDoc {
  title: string;
  path: string;
  html: string;
  toc?: TocItem[];
}

export interface TocItem {
  level: number;
  title: string;
  anchor: string;
}

export interface ThesisData {
  html: string;
  toc: TocItem[];
  word_count?: number;
  line_count?: number;
}
