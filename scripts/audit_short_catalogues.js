const fs = require('fs');

function checkShortCourses(files) {
  files.forEach(file => {
    console.log(`\n================= ${file} =================`);
    const html = fs.readFileSync(file, 'utf8');
    const cards = html.split('<div class="module-card">');
    console.log(`Total module cards: ${cards.length - 1}`);
    let emptyCount = 0;
    cards.slice(1).forEach((card, idx) => {
      const headerMatch = card.match(/<div class="module-header">([\s\S]*?)<\/div>/);
      const header = headerMatch ? headerMatch[1].replace(/<[^>]+>/g, '').replace(/\s+/g, ' ').trim() : 'No header';
      const topicsMatch = card.match(/<ul class="topic-list">([\s\S]*?)<\/ul>/);
      const topicCount = topicsMatch ? (topicsMatch[1].match(/<li/g) || []).length : 0;
      if (topicCount === 0) {
        emptyCount++;
        console.log(`  Empty card #${idx + 1}: "${header}"`);
      }
    });
    console.log(`Total empty cards in ${file}: ${emptyCount}`);
  });
}

checkShortCourses([
  'deployment_NeoNex/syllabus/catalogues/sql-syllabus.html',
  'deployment_NeoNex/syllabus/catalogues/python-programming-syllabus.html',
  'deployment_NeoNex/syllabus/catalogues/excel-power-bi-tableau-syllabus.html',
  'deployment_NeoNex/syllabus/catalogues/machine-learning-syllabus.html'
]);
