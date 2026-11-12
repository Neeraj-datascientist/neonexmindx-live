import re

sitemap_path = 'deployment_NeoNex/sitemap.xml'
content = open(sitemap_path, 'r', encoding='utf-8').read()

new_entry = '''  <url>
    <loc>https://neonexmindx.com/courses/data-science-and-ai-course/</loc>
    <lastmod>2026-11-12</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>'''

if 'https://neonexmindx.com/courses/data-science-and-ai-course/' not in content:
    content = content.replace(
        '  <url>\n    <loc>https://neonexmindx.com/courses/data-science-course/</loc>',
        new_entry + '\n  <url>\n    <loc>https://neonexmindx.com/courses/data-science-course/</loc>'
    )
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added data-science-and-ai-course to sitemap.xml!")
else:
    print("Already in sitemap.xml")
