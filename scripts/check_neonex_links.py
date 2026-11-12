import glob
import re

files = glob.glob('deployment_NeoNex/**/*.html', recursive=True)

matches = []
for f in files:
    txt = open(f, 'r', encoding='utf-8').read()
    if 'href="https://neonexmindx.com/"' in txt:
        # find the element
        for m in re.finditer(r'<a\b[^>]*href=[\"\']https://neonexmindx\.com/?[\"\'][^>]*>(.*?)</a>', txt, re.DOTALL):
            matches.append((f, m.group(0)[:150]))

print(f"Total matching elements: {len(matches)}")
for f, snippet in matches:
    print(f, "->", snippet.replace('\n', ' '))

