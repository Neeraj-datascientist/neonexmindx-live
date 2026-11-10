import os
import glob
import re

ROOT = r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex"
html_files = glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True)

h1_audit = []
for f in html_files:
    rel = os.path.relpath(f, ROOT)
    if any(k in rel.lower() for k in [".git", "savepoints", "cms", "admin", "node_modules"]):
        continue
    with open(f, "r", encoding="utf-8", errors="ignore") as fp:
        html = fp.read()
    h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.S | re.I)
    h1_count = len(h1s)
    h1_texts = [re.sub(r'<[^>]+>', ' ', h).strip() for h in h1s]
    h1_audit.append((rel, h1_count, h1_texts))

print("=" * 60)
print(f"H1 AUDIT ACROSS ALL {len(h1_audit)} PRODUCTION PAGES")
print("=" * 60)

single_h1 = 0
multi_h1 = 0
zero_h1 = 0

for rel, count, texts in h1_audit:
    if count == 1:
        single_h1 += 1
        print(f"[OK] {rel} -> H1: {texts[0][:80]}")
    elif count > 1:
        multi_h1 += 1
        print(f"[WARN: MULTIPLE H1 ({count})] {rel} -> {texts}")
    else:
        zero_h1 += 1
        print(f"[WARN: ZERO H1] {rel}")

print(f"\nSummary: Single H1: {single_h1} | Multiple H1: {multi_h1} | Zero H1: {zero_h1}")

