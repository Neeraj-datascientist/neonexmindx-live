import glob
import os
import re

ROOT = r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex"
html_files = glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True)

fb_empty = 'src="https://www.facebook.com/tr?id=1698036971288322&ev=PageView&noscript=1"/>'
count = 0

for f in html_files:
    if any(k in f.lower() for k in [".git", "savepoints", "cms", "admin", "node_modules"]):
        continue
    with open(f, "r", encoding="utf-8", errors="ignore") as fp:
        txt = fp.read()
    
    new_txt = txt.replace('alt="" src="https://www.facebook.com/tr?id=1698036971288322', 'alt="Facebook Pixel" src="https://www.facebook.com/tr?id=1698036971288322')
    new_txt = new_txt.replace("alt='' src=\"https://www.facebook.com/tr?id=1698036971288322", 'alt="Facebook Pixel" src="https://www.facebook.com/tr?id=1698036971288322')
    
    if new_txt != txt:
        with open(f, "w", encoding="utf-8") as fp:
            fp.write(new_txt)
        count += 1

print(f"Added descriptive alt='Facebook Pixel' across {count} HTML files.")
