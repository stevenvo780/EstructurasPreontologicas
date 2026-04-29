/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        // Paleta editorial sobria, alto contraste
        ink: {
          50: '#f7f8fa',
          100: '#eef0f4',
          200: '#dde1e9',
          300: '#bcc4d1',
          400: '#8d97a8',
          500: '#5d6779',
          600: '#3f4858',
          700: '#2a3140',
          800: '#1a1f2c',
          900: '#0e1219',
          950: '#070a10',
        },
        accent: {
          50: '#fff8eb',
          100: '#ffeac6',
          200: '#fdd089',
          300: '#fbb24d',
          400: '#f99524',
          500: '#e4760a',
          600: '#bd5705',
          700: '#964007',
          800: '#7b330d',
          900: '#682b0e',
        },
        scholar: {
          50: '#f3f6fb',
          100: '#e3ecf5',
          200: '#cedfee',
          300: '#a6c5e0',
          400: '#76a5cf',
          500: '#5388bd',
          600: '#3f6ea3',
          700: '#345984',
          800: '#2f4c6e',
          900: '#2b405c',
        },
        success: '#16a34a',
        warning: '#eab308',
        danger: '#dc2626',
      },
      fontFamily: {
        sans: ['"Inter"', 'system-ui', '-apple-system', 'sans-serif'],
        serif: ['"Source Serif 4"', '"Iowan Old Style"', 'Georgia', 'serif'],
        mono: ['"JetBrains Mono"', '"SF Mono"', 'Menlo', 'monospace'],
      },
      typography: () => ({
        DEFAULT: {
          css: {
            maxWidth: 'none',
          },
        },
      }),
      animation: {
        'fade-in': 'fadeIn 200ms ease-out',
        'slide-in': 'slideIn 250ms ease-out',
        'pulse-slow': 'pulse 3s ease-in-out infinite',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: 0 },
          '100%': { opacity: 1 },
        },
        slideIn: {
          '0%': { opacity: 0, transform: 'translateY(-8px)' },
          '100%': { opacity: 1, transform: 'translateY(0)' },
        },
      },
    },
  },
  plugins: [],
};
