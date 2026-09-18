const { chromium } = require('playwright-core');
const path = require('path'), fs = require('fs');
(async () => {
  const [,, outDir, fpsArg, durArg, timesArg] = process.argv;
  const fps = Number(fpsArg||24), dur = Number(durArg||2.5);
  fs.mkdirSync(outDir, { recursive: true });
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  await p.goto('file://' + path.resolve('endcard.html'));
  await p.evaluate(() => document.fonts.ready);
  const times = timesArg ? timesArg.split(',').map(Number) : Array.from({length: Math.round(dur*fps)}, (_, i) => i/fps);
  for (let i = 0; i < times.length; i++) {
    await p.evaluate(t => window.render(t), times[i]);
    await p.screenshot({ path: path.join(outDir, (timesArg ? `t${times[i].toFixed(2)}` : String(i).padStart(4,'0')) + '.png') });
  }
  console.log('rendered', times.length, 'frames to', outDir);
  await b.close();
})().catch(e => { console.error(e); process.exit(1); });
