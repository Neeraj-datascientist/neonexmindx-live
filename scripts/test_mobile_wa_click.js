const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page = await context.newPage();

  // Test mobile viewport 375x667
  await page.setViewportSize({ width: 375, height: 667 });
  await page.goto('http://localhost:8089/courses/sql-course/', { waitUntil: 'domcontentloaded' });

  console.log('--- Testing Mobile Actions WhatsApp Button ---');
  const mobileWa = page.locator('.mobile-actions a.btn.btn-primary');
  const isVis = await mobileWa.isVisible();
  const box = await mobileWa.boundingBox();
  console.log('Mobile actions WA isVisible:', isVis, 'BoundingBox:', box);

  // Check what element is at the point (x, y) of the button
  if (box) {
    const elAtPoint = await page.evaluate(({x, y}) => {
      const el = document.elementFromPoint(x, y);
      return {
        tag: el ? el.tagName : null,
        class: el ? el.className : null,
        id: el ? el.id : null,
        text: el ? el.textContent.trim().substring(0, 30) : null
      };
    }, { x: box.x + box.width / 2, y: box.y + box.height / 2 });
    console.log('Element directly at center of Mobile WA button:', elAtPoint);
  }

  console.log('\n--- Testing Floating WhatsApp Bubble ---');
  const floatWa = page.locator('.site-floating-whatsapp');
  const floatVis = await floatWa.isVisible();
  const floatBox = await floatWa.boundingBox();
  console.log('Floating WA isVisible:', floatVis, 'BoundingBox:', floatBox);
  if (floatBox) {
    const elAtFloat = await page.evaluate(({x, y}) => {
      const el = document.elementFromPoint(x, y);
      return {
        tag: el ? el.tagName : null,
        class: el ? el.className : null,
        id: el ? el.id : null
      };
    }, { x: floatBox.x + floatBox.width / 2, y: floatBox.y + floatBox.height / 2 });
    console.log('Element at center of Floating WA:', elAtFloat);
  }

  await browser.close();
})();
