const { chromium } = require('playwright');

const urlsToTest = [
  '/',
  '/about-us/',
  '/trainers-and-mentors/',
  '/blogs/',
  '/blog/machine-learning-vs-deep-learning-differences-guide/',
  '/blog/complete-roadmap-to-become-data-scientist-2026/',
  '/blog/top-high-paying-data-analytics-tools-2026/',
  '/courses/data-science-course/',
  '/courses/data-science-and-ai-course/',
  '/courses/data-analytics-course/',
  '/courses/data-engineering-course/',
  '/courses/ai-ml-engineering-course/',
  '/courses/business-analytics-course/',
  '/courses/generative-ai-engineering-course/',
  '/courses/sql-course/',
  '/courses/python-programming-course/',
  '/courses/excel-power-bi-tableau-course/',
  '/courses/machine-learning-course/',
  '/syllabus/catalogues/sql-syllabus.html',
  '/syllabus/catalogues/python-programming-syllabus.html',
  '/syllabus/catalogues/excel-power-bi-tableau-syllabus.html',
  '/syllabus/catalogues/machine-learning-syllabus.html',
  '/syllabus/catalogues/data-science-syllabus.html',
  '/syllabus/catalogues/data-science-and-ai-syllabus.html',
  '/cms/'
];

const viewports = [
  { name: 'Desktop (1440x900)', width: 1440, height: 900 },
  { name: 'Tablet (768x1024)', width: 768, height: 1024 },
  { name: 'Mobile (375x667)', width: 375, height: 667 },
  { name: 'Small Mobile (320x568)', width: 320, height: 568 }
];

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page = await context.newPage();

  const issues = [];

  for (const urlPath of urlsToTest) {
    const fullUrl = `http://localhost:8089${urlPath}`;
    for (const vp of viewports) {
      await page.setViewportSize({ width: vp.width, height: vp.height });
      const consoleErrors = [];
      const failedRequests = [];

      const onConsole = msg => {
        if (msg.type() === 'error') consoleErrors.push(msg.text());
      };
      const onRequestFailed = req => {
        failedRequests.push(`${req.method()} ${req.url()}: ${req.failure()?.errorText}`);
      };

      page.on('console', onConsole);
      page.on('requestfailed', onRequestFailed);

      try {
        await page.goto(fullUrl, { waitUntil: 'domcontentloaded', timeout: 10000 });
        await page.waitForTimeout(500);

        // 1. Check Horizontal Overflow (Wobble)
        const overflow = await page.evaluate(() => {
          const docWidth = document.documentElement.offsetWidth;
          const scrollWidth = document.documentElement.scrollWidth;
          const bodyScrollWidth = document.body ? document.body.scrollWidth : 0;
          const maxW = Math.max(scrollWidth, bodyScrollWidth);
          return {
            hasOverflow: maxW > docWidth + 2,
            diff: maxW - docWidth,
            docWidth,
            maxW
          };
        });

        if (overflow.hasOverflow) {
          // Identify overflowing elements
          const culprits = await page.evaluate(() => {
            const docW = document.documentElement.offsetWidth;
            const bad = [];
            document.querySelectorAll('*').forEach(el => {
              const rect = el.getBoundingClientRect();
              if (rect.right > docW + 2) {
                bad.push({
                  tag: el.tagName,
                  class: el.className,
                  id: el.id,
                  right: rect.right,
                  text: (el.textContent || '').trim().substring(0, 40)
                });
              }
            });
            return bad.slice(0, 5);
          });
          issues.push({
            type: 'HORIZONTAL_OVERFLOW',
            url: urlPath,
            viewport: vp.name,
            diff: overflow.diff,
            culprits
          });
        }

        // 2. Check Broken Images
        const brokenImgs = await page.evaluate(() => {
          const imgs = Array.from(document.querySelectorAll('img'));
          return imgs.filter(img => {
            if (!img.src || img.src.startsWith('data:image/gif')) return false;
            return !img.complete || img.naturalWidth === 0;
          }).map(img => ({
            src: img.src,
            alt: img.alt,
            parent: img.parentElement ? img.parentElement.className : ''
          }));
        });

        if (brokenImgs.length > 0) {
          issues.push({
            type: 'BROKEN_IMAGES',
            url: urlPath,
            viewport: vp.name,
            brokenImgs
          });
        }

        // 3. Console errors
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
          type: 'PAGE_LOAD_ERROR',
          url: urlPath,
          viewport: vp.name,
          error: err.message
        });
      } finally {
        page.off('console', onConsole);
        page.off('requestfailed', onRequestFailed);
      }
    }
  }

  console.log(`\n================ AUDIT SUMMARY (${issues.length} ISSUES) ================`);
  issues.forEach((iss, i) => {
    console.log(`\n[${i+1}] ${iss.type} on ${iss.url} (${iss.viewport})`);
    if (iss.diff) console.log(`    Overflow by: ${iss.diff}px (docW vs maxW)`);
    if (iss.culprits) console.log('    Culprits:', JSON.stringify(iss.culprits));
    if (iss.brokenImgs) console.log('    Broken images:', JSON.stringify(iss.brokenImgs));
    if (iss.errors) console.log('    Console errors:', JSON.stringify(iss.errors));
    if (iss.error) console.log('    Error:', iss.error);
  });

  await browser.close();
})();
