import os

paths = [
    r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex\index.html",
    r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex\Neonex Mindx Home Page.html"
]

old_tag = 'alt=""\n          aria-hidden="true"\n          class="section-bg"'
new_tag = 'alt="NeoNeX MindX live interactive learning model and mentorship environment"\n          aria-hidden="true"\n          class="section-bg"'

for p in paths:
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8") as f:
            txt = f.read()
        txt = txt.replace(old_tag, new_tag)
        # Also check facebook pixel noscript
        txt = txt.replace('<noscript><img height="1" width="1" style="display:none" alt=""', '<noscript><img height="1" width="1" style="display:none" alt="Meta Tracking Pixel"')
        with open(p, "w", encoding="utf-8") as f:
            f.write(txt)
        print(f"Updated alt text in {p}")
