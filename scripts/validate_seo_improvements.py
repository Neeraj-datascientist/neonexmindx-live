import os
import re
import openpyxl

ROOT = r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex"
EXCEL_PATH = r"C:\Users\pcnee\Downloads\neonexmindx-h1-update (2).xlsx"

wb = openpyxl.load_workbook(EXCEL_PATH)
sheet = wb.active

excel_items = []
for r in range(2, sheet.max_row + 1):
    vals = [sheet.cell(r, c).value for c in range(1, 6)]
    if any(vals):
        excel_items.append({
            "page": vals[0],
            "url": vals[1],
            "current_eyebrow": vals[2],
            "current_h1": vals[3],
            "suggested_h1": vals[4]
        })

print("=" * 75)
print("SEO VALIDATION AUDIT: EXCEL MAPPING vs PRODUCTION CODE")
print("=" * 75)

mapping = {
    "Home": "index.html",
    "Data Analytics": "courses/data-analytics-course/index.html",
    "Data Science": "courses/data-science-course/index.html",
    "AI & ML": "courses/ai-ml-engineering-course/index.html",
    "Data Engineering": "courses/data-engineering-course/index.html",
    "Business Analytics": "courses/business-analytics-course/index.html",
    "Generative AI": "courses/generative-ai-engineering-course/index.html",
    "About Us": "about-us/index.html",
    "Trainers": "trainers/index.html",
    "Contact Us": "contact-us/index.html",
    "Blogs": "blogs/index.html"
}

results = []

for item in excel_items:
    page_name = item["page"]
    if page_name not in mapping:
        print(f"[NOTE] '{page_name}' not a primary standalone page (301 redirect or module).")
        continue
    rel = mapping[page_name]
    full = os.path.join(ROOT, rel)
    
    with open(full, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()
        
    h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.S | re.I)
    h1_text = re.sub(r'<[^>]+>', ' ', h1s[0]).strip() if h1s else "NONE"
    # clean entities
    h1_text = h1_text.replace("&amp;", "&").replace("&mdash;", "—").replace("&nbsp;", " ")
    
    # Check if primary keywords from suggested_h1 are contained
    suggested = item["suggested_h1"]
    keywords = [k.strip().lower() for k in re.split(r'[,|—\s]+', suggested) if len(k.strip()) > 2 and k.strip().lower() not in ["for", "and", "the", "in"]]
    
    matches = [k for k in keywords if k in h1_text.lower()]
    match_pct = (len(matches) / len(keywords)) * 100 if keywords else 100
    
    # Check title tag
    title_match = re.search(r'<title>(.*?)</title>', html, re.S | re.I)
    title_text = title_match.group(1).strip() if title_match else "NONE"
    
    # Check meta description
    desc_match = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']*)["\']', html, re.I)
    if not desc_match:
        desc_match = re.search(r'<meta[^>]+content=["\']([^"\']*)["\'][^>]+name=["\']description["\']', html, re.I)
    desc_text = desc_match.group(1).strip() if desc_match else "NONE"
    
    results.append({
        "page": page_name,
        "file": rel,
        "h1_count": len(h1s),
        "h1_text": h1_text,
        "suggested_h1": suggested,
        "keyword_coverage": f"{len(matches)}/{len(keywords)} ({match_pct:.0f}%)",
        "title": title_text[:70],
        "desc_length": len(desc_text)
    })

print(f"{'Page':<20} | {'H1 Count':<8} | {'Keyword Match':<14} | {'H1 Content'}")
print("-" * 75)
for r in results:
    status = "PASS" if r["h1_count"] == 1 else "FAIL"
    print(f"{r['page']:<20} | {r['h1_count']:<8} | {r['keyword_coverage']:<14} | {r['h1_text'][:50]}...")

print("\n" + "=" * 75)
print("DETAILED PAGE-BY-PAGE AUDIT REPORT")
print("=" * 75)
for r in results:
    print(f"\nPage: {r['page']} ({r['file']})")
    print(f"  Target from Excel : {r['suggested_h1']}")
    print(f"  Production H1     : {r['h1_text']}")
    print(f"  Keyword Coverage  : {r['keyword_coverage']}")
    print(f"  Title Tag         : {r['title']}")
    print(f"  Meta Description  : {r['desc_length']} characters")
