const fs = require('fs');
const text = fs.readFileSync('deployment_NeoNex/cms/index.html', 'utf8');
const pos1 = text.indexOf('../home');
if (pos1 !== -1) console.log('pos1:', text.substring(pos1 - 80, pos1 + 80));
const pos2 = text.indexOf('"$2"');
if (pos2 !== -1) console.log('pos2:', text.substring(pos2 - 80, pos2 + 80));
