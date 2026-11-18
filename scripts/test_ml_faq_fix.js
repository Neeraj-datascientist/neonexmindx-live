const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.setViewportSize({ width: 320, height: 568 });
  await page.goto('http://localhost:8089/courses/machine-learning-course/');
  
  const testFix = await page.evaluate(() => {
    const s = document.querySelector('.faq[open] summary');
    const span = s.querySelector('span');
    span.style.flexShrink = '0';
    span.style.marginLeft = '12px';
    s.style.gap = '10px';
    s.style.padding = '18px 4px';
    
    const docW = document.documentElement.offsetWidth;
    const scrollW = document.documentElement.scrollWidth;
    const bodyScrollW = document.body ? document.body.scrollWidth : 0;
    const maxW = Math.max(scrollW, bodyScrollW);
    return { docW, maxW, overflow: maxW > docW };
  });
  console.log('Test fix result in ML course:', testFix);
  await browser.close();
})();
