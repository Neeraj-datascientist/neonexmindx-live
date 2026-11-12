import re

idx_path = 'deployment_NeoNex/index.html'
txt = open(idx_path, 'r', encoding='utf-8').read()

m = re.search(r'<section class="section soft" id="focused-short-courses">.*?</section>', txt, re.DOTALL)
if m:
    print("=== focused-short-courses ===")
    print(m.group(0))

