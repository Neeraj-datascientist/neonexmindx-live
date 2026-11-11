import os

paths = [
    r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex\index.html",
    r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex\Neonex Mindx Home Page.html"
]

old_desc = "Build practical skills through live online Data Analytics, Data Science, AI/ML Engineering, Data Engineering and Business Analytics programs with projects, mentors and honest career support."
new_desc = "Live online Data Analytics, Data Science, AI/ML, Data Engineering & Business Analytics programs with real projects, mentors & honest career support."

print(f"Old length: {len(old_desc)} | New length: {len(new_desc)}")

for p in paths:
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8") as f:
            txt = f.read()
        txt = txt.replace(old_desc, new_desc)
        with open(p, "w", encoding="utf-8") as f:
            f.write(txt)
        print(f"Updated description in {p}")
