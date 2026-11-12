import re

sitemap_path = r"c:\Users\pcnee\Desktop\NeoNeX MindX website\deployment_NeoNex\sitemap.xml"
with open(sitemap_path, "r", encoding="utf-8") as f:
    xml_txt = f.read()

new_short_courses_xml = """
  <!-- Focused Short Courses -->
  <url>
    <loc>https://neonexmindx.com/courses/excel-power-bi-tableau-course/</loc>
    <lastmod>2026-11-12</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.85</priority>
  </url>
  <url>
    <loc>https://neonexmindx.com/courses/python-programming-course/</loc>
    <lastmod>2026-11-12</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.85</priority>
  </url>
  <url>
    <loc>https://neonexmindx.com/courses/sql-course/</loc>
    <lastmod>2026-11-12</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.85</priority>
  </url>
  <url>
    <loc>https://neonexmindx.com/courses/machine-learning-course/</loc>
    <lastmod>2026-11-12</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.85</priority>
  </url>
"""

target = "  <!-- Blog Knowledge Hub -->"
if "courses/excel-power-bi-tableau-course/" not in xml_txt:
    xml_txt = xml_txt.replace(target, new_short_courses_xml.strip() + "\n\n" + target)
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(xml_txt)
    print("Successfully added all 4 short courses to sitemap.xml!")
else:
    print("Already present.")
