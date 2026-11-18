const fs = require('fs');
let text = fs.readFileSync('deployment_NeoNex/cms/index.html', 'utf8');

// Replace href="../home" with href="/"
text = text.replace('href="../home"', 'href="/"');

fs.writeFileSync('deployment_NeoNex/cms/index.html', text, 'utf8');
console.log('Fixed brand-link in cms/index.html to href="/"');
