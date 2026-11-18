const fs = require('fs');
let c = fs.readFileSync('deployment_NeoNex/cms/index.html', 'utf8');

const target = '@media (max-width: 768px) {';
const pos = c.indexOf(target);
if (pos !== -1) {
  const insertPos = pos + target.length;
  const injection = `
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
  c = c.substring(0, insertPos) + injection + c.substring(insertPos);
  fs.writeFileSync('deployment_NeoNex/cms/index.html', c, 'utf8');
  console.log('Successfully injected topbar mobile rules into cms/index.html');
} else {
  console.log('Target not found');
}
