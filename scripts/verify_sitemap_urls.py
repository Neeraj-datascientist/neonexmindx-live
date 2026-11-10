import xml.etree.ElementTree as ET
import urllib.request
import re
import os

with open(r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex\sitemap.xml", "r", encoding="utf-8") as f:
    xml_content = f.read()

root = ET.fromstring(xml_content)
urls = [elem.text for elem in root.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]

print(f"Total sitemap URLs to verify: {len(urls)}")

root_dir = r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex"

for u in urls:
    # Determine corresponding local HTML file
    path_suffix = u.replace("https://neonexmindx.com", "").strip("/")
    candidates = []
    if not path_suffix:
        candidates = [os.path.join(root_dir, "index.html")]
    else:
        candidates = [
            os.path.join(root_dir, path_suffix, "index.html"),
            os.path.join(root_dir, path_suffix + ".html"),
            os.path.join(root_dir, path_suffix.replace("/", "\\"), "index.html"),
            os.path.join(root_dir, path_suffix.replace("/", "\\") + ".html")
        ]
    found = None
    for c in candidates:
        if os.path.exists(c):
            found = c
            break
            
    if not found:
        print(f"MISSING LOCAL FILE: {u}")
        continue
        
    with open(found, "r", encoding="utf-8", errors="ignore") as fp:
        html = fp.read()
        
    # Check meta robots
    robots = re.search(r'<meta[^>]+name=["\']robots["\'][^>]*content=["\']([^"\']+)["\']', html, re.I)
    robots_val = robots.group(1) if robots else "default (index, follow)"
    
    # Check canonical
    can = re.search(r'<link[^>]+(?:href=["\']([^"\']+)["\'][^>]*rel=["\']canonical["\']|rel=["\']canonical["\'][^>]*href=["\']([^"\']+)["\'])', html, re.I)
    can_val = can.group(1) or can.group(2) if can else "MISSING"
    
    # Check word count / content depth
    text_content = re.sub(r'<[^>]+>', ' ', html)
    words = len(text_content.split())
    
    status = "OK"
    if "noindex" in robots_val.lower():
        status = "CRITICAL: NOINDEX"
    elif can_val == "MISSING":
        status = "WARN: NO CANONICAL"
    elif words < 150:
        status = "WARN: THIN CONTENT"
        
    print(f"[{status}] {u} -> Words: {words} | Canonical: {can_val} | Robots: {robots_val}")

