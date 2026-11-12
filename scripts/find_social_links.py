import re

with open(r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex\index.html", "r", encoding="utf-8") as f:
    txt = f.read()

links = set(re.findall(r'href=["\'](https?://(?:www\.)?(?:linkedin|youtube|instagram|facebook|twitter|x)\.com/[^"\']*)["\']', txt, re.I))
print("Social links found in index.html:")
for l in sorted(links):
    print(f"  {l}")

