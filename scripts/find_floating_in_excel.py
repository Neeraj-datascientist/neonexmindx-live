txt = open('deployment_NeoNex/courses/excel-power-bi-tableau-course/index.html', 'r', encoding='utf-8').read()
idx = txt.lower().find('float')
while idx != -1:
    print(txt[max(0, idx-40):min(len(txt), idx+100)].replace('\n', ' '))
    idx = txt.lower().find('float', idx+1)

