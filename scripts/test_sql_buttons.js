const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
  
  await page.goto('http://localhost:8089/courses/sql-course/', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(500);
  
  // Find all buttons or links with 'whatsapp' in text or href
  const waElements = await page.evaluate(() => {
    const els = Array.from(document.querySelectorAll('a, button'));
    return els.filter(el => {
      const txt = el.innerText.toLowerCase();
      const href = el.getAttribute('href') || '';
      return txt.includes('whatsapp') || href.includes('wa.me');
    }).map(el => ({
      tag: el.tagName,
      text: el.innerText.trim(),
      href: el.getAttribute('href'),
      onclick: el.getAttribute('onclick'),
      visible: el.offsetParent !== null,
      box: el.getBoundingClientRect()
    }));
  });
  
  console.log("WhatsApp elements on SQL course page:");
  console.log(JSON.stringify(waElements, null, 2));

  // Also check hero action buttons
  const heroButtons = await page.evaluate(() => {
    const hero = document.querySelector('.hero, header, .hero-actions');
    if (!hero) return [];
    return Array.from(document.querySelectorAll('.hero a, .hero button, .hero-actions a, .hero-actions button')).map(el => ({
      tag: el.tagName,
      text: el.innerText.trim(),
      href: el.getAttribute('href'),
      onclick: el.getAttribute('onclick'),
      box: el.getBoundingClientRect()
    }));
  });

  console.log("\nHero buttons on SQL course page:");
  console.log(JSON.stringify(heroButtons, null, 2));
  
  await browser.close();
})();

