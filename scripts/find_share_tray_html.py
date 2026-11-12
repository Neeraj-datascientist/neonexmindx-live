with open('deployment_NeoNex/blog-post.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('class="share-tray"')
while pos != -1:
    print("--- SHARE TRAY HTML ---")
    print(html[pos:pos+1200])
    pos = html.find('class="share-tray"', pos + 1)
