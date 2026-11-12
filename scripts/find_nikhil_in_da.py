with open('deployment_NeoNex/courses/data-analytics-course/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
pos = html.find('Nikhil')
while pos != -1:
    print("--- FOUND NIKHIL IN DA ---")
    print(html[max(0, pos-200):min(len(html), pos+400)])
    pos = html.find('Nikhil', pos + 1)

