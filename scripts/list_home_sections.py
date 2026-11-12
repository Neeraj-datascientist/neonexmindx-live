import re

idx_path = 'deployment_NeoNex/index.html'
txt = open(idx_path, 'r', encoding='utf-8').read()

matches = re.finditer(r'<section.*?</section>', txt, re.DOTALL)
for i, m in enumerate(matches):
    s = m.group(0)
    h = re.search(r'<h[123][^>]*>(.*?)</h[123]>', s)
    eyebrow = re.search(r'class="eyebrow"[^>]*>(.*?)<', s)
    id_m = re.search(r'id=["\']([^"\']*)["\']', s)
    print(f"Section {i+1}: ID={id_m.group(1) if id_m else 'None'} | Eyebrow={eyebrow.group(1) if eyebrow else 'None'} | Heading={h.group(1) if h else 'None'}")

