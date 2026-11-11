import os
import glob
import re
import xml.etree.ElementTree as ET
import urllib.request
import json

ROOT = r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex"
print("=" * 70)
print("COMPREHENSIVE MULTI-PAGE INCONSISTENCY & SEO/GEO AUDIT")
print("=" * 70)

# 1. Parse sitemap
sitemap_path = os.path.join(ROOT, "sitemap.xml")
with open(sitemap_path, "r", encoding="utf-8") as f:
    xml_tree = ET.fromstring(f.read())
urls = [e.text for e in xml_tree.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]

print(f"Total Sitemap URLs: {len(urls)}")

inconsistencies = []

for u in urls:
    suffix = u.replace("https://neonexmindx.com", "").strip("/")
    candidates = []
    if not suffix:
        candidates = [os.path.join(ROOT, "index.html")]
    else:
        candidates = [
            os.path.join(ROOT, suffix, "index.html"),
            os.path.join(ROOT, suffix + ".html"),
            os.path.join(ROOT, suffix.replace("/", os.sep), "index.html")
        ]
    found = None
    for c in candidates:
        if os.path.exists(c):
            found = c
            break
            
    if not found:
        inconsistencies.append(("SITEMAP_DEAD_LINK", u, f"No matching HTML file on disk"))
        continue
        
    with open(found, "r", encoding="utf-8", errors="ignore") as fp:
        html = fp.read()
        
    # Check 1: Canonical
    can_matches = re.findall(r'<link[^>]+canonical[^>]*>', html, re.I)
    if len(can_matches) != 1:
        inconsistencies.append(("CANONICAL_COUNT", u, f"Found {len(can_matches)} canonical tags"))
    else:
        # Check canonical href vs sitemap
        m = re.search(r'href=["\']([^"\']+)["\']', can_matches[0])
        href = m.group(1) if m else ""
        if href != u and href.rstrip("/") != u.rstrip("/"):
            inconsistencies.append(("CANONICAL_MISMATCH", u, f"Canonical '{href}' does not match URL '{u}'"))
            
    # Check 2: Title
    titles = re.findall(r'<title[^>]*>(.*?)</title>', html, re.I | re.S)
    if len(titles) != 1:
        inconsistencies.append(("TITLE_COUNT", u, f"Found {len(titles)} title tags"))
    elif len(titles[0].strip()) < 10 or len(titles[0].strip()) > 80:
        inconsistencies.append(("TITLE_LENGTH", u, f"Title length {len(titles[0].strip())} chars: '{titles[0].strip()}'"))
        
    # Check 3: Meta description
    descs = re.findall(r'<meta[^>]+name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', html, re.I)
    if not descs:
        descs = re.findall(r'<meta[^>]+content=["\']([^"\']*)["\'][^>]+name=["\']description["\']', html, re.I)
    if len(descs) != 1:
        inconsistencies.append(("DESCRIPTION_COUNT", u, f"Found {len(descs)} meta descriptions"))
    else:
        desc_len = len(descs[0].strip())
        if desc_len < 50 or desc_len > 170:
            inconsistencies.append(("DESCRIPTION_LENGTH", u, f"Description length {desc_len} chars (Recommended: 70-160)"))
            
    # Check 4: H1 count
    h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.I | re.S)
    if len(h1s) != 1:
        inconsistencies.append(("H1_COUNT", u, f"Found {len(h1s)} H1 tags: {h1s}"))
        
    # Check 5: Images missing alt
    imgs = re.findall(r'<img[^>]*>', html, re.I)
    for img in imgs:
        if 'alt=' not in img.lower():
            inconsistencies.append(("IMG_MISSING_ALT", u, f"Missing alt attribute: {img[:60]}"))
        else:
            alt_match = re.search(r'alt=["\']([^"\']*)["\']', img, re.I)
            if alt_match and alt_match.group(1).strip() == "" and "presentation" not in img.lower():
                inconsistencies.append(("IMG_EMPTY_ALT", u, f"Empty alt attribute: {img[:60]}"))

print(f"\nAudit completed. Total inconsistencies detected across {len(urls)} production pages: {len(inconsistencies)}")
for typ, url, msg in inconsistencies:
    print(f"[{typ}] {url} -> {msg}")

