import { useEffect, useRef } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import rehypeRaw from 'rehype-raw';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { atomDark, oneLight } from 'react-syntax-highlighter/dist/esm/styles/prism';
import mermaid from 'mermaid';
import { useTheme } from '../hooks/useTheme';

interface MarkdownProps {
  content: string;
  className?: string;
}

let mermaidInitialized = false;

function ensureMermaid(theme: 'light' | 'dark') {
  if (!mermaidInitialized) {
    mermaid.initialize({
      startOnLoad: false,
      theme: theme === 'dark' ? 'dark' : 'default',
      securityLevel: 'loose',
      fontFamily: '"Inter", system-ui, sans-serif',
    });
    mermaidInitialized = true;
  } else {
    mermaid.initialize({
      startOnLoad: false,
      theme: theme === 'dark' ? 'dark' : 'default',
      securityLevel: 'loose',
      fontFamily: '"Inter", system-ui, sans-serif',
    });
  }
}

/**
 * Renderiza markdown con KaTeX, GFM, mermaid y syntax-highlighting.
 * Acepta también HTML embebido del backend (rehype-raw).
 */
export default function Markdown({ content, className = '' }: MarkdownProps) {
  const { theme } = useTheme();
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!ref.current) return;
    ensureMermaid(theme);
    const blocks = ref.current.querySelectorAll<HTMLElement>('code.language-mermaid');
    blocks.forEach((block, idx) => {
      const wrapper = block.parentElement;
      if (!wrapper) return;
      const id = `mermaid-${Date.now()}-${idx}`;
      const code = block.textContent || '';
      const div = document.createElement('div');
      div.className = 'mermaid';
      div.id = id;
      wrapper.replaceWith(div);
      mermaid
        .render(`${id}-svg`, code)
        .then(({ svg }) => {
          div.innerHTML = svg;
        })
        .catch((err) => {
          div.innerHTML = `<pre class="text-xs text-danger">Error mermaid: ${err.message}</pre>`;
        });
    });
  }, [content, theme]);

  return (
    <div ref={ref} className={`prose-academic max-w-none ${className}`}>
      <ReactMarkdown
        remarkPlugins={[remarkGfm, remarkMath]}
        rehypePlugins={[rehypeKatex, rehypeRaw]}
        components={{
          code({ className: cls, children, ...props }) {
            const match = /language-(\w+)/.exec(cls || '');
            const lang = match?.[1];
            const inline = !lang;
            const codeStr = String(children).replace(/\n$/, '');
            if (inline) {
              return (
                <code className={cls} {...props}>
                  {children}
                </code>
              );
            }
            if (lang === 'mermaid') {
              return <code className="language-mermaid">{codeStr}</code>;
            }
            return (
              <SyntaxHighlighter
                style={(theme === 'dark' ? atomDark : oneLight) as any}
                language={lang || 'text'}
                PreTag="div"
                customStyle={{
                  margin: '1.4em 0',
                  borderRadius: '0.6rem',
                  fontSize: '0.85em',
                  padding: '1em 1.2em',
                }}
              >
                {codeStr}
              </SyntaxHighlighter>
            );
          },
          h1: (p) => <h1 {...p} id={slugify(textOf(p.children))} />,
          h2: (p) => <h2 {...p} id={slugify(textOf(p.children))} />,
          h3: (p) => <h3 {...p} id={slugify(textOf(p.children))} />,
          a: ({ href, children, ...rest }) => {
            const isExternal = href?.startsWith('http');
            return (
              <a
                href={href}
                target={isExternal ? '_blank' : undefined}
                rel={isExternal ? 'noreferrer' : undefined}
                {...rest}
              >
                {children}
              </a>
            );
          },
          table: (p) => (
            <div className="overflow-x-auto my-4">
              <table {...p} />
            </div>
          ),
        }}
      >
        {content}
      </ReactMarkdown>
    </div>
  );
}

function textOf(node: unknown): string {
  if (typeof node === 'string') return node;
  if (Array.isArray(node)) return node.map(textOf).join('');
  if (node && typeof node === 'object' && 'props' in (node as any))
    return textOf((node as any).props.children);
  return '';
}

function slugify(s: string): string {
  return s
    .toLowerCase()
    .normalize('NFKD')
    .replace(/[̀-ͯ]/g, '')
    .replace(/[^a-z0-9\s-]/g, '')
    .trim()
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-');
}
