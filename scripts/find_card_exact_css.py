with open(r'c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex\courses\data-analytics-course\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = re.findall(r'(\.module-card[^{]*\{[^}]*\})', html)
for m in set(matches):
    print(m)

matches2 = re.findall(r'(\.module-toggle[^{]*\{[^}]*\})', html)
for m in set(matches2):
    print(m)

matches3 = re.findall(r'(\.module-num[^{]*\{[^}]*\})', html)
for m in set(matches3):
    print(m)

matches4 = re.findall(r'(\.module-panel[^{]*\{[^}]*\})', html)
for m in set(matches4):
    print(m)
