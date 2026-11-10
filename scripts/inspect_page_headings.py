import os
import re

ROOT = r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex"

def inspect_page(rel_path):
    path = os.path.join(ROOT, rel_path)
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()
    print(f"=== {rel_path} ===")
    
    # Find H1
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.S | re.I)
    if h1_match:
        print("  H1:", repr(h1_match.group(0).strip()[:150]))
    else:
        print("  H1: NONE")
        
    # Find eyebrow / badge preceding H1
    # look at 400 chars before H1
    if h1_match:
        idx = h1_match.start()
        context_before = html[max(0, idx-400):idx]
        print("  Context before H1:\n", "    " + "\n    ".join(context_before.strip().splitlines()[-6:]))

inspect_page("index.html")
inspect_page("courses/data-analytics-course/index.html")
inspect_page("courses/data-science-course/index.html")
inspect_page("courses/ai-ml-engineering-course/index.html")
inspect_page("courses/data-engineering-course/index.html")
inspect_page("courses/business-analytics-course/index.html")
inspect_page("courses/generative-ai-engineering-course/index.html")
inspect_page("about-us/index.html")
inspect_page("trainers/index.html")
inspect_page("contact-us/index.html")
inspect_page("blogs/index.html")

