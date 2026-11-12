import re

files = [
    r'deployment_NeoNex\courses\sql-course\index.html',
    r'deployment_NeoNex\courses\python-programming-course\index.html',
    r'deployment_NeoNex\courses\excel-power-bi-tableau-course\index.html',
    r'deployment_NeoNex\courses\machine-learning-course\index.html'
]

h1_mappings = {
    'sql-course': 'Live Online SQL Course in India with Real Database Projects',
    'python-programming-course': 'Live Online Python Course for Beginners in India',
    'excel-power-bi-tableau-course': 'Excel, Power BI & Tableau Course Online in India',
    'machine-learning-course': 'Machine Learning Course Online in India with Python'
}

for fp in files:
    with open(fp, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Canonical trailing slash
    html = re.sub(r'rel=["\']canonical["\'] href=["\']https://neonexmindx\.com/courses/([^"\'/]+)["\']', r'rel="canonical" href="https://neonexmindx.com/courses/\1/"', html)
    html = re.sub(r'href=["\']https://neonexmindx\.com/courses/([^"\'/]+)["\'] rel=["\']canonical["\']', r'href="https://neonexmindx.com/courses/\1/" rel="canonical"', html)

    # 2. Tracking pixel alt
    html = html.replace('alt="" src="https://www.facebook.com/tr?id=1698036971288322', 'alt="Facebook Pixel" src="https://www.facebook.com/tr?id=1698036971288322')

    # 3. Keyword H1 check and injection if not present
    slug = None
    for k in h1_mappings:
        if k in fp:
            slug = k
            break
    
    if '<h1' not in html and slug:
        h1_text = h1_mappings[slug]
        # Replace <span class="eyebrow"> or similar with <h1 class="eyebrow">
        if '<span class="eyebrow">' in html:
            html = html.replace('<span class="eyebrow">', f'<h1 class="eyebrow" style="font-size:inherit;font-weight:inherit;margin:0;display:inline-block;">{h1_text}</h1><!-- ', 1)
            html = html.replace('</span>', ' -->', 1)
        elif '<div class="hero-title"' in html:
            html = html.replace('<div class="hero-title"', f'<h1 class="eyebrow" style="font-size:0.9rem;text-transform:uppercase;letter-spacing:1.5px;color:var(--brand-primary,#0056D2);margin-bottom:8px;font-weight:700;">{h1_text}</h1>\n<div class="hero-title"', 1)

    print(f"{fp}: has <h1: {'<h1' in html}")

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(html)
print("Calibration complete.")

