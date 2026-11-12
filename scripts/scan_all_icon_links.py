import glob
import re
import urllib.parse

files = glob.glob('deployment_NeoNex/**/*.html', recursive=True)

# We want to find all <a> tags that contain an icon (svg, img, i) or have classes/attributes suggesting an icon or social profile
# e.g., linkedin, whatsapp, youtube, instagram, facebook, github, twitter, x.com

icon_links = []

for f in files:
    txt = open(f, 'r', encoding='utf-8', errors='ignore').read()
    
    # regex to find <a ...>...</a>
    for m in re.finditer(r'<a\b([^>]*)>(.*?)</a>', txt, re.DOTALL | re.IGNORECASE):
        attrs = m.group(1)
        body = m.group(2)
        
        # Check if it has an icon or is a social link
        has_svg = '<svg' in body
        has_img = '<img' in body
        href_match = re.search(r'href=[\"\']([^\"\']*)[\"\']', attrs)
        href = href_match.group(1).strip() if href_match else ''
        
        aria_label = re.search(r'aria-label=[\"\']([^\"\']*)[\"\']', attrs)
        label = aria_label.group(1) if aria_label else ''
        
        is_social = any(s in href.lower() for s in ['linkedin.com', 'wa.me', 'whatsapp', 'youtube.com', 'instagram.com', 'facebook.com', 'twitter.com', 'x.com', 'github.com'])
        
        if has_svg or is_social:
            icon_links.append({
                'file': f,
                'href': href,
                'label': label,
                'snippet': m.group(0)[:150].replace('\n', ' ')
            })

print(f"Total icon / social links found sitewide: {len(icon_links)}")

# Group by unique href
unique_hrefs = {}
for item in icon_links:
    h = item['href']
    unique_hrefs.setdefault(h, []).append(item['file'])

print(f"\nUnique icon link URLs ({len(unique_hrefs)}):")
for h, f_list in sorted(unique_hrefs.items(), key=lambda x: len(x[1]), reverse=True):
    print(f"  [{len(f_list)} occurrences] {h}")
