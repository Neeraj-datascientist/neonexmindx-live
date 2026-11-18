import glob, os, re

html_files = glob.glob('deployment_NeoNex/**/*.html', recursive=True)

broken_links = []

for f in html_files:
    with open(f, 'r', encoding='utf-8', errors='ignore') as fh:
        c = fh.read()
    hrefs = re.findall(r'<a\s+[^>]*href=["\'](.*?)["\']', c, re.I)
    for h in hrefs:
        h_clean = h.strip()
        if not h_clean or h_clean == '#' or h_clean.startswith('javascript:') or '${' in h_clean:
            continue
        if any(h_clean.startswith(proto) for proto in ['http://', 'https://', 'tel:', 'mailto:', '#', 'data:']):
            continue
        # Internal relative or absolute link
        path = h_clean.split('?')[0].split('#')[0]
        if not path:
            continue
        if path.startswith('/'):
            target = os.path.normpath(os.path.join('deployment_NeoNex', path.lstrip('/')))
        else:
            target = os.path.normpath(os.path.join(os.path.dirname(f), path))
        
        # Check if target exists as file or directory with index.html
        exists = (
            os.path.exists(target) or
            os.path.exists(target + '.html') or
            (os.path.isdir(target) and os.path.exists(os.path.join(target, 'index.html'))) or
            os.path.exists(target.rstrip('\\/') + '.html')
        )
        if not exists:
            broken_links.append((f, h_clean, target))

print(f'Actual static broken links: {len(broken_links)}')
for src, link, tgt in broken_links:
    print(f'{src} -> {link}')
