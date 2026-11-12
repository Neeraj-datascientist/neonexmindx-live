import re

txt = open('deployment_NeoNex/courses/data-science-course/index.html', 'r', encoding='utf-8').read()
idx = txt.find('DEEP LEARNING')
# find previous <details
prev_details = txt.rfind('<details', 0, idx)
# find matching </details>
next_details = txt.find('</details>', idx) + len('</details>')
print(txt[prev_details:next_details][:300])

