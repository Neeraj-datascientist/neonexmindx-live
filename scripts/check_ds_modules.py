import re

html = open('deployment_NeoNex/courses/data-science-course/index.html', 'r', encoding='utf-8').read()

curriculum_section = re.search(r'<section class="section" id="curriculum">.*?</section>', html, re.DOTALL)
if curriculum_section:
    c_html = curriculum_section.group(0)
    # find module headers
    headers = re.findall(r'<h[34][^>]*>(.*?)</h[34]>', c_html)
    print(f"Curriculum modules found ({len(headers)}):")
    for h in headers:
        print("  -", h.strip())
