const fs = require('fs');

function inspectSetOperators(f) {
  const c = fs.readFileSync(f, 'utf8');
  const pos = c.indexOf('Set Operators');
  if (pos !== -1) {
    console.log(c.substring(pos - 100, pos + 700));
  }
}

inspectSetOperators('deployment_NeoNex/syllabus/catalogues/sql-syllabus.html');
