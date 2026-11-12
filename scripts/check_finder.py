import re

txt = open('deployment_NeoNex/index.html', 'r', encoding='utf-8').read()
prog_finder = re.search(r'<section[^>]*id=["\']program-finder["\'].*?</section>', txt, re.DOTALL)
if prog_finder:
    print("=== PROGRAM FINDER ===")
    print(prog_finder.group(0)[:1500])

