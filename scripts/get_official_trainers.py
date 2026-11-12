with open('deployment_NeoNex/trainers/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
trainers = re.findall(r'<article[^>]*class=["\']trainer-card["\'][^>]*>[\s\S]*?</article>', html)
print(f"Total trainers in trainers/index.html: {len(trainers)}")
for t in trainers:
    name = re.search(r'<h3>(.*?)</h3>', t)
    title = re.search(r'<p>(.*?)</p>', t)
    href = re.search(r'href=["\']([^"\']+)["\']', t)
    print(f"Name: {name.group(1) if name else 'N/A'} | Title: {title.group(1) if title else 'N/A'} | Link: {href.group(1) if href else 'N/A'}")
