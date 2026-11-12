const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 390, height: 844 } });
  
  await page.goto('http://localhost:8089/courses/sql-course/', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(500);

  const mobActions = await page.evaluate(() => {
    const el = document.querySelector('.mobile-actions');
    if (!el) return null;
    const computed = window.getComputedStyle(el);
    const links = Array.from(el.querySelectorAll('a, button')).map(a => ({
      tag: a.tagName,
      text: a.innerText,
      href: a.getAttribute('href'),
      visible: a.offsetParent !== null,
      box: a.getBoundingClientRect(),
      style: {
        display: window.getComputedStyle(a).display,
        visibility: window.getComputedStyle(a).visibility,
        opacity: window.getComputedStyle(a).opacity,
        pointerEvents: window.getComputedStyle(a).pointerEvents
      }
    }));
    return {
      className: el.className,
      display: computed.display,
      visibility: computed.visibility,
      zIndex: computed.zIndex,
      box: el.getBoundingClientRect(),
      links
    };
  });

  console.log("mobile-actions on Mobile:");
  console.log(JSON.stringify(mobActions, null, 2));

  // Let's also check what element is at the point of the WhatsApp button
  if (mobActions && mobActions.links && mobActions.links[1]) {
    const b = mobActions.links[1].box;
    const pointEl = await page.evaluate(({x, y}) => {
      const el = document.elementFromPoint(x, y);
      return el ? { tag: el.tagName, className: el.className, id: el.id, text: el.innerText } : null;
    }, { x: b.x + b.width / 2, y: b.y + b.height / 2 });
    console.log("Element directly on top of WhatsApp button:", pointEl);
  }

  await browser.close();
})();

