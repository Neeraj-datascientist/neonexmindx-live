const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
  
  await page.goto('http://localhost:8089/courses/sql-course/', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(500);

  // 1. Test Floating WhatsApp
  const floatWa = await page.$('.site-floating-whatsapp');
  console.log("Floating WhatsApp exists:", !!floatWa);
  if (floatWa) {
    const isVisible = await floatWa.isVisible();
    const box = await floatWa.boundingBox();
    const href = await floatWa.getAttribute('href');
    console.log("Floating WA visible:", isVisible, "box:", box, "href:", href);
  }

  // 2. Test Syllabus link
  const sylLink = await page.$('a[href*="sql-syllabus.html"]');
  console.log("SQL syllabus download link exists:", !!sylLink);
  if (sylLink) {
    const isVisible = await sylLink.isVisible();
    const href = await sylLink.getAttribute('href');
    console.log("Syllabus link visible:", isVisible, "href:", href);
  }

  // 3. Test opening sql-syllabus.html
  const pageSyllabus = await browser.newPage();
  const resp = await pageSyllabus.goto('http://localhost:8089/syllabus/catalogues/sql-syllabus.html', { waitUntil: 'domcontentloaded' });
  console.log("SQL syllabus catalogue HTTP status:", resp.status());
  const h1 = await pageSyllabus.$eval('h1', el => el.innerText);
  console.log("SQL syllabus H1:", h1);
  const modulesCount = await pageSyllabus.$$eval('.module-card', els => els.length);
  console.log("SQL syllabus modules count rendered:", modulesCount);

  await browser.close();
})();
