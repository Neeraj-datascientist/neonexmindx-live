import json
import os
import re

base_dir = r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex"
template_path = os.path.join(base_dir, "blog-post.html")
blogs_json_path = os.path.join(base_dir, "data", "blogs.json")

with open(template_path, "r", encoding="utf-8") as f:
    template = f.read()

with open(blogs_json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

posts = data.get("posts", [])

for post in posts:
    slug = post.get("slug")
    title = post.get("title")
    excerpt = post.get("excerpt", "")
    author = post.get("author", "NeoNeX MindX Editorial Team")
    date = post.get("date", "2026-11-06")
    category = post.get("category", "Technology")
    image = post.get("featured_image", "/assets/images/blog/default.webp")
    canonical_url = f"https://neonexmindx.com/blog/{slug}/"
    
    html = template
    # Replace title
    html = re.sub(r'<title>.*?</title>', f'<title>{title} | NeoNeX MindX Blog</title>', html, flags=re.S)
    
    # Replace meta description
    html = re.sub(r'<meta\s+name=["\']description["\'][^>]*content=["\'][^"\']*["\']', 
                  f'<meta name="description" content="{excerpt}"', html, flags=re.I)
                  
    # Replace canonical tag
    html = re.sub(r'<link\s+rel=["\']canonical["\'][^>]*href=["\'][^"\']*["\'][^>]*>', 
                  f'<link rel="canonical" id="canonical-url" href="{canonical_url}" />', html, flags=re.I)
                  
    # Replace OpenGraph
    html = re.sub(r'<meta\s+property=["\']og:title["\'][^>]*content=["\'][^"\']*["\']', 
                  f'<meta property="og:title" content="{title} | NeoNeX MindX"', html, flags=re.I)
    html = re.sub(r'<meta\s+property=["\']og:description["\'][^>]*content=["\'][^"\']*["\']', 
                  f'<meta property="og:description" content="{excerpt}"', html, flags=re.I)
    html = re.sub(r'<meta\s+property=["\']og:url["\'][^>]*content=["\'][^"\']*["\']', 
                  f'<meta property="og:url" content="{canonical_url}"', html, flags=re.I)
                  
    # Replace pre-rendered H1 title
    html = html.replace('id="post-title">Loading Article...</h1>', f'id="post-title">{title}</h1>')
    
    out_dir = os.path.join(base_dir, "blog", slug)
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "index.html")
    with open(out_file, "w", encoding="utf-8") as out_fp:
        out_fp.write(html)
        
print("Updated all static blog index.html files with trailing slashes.")
