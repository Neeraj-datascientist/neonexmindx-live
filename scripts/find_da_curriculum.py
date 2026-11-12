with open(r'c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex\courses\data-analytics-course\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('id="curriculum"')
if pos != -1:
    print(html[pos:pos+3000])
else:
    print("Curriculum not found in data-analytics")
