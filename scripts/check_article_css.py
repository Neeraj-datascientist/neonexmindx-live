import re

b = 'deployment_NeoNex/blog-post.html'
txt = open(b, 'r', encoding='utf-8').read()

# search for article-layout, article-body, side-widget, toc-widget
styles = re.findall(r'((\.article-layout|\.article-body|\.article-sidebar|\.side-widget)[^{]*\{[^}]*\})', txt)
for s in styles:
    print(s[0])

# check media queries
mq = re.findall(r'(@media[^{]*\{.*?\}\s*\})', txt, re.DOTALL)
print(f"Media queries ({len(mq)}):")
for m in mq:
    print(m[:200])

