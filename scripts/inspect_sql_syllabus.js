const fs = require('fs');

function inspectSyllabus(file) {
  console.log(`\n================= ${file} =================`);
  const html = fs.readFileSync(file, 'utf8');
  const cards = html.split('<div class="module-card">');
  cards.slice(1).forEach((card, idx) => {
    const headerMatch = card.match(/<div class="module-header">([\s\S]*?)<\/div>/);
    const header = headerMatch ? headerMatch[1].replace(/<[^>]+>/g, '').replace(/\s+/g, ' ').trim() : 'No header';
    const topicsMatch = card.match(/<ul class="topic-list">([\s\S]*?)<\/ul>/);
    const topicCount = topicsMatch ? (topicsMatch[1].match(/<li/g) || []).length : 0;
    const topicText = topicsMatch ? topicsMatch[1].replace(/<[^>]+>/g, '').replace(/\s+/g, ' ').trim() : '';
    console.log(`[#${idx + 1}] Header: "${header}" | Topics count: ${topicCount}`);
    if (topicCount === 0) {
      console.log(`     ⚠️ EMPTY TOPIC LIST!`);
    } else {
      console.log(`     Content preview: ${topicText.substring(0, 100)}...`);
    }
  });
}

inspectSyllabus('deployment_NeoNex/syllabus/catalogues/sql-syllabus.html');
