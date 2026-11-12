import re

with open(r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex\courses\data-analytics-course\index.html", "r", encoding="utf-8") as f:
    txt = f.read()

# Look for GTM
gtm = re.findall(r'GTM-PG57R85H', txt)
canonical = re.findall(r'<link[^>]+canonical[^>]*>', txt)
h1_seo = re.findall(r'id="h1-seo-styling"', txt)
h1 = re.findall(r'<h1[^>]*>.*?</h1>', txt, re.S)
hero_title = re.findall(r'<div class="hero-title">.*?</div>', txt, re.S)

print("Template Analysis of data-analytics-course:")
print(f"  GTM tags: {len(gtm)}")
print(f"  Canonical: {canonical}")
print(f"  H1 SEO style block present: {len(h1_seo) > 0}")
print(f"  H1: {h1}")
print(f"  Hero Title: {hero_title}")

