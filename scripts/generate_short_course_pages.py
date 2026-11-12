import os
import re

ROOT = r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex"
CLEANED_SRC = r"c:\Users\pcnee\Desktop\NeoNeX MindX website\Cleaned HTML"

# The short courses:
# (cleaned_html_name, target_folder, canonical_url, eyebrow_h1, hero_title, title_tag, meta_desc)
COURSES = [
    {
        "src_file": "Neonex Mindx Python Programming Course.html",
        "folder": "courses/python-programming-course",
        "canonical": "https://neonexmindx.com/courses/python-programming-course/",
        "eyebrow_h1": "Live Online Python Course for Beginners in India",
        "hero_title": 'Stop Saving Python Tutorials. <span>Start Writing Python.</span>',
        "title": "Python Programming Course Online in India for Beginners | NeoNex MindX",
        "desc": "Master Python programming online with live mentor support, practical coding exercises, data automation workflows and real-world project portfolios."
    },
    {
        "src_file": "Neonex Mindx Excel PowerBI Tableau Course.html",
        "folder": "courses/excel-power-bi-tableau-course",
        "canonical": "https://neonexmindx.com/courses/excel-power-bi-tableau-course/",
        "eyebrow_h1": "Excel, Power BI &amp; Tableau Course Online in India",
        "hero_title": 'Your Dashboard Should Answer a Business Question, <span>Not Just Look Good.</span>',
        "title": "Excel Power BI Tableau Course Online India | NeoNex MindX",
        "desc": "Master Microsoft Excel, Power BI and Tableau with real business dashboards, DAX calculations, visual analytics and executive reporting projects."
    },
    {
        "src_file": "Neonex Mindx SQL Course.html",
        "folder": "courses/sql-course",
        "canonical": "https://neonexmindx.com/courses/sql-course/",
        "eyebrow_h1": "Live Online SQL Course in India with Real Database Projects",
        "hero_title": 'Stop Guessing What the Data Says. <span>Query It.</span>',
        "title": "SQL Course Online in India with Projects | NeoNex MindX",
        "desc": "Learn SQL for Data Analytics and Engineering with live queries, complex joins, window functions, database schema design and practical case studies."
    },
    {
        "src_file": "Neonex Mindx Machine Learning Course.html",
        "folder": "courses/machine-learning-course",
        "canonical": "https://neonexmindx.com/courses/machine-learning-course/",
        "eyebrow_h1": "Machine Learning Course Online in India with Python",
        "hero_title": 'Do Not Just Train a Model. <span>Learn When to Trust It.</span>',
        "title": "Machine Learning Course Online India | NeoNex MindX",
        "desc": "Build and deploy production-ready machine learning models in Python covering supervised learning, regression, classification, pipelines and MLOps."
    }
]

SHARED_HERO_CSS = """
<style id="h1-seo-styling">
h1.eyebrow {
  font-family: var(--font-display, inherit);
  display: inline-flex;
  align-items: center;
  gap: 8px;
  margin: 0 0 18px 0;
  color: var(--blue-dark, #0c337c);
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .105em;
  text-transform: uppercase;
  line-height: 1.3;
}
@media (max-width: 768px) {
  h1.eyebrow { font-size: 11px; letter-spacing: .11em; margin-bottom: 15px; }
}
.hero-title {
  font-family: var(--font-display, inherit);
  font-size: clamp(42px, 5.8vw, 74px);
  font-weight: 800;
  line-height: 1.035;
  letter-spacing: -.044em;
  margin-top: 0;
  margin-bottom: 22px;
  text-wrap: balance;
  color: #111827;
}
.hero-title span {
  color: var(--blue, #1B5DB7);
}
@media (max-width: 768px) {
  .hero-title {
    font-size: clamp(34px, 9.5vw, 38px);
    line-height: 1.12;
    letter-spacing: -.032em;
    margin-bottom: 18px;
  }
}
</style>
"""

for c in COURSES:
    src_path = os.path.join(CLEANED_SRC, c["src_file"])
    with open(src_path, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()

    # 1. Update title tag
    html = re.sub(r'<title>.*?</title>', f'<title>{c["title"]}</title>', html, flags=re.S | re.I)
    
    # 2. Update meta description
    html = re.sub(r'<meta[^>]+name=["\']description["\'][^>]*content=["\'][^"\']*["\']', f'<meta name="description" content="{c["desc"]}"', html, flags=re.I)
    
    # 3. Update canonical
    can_tag = f'<link rel="canonical" href="{c["canonical"]}" />'
    if re.search(r'<link[^>]+canonical[^>]*>', html, re.I):
        html = re.sub(r'<link[^>]+canonical[^>]*>', can_tag, html, flags=re.I)
    else:
        html = html.replace('</head>', f'  {can_tag}\n</head>')

    # 4. Convert eyebrow to <h1 class="eyebrow">
    # Look for existing eyebrow div or span
    if re.search(r'<div class=["\']eyebrow["\']>.*?</div>', html, re.S | re.I):
        html = re.sub(r'<div class=["\']eyebrow["\']>.*?</div>', f'<h1 class="eyebrow">{c["eyebrow_h1"]}</h1>', html, count=1, flags=re.S | re.I)
    else:
        # Prepend to hero
        html = re.sub(r'(<div class=["\']hero-copy["\']>)', f'\\1\n            <h1 class="eyebrow">{c["eyebrow_h1"]}</h1>', html, count=1, flags=re.I)
        
    # 5. Convert original H1 to <div class="hero-title">
    html = re.sub(r'<h1[^>]*>(.*?)</h1>', f'<div class="hero-title">{c["hero_title"]}</div>', html, count=1, flags=re.S | re.I)
    
    # 6. Add SHARED_HERO_CSS if missing
    if 'id="h1-seo-styling"' not in html:
        html = html.replace('</head>', f'{SHARED_HERO_CSS}\n</head>')

    # 7. Add Facebook pixel alt text if needed
    html = html.replace('alt="" src="https://www.facebook.com/tr?id=1698036971288322', 'alt="Facebook Pixel" src="https://www.facebook.com/tr?id=1698036971288322')

    # Save to deployment_NeoNex/courses/<course-name>/index.html
    out_dir = os.path.join(ROOT, c["folder"])
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "index.html")
    with open(out_file, "w", encoding="utf-8") as out_fp:
        out_fp.write(html)
        
    # Also save to root fallback file e.g. deployment_NeoNex/<src_file>
    root_file = os.path.join(ROOT, c["src_file"])
    with open(root_file, "w", encoding="utf-8") as out_fp2:
        out_fp2.write(html)
        
    print(f"Generated standalone page for {c['folder']} -> {out_file}")

print("All 4 short course standalone pages generated successfully.")

