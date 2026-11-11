import re

with open(r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex\index.html", "r", encoding="utf-8") as f:
    txt = f.read()

imgs = re.findall(r'<img[^>]*>', txt, re.I)
print(f"Total img tags found: {len(imgs)}")
for idx, img in enumerate(imgs):
    alt_val = re.search(r'alt=["\']([^"\']*)["\']', img, re.I)
    val = alt_val.group(1) if alt_val else "MISSING"
    print(f"Img {idx+1}: alt='{val}' | {img[:90]}")

