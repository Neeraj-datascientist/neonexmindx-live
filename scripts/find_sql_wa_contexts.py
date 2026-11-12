import re

txt = open('deployment_NeoNex/courses/sql-course/index.html', 'r', encoding='utf-8').read()

# Let's inspect the hero actions and hero links in sql-course
idx = txt.find('WhatsApp')
while idx != -1:
    print(txt[max(0, idx-60):min(len(txt), idx+100)].replace('\n', ' '))
    idx = txt.find('WhatsApp', idx+1)
