with open('deployment_NeoNex/blog-post.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# Look for share buttons, social icons, whatsapp, linkedin in blog-post.html
pos_share = html.find('share')
while pos_share != -1:
    print("--- SHARE SNIPPET ---")
    print(html[max(0, pos_share-100):min(len(html), pos_share+300)])
    pos_share = html.find('share', pos_share + 1)
    if pos_share > 30000: break

