const fs = require('fs');
const html = fs.readFileSync('deployment_NeoNex/blogs/index.html', 'utf8');
const s = html.indexOf('h3 class="card-');
console.log(html.substring(s, s + 1000));

