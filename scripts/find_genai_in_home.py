import re

txt = open('deployment_NeoNex/index.html', 'r', encoding='utf-8').read()

print("Generative AI Engineering in home page?")
for m in re.finditer(r'generative[- ]ai|genai', txt, re.IGNORECASE):
    snippet = txt[max(0, m.start()-50):min(len(txt), m.end()+100)]
    print("Match:", snippet.replace('\n', ' '))
