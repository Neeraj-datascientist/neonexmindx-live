import re

with open(r'c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex\courses\excel-power-bi-tableau-course\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

summaries = re.findall(r'<summary>(.*?)</summary>', html, re.DOTALL)
print(f"Total modules in curriculum: {len(summaries)}")
for s in summaries:
    clean = " ".join(re.sub(r'<[^>]+>', ' ', s).split())
    print("-", clean)

