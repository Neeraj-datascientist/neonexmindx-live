import re

txt = open('deployment_NeoNex/trainers/index.html', 'r', encoding='utf-8').read()

for m in re.finditer(r'.{0,100}https://www\.linkedin\.com/in/megha-paul02/.{0,100}', txt):
    print(m.group(0).replace('\n', ' '))

