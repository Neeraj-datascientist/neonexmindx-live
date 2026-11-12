import re

idx_path = 'deployment_NeoNex/index.html'
txt = open(idx_path, 'r', encoding='utf-8').read()

m = re.search(r'<section class="section soft" id="career-programs">.*?</section>', txt, re.DOTALL)
if m:
    print("=== career-programs ===")
    print(m.group(0))

m_comp = re.search(r'<table class="compare">.*?</table>', txt, re.DOTALL)
if m_comp:
    print("=== compare table ===")
    print(m_comp.group(0))
