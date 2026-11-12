import re

path = 'deployment_NeoNex/blog-post.html'
txt = open(path, 'r', encoding='utf-8').read()

# Look for footer
footer = re.search(r'<footer.*?</footer>', txt, re.DOTALL)
if footer:
    print("=== FOOTER ===")
    print(footer.group(0))

# Look for any .social or social-links
socials = re.findall(r'<div[^>]*social[^>]*>.*?</div>', txt, re.DOTALL | re.IGNORECASE)
print(f"=== SOCIAL DIVS ({len(socials)}) ===")
for s in socials:
    print(s)

