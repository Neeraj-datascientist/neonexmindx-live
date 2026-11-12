import re

robots_path = r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex\robots.txt"
with open(robots_path, "r", encoding="utf-8") as f:
    txt = f.read()

lines = txt.splitlines()
new_lines = []
for l in lines:
    if any(k in l for k in ['/courses/sql-course/', '/courses/python-programming-course/', '/courses/excel-power-bi-tableau-course/', '/courses/machine-learning-course/']):
        continue
    new_lines.append(l)

new_txt = "\n".join(new_lines) + "\n"
with open(robots_path, "w", encoding="utf-8") as f:
    f.write(new_txt)

print("Removed short course disallow rules from robots.txt so Google & Bing can index them!")

