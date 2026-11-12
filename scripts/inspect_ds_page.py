import re
import os

path = 'deployment_NeoNex/courses/data-science-course/index.html'
txt = open(path, 'r', encoding='utf-8').read()

matches = re.findall(r'href=[\"\'][^\"\']*data-science[^\"]*[\"\']', txt)
for m in set(matches):
    print(m)

print("--- H1 and sections ---")
h1 = re.search(r'<h1.*?>(.*?)</h1>', txt, re.DOTALL)
if h1:
    print("H1:", h1.group(1).strip())

curriculum_section = re.search(r'(<section[^>]*curriculum[^>]*>.*?</section>)', txt, re.DOTALL | re.IGNORECASE)
if curriculum_section:
    print("Curriculum section found! Length:", len(curriculum_section.group(1)))
    # print first 500 chars
    print(curriculum_section.group(1)[:500])
else:
    print("No curriculum section id/class found")
