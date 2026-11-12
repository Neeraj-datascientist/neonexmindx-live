txt = open('deployment_NeoNex/trainers/index.html', 'r', encoding='utf-8').read()
idx = txt.find('"name": "Venkat Nagarjun"')
print(txt[idx:idx+400])
