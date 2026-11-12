import re

idx_path = 'deployment_NeoNex/index.html'
txt = open(idx_path, 'r', encoding='utf-8').read()

# Let's inspect the entire program grid section including toolbar and eyebrow
m = re.search(r'(<section class="section soft" id="career-programs">.*?</section>)', txt, re.DOTALL)
if m:
    print(m.group(1)[:1200])

