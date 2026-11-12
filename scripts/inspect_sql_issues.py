import re

path = 'deployment_NeoNex/courses/sql-course/index.html'
txt = open(path, 'r', encoding='utf-8').read()

print("=== WhatsApp elements in SQL course ===")
for m in re.finditer(r'<[a-z]+[^>]*whatsapp[^>]*>.*?</[a-z]+>', txt, re.IGNORECASE):
    print(m.group(0))

for m in re.finditer(r'<a\b[^>]*wa\.me[^>]*>.*?</a>', txt, re.DOTALL):
    print("WA link:", m.group(0))

print("\n=== Download syllabus elements in SQL course ===")
for m in re.finditer(r'<[a-z]+[^>]*syllabus[^>]*>.*?</[a-z]+>', txt, re.IGNORECASE):
    print("Syllabus element:", m.group(0)[:200])

for m in re.finditer(r'<a\b[^>]*href=[\"\'][^\"\']*syllabus[^\"\']*[\"\'][^>]*>.*?</a>', txt, re.DOTALL | re.IGNORECASE):
    print("Syllabus link:", m.group(0))
