import re

txt = open('deployment_NeoNex/trainers/index.html', 'r', encoding='utf-8').read()

m = re.search(r'<h3>Megha.*?</h3>.*?</article>', txt, re.DOTALL)
if m:
    print(m.group(0))
else:
    print("No regex match for Megha card")

