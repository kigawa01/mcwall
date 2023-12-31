// vite.config.js
import {defineConfig} from 'vite'
import * as path from "path";

const root = path.resolve(__dirname, "front")
const cssDir = path.resolve(root, "css")
export default defineConfig({
  root: root,
  base: "./",
  build: {
    outDir: path.resolve(__dirname, "static"),
    emptyOutDir: false,
    rollupOptions: {
      input: {
        common: path.resolve(cssDir, "common", "common.scss"),
        "content-page": path.resolve(cssDir, "page", "content-page.scss"),
        "mcwall-index": path.resolve(cssDir, "page", "mcwall-index.scss"),
        "mcwall-detail": path.resolve(cssDir, "page", "mcwall-detail.scss"),
        "mcwall-create": path.resolve(cssDir, "page", "mcwall-create.scss"),
        "user": path.resolve(cssDir, "page", "user.scss"),
        main: path.resolve(root, "script", "main.tsx"),
      },
      output: { // entry chunk assets それぞれの書き出し名の指定
        assetFileNames: (config) => {
          if (config.name?.endsWith(".html")) return `${config.name}`
          if (config.name?.endsWith(".js")) return `script/${config.name}`
          if (config.name?.endsWith(".css")) return `css/${config.name}`
          if ([
            ".png", ".jpg"
          ].find((ext) => {
            return config.name?.toLowerCase()?.endsWith(ext)
          })) return `images/${config.name}`
          return `assets/${config.name}` || "undefined"
        }
      },
    },
    cssCodeSplit: true,
    cssMinify: false,
  },
  optimizeDeps: {
    exclude: [
      "./css/reset.css",
      "./css/common.scss"
    ]
  }
})