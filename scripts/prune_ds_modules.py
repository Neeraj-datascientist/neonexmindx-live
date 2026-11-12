import re

txt = open('deployment_NeoNex/courses/data-science-course/index.html', 'r', encoding='utf-8').read()

modules = re.findall(r'<details class="module-card"[^>]*>.*?</details>', txt, re.DOTALL)
print(f"Total details.module-card found: {len(modules)}")

to_remove = []
for m in modules:
    if any(k in m for k in ['DEEP LEARNING', 'NATURAL LANGUAGE PROCESSING', 'COMPUTER VISION', 'GENERATIVE AI PRACTICAL CRASH COURSE']):
        to_remove.append(m)

print(f"Removing {len(to_remove)} advanced AI modules from data-science-course...")
for r in to_remove:
    txt = txt.replace(r, '')

with open('deployment_NeoNex/courses/data-science-course/index.html', 'w', encoding='utf-8') as f:
    f.write(txt)

print("data-science-course now exclusively features the Pure Data Science curriculum!")

