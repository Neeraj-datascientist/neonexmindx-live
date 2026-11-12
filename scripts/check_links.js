const fs = require('fs');

function checkFile(p) {
    const html = fs.readFileSync(p, 'utf8');
    const matches = html.match(/href=["'][^"']*linkedin[^"']*["']/g);
    console.log(p, matches);
}

checkFile('deployment_NeoNex/trainers/index.html');
checkFile('deployment_NeoNex/trainers-and-mentors/index.html');
checkFile('deployment_NeoNex/courses/sql-course/index.html');
