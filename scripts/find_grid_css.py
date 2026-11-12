import re

b = 'deployment_NeoNex/blog-post.html'
txt = open(b, 'r', encoding='utf-8').read()

m = re.search(r'@media \(max-width:\s*1024px\)\s*\{.*?\}', txt, re.DOTALL)
if m:
    print(m.group(0))

m_art_grid = re.search(r'\.article-grid\s*\{[^}]*\}', txt)
if m_art_grid:
    print(m_art_grid.group(0))

