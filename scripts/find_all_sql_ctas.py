import re

txt = open('deployment_NeoNex/courses/sql-course/index.html', 'r', encoding='utf-8').read()

print("Buttons in SQL course:")
for m in re.finditer(r'<button\b[^>]*>(.*?)</button>', txt, re.DOTALL):
    print("Button:", m.group(0)[:150].replace('\n', ' '))

print("\nCall-to-action links in SQL course:")
for m in re.finditer(r'<a\b[^>]*class=[\"\'][^\"\']*(?:btn|cta|enquire)[^\"\']*[\"\'][^>]*>(.*?)</a>', txt, re.DOTALL):
    print("CTA Link:", m.group(0)[:150].replace('\n', ' '))
