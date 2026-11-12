import re

txt = open('deployment_NeoNex/blogs/index.html', 'r', encoding='utf-8').read()
matches = re.findall(r'<svg[^>]*>.*?</svg>', txt, re.DOTALL)
print(f"SVGs in blogs/index.html: {len(matches)}")

# check if there are share buttons or author cards or cards
cards = re.findall(r'<article[^>]*>.*?</article>', txt, re.DOTALL)
print(f"Articles in blogs/index.html: {len(cards)}")

# check search / filter / categories
print("Links in blogs/index.html:")
for l in re.findall(r'href=[\"\'][^\"\']*[\"\']', txt)[:20]:
    print(" ", l)
