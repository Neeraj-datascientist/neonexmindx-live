import re

with open(r'c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex\courses\excel-power-bi-tableau-course\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

headers = re.findall(r'<button class="accordion-header"[^>]*>(.*?)</button>', html, re.DOTALL)
print(f"Total accordion buttons: {len(headers)}")
for h in headers:
    clean_h = " ".join(re.sub(r'<[^>]+>', ' ', h).split())
    print("-", clean_h)

