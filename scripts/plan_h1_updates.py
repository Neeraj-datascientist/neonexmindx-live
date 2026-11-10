import openpyxl
import os
import re

ROOT = r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex"
EXCEL_PATH = r"C:\Users\pcnee\Downloads\neonexmindx-h1-update (2).xlsx"

wb = openpyxl.load_workbook(EXCEL_PATH)
sheet = wb.active

plan = []
for r in range(2, sheet.max_row + 1):
    vals = [sheet.cell(r, c).value for c in range(1, 6)]
    if any(vals):
        plan.append({
            "page": vals[0],
            "url": vals[1],
            "current_eyebrow": vals[2],
            "current_h1": vals[3],
            "suggested_h1": vals[4]
        })

print("=" * 70)
print(f"H1 UPDATE EXECUTION PLAN ({len(plan)} targets)")
print("=" * 70)

# Map page names to corresponding local files
file_mapping = {
    "Home": ["index.html", "Neonex Mindx Home Page.html"],
    "Data Analytics": ["courses/data-analytics-course/index.html", "Neonex Mindx Data Analytics Course.html"],
    "Data Science": ["courses/data-science-course/index.html", "Neonex Mindx Data Science Course.html"],
    "AI & ML": ["courses/ai-ml-engineering-course/index.html", "ai-ml-course/index.html", "Neonex Mindx AI ML Course.html"],
    "Data Engineering": ["courses/data-engineering-course/index.html", "data-engineering-course/index.html", "Neonex Mindx Data Engineering Course.html"],
    "Business Analytics": ["courses/business-analytics-course/index.html", "business-analytics-course/index.html", "Neonex Mindx Business Analytics Course.html"],
    "Generative AI": ["courses/generative-ai-engineering-course/index.html", "generative-ai-engineering-course/index.html"],
    "About Us": ["about-us/index.html", "Neonex Mindx About us page.html"],
    "Trainers": ["trainers/index.html", "Neonex Mindx Trainers Page.html"],
    "Contact Us": ["contact-us/index.html", "Neonex Mindx Contact Us.html"],
    "Blogs": ["blogs/index.html", "blogs.html"]
}

for item in plan:
    name = item["page"]
    files = file_mapping.get(name, [])
    print(f"\nTarget: {name}")
    print(f"  Suggested H1: '{item['suggested_h1']}'")
    print(f"  Files: {files}")
    for rel in files:
        full = os.path.join(ROOT, rel)
        if os.path.exists(full):
            print(f"    [FOUND] {rel}")
        else:
            print(f"    [MISSING] {rel}")
