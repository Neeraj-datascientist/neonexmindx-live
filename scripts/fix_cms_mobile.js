const fs = require('fs');
let c = fs.readFileSync('deployment_NeoNex/cms/index.html', 'utf8');

// Find @media (max-width: 768px) and add topbar responsive handling
const oldRule = `@media (max-width: 768px) {
      body {
        grid-template-columns: 1fr;
        grid-template-areas: "top" "main";
      }`;

const newRule = `@media (max-width: 768px) {
      body {
        grid-template-columns: 1fr;
        grid-template-areas: "top" "main";
      }
      #topbar {
        padding: 0 12px;
        overflow-x: hidden;
      }
      .tb-actions {
        gap: 6px;
      }
      .tb-actions .btn span, .tb-actions a span {
        display: none;
      }
      .tb-actions .btn, .tb-actions a {
        padding: 6px 10px;
      }`;

if (c.includes(oldRule)) {
  c = c.replace(oldRule, newRule);
  fs.writeFileSync('deployment_NeoNex/cms/index.html', c, 'utf8');
  console.log('Successfully added mobile rules to cms/index.html');
} else {
  console.log('Old rule not found!');
}
