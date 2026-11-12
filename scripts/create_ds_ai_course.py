import shutil
import os
import re

src = 'deployment_NeoNex/courses/data-science-course/index.html'
dst_dir = 'deployment_NeoNex/courses/data-science-and-ai-course'
os.makedirs(dst_dir, exist_ok=True)
dst = os.path.join(dst_dir, 'index.html')

content = open(src, 'r', encoding='utf-8').read()

# Update title, canonical, og:url, og:title, h1, descriptions
content = content.replace(
    '<title>Data Science Course Online India | NeoNex MindX</title>',
    '<title>Data Science and AI Course Online India | NeoNex MindX</title>'
)
content = content.replace(
    'https://neonexmindx.com/courses/data-science-course/',
    'https://neonexmindx.com/courses/data-science-and-ai-course/'
)
content = content.replace(
    'href="/courses/data-science-course/"',
    'href="/courses/data-science-and-ai-course/"'
)
content = content.replace(
    'Live Online Data Science Course in India',
    'Live Online Data Science and AI Master Course in India'
)
content = content.replace(
    'Data Science Course in India',
    'Data Science and AI Master Course in India'
)

# Ensure syllabus link points strictly to data-science-and-ai-syllabus.html
content = content.replace(
    '/syllabus/catalogues/data-science-syllabus.html',
    '/syllabus/catalogues/data-science-and-ai-syllabus.html'
)

with open(dst, 'w', encoding='utf-8') as f:
    f.write(content)

print("Created courses/data-science-and-ai-course/index.html successfully!")

