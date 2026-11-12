import re

txt = open('deployment_NeoNex/courses/data-science-course/index.html', 'r', encoding='utf-8').read()
idx = txt.find('DEEP LEARNING')
print("Surrounding 300 chars of DEEP LEARNING:")
print(txt[max(0, idx-100):min(len(txt), idx+200)])
