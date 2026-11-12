import glob
import re

files = glob.glob('deployment_NeoNex/blog/*/index.html') + ['deployment_NeoNex/blog-post.html']
for f in files:
    txt = open(f, 'r', encoding='utf-8').read()
    # Find author card
    author_card = re.findall(r'<div class="article-author-card">.*?</div>\s*</div>\s*</div>', txt, re.DOTALL)
    if not author_card:
        author_card = re.findall(r'article-author-card.*?</aside>', txt, re.DOTALL)
    
    print(f"\n=== {f} ===")
    # Find all occurrences of nikhil or neeraj or lakshmi or avatar in static HTML
    for m in re.finditer(r'(trainer-nikhil|trainer-neeraj|mentor-lakshmi|nikhil|neeraj|authorObj)', txt, re.IGNORECASE):
        print("  Snippet:", txt[max(0, m.start()-40):min(len(txt), m.end()+60)].replace('\n', ' '))

