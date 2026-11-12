const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const viewports = [
  { name: 'Mobile_SE', width: 375, height: 667 },
  { name: 'Mobile_Pro', width: 390, height: 844 },
  { name: 'Tablet_iPad', width: 768, height: 1024 },
  { name: 'Desktop_Standard', width: 1280, height: 800 },
  { name: 'Desktop_Large', width: 1920, height: 1080 }
];

const testUrls = [
  'http://localhost:8089/',
  'http://localhost:8089/courses/excel-power-bi-tableau-course/',
  'http://localhost:8089/courses/python-programming-course/',
  'http://localhost:8089/courses/sql-course/',
  'http://localhost:8089/courses/machine-learning-course/',
  'http://localhost:8089/courses/data-science-course/',
  'http://localhost:8089/courses/data-science-and-ai-course/',
  'http://localhost:8089/courses/data-analytics-course/',
  'http://localhost:8089/courses/ai-ml-course/',
  'http://localhost:8089/trainers/',
  'http://localhost:8089/blogs/',
  'http://localhost:8089/blog/2026-breakthroughs-in-ai-agents-llms/'
];

(async () => {
  const browser = await chromium.launch();
  const issues = [];
  const ssDir = path.join(__dirname, 'playwright_screenshots');
  if (!fs.existsSync(ssDir)) fs.mkdirSync(ssDir, { recursive: true });

  for (const vp of viewports) {
    console.log(`\nTesting viewport: ${vp.name} (${vp.width}x${vp.height})`);
    const context = await browser.newContext({ viewport: { width: vp.width, height: vp.height } });
    const page = await context.newPage();

    for (const url of testUrls) {
      try {
        const pageErrors = [];
        page.on('pageerror', err => pageErrors.push(err.message));

        await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 15000 });
        await page.waitForTimeout(500);

        // 1. Check Horizontal Overflow (User cannot horizontally scroll unless intended)
        const overflow = await page.evaluate(() => {
          return {
            scrollWidth: document.documentElement.scrollWidth,
            clientWidth: document.documentElement.clientWidth,
            hasOverflow: document.documentElement.scrollWidth > document.documentElement.clientWidth
          };
        });

        if (overflow.hasOverflow) {
          const offendingEl = await page.evaluate(() => {
            const docWidth = document.documentElement.clientWidth;
            const elements = Array.from(document.querySelectorAll('*'));
            const wide = elements.filter(el => {
              const rect = el.getBoundingClientRect();
              return rect.right > docWidth + 2; // allowance
            });
            return wide.slice(0, 3).map(el => ({
              tag: el.tagName,
              className: el.className,
              id: el.id,
              right: el.getBoundingClientRect().right
            }));
          });
          issues.push({
            type: 'HORIZONTAL_OVERFLOW',
            viewport: vp.name,
            url,
            scrollWidth: overflow.scrollWidth,
            clientWidth: overflow.clientWidth,
            offending: offendingEl
          });
        }

        // 2. Check Broken Images (naturalWidth === 0)
        const brokenImages = await page.evaluate(() => {
          const imgs = Array.from(document.querySelectorAll('img'));
          return imgs.filter(img => !img.complete || img.naturalWidth === 0).map(img => ({
            src: img.src,
            alt: img.alt,
            className: img.className
          }));
        });

        if (brokenImages.length > 0) {
          issues.push({
            type: 'BROKEN_IMAGE',
            viewport: vp.name,
            url,
            images: brokenImages
          });
        }

        // 3. Check Overlapping or Negative Sized SVGs
        const badSvgs = await page.evaluate(() => {
          const svgs = Array.from(document.querySelectorAll('svg'));
          return svgs.filter(s => {
            const rect = s.getBoundingClientRect();
            // visible svgs with 0 width or height
            return s.offsetParent !== null && (rect.width === 0 || rect.height === 0);
          }).map(s => ({
            parentClass: s.parentElement ? s.parentElement.className : '',
            viewBox: s.getAttribute('viewBox')
          }));
        });

        if (badSvgs.length > 0) {
          issues.push({
            type: 'ZERO_SIZE_SVG',
            viewport: vp.name,
            url,
            svgs: badSvgs
          });
        }

        // Capture screenshot of course page curriculum
        if (url.includes('short-course') || url.includes('python-programming') || url.includes('excel-power-bi')) {
          const urlSlug = url.split('/').filter(Boolean).pop();
          const ssPath = path.join(ssDir, `${urlSlug}_${vp.name}.png`);
          await page.screenshot({ path: ssPath, fullPage: false });
        }

      } catch (err) {
        issues.push({
          type: 'PAGE_LOAD_ERROR',
          viewport: vp.name,
          url,
          error: err.message
        });
      }
    }
    await context.close();
  }

  await browser.close();

  console.log('\n=======================================');
  console.log(`TOTAL UI ISSUES FOUND: ${issues.length}`);
  console.log('=======================================');
  console.log(JSON.stringify(issues, null, 2));

  fs.writeFileSync(path.join(__dirname, 'playwright_report.json'), JSON.stringify(issues, null, 2));
})();

