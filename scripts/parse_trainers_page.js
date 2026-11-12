const fs = require('fs');

function checkCardInTrainers(f) {
  const c = fs.readFileSync(f, 'utf8');
  const start = c.indexOf('class="team-grid"');
  if (start === -1) return;
  const chunk = c.substring(start, start + 3500);
  const cards = chunk.split('<article class="trainer-card">');
  cards.slice(1).forEach((card, i) => {
    const nameMatch = card.match(/<h3>(.*?)<\/h3>/);
    const name = nameMatch ? nameMatch[1] : 'Unknown';
    const linkMatch = card.match(/href="([^"]+)"/);
    console.log(`Trainer ${i+1}: ${name} -> Link: ${linkMatch ? linkMatch[1] : 'NONE'}`);
  });
}

checkCardInTrainers('deployment_NeoNex/trainers/index.html');
checkCardInTrainers('deployment_NeoNex/trainers-and-mentors/index.html');

