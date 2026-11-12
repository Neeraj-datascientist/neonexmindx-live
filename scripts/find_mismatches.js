const fs = require('fs');
const path = require('path');
const cheerio = require('cheerio');

function scanDir(dir) {
    const files = fs.readdirSync(dir);
    for (const f of files) {
        const full = path.join(dir, f);
        const stat = fs.statSync(full);
        if (stat.isDirectory()) {
            if (f !== 'node_modules' && f !== '.git') scanDir(full);
        } else if (f.endsWith('.html')) {
            checkHtml(full);
        }
    }
}

function checkHtml(file) {
    const html = fs.readFileSync(file, 'utf8');
    if (!html.toLowerCase().includes('nikhil')) return;
    
    const $ = cheerio.load(html);
    
    // Look at all cards/containers containing 'Nikhil'
    $('*').each((i, el) => {
        const text = $(el).text();
        const hasNikhil = text.includes('Nikhil');
        // Check if this element is an author card, mentor card, trainer card
        const cls = ($(el).attr('class') || '').toLowerCase();
        if (cls.includes('mentor') || cls.includes('trainer') || cls.includes('author') || cls.includes('card') || cls.includes('team')) {
            if (hasNikhil) {
                // Find all links inside
                $(el).find('a[href*="linkedin"]').each((j, a) => {
                    const href = $(a).attr('href');
                    console.log(`[FOUND] File: ${file}`);
                    console.log(`  Container class: ${cls}`);
                    console.log(`  Link href: ${href}`);
                    if (href.includes('neeraj')) {
                        console.log(`  >>> MISMATCH! Card mentions Nikhil but links to Neeraj!`);
                    }
                });
            }
        }
    });
}

scanDir('deployment_NeoNex');
