import os
import re

ROOT = r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex"

pages_to_check = [
    ("Home", "index.html"),
    ("Home-Alt", "Neonex Mindx Home Page.html"),
    ("Data Analytics", "courses/data-analytics-course/index.html"),
    ("Data Science", "courses/data-science-course/index.html"),
    ("AI & ML (courses)", "courses/ai-ml-engineering-course/index.html"),
    ("AI & ML (root)", "ai-ml-course/index.html"),
    ("Data Engineering (courses)", "courses/data-engineering-course/index.html"),
    ("Data Engineering (root)", "data-engineering-course/index.html"),
    ("Business Analytics (courses)", "courses/business-analytics-course/index.html"),
    ("Business Analytics (root)", "business-analytics-course/index.html"),
    ("Generative AI (courses)", "courses/generative-ai-engineering-course/index.html"),
    ("Generative AI (root)", "generative-ai-engineering-course/index.html"),
    ("About Us", "about-us/index.html"),
    ("Trainers", "trainers/index.html"),
    ("Contact Us", "contact-us/index.html"),
    ("Blogs", "blogs/index.html"),
]

for name, rel in pages_to_check:
    p = os.path.join(ROOT, rel)
    if not os.path.exists(p):
        print(f"[{name}] NOT FOUND: {rel}")
        continue
    with open(p, "r", encoding="utf-8", errors="ignore") as f:
        txt = f.read()
    
    # Find eyebrow and h1
    h1 = re.search(r'<h1[^>]*>.*?</h1>', txt, re.S | re.I)
    eyebrow = re.search(r'<(?:div|span|p)[^>]*class=["\'][^"\']*(?:eyebrow|badge)[^"\']*["\'][^>]*>(.*?)</(?:div|span|p)>', txt, re.S | re.I)
    
    print(f"[{name}] ({rel}):")
    if eyebrow:
        # strip inner tags
        eb_clean = re.sub(r'<[^>]+>', ' ', eyebrow.group(1)).strip()
        print(f"  Eyebrow: {eb_clean}")
    else:
        print("  Eyebrow: NONE")
    if h1:
        h1_clean = re.sub(r'\s+', ' ', h1.group(0).strip())
        print(f"  H1: {h1_clean[:120]}")
    else:
        print("  H1: NONE")
    print()

