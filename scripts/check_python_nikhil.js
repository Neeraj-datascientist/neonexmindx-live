const fs = require('fs');

function checkCardInCourse(f) {
  const c = fs.readFileSync(f, 'utf8');
  const pos = c.indexOf('trainer-nikhil');
  if (pos !== -1) {
    console.log(`\n=== File: ${f} ===`);
    console.log(c.substring(pos - 100, pos + 500));
  }
}

checkCourse = 'deployment_NeoNex/courses/python-programming-course/index.html';
checkCardInCourse(checkCourse);

