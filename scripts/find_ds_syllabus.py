with open(r'deployment_NeoNex\courses\data-science-course\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
print("Title:", re.findall(r'<title>(.*?)</title>', html))
print("H1:", re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL))
print("Syllabus links:")
for m in re.finditer(r'href=["\']([^"\']*syllabus[^"\']*)["\']', html):
    print("  ", m.group(1))

