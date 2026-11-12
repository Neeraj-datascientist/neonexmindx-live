import os
import glob
import re

root = 'deployment_NeoNex'
blogs = glob.glob(f'{root}/blog/*/index.html')
print(f"Total blog endpoints found: {len(blogs)}")

# Clean canonical in blogs/index.html
blogs_hub = f'{root}/blogs/index.html'
if os.path.exists(blogs_hub):
    with open(blogs_hub, 'r', encoding='utf-8') as f:
        html = f.read()
    html = re.sub(r'rel="canonical" href="https://neonexmindx\.com/blogs"', 'rel="canonical" href="https://neonexmindx.com/blogs/"', html)
    html = re.sub(r'href="https://neonexmindx\.com/blogs" rel="canonical"', 'href="https://neonexmindx.com/blogs/" rel="canonical"', html)
    with open(blogs_hub, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Fixed blogs/index.html canonical trailing slash.")

for b in blogs:
    with open(b, 'r', encoding='utf-8') as f:
        html = f.read()

    # Extract H1 or article title
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL)
    article_title = "NeoNeX MindX Tech Blog"
    if h1:
        article_title = " ".join(re.sub(r'<[^>]+>', ' ', h1.group(1)).split())
    
    slug = os.path.basename(os.path.dirname(b))
    title_text = f"{article_title} | NeoNeX MindX"
    desc_text = f"Explore deep-dive technical insights on {article_title.lower()} with practical code architectures and production workflows."
    canon_url = f"https://neonexmindx.com/blog/{slug}/"

    changed = False
    if '<title>' not in html:
        head_inject = f'<title>{title_text}</title>\n<meta name="description" content="{desc_text}">\n<link rel="canonical" href="{canon_url}">\n'
        html = html.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n' + head_inject)
        changed = True
    else:
        # Check canonical
        if f'href="{canon_url}"' not in html:
            html = re.sub(r'<link[^>]+rel=["\']canonical["\'][^>]*>', f'<link rel="canonical" href="{canon_url}">', html)
            changed = True

    if changed:
        with open(b, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Injected SEO title and canonical into {b}")

print("All blog post headers fully calibrated.")

