import re

with open(r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex\index.html", "r", encoding="utf-8") as f:
    txt = f.read()

can_count = len(re.findall(r'<link[^>]+canonical[^>]*>', txt, re.I))
desc_count = len(re.findall(r'<meta[^>]+name=["\']description["\'][^>]*>', txt, re.I))

imgs = re.findall(r'<img[^>]*>', txt, re.I)
missing_alt = [img for img in imgs if 'alt=' not in img.lower()]

print(f"Index.html Audit in working tree:")
print(f"  Canonical tags count: {can_count}")
print(f"  Meta description count: {desc_count}")
print(f"  Total images: {len(imgs)}")
print(f"  Images missing alt: {len(missing_alt)}")
for m in missing_alt:
    print(f"    -> {m}")

