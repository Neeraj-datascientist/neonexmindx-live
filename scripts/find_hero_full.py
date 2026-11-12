import re

idx_path = 'deployment_NeoNex/index.html'
txt = open(idx_path, 'r', encoding='utf-8').read()

m = re.search(r'<section class="hero".*?</section>', txt, re.DOTALL)
if m:
    print("=== HERO SECTION ===")
    print(m.group(0))

# Next section after hero
m2 = re.search(r'</section>\s*(<section.*?</section>)', txt[txt.find('<section class="hero"'):], re.DOTALL)
if m2:
    print("=== NEXT SECTION AFTER HERO ===")
    print(m2.group(1)[:1500])

