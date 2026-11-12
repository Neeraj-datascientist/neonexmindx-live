import re

path = 'deployment_NeoNex/syllabus/catalogues/data-science-and-ai-syllabus.html'
txt = open(path, 'r', encoding='utf-8').read()

# Let's inspect the first 2 modules
print("=== Head of data-science-and-ai-syllabus.html ===")
print(txt[:1000])

# Find Module 01 and Module 02
m1 = re.search(r'Module 01.*?</details>', txt, re.DOTALL)
if m1:
    print("\n=== Module 01 ===")
    print(m1.group(0)[:800])

m2 = re.search(r'Module 02.*?</details>', txt, re.DOTALL)
if m2:
    print("\n=== Module 02 ===")
    print(m2.group(0)[:800])

