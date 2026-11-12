with open('deployment_NeoNex/courses/data-analytics-course/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
mentor_cards = re.findall(r'<article class="mentor-card">.*?</article>', html, re.DOTALL)
print(f"Found {len(mentor_cards)} mentor cards in Data Analytics:")

trainer_links = {}
for mc in mentor_cards:
    name = re.search(r'<h3>(.*?)</h3>', mc)
    link = re.search(r'href="(https://www\.linkedin\.com/[^"]+)"', mc)
    if name and link:
        n = name.group(1).strip()
        l = link.group(1).strip()
        trainer_links[n] = l
        print(f"  {n} -> {l}")

import json
with open('deployment_NeoNex/scripts/official_mentor_linkedin.json', 'w', encoding='utf-8') as f:
    json.dump(trainer_links, f, indent=2)
print("Saved official links mapping.")
