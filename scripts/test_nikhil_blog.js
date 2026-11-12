const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
  
  // Test both Nikhil posts:
  const slugs = [
    'machine-learning-vs-deep-learning-differences-guide',
    'distributed-data-pipelines-with-apache-spark-iceberg'
  ];

  for (const slug of slugs) {
    const url = `http://localhost:8089/blog/${slug}/`;
    await page.goto(url, { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(600);

    const authorData = await page.evaluate(() => {
      const topAuthorLink = document.querySelector('.article-author-name a, .article-meta-top a[href*="linkedin"]');
      const bottomAuthorLink = document.querySelector('.article-author-card a[href*="linkedin"]');
      const avatarImg = document.querySelector('.article-author-card .author-card-avatar, .article-meta-top img');
      const authorName = document.querySelector('.article-author-name, .article-author-card h4');
      
      return {
        authorName: authorName ? authorName.innerText.trim() : null,
        topHref: topAuthorLink ? topAuthorLink.getAttribute('href') : null,
        bottomHref: bottomAuthorLink ? bottomAuthorLink.getAttribute('href') : null,
        avatarSrc: avatarImg ? avatarImg.getAttribute('src') : null
      };
    });

    console.log(`\n=== Testing ${slug} ===`);
    console.log(JSON.stringify(authorData, null, 2));
  }

  await browser.close();
})();

