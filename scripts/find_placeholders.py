with open(r'deployment_NeoNex/courses/python-programming-course/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

for word in ['TODO', 'example.com', 'undefined']:
    matches = [m.start() for m in re.finditer(re.escape(word), html, re.I)]
    print(f"Word '{word}': {len(matches)} occurrences")
    for pos in matches[:3]:
        snippet = html[max(0, pos-40):min(len(html), pos+60)]
        print("  Snippet:", " ".join(snippet.split()))
