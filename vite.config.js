import { defineConfig } from 'vite';

export default defineConfig({
  build: {
    outDir: 'static/dist',  // Output to Django's static folder
    emptyOutDir: true,      // Empty the directory before building
    assetsDir: '',          // Don't add an extra 'assets' subfolder

    // Define the entry points for JS and CSS
    rollupOptions: {
      input: {
        main: 'static/src/js/main.js',
        styles: 'static/src/input.css',
      }
    }
  },
  server: {
    proxy: {
      '/': 'http://localhost:8000', // Proxy API calls to Django backend (for development)
    },
  },
});
