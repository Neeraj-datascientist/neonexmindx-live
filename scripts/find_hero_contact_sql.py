import re

txt = open('deployment_NeoNex/courses/sql-course/index.html', 'r', encoding='utf-8').read()

m = re.search(r'hero-contact.*?</div>', txt, re.DOTALL)
if m:
    print(m.group(0))
else:
    print("No hero-contact found")

# Look around Call 84318 03839
idx = txt.find('Call 84318 03839')
if idx != -1:
    print("Found around Call 84318 03839:")
    print(txt[max(0, idx-100):min(len(txt), idx+200)])

