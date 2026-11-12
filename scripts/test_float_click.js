const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page = await context.newPage();

  await page.goto('http://localhost:8089/courses/sql-course/', { waitUntil: 'networkidle' });

  // Check if any click handler or preventDefault is attached
  const listeners = await page.evaluate(() => {
    const el = document.querySelector('.site-floating-whatsapp');
    return {
      href: el ? el.href : null,
      target: el ? el.target : null,
      hasPointerEvents: window.getComputedStyle(el).pointerEvents,
      zIndex: window.getComputedStyle(el).zIndex,
      display: window.getComputedStyle(el).display,
      visibility: window.getComputedStyle(el).visibility
    };
  });
  console.log('Floating WhatsApp computed styles:', listeners);

  // Click using page.click
  const [popup] = await Promise.all([
    context.waitForEvent('page', { timeout: 5000 }),
    page.click('.site-floating-whatsapp')
  ]);
  console.log('Opened popup URL:', popup.url());

  await browser.close();
})();
