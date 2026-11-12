const fs = require('fs');

function checkTeamGrid(f) {
  const c = fs.readFileSync(f, 'utf8');
  const start = c.indexOf('class="team-grid"');
  if (start !== -1) {
    console.log(`=== ${f} team-grid ===`);
    console.log(c.substring(start, start + 3000));
  }
}

checkTeamGrid('deployment_NeoNex/trainers/index.html');
