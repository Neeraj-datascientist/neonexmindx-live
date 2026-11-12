import json
import glob
import re
import os

blogs_data = json.load(open('deployment_NeoNex/data/blogs.json', 'r', encoding='utf-8'))
posts = blogs_data.get('posts', [])
post_by_slug = {p['slug']: p for p in posts}

blog_dirs = glob.glob('deployment_NeoNex/blog/*')
for bdir in blog_dirs:
    idx = os.path.join(bdir, 'index.html')
    if not os.path.isfile(idx):
        continue
    slug = os.path.basename(bdir)
    post = post_by_slug.get(slug)
    if not post:
        print(f"No post found for slug: {slug}")
        continue
    
    txt = open(idx, 'r', encoding='utf-8').read()
    
    title_str = post['title'] + " | NeoNeX MindX"
    desc_str = post.get('excerpt') or f"Explore deep-dive technical insights on {post['title']} with practical code architectures and production workflows at NeoNeX MindX."
    canonical_url = f"https://neonexmindx.com/blog/{slug}/"
    share_title_encoded = re.sub(r'\s+', '%20', post['title'])
    
    # Replace in static pre-rendered HTML before script
    # Replace <title>...</title>
    txt = re.sub(r'<title>.*?</title>', f'<title>{title_str}</title>', txt)
    # Replace meta description
    txt = re.sub(r'<meta\s+name=["\']description["\']\s+content=["\'][^"\']*["\']\s*/?>', f'<meta name="description" content="{desc_str}" />', txt)
    # Replace canonical
    txt = re.sub(r'<link\s+rel=["\']canonical["\']\s+href=["\'][^"\']*["\']\s*/?>', f'<link rel="canonical" href="{canonical_url}" />', txt)
    
    # Replace ${post.title} in static body
    # Specifically in breadcrumbs, H1, etc.
    # Be careful not to replace inside <script>
    parts = txt.split('<script>')
    if len(parts) >= 2:
        static_html = parts[0]
        script_part = '<script>' + '<script>'.join(parts[1:])
        
        static_html = static_html.replace('${post.title}', post['title'])
        static_html = static_html.replace('${shareTitle}', share_title_encoded)
        static_html = static_html.replace('${currentUrl}', canonical_url)
        
        txt = static_html + script_part
    
    with open(idx, 'w', encoding='utf-8') as f:
        f.write(txt)
    print(f"Fixed SEO and static placeholders for: {slug}")
