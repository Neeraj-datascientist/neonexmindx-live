import re

ds_html = open('deployment_NeoNex/courses/data-science-course/index.html', 'r', encoding='utf-8').read()

# Check what syllabus it links to
links = re.findall(r'href=[\"\'][^\"\']*syllabus[^\"\']*[\"\']', ds_html)
print("DS Course syllabus links:", links)

# Check titles and headings
h1 = re.search(r'<h1.*?>(.*?)</h1>', ds_html, re.DOTALL)
print("H1:", h1.group(1).strip() if h1 else 'None')

# Check AI mentions in DS course
ai_mentions = len(re.findall(r'\bAI\b|Artificial Intelligence|Deep Learning|NLP|Computer Vision|LLM', ds_html))
print(f"Total AI/DL/NLP/CV mentions in data-science-course: {ai_mentions}")
