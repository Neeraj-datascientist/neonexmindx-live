const { chromium } = require('playwright');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  
  await page.goto('http://localhost:8089/blogs/', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(600);

  // Get all blog cards and articles
  const blogCards = await page.evaluate(() => {
    const cards = Array.from(document.querySelectorAll('.blog-card, article, .post-card'));
    return cards.map(c => {
      const title = c.querySelector('h2, h3, .blog-title');
      const author = c.querySelector('.blog-author, .author, .card-author');
      const links = Array.from(c.querySelectorAll('a')).map(a => ({
        text: a.innerText.trim(),
        href: a.getAttribute('href')
      }));
      const img = c.querySelector('img');
      return {
        title: title ? title.innerText.trim() : '',
        author: author ? author.innerText.trim() : '',
        img: img ? img.getAttribute('src') : '',
        links
      };
    });
  });

  console.log(`Found ${blogCards.length} cards in /blogs/:`);
  console.log(JSON.stringify(blogCards, null, 2));

  await browser.close();
})();

