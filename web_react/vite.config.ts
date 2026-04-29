import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  build: {
    outDir: 'dist',
    emptyOutDir: true,
    sourcemap: false,
    chunkSizeWarningLimit: 1500,
    rollupOptions: {
      output: {
        manualChunks: {
          'react-vendor': ['react', 'react-dom', 'react-router-dom'],
          'markdown': ['react-markdown', 'remark-gfm', 'remark-math', 'rehype-katex', 'rehype-raw'],
          'charts': ['recharts'],
          'mermaid': ['mermaid'],
        },
      },
    },
  },
  server: {
    port: 5173,
    proxy: {
      '/api': 'http://127.0.0.1:8080',
      '/sim_files': 'http://127.0.0.1:8080',
      '/repo_files': 'http://127.0.0.1:8080',
      '/visualizations': 'http://127.0.0.1:8080',
    },
  },
});
