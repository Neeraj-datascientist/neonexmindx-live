import re

txt = open('deployment_NeoNex/trainers/index.html', 'r', encoding='utf-8').read()

# Let's inspect the trainer cards in trainers/index.html
cards = re.findall(r'<article class="trainer-card".*?</article>', txt, re.DOTALL)
print(f"Total trainer cards: {len(cards)}")
for c in cards:
    name = re.search(r'<h3>(.*?)</h3>', c)
    li = re.search(r'href=[\"\']([^\"\']*linkedin[^\"\']*)[\"\']', c)
    print("Trainer:", name.group(1) if name else 'None', "-> LinkedIn:", li.group(1) if li else 'None')

