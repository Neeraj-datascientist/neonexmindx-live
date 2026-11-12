const fs = require('fs');
const html = fs.readFileSync('deployment_NeoNex/courses/sql-course/index.html', 'utf8');
const regex = /<a[^>]+href=["'][^"']*wa\.me[^"']*["'][^>]*>([\s\S]*?)<\/a>/gi;
let m;
while ((m = regex.exec(html)) !== null) {
  console.log('WA link tag:', m[0].substring(0, 150));
}
