import re

txt = open('deployment_NeoNex/index.html', 'r', encoding='utf-8').read()

m = re.search(r'<div class="program-grid" id="programGrid">.*?</div>\s*<div class="section-action', txt, re.DOTALL)
if m:
    cards = re.findall(r'<article class="program-card[^"]*".*?</article>', m.group(0), re.DOTALL)
    print(f"Total program cards: {len(cards)}")
    for c in cards:
        title = re.search(r'<h3[^>]*>(.*?)</h3>', c)
        dur = re.search(r'class="duration"[^>]*>(.*?)<', c)
        cat = re.search(r'data-category="([^"]*)"', c)
        print("  Card:", title.group(1) if title else 'None', "| Duration:", dur.group(1) if dur else 'None', "| Cat:", cat.group(1) if cat else 'None')
