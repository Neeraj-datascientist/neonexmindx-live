import re

txt = open('deployment_NeoNex/syllabus/catalogues/data-science-and-ai-syllabus.html', 'r', encoding='utf-8').read()

m = re.search(r'\.topic-content-body\s*\{[^}]*\}', txt)
if m:
    print(m.group(0))

# print all rules containing .topic-content-body
for m in re.finditer(r'([^{}]*\.topic-content-body[^{]*\{[^}]*\})', txt):
    print("Rule:", m.group(1))

