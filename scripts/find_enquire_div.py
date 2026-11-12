import re

txt = open('deployment_NeoNex/courses/sql-course/index.html', 'r', encoding='utf-8').read()
idx = txt.find('id="enquire"')
print("Surrounding 300 chars:")
print(txt[max(0, idx-100):min(len(txt), idx+200)])
