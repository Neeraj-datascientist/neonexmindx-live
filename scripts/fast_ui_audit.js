const { chromium } = require('playwright');

const urlsToTest = [
  '/',
  '/about-us/',
  '/trainers-and-mentors/',
  '/blogs/',
  '/blog/machine-learning-vs-deep-learning-differences-guide/',
  '/courses/data-science-course/',
  '/courses/data-science-and-ai-course/',
  '/courses/sql-course/',
  '/courses/python-programming-course/',
  '/courses/excel-power-bi-tableau-course/',
  '/courses/machine-learning-course/',
  '/syllabus/catalogues/sql-syllabus.html',
  '/cms/'
];

const viewports = [
  { name: 'Desktop (1440x900)', width: 1440, height: 900 },
  { name: 'Mobile (375x667)', width: 375, height: 667 },
  { name: 'Small Mobile (320x568)', width: 320, height: 568 }
];

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();

  const issues = [];

  for (const urlPath of urlsToTest) {
    const fullUrl = `http://localhost:8089${urlPath}`;
    for (const vp of viewports) {
      await page.setViewportSize({ width: vp.width, height: vp.height });
      const consoleErrors = [];

      const onConsole = msg => {
        if (msg.type() === 'error') consoleErrors.push(msg.text());
      };
      page.on('console', onConsole);

      try {
        await page.goto(fullUrl, { waitUntil: 'domcontentloaded', timeout: 5000 });

        // Check Horizontal Overflow
        const overflow = await page.evaluate(() => {
          const docWidth = document.documentElement.offsetWidth;
          const scrollWidth = document.documentElement.scrollWidth;
          const bodyScrollWidth = document.body ? document.body.scrollWidth : 0;
          const maxW = Math.max(scrollWidth, bodyScrollWidth);
          return {
            hasOverflow: maxW > docWidth + 3,
            diff: maxW - docWidth,
            docWidth,
            maxW
          };
        });

        if (overflow.hasOverflow) {
          const culprits = await page.evaluate(() => {
            const docW = document.documentElement.offsetWidth;
            const bad = [];
            document.querySelectorAll('*').forEach(el => {
              const rect = el.getBoundingClientRect();
              if (rect.right > docW + 3) {
                bad.push({
                  tag: el.tagName,
                  class: (el.className || '').toString().substring(0, 30),
                  id: el.id,
                  right: Math.round(rect.right)
                });
              }
            });
            return bad.slice(0, 3);
          });
          issues.push({
            type: 'HORIZONTAL_OVERFLOW',
            url: urlPath,
            viewport: vp.name,
            diff: overflow.diff,
            culprits
          });
        }

        // Check Broken Images
        const brokenImgs = await page.evaluate(() => {
          return Array.from(document.querySelectorAll('img')).filter(img => {
            if (!img.src || img.src.startsWith('data:image/gif')) return false;
            return img.naturalWidth === 0 && img.complete;
          }).map(img => img.src);
        });

        if (brokenImgs.length > 0) {
          issues.push({
            type: 'BROKEN_IMAGES',
            url: urlPath,
            viewport: vp.name,
            brokenImgs
          });
        }

        if (consoleErrors.length > 0) {
          issues.push({
            type: 'CONSOLE_ERRORS',
            url: urlPath,
            viewport: vp.name,
            errors: consoleErrors
          });
        }
      } catch (err) {
        issues.push({
          type: 'LOAD_ERROR',
          url: urlPath,
          viewport: vp.name,
          error: err.message
        });
      } finally {
        page.off('console', onConsole);
      }
    }
  }

  console.log(`\n================ AUDIT RESULTS: ${issues.length} ISSUES FOUND ================`);
  issues.forEach((iss, i) => {
    console.log(`\n[${i+1}] ${iss.type} on ${iss.url} (${iss.viewport})`);
    if (iss.diff) console.log(`    Overflow: +${iss.diff}px`);
    if (iss.culprits) console.log('    Culprits:', JSON.stringify(iss.culprits));
    if (iss.brokenImgs) console.log('    Broken images:', JSON.stringify(iss.brokenImgs));
    if (iss.errors) console.log('    Console errors:', JSON.stringify(iss.errors));
    if (iss.error) console.log('    Error:', iss.error);
  });

  await browser.close();
})();
