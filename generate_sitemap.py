import os
import json
import datetime

def generate_dynamic_sitemap(directory=None):
    if directory is None:
        directory = os.path.dirname(os.path.abspath(__file__))
    
    blogs_path = os.path.join(directory, "data", "blogs.json")
    posts = []
    custom_urls = []
    site_url = "https://neonexmindx.com"

    if os.path.exists(blogs_path):
        try:
            with open(blogs_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                posts = data.get("posts", [])
                custom_urls = data.get("customSitemapUrls", [])
                site_url = data.get("site", {}).get("siteUrl", site_url).rstrip("/")
        except Exception as e:
            print(f"[Sitemap] Error reading blogs.json: {e}")

    today = datetime.date.today().isoformat()

    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '        xmlns:xhtml="http://www.w3.org/1999/xhtml">',
        '',
        '  <!-- Core Pages -->',
        f'  <url>',
        f'    <loc>{site_url}/</loc>',
        f'    <lastmod>{today}</lastmod>',
        f'    <changefreq>daily</changefreq>',
        f'    <priority>1.0</priority>',
        f'  </url>',
        f'  <url>',
        f'    <loc>{site_url}/about-us</loc>',
        f'    <lastmod>{today}</lastmod>',
        f'    <changefreq>monthly</changefreq>',
        f'    <priority>0.8</priority>',
        f'  </url>',
        f'  <url>',
        f'    <loc>{site_url}/trainers</loc>',
        f'    <lastmod>{today}</lastmod>',
        f'    <changefreq>monthly</changefreq>',
        f'    <priority>0.8</priority>',
        f'  </url>',
        f'  <url>',
        f'    <loc>{site_url}/contact-us</loc>',
        f'    <lastmod>{today}</lastmod>',
        f'    <changefreq>monthly</changefreq>',
        f'    <priority>0.8</priority>',
        f'  </url>',
        '',
        '  <!-- Career Programs -->',
        f'  <url>',
        f'    <loc>{site_url}/courses/data-analytics-course</loc>',
        f'    <lastmod>{today}</lastmod>',
        f'    <changefreq>weekly</changefreq>',
        f'    <priority>0.9</priority>',
        f'  </url>',
        f'  <url>',
        f'    <loc>{site_url}/courses/data-science-course</loc>',
        f'    <lastmod>{today}</lastmod>',
        f'    <changefreq>weekly</changefreq>',
        f'    <priority>0.9</priority>',
        f'  </url>',
        f'  <url>',
        f'    <loc>{site_url}/courses/ai-ml-engineering-course</loc>',
        f'    <lastmod>{today}</lastmod>',
        f'    <changefreq>weekly</changefreq>',
        f'    <priority>0.9</priority>',
        f'  </url>',
        f'  <url>',
        f'    <loc>{site_url}/courses/data-engineering-course</loc>',
        f'    <lastmod>{today}</lastmod>',
        f'    <changefreq>weekly</changefreq>',
        f'    <priority>0.9</priority>',
        f'  </url>',
        f'  <url>',
        f'    <loc>{site_url}/courses/business-analytics-course</loc>',
        f'    <lastmod>{today}</lastmod>',
        f'    <changefreq>weekly</changefreq>',
        f'    <priority>0.9</priority>',
        f'  </url>',
        f'  <url>',
        f'    <loc>{site_url}/courses/generative-ai-engineering-course</loc>',
        f'    <lastmod>{today}</lastmod>',
        f'    <changefreq>weekly</changefreq>',
        f'    <priority>0.9</priority>',
        f'  </url>,'
        '',
        '  <!-- Blog Knowledge Hub -->',
        f'  <url>',
        f'    <loc>{site_url}/blogs</loc>',
        f'    <lastmod>{today}</lastmod>',
        f'    <changefreq>daily</changefreq>',
        f'    <priority>0.8</priority>',
        f'  </url>',
        '',
        '  <!-- Dynamically Generated Published Blog Posts -->'
    ]

    seen_slugs = set()
    blog_count = 0
    for post in posts:
        if post.get("status") == "published" and post.get("slug"):
            slug = post.get("slug").strip().strip("/")
            if slug in seen_slugs:
                continue
            seen_slugs.add(slug)
            p_date = post.get("updatedAt") or post.get("publishedAt") or today
            if "T" in str(p_date):
                p_date = str(p_date).split("T")[0]
            xml_lines.extend([
                f'  <url>',
                f'    <loc>{site_url}/blog/{slug}</loc>',
                f'    <lastmod>{p_date}</lastmod>',
                f'    <changefreq>weekly</changefreq>',
                f'    <priority>0.7</priority>',
                f'  </url>'
            ])
            blog_count += 1

    # Custom URLs added via CMS
    if custom_urls:
        xml_lines.append('')
        xml_lines.append('  <!-- Custom Configured Pages -->')
        for cu in custom_urls:
            loc = cu.get("loc", "").strip()
            if not loc:
                continue
            if not loc.startswith("http"):
                loc = f"{site_url}/{loc.lstrip('/')}"
            prio = cu.get("priority", "0.7")
            freq = cu.get("changefreq", "weekly")
            xml_lines.extend([
                f'  <url>',
                f'    <loc>{loc}</loc>',
                f'    <lastmod>{today}</lastmod>',
                f'    <changefreq>{freq}</changefreq>',
                f'    <priority>{prio}</priority>',
                f'  </url>'
            ])

    xml_lines.extend([
        '',
        '  <!-- Legal & Transparency Pages -->',
        f'  <url>',
        f'    <loc>{site_url}/privacy-policy</loc>',
        f'    <lastmod>{today}</lastmod>',
        f'    <changefreq>yearly</changefreq>',
        f'    <priority>0.3</priority>',
        f'  </url>',
        f'  <url>',
        f'    <loc>{site_url}/terms-and-conditions</loc>',
        f'    <lastmod>{today}</lastmod>',
        f'    <changefreq>yearly</changefreq>',
        f'    <priority>0.3</priority>',
        f'  </url>',
        f'  <url>',
        f'    <loc>{site_url}/refund-and-cancellation-policy</loc>',
        f'    <lastmod>{today}</lastmod>',
        f'    <changefreq>yearly</changefreq>',
        f'    <priority>0.3</priority>',
        f'  </url>',
        f'  <url>',
        f'    <loc>{site_url}/placement-assistance-disclaimer</loc>',
        f'    <lastmod>{today}</lastmod>',
        f'    <changefreq>yearly</changefreq>',
        f'    <priority>0.3</priority>',
        f'  </url>',
        '</urlset>',
        ''
    ])

    xml_text = "\n".join(xml_lines)

    # Write to target directory
    sitemap_target = os.path.join(directory, "sitemap.xml")
    with open(sitemap_target, "w", encoding="utf-8") as f:
        f.write(xml_text)

    # Also sync to finalised_deployment backup
    backup_sitemap = os.path.abspath(os.path.join(directory, "..", "finalised_deployment", "sitemap.xml"))
    if os.path.exists(os.path.dirname(backup_sitemap)):
        try:
            with open(backup_sitemap, "w", encoding="utf-8") as f:
                f.write(xml_text)
        except Exception:
            pass

    return xml_text, blog_count

if __name__ == "__main__":
    xml, count = generate_dynamic_sitemap()
    print(f"Generated dynamic sitemap with {count} published blog articles.")
