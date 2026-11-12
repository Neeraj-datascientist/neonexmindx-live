const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
  
  await page.goto('http://localhost:8089/syllabus/catalogues/data-science-and-ai-syllabus.html', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(500);

  // Inspect Module 01 in detail: all child elements and their borders/backgrounds
  const details = await page.evaluate(() => {
    const card = document.querySelector('.module-card');
    if (!card) return null;
    const body = card.querySelector('.module-body');
    const children = Array.from(body.children);
    return children.map((c, i) => {
      const style = window.getComputedStyle(c);
      return {
        index: i,
        tag: c.tagName,
        className: c.className,
        text: c.innerText.slice(0, 40),
        height: style.height,
        marginTop: style.marginTop,
        marginBottom: style.marginBottom,
        border: style.border,
        background: style.backgroundColor
      };
    });
  });

  console.log("Module 01 children in live render:");
  console.log(JSON.stringify(details, null, 2));

  await browser.close();
})();
