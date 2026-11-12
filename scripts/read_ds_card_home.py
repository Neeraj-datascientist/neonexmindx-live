import re

idx_path = 'deployment_NeoNex/index.html'
txt = open(idx_path, 'r', encoding='utf-8').read()

m = re.search(r'<article class="program-card" data-category="science">.*?</article>', txt, re.DOTALL)
if m:
    print("=== DATA SCIENCE CARD IN HOME ===")
    print(m.group(0))

m_ai = re.search(r'<article class="program-card" data-category="ai">.*?</article>', txt, re.DOTALL)
if m_ai:
    print("=== AI CARD IN HOME ===")
    print(m_ai.group(0))

