import os
import re

ROOT = r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex"

# Mapping: relative path -> (current_eyebrow, new_h1_text)
# We will transform:
# <div class="eyebrow">OLD_TEXT</div>
# into:
# <h1 class="eyebrow">NEW_H1_TEXT</h1>
# and transform:
# <h1>ORIGINAL_TITLE</h1>
# into:
# <div class="hero-title">ORIGINAL_TITLE</div>

updates = [
    # 1. Home
    ("index.html", 
     "Live Online Data, Analytics &amp; AI Career Programs", 
     "Live Online Data, Analytics &amp; AI Career Programs"),
    ("Neonex Mindx Home Page.html", 
     "Live Online Data, Analytics &amp; AI Career Programs", 
     "Live Online Data, Analytics &amp; AI Career Programs"),
     
    # 2. Data Analytics
    ("courses/data-analytics-course/index.html", 
     "Live Online Data Analytics Course in India", 
     "Live Online Data Analytics Course in India"),
    ("Neonex Mindx Data Analytics Course.html", 
     "Live Online Data Analytics Course in India", 
     "Live Online Data Analytics Course in India"),
     
    # 3. Data Science
    ("courses/data-science-course/index.html", 
     "Live Online Data Science Course in India", 
     "Live Online Data Science Course in India"),
    ("Neonex Mindx Data Science Course.html", 
     "Live Online Data Science Course in India", 
     "Live Online Data Science Course in India"),
     
    # 4. AI & ML
    ("courses/ai-ml-engineering-course/index.html", 
     "Live Online AI and Machine Learning Course in India", 
     "Live Online AI and Machine Learning Course in India"),
    ("ai-ml-course/index.html", 
     "Live Online AI and Machine Learning Course in India", 
     "Live Online AI and Machine Learning Course in India"),
    ("Neonex Mindx AI ML Course.html", 
     "Live Online AI and Machine Learning Course in India", 
     "Live Online AI and Machine Learning Course in India"),
     
    # 5. Data Engineering
    ("courses/data-engineering-course/index.html", 
     "Live Online Data Engineering Course in India", 
     "Live Online Data Engineering Course in India"),
    ("data-engineering-course/index.html", 
     "Live Online Data Engineering Course in India", 
     "Live Online Data Engineering Course in India"),
    ("Neonex Mindx Data Engineering Course.html", 
     "Live Online Data Engineering Course in India", 
     "Live Online Data Engineering Course in India"),
     
    # 6. Business Analytics
    ("courses/business-analytics-course/index.html", 
     "Live Online Business Analytics Course in India", 
     "Live Online Business Analytics Course in India"),
    ("business-analytics-course/index.html", 
     "Live Online Business Analytics Course in India", 
     "Live Online Business Analytics Course in India"),
    ("Neonex Mindx Business Analytics Course.html", 
     "Live Online Business Analytics Course in India", 
     "Live Online Business Analytics Course in India"),
     
    # 7. Generative AI
    ("courses/generative-ai-engineering-course/index.html", 
     "Live Online AI and Machine Learning Course in India", 
     "Live Online Generative AI Engineering Course in India"),
    ("generative-ai-engineering-course/index.html", 
     "Live Online AI and Machine Learning Course in India", 
     "Live Online Generative AI Engineering Course in India"),
     
    # 8. About Us
    ("about-us/index.html", 
     "About NeoNex MindX", 
     "About NeoNex MindX"),
    ("Neonex Mindx About us page.html", 
     "About NeoNex MindX", 
     "About NeoNex MindX"),
     
    # 9. Trainers
    ("trainers/index.html", 
     "Know Who Will Teach You Before You Enrol", 
     "Data, Analytics &amp; AI Trainers &mdash; Know Who Will Teach You Before You Enrol"),
    ("Neonex Mindx Trainers Page.html", 
     "Know Who Will Teach You Before You Enrol", 
     "Data, Analytics &amp; AI Trainers &mdash; Know Who Will Teach You Before You Enrol"),
     
    # 10. Contact Us
    ("contact-us/index.html", 
     "Need Clarity Before You Choose a Course?", 
     "Contact NeoNex MindX &mdash; Need Clarity Before You Choose a Course?"),
    ("Neonex Mindx Contact Us.html", 
     "Need Clarity Before You Choose a Course?", 
     "Contact NeoNex MindX &mdash; Need Clarity Before You Choose a Course?"),
     
    # 11. Blogs
    ("blogs/index.html", 
     "NeoNeX Knowledge Hub", 
     "Data Analytics, Data Science &amp; AI Blog &mdash; Knowledge Hub"),
    ("blogs.html", 
     "NeoNeX Knowledge Hub", 
     "Data Analytics, Data Science &amp; AI Blog &mdash; Knowledge Hub"),
]

print(f"Total files to safely transform: {len(updates)}")
for rel, old_eb, new_h1 in updates:
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        print(f"NOT FOUND: {rel}")
    else:
        print(f"READY: {rel}")
