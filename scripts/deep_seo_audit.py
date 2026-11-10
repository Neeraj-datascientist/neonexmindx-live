import os
import glob
import re
import json
from urllib.parse import urlparse

ROOT_DIR = r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex"

print("=" * 60)
print("COMPREHENSIVE CRAWL & INDEXABILITY AUDIT")
print("=" * 60)

# 1. Load Sitemap URLs
sitemap_path = os.path.join(ROOT_DIR, "sitemap.xml")
with open(sitemap_path, "r", encoding="utf-8") as f:
    sitemap_xml = f.read()

sitemap_urls = set(re.findall(r'<loc>(.*?)</loc>', sitemap_xml))
print(f"Total Sitemap URLs: {len(sitemap_urls)}")

# 2. Gather all HTML files
html_files = glob.glob(os.path.join(ROOT_DIR, "**", "*.html"), recursive=True)
print(f"Total HTML files found: {len(html_files)}")

issues = []

for f in html_files:
    rel = os.path.relpath(f, ROOT_DIR)
    if any(p in rel.lower() for p in [".git", "node_modules", "savepoints", "cms"]):
        continue
        
    with open(f, "r", encoding="utf-8", errors="ignore") as fp:
        html = fp.read()
        
    # Check A: Duplicate Title tags
    titles = re.findall(r'<title>(.*?)</title>', html, re.I | re.S)
    if not titles:
        issues.append(("CRITICAL", rel, "Missing <title> tag"))
    elif len(titles) > 1:
        issues.append(("WARNING", rel, f"Multiple <title> tags ({len(titles)})"))
        
    # Check B: Duplicate or mismatched Canonicals
    canonicals = re.findall(r'<link[^>]+(?:rel=["\']canonical["\'][^>]+href=["\']([^"\']+)["\']|href=["\']([^"\']+)["\'][^>]+rel=["\']canonical["\'])', html, re.I)
    can_urls = [c[0] if c[0] else c[1] for c in canonicals]
    if len(can_urls) > 1:
        issues.append(("WARNING", rel, f"Multiple canonical tags found ({len(can_urls)}): {can_urls}"))
        
    # Check C: Duplicate meta descriptions
    descriptions = re.findall(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']*)["\']', html, re.I)
    if not descriptions:
        # Check reverse attribute order
        descriptions = re.findall(r'<meta[^>]+content=["\']([^"\']*)["\'][^>]+name=["\']description["\']', html, re.I)
    if not descriptions:
        if not any(k in rel.lower() for k in ["404", "thank-you", "crm", "sms"]):
            issues.append(("WARNING", rel, "Missing meta description"))
    elif len(descriptions) > 1:
        issues.append(("WARNING", rel, f"Multiple meta descriptions found ({len(descriptions)})"))
        
    # Check D: Trailing slash consistency between Canonical and Sitemap
    for c_url in can_urls:
        # Clean URL
        parsed = urlparse(c_url)
        clean_can = parsed.scheme + "://" + parsed.netloc + parsed.path.rstrip("/")
        # Check against sitemap
        matching_sitemap = [s for s in sitemap_urls if s.rstrip("/") == clean_can]
        if matching_sitemap:
            s_url = matching_sitemap[0]
            if s_url != c_url and (s_url.endswith("/") != c_url.endswith("/")):
                issues.append(("SEO_MISMATCH", rel, f"Canonical trailing-slash mismatch with sitemap: canonical has '{c_url}' vs sitemap '{s_url}'"))

    # Check E: Broken Internal Links
    hrefs = re.findall(r'href=["\']([^"\'#][^"\']*)["\']', html, re.I)
    for h in hrefs:
        if h.startswith("http://") or h.startswith("https://") or h.startswith("mailto:") or h.startswith("tel:") or h.startswith("javascript:"):
            continue
        # internal relative or absolute link
        clean_h = h.split("?")[0].split("#")[0]
        if not clean_h:
            continue
        if clean_h.startswith("/"):
            target_path = os.path.join(ROOT_DIR, clean_h.lstrip("/").replace("/", os.sep))
        else:
            target_path = os.path.join(os.path.dirname(f), clean_h.replace("/", os.sep))
            
        target_candidates = [
            target_path,
            target_path + ".html",
            os.path.join(target_path, "index.html")
        ]
        if not any(os.path.exists(tc) for tc in target_candidates):
            # check if it is a known redirect route in _redirects
            issues.append(("POTENTIAL_404_LINK", rel, f"Internal link target not found on disk: '{h}'"))

# 3. Check JSON-LD Schema syntax
for f in html_files:
    rel = os.path.relpath(f, ROOT_DIR)
    if any(p in rel.lower() for p in [".git", "node_modules", "savepoints", "cms"]):
        continue
    with open(f, "r", encoding="utf-8", errors="ignore") as fp:
        html = fp.read()
    schemas = re.findall(r'<script\s+type=["\']application/ld\+json["\']>(.*?)</script>', html, re.I | re.S)
    for idx, s in enumerate(schemas):
        try:
            json.loads(s.strip())
        except Exception as e:
            issues.append(("SCHEMA_SYNTAX_ERROR", rel, f"JSON-LD block {idx+1} invalid: {e}"))

print(f"\nAudit complete. Found {len(issues)} potential items.")
# Group and print by type
by_type = {}
for level, file, msg in issues:
    by_type.setdefault(level, []).append((file, msg))

for level, items in by_type.items():
    print(f"\n--- [{level}] ({len(items)} items) ---")
    for file, msg in items[:15]:
        print(f"  [{file}]: {msg}")
    if len(items) > 15:
        print(f"  ... and {len(items) - 15} more.")
