import { useEffect, useRef } from 'react';
import { useTheme } from '../hooks/useTheme';
import mermaid from 'mermaid';

interface HtmlContentProps {
  html: string;
  className?: string;
}

let mermaidInitialized = false;

/**
 * Renderiza HTML pre-procesado del backend (markdown-it).
 * Aplica mermaid sobre bloques pre>code.language-mermaid y observa cambios de tema.
 */
export default function HtmlContent({ html, className = '' }: HtmlContentProps) {
  const ref = useRef<HTMLDivElement>(null);
  const { theme } = useTheme();

  useEffect(() => {
    if (!ref.current) return;
    if (!mermaidInitialized) {
      mermaid.initialize({
        startOnLoad: false,
        theme: theme === 'dark' ? 'dark' : 'default',
        securityLevel: 'loose',
        fontFamily: '"Inter", system-ui, sans-serif',
      });
      mermaidInitialized = true;
    }
    const blocks = ref.current.querySelectorAll<HTMLElement>(
      'pre code.language-mermaid, pre code[class*="language-mermaid"]'
    );
    blocks.forEach(async (block, idx) => {
      const wrapper = block.parentElement;
      if (!wrapper) return;
      const code = block.textContent || '';
      const id = `mermaid-rendered-${Date.now()}-${idx}`;
      const div = document.createElement('div');
      div.className = 'mermaid';
      div.id = id;
      try {
        const { svg } = await mermaid.render(`${id}-svg`, code);
        div.innerHTML = svg;
        wrapper.replaceWith(div);
      } catch (err: any) {
        div.innerHTML = `<pre class="text-xs text-danger">Mermaid error: ${err?.message || err}</pre>`;
        wrapper.replaceWith(div);
      }
    });
  }, [html, theme]);

  return (
    <div
      ref={ref}
      className={`prose-academic max-w-none ${className}`}
      dangerouslySetInnerHTML={{ __html: html }}
    />
  );
}
