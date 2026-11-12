with open('deployment_NeoNex/blog-post.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('class="share-btn share-in"')
print(html[pos-50:pos+250])
