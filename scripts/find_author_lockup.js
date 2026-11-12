const fs = require('fs');
const html = fs.readFileSync('deployment_NeoNex/blogs/index.html', 'utf8');
const s = html.indexOf('author-lockup');
const s2 = html.indexOf('author-lockup', s + 20);
console.log('Second author lockup:');
console.log(html.substring(s2, s2 + 600));
const s3 = html.indexOf('author-lockup', s2 + 20);
console.log('Third author lockup:');
console.log(html.substring(s3, s3 + 600));
