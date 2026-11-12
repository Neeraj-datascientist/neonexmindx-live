import json

data = json.load(open('deployment_NeoNex/data/blogs.json', 'r', encoding='utf-8'))
print("Site config:", data.get('site'))
print(f"Posts count: {len(data.get('posts', []))}")
print(f"Authors count: {len(data.get('authors', []))}")
for a in data.get('authors', []):
    print("Author:", a)

