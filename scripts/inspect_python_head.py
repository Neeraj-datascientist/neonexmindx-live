with open(r'deployment_NeoNex/courses/python-programming-course/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
print("Python head:")
print(html[html.find('<head>'):html.find('</head>')+7])

