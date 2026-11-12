const fs = require('fs');
const html = fs.readFileSync('deployment_NeoNex/blog-post.html', 'utf8');
const s = html.indexOf('share-tray');
const s2 = html.indexOf('share-tray', s + 20);
console.log('Template with share-tray:');
console.log(html.substring(Math.max(0, s2 - 800), s2 + 1200));
