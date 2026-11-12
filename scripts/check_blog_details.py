import re

path = 'deployment_NeoNex/blog-post.html'
txt = open(path, 'r', encoding='utf-8').read()

print("Checking blog-post.html icons and share buttons...")
# Find social icons or footer icons or author card icons
matches = re.findall(r'<svg[^>]*>.*?</svg>', txt, re.DOTALL)
print(f"Total SVGs found in blog-post.html: {len(matches)}")

# Check author card in JS template
author_part = re.search(r'authorObj\.linkedin.*?</div>', txt, re.DOTALL)
if author_part:
    print("Author part snippet:")
    print(author_part.group(0)[:300])

# Check header / nav WhatsApp
header_wa = re.findall(r'href=[\"\'][^\"\']*wa\.me[^\"\']*[\"\']', txt)
print("Header WhatsApp links:", header_wa)

