const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
  
  await page.goto('http://localhost:8089/courses/sql-course/', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(500);

  // Check clicking on header WhatsApp
  const headerWa = await page.$('.site-nav-actions a[href*="wa.me"]');
  console.log("Header WA exists:", !!headerWa);
  if (headerWa) {
    const href = await headerWa.getAttribute('href');
    const target = await headerWa.getAttribute('target');
    console.log("Header WA href:", href, "target:", target);
  }

  // Check clicking on hero-contact WhatsApp
  const heroWa = await page.$('.hero-contact a[href*="wa.me"]');
  console.log("Hero WA exists:", !!heroWa);
  if (heroWa) {
    const href = await heroWa.getAttribute('href');
    const target = await heroWa.getAttribute('target');
    console.log("Hero WA href:", href, "target:", target);
  }

  // Check clicking on mobile bottom bar WhatsApp
  const mobWa = await page.$('.mobile-actions a[href*="wa.me"]');
  console.log("Mobile bar WA exists:", !!mobWa);
  if (mobWa) {
    const href = await mobWa.getAttribute('href');
    const target = await mobWa.getAttribute('target');
    console.log("Mobile bar WA href:", href, "target:", target);
  }

  // Check form submit in SQL course
  const form = await page.$('#course-fit-form');
  console.log("Course fit form exists:", !!form);

  await browser.close();
})();

