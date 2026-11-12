with open('deployment_NeoNex/trainers/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
pos = html.find('linkedin.com/in/')
while pos != -1:
    print(html[pos-30:pos+80])
    pos = html.find('linkedin.com/in/', pos + 1)

