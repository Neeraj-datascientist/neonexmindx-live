import glob
import re

files = glob.glob('deployment_NeoNex/**/*.html', recursive=True)

old_nav = '''          <a href="/courses/data-analytics-course/">Data Analytics Course</a>
          <a href="/courses/data-science-course/">Data Science Course</a>
          <a href="/courses/ai-ml-course/">AI &amp; ML Engineering Course</a>'''

new_nav = '''          <a href="/courses/data-analytics-course/">Data Analytics Course</a>
          <a href="/courses/data-science-course/">Data Science Course</a>
          <a href="/courses/data-science-and-ai-course/">Data Science &amp; AI Course</a>
          <a href="/courses/ai-ml-course/">AI &amp; ML Engineering Course</a>'''

count = 0
for f in files:
    txt = open(f, 'r', encoding='utf-8').read()
    if old_nav in txt:
        txt = txt.replace(old_nav, new_nav)
        with open(f, 'w', encoding='utf-8') as out:
            out.write(txt)
        count += 1

print(f"Updated header navigation in {count} HTML files!")
