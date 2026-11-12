const fs = require('fs');

function analyzeFile(filePath) {
  const c = fs.readFileSync(filePath, 'utf8');
  console.log(`\n=================== FILE: ${filePath} ===================`);
  
  // Look for any <a> tag that links to linkedin
  const regex = /<a[^>]+href=["'](https:\/\/[^"']*linkedin[^"']*)["'][^>]*>([\s\S]*?)<\/a>/gi;
  let match;
  let count = 0;
  while ((match = regex.exec(c)) !== null) {
    count++;
    const href = match[1];
    const text = match[2].replace(/<[^>]+>/g, '').trim();
    // find surrounding 300 characters
    const start = Math.max(0, match.index - 200);
    const end = Math.min(c.length, match.index + 200);
    const surrounding = c.substring(start, end).replace(/\s+/g, ' ');
    
    // check if surrounding text has a trainer name
    let mentorMentioned = 'None';
    for (const name of ['Nikhil', 'Sanjana', 'Lakshmi', 'Neeraj', 'Yashas', 'Raveendran', 'Venkat', 'Megha']) {
      if (surrounding.includes(name)) {
        mentorMentioned = name;
        break;
      }
    }
    
    console.log(`Link #${count}: Mentor context = [${mentorMentioned}]`);
    console.log(`   HREF: ${href}`);
    console.log(`   TEXT: "${text}"`);
    if (mentorMentioned === 'Nikhil' && href.includes('neeraj')) {
      console.log(`   🚨🚨🚨 MISMATCH FOUND: Nikhil card links to Neeraj!`);
    } else if (mentorMentioned !== 'None' && !href.includes(mentorMentioned.toLowerCase()) && !href.includes('company/neonex-mindx')) {
      if (mentorMentioned === 'Neeraj' && !href.includes('neeraj')) {
        console.log(`   ⚠️ Potential mismatch: Neeraj context links to ${href}`);
      } else if (mentorMentioned === 'Lakshmi' && !href.includes('lakshmi')) {
        console.log(`   ⚠️ Potential mismatch: Lakshmi context links to ${href}`);
      } else if (mentorMentioned === 'Yashas' && !href.includes('yashas')) {
        console.log(`   ⚠️ Potential mismatch: Yashas context links to ${href}`);
      } else if (mentorMentioned === 'Raveendran' && !href.includes('raveendran')) {
        console.log(`   ⚠️ Potential mismatch: Raveendran context links to ${href}`);
      }
    }
  }
}

const glob = require('path');
const targetFiles = [
  'deployment_NeoNex/courses/python-programming-course/index.html',
  'deployment_NeoNex/courses/sql-course/index.html',
  'deployment_NeoNex/courses/machine-learning-course/index.html',
  'deployment_NeoNex/courses/excel-power-bi-tableau-course/index.html',
  'deployment_NeoNex/courses/data-science-course/index.html',
  'deployment_NeoNex/courses/data-science-and-ai-course/index.html',
  'deployment_NeoNex/courses/data-analytics-course/index.html',
  'deployment_NeoNex/courses/ai-ml-course/index.html',
  'deployment_NeoNex/courses/business-analytics-course/index.html',
  'deployment_NeoNex/courses/data-engineering-course/index.html',
  'deployment_NeoNex/courses/generative-ai-engineering-course/index.html',
  'deployment_NeoNex/index.html',
  'deployment_NeoNex/about-us/index.html',
  'deployment_NeoNex/trainers/index.html',
  'deployment_NeoNex/trainers-and-mentors/index.html',
  'deployment_NeoNex/blog-post.html',
  'deployment_NeoNex/blogs/index.html'
];

targetFiles.forEach(analyzeFile);

