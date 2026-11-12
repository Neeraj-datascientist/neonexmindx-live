import re

txt = open('deployment_NeoNex/courses/data-science-course/index.html', 'r', encoding='utf-8').read()

modules = re.findall(r'<details[^>]*>.*?<summary[^>]*>(.*?)</summary>.*?</details>', txt, re.DOTALL)
print(f"Total modules in data-science-course: {len(modules)}")
for i, m in enumerate(modules):
    clean = re.sub(r'<[^>]+>', ' ', m)
    clean = ' '.join(clean.split())
    print(f"  {i+1}: {clean}")
