with open('deployment_NeoNex/courses/data-analytics-course/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
mentor_cards = re.findall(r'<article class="mentor-card">.*?</article>', html, re.DOTALL)
for mc in mentor_cards:
    if 'Venkat' in mc or 'Nagarjun' in mc:
        print("Venkat card in DA:")
        print(mc)

