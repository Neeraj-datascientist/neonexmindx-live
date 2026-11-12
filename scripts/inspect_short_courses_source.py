import os
import re

source_files = [
    r"c:\Users\pcnee\Desktop\NeoNeX MindX website\Cleaned HTML\Neonex Mindx Python Programming Course.html",
    r"c:\Users\pcnee\Desktop\NeoNeX MindX website\Cleaned HTML\Neonex Mindx Excel PowerBI Tableau Course.html",
    r"c:\Users\pcnee\Desktop\NeoNeX MindX website\Cleaned HTML\Neonex Mindx SQL Course.html"
]

for sf in source_files:
    if os.path.exists(sf):
        size = os.path.getsize(sf)
        print(f"{os.path.basename(sf)}: {size} bytes")
        with open(sf, "r", encoding="utf-8", errors="ignore") as fp:
            txt = fp.read()
        title = re.search(r'<title>(.*?)</title>', txt, re.I)
        h1 = re.search(r'<h1[^>]*>(.*?)</h1>', txt, re.I | re.S)
        print(f"  Title: {title.group(1) if title else 'NONE'}")
        print(f"  H1: {h1.group(0).strip() if h1 else 'NONE'}")

