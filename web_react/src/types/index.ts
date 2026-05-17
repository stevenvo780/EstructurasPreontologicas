// Tipos compartidos de la API

export interface Summary {
  presentation?: {
    title: string;
    subtitle: string;
    source_path: string;
    resumen_html: string;
    resumen_excerpt_html: string;
    abstract_html: string;
    bibliografia_html: string;
    key_lesson_html: string;
    limitations_html: string;
    keywords: string[];
  };
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
  top_cases?: {
    case_id: string;
    case_num?: number | null;
    title: string;
    edi?: number | null;
    category?: string;
    scope?: string;
  }[];
  corpus_scope?: {
    visible_metrics: number;
    declared_core_cases: number;
    core_inter_domain: number;
    multiscale: number;
    extensions: number;
    by_scope: { scope: string; count: number }[];
    note: string;
  };
  by_domain?: { domain: string; count: number }[];
  scatter?: { id: string; case_name: string; edi: number; p?: number; category: string }[];
}

export interface Case {
  case_id: string;
  sim_path?: string;
  scope?: string;
  case_num: number | null;
  case_name: string;
  title: string;
  category: string;
  scale?: string | null;
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
  loe?: number | null;
}

export interface PhaseSummary {
  overall_pass: boolean;
  edi: number | null;
  edi_ci_lo?: number | null;
  edi_ci_hi?: number | null;
  pvalue: number | null;
  significant?: boolean | null;
  cr?: number | null;
  category?: string | null;
  nivel?: number | null;
}

export interface CaseDetail extends Case {
  phase_order?: string[];
  phases?: Record<string, PhaseSummary>;
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
  extras?: ChapterExtraSummary[];
}

export interface ChapterDetail {
  slug: string;
  code: string;
  title: string;
  description?: string;
  docs: ChapterDoc[];
  extras?: ChapterExtraSummary[];
}

export interface ChapterDoc {
  title: string;
  path: string;
  html: string;
  toc?: TocItem[];
}

export interface ChapterExtraSummary {
  name: string;
  title: string;
  extends?: string | null;
  mtime?: number;
}

export interface ChapterExtrasResponse {
  slug: string;
  extras: ChapterExtraSummary[];
}

export interface ChapterExtraContent {
  name: string;
  title: string;
  extends?: string | null;
  html: string;
  toc?: TocItem[];
  mtime?: number;
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
