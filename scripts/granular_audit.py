import re
import glob

short_courses = [
    'deployment_NeoNex/courses/python-programming-course/index.html',
    'deployment_NeoNex/courses/sql-course/index.html',
    'deployment_NeoNex/courses/excel-power-bi-tableau-course/index.html',
    'deployment_NeoNex/courses/machine-learning-course/index.html'
]

print("=== GRANULAR AUDIT OF SHORT COURSE PAGES ===")

for path in short_courses:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    print(f"\n--- Checking {path} ---")
    
    # 1. Check title, meta description, canonical
    title = re.search(r'<title>(.*?)</title>', html)
    desc = re.search(r'<meta content="(.*?)" name="description"', html)
    canon = re.search(r'<link rel="canonical" href="(.*?)"', html) or re.search(r'<link href="(.*?)" rel="canonical"', html)
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL)
    
    print("Title:", title.group(1) if title else "MISSING")
    print("Meta Description:", desc.group(1)[:70] + "..." if desc else "MISSING")
    print("Canonical:", canon.group(1) if canon else "MISSING")
    print("H1 tag:", " ".join(re.sub(r'<[^>]+>', ' ', h1.group(1)).split()) if h1 else "MISSING")
    
    # 2. Check for broken internal links
    links = re.findall(r'href=["\']([^"\']+)["\']', html)
    bad_links = [l for l in links if l.startswith('/courses/') and not l.endswith('/') and not '.' in l]
    print("Non-trailing slash course links:", set(bad_links) if bad_links else "None (All Clean)")
    
    # 3. Check for leftover placeholder texts
    placeholders = ['Lorem ipsum', 'TODO', 'FIXME', 'undefined', 'null', 'test.com', 'example.com']
    found_placeholders = [p for p in placeholders if p.lower() in html.lower()]
    print("Found placeholders:", found_placeholders if found_placeholders else "None")
    
    # 4. Check for broken image alts or missing images
    imgs = re.findall(r'<img[^>]*>', html)
    missing_alt = [img for img in imgs if 'alt=""' in img or 'alt' not in img]
    print(f"Total images: {len(imgs)}, Empty/Missing alts: {len(missing_alt)}")
    if missing_alt:
        for m in missing_alt[:3]:
            print("  -", m[:100])
            
    # 5. Check curriculum module count consistency with eyebrow
    eyebrow = re.search(r'<p class="eyebrow">\s*(\d+)-module.*?</p>', html, re.IGNORECASE) or re.search(r'(\d+)\s+comprehensive modules', html, re.IGNORECASE)
    modules_in_grid = len(re.findall(r'<details class="module-card"', html))
    print(f"Eyebrow module count claim vs Actual modules: claimed {eyebrow.group(1) if eyebrow else 'N/A'} vs rendered {modules_in_grid}")

    # 6. Check WhatsApp links
    wa_links = [l for l in links if 'api.whatsapp.com' in l or 'wa.me' in l]
    print(f"WhatsApp links verified: {len(wa_links)} instances")
