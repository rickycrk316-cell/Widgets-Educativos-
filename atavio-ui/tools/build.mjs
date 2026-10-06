// Build de @atavio/ui: JS (esbuild, ESM), tipos (tsc), CSS y fuentes a dist/.
import { build } from 'esbuild';
import { execFileSync } from 'node:child_process';
import { cpSync, mkdirSync, rmSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const dist = path.join(root, 'dist');
rmSync(dist, { recursive: true, force: true });
mkdirSync(dist, { recursive: true });

await build({
  entryPoints: [path.join(root, 'src/index.ts')],
  outfile: path.join(dist, 'index.es.js'),
  bundle: true, format: 'esm', platform: 'browser', target: 'es2020',
  jsx: 'automatic', external: ['react', 'react-dom', 'react/jsx-runtime'],
  sourcemap: false, logLevel: 'info',
});
execFileSync(process.execPath, [path.join(root, 'node_modules/typescript/bin/tsc'), '-p', root], { stdio: 'inherit' });
cpSync(path.join(root, 'src/style.css'), path.join(dist, 'style.css'));
cpSync(path.join(root, 'fonts'), path.join(dist, 'fonts'), { recursive: true });
console.log('dist listo');
