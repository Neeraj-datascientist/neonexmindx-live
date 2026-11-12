with open(r'c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex\courses\data-analytics-course\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = re.findall(r'(\.modules[^{]*\{[^}]*\})', html)
for m in matches[:10]:
    print(m)

matches2 = re.findall(r'(\.phase-grid[^{]*\{[^}]*\})', html)
for m in matches2[:10]:
    print(m)

matches3 = re.findall(r'(\.module-card[^{]*\{[^}]*\})', html)
for m in matches3[:10]:
    print(m)

