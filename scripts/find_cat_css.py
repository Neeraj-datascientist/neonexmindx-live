import re

path = 'deployment_NeoNex/syllabus/catalogues/data-science-and-ai-syllabus.html'
txt = open(path, 'r', encoding='utf-8').read()

# Let's search for CSS rules on .module, .module-body, .topic-group, .bullet-list
styles = re.findall(r'(\.[a-zA-Z0-9_\-]+\s*\{[^}]*\})', txt)
for s in styles:
    if any(k in s for k in ['module', 'topic', 'bullet', 'list', 'line', 'border']):
        print(s)

