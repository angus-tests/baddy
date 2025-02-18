import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
  root: 'assets',  // Vite serves files from 'assets'
  publicDir: false,  // Disable public assets (handled manually)
  build: {
    outDir: resolve(__dirname, 'static/dist'),  // Build output goes into 'static/dist'
    emptyOutDir: true,  // Clean 'static/dist' before building
    assetsDir: '',  // Prevent Vite from nesting assets under 'assets/'
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'assets/js/main.js'),  // Ensure correct JS path
        styles: resolve(__dirname, 'assets/input.css'),  // Ensure correct CSS path
      },
    },
    manifest: true,  // Optionally, generate a manifest file to map the assets
  },
});
