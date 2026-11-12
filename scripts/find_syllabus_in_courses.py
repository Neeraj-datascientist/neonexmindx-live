import re
import os

courses = [
    'courses/data-science-course/index.html',
    'courses/ai-ml-course/index.html',
    'courses/ai-ml-engineering-course/index.html'
]

for c in courses:
    path = os.path.join('deployment_NeoNex', c)
    if os.path.exists(path):
        txt = open(path, 'r', encoding='utf-8').read()
        syls = set(re.findall(r'/syllabus/[a-zA-Z0-9_\-\./]+', txt))
        print(f"=== {c} ===")
        for s in syls:
            print(f"  {s}")

