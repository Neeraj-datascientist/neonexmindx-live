const fs = require('fs');

const p = 'deployment_NeoNex/trainers/index.html';
const html = fs.readFileSync(p, 'utf8');
const cards = html.split('<article class="trainer-card">');
console.log('Total trainer cards:', cards.length - 1);

cards.slice(1).forEach((card, idx) => {
    const nameMatch = card.match(/<h3>(.*?)<\/h3>/);
    const name = nameMatch ? nameMatch[1] : 'Unknown';
    const linkMatch = card.match(/href=["'](.*?)["']/);
    console.log(`Card ${idx+1}: ${name} -> Link: ${linkMatch ? linkMatch[1] : 'NO LINK'}`);
});

