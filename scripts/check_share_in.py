with open('deployment_NeoNex/blog-post.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('share-in')
print(html[pos-100:pos+300])
