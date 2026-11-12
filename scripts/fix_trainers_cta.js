const fs = require('fs');
let c = fs.readFileSync('deployment_NeoNex/trainers/index.html', 'utf8');
c = c.replace('href="https://www.linkedin.com/in/megha-paul02/"', 'href="#enquire"');
fs.writeFileSync('deployment_NeoNex/trainers/index.html', c, 'utf8');
console.log('Successfully updated trainers/index.html');
