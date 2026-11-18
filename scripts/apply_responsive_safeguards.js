const fs = require('fs');

const files = [
  'deployment_NeoNex/courses/machine-learning-course/index.html',
  'deployment_NeoNex/courses/python-programming-course/index.html',
  'deployment_NeoNex/courses/excel-power-bi-tableau-course/index.html',
  'deployment_NeoNex/courses/sql-course/index.html'
];

files.forEach(f => {
  let c = fs.readFileSync(f, 'utf8');
  
  // 1. Fix FAQ summary overflow
  c = c.replace(
    '.faq summary{display:flex;justify-content:space-between;gap:20px;padding:22px 4px;',
    '.faq summary{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:18px 4px;word-break:break-word;'
  );
  c = c.replace(
    '.faq summary span{font-size:1.5rem;',
    '.faq summary span{font-size:1.5rem;flex-shrink:0;margin-left:8px;'
  );
  
  // 2. Fix final-grid and contact-panel overflow for small mobile
  if (f.includes('sql-course')) {
    c = c.replace(
      '.contact-panel { padding:34px;',
      '.contact-panel { padding:24px 20px; box-sizing:border-box; max-width:100%;'
    );
    c = c.replace(
      '.lead-form { padding:34px;',
      '.lead-form { padding:24px 20px; box-sizing:border-box; max-width:100%;'
    );
    c = c.replace(
      '@media (max-width:1100px) {.hero-grid, .enquiry-band, .problem-grid, .projects-layout, .final-grid { grid-template-columns:1fr;',
      '@media (max-width:1100px) {.hero-grid, .enquiry-band, .problem-grid, .projects-layout, .final-grid { grid-template-columns:minmax(0,1fr);'
    );
  }
  
  fs.writeFileSync(f, c, 'utf8');
  console.log('Patched responsive safeguards in:', f);
});
