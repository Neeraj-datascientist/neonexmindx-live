import os
import glob
import re

files = glob.glob('deployment_NeoNex/**/*.html', recursive=True)

# 1. Check for empty links href="" or href="#"
empty_hrefs = []
broken_placeholders = []
broken_images = []

for f in files:
    txt = open(f, 'r', encoding='utf-8', errors='ignore').read()
    # check href=""
    for m in re.finditer(r'href=[\"\']\s*[\"\']', txt):
        empty_hrefs.append((f, m.start()))
    # check ${...} in static HTML outside of <script>
    # remove <script> tags
    no_script = re.sub(r'<script.*?</script>', '', txt, flags=re.DOTALL)
    for m in re.finditer(r'\$\{([a-zA-Z0-9_\.]+)\}', no_script):
        broken_placeholders.append((f, m.group(0)))

print(f"Empty hrefs found: {len(empty_hrefs)}")
for f, pos in empty_hrefs[:10]:
    print("  ", f)

print(f"Broken JS template literals in static HTML: {len(broken_placeholders)}")
for f, ph in broken_placeholders[:10]:
    print("  ", f, ph)
