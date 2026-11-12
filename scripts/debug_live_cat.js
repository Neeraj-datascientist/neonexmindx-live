const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
  
  await page.goto('http://localhost:8089/syllabus/catalogues/data-science-and-ai-syllabus.html', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(500);

  // Inspect Module 01 and Module 02
  const modData = await page.evaluate(() => {
    const cards = Array.from(document.querySelectorAll('.module-card'));
    return cards.slice(0, 3).map(c => {
      const h2 = c.querySelector('h2');
      const body = c.querySelector('.module-body');
      const topics = Array.from(c.querySelectorAll('.topic-group, .topic-title, .bullet-list li')).map(t => ({
        tag: t.tagName,
        className: t.className,
        text: t.innerText.slice(0, 50),
        computed: {
          display: window.getComputedStyle(t).display,
          color: window.getComputedStyle(t).color,
          fontSize: window.getComputedStyle(t).fontSize,
          height: window.getComputedStyle(t).height,
          border: window.getComputedStyle(t).border
        }
      }));
      return {
        title: h2 ? h2.innerText : '',
        bodyDisplay: body ? window.getComputedStyle(body).display : '',
        topicsCount: topics.length,
        topics: topics.slice(0, 8)
      };
    });
  });

  console.log("Module Data in live render:");
  console.log(JSON.stringify(modData, null, 2));

  await page.screenshot({ path: 'deployment_NeoNex/scripts/cat_debug.png', fullPage: false });
  console.log("Screenshot saved to deployment_NeoNex/scripts/cat_debug.png");

  await browser.close();
})();

