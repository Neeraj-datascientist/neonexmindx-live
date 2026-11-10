import os
import re

targets = [
    r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex\index.html",
    r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex\Neonex Mindx Home Page.html"
]

for p in targets:
    if not os.path.exists(p):
        continue
    with open(p, "r", encoding="utf-8") as f:
        txt = f.read()

    # Pattern for the second canonical + ard block that appears around line 100
    sub_pattern = r'\n\s*<meta\s+content="Build practical skills[^"]+"\s+name="description"\s*/>\s*\n\s*<meta content="index,follow'
    sub_replacement = r'\n    <meta content="index,follow'
    txt, c1 = re.subn(sub_pattern, sub_replacement, txt, count=1)
    
    can_pattern = r'\n\s*<link href="https://neonexmindx\.com/" rel="canonical" />\s*\n\s*<link rel="ard" type="application/json" href="/\.well-known/ard\.json" />'
    # Only replace if there is more than 1 occurrence
    occurrences = len(re.findall(can_pattern, txt))
    if occurrences > 1:
        # replace the last occurrence
        parts = txt.rsplit('\n    <link href="https://neonexmindx.com/" rel="canonical" />\n    <link rel="ard" type="application/json" href="/.well-known/ard.json" />', 1)
        txt = parts[0] + parts[1]
        print(f"Removed second canonical + ard in {p}")
        
    with open(p, "w", encoding="utf-8") as f:
        f.write(txt)
    print(f"Cleaned {p} (c1={c1})")

