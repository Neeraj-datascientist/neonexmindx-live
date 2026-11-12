import os
import glob
import re

html_files = glob.glob('deployment_NeoNex/**/*.html', recursive=True)
print(f"Total HTML files: {len(html_files)}")

# Check blog posts
blog_files = [f for f in html_files if 'blog' in f and 'index.html' in f]
print("Blog files:", blog_files)

for b in blog_files:
    txt = open(b, 'r', encoding='utf-8').read()
    # Check whatsapp
    has_wa = 'whatsapp' in txt.lower() or 'wa.me' in txt.lower()
    # Check linkedin
    has_li = 'linkedin' in txt.lower()
    # Check share tray
    tray = re.search(r'class=[\"\'][^\"\']*share[^\"]*[\"\'].*?</div>', txt, re.DOTALL | re.IGNORECASE)
    print(f"\n{b}:")
    print(f"  has_wa: {has_wa}, has_li: {has_li}")
    if tray:
        print("  Tray snippet:", tray.group(0)[:200])
    else:
        print("  NO share tray match")

