import re

txt = open('deployment_NeoNex/courses/sql-course/index.html', 'r', encoding='utf-8').read()

print("Does id='enquire' exist?")
for m in re.finditer(r'id=[\"\'][^\"\']*enquire[^\"\']*[\"\']', txt):
    print(" ", m.group(0))

print("\nDoes #enquire jump to anything?")
forms = re.findall(r'<form[^>]*>', txt)
for f in forms:
    print(" Form tag:", f)

