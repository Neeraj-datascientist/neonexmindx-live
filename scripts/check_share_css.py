import glob
import re

files = glob.glob('deployment_NeoNex/blog/**/*.html', recursive=True) + ['deployment_NeoNex/blog-post.html', 'deployment_NeoNex/blogs/index.html']
for f in files:
    txt = open(f, 'r', encoding='utf-8').read()
    # check share-btn or share-tray styles
    styles = re.findall(r'\.share-[a-zA-Z0-9_\-]+\s*\{[^}]*\}', txt)
    if styles:
        print(f"=== {f} ===")
        for s in styles:
            print(" ", s)
