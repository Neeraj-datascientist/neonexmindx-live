with open(r'c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex\courses\excel-power-bi-tableau-course\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('id="curriculum"')
if pos != -1:
    print(html[pos:pos+1500])
else:
    print("curriculum id not found, searching 'curriculum'")
    pos2 = html.find('curriculum')
    print(html[pos2:pos2+1000])

