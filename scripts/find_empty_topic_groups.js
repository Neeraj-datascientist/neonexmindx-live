const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
  
  await page.goto('http://localhost:8089/syllabus/catalogues/data-science-and-ai-syllabus.html', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(500);

  const emptyDivs = await page.evaluate(() => {
    const divs = Array.from(document.querySelectorAll('.topic-group'));
    return divs.filter(d => d.innerText.trim() === '').map(d => ({
      className: d.className,
      innerHTML: d.innerHTML,
      outerHTML: d.outerHTML
    }));
  });

  console.log(`Found ${emptyDivs.length} empty .topic-group elements!`);
  if (emptyDivs.length > 0) {
    console.log("Sample empty element:");
    console.log(emptyDivs[0].outerHTML);
  }

  await browser.close();
})();

