import os
import glob
import re

print("=== FIXING ALL IDENTIFIED BOUNTY INCONSISTENCIES ===")

root = 'deployment_NeoNex'
html_files = glob.glob(f'{root}/**/*.html', recursive=True)

# 1. Fix missing title in distributed-data-pipelines-with-apache-spark-iceberg
iceberg_path = f'{root}/blog/distributed-data-pipelines-with-apache-spark-iceberg/index.html'
if os.path.exists(iceberg_path):
    with open(iceberg_path, 'r', encoding='utf-8') as f:
        html = f.read()
    if '<title>' not in html:
        title_block = '<title>Distributed Data Pipelines with Apache Spark & Iceberg | NeoNex MindX</title>\n<meta name="description" content="Master distributed data engineering pipelines using Apache Spark, Apache Iceberg, ACID transactions, and modern cloud lakehouse architectures in 2026.">\n'
        html = html.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n' + title_block)
        with open(iceberg_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print("Fixed missing title and description in Iceberg blog post.")

# 2. Fix canonical trailing slash in trainers/index.html
trainers_path = f'{root}/trainers/index.html'
if os.path.exists(trainers_path):
    with open(trainers_path, 'r', encoding='utf-8') as f:
        html = f.read()
    html = re.sub(r'rel="canonical" href="https://neonexmindx\.com/trainers"', 'rel="canonical" href="https://neonexmindx.com/trainers/"', html)
    html = re.sub(r'href="https://neonexmindx\.com/trainers" rel="canonical"', 'href="https://neonexmindx.com/trainers/" rel="canonical"', html)
    with open(trainers_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Fixed canonical trailing slash in trainers/index.html.")

# 3. Fix all internal links missing trailing slashes sitewide
career_slugs = [
    'data-analytics-course',
    'data-science-course',
    'ai-ml-course',
    'ai-ml-engineering-course',
    'data-engineering-course',
    'business-analytics-course',
    'generative-ai-engineering-course',
    'python-programming-course',
    'sql-course',
    'excel-power-bi-tableau-course',
    'machine-learning-course'
]

fixed_files = 0
for fp in html_files:
    try:
        with open(fp, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content
        for slug in career_slugs:
            # Match href="/courses/slug" without slash
            new_content = re.sub(f'href=["\']/courses/{slug}["\']', f'href="/courses/{slug}/"', new_content)
            # Match href="https://neonexmindx.com/courses/slug" without slash
            new_content = re.sub(f'href=["\']https://neonexmindx\\.com/courses/{slug}["\']', f'href="https://neonexmindx.com/courses/{slug}/"', new_content)

        # Also fix /about-us, /contact-us, /trainers if missing trailing slash
        new_content = re.sub(r'href=["\']/about-us["\']', 'href="/about-us/"', new_content)
        new_content = re.sub(r'href=["\']/contact-us["\']', 'href="/contact-us/"', new_content)
        new_content = re.sub(r'href=["\']/trainers["\']', 'href="/trainers/"', new_content)
        new_content = re.sub(r'href=["\']/blogs["\']', 'href="/blogs/"', new_content)
        
        if new_content != content:
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(new_content)
            fixed_files += 1
    except Exception as e:
        print(f"Error on {fp}: {e}")

print(f"Fixed internal links with trailing slashes across {fixed_files} HTML files sitewide.")
