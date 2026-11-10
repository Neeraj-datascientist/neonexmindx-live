import glob
import os
import re

root_dir = r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex"
files = glob.glob(os.path.join(root_dir, "**", "*.html"), recursive=True)
print(f"Total HTML files scanned: {len(files)}")

issues = []
for f in files:
    rel = os.path.relpath(f, root_dir)
    if any(k in rel.lower() for k in ["node_modules", ".git", "cms", "admin"]):
        continue
    with open(f, "r", encoding="utf-8", errors="ignore") as fp:
        text = fp.read()
    
    # 1. Noindex check
    if re.search(r'content=["\'][^"\']*noindex[^"\']*["\']', text, re.I):
        if "404" not in rel.lower():
            issues.append(f"UNINTENDED NOINDEX: {rel}")
            
    # 2. Canonical check
    can = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\']([^"\']+)["\']', text, re.I)
    if not can and "404" not in rel.lower():
        issues.append(f"MISSING CANONICAL: {rel}")
        
    # 3. Title check
    title = re.search(r'<title>([^<]+)</title>', text, re.I)
    if not title:
        issues.append(f"MISSING TITLE: {rel}")

print(f"Total indexing issues detected: {len(issues)}")
for i in issues:
    print(f"  - {i}")

