const fs = require('fs');

function checkPage(file) {
    if (!fs.existsSync(file)) return;
    const html = fs.readFileSync(file, 'utf8');
    const cards = html.split(/class=["'](?:mentor-card|trainer-card)["']/);
    console.log(`\n=== File: ${file} (Cards: ${cards.length - 1}) ===`);
    cards.slice(1).forEach((card, idx) => {
        const nameMatch = card.match(/<h[34][^>]*>(.*?)<\/h[34]>/);
        const name = nameMatch ? nameMatch[1].replace(/<[^>]+>/g, '').trim() : 'Unknown';
        const links = card.match(/href=["'](https:\/\/[^"']*linkedin[^"']*)["']/g) || [];
        console.log(`  Card ${idx+1}: ${name} -> ${links.join(', ') || 'NO LINK'}`);
    });
}

const pages = [
    'deployment_NeoNex/index.html',
    'deployment_NeoNex/Neonex Mindx Home Page.html',
    'deployment_NeoNex/about-us/index.html',
    'deployment_NeoNex/trainers/index.html',
    'deployment_NeoNex/trainers-and-mentors/index.html',
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
    'deployment_NeoNex/courses/generative-ai-engineering-course/index.html'
];

pages.forEach(checkPage);

