const fs = require('fs');
let html = fs.readFileSync('deployment_NeoNex/digital-marketing/index.html', 'utf8');

const metaInjection = '  <meta name="description" content="NeoNeX MindX Digital Marketing &amp; Competitor Intelligence Hub. Real-time organic search audit, conversion rate optimization, keyword gap analysis, and multi-channel attribution.">\n  <link rel="canonical" href="https://neonexmindx.com/digital-marketing/">\n';

if (!html.includes('canonical')) {
  html = html.replace('<title>', metaInjection + '  <title>');
  fs.writeFileSync('deployment_NeoNex/digital-marketing/index.html', html, 'utf8');
  console.log('Added meta description and canonical to digital-marketing/index.html');
}
