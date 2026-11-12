const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page = await context.newPage();

  console.log('Testing click action on SQL WhatsApp CTA buttons...');
  await page.goto('http://localhost:8089/courses/sql-course/', { waitUntil: 'domcontentloaded' });

  // Listen for popup or navigation
  const floatingWa = page.locator('#whatsapp-direct-bubble');
  const count = await floatingWa.count();
  console.log('Floating WA count:', count);
  if (count > 0) {
    const isVis = await floatingWa.isVisible();
    const href = await floatingWa.getAttribute('href');
    console.log('Floating WA isVisible:', isVis, 'href:', href);
  }

  // Also check inline buttons
  const inlineButtons = page.locator('a.btn-whatsapp, a[data-action="whatsapp"], .course-hero a[href*="wa.me"]');
  const inlineCount = await inlineButtons.count();
  console.log('Inline WhatsApp buttons count:', inlineCount);
  for (let i = 0; i < inlineCount; i++) {
    const btn = inlineButtons.nth(i);
    const vis = await btn.isVisible();
    const href = await btn.getAttribute('href');
    const text = (await btn.textContent() || '').trim();
    console.log(`Inline WA button [${i}]: text="${text}", vis=${vis}, href=${href}`);
  }

  await browser.close();
})();

