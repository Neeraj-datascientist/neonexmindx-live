import glob
import re

files = glob.glob('deployment_NeoNex/blog/*/index.html')
for f in files:
    txt = open(f, 'r', encoding='utf-8').read()
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', txt, re.DOTALL)
    title = re.search(r'<title>(.*?)</title>', txt, re.DOTALL)
    print(f, "->", title.group(1) if title else "NO TITLE", "| H1:", h1.group(1).strip() if h1 else "NO H1")
