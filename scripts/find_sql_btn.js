const fs = require('fs');
const html = fs.readFileSync('deployment_NeoNex/courses/sql-course/index.html', 'utf8');
const s = html.indexOf('class="btn btn-primary" href="https://wa.me/918431803839"');
console.log(html.substring(s - 150, s + 250));
