const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 390, height: 844 } }); // Mobile
  
  await page.goto('http://localhost:8089/courses/sql-course/', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(500);

  // Take screenshot of mobile bottom bar / header
  const stickyOrFixed = await page.evaluate(() => {
    const els = Array.from(document.querySelectorAll('*'));
    return els.filter(el => {
      const style = window.getComputedStyle(el);
      return style.position === 'fixed' || style.position === 'sticky';
    }).map(el => ({
      tag: el.tagName,
      className: el.className,
      id: el.id,
      text: el.innerText.slice(0, 50),
      zIndex: window.getComputedStyle(el).zIndex,
      bottom: window.getComputedStyle(el).bottom
    }));
  });

  console.log("Fixed/Sticky elements on Mobile:");
  console.log(JSON.stringify(stickyOrFixed, null, 2));

  // Try to click WhatsApp button in header or mobile actions
  const waBtn = await page.$('.nav-actions a[href*="wa.me"], .site-nav-actions a[href*="wa.me"], a.site-btn-outline[href*="wa.me"], .mobile-actions a[href*="wa.me"]');
  console.log("waBtn found:", !!waBtn);
  if (waBtn) {
    const isVisible = await waBtn.isVisible();
    const box = await waBtn.boundingBox();
    console.log("waBtn visible:", isVisible, "box:", box);
  }

  await browser.close();
})();

