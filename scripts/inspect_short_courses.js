const fs = require('fs');

function inspectFile(f) {
  const c = fs.readFileSync(f, 'utf8');
  let idx = 0;
  while ((idx = c.indexOf('neeraj-neonexmindx', idx)) !== -1) {
    console.log(`\n--- Occurrence in ${f} at ${idx} ---`);
    console.log(c.substring(Math.max(0, idx - 400), Math.min(c.length, idx + 400)));
    idx += 'neeraj-neonexmindx'.length;
  }
}

inspectFile('deployment_NeoNex/courses/python-programming-course/index.html');
inspectFile('deployment_NeoNex/courses/sql-course/index.html');
inspectFile('deployment_NeoNex/courses/machine-learning-course/index.html');
inspectFile('deployment_NeoNex/courses/excel-power-bi-tableau-course/index.html');
