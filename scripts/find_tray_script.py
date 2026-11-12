import re

b = 'deployment_NeoNex/blog/2026-breakthroughs-in-ai-agents-llms/index.html'
txt = open(b, 'r', encoding='utf-8').read()

match = re.search(r'const shareTitle.*?;', txt)
if match:
    print(match.group(0))

share_tray_in_script = re.search(r'<div class="share-tray">.*?</div>', txt, re.DOTALL)
if share_tray_in_script:
    print("Found share tray in template string!")
    print(share_tray_in_script.group(0))
