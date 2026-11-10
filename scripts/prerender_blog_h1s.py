import json
import os
import re

base_dir = r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex"
blogs_json_path = os.path.join(base_dir, "data", "blogs.json")
with open(blogs_json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

posts = data.get("posts", [])
for p in posts:
    slug = p.get("slug")
    title = p.get("title")
    path = os.path.join(base_dir, "blog", slug, "index.html")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as fp:
            txt = fp.read()
        txt = re.sub(r'<h1[^>]*id=["\']post-title["\'][^>]*>.*?</h1>', f'<h1 id="post-title" class="post-title">{title}</h1>', txt, flags=re.S)
        with open(path, "w", encoding="utf-8") as fp:
            fp.write(txt)
        print(f"Pre-rendered H1 for blog: {slug} -> {title}")

