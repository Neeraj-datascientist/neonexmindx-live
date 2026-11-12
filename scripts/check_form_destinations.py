import re

with open(r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex\index.html", "r", encoding="utf-8") as f:
    txt = f.read()

forms = re.findall(r'<form[^>]*id=["\']([^"\']+)["\']', txt)
print(f"Forms on index.html: {forms}")

# Look for lead dispatch or webhook post
for m in re.finditer(r'fetch\(|localStorage\.setItem\(["\']enquiries|dataStore\.enquiries', txt):
    start = max(0, m.start() - 50)
    end = min(len(txt), m.start() + 250)
    print("Lead dispatch snippet:\n", txt[start:end])

