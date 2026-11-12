const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1280, height: 900 });

  await page.goto('http://localhost:8089/syllabus/catalogues/sql-syllabus.html', { waitUntil: 'networkidle' });

  // Scroll to Module 13 Set Operators
  const mod13 = page.locator('.module-card:has-text("Set Operators")');
  await mod13.scrollIntoViewIfNeeded();

  await page.screenshot({ path: 'deployment_NeoNex/scripts/sql_module_13_clean.png', fullPage: false });
  console.log('Saved screenshot of fixed Module 13!');

  await browser.close();
})();
