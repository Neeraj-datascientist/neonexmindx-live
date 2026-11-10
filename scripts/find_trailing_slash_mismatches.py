import glob
import re
import os

files = glob.glob(r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex\**\*.html", recursive=True)

mismatches = []
for f in files:
    if any(k in f.lower() for k in [".git", "node_modules", "savepoints", "cms"]):
        continue
    with open(f, "r", encoding="utf-8", errors="ignore") as fp:
        txt = fp.read()
    
    # Check duplicate canonicals
    can_matches = re.findall(r'<link[^>]+canonical[^>]*>', txt, re.I)
    if len(can_matches) > 1:
        print(f"DUPLICATE CANONICAL IN {f}: {len(can_matches)} tags")

    # Check trailing slash in canonical
    m = re.search(r'<link[^>]+(?:href=["\']([^"\']+)["\'][^>]*rel=["\']canonical["\']|rel=["\']canonical["\'][^>]*href=["\']([^"\']+)["\'])', txt, re.I)
    if m:
        c = m.group(1) if m.group(1) else m.group(2)
        if c.rstrip("/") != "https://neonexmindx.com" and c.endswith("/"):
            mismatches.append((f, c))

print(f"Total files where canonical has trailing slash: {len(mismatches)}")
for f, c in mismatches[:10]:
    rel = os.path.relpath(f, r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex")
    print(f"  {rel} -> {c}")
