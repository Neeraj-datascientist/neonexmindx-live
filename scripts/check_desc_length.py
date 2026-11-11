import re

with open(r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex\index.html", "r", encoding="utf-8") as f:
    txt = f.read()

m = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']*)["\']', txt, re.I)
if not m:
    m = re.search(r'<meta[^>]+content=["\']([^"\']*)["\'][^>]+name=["\']description["\']', txt, re.I)

desc = m.group(1) if m else "NOT FOUND"
print(f"Current Description Length: {len(desc)} chars")
print(f"Content: '{desc}'")
