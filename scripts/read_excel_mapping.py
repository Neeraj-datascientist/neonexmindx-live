import openpyxl
import re
import os

wb = openpyxl.load_workbook(r'C:\Users\pcnee\Downloads\neonexmindx-h1-update (2).xlsx')
sheet = wb.active

rows = []
for r in range(2, sheet.max_row + 1):
    vals = [sheet.cell(r, c).value for c in range(1, sheet.max_column + 1)]
    if any(vals):
        rows.append({
            "page": vals[0],
            "url": vals[1],
            "eyebrow": vals[2],
            "current_h1": vals[3],
            "suggested_h1": vals[4]
        })

print(f"Loaded {len(rows)} rows from Excel:")
for item in rows:
    print(f"Page: {item['page']}")
    print(f"  URL: {item['url']}")
    print(f"  Eyebrow: {item['eyebrow']}")
    print(f"  Current H1: {item['current_h1']}")
    print(f"  Suggested H1: {item['suggested_h1']}")
    print()

