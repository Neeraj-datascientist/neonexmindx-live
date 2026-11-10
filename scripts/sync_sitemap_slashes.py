import os
import re

sitemap_path = r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex\sitemap.xml"
with open(sitemap_path, "r", encoding="utf-8") as f:
    xml = f.read()

# We want trailing slash on all directory endpoints, but NOT on individual blog post files (since they are /blog/<slug>)
# Actually let's check what canonical says for each:
# /about-us/ -> has trailing slash
# /trainers/ -> has trailing slash
# /contact-us/ -> has trailing slash
# /courses/*-course/ -> has trailing slash
# /blogs/ -> has trailing slash
# /privacy-policy/ -> has trailing slash
# /terms-and-conditions/ -> has trailing slash
# /refund-and-cancellation-policy/ -> has trailing slash
# /placement-assistance-disclaimer/ -> has trailing slash

lines = xml.splitlines()
new_lines = []
for line in lines:
    m = re.search(r'<loc>(https://neonexmindx\.com/[^<]+)</loc>', line)
    if m:
        u = m.group(1)
        if not u.endswith("/"):
            # check if it is not a direct file
            u = u + "/"
            line = f"    <loc>{u}</loc>"
    new_lines.append(line)

new_xml = "\n".join(new_lines) + "\n"
with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write(new_xml)

print("Updated sitemap.xml with canonical trailing slashes.")
