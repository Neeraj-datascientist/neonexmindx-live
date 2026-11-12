import re

txt = open('deployment_NeoNex/trainers/index.html', 'r', encoding='utf-8').read()
idx = txt.find('https://www.linkedin.com/in/megha-paul02/')
print("Surrounding 300 chars:")
print(txt[idx-150:idx+200])
