with open(r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex\index.html", "r", encoding="utf-8") as f:
    txt = f.read()

pos = txt.find('section-bg"')
print(txt[pos-50:pos+350])

