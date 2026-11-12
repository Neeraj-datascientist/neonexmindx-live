import glob
import re

b = 'deployment_NeoNex/blog/2026-breakthroughs-in-ai-agents-llms/index.html'
txt = open(b, 'r', encoding='utf-8').read()

scripts = re.findall(r'<script.*?</script>', txt, re.DOTALL)
for s in scripts:
    if 'shareTitle' in s or 'currentUrl' in s:
        print("Found in script:", s)

if not any('shareTitle' in s or 'currentUrl' in s for s in scripts):
    print("NO SCRIPT DEFINES shareTitle OR currentUrl in static blog post!")
