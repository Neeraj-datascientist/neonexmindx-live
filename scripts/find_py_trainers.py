with open(r'c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex\courses\python-programming-course\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = re.findall(r'<article class="trainer-card">.*?</article>', html, re.DOTALL)
print(f"Total trainer cards in Python: {len(matches)}")
for m in matches:
    print('-------------------')
    print(' '.join(m.split()))

