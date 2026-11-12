import re

txt = open('deployment_NeoNex/courses/data-science-course/index.html', 'r', encoding='utf-8').read()
m = re.search(r'<table[^>]*>.*?Program Duration.*?</table>', txt, re.DOTALL)
if m:
    print("=== SUMMARY TABLE IN DATA SCIENCE COURSE ===")
    print(m.group(0))
