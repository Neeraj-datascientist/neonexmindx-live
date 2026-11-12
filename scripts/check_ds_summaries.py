import re

html = open('deployment_NeoNex/courses/data-science-course/index.html', 'r', encoding='utf-8').read()

curriculum_section = re.search(r'<section class="section" id="curriculum">.*?</section>', html, re.DOTALL)
if curriculum_section:
    c_html = curriculum_section.group(0)
    # find module titles or summary titles
    titles = re.findall(r'<summary[^>]*>.*?</summary>', c_html, re.DOTALL)
    print(f"Summary elements ({len(titles)}):")
    for t in titles:
        clean_t = re.sub(r'<[^>]+>', ' ', t)
        clean_t = ' '.join(clean_t.split())
        print("  -", clean_t)

