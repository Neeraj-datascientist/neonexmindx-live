import re

b = 'deployment_NeoNex/blog/2026-breakthroughs-in-ai-agents-llms/index.html'
txt = open(b, 'r', encoding='utf-8').read()
match = re.search(r'<div class="share-tray">.*?</div>', txt, re.DOTALL)
if match:
    print(match.group(0))

