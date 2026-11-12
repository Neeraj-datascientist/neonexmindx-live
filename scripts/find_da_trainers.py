with open('deployment_NeoNex/courses/data-analytics-course/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = re.findall(r'<article class="trainer-card">.*?</article>', html, re.DOTALL)
print(f"Total trainer cards in Data Analytics: {len(matches)}")
for m in matches:
    print('-------------------')
    print(' '.join(m.split()))

