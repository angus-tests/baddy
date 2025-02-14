import { defineConfig } from 'vite';

export default defineConfig({
  root: 'assets', // This makes sure Vite serves from the 'static' folder
  publicDir: 'static', // This makes sure assets are served from 'static' as well
  build: {
    outDir: 'dist',  // This will build to Django's static folder
    emptyOutDir: true,
    assetsDir: '',
    rollupOptions: {
      input: {
        main: 'js/main.js',  // JS entry
        styles: 'input.css', // CSS entry
      },
    },
  },
});
