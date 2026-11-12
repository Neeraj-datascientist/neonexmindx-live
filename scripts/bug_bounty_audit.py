import os
import glob
import re
import urllib.parse

print("=== FULL-SCOPE WEBSITE BUG BOUNTY & INCONSISTENCY AUDIT ===")

root_dir = 'deployment_NeoNex'
html_files = glob.glob(f'{root_dir}/**/*.html', recursive=True)
print(f"Total HTML files under inspection: {len(html_files)}")

issues = {
    'broken_internal_links': [],
    'canonical_mismatches': [],
    'empty_or_missing_alts': [],
    'empty_hrefs': [],
    'unsecured_http_links': [],
    'missing_titles': [],
    'missing_descriptions': [],
    'broken_form_actions': [],
    'missing_gtm': [],
    'missing_viewport': [],
    'broken_local_assets': [],
    'placeholder_artifacts': []
}

canonical_urls = set()
with open(f'{root_dir}/sitemap.xml', 'r', encoding='utf-8') as f:
    canonical_urls = set(re.findall(r'<loc>(.*?)</loc>', f.read()))

for file_path in html_files:
    # Skip temporary test scripts or build remnants if any
    rel_path = os.path.relpath(file_path, root_dir).replace('\\', '/')
    
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Title & Description
    title_match = re.search(r'<title>(.*?)</title>', html, re.I | re.DOTALL)
    if not title_match or not title_match.group(1).strip():
        issues['missing_titles'].append(rel_path)
        
    desc_match = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']*)["\']', html, re.I) or \
                 re.search(r'<meta[^>]+content=["\']([^"\']*)["\'][^>]+name=["\']description["\']', html, re.I)
    if not desc_match or not desc_match.group(1).strip():
        issues['missing_descriptions'].append(rel_path)

    # 2. Viewport & GTM
    if '<meta name="viewport"' not in html.lower() and '<meta content="width=' not in html.lower():
        issues['missing_viewport'].append(rel_path)
    if 'GTM-PG57R85H' not in html and 'privacy-policy' not in rel_path and 'terms' not in rel_path and 'refund' not in rel_path and 'placement-assistance' not in rel_path:
        issues['missing_gtm'].append(rel_path)

    # 3. Canonical validation
    canon_match = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']*)["\']', html, re.I) or \
                  re.search(r'<link[^>]+href=["\']([^"\']*)["\'][^>]+rel=["\']canonical["\']', html, re.I)
    if canon_match:
        canon_val = canon_match.group(1).strip()
        if canon_val.startswith('https://neonexmindx.com') and not canon_val.endswith('/') and not '.' in canon_val.split('/')[-1]:
            issues['canonical_mismatches'].append((rel_path, canon_val))

    # 4. Image Alts & Assets
    img_tags = re.findall(r'<img[^>]*>', html)
    for img in img_tags:
        src_match = re.search(r'src=["\']([^"\']+)["\']', img)
        alt_match = re.search(r'alt=["\']([^"\']*)["\']', img)
        if not alt_match or not alt_match.group(1).strip():
            # Check if decorative or tracking
            if 'facebook.com' not in img and 'data:image' not in img:
                issues['empty_or_missing_alts'].append((rel_path, img[:100]))
                
        if src_match:
            src = src_match.group(1)
            if src.startswith('/') and not src.startswith('//') and not src.startswith('/#'):
                # Verify local file exists
                asset_local = os.path.join(root_dir, src.lstrip('/'))
                if not os.path.exists(asset_local) and not 'favicon' in src and not 'gtm' in src:
                    issues['broken_local_assets'].append((rel_path, src))

    # 5. Links & Hrefs
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', html)
    for h in hrefs:
        h_clean = h.strip()
        if h_clean == '#' or h_clean == '':
            issues['empty_hrefs'].append(rel_path)
        elif h_clean.startswith('http://') and 'localhost' not in h_clean and 'schema.org' not in h_clean and 'w3.org' not in h_clean:
            issues['unsecured_http_links'].append((rel_path, h_clean))
        elif h_clean.startswith('/courses/') and not h_clean.endswith('/') and not '.' in h_clean.split('/')[-1]:
            issues['broken_internal_links'].append((rel_path, h_clean))

    # 6. Placeholders
    for ph in ['TODO', 'FIXME', 'lorem ipsum', 'test@test.com', 'sample text', 'placeholder text']:
        if ph in html.lower():
            issues['placeholder_artifacts'].append((rel_path, ph))

print("\n=== AUDIT RESULTS SUMMARY ===")
for k, v in issues.items():
    print(f"[{k}]: {len(v)} occurrences")
    if len(v) > 0 and len(v) <= 8:
        for item in v:
            print(f"   -> {item}")
    elif len(v) > 8:
        for item in v[:5]:
            print(f"   -> {item}")
        print(f"   ... and {len(v)-5} more.")

