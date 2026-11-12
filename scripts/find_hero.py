import re

idx_path = 'deployment_NeoNex/index.html'
txt = open(idx_path, 'r', encoding='utf-8').read()

m = re.search(r'<header.*?</header>\s*<main.*?</section>', txt, re.DOTALL)
if m:
    print("=== HEADER TO FIRST SECTION ===")
    print(m.group(0)[:1500])
else:
    # let's find <main
    main_idx = txt.find('<main')
    print("=== MAIN SNIPPET ===")
    print(txt[main_idx:main_idx+1500])
