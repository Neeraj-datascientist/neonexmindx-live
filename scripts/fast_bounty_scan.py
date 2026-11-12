import os
import re

print("=== FAST BUG BOUNTY SCAN OF 28 PRODUCTION CANONICAL ROUTES ===")

canonical_routes = [
    'index.html',
    'about-us/index.html',
    'trainers/index.html',
    'contact-us/index.html',
    'courses/data-analytics-course/index.html',
    'courses/data-science-course/index.html',
    'courses/ai-ml-engineering-course/index.html',
    'courses/data-engineering-course/index.html',
    'courses/business-analytics-course/index.html',
    'courses/generative-ai-engineering-course/index.html',
    'courses/excel-power-bi-tableau-course/index.html',
    'courses/python-programming-course/index.html',
    'courses/sql-course/index.html',
    'courses/machine-learning-course/index.html',
    'blogs/index.html',
    'blog/data-analytics-portfolio-how-to-build-one-in-2026/index.html',
    'blog/complete-roadmap-to-become-data-scientist-2026/index.html',
    'blog/top-high-paying-data-analytics-tools-2026/index.html',
    'blog/how-neonex-mindx-helps-non-tech-learners-transition/index.html',
    'blog/modern-data-engineering-pipelines-kafka-spark-cloud/index.html',
    'blog/machine-learning-vs-deep-learning-differences-guide/index.html',
    'blog/generative-ai-llm-enterprise-deployment-strategies/index.html',
    'blog/2026-breakthroughs-in-ai-agents-llms/index.html',
    'blog/distributed-data-pipelines-with-apache-spark-iceberg/index.html',
    'privacy-policy/index.html',
    'terms-and-conditions/index.html',
    'refund-and-cancellation-policy/index.html',
    'placement-assistance-disclaimer/index.html'
]

root = 'deployment_NeoNex'
audit_results = []

for rel_path in canonical_routes:
    full_path = os.path.join(root, rel_path)
    if not os.path.exists(full_path):
        audit_results.append((rel_path, "FILE_MISSING", "Critical: file does not exist on disk"))
        continue
        
    with open(full_path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Check 1: Missing Title
    title = re.search(r'<title>(.*?)</title>', html, re.I | re.DOTALL)
    if not title or not title.group(1).strip():
        audit_results.append((rel_path, "MISSING_TITLE", "Title tag is missing or empty"))
        
    # Check 2: Missing Meta Description
    desc = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']*)["\']', html, re.I) or \
           re.search(r'<meta[^>]+content=["\']([^"\']*)["\'][^>]+name=["\']description["\']', html, re.I)
    if not desc or not desc.group(1).strip():
        audit_results.append((rel_path, "MISSING_META_DESC", "Meta description is missing or empty"))
        
    # Check 3: Canonical Trailing Slash & Presence
    canon = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']*)["\']', html, re.I) or \
            re.search(r'<link[^>]+href=["\']([^"\']*)["\'][^>]+rel=["\']canonical["\']', html, re.I)
    if not canon:
        audit_results.append((rel_path, "MISSING_CANONICAL", "No canonical tag found"))
    else:
        c_url = canon.group(1).strip()
        if not c_url.endswith('/') and not '.' in c_url.split('/')[-1]:
            audit_results.append((rel_path, "CANONICAL_TRAILING_SLASH", f"Canonical missing trailing slash: {c_url}"))

    # Check 4: Missing Alt attributes on <img>
    imgs = re.findall(r'<img[^>]*>', html)
    for img in imgs:
        if 'alt=""' in img and 'data:image' not in img and 'facebook.com' not in img:
            audit_results.append((rel_path, "EMPTY_ALT_TAG", img[:80]))
        elif 'alt=' not in img:
            audit_results.append((rel_path, "MISSING_ALT_TAG", img[:80]))
            
    # Check 5: Non-trailing slash internal course links
    course_hrefs = re.findall(r'href=["\'](/courses/[^"\'\s#\?]+)["\']', html)
    for ch in set(course_hrefs):
        if not ch.endswith('/') and not '.' in ch:
            audit_results.append((rel_path, "INTERNAL_REDIRECT_LINK", f"Internal link without trailing slash: {ch}"))

    # Check 6: Unsecured HTTP links
    http_links = re.findall(r'href=["\'](http://[^"\'\s]+)["\']', html)
    for hl in set(http_links):
        if 'localhost' not in hl and 'schema.org' not in hl and 'w3.org' not in hl:
            audit_results.append((rel_path, "INSECURE_HTTP_LINK", f"Insecure HTTP link found: {hl}"))

    # Check 7: Broken local asset paths (src="/...")
    srcs = re.findall(r'src=["\'](/[^"\'\s\?#]+)["\']', html)
    for s in set(srcs):
        if not s.startswith('//') and not s.startswith('/api/') and not 'gtm' in s and not 'facebook' in s:
            local_file = os.path.join(root, s.lstrip('/'))
            if not os.path.exists(local_file) and not s.endswith(('.png', '.ico', '.jpg', '.webp')):
                audit_results.append((rel_path, "BROKEN_LOCAL_ASSET", f"Asset does not exist: {s}"))

print(f"Audit completed across all {len(canonical_routes)} canonical production endpoints.")
print(f"Total issues flagged: {len(audit_results)}")

for path, category, detail in audit_results:
    print(f"[{category}] in {path}: {detail}")
