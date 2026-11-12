const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page = await context.newPage();

  console.log('Testing SQL Short Course WhatsApp & Buttons on Desktop & Mobile...');

  // Test SQL course page
  for (const viewport of [
    { name: 'Desktop', width: 1280, height: 800 },
    { name: 'Mobile', width: 375, height: 667 }
  ]) {
    await page.setViewportSize({ width: viewport.width, height: viewport.height });
    await page.goto('http://localhost:8089/courses/sql-course/', { waitUntil: 'domcontentloaded' });

    // Check WhatsApp floating button
    const waFloating = page.locator('#whatsapp-direct-bubble, .whatsapp-floating-bubble, a[href*="wa.me"]');
    const waCount = await waFloating.count();
    console.log(`[${viewport.name}] SQL Course WhatsApp links found: ${waCount}`);

    for (let i = 0; i < waCount; i++) {
      const el = waFloating.nth(i);
      const isVisible = await el.isVisible();
      const href = await el.getAttribute('href');
      console.log(`  WA link [${i}]: visible=${isVisible}, href=${href}`);
    }

    // Check syllabus download link
    const syllabusLinks = page.locator('a[href*="syllabus"]');
    const sylCount = await syllabusLinks.count();
    console.log(`[${viewport.name}] SQL Course Syllabus links found: ${sylCount}`);
    for (let i = 0; i < sylCount; i++) {
      const el = syllabusLinks.nth(i);
      const isVisible = await el.isVisible();
      const href = await el.getAttribute('href');
      const text = (await el.textContent() || '').trim();
      console.log(`  Syllabus link [${i}]: text="${text}", visible=${isVisible}, href=${href}`);
    }
  }

  await browser.close();
})();
