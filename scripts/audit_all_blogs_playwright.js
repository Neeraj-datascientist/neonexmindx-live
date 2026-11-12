const { chromium } = require('playwright');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  
  const blogsData = JSON.parse(fs.readFileSync('deployment_NeoNex/data/blogs.json', 'utf8'));
  const posts = blogsData.posts;
  const authors = blogsData.authors;

  console.log(`Auditing ${posts.length} blog posts in depth...`);

  for (const post of posts) {
    const url = `http://localhost:8089/blog/${post.slug}/`;
    await page.goto(url, { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(400);

    const audit = await page.evaluate((expectedAuthorName) => {
      // Find all linkedin links on page
      const liLinks = Array.from(document.querySelectorAll('a[href*="linkedin.com"]')).map(a => ({
        href: a.getAttribute('href'),
        text: a.innerText.trim(),
        parentTag: a.parentElement ? a.parentElement.tagName : '',
        parentClass: a.parentElement ? a.parentElement.className : '',
        grandParentClass: a.parentElement && a.parentElement.parentElement ? a.parentElement.parentElement.className : ''
      }));

      // Find author card avatar image
      const avatarImg = document.querySelector('.article-author-card img, .author-card-avatar');
      const authorHeading = document.querySelector('.article-author-card h4, .author-name');

      return {
        expectedAuthor: expectedAuthorName,
        renderedAuthorHeading: authorHeading ? authorHeading.innerText.trim() : null,
        renderedAvatarSrc: avatarImg ? avatarImg.getAttribute('src') : null,
        linkedinLinks: liLinks
      };
    }, post.author);

    console.log(`\n========================================`);
    console.log(`SLUG: ${post.slug}`);
    console.log(`Expected Author: ${audit.expectedAuthor}`);
    console.log(`Rendered Heading: ${audit.renderedAuthorHeading}`);
    console.log(`Rendered Avatar: ${audit.renderedAvatarSrc}`);
    console.log(`LinkedIn Links found: ${audit.linkedinLinks.length}`);
    audit.linkedinLinks.forEach((l, i) => {
      console.log(`  [${i+1}] ${l.href} (Text: "${l.text}", Class: "${l.parentClass}")`);
    });
  }

  await browser.close();
})();
