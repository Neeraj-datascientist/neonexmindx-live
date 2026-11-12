txt = open('deployment_NeoNex/courses/data-science-course/index.html', 'r', encoding='utf-8').read()
for line in txt.splitlines():
    if 'track' in line.lower() or 'module 14' in line.lower() or 'module 15' in line.lower():
        print(line[:120])
