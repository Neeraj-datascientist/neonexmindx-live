with open(r'c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex\courses\data-analytics-course\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = re.findall(r'(\.modules[^{]*\{[^}]*\})', html)
for m in matches:
    print(m)

# Find CSS for .modules.phase-grid-spaced or media queries
matches2 = re.findall(r'([^{}]*modules[^{}]*\{[^}]*\})', html)
for m in matches2:
    print(m)

