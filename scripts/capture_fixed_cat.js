const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
  
  await page.goto('http://localhost:8089/syllabus/catalogues/data-science-and-ai-syllabus.html', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(500);

  await page.screenshot({ path: 'deployment_NeoNex/scripts/cat_fixed.png', fullPage: false });
  console.log("Screenshot saved to deployment_NeoNex/scripts/cat_fixed.png");

  await browser.close();
})();
