import glob
import re

files = glob.glob('deployment_NeoNex/**/*.html', recursive=True)

matches = []
for f in files:
    txt = open(f, 'r', encoding='utf-8', errors='ignore').read()
    # find <a ...>Request My Program and Trainer Plan</a>
    m = re.findall(r'<a[^>]*Request My Program and Trainer Plan</a>', txt)
    if m:
        matches.append((f, m))

print(f"Files with 'Request My Program and Trainer Plan': {len(matches)}")
for f, m in matches:
    print(f, m)
