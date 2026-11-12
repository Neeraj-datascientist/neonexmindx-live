import json

data = json.load(open('deployment_NeoNex/data/blogs.json', 'r', encoding='utf-8'))
print("=== POSTS IN BLOGS.JSON ===")
for p in data.get('posts', []):
    print(f"Slug: {p['slug']} | Author: {p.get('author')}")

print("\n=== AUTHORS IN BLOGS.JSON ===")
for a in data.get('authors', []):
    print(f"ID: {a.get('id')} | Name: {a.get('name')} | Avatar: {a.get('avatar')} | LinkedIn: {a.get('linkedin')}")
