import re

path = 'deployment_NeoNex/syllabus/catalogues/data-science-and-ai-syllabus.html'
txt = open(path, 'r', encoding='utf-8').read()

idx = txt.find('Module 01')
if idx != -1:
    print(txt[idx-50:idx+800])

idx2 = txt.find('Module 02')
if idx2 != -1:
    print("\n--- Module 02 ---")
    print(txt[idx2-50:idx2+800])

