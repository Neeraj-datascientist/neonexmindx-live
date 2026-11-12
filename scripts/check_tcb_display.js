const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
  
  await page.goto('http://localhost:8089/syllabus/catalogues/data-science-and-ai-syllabus.html', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(500);

  const hiddenContent = await page.evaluate(() => {
    const bodies = Array.from(document.querySelectorAll('.topic-content-body'));
    return bodies.map(b => ({
      text: b.innerText.slice(0, 50),
      display: window.getComputedStyle(b).display
    }));
  });

  console.log("Total .topic-content-body elements:", hiddenContent.length);
  const noneCount = hiddenContent.filter(h => h.display === 'none').length;
  console.log("Elements with display: none:", noneCount);
  console.log("Sample elements with display: none:", hiddenContent.filter(h => h.display === 'none').slice(0, 5));

  await browser.close();
})();

