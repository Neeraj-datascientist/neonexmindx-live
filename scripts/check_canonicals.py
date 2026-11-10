import re

def check_file(path):
    with open(path, "r", encoding="utf-8") as f:
        txt = f.read()
    tags = re.findall(r'<link[^>]+canonical[^>]*>', txt, re.I)
    print(f"{path}:")
    for t in tags:
        print(f"  {t}")

check_file(r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex\index.html")
check_file(r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex\courses\data-analytics-course\index.html")
check_file(r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex\about-us\index.html")

